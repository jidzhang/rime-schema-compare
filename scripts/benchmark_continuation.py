#!/usr/bin/env python3
"""连续续打黑盒维度：把语料按连续 N 行组成"段落"，段内逐句打全拼+空格上屏
（模拟真实连续输入），逐句截获上屏文本并按句位统计命中率。

与独立单句轮（benchmark_windows_pinyin.py 的 per_sentence）对比可得续打增益：
  gain = 段内第 pos 句命中率 − 同句独立命中率（同句用行号对齐）。

用法：
  python scripts/benchmark_continuation.py --ime moqi_pinyin \
      --corpus data/corpus/zhihu120.txt --group-size 3 \
      --standalone-json <同语料独立轮的 benchmark_*.json> \
      --out-dir <输出目录>
"""
import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(HERE))

from rime_schema_compare.ms_pinyin_harness import (  # noqa: E402
    WindowsImeSwitcher,
    WindowsPinyinImeHarness,
)
import benchmark_windows_pinyin as bw  # noqa: E402


def _run_pair_mode(args, harness):
    items = []
    for ln in (ROOT / args.corpus if not Path(args.corpus).is_absolute() else Path(args.corpus)).read_text(encoding="utf-8").splitlines():
        parts = ln.split()
        if len(parts) < 4 or len(parts) % 2:
            continue
        segs = [(parts[i], parts[i + 1]) for i in range(0, len(parts), 2)]
        items.append(segs)

    def commit(pinyin, prev_len):
        harness.focus_host()
        harness._open_ime()
        harness._send_ascii_keys(pinyin)
        time.sleep(harness.commit_delay_s)
        harness._press_space()
        text = harness._wait_for_committed_text()
        return text[prev_len:].strip(), len(text)

    rows = []
    t0 = time.perf_counter()
    # pass A: 下文独立输入（无上文基线）
    for ii, segs in enumerate(items):
        harness.reset_host()
        pred, _ = commit(segs[1][1], 0)
        rows.append({"item": ii, "arm": "alone", "seg": 1,
                     "gold": segs[1][0], "input": segs[1][1], "prediction": pred,
                     "exact": pred == segs[1][0]})
    # pass B: 逐段连续续打（上文已上屏）
    for ii, segs in enumerate(items):
        harness.reset_host()
        prev_len = 0
        for si, (gold, pinyin) in enumerate(segs):
            pred, prev_len = commit(pinyin, prev_len)
            rows.append({"item": ii, "arm": "cont", "seg": si,
                         "gold": gold, "input": pinyin, "prediction": pred,
                         "exact": pred == gold})
        if (ii + 1) % 10 == 0:
            print("[CONT] %s items %d/%d" % (args.ime, ii + 1, len(items)), flush=True)

    alone = {r["item"]: r for r in rows if r["arm"] == "alone"}
    cont2 = {r["item"]: r for r in rows if r["arm"] == "cont" and r["seg"] == 1}
    cont3 = {r["item"]: r for r in rows if r["arm"] == "cont" and r["seg"] == 2}
    items_a = [i for i, s in enumerate(items) if len(s) == 2]
    items_b = [i for i, s in enumerate(items) if len(s) == 3]
    flips = [i for i in alone if not alone[i]["exact"]]

    def pct(sel, table):
        sel = [i for i in sel if i in table]
        return round(100.0 * sum(1 for i in sel if table[i]["exact"]) / max(1, len(sel)), 2)

    summary = {
        "ime": args.ime, "corpus": args.corpus, "mode": "pair",
        "items": len(items), "elapsed_s": round(time.perf_counter() - t0, 1),
        "alone_hit_seg2": pct(list(alone), alone),
        "usecaseA_cont_hit_seg2": pct(items_a, cont2),
        "usecaseB_cont_hit_seg2": pct(items_b, cont2),
        "usecaseB_cont_hit_seg3": pct(items_b, cont3),
        "flip_items": len(flips),
        "flip_alone_hit": pct(flips, alone),
        "flip_cont_hit": pct(flips, cont2),
        "seg1_hit_in_cont": round(100.0 * sum(
            1 for r in rows if r["arm"] == "cont" and r["seg"] == 0 and r["exact"]) / len(items), 2),
    }
    return rows, summary


