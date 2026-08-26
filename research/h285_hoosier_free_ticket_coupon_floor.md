# H285 — Hoosier Lottery free-ticket coupon deterministic-subsidy audit

Date: 2026-08-26
State: **CLOSED / REJECTED for strict guaranteed-profit use**

## Question
Can the Hoosier Lottery coupon channel supply the deterministic external subsidy sought by the global NEXT ACTION — i.e. value that can be turned into a strictly positive cash floor rather than merely positive expected value?

## Authoritative mechanics checked
1. Hoosier Lottery retailer instructions state that coupons may be for Draw, Fast Play, or Scratch-off products.
2. A Draw/Fast Play coupon is redeemed through `Promo/Coupon`; the terminal automatically prints the free ticket specified by the coupon.
3. A Scratch-off coupon yields one free $1 Scratch-off or $1 off a Scratch-off purchase.
4. Coupons are single-use, limited to one per person, not valid with another offer, and **may not be redeemed for cash or other Hoosier Lottery products**.
5. The current $1 JUMBO BUCKS Fast Play game has overall winning odds 1 in 3.69 and is generated from a constantly replenished pool containing both winning and non-winning outcomes. Therefore a legal zero-prize outcome exists for a free $1 Fast Play ticket.

Primary sources checked 2026-08-26:
- Hoosier Lottery, `Redeeming Coupons`: https://hoosierlottery.com/who-we-are/retailer-resources/redeeming-coupons/
- Hoosier Lottery, FY26 coupon FAQ / coupons-in-market update: https://hoosierlottery.com/getmedia/4e9bae3c-d4d6-4d78-b345-fdaa60a79e37/Coupons_in_Market_Update.pdf
- Hoosier Lottery, JUMBO BUCKS Fast Play: https://hoosierlottery.com/games/fast-play/jumbo-bucks/

## Exact worst-case result
For a single free-ticket coupon whose ticket has at least one legal losing outcome:

`coupon cash cost = 0`

`guaranteed withdrawable cash prize = min_legal_outcome(prize) = 0`

The coupon has promotional retail value, but its **strict cash floor is zero**. Because the coupon itself cannot be redeemed for cash, that zero-prize branch cannot be bypassed by cashing the subsidy before play.

The same blocker applies to any finite set of uncontrolled/non-covering free tickets: if a legal joint outcome leaves all of them losing, the combined guaranteed cash floor remains zero. A future coupon becomes interesting only if it is (a) cash/cash-equivalent, (b) a deterministic discount on a separately proven >cost cover, or (c) issued in enough player-controllable quantity to form a complete positive-floor cover.

## Why this matters
This closes a real promotional channel without relying on average RTP. The global search needs deterministic *cash-convertible* external value. A noncash one-ticket coupon with a legal losing outcome cannot raise the worst-case floor at all, even though it has positive expected/promotional value.

## Conclusion
**REJECT for current strict-guarantee mechanism.** Do not treat ordinary Hoosier free-ticket coupons as withdrawable subsidy. Reopen only on materially different coupon terms such as guaranteed cash, guaranteed minimum prize, multi-ticket complete coverage, or a fixed discount applied to a separately rigorous profitable cover.
