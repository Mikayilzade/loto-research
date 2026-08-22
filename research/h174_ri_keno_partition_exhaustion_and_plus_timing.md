# H174 — Rhode Island doubled-Keno clique-partition exhaustion + Keno Plus timing gate

Updated: 2026-08-22
Status: **H173 PROVEN OPTIMAL WITHIN 1–8 GROUP CLIQUE-PARTITION FAMILY / POST-PLUS PURCHASE LOOPHOLE NOT ESTABLISHED / NOT SUCCESS**

## Purpose
H173 found a 4,560-play guaranteed pre-tax cover under the conditional Rhode Island 3-spot assumptions: current/suitable paytable $25 for 3/3 and $2.50 for 2/3 per $1, with a free deterministic pre-locked 2x multiplier on every qualifying play.

H174 asks two high-value questions:
1. Can a simpler partition-of-80 construction beat 4,560 plays merely by changing the number or sizes of groups?
2. Can ordinary paid Keno Plus be exploited by waiting for its multiplier wheel to resolve and then buying into the immediately following Keno draw?

## Source facts
Current Rhode Island Keno page:
- https://www.rilot.com/en-us/keno.html

Current Rhode Island FAQ:
- https://www.rilot.com/en-us/player-zone/faqs.html

Current Rhode Island Lottery Rules and Regulations:
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules2026.pdf

Current Rhode Island homepage / promotions signal:
- https://www.rilot.com/

The homepage still exposes a live `Kick Back with Keno Promotion` title in August 2026, but indexed primary rules for that promotion remain unavailable. Therefore this packet still does **not** assume that the current promotion is the historical Lucky 3 Spot free doubler.

The 2026 rules state that Keno Plus costs an additional wager equal to the base Keno wager and that its wheel is conducted just prior to the applicable Keno drawing, producing No Plus, 2x, 3x, 4x, 5x or 10x.

The current FAQ states that iLottery wagering is unavailable during each game's draw-break period. The current Keno page offers the next draw / consecutive draws; no public interface was found that allows a player to observe the Plus result for a draw and then submit a new ticket into that same already-entered draw.

## Exact clique-partition model
Partition the 80 numbers into disjoint groups with sizes `g_1,...,g_k`, summing to 80.

For every group, buy **all** 3-subsets wholly inside that group, and buy no cross-group triple.

Portfolio cost:

`C = sum_i C(g_i,3)`.

If the actual 20-number Keno draw hits group `i` in `s_i` numbers, with `sum s_i=20`, then under the conditional free 2x table the group payout is:

`50*C(s_i,3) + 5*C(s_i,2)*(g_i-s_i)`.

So exact worst-case payout is found by dynamic programming over all feasible integer hit allocations `(s_1,...,s_k)` rather than by enumerating all `C(80,20)` physical draws.

A partition is strictly positive iff the DP minimum payout is greater than the portfolio cost.

## Exhaustive partition search
All nondecreasing integer partitions of 80 into exactly `k=1..8` positive group sizes were exhaustively screened.

Total clique partitions tested: **411,498**.

| groups k | partitions tested | positive partitions | cheapest positive construction | cost | worst gross | ratio |
|---:|---:|---:|---|---:|---:|---:|
| 1 | 1 | 1 | (80) | 82,160 | 114,000 | 138.7537% |
| 2 | 40 | 15 | (40,40) | 19,760 | 25,500 | 129.0486% |
| 3 | 533 | 57 | (26,27,27) | 8,450 | 10,170 | 120.3550% |
| 4 | 3,689 | 66 | **(20,20,20,20)** | **4,560** | **5,000** | **109.6491%** |
| 5 | 16,019 | 0 | best is (16,16,16,16,16) | 2,800 | 2,800 | 100.0000% |
| 6 | 49,342 | 0 | best ratio at (13,13,13,13,14,14) | 1,872 | 1,770 | 94.5513% |
| 7 | 116,742 | 0 | best ratio at (11,11,11,11,12,12,12) | 1,320 | 1,100 | 83.3333% |
| 8 | 225,132 | 0 | (10,10,10,10,10,10,10,10) | 960 | 780 | 81.2500% |

### Main mathematical result
Within this entire tested clique-partition family, **H173's 4×20 construction is the cheapest strict positive solution**.

No repartition into five through eight groups yields any strict positive cover at all. In particular, the aesthetically smaller 5×16 construction is exactly break-even, not positive.

This closes the obvious `just adjust the group sizes / use more groups` continuation. A smaller guaranteed portfolio, if it exists, must use a genuinely different combinatorial design — e.g. selective cross-group triples, cyclic blocks, covering designs, or another non-clique construction.

## Keno Plus timing test
Keno Plus is tempting because the multiplier is displayed **before** the corresponding Keno numbers are drawn. A 10x state would create huge conditional coverage margins.

But this does not currently produce an executable post-wheel arbitrage:
- the Plus wager must already be attached to the applicable Keno wager and costs the same as the base wager;
- the Plus wheel belongs to the `applicable Keno drawing` immediately following it;
- iLottery wagering is explicitly unavailable during the game's draw-break period;
- no official retail/online rule or interface was found allowing a player to wait for that draw's Plus wheel, then buy a fresh ticket into that same draw after the wheel result is known.

Therefore the project must treat the Plus multiplier as **unknown at commitment**, not as a pre-purchase state. Reopen only with direct official evidence that wagering for the same Keno draw remains open after its Plus result is displayed.

## What remains open
### Open mathematical branch
Find a family `F` of fewer than 4,560 triples such that, for every 20-number draw `S`,

`50*n3(S) + 5*n2(S) > |F|`,

where `n3` is the number of selected triples contained in `S` and `n2` the number intersecting `S` in exactly two points.

The exhaustive partition result says this family cannot be obtained merely by choosing all triples inside disjoint groups of up to eight groups.

### Open execution branch
Recover current 2026 `Kick Back with Keno` primary rules and current primary 3-spot paytable. If the live promotion is a free pre-locked 2x on every qualifying 3-spot ticket, solve throughput / ticket packing and tax before any SUCCESS claim.

## Result
- **411,498 clique partitions screened exactly.**
- **4×20 / 4,560 plays remains cheapest strict positive partition construction.**
- **No positive clique partition exists for k=5..8.**
- **Keno Plus post-wheel same-draw purchase exploit is not established; online draw-break rules point against it.**
- **Terminal SUCCESS: NO.**
