"""Memory probe: RSS growth per (engine dll, vendor) after load + warm decode."""
import json
import sys
from pathlib import Path

sys.path.insert(0, "src")
import psutil

from rime_schema_compare.benchmark_env import prepare_vendor_for_benchmark
from rime_schema_compare.config import VendorConfig
from rime_schema_compare.rime_runner import RimeDistroRunner
from rime_schema_compare.text_pipeline import sentence_to_continuous_pinyin

VENDORS = {
    "mingyuepinyin": VendorConfig("mingyuepinyin", "vendor/mingyuepinyin", "luna_pinyin_simp"),
    "rime_frost": VendorConfig("rime_frost", "vendor/rime-frost", "rime_frost"),
    "mingyuepinyin_with_gram": VendorConfig("mingyuepinyin_with_gram", "vendor/mingyuepinyin_with_gram", "luna_pinyin_simp"),
    "rime_frost_with_gram": VendorConfig("rime_frost_with_gram", "vendor/rime-frost_with_gram", "rime_frost"),
}
from pathlib import Path as _P
ENGINES = {"weasel": str((_P(__file__).resolve().parents[1] / "lib/rime.dll").resolve()), "moqi": str((_P(__file__).resolve().parents[1] / "lib/rime-moqi.dll").resolve())}

probes = []
corpus = Path("D:/work/github/IME/windows-ime-bench/corpus/zhihu120.txt").read_text(encoding="utf-8").splitlines()
sents = [s.strip() for s in corpus if s.strip()][:40]
inputs = [sentence_to_continuous_pinyin(s) for s in sents]
inputs = [i for i in inputs if i]

for ek, dll in ENGINES.items():
    for vk, vc in VENDORS.items():
        proc = psutil.Process()
        base = proc.memory_info().rss
        runner = RimeDistroRunner(_P(dll))
        runner.switch_distro(vc)
        after_load = proc.memory_info().rss
        ok = runner.begin_decode_batch(vc.schema_id)
        decoded = 0
        for inp in inputs:
            r = runner.decode_pinyin_in_batch(inp)
            if r.ok:
                decoded += 1
        runner.close()
        peak = proc.memory_info().rss
        probes.append({
            "engine": ek, "vendor": vk,
            "rss_base_mb": round(base / 1048576, 1),
            "rss_after_load_mb": round(after_load / 1048576, 1),
            "rss_after_decode_mb": round(peak / 1048576, 1),
            "delta_mb": round((peak - base) / 1048576, 1),
            "decoded": decoded,
        })
        print(f"{ek:7s} {vk:26s} rss_base={base/1048576:7.1f} after_load={after_load/1048576:7.1f} "
              f"after_decode={peak/1048576:7.1f} delta={(peak-base)/1048576:7.1f} decoded={decoded}")

Path("artifacts_matrix/memory_probe.json").write_text(
    json.dumps(probes, ensure_ascii=False, indent=2), encoding="utf-8")
print("PROBE_DONE")
