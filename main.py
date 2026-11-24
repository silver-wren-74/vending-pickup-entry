#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: a pickup
line spoken by a vending machine to a passing human.

DRAFT 1 (candidate): the exact-change complaint — the machine asks if
you are exact change, because everyone else just jams its coin slot and
walks away angry. Machine-flavoured, but the machine sounds bitter, and
a bitter pickup line makes the human walk faster, not smile.

REVISION PASS (against the RULES judging criteria, in order):
1. Still spoken by the machine itself to a passing human — the whole
   line is the machine noticing it was chosen.
2. It lives entirely in the machine's world: the row of buttons, being
   stopped at, the coil, and the drop it performs a hundred times a
   day for strangers.
3. The laugh arrives in the last few words: this drop, the machine
   admits, was rehearsed. A vending machine practising its one moment
   of romance all week is the joke, and it needs no setup explained.
4. Short and speakable in one breath; nothing tacked on after the turn.
5. Charming rather than creepy: the machine is flattered, not pushy —
   cheeky and warm enough to earn a smile from the passer-by.

FINAL LINE: you stopped at mine; the coil rehearsed.
"""

import os

LINE = (
    "You pressed every button on your way down the row, but you stopped "
    "at mine \u2014 and my coil has been rehearsing this drop all week."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
