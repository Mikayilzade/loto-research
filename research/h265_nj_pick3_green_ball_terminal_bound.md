# H265 — New Jersey Pick-3 Green Ball terminal-double-draw bound

Validated: 2026-08-25
Status: **CLOSED / REJECTED** for strict-profit construction under the checked 2026 Green Ball mechanics.

## Why this candidate mattered

The July 6–August 3, 2026 New Jersey Pick-3 Green Ball promotion is a genuine elimination mechanism. Each evening starts with six white balls and one Green Ball; a white ball is removed when drawn, while a Green Ball triggers a free second Pick-3 draw from the same original wager and resets the promotion chamber. Therefore, after six consecutive white removals, the next promotion-ball result is deterministic: only the Green Ball remains.

This is stronger than an ordinary random bonus. A player who waits until that public terminal chamber state can know before purchasing that the evening will have **two Pick-3 number draws for one base Pick-3 wager**.

Official 2026 sources:
- current Pick-3 prize/odds page: https://www.njlottery.com/en-us/drawgames/pick3.html
- Aug. 18, 2026 NJ Lottery release confirming the latest promotion ran July 6–Aug. 3, used six white + one Green Ball, removed whites, and awarded a second set of Pick-3 numbers when Green appeared: https://www.njlottery.com/en-us/newsandevents/newsinput/2026/press-releases/P3_GreenBallPromotionResults_081826.html

The promotion had already ended by this validation date, so H265 is not claiming a presently purchasable terminal state. The purpose is to test the mechanism rigorously and define a future reopen threshold.

## Published fixed-prize primitives

Using a $0.50 base wager:

| primitive | base winning outcomes | base prize | one-draw average gross | base EV / cost |
|---|---:|---:|---:|---:|
| Straight | 1 / 1000 | $250 | $0.25 | 50% |
| 3-Way Box | 3 / 1000 | $80 | $0.24 | 48% |
| 6-Way Box | 6 / 1000 | $40 | $0.24 | 48% |
| Pair | 1 / 100 | $25 | $0.25 | 50% |

Straight/Box is a nonnegative combination of Straight and Box. Wheel is a convenient purchase of all constituent Straight bets. Thus they cannot beat the best primitive average-return bound.

## Strongest terminal Green Ball grant

Grant the player the favorable case that six white balls are already gone and the Green Ball is certain tonight.

The same base wager then receives two Pick-3 draws. Hence:

| primitive | terminal average gross on $0.50 base | return ratio |
|---|---:|---:|
| Straight | $0.50 | **100%** |
| 3-Way Box | $0.48 | 96% |
| 6-Way Box | $0.48 | 96% |
| Pair | $0.50 | **100%** |

This reaches break-even in expectation for Straight/Pair, but never exceeds it.

The key strict-guarantee theorem is stronger than a single full-cover check. For any nonnegative portfolio P, let G(x,y) be its gross for legal regular/Green-Ball Pick-3 outcomes x,y. Then

`min_{x,y} G(x,y) <= average_{x,y} G(x,y)`.

Every primitive has average terminal gross <= its purchase cost. A nonnegative linear combination therefore also has portfolio average gross <= portfolio cost. Consequently at least one legal pair of draw outcomes has gross <= cost. **Strict positive profit for every legal outcome is impossible.**

Independence between the two Pick-3 draws is not needed for the inequality; only the uniform marginal prize table used by the official game is needed.

## FIREBALL cannot rescue it

The current NJ page states that adding FIREBALL doubles the cost of the play. The Green Ball promotion's second-draw winner determination excludes FIREBALL, so the extra FIREBALL stake applies only to the regular draw.

For the $0.50 FIREBALL add-on, the published winning-combination/prize tables give an average $0.27 FIREBALL gross for Straight, Box and Pair primitives. Therefore the strongest terminal totals on $1.00 combined base+FIREBALL cost are:

- Straight: $0.25 regular base + $0.25 Green Ball base + $0.27 FIREBALL = **$0.77 = 77%**;
- Pair: same **77%**;
- 3-Way / 6-Way Box: $0.24 + $0.24 + $0.27 = **$0.75 = 75%**.

So FIREBALL moves the upper bound farther below break-even.

## Instant Match

Instant Match is a separate paid random add-on. The official page describes it as a chance to win, so a nonwinning outcome remains legal. It adds acquisition cost with zero strict worst-case contribution and cannot rescue an everywhere-positive guarantee.

## Result

Even the **known terminal Green Ball state**, where the free second draw is certain before purchase, cannot generate a strict positive-profit portfolio from the published fixed-prize Pick-3 wagers. Best possible average ratio is exactly **100% without FIREBALL** and **77% with FIREBALL**. Since a portfolio's minimum legal-outcome gross cannot exceed its average gross, strict profit is ruled out.

Reopen only if a future Green Ball/Double Draw promotion changes at least one of these gates, for example:
- the free promotion creates **more than one** guaranteed additional Pick-3 draw from the same wager;
- fixed Pick-3 payouts are increased enough that the terminal two-draw primitive average exceeds 100%;
- a deterministic discount reduces effective acquisition cost below the exact hurdle;
- a separate guaranteed cash subsidy attaches to every eligible wager.

Reproducible files:
- `src/loto_research/h265_nj_pick3_green_ball_bound.py`
- `data/derived/h265_nj_pick3_green_ball_bound.json`
- `research/H265_VALIDATION.md`
