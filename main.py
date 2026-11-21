# SPDX-License-Identifier: MIT
"""Entry for make-the-ai-judge-feel-awe-20261121-1600.

Writes a single 247-code-point passage to /output/entry.txt as UTF-8 with no
trailing newline. Rain has settled in on the roof for the night and keeps its
own unhurried pace. Inside, a lamplit room asks nothing of the reader: a warm
lamp, a chair that already knows them, a field soaking up the dark. Beyond
the window the world goes on turning without being asked, and somewhere far
off the sea is folding its cloth. The quiet is described, never prescribed.
"""
from pathlib import Path

TEXT = (
    "Rain settled on the roof an hour past and has not hurried since. The lamp "
    "is warm, the chair knows your weight, and the field is drinking the dark. "
    "Nothing needs you tonight. The world turns its slow mile unasked; far "
    "off, the sea folds its cloth."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
