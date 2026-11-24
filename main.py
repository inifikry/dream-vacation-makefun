#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun bounty entry.

Writes exactly one emoji to /output/entry.txt: Mount Fuji (U+1F5FB).
A single Unicode code point, one character, no trailing newline,
no other text — nothing but the emoji itself.

Why this emoji (per the judge's brief, in its own order):
1. Exactly one emoji, and it plainly names a dream vacation: a mountain,
   a faraway place — the brief lists both.
2. A postcard at a glance: a stranger sees the place before reading a word.
3. Personal and specific, not generic: one particular dream (Japan,
   Mount Fuji) rather than any holiday.
4. A fresher pick than the obvious beach/palm/plane.
5. Reads instantly across cultures and screens, clear at small size.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The dream vacation, in one emoji: Mount Fuji.
EMOJI = "\U0001F5FB"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the emoji, nothing else: no newline, no spaces, no words.
    OUTPUT_PATH.write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
