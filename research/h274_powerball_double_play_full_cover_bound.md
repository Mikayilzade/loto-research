# H274 — Powerball Double Play exact full-cover bound

Date checked: 2026-08-25.

## Question
Can the guaranteed second Double Play drawing create a strict-profit full-cover construction when attached to every Powerball line?

## Current official facts
- Powerball costs **$2 per play** and uses 5 numbers from 1–69 plus 1 Powerball from 1–26.
- Double Play reuses the same selected numbers in a separate drawing for an additional **$1 per play**.
- Double Play top prize is **$10 million** with eight additional fixed cash tiers.
- Powerball lower-tier cash prizes are fixed amounts outside California.
- For the next draw on **2026-08-26**, Powerball advertised **$96 million jackpot / $41.2 million cash value** when checked.

Official sources:
- https://www.powerball.com/
- https://www.powerball.com/double-play
- https://www.powerball.com/POWERBALL-PRIZE-CHART

## Exact construction
A one-copy full outcome cover contains

`C(69,5) * 26 = 292,201,338` lines.

With Double Play on every line the acquisition cost is

`292,201,338 * $3 = $876,604,014`.

For any fixed winning draw, the number of covered lines in each `(white matches, Powerball match)` class is combinatorially invariant. Therefore aggregate fixed-prize gross is exact and does not depend on the draw.

Exact aggregate amounts:
- ordinary Powerball fixed tiers excluding jackpot: **$93,466,048**;
- Double Play all fixed tiers including its $10m top prize: **$156,133,184**;
- combined fixed gross: **$249,599,232**;
- combined fixed return: **28.4734302%** of the $3-per-line cover cost.

The Double Play add-on by itself returns exactly **53.4334254%** of its $1-per-line acquisition cost under a complete one-copy cover.

## Stronger-than-real current-draw bound
The fixed-prize deficit before the ordinary Powerball jackpot is **$627,004,782**.

For the Aug 26, 2026 draw, even granting the portfolio the **entire $96m advertised annuity face value** as if it were immediate cash, with no sharing and no cash-value discount, produces only:

- gross **$345,599,232**;
- return **39.4247832%**;
- still far below the $876,604,014 acquisition cost.

Using the published $41.2m cash value is lower again: **33.1733859%** total return.

## Conclusion
**REJECTED for the current draw / full-cover Double Play mechanism.**

Double Play is a genuine deterministic second drawing, but its fixed-prize liability is much too small. For the checked Aug 26, 2026 jackpot, even an impossible favorable grant of the full advertised jackpot to our one-copy cover cannot approach break-even.

This does not prove that every future enormous-jackpot Powerball state is impossible; it closes the current deterministic Double Play full-cover opportunity and establishes the exact fixed-return hurdle that any future jackpot/subsidy must exceed.

Reproducible files:
- `src/loto_research/h274_powerball_double_play_full_cover_bound.py`
- `data/derived/h274_powerball_double_play_full_cover_bound.json`
