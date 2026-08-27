# H319 — Giveaway Guys 20% subscription-credit finite-pool upper bound

Updated: 2026-08-27
State: **CLOSED / ARITHMETIC-BOUND**

## Question

Can the current Giveaway Guys subscription benefit — advertised as **20% extra site credits** — turn one of the site's current finite prize pools into a strict guaranteed-profit full takeover?

This directly follows the H318 filter: use a finite pool, allow full acquisition whenever possible, and test a deterministic subsidy against exact acquisition cost.

## Current evidence

Checked current operator pages:

- https://giveawayguys.co.uk/
- https://giveawayguys.co.uk/all-competitions-2/
- https://giveawayguys.co.uk/product/high-roller-hit-win-500-instantly/
- https://giveawayguys.co.uk/product/uno-10000-wild-card/

The current homepage/all-competitions pages list live September 30, 2026 pools including:

- £30,000 Mega Instants: 90,000 entries at £1;
- £500 Daily Instants: 1,000 entries at £1;
- £1,000 Weekly Cash Grab: 2,000 entries at £1;
- Simpsons Hit & Run £17,500 Prize Pot: 25,000 entries at £0.99;
- UNO £10,000 Wild Card: 6,000 entries at £2.50;
- Cashopoly £15,000: 30,000 entries at £1;
- Big Brother £5,000 Cash House: 2,000 entries at £5;
- Lucky 7's £250: 1,000 entries at £0.99;
- High Roller Hit: 500 entries at £4.99.

The same current operator page states under **SUBSCRIPTION BONUS** that subscribers receive **20% extra site credits**.

For High Roller the published instant schedule is explicit: 1x£500 cash, 2x£100 site credit, 5x£50 site credit, 10x£20 cash, 20x£10 site credit, total face liability £1,350.

## Deliberately stronger-than-real model

To avoid closing a candidate because of execution details, H319 grants all of the following impossible/favourable assumptions:

1. the 20% subscription-credit uplift scales without limit to the entire pool;
2. site credits and every advertised prize-pound are valued at **100% withdrawable cash**;
3. one player can acquire the whole pool from inception, ignoring tickets already sold, checkout limits, competing buyers, postal/free entries and allocation friction;
4. the headline advertised prize/pot value is granted in full to the takeover portfolio.

Thus a £1 cash outlay is treated as buying £1.20 of entries. The impossible-favourable cash acquisition cost of a pool with face cost `C` is therefore `C / 1.2`.

If even this upper bound is below 100%, the real construction is closed.

## Exact results

| Pool | Face full cost | Favourable liability | Base upper return | With unlimited 20% credit |
|---|---:|---:|---:|---:|
| Mega Instants | £90,000 | £30,000 | 33.3333% | 40.0000% |
| Daily Instants | £1,000 | £500 | 50.0000% | 60.0000% |
| Weekly Cash Grab | £2,000 | £1,000 | 50.0000% | 60.0000% |
| **Simpsons Hit & Run** | **£24,750** | **£17,500** | **70.7071%** | **84.8485%** |
| UNO Wild Card | £15,000 | £10,000 | 66.6667% | 80.0000% |
| Cashopoly | £30,000 | £15,000 | 50.0000% | 60.0000% |
| Big Brother Cash House | £10,000 | £5,000 | 50.0000% | 60.0000% |
| Lucky 7s | £990 | £250 | 25.2525% | 30.3030% |
| High Roller Hit | £2,495 | £1,350 | 54.1082% | 64.9299% |

The best checked pool is Simpsons Hit & Run:

- face acquisition: `25,000 × £0.99 = £24,750`;
- impossible cash cost after unlimited 20% leverage: `£24,750 / 1.2 = £20,625`;
- full favourable prize liability: £17,500;
- return: `17,500 / 20,625 = 84.8484848%`;
- deficit: **£3,125** even in the impossible-favourable model.

## Reusable threshold

For a finite pool with base full-buyout ratio `r = liability / face_cost`, a deterministic credit leverage `L` can only cross strict break-even if:

`L * r > 1`.

For the strongest current checked pool, `r = 0.7070707`; required leverage is therefore greater than `1 / r = 1.4142857`, i.e. an extra-credit uplift **strictly above 41.42857%** if all other impossible favourable assumptions were retained.

The advertised 20% is far below that threshold.

## Conclusion

**H319 is closed.** The current 20% subscription-credit benefit cannot turn any of the checked live Giveaway Guys finite pools into a guaranteed-positive full takeover. The result is stronger than real execution because it grants unlimited bonus scaling, full pool ownership, and 100% cash value to all headline liabilities.

Do not reopen this exact subscription/full-pool construction unless either:

- the deterministic extra-credit rate rises enough to cross the exact threshold for a live pool; or
- a new pool appears whose player-facing liability/full-cost ratio is already near or above 83.3333% (the minimum base ratio needed for a 20% leverage factor to reach break-even).

Reproducible files:

- `src/loto_research/h319_giveaway_guys_subscription_subsidy_bound.py`
- `data/derived/h319_giveaway_guys_subscription_subsidy_bound.json`
