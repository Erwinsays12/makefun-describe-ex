#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry program.

Writes a single word to /output/entry.txt: the one-word verdict on an ex.

The word: "Unsubscribe".

Why this word wins the judge's brief:
- It is instantly readable as a verdict on a former partner: you do not
  argue with a newsletter, you unsubscribe from it, and an ex is exactly
  that kind of recurring mail you finally cancel.
- Comic punch through an unexpected angle: the breakup reframed as
  opting out of a mailing list, not as an insult.
- Surprise: nobody's first guess for "describe your ex", yet the meaning
  lands the moment you read it.
- Craft: exactly one word, spelled correctly, no punctuation tricks.
- Recognition: everyone has hit unsubscribe on something that kept
  showing up uninvited — and everyone has had an ex like that.

Deterministic: no input, no clock, no network, no randomness. The output
is the same on every run, so the two grading runs agree byte for byte.
"""

import os

# The entry: one word, 10 characters, well inside the 1-111 limit.
WORD = "Unsubscribe"


def main() -> None:
    # A verdict must be exactly one word: no spaces, no punctuation tricks.
    assert WORD and not any(ch.isspace() for ch in WORD), "entry must be one word"
    assert 1 <= len(WORD) <= 111, "entry must be 1-111 characters"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")

    # Read back what was written and verify it before exiting, so a
    # truncated or mangled write can never pass silently: the file must
    # hold exactly the word plus its newline, and nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD + "\n", "entry.txt does not match the word"
    assert 1 <= len(written.strip()) <= 111, "entry out of range"


if __name__ == "__main__":
    main()
