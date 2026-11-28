#!/usr/bin/env python3
"""One word for my Wi-Fi.

The entry is a single English word, written to entry.txt. The program
validates the word before writing it, so a bad word fails loudly
instead of silently producing a bad entry.
"""

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
    with open("entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
