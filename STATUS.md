# STATUS

Updated: 2026-08-20
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H135 — Washington Happy Hour scalable subsidy + compact fixed-prize coverage**.

### H135 result
Washington's Lottery provides a rare validated promotion class with all the right structural properties: player-owned, deterministic free ticket value and explicit scaling in fixed purchase increments.

Strongest test used historical Match 4 Happy Hour:
- buy **$10 Match 4**, receive **$4 Match 4 free**;
- multiple offers expressly allowed in $10 increments;
- Match 4 is compact `4/24`, costs $2/play, and its $10,000 top prize is explicitly **not divided among winners**.

Exact full-cover identity:
- `C(24,4)=10,626` plays;
- face cost **$21,252**;
- deterministic payout **$13,880** (`1×$10,000 + 80×$20 + 1,140×$2`);
- base deterministic return **65.3115%**.

Under the deliberately strongest interpretation that every free promo play can be directed to a distinct uncovered selection, effective cash cost is:

`$21,252 × 10/14 = $15,180`.

Strict promo-covered return:

`$13,880 / $15,180 = 91.4361%`.

Guaranteed pre-cost loss remains **$1,300**.

New fast screen for Match 4:
- required face discount to break even: **>34.6885%**;
- equivalent required free-ticket bonus on paid spend: **>53.1124%**.

Observed Match 4 Happy Hour bonus was only 40% of spend, so even this unusually favorable non-shareable compact game fails.

Current controls:
- Washington Lotto Happy Hour Jun 14–27 2026: buy $5, get $1 free; scalable but only 16.67% effective discount and jackpot sharing remains.
- OLG current 2026 LOTTO 6/49 / LOTTO MAX BOGO: real player-account bonuses but targeted and capped to one bonus, therefore not scalable into full coverage.

Files:
- `research/h135_washington_happy_hour_compact_coverage.md`
- `data/derived/h135_washington_happy_hour_compact_coverage.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H135_APPEND.md`

## Preserved lottery conclusions
- Cash WinFall historical rolldown: genuine historical +EV control, not current guarantee.
- H108 Lotto Texas 2023 near-full acquisition: operationally real; current Texas route legally closed and duplicate jackpot sharing defeats strict guarantee.
- H109-H112 fixed raffle/scratch/sealed-pack standard takeover class materially closed.
- H113-H116 Azerbaijan 4+4 ordinary/realistic carryover guarantee routes materially closed; reopen only on rare high-order zero-category states, major primary-rule improvement, extreme observable sales collapse, or explicit operator-funded addition.
- H114 TezLoto published-state full coverage negative; only empirical RNG/bias route remains, requiring reliable bulk history and >27.78% probability lift out of sample.
- H117-H121 ordinary fixed-board/promo full-takeover screens materially closed.
- H122/H128 Florida fixed-board undersubscription and cumulative early-ticket duration: strong +EV class validated, but no strict guarantee because external tickets can occupy all winning slots.
- H124 lottery loyalty rebate: deterministic but insufficient for guaranteed coverage.
- H129 deterministic all-unsold takeover theorem validated; sampled NC board fails strict floor.
- H130 replenishing Fast Play grids are not depleting inventories; buy-the-pot rejected.
- H131 statewide `Nth` cash coupon: subsidy inversion validated but ownership rejected because unrelated purchases can take coupon-bearing positions.
- H132 purchase-local deterministic free-ticket subsidy: ownership problem solved structurally, but Mega Millions still fails because of unbounded jackpot sharing.
- H133 current capped wallet bonuses: deterministic player-owned subsidy confirmed, but Georgia Cash Pop and WV Daily 3 remain well below strict coverage break-even.
- H134 free random tickets / second-chance entries cannot be counted at face value toward a guaranteed coverage floor; guaranteed-prize subscriptions must be netted against vesting cost.
- H135 scalable BOGO + non-shareable compact coverage validated structurally, but best tested Match 4 package still only reaches **91.4361%** strict return.

## Azerbaijan live branches
- `4+4`: only rare exceptional carryover states / materially better primary rules.
- `TezLoto`: only bulk-history RNG/bias testing on reliable recovered data.
- `Poz-Qazan`: remaining-prize conditional edge remains data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: search recurring/scalable deterministic lottery subsidies above exact compact-game thresholds.** Prioritize promotions with >50% bonus-on-spend, direct ticket discounts, unrestricted wallet credit, fixed per-block cash coupons, or guaranteed retailer-local awards.
2. Pair subsidies first with compact games having fixed, non-shareable payouts. Compute exact deterministic cover ratio `r` and reject immediately unless bonus-on-spend exceeds `1/r - 1` after costs.
3. Specifically monitor Washington Happy Hour and analogous retailer-local offers for Match 4 or other compact games where the subsidy exceeds H135's **53.1124%** threshold or the game has a stronger base coverage ratio.
4. Continue current/upcoming fixed-board raffle monitor with H129 exact worst-case floor and H122/H128 +EV denominator math, prioritizing unusually flat boards and high winner-count/cap ratios.
5. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
6. H007 TezLoto/RNG only upon recovery of reliable bulk history/API; preregister test and require >27.78% out-of-sample probability lift in the best published state.
7. Azerbaijan 4+4 only on materially new primary rules or rare high-order carryover state.
8. Fixed-pack instants only with official guaranteed per-pack minimum/subsidy above exact break-even.
9. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe append packets are authoritative additions where direct replacement of the large master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H135_APPEND.md`.
Latest case: `research/h135_washington_happy_hour_compact_coverage.md`.
