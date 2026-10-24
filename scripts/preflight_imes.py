#!/usr/bin/env python3
"""Preflight check: which requested IMEs are actually enabled in Windows.

Prints one [OK]/[MISSING] line per IME and finishes with a machine-readable
`OK_IMES=<keys>` line that run.bat consumes to skip missing IMEs cleanly.

Usage: python preflight_imes.py <ime_key> [ime_key ...]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from rime_schema_compare.ms_pinyin_harness import WindowsImeSwitcher  # noqa: E402


def main(argv):
    keys = [k.strip() for k in argv if k.strip()]
    if not keys:
        print("usage: preflight_imes.py <ime_key> [ime_key ...]")
        return 2
    switcher = WindowsImeSwitcher()
    by_key = {p.ime_key: p for p in switcher.list_installed_profiles()}
    ok = []
    for key in keys:
        profile = by_key.get(key)
        if profile is None:
            print("[MISSING] %s - not installed or not ticked in the Windows language list; will be skipped" % key)
        else:
            print("[OK] %s -> %s" % (key, profile.description))
            ok.append(key)
    print("OK_IMES=%s" % " ".join(ok))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
