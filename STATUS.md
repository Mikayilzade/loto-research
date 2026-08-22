# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H183 — H180 symmetry reduction + persistent 246-counterexample cut bank**.

### H183 major result
The unresolved H175 target remains the 4,336-play doubled 3-spot hybrid whose only mathematical gate is: every balanced `4+4+4+4+4` draw must complete at least three of the six transversal layers (`n3>=3`).

H183 materially strengthens H180's restricted diagonal cyclic-affine master `z=a*x+a*y+c (mod 16)` in two exact WLOG ways:
1. a common translation of all five 16-symbol groups can normalize the selected `(2,3,4)` layer to `c=0`, because `1-2a` is odd/invertible mod 16;
2. swapping groups 0/1 leaves the `(0,1,2)` layers invariant and exchanges the `(0,3,4)` / `(1,3,4)` single layers, so their candidate ids can be ordered.

This reduces the representative master from **715,917,361,152** raw designs to **22,547,202,048** symmetry orientations (~31.75x reduction).

A fast adversarial separator was then coupled to the exact master. Any local-search witness is accepted only after exact `n3` recomputation; if local search stops above 2, the exact MILP separator is used. Timeouts are never validation.

Starting from H180's same 8 initial cuts, H183 generated **246 additional adaptive explicit counterexamples**:
- `n3=0`: **20**;
- `n3=1`: **45**;
- `n3=2`: **181**.

One heuristic-hard candidate reached local `n3=3`; exact MILP independently broke it at **n3=2**. Thus 246/246 adaptively selected candidates were rejected, but this is still not an impossibility proof.

The complete reusable cut bank is now persisted:
- 8 initial cuts + 246 adaptive cuts = **254 balanced necessary cuts**;
- `data/derived/h183_h180_witness_bank.zlib.b64`;
- continuation code: `src/loto_research/h183_h180_symmetry_persistent_cuts.py`.

After all 254 cuts the symmetry-reduced master is **still feasible**. Current unresolved master ids are `[[3,16,94],[1],[9],[16]]`; this is only the next separator target, not a validated construction.

Status: **RESTRICTED FAMILY HEAVILY NARROWED / NO UNIVERSAL CONSTRUCTION / NO INFEASIBILITY PROOF YET**.

Files:
- `research/h183_h180_symmetry_reduced_persistent_cut_bank.md`
- `src/loto_research/h183_h180_symmetry_persistent_cuts.py`
- `data/derived/h183_h180_witness_bank.zlib.b64`
- `research/CHECKED_PROJECTS_AND_TESTS_H183_APPEND.md`

### H182 preserved result
Current August 2026 Michigan Club Keno Tripler Time is closed as an ex-ante guaranteed subsidy: Doubler/Tripler tags are assigned to random paid tickets and no finite forced-issuance bound is published. Tagged-ticket states remain conditional overlays only.

### H175-H180 preserved result
- H175: 4,336-play hybrid; all non-balanced draw compositions are already strict-positive; balanced draws require universal `n3>=3`.
- H178/H179: broad concrete cyclic/XOR/isotopy screens repeatedly found exact `n3<=2` witnesses; timeout never counts as validation.
- H180: first adaptive exact master/separator architecture; original run broke 20 master candidates but did not close the restricted family.
- H183 now supersedes H180's restart behavior by persisting 254 cuts and adding exact WLOG symmetry reduction.

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
- H174 proves 4×20 is the cheapest strict-positive member among 411,498 tested clique partitions.
- H175 identifies the 4,336-play transversal hybrid and universal balanced `n3>=3` gate.
- H176-H177 leave current RI free-doubler terms/execution unresolved and reject ordinary paid Keno Plus as a substitute.
- H178-H180 repeatedly break candidate Latin/transversal designs and establish adaptive exact separation.
- H181-H182 validate Michigan's current free pre-draw multiplier architecture but close random tag acquisition as a strict-guarantee source.
- **H183 adds a 31.75x WLOG master reduction and persists 254 cuts; 246 new adaptive candidates are explicitly rejected, but the restricted family remains feasible.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: resume H183 directly from the persisted 254-cut bank** and attack current master ids `[[3,16,94],[1],[9],[16]]`; continue until symmetry-reduced master infeasibility or independently certified exact-separator infeasibility.
2. Add only mathematically safe symmetry/orbit cuts or stronger valid inequalities that accelerate restricted-family closure; never count a timeout as validation.
3. If the restricted diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod 16)` with independent odd `a,b` (1,024 layers/support), reusing the witness bank.
4. General H175 remains open until a construction or impossibility theorem covers arbitrary allowed Latin/transversal designs.
5. Recover exact official current Rhode Island `Kick Back with Keno` rules, current primary 3-spot prize data, and retailer/terminal throughput mechanics.
6. Search other current **deterministic** pre-printed/pre-locked free doublers in smaller lottery state spaces; random multiplier probabilities require a hard issuance bound.
7. Continue BCLC deterministic `X paid + Y free` Keno monitor, Nebraska/community fixed scheduled-special recovery, and H159 fixed-board raffle monitor.
8. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
9. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H183_APPEND.md`.
Latest case: `research/h183_h180_symmetry_reduced_persistent_cut_bank.md`.
