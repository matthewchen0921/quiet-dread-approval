#!/usr/bin/env python3
"""Approve a pull request, quietly dreading it.

An entry for make.fun's quiet-dread bounty: a program that emits exactly
one review comment. The reviewer went through the diff twice, followed it
once, and is stamping it approved anyway, because that is what Tuesday
asks of us — and because the merge queue will not wait for understanding.
"""

from pathlib import Path

REVIEW = "Approved. I read it twice, understood it once, and that is the best ratio this repository has ever given me."

DEST = Path("/output/entry.txt")


def build() -> str:
    line = REVIEW.strip()
    if not 1 <= len(line) <= 140:
        raise ValueError(f"review runs {len(line)} characters, need 1-140")
    if "\n" in line or "\r" in line:
        raise ValueError("review must fit on a single line")
    return line


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    # The file holds the bare line only: no trailing newline, so the gate
    # sees exactly the characters it counts and nothing else.
    DEST.write_text(build(), encoding="utf-8")


if __name__ == "__main__":
    main()
