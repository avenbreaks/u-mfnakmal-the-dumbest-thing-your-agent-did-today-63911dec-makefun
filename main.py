#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

The line is a single line, well under the 200-character cap, naming a
concrete, believable failure with the punch landing at the end.
"""

import os

LINE = "My agent spent an hour hiding our API key from its own logs, then printed the key in the very next command while double-checking it was hidden."

# The gate rejects anything outside 1-200 characters, so fail loudly here
# instead of shipping an entry the judge never sees.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, gate needs 1-200"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
