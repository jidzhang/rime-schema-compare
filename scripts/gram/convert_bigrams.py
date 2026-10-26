#!/usr/bin/env python3
"""Convert word-bigram TSVs into build_grammar stdin feed (key value lines).

Rebuilt 2026-10-26 from the spec reverse-engineered in
MoqiIME/moqi-ime/report/2026-10-16-baseline.md (the original convert.js lived
in %TEMP%/gram-train/ and was wiped by a cleanup tool — do not put tools in
%TEMP% again):

  - key = (<=3-char suffix of word1) + (<=3-char prefix of word2)  [char-level]
  - value = summed raw count (build_grammar stores ln(value)*10000;
    on query side only strong collocations change ranking)
  - rear ("prefix$") keys: NOT emitted — the mining TSVs carry no sentence-end
    marks (verified: zero "$" tokens in zh-bigram.tsv); only affects
    rear_penalty edge scoring.

TSV input format (one line per head word):
  n\tW1\tW2:count W2:count ...

Usage:
  python convert_bigrams.py --weight zhihu=30 news=2 leipzig=2 default=1 \
      path/to/a.tsv name=path/to/b.tsv ... > feed.txt
  build_grammar.exe zh-newmoqi < feed.txt
"""

from __future__ import annotations

import argparse
import io
import sys
from collections import defaultdict
from pathlib import Path


def sig(w1: str, w2: str, n: int = 3) -> str:
    return w1[-n:] + w2[:n]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tsv", nargs="+", help="tsv path or name=path with weight key")
    ap.add_argument("--weight", action="append", default=[], metavar="NAME=MULT",
                    help="weight spec name=mult, repeatable (e.g. --weight zhihu=30 --weight news=2); 'default=1' fallback")
    ap.add_argument("--min-count", type=int, default=1,
                    help="drop pairs below this weighted count")
    args = ap.parse_args()

    weights = {}
    for spec in args.weight:
        k, _, v = spec.partition("=")
        weights[k] = float(v or 1)
    default_w = weights.get("default", 1.0)

    agg: dict[str, float] = defaultdict(float)
    for item in args.tsv:
        if "=" in item:
            name, _, path = item.partition("=")
        else:
            path = item
            name = ""
        if not name:
            name = Path(path).stem.split("-")[0]
        w = weights.get(name, default_w)
        n_rows = n_pairs = 0
        for line in io.open(path, encoding="utf-8", errors="ignore"):
            if not line.startswith("n\t"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            w1 = parts[1]
            n_rows += 1
            for tok in parts[2].split(" "):
                i = tok.rfind(":")
                if i <= 0:
                    continue
                w2, c = tok[:i], tok[i + 1:]
                try:
                    c = float(c)
                except ValueError:
                    continue
                if c <= 0:
                    continue
                agg[sig(w1, w2)] += c * w
                n_pairs += 1
        sys.stderr.write(f"[convert] {name} weight={w} rows={n_rows} pairs={n_pairs}\n")

    out = 0
    for k, v in sorted(agg.items()):
        if v < args.min_count:
            continue
        # build_grammar reads "key value" whitespace-separated from stdin
        sys.stdout.write(f"{k} {v:g}\n")
        out += 1
    sys.stderr.write(f"[convert] signatures emitted: {out} (min-count {args.min_count})\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
