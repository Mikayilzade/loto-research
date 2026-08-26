# H285 VALIDATION — Hoosier free-ticket coupon floor

Validated: 2026-08-26

## Evidence gates
- Official retailer instructions explicitly classify coupon redemption into Scratch-off and Draw/Fast Play paths.
- Draw/Fast Play coupon redemption prints the ticket identified by the coupon rather than cash.
- Coupons are single-use, limited to one per person, and may not be redeemed for cash or substituted for another Lottery product.
- Current Hoosier $1 JUMBO BUCKS Fast Play explicitly has both winning and non-winning outcomes; overall win odds are 1 in 3.69.

## Logical gate
Let `P(omega) >= 0` be the cash prize from the free ticket. The official game admits at least one legal `omega0` with `P(omega0)=0`. Hence

`min_omega P(omega) = 0`.

The coupon has zero acquisition cost but is not itself withdrawable cash, so promotional face value does not imply a positive cash floor. Any strategy that requires this single coupon to contribute a guaranteed positive amount therefore fails.

## Stress tests
- Giving the coupon its full face value as a *budget* still does not change `min prize = 0`.
- Removing retailer fees does not change the result.
- Allowing the player to choose when to redeem does not remove the legal losing outcome.
- Expected value is irrelevant to an everywhere-positive guarantee.

## Validation conclusion
The checked Hoosier free-ticket coupon channel is **not a deterministic cash-equivalent subsidy**. H285 is closed for the strict-guarantee mechanism unless coupon terms materially change.
