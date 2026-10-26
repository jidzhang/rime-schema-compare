"""Gold-pinyin sidecar: freeze corpus readings + cross-audit against vendor dicts.

Why: runtime pypinyin + word patches only covers audited corpora. New corpora need a
mechanical audit and a frozen pronunciation file that travels with the corpus:

- freeze: <corpus>.pin.tsv  (hanzi_segment<TAB>pinyin)  — benchmark prefers it
- audit : cross-check every segment reading against vendor dict yamls already in
  vendor/ (independent annotations). Unanimous vendor disagreement => ERROR
  candidate; vendor disagreement or OOV polyphone => REVIEW candidate.

CLI:
  python -m rime_schema_compare.gold_pinyin freeze <corpus.txt> [out.tsv]
  python -m rime_schema_compare.gold_pinyin audit  <corpus.txt> <corpus>.pin.tsv
"""

from __future__ import annotations

import io
import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from . import text_pipeline as tp
from pypinyin import lazy_pinyin

# 常见多音字（审读重点；OOV 词含这些字时升 REVIEW）
_POLYPHONE_STR = (
    "重降得地长行还都着落系为教难斗提干处传参种发结解当相把省觉差石率数弹调号假卡盛称乘仇单"
    "薄剥泊藏曾禅昌偿畜创答大逮度恶否夫服杆冈格骨观过汗好呵合和横华晃会稽饥几济家价间见将劲"
    "卷慨看亢科可空苦夸狂况拉累离里俩练量料劣裂笼隆论罗脉曼猫蒙眯密缪模磨摩哪囊挠内您宁弄女"
    "趴磅剖仆铺朴栖奇乞起强悄翘切亲区曲全拳让若撒塞散丧扫色僧纱厦稍勺蛇舍审失什氏熟属说宿缩"
    "所塌台太提挑帖同吐屯托驼挖湾丸王微委巫五勿西藏洗细匣纤鲜相销削芯行省虚续轩咽燕要钥一遗"
    "夷以已椅义音殷应影庸拥涌尤犹有余与宇语约晕载灶造择增扎乍粘涨朝赵浙贞症挣只芝吱织指制质"
    "种转幢作坐"
)
POLYPHONE_CHARS = set(_POLYPHONE_STR)

# 每家 vendor 的主词库（全拼、纯拼音码，可作独立注音源）
VENDOR_DICTS = {
    "rime_ice": ["vendor/rime-ice/cn_dicts/8105.dict.yaml",
                 "vendor/rime-ice/cn_dicts/base.dict.yaml",
                 "vendor/rime-ice/cn_dicts/ext.dict.yaml",
                 "vendor/rime-ice/cn_dicts/tencent.dict.yaml"],
    "rime_frost": ["vendor/rime-frost/cn_dicts/8105.dict.yaml",
                   "vendor/rime-frost/cn_dicts/base.dict.yaml",
                   "vendor/rime-frost/cn_dicts/ext.dict.yaml",
                   "vendor/rime-frost/cn_dicts/tencent.dict.yaml"],
    "oh_my_rime": ["vendor/oh-my-rime/dicts/rime_mint.base.dict.yaml",
                   "vendor/oh-my-rime/dicts/rime_mint.chars.dict.yaml",
                   "vendor/oh-my-rime/dicts/rime_mint.ext.dict.yaml"],
}

_NON_AZ = re.compile(r"[^a-z]")


