# H239 — Deterministic Keno Bonus Hours full-coverage closure

Date: 2026-08-24
Status: NOT SUCCESS
Scope: lottery-only

## Question
Can deterministic time-window promotions that increase every qualifying Keno win turn exact full 3-spot coverage into a guaranteed positive-profit strategy?

## Exact common 3-spot combinatorics
For a standard 20-of-80 Keno draw and the portfolio containing every 3-subset once:

- total lines: C(80,3) = 82,160;
- 0 matches: C(20,0)C(60,3) = 34,220;
- 1 match: C(20,1)C(60,2) = 35,400;
- 2 matches: C(20,2)C(60,1) = 11,400;
- 3 matches: C(20,3) = 1,140.

These counts are outcome-independent, so any fixed prize table gives a deterministic full-space gross before execution constraints.

## Georgia KENO! Bonus Hours — +30%
Official Georgia Lottery promotion rules for June 15–July 15, 2026 state that winning KENO! tickets purchased during the specified Bonus Hours receive a **30% higher payout than the standard payout**, at retail or online. The current Georgia KENO page lists the base 3-spot table as:

- match 3: $25;
- match 2: $2;
- match 1/0: $0.

At a $1 base wager per line:

- full-space spend = 82,160 × $1 = **$82,160**;
- standard deterministic gross = 11,400×$2 + 1,140×$25 = **$51,300**;
- with guaranteed +30% Bonus Hours uplift = **$66,690**;
- deterministic net = **-$15,470**;
- gross return = **81.170886%**.

Therefore even if all 82,160 distinct 3-spot wagers could be lawfully executed inside one qualifying Bonus Hours window, the guaranteed payout uplift is insufficient. Execution limits can only worsen practical feasibility; they are not needed for the mathematical rejection.

## North Carolina Keno Bonus Hours — +50% with Multiplier
Official NC Education Lottery material for June–July 2026 states that during Friday Bonus Hours (4–6 p.m.), a winning Keno ticket receives **50% more prize money when the Multiplier is added**. Adding the Multiplier doubles the base ticket cost. The current NC Keno 3-spot table is:

- match 3: $27;
- match 2: $2;
- match 1/0: $0.

The current NC page also states that the Multiplier can yield no enhancement below 2X (overall odds of receiving 2X or higher are 1 in 1.67), so a strict guarantee must include the lowest multiplier branch. Using the most favorable interpretation for the player that the +50% promotional uplift applies to every winning prize in that branch:

- base full-space deterministic gross = 11,400×$2 + 1,140×$27 = **$53,580**;
- worst-branch Bonus Hours gross at +50% = **$80,370**;
- Multiplier-required spend = 82,160×$2 = **$164,320**;
- deterministic net = **-$83,950**;
- gross return = **48.910662%**.

Even granting the full +50% uplift on the lowest multiplier branch, the portfolio is far below break-even. Thus this promotion cannot create a guaranteed-profit full-coverage strategy.

## General implication
A deterministic time-window uplift is a genuine nonlinear/overlay mechanism and therefore deserves separate treatment from ordinary negative-EV Keno. But for exact full 3-spot coverage the uplift must exceed the takeout gap after any mandatory add-on cost.

For Georgia's current 3-spot base table, the required multiplicative uplift on all winning payouts is:

`82,160 / 51,300 = 1.601559...`, i.e. **more than +60.1559%**.

Georgia's +30% window is below this threshold.

For NC when the Multiplier doubles ticket cost, the required guaranteed total uplift over the base-table deterministic gross is:

`164,320 / 53,580 = 3.066816...`, i.e. **more than +206.6816%** relative to base-table payouts in the worst multiplier branch.

The +50% Bonus Hours overlay is nowhere close.

## Verdict
**REJECTED for guaranteed-profit full 3-spot coverage.** Two real operator-run deterministic payout-uplift promotions were tested exactly. Georgia +30% remains at 81.17% deterministic gross return; NC +50% with mandatory Multiplier remains at 48.91% in the guarantee-relevant lowest multiplier branch.

This closes these historical Bonus Hours instances and establishes reusable threshold logic for future deterministic Keno payout-uplift promotions. Reopen only if a future promotion exceeds the game-specific exact full-coverage threshold and execution/caps/taxes remain compatible.

## Primary sources
- Georgia Lottery, Keno! Bonus Hours June and July (2026): https://www.galottery.com/en-us/promotions/2026/June/KenoBonusHoursJuneJuly.html
- Georgia Lottery, current KENO! game / odds & prizes: https://www.galottery.com/en-us/games/draw-games/keno.html
- NC Education Lottery, Keno Bonus Hours announcement (2026-06-05): https://nclottery.com/NewsBlogDetails/2026/6/5/Enjoy-a-bonus-month-of-Keno-Bonus-Hours-/
- NC Education Lottery, current Keno How to Play / prize table: https://nclottery.com/keno-how-to-play
