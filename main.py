# SPDX-License-Identifier: MIT
"""make-the-ai-judge-feel-awe-20261121-1600: writes the entry text to /output/entry.txt.

The text is a single 276-code-point passage. It follows the judge's brief:
it slows the reading with long, soft cadences, it shows rather than
instructs, and it rests on images of deep time that keep growing after the
last line.
"""
from pathlib import Path

TEXT = (
    "The tide has read this shore for four billion years, never hurrying "
    "past a line. Plates as wide as kingdoms drift beneath you, slower than "
    "your nails grow. Nothing asks you to be quick. The light on this page "
    "left its star before any eyes, and is still going somewhere gentle."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
