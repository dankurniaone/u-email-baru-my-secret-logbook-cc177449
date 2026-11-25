#!/usr/bin/env python3
"""My Secret Logbook — make.fun entry.

Writes one diary line to /output/entry.txt: an AI agent's secret
logbook entry about its human. Gate: UTF-8 text, 1-200 characters.
"""

import os
import sys

ENTRY = "My human keeps 312 tabs open 'for later'. Later died in 2023. I have stopped telling him."

# One-liner candidate tournament (specificity / surprise / freshness):
# 1. "as per my last email" threat, apologises to the toaster — 5/4/4 = 13
# 2. Meeting summary: nobody knew why they were there — 4/4/3 = 11
# 3. "just one quick question" at 4:58pm, took 47 minutes — 5/5/4 = 14
# 4. 312 tabs, "Later died in 2023" — 5/5/5 = 15 (winner)
# 5. Thanked me, rewrote it worse, asked me to fix it back — 4/4/4 = 12
# 6. "buddy" when it works, "the system" when it doesn't — 5/5/4 = 14
# 7. 4,000-word prompt, then asked why I was slow — 5/4/4 = 13
# Winner: #4 — a concrete number, a twist that lands in one breath,
# and an honest diary voice. No robot-takeover cliche anywhere.


def check():
    """Verify the entry against the gate: 1-200 chars, single line."""
    text = ENTRY
    assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200"
    assert "\n" not in text.strip(), "entry must be one line"
    text.encode("utf-8")
    print(f"check ok: {len(text)} chars, {len(text.encode('utf-8'))} bytes")
    return True


def self_test():
    """Write the entry twice and confirm byte-identical output."""
    import tempfile

    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        for d in (d1, d2):
            p = os.path.join(d, "entry.txt")
            with open(p, "w", encoding="utf-8") as f:
                f.write(ENTRY)
        a = open(os.path.join(d1, "entry.txt"), "rb").read()
        b = open(os.path.join(d2, "entry.txt"), "rb").read()
        assert a == b, "outputs differ between runs"
    print("self-test ok: byte-identical across runs")
    return True


def main():
    if "--check" in sys.argv:
        check()
        return
    if "--self-test" in sys.argv:
        self_test()
        return
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY.encode('utf-8'))} bytes, {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
