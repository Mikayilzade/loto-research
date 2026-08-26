# H293 — Flash Rewards finite-pool full-acquisition screen

Checked: 2026-08-26
Status: **REJECTED / CLOSED**

## Question
Can a current hard-capped Flash Rewards draw be monopolized cheaply enough that owning every issued entry guarantees value strictly above acquisition cost?

This packet deliberately grants the player the impossible stronger condition of perfect full-pool ownership. If even that is below cost, real execution cannot rescue the mechanism.

## Current source facts
Current-draw page and promotion pages publish hard entry caps, package prices and prize/cash alternatives:

- Flight Centre Gift Card: 2,000 entries; packages 1/$10, 4/$34, 8/$60; player prize value A$5,000, cash alternative A$4,000.
- DJI Osmo Pocket 4: 500 entries; packages 1/$5, 5/$22, 10/$40; player prize value A$769, cash alternative A$600.
- Apple Watch SE 3 + AirPods 4: 1,000 entries; packages 1/$1, 8/$7, 19/$15; player prize value A$618, cash alternative A$500.
- AirPods 4: 90 entries; packages 1/$5, 3/$13, 6/$24; player prize value A$219, cash alternative A$150.

Sources:
- https://flashrewards.com.au/giveaways/
- https://flashrewards.com.au/promotions/flight-centre-gift-card-5000/
- https://flashrewards.com.au/promotions/osmo-pocket-4-gimble-camera-769-value/
- https://flashrewards.com.au/promotions/1005-apple-watch-se-3/
- https://flashrewards.com.au/promotions/1006-apple-airpods-4/

The site separately mentions charity donations. Those are not player-facing value and are not counted as guaranteed player return.

## Exact package optimization
`src/loto_research/h293_flash_rewards_finite_pool.py` performs an exact integer dynamic-programming minimization over the published package sizes, requiring exactly the full number of entries.

Results:

| Draw | Entries | Minimum exact full-acquisition cost | Player prize value | Retail-value return | Cash alternative | Cash return |
|---|---:|---:|---:|---:|---:|---:|
| Flight Centre | 2,000 | A$15,000 | A$5,000 | 33.3333% | A$4,000 | 26.6667% |
| DJI Osmo | 500 | A$2,000 | A$769 | 38.4500% | A$600 | 30.0000% |
| Watch + AirPods | 1,000 | **A$791** | A$618 | **78.12895%** | A$500 | 63.21113% |
| AirPods | 90 | A$360 | A$219 | 60.8333% | A$150 | 41.6667% |

The best current case is the Apple Watch + AirPods draw, but even impossible-perfect ownership leaves an A$173 deficit using advertised retail value and an A$291 deficit using the cash alternative.

## Stronger execution blocker
The promotion terms also state that the Promoter may, in its absolute discretion, not accept a particular entry, disqualify an entry, or cancel the entire promotion, subject to regulatory directions. Thus full acquisition is not a pre-committed player right anyway.

This blocker is secondary: the economics already fail under impossible-perfect ownership.

## Conclusion
**H293 is closed.** The checked current Flash Rewards hard-capped pools do not cross 100% even under perfect monopolization. Do not revisit these exact draws unless package pricing or player-facing prize values materially change.

The useful continuation remains: search for a hard-capped/reservable pool where player-facing guaranteed liabilities exceed exact cheapest full-acquisition cost, or a deterministic external subsidy large enough to push a near-miss above 100%.
