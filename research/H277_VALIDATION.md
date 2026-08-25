# H277 validation certificate — Millionaire for Life

Validated 2026-08-26 against current 2026 game material.

## Inputs

- Matrix: choose 5 of 58 white balls and 1 of 5 Millionaire Balls.
- Price: $5 per play.
- Published top cash option: $18,000,000.
- Published second-prize cash option: $2,200,000.
- Fixed lower prizes used: $7,500 / $500 / $250 / $50 / $25 / $8 / $8.
- Official rules state the top two levels can be pari-mutuel, so treating their published cash options as fixed and undiluted is a strict player-favourable upper model.

Primary/current sources:
- https://www.powerball.com/millionaire-for-life
- https://cdnprodpaasmedia-valottery-com.azureedge.net/-/media/images/game-rules/2026/millionaire-for-life-197-2025.pdf
- https://mobile.masslottery.com/games/draw-and-instants/millionaire-for-life

## Exact checks

`C(58,5) * 5 = 22,910,580` legal plays / draw outcomes.

The hypergeometric match multiplicities for one complete cover sum exactly to **22,910,580**.

At $5 each:
- cover cost = **$114,552,900**;
- dominating no-sharing gross = **$60,584,320**;
- return = **52.88763531957724%**;
- deficit = **$53,968,580**.

The stored script asserts the exact universe, cost, gross, and sub-100% ratio.

## Guarantee proof gate

For any fixed ticket, the legal draw space acts symmetrically, so its average gross under the dominating payout table is identical to every other legal ticket. A nonnegative portfolio is a linear combination of tickets, hence its average gross/cost ratio is also exactly 52.88763531957724%.

For any finite outcome set, minimum gross is no larger than average gross. Therefore every nonempty paid portfolio has at least one legal draw outcome whose gross is below its cost. Strict guaranteed profit is impossible in the dominating model, and a fortiori impossible under the actual top-tier pari-mutuel rules.

## Verdict

**H277 CLOSED / REJECTED.** This is a portfolio-wide impossibility result for ordinary current Millionaire for Life tickets, not merely a losing full-cover example.
