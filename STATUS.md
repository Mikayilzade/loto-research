# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H191 — exact A-set stabilizer classification after H190**.

### H191 major result
The unresolved H175 4,336-play doubled 3-spot hybrid gate still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

H191 exactly classified when H190's withdrawn full-S3 quotient can nevertheless be used on an actual three-layer A-set. For the restricted diagonal A family

`x2 = a*x0 + a*x1 + c (mod16)`, odd `a`,

all 128 layers were tested under all 6 coordinate permutations by exact 256-triple set comparison.

Preservation counts:
- identity `(0,1,2)`: 128/128;
- input swap `(1,0,2)`: 128/128;
- each other permutation: exactly 16/128, precisely the slope-15 layers `(a,c)=(15,c)`.

For `a=15`, the relation becomes `x0+x1+x2=c`, so every S3 permutation fixes each layer individually. Therefore an actual three-layer A-set has stabilizer larger than the universal input-swap C2 **iff all three layers have slope 15**.

Exact counts:
- all A-sets: `C(128,3)=341,376`;
- exceptional full-S3 A-sets: `C(16,3)=560`;
- generic C2 A-sets: `340,816`.

Applying H189's 15 B/C coefficient orbits only to those 560 exceptional A-sets gives the safe stabilizer-aware representative count

`340,816*36 + 560*15 = 12,277,776`.

H188's count was `12,289,536`, so the exact saving is only `11,760 = 0.09578%`. The stabilizer-quotient acceleration direction is therefore materially exhausted; meaningful next progress must come from stronger valid cuts, better separator/master formulations, direct exact pruning, or a broader structural theorem.

Files:
- `research/h191_a_set_stabilizer_classification.md`
- `data/derived/h191_a_set_stabilizer_summary.json`
- `src/loto_research/h191_a_set_stabilizer_classification.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H191_APPEND.md`

### Preserved H185-H190 state
- H185: 297 stored exact balanced witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit balanced counterexamples across two rejected candidates; 18,952 H186-only affine-expanded valid rows; timeout/no-incumbent was inconclusive.
- H187: exact D coefficient+shift normalization to id0 `(1,0)`.
- H188: exact B/C zero-shift normalization and B/C ordering; **12,289,536** globally justified representatives.
- H189: proposed full-S3 coefficient quotient to 15 classes / 5,120,640 representatives; rejected globally by H190.
- H190: proved full S3 is globally unsafe; restored H188 as authoritative global quotient.
- H191: proved extra S3 applies only to 560 all-slope-15 A-sets, reducing count only to **12,277,776**.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Lotto Texas 2023 near-full acquisition was operationally real; current Texas route legally closed and jackpot sharing blocks strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeover materially closed; residual raffle takeovers have a forced-slot theorem but sampled boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic carryover guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias branch needs reliable bulk history.
- Several Keno/Pick-style conditional overlays can reach/exceed 100% only in favorable modifier states; random state assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- Rhode Island proves lottery-issued pre-draw doubled entitlement can exist historically; current exact free-doubler terms/execution remain unresolved. Ordinary paid Keno Plus is not a locked-2x substitute.
- H173 conditional 4,560-play doubled 3-spot cover remains valid; H175's 4,336-play hybrid would improve it if universal `n3>=3` can be constructed.
- H178-H191 continue exact search/audit of that 4,336-play gate; no universal construction or impossibility theorem yet.
- Michigan current pre-draw multiplier architecture exists but random ticket tagging prevents strict ex-ante guarantee.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: resume from H191/H188's safe 12,277,776 representatives plus the full valid H185+H186 witness/cut bank. Stop spending effort on further coordinate-symmetry quotients unless a new theorem gives a materially larger group.**
2. Build stronger exact pruning for the restricted diagonal family: precompute per-A compatibility with existing balanced cuts and eliminate B/C coefficient pairs before full master solve.
3. Use exact separator/adversary search against every surviving candidate; add explicit `n3<=2` witnesses and safe affine orbits. Timeout/no-incumbent is never infeasibility and never validation.
4. Solver-certified infeasibility closes the restricted diagonal family.
5. If the diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` with independent odd `a,b`, reusing all accumulated balanced witnesses.
6. General H175 remains open until a construction or impossibility theorem covers arbitrary allowed Latin/transversal designs.
7. After the master packet, continue current Rhode Island prelocked-doubler/3-spot throughput evidence and other deterministic lottery overlays.
8. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where replacing the large legacy ledger directly is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H191_APPEND.md`.
Latest case: `research/h191_a_set_stabilizer_classification.md`.
