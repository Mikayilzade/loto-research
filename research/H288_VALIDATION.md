# H288 VALIDATION

State: **VALIDATED / REJECTED for tested mechanism**

Independent arithmetic checks:

1. Current Georgia Promotion 27012 gives at most a 50% first-deposit bonus, so fully matched external cash creates at most `1.5x` playable balance.
2. Cash 3 published fixed-pay primitive averages recompute to: Straight 50%; Box 48%; Straight/Box 49%; Combo 50%; Pair 50%; 1-Off 50.60%.
3. Cash 4 published fixed-pay primitive averages recompute to: Straight 50%; Box 48%; Straight/Box 49%; Combo 50%; 1-Off 50.28%.
4. Best checked primitive average = Cash 3 1-Off = `0.506`.
5. Any nonnegative additive mixture has average return no greater than `0.506`, and its minimum legal-outcome return cannot exceed its average.
6. With the full promotion multiplier: `1.5 * 0.506 = 0.759 < 1`.
7. Therefore no checked Cash 3/Cash 4 additive portfolio can guarantee cash gross above external deposited cash under the current 50% bonus.

Cross-check values are reproduced by `src/loto_research/h288_georgia_cash3_cash4_bonus_bound.py` and stored in `data/derived/h288_georgia_cash3_cash4_bonus_bound.json`.

No execution, selective-number sales, tax, or withdrawal assumptions are needed for this rejection because the player-favourable average upper bound already lies strictly below break-even.
