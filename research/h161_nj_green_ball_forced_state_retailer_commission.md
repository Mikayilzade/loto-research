# H161 — New Jersey Pick-3 Green Ball forced-state + retailer commission corollary

Updated: 2026-08-21
Status: **NO SUCCESS / FORCED SECOND-DRAW STATE VALIDATED / RETAILER COMMISSION CREATES POSITIVE PRE-TAX COROLLARY BUT CONTRACT/TAX EXECUTION GATES REMAIN**

## Objective
Extend H160 beyond Michigan by finding a recurring lottery promotion where the free second draw becomes certain before betting closes, then test whether a lawful lottery-specific structural subsidy can move exact coverage above 100%.

## Current/primary-source findings
New Jersey ran a Pick-3 Green Ball promotion from **July 6 through August 2, 2026**. Official rules used six white balls and one green ball. Each white ball was removed after it was drawn. When the green ball was drawn, the same Pick-3 wager received a second Pick-3 draw at the unchanged prize structure, then all seven balls reset.

Crucially, New Jersey also publicly stated during the 2025 recurrence that the Lottery homepage displayed the **number of white balls remaining** for the nightly drawing. This means the state of the trigger process is observable to players before purchase. With six whites already removed, the next Green Ball promotional draw contains only the green ball, so the second Pick-3 draw is certain ex ante.

The architecture is recurring, not hypothetical: official releases document Green Ball periods in May 2025, Jan-Feb 2026, and Jul-Aug 2026. The latest 2026 cycle produced eight Green Ball double draws and $2.55m of incremental prizes.

Primary sources:
- 2026 Green Ball rules: https://njs-cdn.lotteryservices.com/content/dam/portal/pdfs/drawgames/pick3/Pick-3-Green-Ball-Rules-Effective-07.06.2026_V1.pdf
- 2026 results: https://www.njlottery.com/en-us/newsandevents/newsinput/2026/press-releases/P3_GreenBallPromotionResults_081826.html
- 2025 page-state disclosure: https://www.njlottery.com/en-us/newsandevents/newsinput/2025/press-releases/P3_GreenBall_050725.html
- Jan 2026 recurrence announcement: https://www.njlottery.com/en-us/newsandevents/newsinput/2025/press-releases/NJL_GreenBall_123025.html

## Pick-3 Pair full-cover identity
Current official Pick-3 prize table:
- Pair wager minimum: $0.50;
- 100 possible ordered pair outcomes;
- $0.50 winning Pair prize: $25;
- fixed prizes since Nov. 2022.

Therefore a complete cover of one Pair position costs:
- `100 * $0.50 = $50`.

For one draw exactly one Pair wins:
- deterministic gross = `$25`;
- base cover ratio = **50%**.

At forced-green state (`k=6`, all six white balls already removed), the same 100-wager basket participates in two full Pick-3 draws:
- regular draw Pair winner = `$25`;
- Green Ball Double Draw Pair winner = `$25`;
- guaranteed gross = **$50**;
- deterministic gross ratio = **100%**.

This reproduces H160's 100% forced-second-draw theorem with one-tenth the transaction count and one-tenth the face capital of a full Straight cover.

Official current prize table:
- https://www.njlottery.com/en-us/drawgames/pick3.html

## New retailer-commission corollary
New Jersey's current Full Service Retailer page states:
- **5% commission on every ticket sold**;
- **1.25% payout/cashing commission on prizes up to $600**.

Official page:
- https://www.njlottery.com/en-us/retailer/becomeretailer/full-service-retailer.html

New Jersey's own 2023 winner release documents a licensed retailer owner, Jay Shortway, purchasing a CASH4LIFE ticket for himself at his own restaurant/lottery location and being recognized as the winner. This is strong evidence that retailer-owner self-purchase is not categorically prohibited.

Official release:
- https://www.njlottery.com/en-us/newsandevents/newsinput/2023/press-releases/C4L_GrandPrize_042123.html

The current prohibited-person rule lists Lottery commissioners, certain Lottery/vendor personnel, households of those persons, and courier personnel; ordinary licensed retailer owners are not listed in that prohibition.

