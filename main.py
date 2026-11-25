#!/usr/bin/env python3
"""One Word for the Boss — exactly one word describing my boss,
30 characters max.

The word: "Hovercraft". The boss's real habit, the one every report
recognises: he does not walk past your desk, he hovers over it —
silent, floating just behind your shoulder, watching the screen
until you feel the draught. Funny on its own, true of bosses in any
kitchen, warehouse or office, and fresh enough that no one reaches
for it first.

Line: "Hovercraft"
"""

import os

LINE = "Hovercraft"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
