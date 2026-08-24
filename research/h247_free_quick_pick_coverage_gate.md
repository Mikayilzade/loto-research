# H247 — Free Quick Pick / BOGO coverage-subsidy gate

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: REJECTED as a strict controlled-coverage subsidy

## Question
Can a lottery promotion that gives a free **Quick Pick** ticket materially reduce the purchase cost of a deterministic full-coverage construction?

## Current primary examples

### Kentucky Lottery — active August 2026 Kroger promotion
The Kentucky Lottery promotions page states that from **2026-08-01 through 2026-08-31**, buying **$10 or more in Millionaire for Life** in one Kroger transaction automatically gives **two free $1 Cash Ball 225 Quick Pick plays**.

The free legs are explicitly Quick Picks in a different draw game. They therefore cannot be assigned to missing Millionaire for Life combinations, and each can legally return $0.

### Hoosier Lottery — current Millionaire for Life coupon
The Hoosier Lottery current coupon sheet states that a Millionaire for Life coupon is valid **2026-03-23 through 2027-03-31**, is good for one free $5 Millionaire for Life ticket, and is **valid on Quick Pick only**. The terminal automatically prints the free ticket when the coupon is redeemed.

This establishes the same structural issue even when the free ticket is in the *same* game: the player does not control the combination.

### Pennsylvania control examples
Pennsylvania Lottery retailer coupon materials explicitly describe current/recent free Mega Millions and Millionaire for Life coupons as **Quick Pick** tickets. Pennsylvania also ran a March 9–15, 2026 Millionaire for Life BOGO promotion, but the public poster alone does not establish player-selectability of the free leg, so H247 does not assume it.

## Exact guarantee theorem
Let the target game have finite state space `U` with `|U| = N`, and suppose a strict full-coverage strategy must own at least one ticket for every element of `U` before the draw.

A promotion may issue any number of free Quick Picks whose selections are random and not controllable by the player.

For a **guaranteed** coverage claim, all allowed Quick-Pick realizations must be considered. There is always an allowed realization in which every free Quick Pick duplicates a combination already owned by the player (or duplicates each other). Therefore the free Quick Picks have **zero guaranteed marginal coverage**.

Consequently:

`minimum guaranteed controlled paid coverage count = N`

unless the promotion contract gives the player deterministic control over the free selection, or guarantees a non-duplicating assignment covering specific missing states.

The same logic applies to cash floor: if a free Quick Pick has a legal losing outcome, its strict guaranteed cash contribution is `$0`, regardless of its face value or expected value.

## Millionaire for Life implication
H026 established the current Millionaire for Life controlled full-space size:

- `N = C(58,5)*5 = 22,910,580` plays;
- controlled paid full-cover cost = **$114,552,900** at $5/play;
- deliberately favorable full-cover gross upper bound = **$60,584,320 = 52.8876%** of cost.

A superficial BOGO calculation might divide acquisition cost by two. H247 shows why that is invalid when the free leg is Quick Pick: in the worst allowed Quick-Pick realization, it covers no missing state and can pay $0. Therefore the strict controlled-coverage acquisition requirement remains the H026 paid full-space requirement.

## Verdict
**REJECTED.** Free Quick Pick tickets, including BOGO-style free legs, cannot be booked as deterministic coverage discounts or deterministic cash rebates. Reopen this class only if primary rules establish that the player can choose the free combination or that the operator guarantees non-duplicating missing-state coverage.

## Sources
- Kentucky Lottery current Promotions and Events page, active Kroger offer Aug. 1–31, 2026: https://www.kylottery.com/apps/promotions/promotions.html
- Hoosier Lottery Coupons in Market Update, Millionaire for Life coupon valid Mar. 23, 2026–Mar. 31, 2027, Quick Pick only: https://hoosierlottery.com/getmedia/4e9bae3c-d4d6-4d78-b345-fdaa60a79e37/Coupons_in_Market_Update.pdf
- Pennsylvania Lottery April 2026 Coupon Offers, free Mega Millions / Millionaire for Life Quick Pick examples: https://www.palottery.pa.gov/PaLotteryWebSite/media/Retailer-Documents/Coupon-Promos/April2026_Coupon-Offers.pdf
- Pennsylvania Lottery Millionaire for Life BOGO poster, Mar. 9–15, 2026: https://www.palottery.pa.gov/PaLotteryWebSite/media/Retailer-Documents/POS/PAL_MillionaireForLife_POS.pdf
- Existing exact base calculation: `research/h026_millionaire_for_life_full_coverage.md`
