# SPDX-License-Identifier: MIT
"""Entry for make-the-ai-judge-feel-awe-20261121-1600.

Writes one 270-code-point passage to /output/entry.txt, UTF-8, no trailing
newline. The passage slows the reading with long, soft cadences, shows the
calm instead of asking for it, and ends on an image of deep time that keeps
growing past its last line.
"""
from pathlib import Path

TEXT = (
    "The tide has read this shore for four billion years and never once "
    "hurried past a line. Beneath it, plates as wide as kingdoms drift, "
    "slower than nails grow. Tonight the water holds light that left its "
    "star before there were eyes. More is still coming, from farther off."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
