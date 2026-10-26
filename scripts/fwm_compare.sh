#!/usr/bin/env bash
# Product-level A/B: weasel+frost / weasel+luna / moqi(product, default=frost)
# One-off driver, mirrors run.bat :bench per arm, with resets + timestamps.
set -u
ROOT="D:/work/github/IME/windows-ime-bench"
ENG="$ROOT/engine/rime-schema-compare"
IMES_JSON="$ROOT/imes.json"
RIME_DIR="$APPDATA/Rime"
BAK="$APPDATA/Rime.bak_luna_arm"
LOG="$ROOT/results/run/fwm_run_log.txt"
DEPLOY_PY='
import sys; sys.path.insert(0,"src")
from rime_schema_compare.call_librime import RimeDllWrapper
w=RimeDllWrapper(dll_path=r"C:\Program Files\Rime\weasel-0.17.4\rime.dll")
w.initialize(app_name="rime.weasel", shared_data_dir=r"C:\Program Files\Rime\weasel-0.17.4\data", user_data_dir=r"C:\Users\TEST\AppData\Roaming\Rime")
w.finalize()
'

log() { echo "[$(date '+%F %T')] $*" >> "$LOG"; }

bench() { # ime label corpus outdir minhanzi
  local ime=$1 label=$2 corpus=$3 outdir=$4 minh=${5:-5}
  (cd "$ENG" && python -c "
import sys,json; sys.path.insert(0,'src')
from rime_schema_compare.ms_pinyin_harness import WindowsImeSwitcher
payload=json.load(open(r'$IMES_JSON',encoding='utf-8'))
WindowsImeSwitcher(extra_profiles=payload).activate_profile('$ime')
" >/dev/null 2>&1)
  (cd "$ENG" && python scripts/benchmark_windows_pinyin.py --ime "$ime" --corpus "data/corpus/$corpus" \
    --min-hanzi "$minh" --extra-imes "$IMES_JSON" --out-dir "$outdir" 2>&1 | grep -E "RESULT|ABORT|SKIP|Error" | tail -2)
}

reset_weasel_userdb() {
  taskkill //IM WeaselServer.exe //F >/dev/null 2>&1
  sleep 1
  find "$RIME_DIR" -maxdepth 1 -name "*.userdb" -exec rm -rf {} + 2>/dev/null
  log "weasel userdb wiped: $(find "$RIME_DIR" -maxdepth 1 -name '*.userdb' | wc -l) left"
}

mkdir -p "$ROOT/results/run"
ping -n 1 -w 2000 223.5.5.5 >/dev/null 2>&1 && NET=True || NET=False
log "==== FWM compare start, network=$NET"

# ---- arm 1: weasel + rime_frost ----
log "arm1 weasel_frost begin"
reset_weasel_userdb
bench weasel_rime weasel_frost zhihu120.txt "$ROOT/results/run/weasel_frost/sentences" 5
bench weasel_rime weasel_frost words234.txt "$ROOT/results/run/weasel_frost/words" 2
log "arm1 weasel_frost done"

# ---- arm 2: weasel + luna_pinyin_simp (default) ----
log "arm2 weasel_luna begin"
taskkill //IM WeaselServer.exe //F >/dev/null 2>&1
sleep 1
rm -rf "$RIME_DIR"
cp -r "$BAK" "$RIME_DIR"
find "$RIME_DIR" -maxdepth 1 -name "*.userdb" -exec rm -rf {} + 2>/dev/null
rm -rf "$RIME_DIR/build"
(cd "$ENG" && python -c "$DEPLOY_PY")
ls "$RIME_DIR/build/luna_pinyin_simp.prism.bin" >/dev/null 2>&1 && log "luna deploy OK" || log "luna deploy MISSING"
bench weasel_rime weasel_luna zhihu120.txt "$ROOT/results/run/weasel_luna/sentences" 5
bench weasel_rime weasel_luna words234.txt "$ROOT/results/run/weasel_luna/words" 2
log "arm2 weasel_luna done"

# ---- arm 3: moqi product (default schema = frost) ----
log "arm3 moqi begin"
taskkill //IM MoqiLauncher.exe //F >/dev/null 2>&1
taskkill //IM MoqiLaunch.exe  //F >/dev/null 2>&1
taskkill //IM MoqiIME.exe     //F >/dev/null 2>&1
sleep 2
rm -rf "$APPDATA/Moqi/Rime/rime_frost.userdb" 2>/dev/null
rm -f "$APPDATA/Moqi/grammar_penalty_cache.json" 2>/dev/null
log "moqi userdb wiped: $(ls "$APPDATA/Moqi/Rime" 2>/dev/null | grep -c userdb) userdb left"
bench moqi_pinyin moqi_rerun zhihu120.txt "$ROOT/results/run/moqi_rerun/sentences" 5
bench moqi_pinyin moqi_rerun words234.txt "$ROOT/results/run/moqi_rerun/words" 2
log "arm3 moqi done"

python "$ROOT/scripts/collect_results.py" "$ROOT" weasel_frost
python "$ROOT/scripts/collect_results.py" "$ROOT" weasel_luna
python "$ROOT/scripts/collect_results.py" "$ROOT" moqi_rerun
log "==== FWM compare end"
echo ALL_DONE
