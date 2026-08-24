# H243 — Illinois Pick 3 / Pick 4 plus FIREBALL full-coverage upper bound

Date: 2026-08-24
Status: REJECTED for guaranteed-profit full coverage
Scope: lottery only

## Question
Illinois Lottery changed the plus FIREBALL prize schedule effective August 22, 2026. Does the stronger current add-on make exhaustive Straight coverage of Pick 3 or Pick 4 a deterministic positive-profit strategy?

## Current primary evidence
The Illinois Lottery results page states that plus FIREBALL prizes changed from August 22, 2026. The current official Game Rules prize tables show:

### Pick 3, $1 Straight
- base Straight prize: $500;
- plus FIREBALL Straight prize: $250;
- plus FIREBALL costs the same as the original wager, so a $1 line costs $2 with the add-on;
- plus FIREBALL adds one random digit and produces winning combinations by substituting that digit into player-number positions.

### Pick 4, $1 Straight
- base Straight prize: $5,000;
- plus FIREBALL Straight prize: $2,000;
- plus FIREBALL costs the same as the original wager, so a $1 line costs $2 with the add-on.

The current rules also explicitly permit the Lottery to restrict wagers on number combinations based on potential fixed-prize liability. That execution restriction is adverse, but it is not even needed for the mathematical rejection below.

## Exact dominant upper bound
For full Straight coverage, buy every ordered digit string once with plus FIREBALL.

### Pick 3
There are 10^3 = 1,000 Straight selections.

Spend:
`1,000 * $2 = $2,000`.

For any draw there is exactly one base Straight winner. A single Fireball digit can create no more than three position-substitution winning combinations. Grant the player the full listed plus FIREBALL prize for all three, even if the actual duplicate-combination accounting were less favorable.

Therefore a universal all-outcome gross upper bound is:
`$500 + 3*$250 = $1,250`.

Return upper bound:
`1,250 / 2,000 = 62.5%`.

Guaranteed net is at most `-$750` before tax/execution costs.

### Pick 4
There are 10^4 = 10,000 Straight selections.

Spend:
`10,000 * $2 = $20,000`.

There is exactly one base Straight winner. A single Fireball digit can create no more than four position-substitution winning combinations. Again grant the full plus FIREBALL Straight prize for all four.

Gross upper bound:
`$5,000 + 4*$2,000 = $13,000`.

Return upper bound:
`13,000 / 20,000 = 65.0%`.

Guaranteed net is at most `-$7,000` before tax/execution costs.

## Why this closes more than one draw realization
This is an outcome-independent upper bound. It does not rely on the Fireball value, repeated digits, popularity, or winner sharing. Any duplicate Fireball substitution can only reduce the count of distinct winning strings unless the rules pay multiple substitution-combination awards on one covered line; the bound already grants all positional awards, so it remains player-favorable.

Thus neither Pick 3 nor Pick 4 plus FIREBALL can support guaranteed positive profit by exhaustive Straight coverage under the current August 22, 2026 prize schedule.

## Verdict
**REJECTED.** Current plus FIREBALL is a genuine nonlinear random-number add-on, but even the most favorable all-position payout accounting yields only 62.5% (Pick 3) and 65.0% (Pick 4) of exhaustive Straight-cover spend. Wager-restriction authority can only worsen practical executability.

## Sources
- Illinois Lottery Pick 4 results page (current; notice of August 22 prize change): https://www.illinoislottery.com/dbg/results/pick4
- Illinois Department of Lottery current Game Rules PDF: https://mapp.illinoislottery.com/content/dam/il/illinois-lottery/GameRules.pdf
- Current Pick 4 Aug 22, 2026 result page confirming Fireball result structure: https://www.illinoislottery.com/dbg/results/pick4/draw/23996
