# H290 STATUS

Updated: 2026-08-26
Status: **OPEN LEAD / ENTITLEMENT + CHANNEL GATES BEFORE CI**

## H225-X* lane
H225-X* remains **CLOSED / EXHAUSTED** at X20: 44 canonical shards / 11 sectors / exactly 306,450 states -> **0 coefficient survivors / 0 legal shift tuples**. No X21/X22 under the unchanged family.

## New checkpoint
H290 screens Delaware KENO against an official Delaware Lottery 2026 iLottery/WebCash **100% deposit-match up to $100** lead.

Exact current KENO paytable arithmetic gives the following average gross per $1 for Spot 1–10:
`[0.5000000000, 0.6012658228, 0.6243914314, 0.5820445377, 0.5427325839, 0.5562760025, 0.5953577726, 0.5880531299, 0.5636501380, 0.5712408062]`.

Spot-3 is best at **62.43914314%**, so a genuine 100% spendable subsidy is mathematically above the simple average-return hurdle.

The trivial deterministic Spot-1 cover costs $80 and always returns exactly $40; funded by $40 cash + $40 100%-match it is exactly break-even, not strict profit.

For Spot-2, represent purchased pairs as edges of a graph on 80 numbers. A 20-number draw wins $10 per purchased induced edge. With `E<=200` edges (the range fully fundable by at most $100 cash + $100 matched bonus), strict guaranteed cash profit is exactly the finite condition

`min_{|S|=20} e(S) > E/20`.

Balanced disjoint-clique constructions under the cap fail; e.g. a 14-part balanced partition uses `E=190` purchased pairs but a legal 20-set can induce only 6 of them, so gross $60 < $95 cash funding. The averaging bound does not prove impossibility, so a better graph remains mathematically open.

## Gates before exact CI
1. Prove from current official material that the 100% iLottery/WebCash match is actually available in August 2026; the official 2026 retailer newsletter establishes the offer but not August currentness.
2. Prove that player-selected KENO wagers can be purchased with the matched online balance. Current KENO public pages are retailer-oriented; broader Internet Lottery regulations include keno but do not by themselves prove the current product/funding channel.

Only if both gates pass should H290 launch exact/minimax graph search under `E<=200`. Otherwise close H290 without spending CI.

Files:
- `research/h290_delaware_keno_deposit_subsidy_screen.md`
- `src/loto_research/h290_delaware_keno_subsidy_screen.py`
