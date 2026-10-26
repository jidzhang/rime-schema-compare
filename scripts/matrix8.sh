#!/usr/bin/env bash
# 8-cell matrix: {weasel,moqi} x {mingyue,frost} x {as-shipped, +wanxiang-gram}
# White-box, per-cell 2 rounds x 2 corpora + memory probe. ASCII only.
set -u
ENG="D:/work/github/IME/windows-ime-bench/engine/rime-schema-compare"
cd "$ENG" || exit 1
OUT="$ENG/artifacts_matrix"
mkdir -p "$OUT"
C="D:/work/github/IME/windows-ime-bench/corpus/zhihu120.txt D:/work/github/IME/windows-ime-bench/corpus/words234.txt"
declare -A DLL=( [weasel]=lib/rime.dll [moqi]=lib/rime-moqi.dll )

for ENGK in weasel moqi; do
  for V in mingyuepinyin rime_frost mingyuepinyin_with_gram rime_frost_with_gram; do
    for RND in 1 2; do
      # sentences
      python scripts/benchmark_sentences.py --rime-dll "${DLL[$ENGK]}" --vendors "$V" \
        --corpus D:/work/github/IME/windows-ime-bench/corpus/zhihu120.txt \
        --out-dir "$OUT/${ENGK}_${V}_r${RND}" --progress-every 0 >/dev/null 2>&1
      # words
      RIME_BENCH_MIN_HANZI=2 python scripts/benchmark_sentences.py --rime-dll "${DLL[$ENGK]}" --vendors "$V" \
        --corpus D:/work/github/IME/windows-ime-bench/corpus/words234.txt \
        --out-dir "$OUT/${ENGK}_${V}_r${RND}" --progress-every 0 >/dev/null 2>&1
      echo "cell ${ENGK}/${V} round ${RND} done"
    done
  done
done
echo MATRIX_DONE
