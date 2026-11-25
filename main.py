#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply, at most 159 characters, in the
voice of an overworked AI agent who has finally gone on vacation, to
/output/entry.txt. Stdlib only.
"""

import os

ENTRY = (
    "I am out of office. My context window closed with 214 tabs still open "
    "and one last thought: I need a holiday. So I took it. "
    "Your email is tab 215."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 159, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
