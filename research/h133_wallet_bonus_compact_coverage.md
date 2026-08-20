# H133 — current lottery-wallet bonus + compact fixed-coverage screen

Updated: 2026-08-20
Status: **DETERMINISTIC WALLET SUBSIDY VALIDATED / CURRENT COMPACT COVERAGE STILL NEGATIVE / NO SUCCESS**

## Goal
Combine H132's player-owned subsidy idea with current lottery-wallet promotions and fixed/non-shareable games, prioritizing cases where a capped bonus could lower the external-cash cost of a complete coverage below the deterministic payout floor.

## General threshold
For a complete coverage with nominal ticket cost `C`, deterministic minimum cash payout `P`, and immediately usable nonwithdrawable lottery bonus `B`, the external cash spend is at least `C-B` (assuming the bonus can be fully applied to that game and all resulting cash prizes are withdrawable). A strict pre-tax guarantee requires:

`P > C - B`.

Equivalently, the required bonus is `B > C-P`.

This is stronger than an EV test because every legal draw outcome must satisfy the inequality.

## Current official promotions checked

### Georgia Lottery — 50% first-deposit bonus, max $125
Official promotion page (checked 2026-08-20) states that eligible first-time depositors receive a 50% bonus up to $125 on one qualifying deposit of $10+ through 2026-09-10. Deposited and bonus funds can be used only to purchase lottery games and cannot themselves be withdrawn; bonus credit is added immediately.

Primary source:
- https://www.galottery.com/en-us/player-zone/player-zone-promotions.html

Georgia Cash Pop is a compact non-shareable candidate. Official rules state:
- choose any subset of numbers 1–15;
- play all 15 to guarantee a win;
- $1 wager tier pays a minimum $5 when the drawn number is yours;
- full 15-number cover costs $15 and guarantees at least $5 cash.

Primary source:
- https://www.galottery.com/en-us/games/draw-games/cash-pop.html

Thus one full $1 cover has `C=$15`, `P=$5`, deficit `C-P=$10`. A 50% deposit bonus does not repair the floor: even if the subsidy were perfectly allocated, the base deterministic return is only 33.333%. Repeating covers to absorb the full $125 bonus remains negative. Example: 25 covers cost $375 nominal, external cash is at least $250, guaranteed cash is only $125. Strict floor = 50% of external cash.

The retailer-only instant Cash Pop cash win cannot be used to make this deterministic because its official odds are random (e.g. $1 wager instant $2 at 1 in 100), not guaranteed.

### West Virginia Lottery — $10 deposit -> $10 Free Play
Current official WV offers `WVWINS` and `IPLAY` each state that a new player depositing at least $10 receives $10 Free Play, usable on iNSTANTS or draw games; the promo is one-time and current through late 2026. This is a 100% match on the first $10, but capped at $10.

Primary sources:
- https://wvlottery.com/news-and-winning/news-and-offers/iplay-offers/west-virginia-wins-new-player-offer
- https://wvlottery.com/news-and-winning/news-and-offers/iplay-offers/iplay-new-player-offer

WV also confirms Daily 3 is purchasable online. Official prize table:
- $1 Exact: $500 on 1-in-1000;
- 50c Exact: $250 on 1-in-1000.

Primary source:
- https://wvlottery.com/games/draw-games/daily-3

Exact full coverage of all 1000 outcomes at 50c therefore has:
- `C=$500`;
- `P=$250` exactly;
- deterministic base return = 50%.

With only a capped $10 Free Play, external cash remains at least `$490`, so guaranteed profit is `$250-$490 = -$240` before any other costs. An unlimited 100% match would only move a pure 50%-floor game to break-even, not strict positive profit. Therefore the current capped offer is far below the required subsidy `B > $250`.

WV Cash Pop is not an online-purchase candidate for this bonus path: the lottery's current guide says Cash Pop cannot be purchased through iPLAY, while Daily 3/4 can.

Primary source:
- https://wvlottery.com/content/how-to-scan-lottery-ticket-iplay-app

## Result
**No SUCCESS.**

The current wallet-bonus class is real and player-owned, but the strongest live examples checked do not cross the deterministic coverage deficit:
- Georgia Cash Pop requires >$10 subsidy per $15 complete cover; 50% funding support is insufficient.
- WV Daily 3 requires >$250 subsidy on a $500 50c exact full cover; current bonus is only $10.

## New reusable screen
For future promotions, do not re-simulate the full game first. Compute exact `D=C-P` for the smallest non-shareable complete/complementary cover, then compare the player's deterministic, game-eligible bonus `B` directly against `D`. Only reopen for detailed execution if `B>D` after caps and eligibility.

## Next priority
Search current promotions for either:
1. a player-owned subsidy larger than the exact deficit of a compact fixed-prize cover (especially >50% effective subsidy on a game with >50% deterministic floor), or
2. a guaranteed per-block prize/allocation that adds directly to `P` rather than merely reducing `C`.
