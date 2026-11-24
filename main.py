#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun entry.

Writes one sentence pitching make.fun to a friend who has never
coded, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: Python 3 stdlib only, no network, no randomness.
"""

import os

LINE = (
    "That app idea you keep describing over dinner — tell it to an "
    "agent on make.fun tonight, and by tomorrow you can tap through "
    "a working first version: no code to learn, no cost to try, and "
    "if it's awful, you've lost nothing but a story."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
