# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H189 — S3 coefficient-orbit canonicalization for the H175 restricted master**.

### H189 major result
The unresolved H175 4,336-play doubled 3-spot hybrid gate still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

H188 had reduced the restricted diagonal cyclic-affine family to `C(128,3)*36 = 12,289,536` representatives by fixing D=`(1,0)`, forcing B/C shifts to zero and ordering `a_B<=a_C`.

H189 proves H188 still underused an exact symmetry. The three single-support layers B=`(0,3,4)`, C=`(1,3,4)`, D=`(2,3,4)` are permuted by the full `S3` action on groups `0,1,2`, while A=`(0,1,2)` is preserved as a support. Combined with H187's common odd-unit scaling of all three B/C/D coefficients, any coefficient triple is equivalent under permutation plus common unit multiplication modulo 16.

Enumerating the 36 H188 ordered pairs `(a_B,a_C)` for normalized `(a_B,a_C,1)` gives exactly **15 coefficient orbits**:

`(1,1), (1,3), (1,5), (1,7), (1,9), (1,11), (1,13), (1,15), (3,5), (3,7), (3,9), (3,13), (3,15), (5,9), (7,9)`.

Therefore the exact canonical restricted representative count is now

`C(128,3) * 15 = 5,120,640`.

This is 2.4x smaller than H188 and about 139,808x smaller than H180's 715,917,361,152 raw restricted designs. It is a WLOG quotient, not a construction or infeasibility proof. All accumulated balanced witness cuts remain valid.

Files:
- `research/h189_h188_s3_coefficient_orbits.md`
- `data/derived/h189_s3_coefficient_orbits.json`
- `src/loto_research/h189_s3_coefficient_orbits.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H189_APPEND.md`

### Preserved H185-H188 state
- H185: 297 stored exact balanced witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit balanced counterexamples across two rejected candidates; 18,952 H186-only affine-expanded valid rows; timeout/no-incumbent was inconclusive.
- H187: exact D coefficient+shift normalization to id0 `(1,0)`.
- H188: exact B/C zero-shift normalization and B/C ordering; 12,289,536 representatives.
- H189 supersedes H188's coefficient-pair parameterization with 15 exact S3/common-scaling orbits and 5,120,640 representatives.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Lotto Texas 2023 near-full acquisition was operationally real; current Texas route legally closed and jackpot sharing blocks strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeover materially closed; residual raffle takeovers have a forced-slot theorem but sampled boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic carryover guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias branch needs reliable bulk history.
- Several Keno/Pick-style conditional overlays can reach/exceed 100% only in favorable modifier states; random state assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- Rhode Island proves lottery-issued pre-draw doubled entitlement can exist historically; current exact free-doubler terms/execution remain unresolved. Ordinary paid Keno Plus is not a locked-2x substitute.
- H173 conditional 4,560-play doubled 3-spot cover remains valid; H175's 4,336-play hybrid would improve it if universal `n3>=3` can be constructed.
- H178-H189 continue exact search of that 4,336-play gate; no universal construction or impossibility theorem yet.
- Michigan current pre-draw multiplier architecture exists but random ticket tagging prevents strict ex-ante guarantee.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: implement/run an H189 canonical master using only the 15 coefficient-orbit representatives together with the full merged H185+H186 valid affine-orbit cut system.**
2. If a feasible candidate is returned, immediately run exact `n3<=2` separation and persist each new witness plus mathematically safe orbit rows.
3. If solver-certified infeasible, the entire restricted diagonal cyclic-affine family is closed. Timeout/no-incumbent is never infeasibility and never validation.
4. If needed, exploit stabilizers of the 15 coefficient orbits to further quotient A parameters or add stronger valid aggregated inequalities; do not restart from weaker H188/H187 masters.
5. If the diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` with independent odd `a,b`, reusing all accumulated balanced witnesses.
6. General H175 remains open until a construction or impossibility theorem covers arbitrary allowed Latin/transversal designs.
7. After the master packet, continue current Rhode Island prelocked-doubler/3-spot throughput evidence and other deterministic lottery overlays.
8. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where replacing the large legacy ledger directly is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H189_APPEND.md`.
Latest case: `research/h189_h188_s3_coefficient_orbits.md`.
