# H265 validation — NJ Pick-3 Green Ball terminal bound

Validated 2026-08-25 against current NJ Lottery Pick-3 prize tables and the official Aug. 18, 2026 Green Ball promotion report.

## Rule gates
- Latest checked Green Ball promotion: July 6 through August 3, 2026; now ended.
- Promotion chamber: six white balls + one Green Ball.
- White balls are removed after selection; Green Ball triggers a free second set of Pick-3 winning numbers from the same wager.
- Therefore six consecutive white removals create a deterministic next Green Ball event.
- FIREBALL doubles play cost and is not part of Green Ball second-draw winner determination.

## Arithmetic gates
For a $0.50 base wager:
- Straight: one-draw average gross = `1/1000 * $250 = $0.25` = 50%.
- 3-Way Box: `3/1000 * $80 = $0.24` = 48%.
- 6-Way Box: `6/1000 * $40 = $0.24` = 48%.
- Pair: `1/100 * $25 = $0.25` = 50%.

Known terminal Green Ball state grants exactly two base Pick-3 draws for one base wager:
- Straight / Pair terminal average return = **100%**.
- 3-Way / 6-Way Box terminal average return = **96%**.

FIREBALL add-on average gross from the published combination/prize table is `$0.27` per $0.50 add-on for the checked primitives. Because combined base+FIREBALL cost is $1 and Green Ball excludes FIREBALL:
- Straight / Pair terminal combined average return = **77%**.
- Box terminal combined average return = **75%**.

## Portfolio theorem
For every nonnegative portfolio, minimum legal-outcome gross is at most average gross. Since every allowed primitive has terminal average gross <= its cost, and Straight/Box plus Wheel are nonnegative decompositions of those primitives, no mixture can guarantee gross strictly greater than cost for every legal regular/bonus outcome pair.

This is stronger than checking a specific 1000-line full cover: it closes the entire nonnegative fixed-wager portfolio class for this promotion mechanism.

## Conclusion
**CLOSED / REJECTED.** The elimination mechanic is real and can make the second draw deterministic before purchase, but the exact fixed-prize economics stop at break-even average in the best no-FIREBALL primitive. Strict guaranteed profit is impossible under the checked rules.

Reopen only after a material rule/payout/discount change that pushes the deterministic terminal average strictly above 100%.
