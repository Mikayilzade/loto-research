# H290 — Delaware KENO + iLottery/WebCash deposit-subsidy screen

Date: 2026-08-26
Status: **OPEN LEAD / ENTITLEMENT + CHANNEL GATES**

## Why this mechanism is new
H289 failed because Kentucky's governing online terms expressly allow selective refusal of number wagers. H290 instead screens Delaware's KENO paytable against an official Delaware Lottery iLottery/WebCash 100% deposit-match lead, looking for a compact deterministic cover that could cross cash break-even without relying on jackpot sharing.

## Official evidence checked
1. Delaware Lottery KENO current prize page: https://www.delottery.com/Keno/Prizes-And-Odds
   - field 1–80, 20 numbers drawn;
   - $1 base payouts include Spot-1 Match 1 = $2, Spot-2 Match 2 = $10, Spot-3 Match 3 = $25 / Match 2 = $2, etc.
2. Delaware Lottery KENO current play material: https://www.delottery.com/Keno/How-To-Play and current brochure.
   - player-selected numbers are supported;
   - $1–$20 wager per game;
   - retail game-slip maximum is $100 per KENO slip.
3. Delaware Lottery retailer newsletter (2026 Issue 85) described then-current iLottery promotions including a **100% Deposit Match up to $100** and a **WebCash 100% Deposit Bonus up to $100**.
4. Current Delaware Lottery affiliate page describes iLottery as internet Instant Games **and other Lottery products sold online**, and states new customers receive a Welcome Offer with a qualified deposit.
5. Current public KENO pages still direct the player to KENO retailers; current public material does not yet establish that the specific KENO wager needed here is purchasable with iLottery/WebCash bonus funds in August 2026.

## Exact base-game average-return screen
Using the current official $1 paytable and the exact hypergeometric distribution `P(M=m)=C(20,m)C(60,s-m)/C(80,s)`, the base-game expected gross per $1 is:

| Spot | exact average gross |
|---:|---:|
| 1 | 0.5000000000 |
| 2 | 0.6012658228 |
| 3 | **0.6243914314** |
| 4 | 0.5820445377 |
| 5 | 0.5427325839 |
| 6 | 0.5562760025 |
| 7 | 0.5953577726 |
| 8 | 0.5880531299 |
| 9 | 0.5636501380 |
| 10 | 0.5712408062 |

Spot-3 has the highest checked average return, about **62.4391%**. Therefore a genuine 100% spendable subsidy is mathematically strong enough in principle to cross the average-return hurdle; this is not an automatic no-go like many ~50% fixed-pay games.

## Deterministic Spot-1 cover
Buying all 80 Spot-1 numbers at $1 costs $80. Exactly 20 of the 80 tickets win $2 for every legal draw, so deterministic gross is exactly **$40**.

With a pure 100% deposit match funding `$40 cash + $40 bonus = $80`, the cash recovery is exactly `$40`, i.e. **break-even, not strict profit**. Thus Spot-1 alone cannot establish SUCCESS.

## Spot-2 graph formulation for the $100-match cap
A Spot-2 portfolio is a graph on the 80 KENO numbers:
- each purchased pair is one edge costing $1;
- a draw is a 20-vertex subset `S`;
- each purchased edge induced by `S` wins $10.

For `E <= 200` total purchased edges, a 100% match can fund the whole portfolio with `E/2` cash (subject to the $100 match cap). Strict guaranteed cash profit requires

`10 * min_{|S|=20} e(S) > E/2`,

or equivalently

`min_{|S|=20} e(S) > E/20`.

This is a finite extremal graph-design problem. A simple balanced disjoint-clique family does **not** pass: at the best sub-$200 examples checked, e.g. 14 balanced groups, `E=190` but the minimum 20-set contains only 6 purchased internal pairs, giving $60 gross versus $95 cash funding.

The averaging bound does not rule out a better graph: the average 20-set induced-edge count equals `E * C(78,18)/C(80,20) = E * 380/6320 ≈ 0.0601266 E`, above the strict-profit threshold `0.05E`. Therefore H290 contains a real exact-design subproblem rather than an already-proved impossibility.

## Gates before spending CI on exact graph optimization
Do **not** launch a large exact graph search until both entitlement/channel facts are established from current official material:

1. **Currentness gate:** prove that the 100% iLottery/WebCash deposit match is actually available to an eligible player in August 2026 (the official newsletter proves the offer existed in 2026, but not its present August validity).
2. **KENO funding/channel gate:** prove that the relevant player-selected KENO wagers can be purchased online using the matched/bonus balance. Current public KENO pages are retailer-oriented, while the broader Internet Lottery regulations include keno generically; this is not yet enough for a rigorous execution claim.

If both gates pass, NEXT ACTION is an exact/minimax Spot-2 graph search under `E<=200`, with a certificate of `min_{|S|=20} e(S)` and a strict-profit check. If either gate fails, close H290 without wasting CI.
