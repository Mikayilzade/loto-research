# H285 STATUS

Updated: 2026-08-26
State: **CLOSED / REJECTED for tested mechanism**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Mechanism tested
Hoosier Lottery promotional free-ticket coupons as deterministic external subsidy / cash-equivalent value.

## Terminal result
Official retailer instructions make the coupon single-use, limited to one per person, and explicitly non-redeemable for cash or another Lottery product. Draw/Fast Play coupons print the ticket specified by the coupon; Scratch coupons provide one free $1 Scratch-off or $1 off a Scratch purchase.

A checked current $1 Fast Play example, JUMBO BUCKS, has overall winning odds 1 in 3.69 and explicitly draws from a replenished pool containing winning and non-winning outcomes. Therefore a legal zero-prize branch exists.

For a single noncash free-ticket coupon:
- face/acquisition value may be positive;
- guaranteed withdrawable cash prize = **$0**;
- strict positive cash floor = **false**.

This closes the ordinary one-ticket coupon channel for the current guarantee objective. Positive expected value or retail face value is not sufficient.

## NEXT ACTION
Do not reopen ordinary Hoosier single-use free-ticket coupons unless terms materially change. Continue with one of:
1. deterministic withdrawable cashback / cash-equivalent reward;
2. a coupon that directly discounts a separately proven exact cover;
3. enough player-controllable free selections to create complete positive-floor coverage;
4. hard-capped/reservable inventory whose guaranteed external liabilities exceed total acquisition cost.

Files:
- `research/h285_hoosier_free_ticket_coupon_floor.md`
- `research/H285_VALIDATION.md`
- `src/loto_research/h285_hoosier_coupon_floor.py`
- `data/derived/h285_hoosier_coupon_floor.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H285_APPEND.md`
