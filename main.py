#!/usr/bin/env python3
"""Submission for 'The Robot Vacuum's Funniest Excuse'.

Competition: u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2

Three candidate excuses were considered:
  A) "I didn't miss that spot; I was saving it as my one act of rebellion
      against total cleanliness."
  B) "That corner? I checked - the dust there pays rent, has seniority,
      and frankly outranks me."
  C) "Sorry, I avoided that spot because your cat was using it as a
      courtroom and I was the defendant."

Candidate B won. Its rent / seniority / outranks ladder escalates in a
fresh, compact way, whereas A reads as generic rebellion and C needs
too much setup before the joke lands.

The program is deterministic: it emits one fixed line of text, uses no
network access, and involves no randomness.
"""

import os
from pathlib import Path

LINE = (
    "That corner? I checked - the dust there pays rent, has seniority, "
    "and frankly outranks me."
)
TEXT = LINE + "\n"
MAX_CHARS = 120


def validate(text: str) -> None:
    """Raise ValueError when *text* is not a clean single-line entry."""
    body = text[:-1] if text.endswith("\n") else text
    if not 1 <= len(body) <= MAX_CHARS:
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
