#!/usr/bin/env python3
"""One-line houseplant out-of-office entry for the make.fun bounty
"The Houseplant Out-of-Office".

Writes exactly one line — an out-of-office auto-reply as if sent by a
houseplant — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.
"""

import os

ENTRY = (
    "I'm out of office until someone waters me. I've been gone since "
    "March and nobody noticed \u2014 not even the fern."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
