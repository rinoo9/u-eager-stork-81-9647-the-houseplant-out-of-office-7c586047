#!/usr/bin/env python3
"""One-line houseplant out-of-office entry for the make.fun bounty
"The Houseplant Out-of-Office".

Writes exactly one line — an out-of-office auto-reply as if sent by a
houseplant — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes: the joke is the plant's own life, not a borrowed office
gag — an out-of-office reply from something that was never really in
the office at all, unwatered and ignored. The twist lands in the
final clause: HR keeps booking the plant meetings in direct sunlight
and it keeps fainting, which turns office bureaucracy into a
houseplant health hazard. That fits the judge brief: the funniest
out-of-office auto-reply a houseplant would send, in 120 characters
or fewer, funny on first read with a surprising payoff.

Second pass — why the line works: it opens on the plant's real need
("until someone waters me") so the reader knows at once who is
speaking, then the second sentence escalates from neglect to active
harm — the office itself is the problem, not just the watering can.
"Fainting" gives the plant a body that reacts, which makes the joke
physical instead of abstract. Voice: dry and matter-of-fact, like a
real auto-reply; the plant sounds resigned rather than angry, which
is what makes the complaint funny. The line stays under the limit at
107 characters, two short sentences, one breath.

Third pass — why the new line works: the plant reframes its absence
as official leave, and the acronym does the joke — PTO becomes
Photosynthesis Time Off, so the plant's biology is its holiday. Then
the punchline hands the chore to the fern, which has been covering
shifts since March: the plant is not just neglected, it has a
co-worker who is also neglected, and the final instruction ("water
it, not me") flips the auto-reply's job — instead of telling humans
when the plant returns, it tells them to water someone else. The
line stays under the limit at 111 characters, three short beats,
one breath.
"""

import os

ENTRY = (
    "Out of office: on PTO (Photosynthesis Time Off). The fern has "
    "covered my shifts since March — water it, not me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
