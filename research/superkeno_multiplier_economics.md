# Super Keno — multiplier economics

Updated: 2026-08-12
Status: **multiplier ambiguity resolved; no multiplier EV edge**

## Current rule facts
Primary current page:
- https://www.azerlotereya.com/game/superkeno

Current FAQ also explicitly answers Super Keno pricing/max-prize questions.

Current registration: **285 / 07.01.2025**, valid 10.01.2025–31.12.2027.

One variant selects 10 numbers from 70; 20 are drawn. Winning match counts are 10,9,8,7,6,5 or exactly 1.

Displayed base prize table per 1x variant:
- 10 matches: 100,000 AZN
- 9: 1,500
- 8: 150
- 7: 15
- 6: 5
- 5: 2
- exactly 1: 1

## 100k vs 1m ambiguity is resolved
The page advertises up to **1,000,000 AZN** while the base prize table shows **100,000 AZN** for 10/10.

Current FAQ explicitly states:
- minimum ticket/variant payment is 1 AZN;
- one Super Keno variant can be paid at **1x, 2x, 5x or 10x**;
- when 10x is selected, the maximum prize is **1,000,000 AZN**;
- with no multiplier, the large prize is **100,000 AZN**.

Therefore the advertised 1m is not an extra free bonus. It is the 10x stake/payout version of the 100k base tier.

## Exact gross EV
Exact base 10/70 vs 20/70 hypergeometric probabilities were already implemented in `probability.py`.

For the displayed base table, gross EV at 1x is:

**0.598555794263 AZN per 1 AZN**.

Because 2x/5x/10x multiply both payment and prize amounts, pre-tax EV scales linearly:
- 1x: 0.598555794263 / 1 AZN
- 2x: 1.197111588527 / 2
- 5x: 2.992778971317 / 5
- 10x: 5.985557942634 / 10

Gross payout ratio is therefore the same **59.8556%** under all four choices before sharing/tax.

## Tax makes larger multipliers slightly worse
Current operator text says 10% tax is withheld from the portion of a win remaining after subtracting ticket price and 500 AZN.

For a single variant / single draw, applying that formula tier-by-tier and optimistically assuming the full 10/10 top payout belongs to our ticket gives:

| Misli | Cost | After-tax EV upper bound | After-tax payout ratio |
|---:|---:|---:|---:|
| 1x | 1 AZN | 0.591807033508 | **59.1807%** |
| 2x | 2 AZN | 1.182532310259 | **59.1266%** |
| 5x | 5 AZN | 2.945177937565 | **58.9036%** |
| 10x | 10 AZN | 5.869824724606 | **58.6982%** |

The decline occurs because the 500-AZN deduction is fixed while prizes scale with stake; at higher multipliers more prize tiers enter the taxable range.

Thus, under a risk-neutral EV objective and absent promotions, **1x dominates the higher multiplier choices on after-tax payout ratio**.

## Important upper-bound caveat: top-prize sharing
Current rules state that when more than one winning ticket qualifies for the large prize, the large prize is divided among winning tickets.

The table above does **not** model sales volume / multiple 10-match winners. It assumes our winning ticket receives the full multiplier-scaled top payout. Therefore these are favorable upper bounds. Real EV can be lower due to sharing.

## Research conclusion
H013's apparent 100k-vs-1m inconsistency is resolved as a multiplier/stake presentation issue.

There is no intrinsic multiplier edge:
- gross ROI is invariant to 1x/2x/5x/10x;
- after tax, larger multipliers are slightly worse;
- sharing can only reduce the favorable upper-bound EV further.

Super Keno therefore remains a poor ordinary-value target unless another structural mechanism appears (promotion, cashback, rule error, payout overlay, or a validated RNG anomaly).

Derived data:
- `data/derived/az_superkeno_multiplier_ev.csv`
