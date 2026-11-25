#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — one sharp cat joke, under 200 chars.

A cat who has never paid rent somehow owns the sunny spot, the good
chair, and — legally, I suspect — the whole house. The turn lands in
the aside: she did not earn the house, she simply took possession.
"""
import os

ENTRY = "My cat has never paid a cent of rent, but she owns the sunny spot, the good chair, and \u2014 legally, I suspect \u2014 the house."

# Gate: /output/entry.txt must be 1-200 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
