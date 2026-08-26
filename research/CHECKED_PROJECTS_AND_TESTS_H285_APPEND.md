# Checked projects/tests — H285 append

## H285 — Hoosier Lottery free-ticket coupon cash-floor audit
- Date checked: 2026-08-26.
- Candidate type: deterministic promotional subsidy / coupon.
- Official mechanism: single-use coupon for one specified Draw/Fast Play ticket, or one free $1 Scratch-off / $1 off Scratch-off.
- Cashability: coupon itself explicitly cannot be redeemed for cash or another Lottery product.
- Exact guarantee result: **$0 guaranteed withdrawable cash floor** whenever the issued free ticket has a legal losing outcome.
- Current witness game: $1 JUMBO BUCKS Fast Play, overall winning odds 1 in 3.69, with official rules explicitly describing both winning and non-winning outcomes in the replenished pool.
- Outcome: **REJECTED / CLOSED for strict guaranteed-profit use**.
- Reopen condition: materially different coupon providing cash/cash-equivalent value, guaranteed minimum prize, a deterministic discount on a rigorous cover, or enough player-controlled free entries for full positive-floor coverage.

Primary evidence:
- https://hoosierlottery.com/who-we-are/retailer-resources/redeeming-coupons/
- https://hoosierlottery.com/getmedia/4e9bae3c-d4d6-4d78-b345-fdaa60a79e37/Coupons_in_Market_Update.pdf
- https://hoosierlottery.com/games/fast-play/jumbo-bucks/