def normalize_syllables(code: str) -> str:
    """dict 码列 -> 规范化音节串（小写、去调、ü→v、只留 a-z，空格分隔）。"""
    s = unicodedata.normalize("NFD", code.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.replace("ü", "v")
    syls = [_NON_AZ.sub("", part) for part in s.split()]
    return " ".join(p for p in syls if p)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_vendor_vocab() -> Dict[str, Dict[str, set]]:
    """word -> {vendor_key: {readings}}（音节串集合，多音词可有多个读音）。"""
    root = _repo_root()
    vocab: Dict[str, Dict[str, set]] = {}
    for vendor, rels in VENDOR_DICTS.items():
        for rel in rels:
            p = root / rel
            if not p.is_file():
                continue
            in_table = False
            for line in io.open(p, encoding="utf-8", errors="ignore"):
                s = line.strip()
                if not in_table:
                    if s == "...":
                        in_table = True
                    continue
                if not s or s.startswith("#"):
                    continue
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 2:
                    continue
                word = parts[0].strip()
                code = parts[1].strip()
                if not word or not code or not re.fullmatch(r"[\u4e00-\u9fff]+", word):
                    continue
                reading = normalize_syllables(code)
                if not reading or len(reading.split()) != len(word):
                    continue
                vocab.setdefault(word, {}).setdefault(vendor, set()).add(reading)
    return vocab


def longest_match_tokenize(hz: str, vocab: Dict[str, Dict[str, set]], max_len: int = 8) -> List[str]:
    out: List[str] = []
    i = 0
    while i < len(hz):
        hit = ""
        for l in range(min(max_len, len(hz) - i), 1, -1):
            w = hz[i:i + l]
            if w in vocab:
                hit = w
                break
        if hit:
            out.append(hit)
            i += len(hit)
        else:
            out.append(hz[i])
            i += 1
    return out


def iter_segments(corpus_path: Path) -> List[str]:
    """与 benchmark 相同的切分/过滤，返回参评的纯汉字段。"""
    text = io.open(corpus_path, encoding="utf-8").read()
    segs: List[str] = []
    for seg in tp.split_sentences(text):
        if not tp.is_pure_hanzi_segment(seg):
            continue
        hz = tp.extract_hanzi(seg)
        if len(hz) >= tp.MIN_EVAL_HANZI_CHARS:
            segs.append(hz)
    return segs


def freeze(corpus_path: Path, out_path: Path) -> int:
    segs = iter_segments(corpus_path)
    seen = set()
    n = 0
    with io.open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("# gold pinyin sidecar (frozen; audit with gold_pinyin audit)\n")
        for hz in segs:
            if hz in seen:
                continue
            seen.add(hz)
            f.write(f"{hz}\t{tp.sentence_to_continuous_pinyin(hz)}\n")
            n += 1
    print(f"froze {n} segments -> {out_path}")
    return n


def audit(corpus_path: Path, tsv_path: Path) -> int:
    gold: Dict[str, str] = {}
    for line in io.open(tsv_path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        hz, py = line.rstrip("\n").split("\t")
        gold[hz] = py
    vocab = load_vendor_vocab()
    conv_diag: List[str] = []
    reviews: List[str] = []
    sidecar_bad: List[str] = []
    unresolved: List[str] = []
    converter_errors = 0
    for hz, py in gold.items():
        syls = lazy_pinyin(hz, errors="ignore")
        if len(syls) != len(hz):
            reviews.append(f"[REVIEW] {hz}: lazy_pinyin 长度异常 {syls}")
            continue
        pos = 0
        conv_parts: List[str] = []
        fixed_parts: List[str] = []
        for tok in longest_match_tokenize(hz, vocab):
            span_py = [normalize_syllables(s) for s in syls[pos:pos + len(tok)]]
            mine = " ".join(span_py)
            conv_parts.append("".join(span_py))
            vend = vocab.get(tok)
            if vend is None:
                if any(c in POLYPHONE_CHARS for c in tok):
                    reviews.append(f"[REVIEW] {hz}: OOV 含多音字 '{tok}' -> {py}")
                fixed_parts.append("".join(span_py))
            else:
                readings = {r for rs in vend.values() for r in rs}
                if mine not in readings:
                    if len(readings) == 1:
                        conv_diag.append(f"[ERROR] {hz}: '{tok}' pypinyin={mine} 词库一致={sorted(readings)}")
                        converter_errors += 1
                        fixed_parts.append(readings.pop().replace(" ", ""))
                    else:
                        reviews.append(f"[REVIEW] {hz}: '{tok}' pypinyin={mine} 词库分歧={sorted(readings)}")
                        fixed_parts.append("".join(span_py))
                else:
                    fixed_parts.append("".join(span_py))
            pos += len(tok)
        conv_str = "".join(conv_parts)
        fixed_str = "".join(fixed_parts)
        if py != conv_str and py != fixed_str:
            sidecar_bad.append(f"[SIDECAR-BAD] {hz}: sidecar={py} 应为 {conv_str} 或修正 {fixed_str}")
        elif conv_str != fixed_str and py == conv_str:
            # 转换器有错且 sidecar 未采纳修正 → 未决
            unresolved.append(f"[UNRESOLVED] {hz}: sidecar 保留了转换器错误值 {py}（应为 {fixed_str}）")
    for m in conv_diag:
        print(m)
    for m in reviews:
        print(m)
    for m in sidecar_bad:
        print(m)
    for m in unresolved:
        print(m)
    resolved = converter_errors - len(unresolved)
    print(
        f"== audit done: {converter_errors} converter-ERROR（{resolved} 已由 sidecar 修正 / "
        f"{len(unresolved)} 未决）/ {len(reviews)} REVIEW / {len(sidecar_bad)} SIDECAR-BAD / {len(gold)} segments"
    )
    return 1 if (unresolved or sidecar_bad) else 0


def main(argv: List[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, corpus = argv[1], Path(argv[2])
    if cmd == "freeze":
        out = Path(argv[3]) if len(argv) > 3 else corpus.with_suffix("").with_name(corpus.stem + ".pin.tsv")
        freeze(corpus, out)
        return 0
    if cmd == "audit":
        return audit(corpus, Path(argv[3]))
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
