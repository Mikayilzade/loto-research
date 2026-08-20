# H117 — Poland Multi Multi recurring +50% promotion full-space bound

Updated: 2026-08-20
Status: **CURRENT PROMOTION + ENTIRE RECURRING 50%-BOOST CLASS CLOSED / NO SUCCESS**

## Goal
Test a high-value deterministic-promotion branch that was not covered by generic promo screens: Poland LOTTO's recurring Multi Multi promotions explicitly raise the fixed prize table for one chosen selection size by 50%. Because Multi Multi draws exactly 20 of 80 numbers and allows a player to choose k=1..10 numbers, buying every k-subset creates an outcome-invariant full-space portfolio. If the promotion lifted a sufficiently high base return above 100%, this would be a strict all-outcome arbitrage independent of number prediction or crowd behavior.

## Current official promotion state
The official Multi Multi page lists a supplemental rule in force **19–22 August 2026**. The official PDF states:
- base stake (`stawka`) is 2.00 PLN; the retail ticket price remains 2.50 PLN because the normal statutory surcharge applies;
- draws remain 20 numbers from 80, twice daily;
- the temporary prize table boosts the k=9 column by 50% versus the ordinary table;
- for ordinary Multi Multi, k=9 prizes become 105,000 / 3,000 / 450 / 63 / 12 / 3 PLN for 9/8/7/6/5/4 hits, versus ordinary 70,000 / 2,000 / 300 / 42 / 8 / 2;
- for Multi Multi Plus when Plus is hit, the k=9 prizes likewise become 450,000 / 15,000 / 1,350 / 183 / 33 / 9 / 6 / 6 / 21 PLN for 9..1 hits, exactly 1.5x the ordinary k=9 Plus column.

Official sources:
- https://www.lotto.pl/multi-multi/jak-grac
- https://www.lotto.pl/regulaminy#Regulaminy-promocje
- current supplemental PDF linked from the official page for 19–22.08.2026.

The public FAQ confirms the actual player price is **2.50 PLN** for ordinary Multi Multi and **5.00 PLN** with Plus.

## Deterministic full-space identity
For a fixed k, buy every `C(80,k)` distinct k-subset. Any draw contains exactly 20 winning numbers and 60 losing numbers. Therefore the number of owned tickets with exactly j hits is fixed for every possible draw:

`n(k,j) = C(20,j) * C(60,k-j)`.

Hence full-space gross return is deterministic and equals:

`G_k = sum_j n(k,j) * prize(k,j)`.

No draw simulation is needed; the portfolio has the same payout under every 20-of-80 outcome.

For Plus, distinguish whether the special twentieth drawn number is contained in the ticket. For a ticket with j total hits:

- Plus not contained: `C(19,j) * C(60,k-j)` tickets;
- Plus contained: `C(19,j-1) * C(60,k-j)` tickets.

This gives an exact deterministic full-space payout using the ordinary and Plus-hit prize tables.

## Current k=9 promotion result
The current 19–22 August promotion targets k=9.

### Without Plus
- combinations: `C(80,9) = 231,900,297,200`;
- ticket cost: 2.50 PLN;
- full-space cost: **579,750,743,000 PLN**;
- deterministic promotional gross: **355,722,807,000 PLN**;
- deterministic gross return: **61.3578872%**.

### With Plus
- same 231,900,297,200 k=9 combinations;
- ticket cost: 5.00 PLN;
- full-space cost: **1,159,501,486,000 PLN**;
- exact Plus/non-Plus partition payout under the 50%-boosted k=9 tables gives deterministic return **62.9250913%**.

Both are far below break-even before any execution, tax, purchase-limit or operational friction.

## Entire recurring 50%-boost class
The recurring campaign changes which k receives the +50% prize-table boost. To avoid re-testing each future rotation, every k=1..10 was screened using the current ordinary fixed prize tables and then granting a deliberately favorable **1.5x multiplier to every winning payout in that k column**.

Exact full-space returns are stored in `data/derived/h117_multimulti_promo_fullspace.csv`.

Best possible promotional full-space return across all k:
- ordinary Multi Multi: **61.7420554%** at k=5;
- Multi Multi Plus: **63.7186775%** at k=6.

Thus even if a future recurring promotion gives the same +50% boost to the most favorable k, the deterministic full-space portfolio remains below 64% gross. The current k=9 event is weaker than that bound.

## Why partial coverage cannot create a strict guarantee from this promotion alone
A partial set of k-subsets leaves possible draw states whose winning-ticket count is lower than under complete coverage, including states where no promoted high-tier payout is captured. The promotion only scales fixed prizes; it does not add an outcome-independent cash rebate. Since even complete coverage returns <1, removing tickets cannot establish an all-outcome positive-profit guarantee without an additional independent structural edge.

## Result
**NO SUCCESS.** The current 19–22 August 2026 Multi Multi +50% promotion is not a guaranteed-profit route, and the whole recurring `choose k / win 50% more` class is now closed under the current price/payout architecture:

- current k=9 no-Plus full-space: **61.3579%**;
- current k=9 Plus full-space: **62.9251%**;
- best hypothetical +50% k across all ordinary variants: **61.7421%**;
- best hypothetical +50% k across all Plus variants: **63.7187%**.

Reopen only if a future promotion exceeds roughly the reciprocal base-return multiplier needed for break-even (about 2.35x–2.60x depending on k/Plus), introduces a separate deterministic cash rebate, or materially changes ticket price/payout structure.
