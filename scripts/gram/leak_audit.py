#!/usr/bin/env python3
"""Gate 1: refuse training if any eval sentence leaks into a training text."""
import argparse, io, re, sys
def norm(s):
    return re.sub(r"[^\u4e00-\u9fff]+","",s)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("train_txt",nargs="+")
    ap.add_argument("--eval",required=True)
    ap.add_argument("--report-only",action="store_true")
    a=ap.parse_args()
    tests=[norm(l) for l in io.open(a.eval,encoding="utf-8") if l.strip()]
    tests=set(t for t in tests if len(t)>=5)
    total=0
    for f in a.train_txt:
        hits=set()
        for l in io.open(f,encoding="utf-8",errors="ignore"):
            n=norm(l)
            if not n: continue
            total+=1
            for t in tests:
                if t in n or n in t:
                    hits.add(t); break
        if hits:
            print(f"[LEAK] {f}: {len(hits)} eval sentences overlapped")
            if not a.report_only: return 1
    print(f"[OK] leak audit passed ({len(tests)} eval sentences vs {total} train lines)")
    return 0
sys.exit(main())
