# H242 — Michigan Club Keno Tripler Time: random-entitlement guarantee gate

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: NOT SUCCESS; active promotion mathematically strong but entitlement is not guaranteed

## Current primary evidence
Michigan Lottery announced on 2026-07-30 that Club Keno tickets purchased at retailers beginning 2026-08-01 are eligible for the August `Tripler Time` promotion at no additional cost. A ticket that receives a printed **Doubler** or **Tripler** message has eligible Club Keno, Plus 3 and Kicker winnings multiplied 2x or 3x, subject to the stated $4 million maximum. Multi-draw tickets preserve the message across all eligible drawings on that ticket. The Jack is excluded.

The same official announcement explicitly frames the multiplier as conditional on **receiving** a Doubler or Tripler message; receiving such a message alone is not itself a win. It does not state that every ticket receives a multiplier message, nor a deterministic player-selectable way to obtain one.

Official current Michigan Lottery help establishes ordinary Club Keno as 20 numbers drawn from 80, spot sizes 1–10, $1 minimum wager, up to 60 consecutive draws per ticket, and in-store purchase. Current Kicker is separately random and costs an additional base wager; it is not used in this H242 base-game screen.

## Exact full-coverage mathematics
For a fixed k-spot ticket, full coverage contains `C(80,k)` distinct selections. For a draw with 20 winners and 60 losers, exactly

`C(20,h) * C(60,k-h)`

of those selections hit exactly `h` numbers. Therefore deterministic full-coverage gross at $1 per line is the sum of that count times the current base prize for each paying hit tier.

Using the current Michigan Club Keno base prize table reproduced in the official game guide / current help-linked materials, the exact base returns are:

| spot | base full-cover return | hypothetical universal 2x | hypothetical universal 3x |
|---:|---:|---:|---:|
| 1 | 50.0000% | 100.0000% | 150.0000% |
| 2 | 66.1392% | 132.2785% | 198.4177% |
| 3 | 65.2142% | 130.4284% | 195.6426% |
| 4 | 64.9439% | 129.8878% | 194.8318% |
| 5 | 64.9951% | 129.9903% | 194.9854% |
| 6 | 64.7920% | 129.5840% | 194.3759% |
| 7 | 65.2984% | 130.5969% | 195.8953% |
| 8 | 64.7475% | 129.4950% | 194.2425% |
| 9 | 64.8069% | 129.6137% | 194.4206% |
| 10 | 52.9653% | 105.9305% | 158.8958% |

This is an important positive finding about mechanism strength: if a free Doubler entitlement were guaranteed for every line, full coverage would be strictly profitable for spots 2–10; a universal Tripler would also make 1-spot profitable. For example, exact 3-spot full coverage costs $82,160 and returns $53,580 base, $107,160 under universal 2x, or $160,740 under universal 3x.

At $1 wager the stated $4 million promotional maximum does not bind any individual base prize, so it does not alter these particular full-coverage upper-bound calculations.

## Why the current promotion still does not create a guaranteed strategy
The promotion's multiplier is a **ticket-level random entitlement**, not a deterministic purchase-time overlay applying to every qualifying ticket. For strict guarantee analysis, any finite acquisition strategy must include the legal branch in which required tickets fail to receive the necessary Doubler/Tripler messages unless the rules establish a deterministic quota/floor or the player can lawfully reject/refund untagged tickets after observing the message.

No current primary source located in this run establishes either:

1. a minimum guaranteed number/fraction of Doubler or Tripler tickets for a purchaser; or
2. a lawful post-print cancellation/refund right that lets the player inspect the message and keep only tagged tickets.

The official how-to flow instead describes taking the playslip to the retailer, paying, and receiving the printed ticket. This is insufficient to support a selective-acquisition arbitrage.

Thus the active promotion is **not rejected as weak**; it is rejected as a strict guarantee because the economically valuable entitlement cannot be guaranteed across the required coverage set.

## Reopen conditions
Reopen immediately on materially new primary evidence showing any of:
- a deterministic ticket-tag allocation rule or hard minimum multiplier frequency;
- a lawful, non-discretionary cancellation/refund mechanism after the multiplier message is observable and before any draw;
- a retailer/terminal batching feature that guarantees every line on a tagged ticket can cover the necessary full combination space without losing the entitlement;
- another current Michigan promotion that applies a deterministic free >=2x multiplier to every qualifying Club Keno ticket.

## Verdict
**NOT SUCCESS.** August 2026 Michigan Tripler Time is one of the strongest current lottery overlays found: a free universal Doubler would mathematically clear full-coverage break-even for spots 2–10. But the current multiplier is randomly printed on tickets, so no strict all-outcome profit guarantee follows without a guaranteed entitlement-acquisition mechanism.

## Sources
- Michigan Lottery Connect, 2026-07-30, `Club Keno Tripler Time Gives Players a Chance to Double and Triple Their Winnings`: https://milotteryconnect.com/2026/07/30/club-keno-tripler-time-gives-players-a-chance-to-double-and-triple-their-winnings-13/
- Michigan Lottery Help, current `How to Play Club Keno`: https://help.michiganlottery.com/support/solutions/articles/158000441486-how-to-play-club-keno
- Michigan Lottery Help, current `Club Keno Add-Ons`: https://help.michiganlottery.com/support/solutions/articles/158000441485-club-keno-add-ons
- Michigan Lottery game guide / Plus 3 prize-table material: https://assets.ctfassets.net/d6o62jwe1jlr/3e5AHjImwEBygprYXeX71y/d21dc23143b9000193c1bcb740a868d1/January_2025_GL_single_page_format_v2.pdf
