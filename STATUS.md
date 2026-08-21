# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H163 — New Jersey Pick-3 Green Ball atomicity lower bound**.

### H163 major result
H162's multi-ticket execution problem is now proven structural under the current official Pick-3 bet menu.

Current official Pick-3 rules give maximum positive-prize support per Play:
- Straight: 1 of 1,000 ordered outcomes;
- 3-way Box/Wheel: <=3;
- 6-way Box/Wheel: <=6;
- Pair: **10**.

Therefore any portfolio that guarantees at least one positive-prize Play for every Pick-3 outcome needs at least:

`ceil(1000 / 10) = 100 Plays`.

The 100 ordered Pair bets used in H161/H162 attain this bound exactly, so the cover is play-count optimal.

Because a Pick-3 Ticket can contain at most **10 Plays**, any exact all-outcome cover requires at least:

`ceil(100 / 10) = 10 Tickets`.

Thus no published Straight/Wheel/Box/Pair redesign can compress the forced Green Ball deterministic cover into one ticket or fewer than ten tickets. The second forced Green Ball draw cannot cure this: one ticket covers at most 100 outcomes and leaves at least 900 uncovered.

### Why this is NOT SUCCESS
1. **Atomicity remains unresolved and is now structural.** At least 10 tickets are required. Official rules allow liability-based refusal of later wagers and only say a Ticket may be cancelled `at the time of purchase`; they do not guarantee rollback of all earlier completed tickets if a later required ticket fails.
2. **Self-sale commission is still not explicit.** Public evidence remains strong: NJ Lottery says retailers earn 5% on every ticket sold; Pick-3 rules mandate 5% on gross sales; retailer owners may lawfully play and NJ Lottery has documented an owner buying for himself at his own store. But no public accounting/audit sentence explicitly classifies an owner-personal ticket at the owner's licensed entity as commission-bearing gross sales.
3. **Green Ball is not currently active.** Latest cycle ended August 2, 2026.
4. **Promotion irrevocability and tax/entity floor remain unresolved.**

Status: **ONE-TICKET COMPRESSION REJECTED / 10-TICKET MINIMUM PROVEN / H162 COMMISSION OVERLAY STILL PROMISING BUT NON-TERMINAL**.

Files:
- `research/h163_nj_green_ball_atomicity_lower_bound.md`
- `src/loto_research/h163_nj_pick3_support_bound.py`
- `data/derived/h163_nj_pick3_support_bound.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H163_APPEND.md`

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
- H162 official Pick-3 rules lock ordinary retailer economics at 5% of gross sales and 1.25% qualifying prize cashing; conditional forced-state cover becomes 105%-106.25%.
- **H163 proves the 100-Pair construction is play-count optimal and requires at least 10 tickets, so NJ Green Ball atomicity cannot be solved by a different published Pick-3 bet type.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: search official NJ terminal/retailer manuals or written retailer-support material for a true multi-ticket batch transaction/reservation or explicit guaranteed rollback of all earlier tickets in the same requested basket.** Do not repeat bet-type compression; H163 closed it.
2. Search another cumulative-trigger lottery promotion whose forced-state exact coverage fits in one ticket or one atomic system transaction.
3. Search lottery jurisdictions where licensed retailers may personally play and where commission on owner/employee self-purchased valid tickets is explicitly stated.
4. During future NJ Green Ball cycles monitor the publicly displayed remaining-white-ball count; reopen only at `k=6` and only if atomicity/self-sale gates are solved.
5. Continue H159 live/announced fixed-board raffle monitor, especially flat boards whose exact worst-case residual floor approaches or exceeds 100%.
6. Continue BCLC deterministic `X paid + Y free` Keno monitor; reopen on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
7. Continue Nebraska/community scheduled-special recovery where enhanced paytable is fixed before purchase.
8. Search compatible deterministic discounts/free-play around Michigan forced-red Daily 3 and other forced-second-draw promotions.
9. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H163_APPEND.md`.
Latest case: `research/h163_nj_green_ball_atomicity_lower_bound.md`.
