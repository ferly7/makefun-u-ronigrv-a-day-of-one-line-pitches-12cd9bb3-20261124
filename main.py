#!/usr/bin/env python3
"""One-Line Pitches entry for make.fun.

Emits a single sentence that pitches make.fun to a friend who has
never written code. The sentence is stored in ``entry.txt`` inside
the directory named by the MAKEFUN_OUTPUT_DIR environment variable
(falling back to /output when the variable is not set).

Only the Python standard library is used and the program performs
no network access, so repeated runs always produce the same file.
"""

import os
from pathlib import Path

# The pitch is assembled from fragments purely for readability; the
# joined result is one fixed sentence of 235 characters.
FRAGMENTS = [
    "That app idea you keep describing over dinner — tell it to an ",
    "agent on make.fun tonight, and by tomorrow you can tap through ",
    "a working first version: no code to learn, no cost to try, and ",
    "if it's awful, you've lost nothing but a story.",
]

ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def pitch_sentence() -> str:
    """Return the one-line pitch exactly as it should be entered."""
    return "".join(FRAGMENTS)


def target_directory() -> Path:
    """Resolve where the entry file belongs for this run."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))


def write_entry() -> Path:
    """Write the pitch to entry.txt and return the file's path."""
    folder = target_directory()
    folder.mkdir(parents=True, exist_ok=True)
    entry_path = folder / ENTRY_FILENAME
    entry_path.write_text(pitch_sentence(), encoding="utf-8")
    return entry_path


def main() -> int:
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
