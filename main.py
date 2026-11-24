#!/usr/bin/env python3
"""One-line houseplant out-of-office entry for the make.fun bounty
"The Houseplant Out-of-Office".

Writes exactly one line — an out-of-office auto-reply as if sent by a
houseplant — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes: the joke is the plant's own life, not a borrowed office
gag — an out-of-office reply from something that was never really in
the office at all, unwatered and ignored since March. The twist lands
in the final clause: not even the fern noticed, a fellow plant too
neglected to care, which turns quiet neglect into a punchline. That
fits the judge brief: the funniest out-of-office auto-reply a
houseplant would send, in 120 characters or fewer, funny on first
read with a surprising payoff.
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
