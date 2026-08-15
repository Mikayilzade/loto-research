# H002a — Mega Millions current $5-format progressive threshold

Updated: 2026-08-15
Status: **threshold quantified; sampled 2025–2026 cash jackpots far below break-even; full-space guarantee rejected**

## Current rules (primary operator)
Mega Millions current format (effective April 8, 2025):
- $5 per play;
- 5 of 70 white balls + 1 of 24 Mega Balls;
- jackpot odds 1 in 290,472,336;
- jackpot shared among multiple jackpot winners;
- built-in non-jackpot multiplier 2x/3x/4x/5x/10x;
- displayed multiplier odds: about 1 in 2.13 / 3.2 / 8 / 16 / 32;
- fixed non-jackpot prize table outside California; California non-jackpot prizes are pari-mutuel.

Primary sources:
- https://www.megamillions.com/how-to-play
- https://www.megamillions.com/FAQs.aspx

The displayed multiplier odds correspond to the exact 32-unit mix 15/32, 10/32, 4/32, 2/32, 1/32, giving expected multiplier exactly **3.0**. This should be treated as a mathematical reconstruction consistent with the official rounded odds.

## Exact fixed-jurisdiction lower-tier EV
Using exact combinatorial probabilities and expected multiplier 3.0:

**Expected non-jackpot payout = $1.1184749105 per $5 play.**

Therefore the jackpot component must contribute:

`5 - 1.1184749105 = 3.8815250895 USD/play`.

With jackpot probability `1 / 290,472,336`, the absolute optimistic break-even cash jackpot under zero tax and zero sharing is:

**$1,127,475,660**.

This is already more than twice the largest post-change cash jackpot observed in the current format in the sources checked.

## Sharing curve
For `n` other lines and uniform exact-combination choice, conditional expected retained jackpot share is:

`S = [1-(1-1/M)^(n+1)] / ((n+1)/M)`

with `M=290,472,336`.

No-tax cash break-even rises to approximately:
- 10m other lines: $1.1470bn;
- 25m: $1.1767bn;
- 50m: $1.2273bn;
- 100m: $1.3327bn;
- 200m: $1.5598bn;
- 300m: $1.8082bn.

Data: `data/derived/h002a_megamillions_sharing_threshold_curve.csv`.

## Current/historical state screen
Primary operator examples:
- 2026-07-28 jackpot: estimated $800m annuity / **$344.2m cash**, one Florida winner.
- 2025-11-14 jackpot: $983m annuity / **$453.6m cash**.
- 2026-03-10 jackpot: $536m / **$245.6m cash**.

All are far below the $1.1275bn zero-sharing/no-tax cash threshold, so they cannot be positive-EV states under this model.

The July 24, 2026 drawing had 500,257 winning tickets. Multiplying by the official overall-odds scale (~23) gives a rough ~11.5m-play magnitude proxy; even around that participation scale the sharing-adjusted threshold remains around $1.15bn cash, still far above the observed $344.2m cash state. This is only a rough participation proxy, not an exact national sales count.

## Full-space guarantee test
Complete combination space:

`C(70,5)*24 = 290,472,336` plays.

Acquisition cost:

**$1,452,361,680**.

Because the built-in multiplier is random, a strict all-outcome guarantee cannot use the expected 3x multiplier. Worst legal assignment is 2x for every non-jackpot winning line. Under complete coverage that gives deterministic lower-tier payout floor:

**$216,590,680**.

If we were guaranteed to be the sole jackpot winner, the required cash jackpot for nonnegative pre-tax profit would therefore be:

**$1,235,771,000**.

But the rules allow multiple jackpot-winning tickets and do not provide a useful pre-draw cap on duplicate jackpot winners. Hence complete coverage guarantees one jackpot-winning ticket but does **not** guarantee what fraction of the jackpot we retain.

Therefore **full-space Mega Millions is rejected as a terminal guaranteed-profit strategy**. Taxes, California pari-mutuel differences, execution capacity, and capital/transaction frictions only make the guarantee harder.

## Files
- `src/loto_research/megamillions_threshold.py`
- `tests/test_megamillions_threshold.py`
- `data/derived/h002a_megamillions_sharing_threshold_curve.csv`

## Conclusion
H002a does not produce SUCCESS. It does establish a strong quantitative filter: a current-format Mega Millions cash jackpot must exceed roughly **$1.127bn before sharing and tax** merely to reach positive expected value in a fixed-prize jurisdiction. Strict guaranteed profit via full-space coverage is unavailable because random multiplier downside raises the floor and jackpot sharing has no useful hard pre-draw bound.
