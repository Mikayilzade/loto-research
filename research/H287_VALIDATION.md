# H287 VALIDATION — Atlantic Lottery AL Rewards + KENO Atlantic

Date: 2026-08-26
Result: **VALIDATED / CLOSED for checked additive mechanism**

## Independent checks performed
1. Re-read `STATUS.md` and `research/H225_EXACT_STATUS.md`; H225-X* is terminal at X20 with 0 coefficient survivors / 0 legal shift tuples, so no H225 continuation was created.
2. Inspected newest branch commits before assigning H287; latest completed packet was H286 and no H287 file/result existed.
3. Verified current Atlantic Lottery Terms: 1,000 AL Rewards points = $1 Promo Cash; Promo Cash is not withdrawable; Promo-Cash-funded purchases do not earn points on that portion.
4. Granted the player the current advertised maximum **6 points per $1** as a deliberately favourable upper bound.
5. Recomputed KENO Atlantic 2- through 10-Spot expected gross directly from exact hypergeometric multiplicities `C(20,m)C(50,k-m)/C(70,k)` and the current published fixed paytable.
6. Best base average is independently attained by 7-Spot: exact fraction `497325/881452 = 56.4211097144%`.
7. Maximum one-step Rewards playable factor is `1.006`; therefore the best player-favourable average after the rebate is `56.7596363727%`.
8. Because every selection within a spot class is symmetric, and nonnegative mixtures average linearly, any checked additive portfolio has `minimum legal-outcome gross <= average gross <= 56.7596363727% of original cash spend`.

## Closure criterion
The bound is strictly below 100%, so an everywhere-positive cash-profit guarantee is impossible for the checked KENO + AL Rewards additive portfolio class even before applying KENO Atlantic's adverse C$3m draw prize cap.

No success claim is warranted. Global state remains **NO SUCCESS; NOT EXHAUSTED**.
