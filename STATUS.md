# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H187 — stronger support-(2,3,4) coefficient normalization**.

### H187 major result
H187 continues the unresolved H175 4,336-play doubled 3-spot hybrid gate. The universal mathematical condition remains `n3>=3` on every balanced `4+4+4+4+4` draw.

H186's follow-up master over 18,952 H186-only valid rows reached a time limit with no incumbent, which remains inconclusive. H187 targets that solver bottleneck with a new exact WLOG symmetry.

Restricted layers are `z=a*x+a*y+c (mod16)` with odd `a`. H183 had normalized the single `(2,3,4)` layer to `c=0` but left all 8 odd values of `a`.

H187 proves that this coefficient can also be normalized:
- scale groups 0,1,2,3 by a common odd unit `u`;
- scale group 4 by an independently chosen odd unit `w`;
- the `(0,1,2)` coefficients remain unchanged;
- each support ending in group 4 gets coefficient `a'=(w/u)*a`;
- choose `w/u=a_D^{-1}` for the selected `(2,3,4)` layer, then choose the group-4 translation to set its shift to zero.

Therefore every universal restricted-family design has an equivalent representative whose sole `(2,3,4)` layer is exactly candidate id **0 = `(a,c)=(1,0)`**. Balanced four-subsets are mapped bijectively, so this does not remove any possible universal `n3>=3` design.

The H183 group-0/group-1 swap symmetry remains available, so its B/C ordering constraint can be retained.

Representative master count therefore falls from

`22,547,202,048`

to

`2,818,400,256`,

an additional exact **8x WLOG reduction** and about 254x fewer representative orientations than H180's original 715.9B raw restricted designs.

A concrete normalization sanity check maps the already-rejected H185 candidate `[[18,54,111],[12],[88],[16]]` to ordered normalized ids `[[18,54,111],[72],[84],[0]]`; the transformed balanced witness still has exact `n3=2`.

A fresh deterministic normalized-master prototype also completed **12 adaptive cycles**:
- 12/12 master candidates explicitly rejected;
- exact score histogram: `n3=2` x12;
- 12 initial valid rows grew to **1,172** unique valid rows after safe common-affine witness-orbit expansion.

This prototype is evidence for the stronger formulation, not an infeasibility proof and not a substitute for the H185/H186 persistent witness banks.

Files:
- `research/h187_h180_support4_coefficient_normalization.md`
- `data/derived/h187_support4_normalization_results.json`
- `src/loto_research/h187_support4_normalized_merged_master.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H187_APPEND.md`

### H186 preserved result
H186 produced **189 explicit balanced counterexamples** across two attacked restricted candidates. Their common-affine expansion/deduplication produced **18,952 unique H186-only valid rows**. The subsequent master solve hit its configured time limit with no incumbent; this is inconclusive, not infeasibility.

H186 files:
- `research/h186_h185_mass_counterexample_packet.md`
- `data/derived/h186_h185_counterexample_packet.zlib.b64`
- `src/loto_research/h186_h185_mass_counterexample_packet.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H186_APPEND.md`

### H185 preserved checkpoint
H185 has 297 stored exact witnesses and 4,878 active unique valid rows after affine expansion. H186 adds 189 new witnesses; H187 provides the stronger normalized master into which the merged bank should now be loaded.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not current guarantee.
- H108 Lotto Texas 2023: near-full acquisition operationally real; current Texas route legally closed and jackpot sharing blocks strict guarantee.
- H109-H112 fixed raffle/scratch/sealed-pack standard takeover materially closed.
- H113-H116 Azerbaijan `4+4` ordinary/realistic carryover guarantee routes materially closed; reopen only on rare exceptional states/rule change/external subsidy.
- H114 TezLoto full coverage negative; bias route requires reliable bulk history and out-of-sample lift.
- H122/H128 fixed-board undersubscription is a strong +EV class but external winning ownership blocks strict guarantee.
- H129/H159 residual raffle takeovers have exact worst-case forced-slot theorem; sampled boards fail strict floor.
- H130-H141 replenishing games / coupons / wallet / cart subsidy architectures do not currently produce a strict executable guarantee.
- H142-H171 several Keno/Pick-style conditional overlays can reach or exceed 100% in favorable modifier states, but random state assignment, execution atomicity, liability limits or insufficient subsidy block terminal guarantee.
- H172 proves a lottery-issued pre-draw doubled entitlement can exist; current exact Rhode Island terms/execution remain unresolved.
- H173 gives conditional 4,560-play / 109.6491% doubled 3-spot worst-case cover.
- H174 proves 4x20 is the cheapest strict-positive member among 411,498 tested clique partitions.
- H175 identifies the 4,336-play transversal hybrid and universal balanced `n3>=3` gate.
- H176-H177 reject ordinary paid RI Keno Plus as a locked-2x substitute and leave current free-doubler/execution terms unresolved.
- H178-H187 continue exact search of the 4,336-play gate; no universal design or impossibility theorem yet.
- H181-H182 validate Michigan's current free pre-draw multiplier architecture but close random tag acquisition as a strict-guarantee source.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: merge H185's 297 stored witnesses with H186's 189 new explicit witnesses, deduplicate across packets, and regenerate the full valid affine-orbit union.**
2. Solve that merged cut system under H187's stronger exact normalization `(2,3,4)=id0`, retaining the H183 B/C ordering symmetry. Use `src/loto_research/h187_support4_normalized_merged_master.py`.
3. If a feasible candidate is returned, immediately run exact `n3<=2` separation and persist any witness. If solver-certified infeasible, the entire restricted diagonal cyclic-affine family is closed.
4. Timeout/no-incumbent is never validation and never an infeasibility proof.
5. If the diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` with independent odd `a,b`, reusing all accumulated balanced witness cuts.
6. General H175 remains open until a construction or impossibility theorem covers arbitrary allowed Latin/transversal designs.
7. After this master packet, continue recovery of current official Rhode Island free-doubler terms/3-spot data/throughput and deterministic pre-locked lottery overlays.
8. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H187_APPEND.md`.
Latest case: `research/h187_h180_support4_coefficient_normalization.md`.
