# H261 — Hospital Research Foundation capped-raffle full-buyout screen

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: **REJECTED as a guaranteed-profit complete-issuance takeover**

## Question
Can a current raffle with a hard maximum ticket count and bulk-ticket discounts become a strict guaranteed-profit strategy by acquiring the entire issuance, thereby owning every possible winning identifier?

This is the clean finite-identifier version of the H019 takeover idea: unlike ordinary draw lotteries, complete ownership of a capped raffle issuance eliminates draw randomness and external prize sharing. If total guaranteed prize value exceeds the minimum exact cost of owning every ticket, the construction could in principle create an all-outcome floor.

## Current primary evidence
Official Hospital Research Foundation Group terms:
https://www.homelottery.com.au/terms-and-conditions.html

The current `2026 No 3` terms state:

### Home Lottery — Licence M15011
- maximum **170,000** tickets;
- ticket prices: $100 single, 3 for $250, 5 for $375, 10 for $700;
- **4,010 prizes**;
- total retail value of all prizes approximately **A$6,260,851.86**;
- draws use an RNG and a winning ticket remains eligible for later draws.

### Cash Calendar — Licence M15012
- maximum **146,888** tickets;
- prices: $25 single, 5 for $60, 8 for $85, 12 for $110;
- five cash draws: one A$300,000 and four A$25,000 prizes;
- total fixed cash = **A$400,000**;
- winning ticket numbers remain eligible for later draws.

### Holiday for Life — Licence M15013
- maximum **239,778** tickets;
- prices: $15 single, 5 for $30, 15 for $55, 30 for $80;
- one prize with an immediate cash alternative of **A$240,000**.

The published `Super Pack` and `Max Pack` prices equal the sum of the corresponding best component packs; they create no extra cross-product discount.

## Exact minimum full-issuance acquisition costs
For each raffle, solve the unbounded integer pack problem exactly: choose nonnegative counts of allowed package sizes summing to the hard ticket cap while minimizing total purchase cost.

### Home Lottery
170,000 is divisible by 10, so the cheapest exact cover is 17,000 ten-packs:

`cost = 17,000 * A$700 = A$11,900,000`.

Even valuing every physical/noncash prize at the operator's full stated retail value:

`return <= 6,260,851.86 / 11,900,000 = 52.6122005%`.

Deterministic deficit:

`A$5,639,148.14`.

A universal deterministic discount would need to exceed **47.3878%** merely to reach nominal retail-value break-even, before tax, transfer, transport, foreign-ownership, execution or valuation haircuts.

As an extra robustness check, even if the separately described A$87,986 Membership Draw were added *again* on top of the stated all-prize total, the impossible-favorable return would still be only about **53.3516%**.

### Cash Calendar
Exact cheapest pack decomposition for 146,888 tickets:
- 12,240 twelve-packs = 146,880 tickets for A$1,346,400;
- one eight-pack = 8 tickets for A$85.

Total exact cost:

`A$1,346,485`.

Owning every issued ticket guarantees all five cash prizes even if the same ticket wins more than once, because winning tickets remain eligible for subsequent draws.

Guaranteed prize mass:

`A$300,000 + 4*A$25,000 = A$400,000`.

Return:

`29.7069778%`.

Deterministic deficit:

`A$946,485`.

Required universal discount for break-even: **70.2930%**.

### Holiday for Life
Exact minimum package cost for 239,778 tickets is **A$639,460**. One optimal decomposition is:
- 7,992 thirty-packs = 239,760 tickets for A$639,360;
- one 15-pack + three singles = 18 tickets for A$100.

The immediate-cash alternative is A$240,000, so complete ownership yields at most:

`240,000 / 639,460 = 37.5316673%`.

Deterministic deficit:

`A$399,460`.

Required universal discount for break-even: **62.4683%**.

## Combined takeover
Even granting perfect full ownership of all three maximum issuances simultaneously:

- total acquisition cost: **A$13,885,945**;
- total stated/guaranteed prize value used here: **A$6,900,851.86**;
- gross return: **49.6966671%**;
- deterministic deficit: **A$6,985,093.14**.

No cross-raffle package creates a better rate than the individual cheapest packs, so combination does not rescue the construction.

## Execution note
At the current checkpoint ticket sales have already been open since 2026-07-20, so a literal complete-issuance takeover is not presently available if any identifiers were already sold to others. This is not needed for rejection: H261 grants the player the impossible stronger condition of owning the entire maximum issuance from inception and still obtains a large loss.

## Conclusion
**REJECTED.** These current hard-capped raffles validate the finite-ticket takeover mechanism structurally, but not economically. Even impossible-perfect ownership of every issued identifier at the best published bulk prices yields only **52.6122%**, **29.7070%**, and **37.5317%** respectively.

This closes the current Hospital Research Foundation 2026 No 3 capped-raffle family for strict guaranteed profit. Reopen only if a capped raffle has prize mass above exact full-issuance acquisition cost, or a deterministic player-eligible subsidy/discount large enough to cross the exact deficit.

Reproduction:
- `src/loto_research/h261_capped_raffle_buyout.py`
- `data/derived/h261_capped_raffle_buyout.json`
