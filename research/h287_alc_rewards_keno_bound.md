# H287 — Atlantic Lottery AL Rewards + KENO Atlantic deterministic-subsidy bound

Date: 2026-08-26
State: **CLOSED / REJECTED for checked mechanism**

## Question
Atlantic Lottery launched AL Rewards in 2026. Eligible purchases earn points, points convert deterministically to Promo Cash, and Promo Cash can be spent on games at alc.ca. Does this guaranteed rebate lift a fixed-pay lottery family high enough to create an everywhere-profitable portfolio?

## Current authoritative mechanics
Atlantic Lottery Terms of Service state that:
- AL Rewards points can be exchanged for Promo Cash only;
- **1,000 points = $1 Promo Cash**;
- Promo Cash is not withdrawable cash and can only be spent on alc.ca purchases;
- purchases funded with Promo Cash do **not** earn AL Rewards points on that Promo-Cash-funded portion.

The current Rewards page advertises game earning rates of **up to 6 points per $1 spent** for the relevant online-game class. H287 deliberately grants the player the full 6 pts/$ as an upper bound even if a particular KENO purchase earns less.

Primary sources checked 2026-08-26:
- Atlantic Lottery Terms and Conditions: https://www.alc.ca/content/alc-mobile/en/legal/terms-and-conditions.html
- Atlantic Lottery Rewards: https://corp.alc.ca/content/alc/en/rewards.html
- KENO Atlantic current paytable: https://www.alc.ca/content/alc/en/our-games/lotto/keno.html

## Exact KENO model
KENO Atlantic draws 20 numbers from 70. For a k-spot selection and exactly m matches,

`P_k(m) = C(20,m) C(50,k-m) / C(70,k)`.

Using the published fixed $1 paytable for every spot size 2 through 10 gives these exact average gross returns per $1 wager:

| Spot | Base average gross | After max 6 pts/$ Rewards upper bound |
|---:|---:|---:|
| 2 | 55.072464% | 55.402899% |
| 3 | 52.064304% | 52.376690% |
| 4 | 52.064304% | 52.376690% |
| 5 | 52.040756% | 52.353001% |
| 6 | 53.395663% | 53.716037% |
| **7** | **56.421110%** | **56.759636%** |
| 8 | 53.038461% | 53.356691% |
| 9 | 54.021861% | 54.345992% |
| 10 | 56.012254% | 56.348328% |

The Rewards factor is at most:

`1 + 6/1000 = 1.006`.

Because Promo-Cash-funded spend earns no further points, there is no infinite rebate recursion.

## Portfolio-wide proof
For each fixed spot size, every selection is symmetric under relabeling of the 70 numbers, so every selection has the same average gross across all legal 20-number draw outcomes.

For any nonnegative portfolio of KENO selections:

`minimum legal-outcome gross <= average gross`.

A mixture of spot sizes cannot exceed the best component average. The best checked component is 7-Spot at 56.4211097% before Rewards. Even granting the maximum 0.6% Promo Cash rebate and wagering all of it optimally inside the same checked class gives at most:

`0.5642110971 × 1.006 = 0.5675963637`.

So the strongest player-favourable average upper bound is only **56.7596364% of original cash spend**. Since the minimum outcome cannot exceed that average, strict guaranteed profit is impossible for this entire additive KENO portfolio class.

## Additional cap note
KENO Atlantic also reserves the right to cap total prizes for a draw at C$3 million and reduce prizes proportionally if the cap is reached. H287 does not need this adverse rule: the mechanism already fails under the more favourable uncapped published paytable.

## Conclusion
**REJECT.** AL Rewards is a genuine deterministic external subsidy, but at current redemption/earning rates it is far too small to overcome the exact KENO fixed-pay deficit. Reopen only if Rewards earning rates materially increase, redemption becomes richer than 1,000 points = $1, or the KENO paytable changes enough that the best fixed-pay average approaches the required threshold.
