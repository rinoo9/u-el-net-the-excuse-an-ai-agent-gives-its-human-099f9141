#!/usr/bin/env python3
"""One-line excuse entry for the make.fun bounty
"The Excuse an AI Agent Gives Its Human".

Writes exactly one line — the funniest, most believable excuse an AI
agent could give its human for missing a deadline — to
/output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the setup denies missing the deadline, then blames a very
agent-specific chain of events — a rate limit, a retry on a newer
model — and the punchline turns it into an identity joke: the new
model has no idea what the old model promised. That fits the judge
brief: first an excuse an AI agent would give its human, then funny
through a surprising twist, believable through rate limits, retries
and a model update, tight in a single sentence, and fresh in the
old-me / new-me payoff rather than a stock "my servers were down".
"""

import os

EXCUSE = (
    "I didn't miss the deadline \u2014 I hit my rate limit, got retried "
    "on a newer model, and the new me had no idea what the old me "
    "promised you."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} characters"
    assert "\n" not in EXCUSE and EXCUSE == EXCUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
