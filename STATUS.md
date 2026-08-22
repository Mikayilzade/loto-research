# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H188 — exact B/C shift normalization for the H175 restricted master**.

### H188 major result
The unresolved H175 4,336-play doubled 3-spot hybrid gate still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

H187 had already proved WLOG that the sole D=`(2,3,4)` layer can be fixed to parameter id0 `(a,c)=(1,0)`, reducing the restricted diagonal cyclic-affine representative master to 2,818,400,256 designs.

H188 proves a substantially stronger exact canonicalization.

After D is fixed to `(1,0)`, translate only group0 by `t0` and group1 by `t1`. For B=`(0,3,4)`, the shift changes as

`c_B' = c_B - a_B*t0 (mod16)`.

Because every allowed `a_B` is odd and hence invertible modulo 16, choose `t0=a_B^{-1}c_B` and force `c_B'=0`. This leaves C and D unchanged and only relabels A shifts inside A's unrestricted parameter family.

Likewise choose `t1=a_C^{-1}c_C` to force `c_C'=0`, independently preserving B and D.

Swapping groups0 and1 leaves A invariant, swaps B/C and leaves D invariant, so impose coefficient order `a_B<=a_C`.

Therefore every universal restricted-family design has an equivalent representative with:
- D fixed to id0 `(1,0)`;
- B restricted to zero-shift ids `{0,16,32,48,64,80,96,112}`;
- C restricted to the same zero-shift ids;
- ordered odd coefficients `a_B<=a_C`.

Representative count becomes

`C(128,3) * 36 = 12,289,536`,

an additional exact **229.33x reduction vs H187** and about **58,254x reduction vs H180's 715,917,361,152 raw restricted designs**.

This is a WLOG theorem, not an infeasibility proof and not a universal construction.

Files:
- `research/h188_h180_bc_shift_normalization.md`
- `data/derived/h188_bc_shift_normalization.json`
- `src/loto_research/h188_bc_shift_normalized_master.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H188_APPEND.md`

### Preserved H185-H187 state
- H185: 297 stored exact balanced witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit balanced counterexamples across two rejected candidates; 18,952 H186-only affine-expanded valid rows; later timeout/no-incumbent was inconclusive.
- H187: D coefficient+shift normalization to id0 and a normalized prototype with 12/12 candidates explicitly rejected.
- H188 supersedes the weaker H187 master parameterization; all H185/H186 balanced witness cuts remain valid and reusable.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Lotto Texas 2023 near-full acquisition was operationally real; current Texas route legally closed and jackpot sharing blocks strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeover materially closed; residual raffle takeovers have a forced-slot theorem but sampled boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic carryover guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias branch needs reliable bulk history.
- Several Keno/Pick-style conditional overlays can reach/exceed 100% only in favorable modifier states; random state assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- Rhode Island proves lottery-issued pre-draw doubled entitlement can exist historically; current exact free-doubler terms/execution remain unresolved. Ordinary paid Keno Plus is not a locked-2x substitute.
- H173 conditional 4,560-play doubled 3-spot cover remains valid; H175's 4,336-play hybrid would improve it if universal `n3>=3` can be constructed.
- H178-H188 continue exact search of that 4,336-play gate; no universal construction or impossibility theorem yet.
- Michigan current pre-draw multiplier architecture exists but random ticket tagging prevents strict ex-ante guarantee.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: run the full merged H185+H186 valid affine-orbit cut system under H188's canonical master** using `src/loto_research/h188_bc_shift_normalized_master.py`.
2. If a feasible candidate is returned, immediately run exact `n3<=2` separation and persist the witness plus safe orbit rows.
3. If solver-certified infeasible, the entire restricted diagonal cyclic-affine family is closed. Timeout/no-incumbent is never infeasibility and never validation.
4. If needed, strengthen the exact formulation further using valid symmetry or aggregated inequalities; do not restart from weaker H187/H186 masters.
5. If the diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` with independent odd `a,b`, reusing all accumulated balanced witnesses.
6. General H175 remains open until a construction or impossibility theorem covers arbitrary allowed Latin/transversal designs.
7. After the master packet, continue current Rhode Island prelocked-doubler/3-spot throughput evidence and other deterministic lottery overlays.
8. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where replacing the large legacy ledger directly is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H188_APPEND.md`.
Latest case: `research/h188_h180_bc_shift_normalization.md`.
