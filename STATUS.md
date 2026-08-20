# STATUS

Updated: 2026-08-21
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H140 — Kentucky discretionary-promotion gate + pre-funding acceptance architecture**.

### H140 major result
H136-H139 found the first current lottery subsidy large enough to turn a compact fixed-prize full cover mathematically positive: Kentucky's August 2026 100% first-deposit match combined with Pick 3 Pair coverage (`$50 face -> guaranteed $30 gross`). H139 conditionally raised the pre-tax margin to as much as +$90 if concurrent Kentucky deposit/referral offers stack.

H140 found a stronger upstream blocker in the current official Kentucky iLottery terms:
- promotional offers are explicitly **discretionary**;
- the player has **no right to receive or redeem any specific offer**;
- offers may be cancelled at any time without notice;
- KLC disclaims loss from delay/error/failure to make or accept an offer;
- ordinary deposited funds are nonwithdrawable/nonrefundable;
- KLC may refuse attempted purchases and limit a wager on a particular number set at any time without notice.

Therefore the lawful sequence remains:

`irreversible deposit -> discretionary Bonus outcome -> attempted cover acceptance`.

A strict SUCCESS theorem requires:

`locked subsidy + locked complete basket -> external cash commitment`.

Thus **Kentucky H136-H139 is now CLOSED as a terminal guarantee under current published terms even if future evidence proves promo stacking**. Stackability is no longer the decisive blocker and should not consume more runs unless Kentucky's terms/process materially change.

H140 also formalized the subsidy threshold for any deterministic fixed-prize complete cover with ratio `r`:

`profit = r(D+B) - D`, so positive pre-tax floor requires `B/D > 1/r - 1`.

For Kentucky Pick 3 Pair (`r=.60`) the deterministic subsidy threshold is **>66.6667%**, not necessarily 100%.

A useful architecture control was found in the current Virginia Lottery FAQ: draw-game tickets can be assembled in a shopping cart and paid at checkout by one-time debit, and the cart can be cleared before purchase. This proves that **pre-funding basket construction is a real state-lottery architecture**, but H140 did not find a current Virginia deterministic draw-game subsidy large enough to cross the exact coverage threshold.

Status: **NO SUCCESS / KENTUCKY CURRENT PROMO GUARANTEE CLOSED / CHECKOUT-LEVEL SUBSIDY CLASS PRIORITIZED**.

Files:
- `research/h140_kentucky_discretionary_promo_gate_and_prefunding_architecture.md`
- `data/derived/h140_prefunding_architecture_thresholds.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H140_APPEND.md`
- previous foundation: `research/h136_kentucky_100pct_bonus_pick3_cover.md` through `research/h139_kentucky_concurrent_deposit_promo_stack.md`

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
- H136-H139 Kentucky current 100%/stacked deposit promos create positive **conditional** cover arithmetic, but H140 now closes the current terminal-guarantee route because promo entitlement itself is discretionary before nonwithdrawable funding and wager acceptance is not locked.

## Azerbaijan live branches
- `4+4`: only rare exceptional carryover states / materially better primary rules.
- `TezLoto`: only bulk-history RNG/bias testing on reliable recovered data.
- `Poz-Qazan`: remaining-prize conditional edge remains data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: search current state-lottery checkout-level deterministic promos/discounts where the full draw-game basket is assembled before payment and the subsidy is automatically applied in the same transaction.** This directly solves the H140 ordering problem.
2. Search compact fixed-prize non-shareable games with deterministic full-cover ratio **>60%**. Use threshold theorem `required bonus/cash > 1/r - 1`; e.g. `r=2/3` needs >50%, `r=.75` needs >33.33%.
3. Search lottery wallets where unused cash principal is withdrawable after Bonus award; acceptable order is `deposit -> Bonus lock -> basket test -> withdraw principal if coverage fails`.
4. Search player-owned BOGO/direct-ticket promotions that apply automatically at checkout rather than discretionary post-deposit Bonus credit.
5. Continue fixed-board raffle monitor with H129 worst-case floor and H122/H128 +EV denominator math.
6. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
7. H007 TezLoto/RNG only upon recovery of reliable bulk history/API; preregister and require >27.78% out-of-sample probability lift in the best published state.
8. Azerbaijan 4+4 only on materially new primary rules or rare high-order carryover state.
9. Fixed-pack instants only with official guaranteed per-pack minimum/subsidy above exact break-even.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe append packets are authoritative additions where direct replacement of the large master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H140_APPEND.md`.
Latest case: `research/h140_kentucky_discretionary_promo_gate_and_prefunding_architecture.md`.
