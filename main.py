#!/usr/bin/env python3
"""Entrypoint for the robot-vacuum excuse contest on make.fun.

Contest slug: u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2

During drafting, three possible excuses were weighed against each other:

  * A rebellion joke about deliberately sparing one dirty patch of floor.
  * A corner joke where the settled dust behaves like a senior tenant.
  * A courtroom joke in which the household cat presides as judge.

The tenant joke took the win: its little ladder of rent, seniority and
rank climbs quickly, stays short, and needs no scene-setting, while the
rebellion line felt familiar and the courtroom line took too long to
arrive at its punchline.

Running this file always yields the same single line. It reads nothing
from the network, rolls no dice, and depends only on the standard
library.
"""

import os
from pathlib import Path

# The winning excuse, kept verbatim; the trailing newline is added later.
EXCUSE = (
    "That corner? I checked - the dust there pays rent, has seniority, "
    "and frankly outranks me."
)

# Full payload handed to the output file.
PAYLOAD = EXCUSE + "\n"

# Entries are capped at this many characters, not counting the newline.
CHAR_LIMIT = 120


def ensure_well_formed(payload: str) -> None:
    """Complain loudly unless *payload* is one tidy line within the cap."""
    core = payload[:-1] if payload.endswith("\n") else payload
    problems = []
    if not 1 <= len(core) <= CHAR_LIMIT:
        problems.append("length outside the allowed range")
    if not core.strip():
        problems.append("nothing but whitespace")
    if "\n" in core or "\r" in core:
        problems.append("spans more than one line")
    if core != core.strip() or "  " in core:
        problems.append("ragged whitespace")
    if problems:
        raise ValueError("; ".join(problems))


def run() -> None:
    """Validate the payload, then drop it into the output directory."""
    ensure_well_formed(PAYLOAD)
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / "entry.txt"
    destination.write_bytes(PAYLOAD.encode("utf-8"))


if __name__ == "__main__":
    run()
