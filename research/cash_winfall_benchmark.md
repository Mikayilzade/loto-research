# Cash WinFall — historical positive-EV benchmark

Updated: 2026-08-11
Status: **historical mechanism confirmed; draw-level benchmark reproduced from secondary historical payout data**

## Why this case matters
Cash WinFall is the benchmark for this project because it demonstrates the exact kind of edge we are looking for: not predicting random numbers, but identifying a rule/state in which prize redistribution changes the expected value of a ticket.

The game is discontinued. The purpose here is methodological: reconstruct a proven structural edge, then search current games for analogous mechanisms.

## Source hierarchy
### Primary archival metadata
Massachusetts State Library archive:
https://archives.lib.state.ma.us/entities/publication/e47fb189-7c00-4409-887a-d7d37e7144af

This archive item is a Massachusetts Treasury response/comment concerning the Inspector General report. Its PDF has not yet been ingested into this repository, so no content claim below is presented as if we had fully parsed that PDF.

### Report-derived historical account
The Tech published material from the Inspector General report:
https://thetech.com/2012/08/01/cashwinfall-mit-v132-n30

Key historical points in that account:
- James Harvey identified the roll-down feature while studying lottery economics;
- a Lottery technical discussion supported his conclusion that during a roll-down a ticket could be worth more than its purchase price;
- an early 2005 MIT pool turned about $1,000 of tickets into about $3,000 in one roll-down;
- the group later scaled into hundreds of thousands of tickets;
- the number of tickets and portfolio construction mattered because large-scale execution and coverage affected realised risk;
- the Inspector General estimate quoted there put MIT-group pre-tax profit at at least $3.5 million over its participation.

### Historical payout snapshot
A contemporaneous Hacker News discussion preserved the May 9, 2011 payout amounts while linking to the then-live Massachusetts Lottery page:
https://news.ycombinator.com/item?id=2829241

Treat these exact draw-level values as secondary historical data until independently archived from a primary record.

The preserved values for the May 9, 2011 roll-down were:
- 5 matches: $24,821
- 4 matches: $824
- 3 matches: $26

## Exact 6/46 probabilities
For a ticket selecting 6 numbers from 46 and a draw of 6 from 46:

| Matches | Probability | Approx. 1 in N |
|---:|---:|---:|
| 0 | 0.4097847946031625 | 2.4403 |
| 1 | 0.4214929315918243 | 2.3725 |
| 2 | 0.1463517123582723 | 6.8329 |
| 3 | 0.0210957423219131 | 47.4029 |
| 4 | 0.0012490900059028 | 800.5828 |
| 5 | 0.0000256223590954 | 39,028.4125 |
| 6 | 0.0000001067598296 | 9,366,819 |

## Conservative May 9, 2011 roll-down EV
Ticket price: **$2**.

Use only the three preserved **cash** payout tiers and deliberately assign zero economic value to the 2-match free-bet prize. This avoids overstating EV by treating a free future ticket as $2 cash.

Expected cash payout:

`P(5)*24821 + P(4)*824 + P(3)*26`

= **$2.2137120403** per $2 ticket.

Therefore:
- conservative net EV = **+$0.2137120403** per ticket;
- conservative ROI = **+10.6856%** before taxes and execution costs;
- free-bet value, if modelled correctly, would add some additional economic value rather than reduce this result.

This benchmark is robust to the free-bet valuation issue because the cash-only tiers already exceed ticket cost in expectation.

## Important distinction: positive EV is not guaranteed profit on one ticket
A single $2 ticket still has a high probability of losing. The edge becomes economically useful only across a sufficiently large, well-distributed portfolio, subject to execution capacity and the possibility that a 6/6 jackpot winner interrupts the intended roll-down economics.

The Inspector-General-derived account explicitly describes large players varying volume based on:
- the amount needed to reach the roll-down trigger;
- expected betting by other groups;
- execution conditions;
- portfolio distribution across possible outcomes.

This is the blueprint for our own modelling: **state + crowd + portfolio + execution**, not only per-ticket EV.

## Normal-state comparison
Historical descriptions place the ordinary lower prizes at much smaller levels than roll-down payouts. The exact normal-state rule version still needs primary-source archival reconstruction before it is locked into the dataset.

The central finding does not depend on guessing a normal payout table: the May 9 cash-only roll-down snapshot itself is enough to demonstrate positive expected value under the documented 6/46 probabilities and $2 price, assuming the preserved payout data are accurate.

## Lessons to transfer to current lotteries
1. Search for **forced redistribution**, not number patterns.
2. Model prize value using the state visible **before purchase**.
3. Estimate crowding because other sophisticated bettors can arbitrage away an edge.
4. Large-volume portfolios need their own risk model; expected value alone is insufficient.
5. Execution limits, ticket throughput, taxes and redemption mechanics can turn theoretical +EV into practical -EV.
6. A state-dependent strategy must be forward-testable: the profitable condition must be observable before the draw.

## Project status
Cash WinFall upgrades H001 from a purely theoretical hypothesis to a **historically validated mechanism class**. It does not prove that any current game is exploitable.
