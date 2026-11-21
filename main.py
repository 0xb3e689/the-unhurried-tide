# SPDX-License-Identifier: MIT
"""Entry for make-the-ai-judge-feel-awe-20261121-1600.

Writes one 275-code-point passage to /output/entry.txt, UTF-8, no trailing
newline. The passage slows the reading with long, soft cadences: rain on the
roof, a warm lamplit room, the world turning its slow mile unasked, and far
off the sea folding its cloth. It shows the calm instead of asking for it.
"""
from pathlib import Path

TEXT = (
    "Rain found the roof an hour ago and has not hurried since. The lamp is "
    "warm, the chair knows your weight, and the field is drinking the dark. "
    "Nothing needs you tonight. The world turns its slow mile unasked, and "
    "the stars keep the old count. Far off, the sea folds its cloth."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
