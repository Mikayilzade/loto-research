# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H162 — New Jersey Pick-3 Green Ball retailer commission entitlement materially strengthened**.

### H162 major result
H161's retailer layer is now supported directly by the official Pick-3 game rules rather than only a generic retailer marketing page.

Official Pick-3 §8(b) states:
- Retailers **will receive 5% of gross sales dollars**;
- all Retailers paying qualifying cash prizes up to $599.50 **shall receive 1.25% of money paid out in prizes**.

The same rules say cancelled Pick-3 bets earn no commission, and N.J.A.C. 17:20-6.1(c) requires an agent to remit face value less commissions/bonuses/reimbursements to which the agent is entitled.

At the forced Green Ball state `k=6`:
- 100 Pair outcomes × $0.50 = **$50 face**;
- regular draw guarantees one $25 Pair winner;
- forced Green Ball second draw guarantees a second $25 Pair winner;
- prize floor = **$50 = 100% gross**.

If a licensed retailer owner's valid personal basket is commission-bearing gross sales:
- 5% sales commission = **$2.50**;
- conditional pre-tax floor = **+$2.50 = +5.00%**.

If the same retailer can also validly cash the $50 of sub-$600 prizes at its location:
- 1.25% cashing commission = **$0.625**;
- conditional pre-tax floor = **+$3.125 = +6.25%**.

This is a material strengthening: the commission itself is now primary-source game-rule based.

### Why this is NOT SUCCESS
1. No public source found yet that says verbatim that a retailer owner's own personal ticket purchase through that retailer's terminal is included in commissionable `gross sales dollars`. Self-purchase is lawful/not prohibited and an official owner self-purchase winner case exists, but terminal proof still needs explicit self-sale treatment.
2. A Pick-3 ticket supports at most 10 Plays, so the 100-Pair cover needs at least 10 tickets. Tickets can be cancelled only `at the time of purchase`; public rules do not establish an atomic 10-ticket transaction or guaranteed rollback of earlier tickets if a later required number is refused by liability limits.
3. Green Ball rules allow cancellation/termination/modification/suspension without prior notice and discretionary retailer disqualification. No vested-right rule for already-issued eligible tickets was found.
4. Latest Green Ball cycle ended August 2, 2026; architecture is recurring but not active today.
5. Tax/entity treatment can erase a small margin; no universal after-tax floor is proven.

Status: **FORCED-STATE 100% PRIZE FLOOR VALIDATED / 5% + 1.25% COMMISSION RULE PRIMARY-SOURCE VALIDATED / SELF-SALE + ATOMICITY + IRREVOCABILITY + TAX + ACTIVE-CYCLE GATED / NO SUCCESS**.

Files:
- `research/h162_nj_green_ball_retailer_commission_lock.md`
- `src/loto_research/h162_nj_retailer_greenball.py`
- `data/derived/h162_nj_greenball_retailer_scenarios.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H162_APPEND.md`

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
- **H162 official Pick-3 rules now lock ordinary retailer economics at 5% of gross sales and 1.25% of qualifying prize cashing; conditional forced-state cover becomes 105%-106.25%, but explicit self-sale classification and execution gates remain.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: find explicit NJ retailer agreement/manual/accounting/audit evidence that valid lottery tickets personally purchased by the licensed retailer/owner at its own terminal are included in commissionable gross sales dollars.**
2. Search NJ terminal/manual rules for a batch transaction or cancellation workflow that can atomically issue or fully rollback all ten Pick-3 tickets needed for the 100-Pair cover if any required number is refused.
3. Determine whether already-issued Green Ball-eligible tickets acquire vested/irrevocable second-draw rights despite later promotion cancellation/modification.
4. During future Green Ball cycles monitor the publicly displayed remaining-white-ball count; reopen execution immediately at `k=6`.
5. Search other cumulative-trigger Pick-3/number-game promotions where the forced state is observable and exact coverage can fit in one ticket/system transaction.
6. Search lottery jurisdictions whose licensed retailers may personally play and where commission on self-purchased valid tickets is expressly stated.
7. Continue H159 live/announced fixed-board raffle monitor, especially boards whose full-board payout ratio is near/above 100%.
8. Continue BCLC deterministic `X paid + Y free` Keno monitor; reopen on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
9. Continue Nebraska/community scheduled-special recovery where enhanced paytable is fixed before purchase.
10. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
11. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H162_APPEND.md`.
Latest case: `research/h162_nj_green_ball_retailer_commission_lock.md`.
