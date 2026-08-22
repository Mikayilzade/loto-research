# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H175 — Rhode Island doubled-Keno 4,336-play hybrid transversal gate**.

### H175 major result
H173/H174's 4,560-play doubled 3-spot construction is no longer the only concrete subproblem outside clique partitions.

Start from the exact break-even `5 x 16` base:
- `5*C(16,3)=2,800` plays;
- worst doubled gross = $2,800;
- the unique count-composition attaining that minimum is `4+4+4+4+4`.

Add six 256-block Latin-square transversal layers across triples of the five groups:
- add-on = 1,536 plays;
- total = **4,336 plays**.

For one transversal layer on groups with draw counts `(a,b,c)`, pair incidence is constant at `ab+ac+bc`, so doubled payout is `5(ab+ac+bc)+35*n3`, where `n3` is the number of fully contained layer blocks.

All **5,005** weak allocations of six layers over the 10 three-group supports were screened against all **10,451** feasible draw count-compositions. A strong allocation is:
- 3 layers on `(0,1,2)`;
- 1 each on `(0,3,4)`, `(1,3,4)`, `(2,3,4)`.

For this allocation:
- every non-balanced composition has pair-only gross at least **$4,370 > $4,336**;
- balanced `4+4+4+4+4` has pair-only gross **$4,240**;
- therefore the entire guarantee reduces to one exact condition: across the six layers, every balanced draw must contain at least **3 full transversal triples**;
- if `n3>=3` universally, worst gross is at least **$4,345**, ratio **100.2076%**, surplus **+$9**.

A first natural GF(16) affine realization was tested by exact binary MILP. Using coefficients `1,2,4` on the three `(0,1,2)` layers and coefficient `1` on each other support, the adversarial balanced minimum is **n3=0**. That concrete realization is rejected.

Status: **NEW 4,336-PLAY CANDIDATE CLASS / ALL NON-BALANCED COMPOSITIONS CLOSED POSITIVE FOR ONE SUPPORT ALLOCATION / BALANCED UNIVERSAL n3>=3 DESIGN STILL OPEN / FIRST AFFINE REALIZATION REJECTED**.

Files:
- `research/h175_ri_keno_hybrid_4336_transversal_gate.md`
- `src/loto_research/h175_ri_keno_hybrid_transversal.py`
- `data/derived/h175_ri_keno_hybrid_summary.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H175_APPEND.md`

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
- H154 KenoGO Minor/Major can exceed 100% after state resolution, but profitable state is unknown until betting closes.
- H155-H156 universal free multiplier would work for some Keno tables, but current promos assign multiplier randomly or charge offsetting surcharge.
- H157 BCLC deterministic `X paid + Y free` architecture is structurally correct; current offer not strong enough.
- H158 Emirates Draw deterministic cart discount validated but EASY6/SURE economics fail strict floor.
- H159 fixed-board residual takeover theorem preserved.
- H160 Michigan cumulative-trigger promotion: forced-red Daily 3 reaches exactly **100% gross**, making compatible pre-locked subsidy sufficient.
- H161-H163 New Jersey Green Ball: forced-state Pair cover reaches 100%; retailer commissions create conditional 105%-106.25%, but atomicity remains unresolved.
- H164-H169 North Carolina forced Pick 3 Double Draw reaches 100% gross and retailer-discount economics can be positive, but current public rules allow liability-limit refusal and lack whole-basket atomic rollback; strict guarantee rejected.
- H170 Barbados Pick 3 Mega Ball Pair cover reaches **106% in successful-MB state**, but MB success is random; strict floor 26.5%.
- H171 Jamaica Cash Pot + Mega reaches **136.11% in Gold state**, but modifier state is random after purchase; strict floor 38.89%.
- H172 Rhode Island proves that lottery-issued 2x entitlement can be printed/locked before the draw; naive doubled 3-spot full space = **138.7537% conditional**, but 82,160 plays are operationally too large and current 2026 promo terms remain unresolved.
- H173 reduces that conditional strict doubled cover to **4,560 plays / 109.6491% worst-case pre-tax** using four 20-number triple cliques.
- H174 exhaustively screens **411,498** clique partitions with 1–8 groups and proves 4×20 is the cheapest strict-positive member; Keno Plus cannot currently be treated as a known pre-purchase multiplier state.
- **H175 identifies a 4,336-play hybrid candidate: one support allocation makes every non-balanced draw strict-positive by pair counting; only balanced draws need a universal three-full-block property. First GF(16) affine realization fails with exact MILP minimum n3=0.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest mathematical priority: solve the H175 balanced transversal gate.** Search six-layer non-affine/mixed Latin designs satisfying `n3>=3` for every balanced `4+4+4+4+4` draw, using MILP/CP-SAT/cutting planes. If impossible, prove a counterbound and close the 4,336 class.
2. Recover official 2026 Rhode Island `Kick Back with Keno` rules and current primary RI 3-spot paytable. Any H173-H175 construction remains conditional until a current free deterministic pre-locked 2x is proven.
3. Recover Rhode Island terminal/ticket mechanics: distinct 3-spot selections per ticket/transaction, future-draw targeting and throughput.
4. If H175 fails, search other non-clique block/cyclic designs below 4,560 plays.
5. Search current pre-printed/pre-locked free doublers in lotteries with smaller state spaces than 80-number Keno.
6. Continue BCLC deterministic `X paid + Y free` Keno monitor; reopen on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
7. Continue Nebraska/community fixed scheduled-special recovery and H159 fixed-board raffle monitor.
8. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
9. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H175_APPEND.md`.
Latest case: `research/h175_ri_keno_hybrid_4336_transversal_gate.md`.
