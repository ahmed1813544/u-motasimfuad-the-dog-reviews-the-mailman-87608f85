#!/usr/bin/env python3
"""The Dog Reviews the Mailman.

Writes one funny one-line review that a dog gives the mailman to
``entry.txt`` inside MAKEFUN_OUTPUT_DIR (falling back to /output).

Standard library only; the output is a fixed, hand-written line, so the
program is fully deterministic.
"""

import os

REVIEW = (
    "He brings a biscuit, smells like every dog on the street, "
    "and leaves without a single belly rub. "
    "One star - would bark again."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace text.
    assert 1 <= len(REVIEW) <= 200, "review must be 1-200 characters"
    assert REVIEW.strip(), "review must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
