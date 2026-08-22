# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H190 — correction of H189 full-S3 canonicalization**.

### H190 major result
The unresolved H175 4,336-play doubled 3-spot hybrid gate still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

H190 audited H189's claimed full `S3` symmetry on groups `0,1,2`. H189 correctly observed that these permutations rearrange the B/C/D supports, but it did not check that they preserve the restricted diagonal layer family on A=`(0,1,2)`.

For A layers

`x2 = a*x0 + a*x1 + c (mod16)`, odd `a`,

an input/output swap transforms the relation into a general affine layer whose two input coefficients are `a^{-1}` and `-1`. These are equal only for `a=15`.

H190 exhaustively enumerated all **128 A layers × 6 coordinate permutations** and compared exact 256-triple images against the complete 128-layer restricted family:
- identity `(0,1,2)`: 128/128 preserved;
- input swap `(1,0,2)`: 128/128 preserved;
- each of the other four permutations: only 16/128 preserved, exactly the `a=15` layers.

Therefore the restricted diagonal family is globally invariant only under the order-2 subgroup that keeps group 2 as A output. Full S3 is **not** a valid global WLOG symmetry.

Consequences:
- H189's reduction from 36 normalized B/C coefficient pairs to 15 coefficient orbits is withdrawn as globally unsafe;
- H189's `5,120,640` exhaustive representative count is withdrawn;
- H188 is restored as the last globally justified canonical checkpoint: `C(128,3)*36 = 12,289,536` representatives;
- H183-H186 direct balanced witness cuts remain valid because they do not depend on H189's quotient.

Files:
- `research/h190_h189_s3_symmetry_correction.md`
- `data/derived/h190_a_support_s3_symmetry_audit.json`
- `src/loto_research/h190_a_support_s3_symmetry_audit.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H190_APPEND.md`

### Preserved H185-H189 state
- H185: 297 stored exact balanced witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit balanced counterexamples across two rejected candidates; 18,952 H186-only affine-expanded valid rows; timeout/no-incumbent was inconclusive.
- H187: exact D coefficient+shift normalization to id0 `(1,0)`.
- H188: exact B/C zero-shift normalization and B/C ordering; **12,289,536** globally justified representatives.
- H189: proposed full-S3 coefficient quotient to 15 classes / 5,120,640 representatives; **rejected by H190 as unsafe globally**. It may remain usable only for explicitly proved A-stabilized subfamilies.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Lotto Texas 2023 near-full acquisition was operationally real; current Texas route legally closed and jackpot sharing blocks strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeover materially closed; residual raffle takeovers have a forced-slot theorem but sampled boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic carryover guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias branch needs reliable bulk history.
- Several Keno/Pick-style conditional overlays can reach/exceed 100% only in favorable modifier states; random state assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- Rhode Island proves lottery-issued pre-draw doubled entitlement can exist historically; current exact free-doubler terms/execution remain unresolved. Ordinary paid Keno Plus is not a locked-2x substitute.
- H173 conditional 4,560-play doubled 3-spot cover remains valid; H175's 4,336-play hybrid would improve it if universal `n3>=3` can be constructed.
- H178-H190 continue exact search/audit of that 4,336-play gate; no universal construction or impossibility theorem yet.
- Michigan current pre-draw multiplier architecture exists but random ticket tagging prevents strict ex-ante guarantee.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: resume from H188's 12,289,536 globally justified canonical designs and the full H185+H186 valid witness/cut bank. Do not use H189's 15-class quotient globally.**
2. Compute the exact permutation stabilizer of each actual three-layer A set; use extra B/C/D symmetry only when that A set is mapped back into the restricted diagonal family.
3. Build/run a stabilizer-aware H188 master or enumerate per-A stabilizer classes, then exact-separate every feasible candidate with `n3<=2` adversaries.
4. Solver-certified infeasibility closes the restricted diagonal family; timeout/no-incumbent is never infeasibility and never validation.
5. If the diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` with independent odd `a,b`, reusing all accumulated balanced witnesses.
6. General H175 remains open until a construction or impossibility theorem covers arbitrary allowed Latin/transversal designs.
7. After the master packet, continue current Rhode Island prelocked-doubler/3-spot throughput evidence and other deterministic lottery overlays.
8. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where replacing the large legacy ledger directly is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H190_APPEND.md`.
Latest case: `research/h190_h189_s3_symmetry_correction.md`.
