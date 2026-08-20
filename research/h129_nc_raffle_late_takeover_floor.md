# H129 — fixed-board raffle late-takeover floor / North Carolina Celebrate America 2026

Updated: 2026-08-20
Status: **NEW DETERMINISTIC TAKEOVER THEOREM VALIDATED / NC CASE REJECTED / MONITOR UPGRADED**

## Question
H122-H128 showed that deadline raffles can become strongly +EV when sales are weak, but incomplete ownership retains a zero-payout branch. A possible escape is to buy **all tickets still unsold** late in the sales period. Can that convert an undersubscribed raffle into a strict guaranteed-profit position?

## General theorem
Consider a fixed-board raffle with:
- ticket cap `C`;
- ticket price `p`;
- fixed prize values sorted descending `v1 >= v2 >= ... >= vW`;
- `E` tickets already sold to external players;
- buyer purchases every remaining ticket `R=C-E`.

Because winners are drawn from sold tickets and an external ticket cannot occupy more than one winning slot in an ordinary without-replacement raffle, a worst-case outcome can allocate the **E highest-value prize slots** to external holders. The buyer's deterministic prize floor is therefore

`G(E) = max(0, sum(v_i) - sum_{i=1}^{min(E,W)} v_i)`.

The all-remaining takeover cost is

`K(E) = (C-E)*p`.

Strict guaranteed profit requires

`G(E) > K(E) + all taxes/fees/execution costs`.

Immediate corollary: if `E >= W`, the strict takeover floor is **zero**, no matter how attractive expected value becomes.

This is stronger than the earlier generic “external winners can take all prizes” argument because it quantifies the exact deterministic floor before that zero-floor threshold.

Implementation: `src/loto_research/raffle_takeover_floor.py`.

## North Carolina Celebrate America Raffle 2026 — primary facts
NC Education Lottery's 2026 Celebrate America Raffle had:
- maximum **25,000** tickets;
- price **$10**;
- **20 × $2,500** prizes;
- **250 × $250** prizes;
- **2,000 × $25** prizes;
- total fixed cash board **$162,500** across **2,270** winning tickets;
- sales ending when all tickets sold or at the fixed July 30, 2026 deadline;
- no limit on total raffle tickets a player may purchase (250 per cart, unlimited repeated carts);
- the raffle page exposed the number of remaining tickets during sales.

Primary sources:
- NCEL raffle announcement: https://nclottery.com/NewsBlogDetails/2026/5/26/Celebrate-America-with-a-new-limited-edition-raffle
- NCEL raffle page: https://nclottery.com/raffle
- NCEL raffle FAQ: https://nclottery.com/FAQGames
- NCEL rules index: https://nclottery.com/Rules

This is an unusually good architecture for testing the theorem because the board is all cash, ticket supply is small, purchase quantity is not globally capped, and remaining inventory is observable.

## Exact deterministic takeover screen
At `E=0`, buying the entire game costs **$250,000** and guarantees the full **$162,500** board: only **65.0% gross**.

As external ownership increases, the cost falls slowly but the worst-case prize floor falls faster because external players can consume the highest-value slots first.

Selected exact states:

| External tickets E | Remaining bought | Guaranteed prize floor | Cost | Strict gross floor |
|---:|---:|---:|---:|---:|
| 0 | 25,000 | $162,500 | $250,000 | **65.0000%** |
| 1 | 24,999 | $160,000 | $249,990 | **64.0026%** |
| 20 | 24,980 | $112,500 | $249,800 | **45.0360%** |
| 21 | 24,979 | $112,250 | $249,790 | **44.9377%** |
| 270 | 24,730 | $50,000 | $247,300 | **20.2184%** |
| 1,000 | 24,000 | $31,750 | $240,000 | **13.2292%** |
| 2,000 | 23,000 | $6,750 | $230,000 | **2.9348%** |
| 2,269 | 22,731 | $25 | $227,310 | **0.0110%** |
| 2,270 | 22,730 | $0 | $227,300 | **0%** |

The maximum strict gross floor over every `E in [0, 2,270]` occurs at launch: **65%**. There is therefore no late point at which buying all unsold tickets turns this raffle into guaranteed profit. Once 2,270 external tickets exist, the deterministic floor becomes zero permanently.

## Expected-value threshold is different
The total fixed board is $162,500, so a randomly held ticket becomes positive pre-tax EV whenever the final sold denominator is below

`N* = 162,500 / 10 = 16,250 tickets`.

Thus this product could have become a **strong +EV undersubscription** if sales finished below 16,250, while still failing guaranteed-profit takeover. This cleanly separates two conditions:
- **+EV threshold:** final denominator `<16,250`;
- **strict all-remaining takeover:** never profitable under the published board, even with zero prior external tickets.

The current public search did not yield a reliable official final sold count/results denominator, so no claim is made about whether the historical 2026 draw actually crossed the +EV threshold.

## Reusable monitor upgrade
For every fixed-board raffle, track both:

1. **EV overlay metric**
   `board / expected_or_bounded_final_sales / ticket_price`.

2. **all-remaining deterministic floor**
   `G(E) / ((C-E)*p)`, where `G(E)` subtracts the E highest prize slots from the board.

This identifies prize-board inversions that an EV-only monitor can miss. A terminal candidate would require some observable `E` such that the residual worst-case board exceeds the cost of all remaining tickets after tax/fees.

The most promising architectures are therefore not merely undersubscribed raffles, but raffles with one or more of:
- a very large count of fixed prize slots relative to ticket cap;
- relatively flat prize values, so external tickets cannot strip most board value by taking only a few top slots;
- operator-funded board larger than total possible ticket revenue;
- deterministic minimum allocation per purchased block / tranche;
- ring-fenced prize pools whose winner count exceeds external ownership in that pool.

## Result
H129 validates a new exact **late-takeover deterministic-floor theorem** and closes the North Carolina Celebrate America 2026 product as a guarantee. The game is a useful monitor prototype because remaining tickets were publicly visible and unlimited repeated purchases were permitted, but its best possible strict full-takeover floor was only **65%**.

No terminal SUCCESS.
