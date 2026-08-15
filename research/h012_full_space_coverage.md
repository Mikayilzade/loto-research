# H012 — full-space coverage / buy-the-pot

Updated: 2026-08-15
Status: **tested for Beşdə 5 and all ONLOTO base bet types; guaranteed-profit full coverage rejected for these cases**

## Goal
Test the most direct possible guarantee strategy: buy every possible base combination exactly once so that the realized draw cannot escape the portfolio.

This is stronger than ordinary positive-EV analysis. If the deterministic gross payout is below deterministic acquisition cost even before tax, sharing and execution friction, the guarantee path is rejected immediately.

## 1. Azerbaijan Beşdə 5
Official current rules state:
- choose 5 of 36;
- one variant costs 1 AZN; minimum ticket contains 2 variants;
- exact fixed payouts per variant: 5 matches = 50,000 AZN, 4 = 100, 3 = 10, 2 = 2;
- if there are 3+ jackpot-winning variants across the draw, 100,000 AZN is shared among them;
- winnings above the tax threshold are taxed under the published rule.

Primary source:
- https://www.azerlotereya.com/game/besde5

### Deterministic full-space count
Total variants:

`C(36,5) = 376,992`.

If every 5-set is purchased exactly once, then for any winning 5-set the number of our tickets with exactly m matches is:

`C(5,m) * C(31,5-m)`.

Therefore:
- 5 matches: 1
- 4 matches: 155
- 3 matches: 4,650
- 2 matches: 44,950
- 1 match: 157,325
- 0 matches: 169,911

Using the deliberately favorable assumption that our jackpot variant receives the full 50,000 AZN and ignoring tax/sharing deterioration:

`gross = 1*50,000 + 155*100 + 4,650*10 + 44,950*2`

`gross = 201,900 AZN`.

Cost:

`376,992 * 1 = 376,992 AZN`.

Guaranteed pre-tax/pre-sharing net:

`201,900 - 376,992 = -175,092 AZN`.

Return ratio:

`53.5555%`.

### Conclusion
Full-space Beşdə 5 is a **strict guaranteed loss** even under assumptions biased in favor of the player. Tax, possible jackpot sharing and execution costs can only worsen it.

Status: **REJECTED as guaranteed-profit full-space strategy**.

## 2. Azerbaijan ONLOTO
Official current page states:
- pool of 50 numbers;
- 36 numbers are drawn in order;
- player may choose 1–10 numbers;
- public base ticket price shown as 1 AZN;
- winning multiplier depends on the position at which the last required selected number appears;
- System play creates all selected sub-combinations as separate variants;
- official multiplier table is published for bet types 1–10.

Primary source:
- https://www.azerlotereya.com/lotereya/onloto

### Exact full-space identity
For bet type k, buy every k-subset of 50 exactly once.

There are:

`C(50,k)` variants.

For any realized draw order, exactly

`C(j-1,k-1)`

of those variants have their final selected number appear at draw position j.

If the official multiplier for type k at last-hit position j is `M(k,j)`, deterministic full-space gross payout is:

`stake * sum_j C(j-1,k-1) * M(k,j)`.

This does not require simulation and does not depend on which numbers are drawn first; the payout is invariant to draw order.

### Results
See `data/derived/h012_full_space_screen.csv`.

Guaranteed return ratios by bet type:
- type 1: **78.0000%**
- type 2: **77.5510%**
- type 3: **77.5408%**
- type 4: **77.6878%**
- type 5: **77.5309%**
- type 6: **76.5943%**
- type 7: **77.3335%**
- type 8: **77.3440%**
- type 9: **77.3644%**
- type 10: **77.2782%**

Best of the ten is still only 78% deterministic gross return.

The indexed operator table for type 6 contains a locally non-monotone parsed sequence around positions 24–25 (13 then 15). This is flagged for source-display recheck, but the guaranteed-return deficit is roughly 22–23%, so any plausible one-cell correction cannot change the conclusion.

### Conclusion
All ten ONLOTO full-space portfolios are **strict guaranteed losses before tax/execution**.

Status: **REJECTED as guaranteed-profit full-space strategy**.

## 3. 4+4 status
A naive full-space base portfolio contains:

`C(20,4)^2 = 23,474,025`

base 4+4 variants.

However a strict guarantee proof/rejection still requires:
- authoritative per-base-variant cost for ordinary vs 5+5/6+6 system tickets;
- category-II allocation/carryover rule;
- exact treatment of jackpot sharing and state-dependent pools under a portfolio that itself materially changes sales.

The public page confirms a 2-AZN ticket display and 5+5/6+6 system options but does not expose enough pricing/state accounting to certify a full-space profit guarantee.

Status: **BLOCKED for exact guaranteed-profit theorem; no evidence of a nonlinear system-ticket discount yet**.

## Code
- `src/loto_research/full_space.py`
- `tests/test_full_space.py`

## Data
- `data/derived/h012_full_space_screen.csv`

## Strategic conclusion
H012 remains open globally, but two highly relevant finite current Azerbaijan targets are now closed:
- Beşdə 5 full-space: rejected;
- ONLOTO bet types 1–10 full-space: rejected.

The next H012 work should target games with one or more of:
- accumulated guaranteed prize pool / final draw;
- bounded finite space small enough to cover;
- promotional subsidy;
- nonlinear system-ticket pricing cheaper than the sum of constituent variants;
- guaranteed lower-tier floor exceeding portfolio acquisition cost.
