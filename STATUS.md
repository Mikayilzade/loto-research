# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H164 — North Carolina Pick 3 forced Double Draw + 7% retailer commission overlay**.

### H164 major result
North Carolina now provides a stronger recurring analogue to the NJ Green Ball lead.

Current Carolina Pick 3 Pair economics:
- 100 ordered Pair outcomes;
- $0.50 per Pair;
- full Pair cover cost **$50**;
- one drawing guarantees exactly one $25 Pair prize.

NC Pick 3 Double Draw uses a depleting white-ball mechanism. Official NC Lottery announcements have identified nights where only the Yellow Ball remains and a second Pick-3 drawing is therefore **guaranteed**. The latest verified 2026 promotion ran in July 2026.

On such a forced Double Draw evening:
- full Pair cover cost = **$50**;
- first Pick-3 draw guarantees **$25**;
- second Pick-3 draw guarantees **$25**;
- prize-only deterministic gross = **$50 = 100%**.

North Carolina statute G.S. 18C-142 and the current NCEL retailer contract (v. 05-27-2026) set retailer compensation at **7% of the retail price/face value of tickets or shares sold by the retailer**.

If a licensed retailer owner's own otherwise-valid $50 Pick-3 purchase is commission-bearing sales:
- guaranteed prizes = $50;
- retailer commission = **$3.50**;
- conditional deterministic pre-tax total = **$53.50 = 107%**;
- conditional pre-tax profit = **+$3.50**.

Execution is materially stronger than New Jersey because NC Lottery's official FAQ says a retail Pick-3 ticket may be canceled on the issuing terminal, at the purchaser's request, **within 15 minutes of purchase or before draw break, whichever occurs first**. This creates a plausible rollback protocol if any required cover selection fails.

### Why this is NOT SUCCESS
1. **No active forced state today.** Latest identified 2026 Double Draw promotion ended July 31; the mechanism is recurring but currently dormant.
2. **Self-sale commission is not explicit.** Public contract/statute says 7% on tickets sold by retailer, but no public sentence yet confirms that an owner-personal ticket at the owner's licensed store remains commission-bearing sales.
3. **Rollback is not atomic.** The 15-minute cancellation right is strong, but public rules do not guarantee an all-prior-ticket basket rollback under terminal/system outage or similar operational failure.
4. **After-tax floor is unresolved.** The edge is only $3.50/$50 and may involve separate player/retailer tax persons plus 2026 wagering-loss treatment.
5. **Future promotion rules must be revalidated each cycle.**

Status: **PROMISING RECURRING DETERMINISTIC OVERLAY / TERMINAL GUARANTEE NOT YET PROVEN**.

Files:
- `research/h164_nc_pick3_double_draw_retailer_overlay.md`
- `src/loto_research/h164_nc_pick3_double_draw.py`
- `data/derived/h164_nc_pick3_double_draw.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H164_APPEND.md`

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
- H161 New Jersey Green Ball: publicly observable forced state + 100-Pair/$50 exact cover reaches **100% prize gross**.
- H162 official NJ Pick-3 rules lock ordinary retailer economics at 5% of gross sales and 1.25% qualifying prize cashing; conditional forced-state cover becomes 105%-106.25%.
- H163 proves the NJ 100-Pair construction is play-count optimal and requires at least 10 tickets, so atomicity cannot be solved by another published Pick-3 bet type.
- **H164 NC Pick 3 forced Double Draw reaches 100% prize gross and conditionally 107% with the statutory 7% retailer commission; NC also supplies an explicit 15-minute retail cancellation window, making this the strongest current recurring execution architecture, but self-sale/atomic-outage/tax/current-state gates remain.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: investigate NCEL retailer rules/reference material for explicit treatment of retailer-owner self-purchases and whether those valid own-store sales receive the statutory 7% commission.** Do not repeat Pair-cover arithmetic.
2. Search current NC terminal/reference rules for cancellation after intervening ticket transactions: can all earlier Pick-3 tickets still be cancelled within the 15-minute window, and what happens under terminal outage/recovery?
3. Monitor for the next NC Pick 3 Double Draw cycle; reopen immediately as white-ball count approaches zero and verify the current promotion wording before execution.
4. Solve H164 tax/entity floor for plausible lawful retailer structures only after self-sale commission is confirmed.
5. Continue searching cumulative-trigger lottery promotions where forced-state exact coverage reaches 100% and execution can be canceled/rolled back before draw.
6. Continue NJ Green Ball only if batch/rollback or explicit self-sale evidence appears; H163 closed bet-type compression.
7. Continue H159 live/announced fixed-board raffle monitor, especially flat boards whose exact worst-case residual floor approaches or exceeds 100%.
8. Continue BCLC deterministic `X paid + Y free` Keno monitor; reopen on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
9. Continue Nebraska/community scheduled-special recovery where enhanced paytable is fixed before purchase.
10. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
11. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H164_APPEND.md`.
Latest case: `research/h164_nc_pick3_double_draw_retailer_overlay.md`.
