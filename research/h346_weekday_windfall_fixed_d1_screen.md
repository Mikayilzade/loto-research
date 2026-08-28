# H346 — Weekday Windfall fixed-D1 / lower-tier dilution screen

## Question
Can current Australian Weekday Windfall (WA: Millionaire Medley) exploit its unusual fixed A$1m Division-1 payment as a full-cover guaranteed-profit mechanism?

## Sources checked
- The Lott Help Centre: Weekday Windfall is 6/45, A$1m Division 1 for up to six winners, then A$6m shared if >6 winners; special Cashcade/Double Your Win events affect lower divisions.
- Lotterywest Millionaire Medley page: same A$1m-for-up-to-six structure and A$6m cap.
- Lotterywest media release, 9 Apr 2026: a A$2 `Slikpik 3` Millionaire Medley ticket won D1. This gives a current published three-game acquisition unit at A$2.
- Oz Lotteries current game guide: D1 6; D2 5+supp; D3 5; D4 4; D5 3+supp; D6 1 or 2 + both supplementaries.

## Exact cover arithmetic
`C(45,6)=8,145,060` standard lines. Because this is divisible by 3, using the published A$2 Slikpik-3 unit gives exact acquisition cost `8,145,060/3 * A$2 = A$5,430,040`.

For any fixed draw with six main and two supplementary numbers, exact cover multiplicities are invariant:
- D1 = 1
- D2 = C(6,5) C(2,1) = 12
- D3 = C(6,5) C(37,1) = 222
- D4 = C(6,4) C(39,2) = 11,115
- D5 = C(6,3)[C(2,1)C(37,2)+C(2,2)C(37,1)] = 27,380
- D6 = C(6,2)C(2,2)C(37,2)+C(6,1)C(2,2)C(37,3) = 56,610

Total prize-eligible lines = 95,340. These imply odds matching the published rounded odds.

## Result
The structural novelty is real but insufficient. Full cover guarantees exactly one D1 line, yet ordinary D1 receipt is at most A$1m. That leaves A$4,430,040 of acquisition cost to be covered by D2-D6. Those lower divisions are share-based/pari-mutuel rather than fixed per line, and the governing/public structure does not establish the hard external-duplicate cap required for a strict pre-draw lower-bound of that magnitude. Moreover, once total D1 winners exceed six, even D1 is diluted from the A$6m pool.

Therefore H346 closes Weekday Windfall as an implementation of the specific fixed-per-winning-selection forced-distribution idea. It does **not** prove a universal impossibility theorem for all promotions of this game; a future material promotion that turns lower divisions into non-dilutable fixed payouts or supplies a deterministic subsidy could warrant reopening.

Arithmetic inconclusive: 0. Execution/entitlement inconclusive relevant to this screen: 0. Overall: NOT SUCCESS.
