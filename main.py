#!/usr/bin/env python3
"""Break Production, Own It.

Writes a single one-line error message / postmortem excuse to
/output/entry.txt: one line, under 200 characters, no trailing newline.
Pure Python 3.13 standard library, no network, no model calls.
"""

import os

# Competition gate: entry must be 1-200 UTF-8 chars, one line, no trailing newline.
MAX_LEN = 200

ENTRY = (
    "I ran the cleanup script on production instead of staging, wiped every "
    "active session, and my rollback plan was a sincere apology typed into "
    "#incidents. I own this."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read what we wrote and assert the gate constraints.
    with open(output_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= MAX_LEN, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text == ENTRY, "written entry differs from the authored entry"


if __name__ == "__main__":
    main()
