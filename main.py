#!/usr/bin/env python3
"""One word for my Wi-Fi.

The entry is a single English word, written to entry.txt. The program
validates the word before writing it, so a bad word fails loudly
instead of silently producing a bad entry.
"""

import os

WORD = "Flaky"


def build_entry(word: str) -> str:
    """Return the entry text for one word."""
    cleaned = word.strip()
    if not cleaned.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    if not cleaned[0].isupper() or not cleaned[1:].islower():
        raise ValueError("entry must be one capitalised word")
    return cleaned + "\n"


def main() -> None:
    # Flaky: the signal comes and goes, and so does the connection.
    text = build_entry(WORD)
    assert text.strip() == WORD, "entry.txt must hold exactly the chosen word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read back and verify: a silent bad write must fail loudly, not ship an empty file.
    with open(entry_path, encoding="utf-8") as handle:
        written = handle.read()
    assert written == "Flaky\n", "entry.txt content does not match the chosen word"


if __name__ == "__main__":
    main()
