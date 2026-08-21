# STATUS

Updated: 2026-08-21
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H141 — North Carolina checkout-level Lottery Offer architecture**.

### H141 major result
H140 identified the required ordering for a strict subsidy-backed lottery cover:

`lock complete basket + lock subsidy -> commit external cash`.

H141 found the strongest official state-lottery architecture match so far in North Carolina. Current NCEL Online Play Terms explicitly define `Lottery Offers` that can apply to a single game **or the whole shopping cart**, and state that upon qualifying for a **Discount Offer, the ticket is immediately discounted**. A 2026 official campaign (`M4LDEAL26`) separately proves that a lottery promo code can be entered on the Shopping Cart page before completing the purchase.

This materially validates the checkout-level subsidy class and solves the harmful Kentucky-style sequencing **in principle**: a player can potentially verify a purchase-level discount before committing the checkout.

However, no current August 2026 public NCEL purchase-level Discount Offer was found that crosses a compact game's deterministic break-even threshold.

Current NC Pick 3 is also weaker than Kentucky for full coverage:
- Exact: 1,000 × $0.50 = $500 face; one winning Exact pays $250 -> **50% deterministic cover**.
- Pair: 100 × $0.50 = $50 face; one winning Pair pays $25 -> **50% deterministic cover**.

Therefore a subsidy must be **strictly greater than 100% of external cash**, equivalently a checkout discount **strictly greater than 50% of face price**, for positive pre-tax Pick 3 coverage. NCEL's current 100% first-deposit Welcome Offer reaches only theoretical pre-tax break-even and remains a deposit/promo mechanism subject to the same execution/discretion issues already rejected in H140.

Status: **CHECKOUT-LEVEL SUBSIDY ARCHITECTURE VALIDATED / CURRENT SUITABLE >BREAK-EVEN OFFER NOT FOUND / NO SUCCESS**.

Files:
- `research/h141_north_carolina_checkout_offer_architecture.md`
- `data/derived/h141_nc_checkout_thresholds.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H141_APPEND.md`
- prior architecture foundation: `research/h140_kentucky_discretionary_promo_gate_and_prefunding_architecture.md`

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
- **H141 validates a better state-lottery checkout architecture: whole-cart immediate Discount Offers exist in NCEL terms and a 2026 promo used Shopping Cart code entry before purchase; no current >break-even compact-game offer found.**

## Azerbaijan live branches
- `4+4`: only rare exceptional carryover states / materially better primary rules.
- `TezLoto`: only bulk-history RNG/bias testing on reliable recovered data.
- `Poz-Qazan`: remaining-prize conditional edge remains data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: search current player-owned checkout-level Discount/BOGO offers that are visible/applied before payment, and pair them with compact non-shareable games having deterministic full-cover ratio >60%.** Required face discount is `q > 1-r`.
2. Prioritize games with `r >= 2/3` (discount >33.33%) or `r >= .75` (discount >25%); this dramatically widens the set of ordinary checkout promotions that can cross break-even.
3. Search NCEL and other state lotteries for purchase-level offers explicitly applying to Pick 3/4/5 or whole cart, especially repeated `buy X get Y free` campaigns where free numbers are player-selectable.
4. Search for wallet systems where unused external cash remains withdrawable after Bonus award; acceptable sequence is `deposit -> lock Bonus -> test basket -> withdraw principal if basket fails`.
5. Continue fixed-board raffle monitor with H129 worst-case floor and H122/H128 +EV denominator math.
6. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
7. H007 TezLoto/RNG only upon recovery of reliable bulk history/API; preregister and require >27.78% out-of-sample probability lift in the best published state.
8. Azerbaijan 4+4 only on materially new primary rules or rare high-order carryover state.
9. Fixed-pack instants only with official guaranteed per-pack minimum/subsidy above exact break-even.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe append packets are authoritative additions where direct replacement of the large master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H141_APPEND.md`.
Latest case: `research/h141_north_carolina_checkout_offer_architecture.md`.
