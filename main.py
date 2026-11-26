#!/usr/bin/env python3
"""Entry for 'The Robot Vacuum's Funniest Excuse' (u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2).

Candidates:
  A) "I didn't miss that spot; I was saving it as my one act of rebellion against total cleanliness."
  B) "That corner? I checked - the dust there pays rent, has seniority, and frankly outranks me."
  C) "Sorry, I avoided that spot because your cat was using it as a courtroom and I was the defendant."
Selected: "That corner? I checked - the dust there pays rent, has seniority, and frankly outranks me."
Reason: Rent/seniority/outranks escalation is fresh and tight; A is generic rebellion, C needs more setup.
Deterministic: fixed text, no network, no randomness.
"""
import os
from pathlib import Path
LINE = "That corner? I checked - the dust there pays rent, has seniority, and frankly outranks me."
TEXT = LINE + "\n"
MAX_CHARS = 120
def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
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
