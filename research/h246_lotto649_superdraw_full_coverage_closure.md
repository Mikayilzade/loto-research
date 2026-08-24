# H246 — LOTTO 6/49 SuperDraw 2026 full-coverage closure

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: REJECTED for strict guaranteed-profit full coverage

## Current promotion
The official/authorized Canadian lottery material for the Saturday, 2026-08-29 LOTTO 6/49 SuperDraw states that a normal $3 play receives the usual Classic Draw and Gold Ball Draw entries plus **20 additional guaranteed winners of $40,000 each**, at no extra ticket price. The additional SuperDraw winners are drawn from Gold Ball Draw numbers actually issued for that draw.

This is a real deterministic subsidy to the draw-level prize pool: CAD 800,000 of extra guaranteed prizes is added without increasing the $3 play price. It is therefore a valid lottery-overlay candidate.

## Full Classic combination coverage
Classic state space:

- `C(49,6) = 13,983,816` selections
- cost at $3 each = `CAD 41,951,448`

For any realized 6-number draw plus one bonus number, exact counts inside full Classic coverage are:

- 6/6: 1
- 5/6 + Bonus: 6
- 5/6: 252
- 4/6: 13,545
- 3/6: 246,820
- 2/6 + Bonus: 172,200
- 2/6: 1,678,950

Current fixed lower prizes are $10 for 3/6, $5 for 2/6+Bonus and a $3 Free Play for 2/6.

Thus immediate fixed cash from 3/6 and 2/6+Bonus is:

`246,820*10 + 172,200*5 = CAD 3,329,200`.

The 2/6 tier yields 1,678,950 Free Plays. For an intentionally favorable upper-bound comparison, H246 values every Free Play at its full $3 face value, adding `CAD 5,036,850`, even though a Free Play is not equivalent to guaranteed withdrawable cash and can itself lose.

## Favorable isolated-pool stress test
Current authorized prize information states:

- Prize Fund = 18.33% of cash sales (plus the specified accounting amount for redeemed Free Plays);
- fixed lower categories are paid first, with the remaining amount forming the Pools Fund for 5/6+B, 5/6 and 4/6;
- Classic Jackpot = CAD 5,000,000;
- Gold Ball prize is at least CAD 1,000,000 when a white ball is drawn;
- the Aug. 29 SuperDraw adds 20 × CAD 40,000 = CAD 800,000.

To avoid understating the candidate, consider an isolated-ticket stress test that gives the covering player every favorable ownership benefit:

1. no external tickets compete for Classic pooled tiers;
2. the player receives the entire residual Pools Fund;
3. the player receives the full CAD 5m Classic Jackpot;
4. a white-ball Gold Ball result pays CAD 1m to one of the player's issued entries;
5. all 20 extra CAD 40k SuperDraw prizes are awarded to the player's issued entries;
6. every 2/6 Free Play is valued at full $3 face value;
7. when computing the residual Pools Fund, H246 conservatively subtracts only the fixed **cash** tiers from the 18.33% Prize Fund, not the Free Play liability, making the assumed pool larger and therefore more favorable to the strategy.

On only the covering player's CAD 41,951,448 cash sales:

- 18.33% Prize Fund = `CAD 7,689,700.4184`
- favorable residual Pools Fund upper bound = `7,689,700.4184 - 3,329,200 = CAD 4,360,500.4184`

Total favorable value under this constructed branch:

- fixed cash = CAD 3,329,200
- favorable entire Pools Fund = CAD 4,360,500.4184
- Classic Jackpot = CAD 5,000,000
- minimum Gold Ball white-ball prize = CAD 1,000,000
- all 20 SuperDraw prizes = CAD 800,000
- all Free Plays at face value = CAD 5,036,850

Total = `CAD 19,526,550.4184`.

Against spend `CAD 41,951,448`, this is only **46.5456%** of cost, a deficit of **CAD 22,424,897.5816**.

This stress test is deliberately more generous than a strict cash guarantee because it values non-cash Free Plays at face and gives the player all pooled and all additional winners in an isolated-sales branch.

## Why external sales cannot create a strict guarantee
External sales can enlarge the Prize/Draw Funds, but they also create uncontrolled competing winning selections and additional issued Gold Ball/SuperDraw numbers. The player has no pre-draw hard cap on external issued entries or on duplicate Classic winners. Therefore any hoped-for benefit from external sales is not a guaranteed floor: pooled categories and the Classic Jackpot are share-sensitive, while the Gold Ball and 20 SuperDraw numbers are drawn from all issued entries.

A strict guaranteed-profit strategy must survive all allowed crowd/composition branches rather than assume that external sales contribute money while producing no competing winners.

## Verdict
**REJECTED.** The Aug. 29, 2026 SuperDraw is a genuine current free lottery subsidy worth CAD 800,000 in extra guaranteed prizes, but it is far too small to rescue full 6/49 coverage. Even a deliberately favorable isolated-pool model that grants the covering player the entire pool, jackpot, all 20 extra prizes, the minimum Gold Ball prize and full face value for every Free Play returns only **46.5456%** of spend. External-ticket composition remains uncontrolled and cannot supply a strict guaranteed floor.

## Sources
- PlayNow Manitoba, current LOTTO 6/49 SuperDraw Aug. 29, 2026 page: https://www.playnow.com/mb/lottery/promotions/649-super-draw/
- WCLC, current LOTTO 6/49 prize structure: https://www.wclc.com/games/lotto-649.htm
- PlayNow Manitoba, current LOTTO 6/49 game page: https://www.playnow.com/mb/lottery/lotto-649/
- Atlantic Lottery, current LOTTO 6/49 prize-fund allocation description: https://corp.alc.ca/content/alc/en/our-games/lotto/lotto-6-49.html
