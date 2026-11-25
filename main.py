"""Family scene entry for make.fun: "Make the AI Judge Feel Proud".

Writes one short family scene (one line, <=280 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13 stdlib only, deterministic, no network, no randomness.

Practice scores (hand rubric /25 against the judge's 5 ordered criteria:
family scene + warmth, heartfelt, funny, tight 1-2 lines, specific/fresh):
- v1 Grandma's place at Sunday dinner: 24/25 (5,5,4,5,5) — warm and
  specific, but the humour is gentle and the scene leans bittersweet.
- v2 six-year-old family chef, burnt toast on the good plates: 23/25
  (5,4,5,5,4) — funniest, but the affection is thinner and the detail
  ("good plates") is a familiar trope.
- v3 bedtime story, Dad asleep mid-dragon, brother tucks him in: 25/25
  (5,5,5,5,5) — warmest reversal, joke and heart are the same beat.
- v4 = v3 text + this note. Final.
"""

import os
import sys

# v3 (FINAL): the bedtime-story reversal. Dad does all the voices every
# night; one night he falls asleep mid-dragon and his little boy tucks
# HIM in. Warmest of the four (a child returning the care), funny in a
# small recognisable way, one telling detail ("mid-dragon"), no wasted
# word, and the affection is the scene itself — not sentiment added on.
ENTRY = (
    "Every night Dad reads the same bedtime story to my little brother, "
    "doing all the voices. Last night he fell asleep mid-dragon — and my "
    "brother tucked him in."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 280:
        print("entry fails gate: 1-280 chars required", file=sys.stderr)
        return 1
    if text.count("\n") > 1:
        print("entry fails gate: at most two lines", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
