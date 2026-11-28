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


def write_entry(text: str) -> None:
    """Write the entry where the scorer expects it.

    The scorer mounts the repository read-only, so the entry must go
    to MAKEFUN_OUTPUT_DIR instead of the current directory. The
    directory is created first and the file is read back to verify.
    """
    # The scorer only guarantees this directory is writable.
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest, exist_ok=True)
    assert os.path.isdir(dest), "output directory is not a directory"
    target = os.path.join(dest, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(target, encoding="utf-8") as handle:
        saved = handle.read()
    assert saved == "Flaky\n", "entry.txt content does not match the chosen word"


def main() -> None:
    # Flaky: the signal comes and goes, and so does the connection.
    text = build_entry(WORD)
    assert text.strip() == WORD, "entry.txt must hold exactly the chosen word"
    write_entry(text)


if __name__ == "__main__":
    main()
