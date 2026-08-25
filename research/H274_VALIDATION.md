# H274 VALIDATION — Powerball Double Play full-cover bound

Validated: 2026-08-25.

## Independent combinatorial checks
For a fixed 5/69 + 1/26 winning outcome, the one-copy full universe has these exact multiplicities:

| White matches | PB match | PB nonmatch |
|---:|---:|---:|
| 5 | 1 | 25 |
| 4 | 320 | 8,000 |
| 3 | 20,160 | 504,000 |
| 2 | 416,640 | 10,416,000 |
| 1 | 3,176,880 | 79,422,000 |
| 0 | 7,624,512 | 190,612,800 |

The sum is exactly **292,201,338 = C(69,5)*26**.

Applying the official current prize tables gives:
- ordinary Powerball fixed lower tiers, excluding jackpot: **$93,466,048**;
- Double Play fixed schedule, including $10m top prize: **$156,133,184**;
- fixed combined gross: **$249,599,232**.

At $3 per covered line, exact full-cover cost is **$876,604,014**, so fixed return is **0.284734301935332**.

The checked next-draw advertised jackpot is $96m with $41.2m cash value. An intentionally stronger-than-real upper bound that grants the portfolio all $96m with no sharing still yields only **$345,599,232 = 39.4247832%** of cost. Therefore the current-draw full-cover construction is decisively below break-even without needing any assumptions about external jackpot duplicates.

## Source validation
Official Powerball sources checked on 2026-08-25:
- https://www.powerball.com/ — $2 base price, 5/69 + 1/26 matrix, current next-draw jackpot/cash value, +$1 Double Play statement.
- https://www.powerball.com/double-play — same numbers replayed in separate draw; $10m top prize; fixed Double Play prize chart.
- https://www.powerball.com/POWERBALL-PRIZE-CHART — ordinary lower-tier fixed prize schedule and 1-in-292,201,338 jackpot odds.

## Gate
**PASS validation / REJECT strategy for current draw.** Arithmetic is exact, universe total is exact, and the upper-bound conclusion remains below cost even after an impossible favorable jackpot grant.