def main(argv=None):
    parser = argparse.ArgumentParser(description="连续续打黑盒维度")
    parser.add_argument("--ime", required=True)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--group-size", type=int, default=3)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--label", default="continuation")
    parser.add_argument("--standalone-json", help="同语料独立轮 JSON，用于续打增益对比")
    parser.add_argument("--mode", choices=["commit", "long", "pair"], default="commit",
                        help="commit=逐句上屏（真实续打）；long=整段一次连续输入、"
                             "结尾一次空格（长组字串，测 gram 组内上下文）")
    args = parser.parse_args(argv)

    if args.mode == "pair":
        prepared = None
    else:
        prepared = bw._prepare_blackbox_corpus((ROOT / args.corpus).resolve(), Path(args.corpus).stem)
    slots = prepared.prepared_vendor if prepared else []
    eval_syn, _ = bw.init_eval_synonyms(ROOT, None)
    profile = bw.IME_PROFILES[args.ime]
    switcher = WindowsImeSwitcher()
    switcher.resolve_profile(args.ime)

    standalone = {}
    if args.standalone_json:
        payload = json.loads(Path(args.standalone_json).read_text(encoding="utf-8"))
        for row in payload.get("per_sentence", []):
            standalone[int(row["index"])] = bool(row.get("exact"))

    harness = WindowsPinyinImeHarness(**bw._harness_kwargs_for_profile(profile, {
        "launch_timeout_s": 10.0, "settle_timeout_s": 3.0,
        "inter_key_delay_s": 0.012, "commit_delay_s": 0.12,
    }))
    harness.start()
    switcher.activate_profile(args.ime, focus_callback=harness.focus_host)
    harness.self_check()

    if args.mode == "pair":
        rows, summary = _run_pair_mode(args, harness)
        out = Path(args.out_dir)
        out.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
        (out / ("cont_%s_%s_%s.json" % (args.ime, args.label, stamp))).write_text(
            json.dumps({"summary": summary, "rows": rows}, ensure_ascii=False, indent=1),
            encoding="utf-8")
        print("[RESULT-CONT] " + json.dumps(summary, ensure_ascii=False), flush=True)
        harness.close()
        return 0

    rows = []
    groups = [slots[i:i + args.group_size] for i in range(0, len(slots), args.group_size)]
    t0 = time.perf_counter()
    for gi, group in enumerate(groups):
        if args.mode == "long":
            harness.reset_host()
            harness.focus_host()
            harness._open_ime()
            joined_input = "".join(slot["input"] for slot in group)
            harness._send_ascii_keys(joined_input)
            time.sleep(harness.commit_delay_s)
            harness._press_space()
            text = harness._wait_for_committed_text().strip()
            pred = text
            gold = "".join(slot["gold"] for slot in group)
            exact = bool(pred) and bw.sentence_exact_match(
                eval_syn.normalize(pred), eval_syn.normalize(gold))
            rows.append({"group": gi, "pos": 0, "index": gi * args.group_size,
                         "gold": gold, "input": joined_input, "prediction": pred,
                         "exact": exact, "standalone_exact": None})
        else:
            harness.reset_host()
            prev_len = 0
            for pos, slot in enumerate(group):
                harness.focus_host()
                harness._open_ime()
                harness._send_ascii_keys(slot["input"])
                time.sleep(harness.commit_delay_s)
                harness._press_space()
                text = harness._wait_for_committed_text()
                pred = text[prev_len:].strip()
                prev_len = len(text)
                gold = slot["gold"]
                exact = bool(pred) and bw.sentence_exact_match(
                    eval_syn.normalize(pred), eval_syn.normalize(gold))
                idx = gi * args.group_size + pos
                rows.append({
                    "group": gi, "pos": pos, "index": idx,
                    "gold": gold, "input": slot["input"], "prediction": pred,
                    "exact": exact,
                    "standalone_exact": standalone.get(idx),
                })
        if (gi + 1) % 10 == 0:
            print("[CONT] %s groups %d/%d" % (args.ime, gi + 1, len(groups)), flush=True)

    by_pos = {}
    for pos in range(args.group_size):
        sel = [r for r in rows if r["pos"] == pos]
        cont = sum(1 for r in sel if r["exact"])
        alone = [r for r in sel if r["standalone_exact"] is not None]
        alone_ok = sum(1 for r in alone if r["standalone_exact"])
        by_pos[pos] = {
            "n": len(sel), "cont_acc": round(100.0 * cont / max(1, len(sel)), 2),
            "alone_n": len(alone),
            "alone_acc": round(100.0 * alone_ok / max(1, len(alone)), 2) if alone else None,
        }
    overall_cont = sum(1 for r in rows if r["exact"])
    summary = {
        "ime": args.ime, "corpus": args.corpus, "group_size": args.group_size,
        "elapsed_s": round(time.perf_counter() - t0, 1),
        "overall_cont_acc": round(100.0 * overall_cont / len(rows), 2),
        "by_position": by_pos,
    }
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (out / ("cont_%s_%s_%s.json" % (args.ime, args.label, stamp))).write_text(
        json.dumps({"summary": summary, "rows": rows}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    print("[RESULT-CONT] " + json.dumps(summary, ensure_ascii=False), flush=True)
    harness.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
