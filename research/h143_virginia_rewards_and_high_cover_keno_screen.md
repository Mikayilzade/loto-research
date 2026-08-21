# H143 — Virginia Rewards exact-gate + >75% compact Keno screen

Updated: 2026-08-21
Status: **VIRGINIA 75% COVER REMAINS BEST VERIFIED / CURRENT >25% PRE-LOCKED SUBSIDY NOT FOUND / NOT SUCCESS**

## Goal
Continue directly from H142 without repeating its 75% theorem. Two questions were tested:

1. Can current Virginia Rewards/promotions provide more than $20 of player-owned, pre-committed Keno-usable value for an $80 1-Spot cover?
2. Is there a current comparable compact Keno game with deterministic cover ratio above Virginia's 75%, lowering the required subsidy threshold below 25%?

## Current Virginia Rewards findings
Primary current sources:
- Virginia Lottery Rewards FAQ: https://www.valottery.com/rewards/faq
- Virginia Lottery Rewards home: https://www.valottery.com/rewards
- Virginia Lottery current promotions / Summer Sizzle: https://www.valottery.com/rewards/promotions/summersizzle

The current Rewards FAQ confirms:
- retail lottery purchases earn 5 points per $1;
- draw games purchased online earn 5 points per $1;
- points may be redeemed for free play;
- retail free play can be redeemed as either Lottery Vending Machine credit usable on available games or a draw-game retail coupon;
- the player chooses the number of points to redeem;
- monthly free-play redemption is capped at 5,000 points;
- points from ordinary purchases can take up to 48 hours to appear.

The current public redemption page is account-state dependent and does **not** expose a fixed public dollar mapping from 250 points (or another point amount) to Keno face value while logged out. Therefore the exact dollar value of a redeemed Keno-usable coupon/credit remains unproven from public primary evidence.

This matters because H142's exact threshold is already known:
- $80 face cover;
- $60 deterministic fixed payout;
- strict pre-tax requirement: more than $20 of already-owned free play / discount on that basket.

A 5,000-point monthly redemption cap is not itself evidence of >$20 face value. We cannot legally/economically assign a dollar value to points without the actual redemption menu/terms.

## Current Virginia promotion screen
The live/currently indexed Summer Sizzle promotion is a second-chance drawing based on qualifying Scratchers; it does not provide a deterministic Keno discount or Keno free-play credit. Its promotional period ended August 2, 2026, and winner selection is random.

No current official Virginia page located in this run establishes a direct Keno purchase rebate, BOGO, checkout discount, or fixed free-play award above the >25% H142 threshold.

Result: **current public Virginia subsidy evidence remains insufficient for a strict positive Keno cover.**

## >75% compact Keno screen
For a standard 80-number Keno drawing with 20 numbers drawn, a full cover of all 80 distinct 1-Spot selections has deterministic gross ratio:

`r = (20 * one_spot_prize) / 80 = one_spot_prize / 4`

for a $1 wager on each selection, provided the 1-Spot prize is fixed.

Current official screens:

### Virginia Keno
- 1-Spot hit prize: $3 on $1.
- deterministic cover ratio: **75%**.
- H142 official rules additionally establish that this tier is fixed rather than subject to the top-tier pari-mutuel conversion.

### Massachusetts Keno
Official current page:
- 1-Spot win shown at **$2.50** on $1;
- 20 of 80 numbers are drawn;
- base 1-Spot full-cover ratio = **62.5%**.

Massachusetts offers **10% Extend & Save** on 50, 60, 70, 80, 90 or 100 consecutive games. Even giving this discount its most useful deterministic interpretation and covering all 80 1-Spots across discounted consecutive draws:

`effective ratio = 0.625 / 0.90 = 69.4444%`

still below Virginia's 75%.

Official source: https://www.masslottery.com/games/keno.html

### Ohio KENO
Official current page:
- 1-Spot hit prize: **$2** on $1;
- 20 of 80 numbers drawn;
- full-cover ratio = **50%**.

Source: https://www.ohiolottery.com/games/keno

### Delaware KENO
Official current page:
- 1-Spot hit prize: **$2** on $1;
- odds 1:4, consistent with 20/80 draw fraction;
- full-cover ratio = **50%**.

Source: https://www.delottery.com/Keno/Prizes-And-Odds

### Pennsylvania Keno control
Current/official retailer prize material shows a $2.50 1-Spot prize on $1, implying **62.5%** under the same 20/80 structure. This does not exceed Virginia.

## Comparative threshold
For deterministic coverage ratio `r`, a pre-locked face-value subsidy must satisfy:

`q > 1-r`.

Screened results:
- Virginia: r=75% -> q>25%.
- Massachusetts base: r=62.5% -> q>37.5%.
- Massachusetts with 10% multi-draw discount: effective r=69.4444% -> remaining subsidy requirement >30.5556% relative to undiscounted face, and still worse than Virginia.
- Pennsylvania: r=62.5% -> q>37.5%.
- Ohio: r=50% -> q>50%.
- Delaware: r=50% -> q>50%.

No screened current Keno 1-Spot product exceeds Virginia's verified 75% deterministic cover ratio.

## Execution gate remains
Virginia Keno drawings occur every four minutes and H142 established that one Keno ticket contains one play; current public material still does not provide an atomic pre-acceptance mechanism for all 80 distinct 1-Spot selections as one all-or-none basket.

This is secondary unless a >$20 pre-owned subsidy is found: with genuinely pre-existing free play, partial acceptance may preserve the external-cash floor if uncovered cash is not committed until enough subsidized plays have been accepted. But the exact coupon denomination/use rule must be known first.

## Result
1. **No current >25% pre-committed Virginia Keno subsidy was verified from public primary sources.**
2. **Exact Rewards free-play dollar denomination is public-web/login gated; do not assume point value.**
3. **Virginia 75% remains the best verified compact Keno fixed-prize cover among Virginia, Massachusetts, Pennsylvania, Ohio and Delaware controls.**
4. Massachusetts' deterministic 10% long-play discount is real but raises effective cover only to ~69.44%, still below Virginia.
5. Terminal SUCCESS remains unproven.

## Next action
1. Search other compact non-shareable lottery games (not only Keno) for deterministic cover ratio >75%.
2. Monitor Virginia official Rewards redemption/menu changes or public rule updates that reveal exact free-play denomination and stacking/use limits.
3. Search current player-owned direct ticket discounts/BOGOs >25% that can be applied to Virginia Keno or to another >=75% cover game before cash is committed.
4. If exact Virginia Rewards denomination becomes observable, immediately compute maximum pre-owned free-play cover and test whether multiple coupons/credits can purchase distinct 1-Spots for one draw.