If the ordinary published retailer commissions apply without an undisclosed self-purchase exclusion, the forced-green Pair-cover cash arithmetic would be:
- ticket face cost = `$50`;
- guaranteed two-draw prize gross = `$50`;
- 5% sales commission = `$2.50`;
- 1.25% payout commission on $50 = `$0.625`;
- **pre-tax economic surplus = $3.125 = 6.25% of ticket face**.

This is the first forced-second-draw branch in the project where an ordinary lottery-industry structural commission, rather than a separate promotional coupon, can mathematically push the deterministic cover above 100%.

## Why this is NOT terminal SUCCESS
### 1. Commission-on-self-purchase is not expressly locked
The sources establish that retailer owners can buy/claim tickets and that retailers generally earn 5% on every ticket sold plus 1.25% payout commission. They do **not** expressly state that the 5% sales commission and 1.25% payout commission are guaranteed on a retailer owner's own strategically purchased ticket basket. A written retailer-contract or Lottery confirmation is required before counting this as a strict entitlement.

### 2. Promotion can be modified/cancelled without prior notice
The 2026 Green Ball rules reserve Lottery discretion to cancel, terminate, modify or suspend the promotion at any time and for any reason, including when payout exceeds the promotion budget. That creates a lawful branch in which the forced second draw disappears after tickets are bought unless the Lottery's obligations become irrevocably fixed at ticket issuance.

### 3. Pick-3 liability limits can stop complete coverage
Official Pick-3 rules state that if liability on a number exceeds a pre-determined Lottery limit, no further wagers on that number are accepted, and the limit can be changed at the Director's discretion. The 100 Pair bets are much easier to execute than 1,000 Straights, but complete basket acceptance still must be verified.

### 4. Promotion cannot stack with ordinary coupons/promotions
The 2026 Green Ball rules expressly say it is not valid in combination with another New Jersey Lottery promotion or coupon. Therefore the obvious coupon/free-play stacking route is closed by rule. Retailer commission is analytically separate, but its self-purchase applicability still needs explicit confirmation.

### 5. Tax floor is not proven
The deterministic pre-tax margin is only $3.125 on $50 face. 2026 federal wagering-loss deduction restrictions plus federal/state business-income treatment can consume that margin in some taxpayer/entity configurations. Terminal SUCCESS requires a specific lawful tax/entity treatment leaving a strictly positive after-tax floor.

### 6. Not active today
The latest Green Ball period ended August 2, 2026. This is a **recurring monitor**, not a currently executable trade on 2026-08-21.

## Exact state screen
See `data/derived/h161_nj_green_ball_pair_cover.csv`.

Only `k=6` provides a strict second-draw guarantee. For k=0..5, a white-ball outcome remains possible, so the strict draw-count floor stays one and the Pair cover floor remains 50%.

## Result
- New Jersey recurring cumulative-trigger Green Ball architecture: **VALIDATED**.
- Trigger state is publicly observable before betting: **VALIDATED historically/current architecture**.
- Forced-green Pair cover: **100% deterministic gross with only $50 face and 100 wagers**.
- General retailer commission layer: **5% sales + 1.25% sub-$600 payout VALIDATED**.
- Retailer-owner self-purchase: **demonstrated by official NJ Lottery winner case**.
- Commission entitlement on self-purchased strategic basket: **NOT EXPRESSLY PROVEN**.
- Terminal SUCCESS: **NO**, due commission-entitlement, cancellation/discretion, full-basket acceptance, tax, and inactive-current-period gates.

## Highest-value next action
1. Find an official NJ retailer agreement/manual or written rule stating whether sales and payout commissions apply to tickets purchased by the licensed retailer/owner/employee for personal play.
2. During the next Green Ball cycle, monitor the publicly displayed remaining-white-ball count; reopen immediately at `k=6`.
3. Determine whether accepted Green Ball-eligible tickets acquire an irrevocable right to the second draw even if the promotion is subsequently cancelled/modified.
4. Search other jurisdictions with the same cumulative-trigger architecture but larger fixed-prize base cover ratio or less discretionary promo language.
5. Search retailer-commission structures in other forced-second-draw jurisdictions where self-purchase is expressly allowed and commissions are unambiguously earned.
