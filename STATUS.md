# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H184 — exact rejection of the current H183 master candidate**.

### H184 major result
H184 resumed H183 from its persisted 254-cut state without repeating prior tests and attacked the exact unresolved master ids recorded by H183:

`[[3,16,94],[1],[9],[16]]`.

This corresponds to six diagonal cyclic-affine transversal layers `z=a*x+a*y+c (mod 16)`:
- support `(0,1,2)`: `(a,c)=(1,3),(3,0),(11,14)`;
- support `(0,3,4)`: `(1,1)`;
- support `(1,3,4)`: `(1,9)`;
- support `(2,3,4)`: `(3,0)`.

An independently reconstructed exact separator MILP (80 symbol binaries + 1,536 hit binaries; exactly four symbols per group; total completed transversal triples constrained `<=2`) returned HiGHS status **Optimal** in about 2.43 seconds.

Exact balanced counterexample:

`[[1,5,7,14],[4,6,9,13],[2,3,9,15],[1,8,11,15],[2,4,11,15]]`

Exact score: **`n3=2`**. Only two transversal triples are completed, both on support `(0,1,2)`:
- layer `(a,c)=(1,3)`: `(7,9,3)`;
- layer `(a,c)=(3,0)`: `(1,4,15)`.

Therefore the current H183 master candidate violates the necessary H175 universal condition `n3>=3` and is rejected exactly.

Persistent continuation state:
- H183 bank: 254 necessary cuts;
- H184 delta: 1 new exact cut;
- known total after merge: **255 cuts**;
- restricted diagonal cyclic-affine family: **still OPEN until the master is re-solved with cut 255**.

Files:
- `research/h184_h183_current_master_exact_rejection.md`
- `data/derived/h184_h183_new_witnesses.json`
- `src/loto_research/h184_h183_current_candidate_break.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H184_APPEND.md`

### H183 preserved result
H183 added exact WLOG symmetry reduction to H180's diagonal cyclic-affine family, reducing representative orientations from 715,917,361,152 to 22,547,202,048 (~31.75x). It generated 246 adaptive explicit counterexamples and persisted 254 total cuts. The master remained feasible at that checkpoint; H184 has now exactly rejected the recorded next master candidate.

### H182 preserved result
Current August 2026 Michigan Club Keno Tripler Time is closed as an ex-ante guaranteed subsidy: Doubler/Tripler tags are assigned to random paid tickets and no finite forced-issuance bound is published. Tagged-ticket states remain conditional overlays only.

### H175-H180 preserved result
- H175: 4,336-play doubled 3-spot hybrid; all non-balanced draw compositions are strict-positive; balanced draws require universal `n3>=3`.
- H178/H179: broad concrete cyclic/XOR/isotopy screens repeatedly found exact `n3<=2` witnesses; timeout never counts as validation.
- H180: first adaptive exact master/separator architecture.
- H183/H184: persistent cutting-plane continuation with symmetry reduction; 255 necessary balanced cuts are now known, and the latest recorded candidate is rejected.

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
- H142 Virginia Keno 1-Spot deterministic cover = 75%; no >25% pre-locked subsidy found.
- H144-H149 Nebraska dynamic-special screening/void architecture developed.
- H150-H153 broader Keno screens: La Vista benchmark 81.0636%; ordinary state tables remain below strict break-even.
- H154 KenoGO Minor/Major can exceed 100% after state resolution, but profitable state is unknown until betting closes.
- H155-H156 universal free multiplier would work for some Keno tables, but current promos assign multiplier randomly or charge offsetting surcharge.
- H157 BCLC deterministic `X paid + Y free` architecture is structurally correct; current offer not strong enough.
- H158 Emirates Draw deterministic cart discount validated but EASY6/SURE economics fail strict floor.
- H160 Michigan cumulative-trigger promotion: forced-red Daily 3 reaches exactly 100% gross, making compatible pre-locked subsidy sufficient.
- H161-H163 New Jersey Green Ball: forced-state Pair cover reaches 100%; retailer commissions create conditional 105%-106.25%, but atomicity remains unresolved.
- H164-H169 North Carolina forced Pick 3 Double Draw reaches 100% gross and retailer-discount economics can be positive, but liability-limit refusal / whole-basket rollback block strict guarantee.
- H170 Barbados Pick 3 Mega Ball Pair cover reaches 106% in successful-MB state, but MB success is random.
- H171 Jamaica Cash Pot + Mega reaches 136.11% in Gold state, but modifier state is random after purchase.
- H172 Rhode Island proves a lottery-issued 2x entitlement can be printed/locked before the draw; current 2026 exact promo terms remain unresolved.
- H173 gives a conditional 4,560-play / 109.6491% doubled 3-spot worst-case cover.
- H174 proves 4x20 is the cheapest strict-positive member among 411,498 tested clique partitions.
- H175 identifies the 4,336-play transversal hybrid and universal balanced `n3>=3` gate.
- H176-H177 leave current RI free-doubler terms/execution unresolved and reject ordinary paid Keno Plus as a substitute.
- H178-H184 continue exact search of the 4,336-play gate; no universal design or impossibility proof yet.
- H181-H182 validate Michigan's current free pre-draw multiplier architecture but close random tag acquisition as a strict-guarantee source.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: merge H184's exact delta witness with H183's persisted 254-cut bank, solve the 255-cut symmetry-reduced master, and immediately separate the new candidate.** Continue until restricted-master infeasibility or independently certified exact-separator infeasibility.
2. Persist subsequent witnesses in a merged/appendable bank so later runs never restart from H183.
3. Add only mathematically safe symmetry/orbit cuts or valid inequalities; solver timeout is never validation.
4. If the diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod 16)` with independent odd `a,b` (1,024 layers/support), reusing all valid balanced witnesses.
5. General H175 remains open until a construction or impossibility theorem covers arbitrary allowed Latin/transversal designs.
6. In parallel only after the master packet: recover current official Rhode Island free-doubler terms/3-spot data/throughput, and search deterministic pre-locked lottery overlays in smaller state spaces.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H184_APPEND.md`.
Latest case: `research/h184_h183_current_master_exact_rejection.md`.
