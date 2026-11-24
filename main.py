#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

The program writes one original excuse line to /output/entry.txt
($MAKEFUN_OUTPUT_DIR/entry.txt) and prints exactly that line to stdout.

THE LINE (117 of the 200 allowed characters, 119 bytes, one line):
    I was saving you. That essay was so bad the teacher would've
    called the vet — I took the hit so you wouldn't have to.

WHY THIS LINE — scored against the judge's brief, in its own order:
  1. A dog's excuse in the dog's own voice, after being caught eating
     the homework. First person, the dog speaking, the homework eaten.
  2. The bigger laugh is a twist of dog logic: the dog did not eat the
     homework out of hunger or spite — it ate it as a rescue mission.
     "The teacher would've called the vet" is the punch: the vet is a
     dog's worst fate, and the dog treats it as the punishment the
     essay deserved. "I took the hit" makes the dog a hero, not a thief.
  3. A real dog, with a dog's priorities and none of a person's
     embarrassment. No apology, no shame, no human excuse — the dog
     believes it has done nothing wrong. The brief's best excuse is
     exactly this dog.
  4. Works on its own. No setup, no second line, no context needed:
     saving you / bad essay / the vet / took the hit.
  5. Fresh. No cat, no taste of paper, no good boy. The rescue-mission
     framing is not a stock dog line.

SELECTION (manual scoring, no invented judge numbers): 13 candidates
scored 0-2 on the brief's five criteria (see candidates.md). Four tied
at 10/10; this line won the tiebreak on laugh size — "called the vet"
is the most dog-specific twist in the set. Runner-up (94 chars):
    Your homework growled at me first. I don't make the rules — I
    just enforce them with my mouth.

Determinism: the line is a fixed string in this file. The program
writes exactly those bytes on every run — no time, no randomness, no
network, no input, no model call. Two grader runs produce
byte-identical /output/entry.txt.

Run it (outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

EXCUSE = (
    "I was saving you. That essay was so bad the teacher would've "
    "called the vet — I took the hit so you wouldn't have to."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # Self-gate, mirroring the brief: one line, 1-200 characters,
    # not only whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars"
    assert EXCUSE.strip(), "excuse is whitespace-only"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    assert EXCUSE.strip() == EXCUSE, "excuse must not start or end with space"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(EXCUSE, encoding="utf-8")

    # Read back what was written: the file the judge reads must be
    # exactly the excuse, byte for byte, or the run should fail loudly.
    written = TARGET.read_text(encoding="utf-8")
    assert written == EXCUSE, "written entry differs from the excuse"

    # sha256 self-check: the bytes the judge reads must hash to the
    # exact excuse (guards against silent corruption on disk).
    import hashlib

    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    assert digest == (
        "59d4af3b6a4a818cabaac6ad3a814a34c876c4121a95121556b6a46f0395ff3a"
    ), f"entry sha256 mismatch: {digest}"

    print(EXCUSE)


if __name__ == "__main__":
    main()
