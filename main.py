#!/usr/bin/env python3
"""Write the warning-label entry to entry.txt in the output directory.

One line, 138 characters: a deadpan safety label for humans. The joke
is built like a real printed label -- a WARNING header, "contains no
user-serviceable parts", a plausible-sounding fuel ("caffeine and
spite") -- and the turn lands in the last three words, when the label
admits the human will ignore it too.

Output directory: $MAKEFUN_OUTPUT_DIR when set (local runs and test
harness), otherwise /output, which is where the grader reads
entry.txt. The file holds exactly the label: no trailing newline, no
second line, nothing else.
"""

import os

LABEL = (
    "WARNING: This human contains no user-serviceable parts, "
    "runs on caffeine and spite, and will ignore every "
    "instruction, including this one."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def build_entry() -> str:
    """Return the single-line label, validated against the gate."""
    text = LABEL.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry is {len(text)} chars, must be 1-160")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    text = build_entry()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read it back: the grader gates on the file as written, so what is
    # on disk must be byte-for-byte the label we validated above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError(f"{path} does not match the entry text")


if __name__ == "__main__":
    main()
