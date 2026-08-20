# H124 — Ohio MyLotto Rewards deterministic losing-ticket rebate screen

Updated: 2026-08-20
Status: **DETERMINISTIC LOTTERY-CREDIT REBATE VALIDATED / GUARANTEED-PROFIT COVERAGE REJECTED / CURRENT COUPON UPSIDE UNRESOLVED**

## Question
Can an official lottery loyalty program create a nonlinearity strong enough to turn an otherwise negative full/partition coverage into a strict guaranteed positive net return?

This is distinct from ordinary second-chance drawings: Ohio MyLotto Rewards awards deterministic points for eligible **non-winning** tickets, and those points can be redeemed for Lottery Cash or game-specific coupons.

## Current primary-source rules
Ohio Lottery currently states:
- non-winning Scratch-Offs earn **1 point per $1 ticket value**;
- non-winning Draw/online tickets earn **5 points per ticket regardless of ticket price**;
- ticket-entry earning is capped at **1,200 points per participant per month**;
- points themselves are non-cash and non-transferable;
- Lottery Cash and Coupons can be redeemed using points and used to buy Ohio Lottery products;
- the published FAQ gives prior Lottery Cash examples of **$5 for 400 points** and **$10 for 800 points** (same 80 points per $1 Lottery Cash conversion), while also warning that catalog pricing can change.

Sources:
- https://www.ohiolottery.com/mylotto-rewards/about-the-program
- https://www.ohiolottery.com/mylotto-rewards/help
- https://www.ohiolottery.com/mylotto-rewards/about-the-program/club-procedures
- https://www.ohiolottery.com/mylotto-rewards/redemption-central/coupons-and-lottery-cash/faq
- https://www.ohiolottery.com/mylotto-rewards/redemption-central/coupons-and-lottery-cash

## Deterministic rebate identity
At the documented 400 points -> $5 Lottery Cash example rate:

`credit_value_per_point = $5 / 400 = $0.0125`.

For a losing draw ticket:

`5 points -> $0.0625 face value of Lottery Cash`.

Therefore a $1 losing draw ticket has a nominal lottery-credit rebate of **6.25%**, before the monthly cap and before discounting Lottery Cash below cash value.

The reward is not paid on winning tickets, so for an all-outcome portfolio the deterministic reward can be computed from the exact number of losing tickets in each outcome whenever that count is fixed by symmetry/partition.

## Exact current coverage control — Ohio The Lucky One
Ohio Lottery currently publishes the following $1 payouts:
- Lucky Number: choose 1 of 36, win $24 if correct; official payout 66.7%.
- Odd/Even: win $1.50 at 1 in 2; official payout 75%.
- Low/High: win $1.50 at 1 in 2; official payout 75%.

Source:
- https://www.ohiolottery.com/games/the-lucky-one

### A. Cover all 36 Lucky Numbers
Buy one $1 Lucky Number ticket on every number 1–36.

Every legal outcome has exactly:
- 1 winner returning $24;
- 35 losers, each eligible for 5 reward points.

Spend:
`S = $36`.

Nominal reward points:
`35 * 5 = 175 points`.

At the documented 80-points-per-$1 Lottery Cash example:
`175 / 80 = $2.1875 Lottery Cash face value`.

Outcome-independent gross package value:
`$24 + $2.1875 = $26.1875`.

Gross ratio:
`26.1875 / 36 = 72.7431%`.

Thus the deterministic reward improves the base full-coverage return from 66.67% to about **72.74%**, but remains far below break-even.

### B. Cover Odd + Even
Buy $1 on Odd and $1 on Even.

Every outcome has:
- 1 winner returning $1.50;
- 1 loser earning 5 points = $0.0625 Lottery Cash face value at the example rate.

Spend: `$2`.
Package value: `$1.5625`.
Gross ratio: **78.125%**.

The same result applies to Low + High.

### C. Monthly cap
The 1,200-point monthly cap limits nominal Lottery Cash at the example rate to:

`1200 / 80 = $15` per month.

For large coverage portfolios, the effective rebate therefore collapses rapidly. As a deliberately favorable control, even a hypothetical $1,000 partition portfolio with a fixed $500 cash floor becomes only `$515/$1,000 = 51.5%` once the participant has hit the 1,200-point cap.

Without the cap, 999 losing $1 draw tickets would nominally generate 4,995 points = $62.4375 Lottery Cash, lifting that hypothetical 50% floor only to 56.24375% — still nowhere near a guarantee.

## Why this does not produce SUCCESS
1. The deterministic loyalty rebate is too small relative to lottery takeout in tested partition/coverage structures.
2. The **1,200 points/month** cap prevents scaling the rebate with a large full-space purchase.
3. Lottery Cash is restricted-use lottery credit, not cash; valuing it at face value is already player-favorable.
4. The published 400->5 / 800->10 point prices are examples of prior/current catalog offerings, not a contractual permanent conversion rate.
5. Game-specific Coupons may occasionally be priced more aggressively, but the public page says coupon prices change and the crawlable public catalog does not expose a currently guaranteed coupon deep enough to invert any tested coverage.

## General bound
For any coverage portfolio with cash floor `C`, spend `S`, fixed loser count `L`, draw-ticket points `p=5`, point-to-credit face value `v`, and monthly cap `M=1200`:

`guaranteed_package_floor <= C + min(L*p, M)*v`.

A strict lottery-credit package inversion would require:

`C + min(L*p, M)*v > S`.

For cash SUCCESS, the hurdle is stricter because restricted Lottery Cash must be valued below or equal to cash and then converted through another lottery wager with its own loss branch.

## Result
H124 validates a genuine deterministic lottery-subsidy mechanism but rejects it as a guaranteed-profit engine under the current published Ohio reward structure. It is useful as a small EV enhancer and as a general template for scanning loyalty programs, but it cannot rescue ordinary negative full-space/partition systems.

## Reopen conditions
Reopen only if an official lottery offers one of:
- uncapped reward credit large enough to exceed the exact coverage deficit;
- a fixed game coupon whose deterministic discount crosses the coverage break-even point;
- cash-equivalent rewards rather than restricted lottery credit;
- reward earning on **all** tickets (including winners) at a sufficiently high deterministic rate;
- a block-purchase promotion with a fixed added cash value per block.
