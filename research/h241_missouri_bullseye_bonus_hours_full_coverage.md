# H241 — Missouri Club Keno Bulls-Eye / Double Bulls-Eye Bonus Hours full-coverage upper-bound closure

Date: 2026-08-24
Status: REJECTED for guaranteed-profit full coverage
Scope: LOTTERY ONLY

## Question
Does Missouri Club Keno Bonus Hours become a deterministic guaranteed-profit strategy when full combinatorial coverage uses the Bulls-Eye or Double Bulls-Eye add-on instead of ordinary base Club Keno?

## Current game facts
Official Missouri Lottery rules/page establish:
- Club Keno draws 20 numbers from 80.
- Bulls-Eye designates one of the 20 winning numbers as the red Bulls-Eye.
- Double Bulls-Eye designates two of the 20 winning numbers (red and green).
- Bulls-Eye doubles ticket cost; Double Bulls-Eye triples ticket cost.
- If Double Bulls-Eye is played, matching exactly one marked Bulls-Eye uses the Bulls-Eye prize schedule; matching both uses the Double Bulls-Eye schedule; no marked Bulls-Eye uses the ordinary base schedule.
- Bonus Hours historically/recurringly permits qualifying 10-draw Club Keno, Bulls-Eye and Double Bulls-Eye wagers, while Multiplier is excluded. The promotion advertises increased prizes up to 50%, with exclusions.

Primary sources:
- https://www.molottery.com/club-keno/club-keno.jsp
- https://www.molottery.com/club-keno/rules.jsp
- https://www.molottery.com/article.do?id=842&method=s
- https://www.molottery.com/article.do?id=2039&method=s

## Exact full-space identity
For an s-spot full cover, every C(80,s) subset is bought.

For Bulls-Eye, with one marked winning number, the number of selected tickets having m total winning numbers and r in {0,1} marked Bulls-Eyes is:

`C(1,r) * C(19,m-r) * C(60,s-m)`.

For Double Bulls-Eye, with two marked winning numbers, r in {0,1,2}:

`C(2,r) * C(18,m-r) * C(60,s-m)`.

The payout used is ordinary Club Keno for r=0, Bulls-Eye for r=1, and Double Bulls-Eye for r=2. Summing over all m,r is deterministic and independent of which specific numbers are drawn.

## Dominating promotion bound
To avoid depending on the detailed Bonus Hours increase schedule, H241 gives the player a strictly stronger promotion than the real one:

**every payout is multiplied by 1.50, with no exclusions at all.**

This dominates the actual promotion because actual rules say `up to 50%` and contain exclusions. Therefore if full coverage loses even under this artificial upper bound, the real promotion cannot guarantee profit.

The required 10-draw qualification multiplies both spend and deterministic gross by 10, so return ratios are unchanged.

## Results
All Bulls-Eye and Double Bulls-Eye spot categories remain below break-even under the universal +50% upper bound.

- Best Bulls-Eye result: **3-spot, 90.9749%** return.
- Best Double Bulls-Eye result: **9-spot, 98.0054%** return.
- Thus even the strongest add-on case remains below 100% before taxes, execution costs, liability caps or operational constraints.

For the practically smaller 3-spot space:
- full space = 82,160 combinations;
- Bulls-Eye cost per draw = $164,320; deterministic gross = $99,660; artificial +50% gross = $149,490; net = **-$14,830** per fully covered draw;
- Double Bulls-Eye cost per draw = $246,480; deterministic gross = $150,264; artificial +50% gross = $225,396; net = **-$21,084** per fully covered draw.

With the required 10-draw ticket these deficits scale by 10.

## Verdict
**REJECTED.** H240 closed ordinary base Club Keno Bonus Hours full coverage. H241 now closes the remaining Bulls-Eye and Double Bulls-Eye full-coverage variants for every spot category 1–10 by a promotion upper bound stronger than the actual rules. No execution-feasibility analysis can rescue a mathematically negative deterministic upper bound.

Reopen only if Missouri materially changes ticket pricing, payout tables, or offers a deterministic promotion stronger than the modeled universal +50% payout multiplier.