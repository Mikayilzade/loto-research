# STATUS

Updated: 2026-08-21
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H142 — Virginia Keno 75% deterministic 1-Spot cover + Rewards/free-play threshold**.

### H142 major result
A materially better compact fixed-prize coverage game has been validated from current official Virginia Lottery rules.

Virginia Keno 1-Spot:
- field: 80 numbers;
- exactly 20 numbers drawn;
- $1 wager on one number;
- a hit pays fixed **$3**;
- official rules state only the 10-Spot match-10 tier can become pari-mutuel; **all other tier payout values are fixed**.

Therefore buying all 80 distinct 1-Spot numbers for the same drawing has the exact deterministic identity:
- face cost **$80**;
- exactly 20 winners in every possible draw;
- guaranteed gross **20 × $3 = $60**;
- deterministic full-cover ratio **75%**.

This is stronger than Kentucky Pick 3 (60%) and NC Pick 3 (50%). The exact purchase-level subsidy threshold is now only:

`q > 25% of face`, equivalently more than **$20 of pre-locked Keno-usable free play** on the $80 basket.

Virginia Rewards also provides a relevant live subsidy architecture:
- Keno is explicitly eligible;
- eligible computer-generated purchases earn 5 points per $1;
- 250 points redeem a coupon for a free play of a Lottery product;
- up to 5,000 points/month may be redeemed for free plays;
- retail redemption can use vending-machine credit or a draw-game coupon.

However no current public rule found in H142 establishes more than $20 of **pre-committed Keno-usable value** for one $80 basket. Same-spend points post only after purchase, and the exact Keno denomination/value represented by each 250-point coupon remains insufficiently specified in the public evidence retrieved.

Execution also remains open: Keno uses one play per ticket, draws every four minutes, and the rules contemplate unaccepted plays/refunds. All 80 required selections must be valid for the same draw before the $60 floor exists.

Status: **75% FIXED-PAYOUT COVER VALIDATED / >25% PRE-COMMITTED SUBSIDY NOT YET FOUND / NO SUCCESS**.

Files:
- `research/h142_virginia_keno_75pct_cover_rewards_threshold.md`
- `data/derived/h142_virginia_keno_subsidy_thresholds.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H142_APPEND.md`
- prior checkout architecture: `research/h141_north_carolina_checkout_offer_architecture.md`

## Preserved lottery conclusions
- Cash WinFall historical rolldown: genuine historical +EV control, not current guarantee.
- H108 Lotto Texas 2023 near-full acquisition: operationally real; current Texas route legally closed and duplicate jackpot sharing defeats strict guarantee.
- H109-H112 fixed raffle/scratch/sealed-pack standard takeover class materially closed.
- H113-H116 Azerbaijan 4+4 ordinary/realistic carryover guarantee routes materially closed; reopen only on rare high-order zero-category states, major primary-rule improvement, extreme observable sales collapse, or explicit operator-funded addition.
- H114 TezLoto published-state full coverage negative; only empirical RNG/bias route remains, requiring reliable bulk history and >27.78% probability lift out of sample.
- H117-H121 ordinary fixed-board/promo full-takeover screens materially closed.
- H122/H128 Florida fixed-board undersubscription: strong +EV class validated, but no strict guarantee because external tickets can occupy all winning slots.
- H124 lottery loyalty rebate: deterministic but insufficient for guaranteed coverage.
- H129 deterministic all-unsold takeover theorem validated; sampled NC board fails strict floor.
- H130 replenishing Fast Play grids are not depleting inventories; buy-the-pot rejected.
- H131 statewide `Nth` cash coupon: subsidy inversion validated but ownership rejected because unrelated purchases can take coupon-bearing positions.
- H132 purchase-local deterministic free-ticket subsidy: ownership solved structurally, but Mega Millions fails because of unbounded jackpot sharing.
- H133 current capped wallet bonuses: deterministic player-owned subsidy confirmed, but tested compact games remain below strict break-even.
- H134 free random tickets / second-chance entries cannot be counted at face value toward guaranteed floor.
- H135 scalable BOGO + non-shareable compact coverage validated structurally, but best tested Washington Match 4 package reaches only 91.4361% strict return.
- H136-H139 Kentucky current 100%/stacked deposit promos create positive conditional cover arithmetic, but H140 closes the current terminal-guarantee route because promo entitlement itself is discretionary before nonwithdrawable funding and wager acceptance is not locked.
- H141 validates whole-cart immediate Discount Offer architecture in North Carolina, but no current >break-even compact-game offer was found.
- **H142 validates Virginia Keno 1-Spot as a 75% fixed-payout deterministic cover, reducing the required pre-committed subsidy to only >25%; no current locked subsidy above that threshold has yet been verified.**

## Azerbaijan live branches
- `4+4`: only rare exceptional carryover states / materially better primary rules.
- `TezLoto`: only bulk-history RNG/bias testing on reliable recovered data.
- `Poz-Qazan`: remaining-prize conditional edge remains data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: pair Virginia Keno 1-Spot's 75% deterministic fixed payout with a current player-owned subsidy strictly above 25% that is visible/locked before uncovered cash is committed.** Search Virginia purchase promos, Rewards coupon denominations, direct discounts, vending-machine credits and checkout offers.
2. Determine the exact Keno value/wager represented by a **250-point Rewards free-play coupon** and whether multiple coupons can fund distinct 1-Spot selections for one drawing. If pre-existing/redeemed free play can exceed $20 on the same $80 cover, test execution immediately.
3. Test Virginia digital playslip/terminal batching and same-draw cutoff: can all 80 1-Spot selections be prepared/accepted reliably before a four-minute drawing? Preserve the fixed-payout theorem; do not repeat its math.
4. Search compact non-shareable fixed-prize games with deterministic coverage ratio **>75%**. A game with ratio `r` requires only a face subsidy `q > 1-r`.
5. Continue state-lottery checkout-level Discount/BOGO monitor, especially whole-cart player-selectable offers.
6. Continue fixed-board raffle monitor with H129 worst-case floor and H122/H128 +EV denominator math.
7. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
8. H007 TezLoto/RNG only upon recovery of reliable bulk history/API; preregister and require >27.78% out-of-sample probability lift in the best published state.
9. Azerbaijan 4+4 only on materially new primary rules or rare high-order carryover state.
10. Fixed-pack instants only with official guaranteed per-pack minimum/subsidy above exact break-even.
11. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe append packets are authoritative additions where direct replacement of the large master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H142_APPEND.md`.
Latest case: `research/h142_virginia_keno_75pct_cover_rewards_threshold.md`.
