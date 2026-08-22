# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H167 — North Carolina retailer-authorized promotional discount + forced Pick 3 Double Draw**.

### H167 major result
NCEL's official Draw Game Rules contain a materially stronger execution architecture than the H166 self-commission theory: subject to governing law/regulation, **retailers may authorize Draw Game ticket sales at a discount for promotional purposes while reporting those discounted sales to NCEL at full gross sales value**.

On an officially forced Pick 3 Double Draw evening:
- 100 Front Pair outcomes × $0.50 = **$50 face cover**;
- each of the two guaranteed drawings necessarily has exactly one covered Front Pair;
- each $0.50 Pair win pays **$25**;
- guaranteed prize gross = **$50**, i.e. base deterministic cover is exactly **100%**.

A retailer promotional discount `d` therefore gives the independent customer a deterministic pre-tax surplus of `50*d`, without requiring the retailer itself to own/claim the tickets.

Because NC retailer compensation is 7% of face value, the retailer's direct ticket margin before other costs is approximately `50*(0.07-d)`. Thus a negotiated discount below 7% can leave both retailer and customer positive before their respective other costs.

Using the deliberately conservative H166 simple C-corp tax screen (21% federal + 2% NC; only 90% of actual wagering cost deductible), customer after-tax model per $50 cover is:

`A(d) = 50d - 0.23*(5 + 45d) = 39.65d - 1.15`.

Break-even discount is **2.9004%**. Examples:
- 3% discount: about **+$0.0395** modeled after tax;
- 5%: **+$0.8325**;
- 6%: **+$1.2290**;
- 7%: **+$1.6255**.

NCEL claim documentation also explicitly allows claim forms in the name of an **individual or legal entity**, materially strengthening the separate C-corp player architecture.

### Why this is NOT SUCCESS
Three execution gates remain:
1. **Forced-state lock:** the Double Draw must be under a current official promotion and already in a state where the second drawing is guaranteed before purchase.
2. **Specific discount lock:** Rule 2.02 authorizes retailer promotional discounts, but terminal proof needs a specific licensed retailer willing to fix the exact discount in advance and confirmation of any current approval/accounting procedure.
3. **Atomicity/rollback:** the 100 Pair selections are not one all-or-none transaction. NCEL number-liability limits can refuse a required selection, and the public 15-minute ticket cancellation rule does not yet prove guaranteed bulk rollback under terminal/power/network interruption.

Status: **STRONG CONDITIONAL DETERMINISTIC OVERLAY / TERMINAL GUARANTEE NOT YET PROVEN**.

Files:
- `research/h167_nc_retail_discount_double_draw.md`
- `data/derived/h167_nc_discount_double_draw.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H167_APPEND.md`

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not current guarantee.
- H108 Lotto Texas 2023: near-full acquisition operationally real; current Texas route legally closed and jackpot sharing blocks strict guarantee.
- H109-H112 fixed raffle/scratch/sealed-pack standard takeover materially closed.
- H113-H116 Azerbaijan `4+4` ordinary/realistic carryover guarantee routes materially closed; reopen only on rare high-order zero-category states, major rule change, extreme observable sales collapse, or explicit external subsidy.
- H114 TezLoto published-state full coverage negative; empirical RNG/bias route remains only with reliable bulk history and >27.78% out-of-sample probability lift.
- H122/H128 Florida fixed-board undersubscription: strong +EV class, no strict guarantee because external tickets can occupy winning slots.
- H129/H159 residual raffle takeovers have exact worst-case forced-slot theorem; sampled boards fail strict floor.
- H130 replenishing Fast Play grids are not depleting inventories.
- H131 statewide Nth-ticket coupons fail ownership because unrelated purchases can take target positions.
- H132 deterministic purchase-local free-ticket ownership is structurally valid, but Mega Millions jackpot sharing blocks strict guarantee.
- H133-H141 wallet/deposit/cart subsidy architectures screened; Kentucky crossed pre-tax break-even mathematically but failed pre-commitment acceptance/entitlement gates.
- H142 Virginia Keno 1-Spot deterministic cover = **75%**; no >25% pre-locked subsidy found.
- H144-H149 Nebraska dynamic-special screening/void architecture developed.
- H150-H153 broader Keno screens: La Vista benchmark **81.0636%**, ordinary state tables remain below strict break-even.
- H154 KenoGO Minor/Major can exceed 100% after state resolution, but the profitable state is unknown until betting closes.
- H155-H156 universal free multiplier would work for some Keno tables, but current promos assign multiplier randomly or charge offsetting surcharge.
- H157 BCLC deterministic `X paid + Y free` architecture is structurally correct; current offer not strong enough.
- H158 Emirates Draw deterministic cart discount validated but EASY6/SURE economics fail strict floor.
- H159 fixed-board residual takeover theorem preserved.
- H160 Michigan cumulative-trigger promotion: forced-red Daily 3 reaches exactly **100% gross**, making compatible pre-locked subsidy sufficient.
- H161-H163 New Jersey Green Ball: forced-state Pair cover reaches 100%; retailer commissions create conditional 105%-106.25%, but atomicity remains unresolved.
- H164 NC Pick 3 Double Draw reaches 100% prize gross and conditionally 107% with 7% retailer commission; cancellation window improves rollback architecture.
- H165 validates retailers may legally play, but broad retailer-play legality should not be retested.
- H166 C-corp same-entity tax salvage remains numerically valid but own-store commission/entity ownership was weak.
- **H167 supersedes the H166 self-play dependency by validating an explicit retailer promotional-discount route. Under the stated C-corp tax screen, any discount >2.9004% makes the forced Double Draw cover positive.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: recover current NCEL retailer procedures/manuals showing how Rule 2.02 promotional discounts are authorized/accounted and whether separate NCEL pre-approval is required for ordinary Pick 3 draw tickets.** Do not repeat the existence of the discount rule; H167 validated it.
2. Recover the active/current Pick 3 Double Draw promotion document and state machine; identify whether a future evening can be known with certainty to contain two drawings before ticket purchase.
3. Search NCEL retailer terminal manuals/support material for multi-ticket or sequence cancellation and outage recovery. Atomic rollback is now the main H167 execution blocker.
4. Search other NCEL cumulative-trigger/forced-second-draw promotions where deterministic base coverage is 100% but requires fewer than 100 selections; this can reduce atomicity risk while retaining the retailer-discount overlay.
5. Continue H159 live/announced fixed-board raffle monitor, prioritizing flat boards near/exceeding 100% worst-case residual floor.
6. Continue BCLC deterministic `X paid + Y free` Keno monitor; reopen on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
7. Continue Nebraska/community scheduled-special recovery where enhanced paytable is fixed before purchase.
8. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
9. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H167_APPEND.md`.
Latest case: `research/h167_nc_retail_discount_double_draw.md`.
