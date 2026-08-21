# STATUS

Updated: 2026-08-21
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H161 — New Jersey Pick-3 Green Ball forced-state + retailer commission corollary**.

### H161 major result
New Jersey provides a stronger recurring implementation of the forced-second-draw idea from H160.

Official 2026 Pick-3 Green Ball rules use **six white balls + one green ball**; each white ball is removed after selection. When the green ball is selected, the same Pick-3 wager gets a second full-prize Pick-3 draw and the machine resets. Official 2025 material says the NJ Lottery homepage displays the **number of white balls remaining**, so the state is observable before purchase.

At `k=6` (all six whites already removed), the next Green Ball draw is certain before betting closes.

Current Pick-3 Pair full-cover arithmetic:
- 100 ordered Pair outcomes;
- $0.50 per Pair;
- full-cover face cost **$50**;
- one draw guarantees one $25 Pair winner = **50% gross**;
- forced Green Ball state guarantees two full draws, hence **$25 + $25 = $50 = 100% gross**.

This is operationally much smaller than H160's 1,000-line/$500 Straight cover.

New lottery-specific subsidy layer:
- NJ Full Service Retailer terms publicly advertise **5% commission on every ticket sold**;
- retailers also receive **1.25% payout commission on prizes up to $600**;
- an official 2023 NJ Lottery release documents licensed retailer owner Jay Shortway purchasing a lottery ticket for himself at his own restaurant/lottery location and being recognized as the winner.

If ordinary commissions apply to a retailer owner's own forced-Green Pair-cover purchases:
- prize gross = $50;
- sales commission = $2.50;
- payout commission = $0.625;
- face spend = $50;
- conditional pre-tax deterministic surplus = **+$3.125 = +6.25%**.

This is the first forced-second-draw branch where an ordinary lottery retailer compensation layer can mathematically push exact deterministic coverage above 100% without a separate player coupon.

### Why this is NOT SUCCESS
1. Public rules do not expressly state that the 5% sales and 1.25% payout commissions are guaranteed on a retailer owner's own strategically purchased basket; self-purchase is demonstrated, commission entitlement on self-sale is not.
2. 2026 Green Ball rules let the Lottery cancel/terminate/modify/suspend the promotion without prior notice, including for payout-budget reasons; strict post-ticket irrevocability is not proven.
3. Pick-3 rules allow further wagers on a number to be refused when internal liability limits are reached; whole-basket acceptance still must be locked.
4. Green Ball rules expressly prohibit combination with another NJ Lottery promotion/coupon, closing the obvious coupon-stacking route.
5. The +$3.125 pre-tax margin is small enough that 2026 federal/state tax treatment can erase it in some taxpayer/entity configurations.
6. Latest Green Ball cycle ran July 6-August 2, 2026 and is not active today, although official releases show the architecture has recurred repeatedly in 2025-2026.

Status: **FORCED STATE + 100% PAIR COVER VALIDATED / RETAILER OVERLAY PROMISING / COMMISSION-ENTITLEMENT + IRREVOCABILITY + TAX GATED / NO CURRENT SUCCESS**.

Files:
- `research/h161_nj_green_ball_forced_state_retailer_commission.md`
- `src/loto_research/h161_nj_green_ball_pair_cover.py`
- `data/derived/h161_nj_green_ball_pair_cover.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H161_APPEND.md`

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not current guarantee.
- H108 Lotto Texas 2023: near-full acquisition operationally real; current Texas route legally closed and jackpot sharing blocks strict guarantee.
- H109-H112 fixed raffle/scratch/sealed-pack standard takeover materially closed.
- H113-H116 Azerbaijan `4+4` ordinary/realistic carryover guarantee routes materially closed; reopen only on rare high-order zero-category states, major rule change, extreme observable sales collapse, or explicit external subsidy.
- H114 TezLoto published-state full coverage negative; empirical RNG/bias route remains only with reliable bulk history and >27.78% out-of-sample probability lift.
- H122/H128 Florida fixed-board undersubscription: strong +EV class, no strict guarantee because external tickets can occupy winning slots.
- H129/H159 residual raffle takeovers now have exact worst-case forced-slot theorem; Virginia 2026 high-winner board fails every possible sales state.
- H130 replenishing Fast Play grids are not depleting inventories.
- H131 statewide Nth-ticket coupons fail ownership because unrelated purchases can take target positions.
- H132 deterministic purchase-local free-ticket ownership is structurally valid, but Mega Millions jackpot sharing blocks strict guarantee.
- H133-H141 multiple wallet/deposit/cart subsidy architectures screened; Kentucky crossed pre-tax break-even mathematically but failed pre-commitment acceptance/entitlement gates.
- H142 Virginia Keno 1-Spot deterministic cover = **75%**; no >25% pre-locked subsidy found.
- H144-H149 Nebraska dynamic-special screening/void architecture developed.
- H150-H153 broader Keno screens: La Vista benchmark **81.0636%**, ordinary state tables remain below strict break-even.
- H154 KenoGO Minor/Major can exceed 100% after state resolution, but the profitable state is unknown until betting closes.
- H155-H156 universal free multiplier would work for some Keno tables, but current promos assign multiplier randomly or charge offsetting surcharge.
- H157 BCLC deterministic `X paid + Y free` architecture is structurally correct; current offer not strong enough.
- H158 Emirates Draw deterministic cart discount validated but EASY6/SURE economics fail strict floor.
- H159 fixed-board residual takeover theorem: if `e<W`, exact strict floor is the sum of the `W-e` cheapest prizes; if `e>=W`, floor is zero.
- H160 Michigan cumulative-trigger promotion: forced-red Daily 3 reaches exactly **100% gross**, making any compatible subsidy sufficient before tax/friction.
- **H161 New Jersey Green Ball provides a publicly observable forced state and a much smaller 100-Pair/$50 exact cover; published retailer compensation conditionally lifts it to +6.25% pre-tax if self-sale commissions are contractually earned.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: obtain official NJ retailer agreement/manual/rule evidence on whether the 5% sales and 1.25% payout commissions apply to tickets personally purchased by the licensed retailer/owner/employee.** Self-purchase is already officially demonstrated; commission entitlement is the missing structural lock.
2. Determine whether an already-issued Green Ball-eligible ticket has an irrevocable contractual right to the bonus draw if the Lottery later cancels/modifies the promotion under its discretionary clause.
3. During future NJ Green Ball cycles monitor the publicly displayed remaining-white-ball count; reopen immediately at `k=6` and test whole-basket Pair acceptance before cutoff.
4. Search other cumulative-trigger Pick-3/number-game promotions where the forced state is observable before purchase and retailer/player discounts are expressly non-discretionary.
5. Search lottery jurisdictions whose licensed retailers may personally play and where commissions on self-purchased tickets are expressly covered in public contracts/manuals.
6. Continue H159 live/announced fixed-board raffle monitor, especially boards whose full-board payout ratio is near/above 100%.
7. Continue BCLC deterministic `X paid + Y free` Keno monitor; reopen on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
8. Continue Nebraska/community scheduled-special recovery where enhanced paytable is fixed before purchase.
9. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
10. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
11. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H161_APPEND.md`.
Latest case: `research/h161_nj_green_ball_forced_state_retailer_commission.md`.
