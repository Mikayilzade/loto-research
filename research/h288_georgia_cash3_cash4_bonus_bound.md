# H288 — Georgia Cash 3 / Cash 4 under current 50% iHOPE deposit bonus

## Question
Can the current Georgia Lottery Promotion 27012 (50% first-deposit bonus, up to $125) turn Cash 3 or Cash 4 fixed-pay portfolios into a strict guaranteed cash profit?

## Current external subsidy
The current Georgia Lottery promotions page states that eligible never-deposited iHOPE accounts receive a 50% bonus on the first qualifying deposit of at least $10, capped at $125. Both deposited and bonus funds are restricted to lottery purchases. A fully matched deposit therefore creates at most 1.5 units of playable balance per 1 unit of external cash deposited.

For a strict cash-profit construction, the checked wager family must therefore have a rigorous worst-case prize return strictly above 2/3 of stake.

Official source: https://www.galottery.com/en-us/player-zone/player-zone-promotions.html (Promotion ID 27012, expires 2026-09-15).

## Current fixed prize tables
Georgia Lottery's current Cash 3 and Cash 4 pages publish the online play types and fixed prize tables used below.

Sources:
- https://www.galottery.com/en-us/games/draw-games/cash-three.html
- https://www.galottery.com/en-us/games/draw-games/cash-four.html

Cash 3 includes Straight, Box, Straight/Box, Combo, 1-Off and Front/Back Pair. Cash 4 includes Straight, Box, Straight/Box, Combo and 1-Off.

## Exact average-return screen
For every primitive fixed-pay wager class, compute total prize liability across the complete equally likely result space and divide by total stake.

Cash 3:
- Straight: 50.00%
- 3-way / 6-way Box: 48.00%
- 3-way / 6-way Straight/Box: 49.00%
- Combo: 50.00%
- Front/Back Pair: 50.00%
- 1-Off: `(250 + 6*24 + 12*4 + 8*8) / 1000 = 50.60%`

Cash 4:
- Straight: 50.00%
- every published Box class: 48.00%
- every published Straight/Box class: 49.00%
- every published Combo class: 50.00%
- 1-Off: `(2500 + 8*124 + 24*24 + 32*14 + 16*32) / 10000 = 50.28%`

Thus the best checked primitive is Cash 3 1-Off at exactly 50.60% average gross.

## Portfolio-wide impossibility bound
Any nonnegative additive portfolio of these wagers has an average gross/stake ratio no larger than the best primitive ratio, 50.60%. For every finite portfolio,

`minimum legal-outcome gross <= average legal-outcome gross`.

Even granting the full deterministic 50% deposit bonus to every dollar of spend, the strongest possible checked upper bound relative to external deposited cash is therefore:

`1.5 * 0.506 = 0.759 = 75.90%`.

Cash 4 is lower: `1.5 * 0.5028 = 75.42%`.

So at least one legal draw outcome leaves the player below deposited cash for every nonnegative additive portfolio formed from the checked Cash 3 / Cash 4 fixed-pay wager classes. This rejects the mechanism without needing execution/cart limits, number-liability cutoffs, taxes, or withdrawal friction.

## Result
**CLOSED / REJECTED for the checked mechanism.** The current 50% Georgia iHOPE subsidy is far too small for Cash 3 / Cash 4: the best portfolio-wide cash-recovery upper bound is 75.90% of deposited cash.

Reopen only if the deterministic subsidy rises above approximately `1/0.506 - 1 = 97.6285%` of deposited cash, or the fixed paytable materially improves.
