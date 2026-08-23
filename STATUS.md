# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H227 — exact cross-sector support-hypergraph symmetry for H225 general cyclic-affine family**.

### H227 major result
H226's coefficient-envelope output was still absent at H227 start, so no general-family closure was inferred. H227 instead proves and exploits a new exact symmetry of the complete H175 support structure.

The four affine support types A={0,1,2}, B={0,3,4}, C={1,3,4}, D={2,3,4} have support-hypergraph automorphism group `S3 x S2` of order 12: arbitrary permutation of groups {0,1,2} and independent swap of groups 3/4. General cyclic-affine layers remain inside the family under these reorientations because all coefficients are odd units modulo 16.

Under H225 normalization, the sole B/C/D layers are encoded projectively by `q=(beta,gamma,1)`. S3 permutes q coordinates and re-normalization divides by the new third entry; swapping groups 3/4 induces inversion. The resulting exact 12-element action permutes the 36 normalized beta<=gamma sectors into exactly **11 WLOG sector orbits**.

Orbit sizes: `1,4,4,2,2,2,6,3,6,3,3`.
Representatives: `(1,1),(1,3),(1,5),(1,7),(1,9),(1,15),(3,5),(3,9),(3,13),(5,9),(7,9)`.

Therefore an exhaustive H226-style coefficient-pattern search needs only 11 complete sector representatives rather than 36. Top-level sector/coefficient cases reduce exactly from `36*45,760 = 1,647,360` to `11*45,760 = 503,360`, factor **3.272727x**, before envelope rejection or shift-level quotienting.

Files:
- `src/loto_research/h227_general_sector_hypergraph_symmetry.py`
- `data/derived/h227_general_sector_orbits.json`
- `research/h227_general_sector_hypergraph_symmetry.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H227_APPEND.md`

This is a WLOG search reduction, not a universal construction/impossibility proof. Do not divide H225's 36,243,104 canonical-design count naively by 36/11 because sector stabilizers vary.

### Preserved H226/H225 general-family state
- H226 target `data/derived/h226_general_coefficient_envelope.json` was absent at H227 start; missing output remains inconclusive.
- H226 exact coefficient-envelope theorem remains valid: 45,760 A coefficient multisets per sector can be rejected when even rowwise best legal shifts fail a stored balanced witness.
- H225 general cyclic-affine normalization/Burnside quotient remains valid: 36,243,104 canonical classes under the earlier residual group.
- H227 adds a larger cross-sector WLOG symmetry and reduces the existence/impossibility search to 11 representative sectors.

### Preserved restricted-family state
- H224/H223/H222/H219 exact restricted output files have not produced an authoritative closure result in the preserved checkpoint.
- H221 proves any schema-valid exact restricted screen with `survivor_count=0` over all 143,712 H212-normalized classes closes that restricted diagonal family without a second MILP.

### Preserved promotion/execution state
- Current RI `Kick Back with Keno Promotion` is officially visible, but exact mechanics remain unrecovered; do not repeat H209's exhausted searches without new evidence.
- Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist, but doubled tickets were explicitly non-cancellable.
- Current RI online/iLottery and ordinary retailer/SSVM remain closed as sole strict-guarantee execution channels under recovered public rules.

## NEXT ACTION
1. **Check `data/derived/h226_general_coefficient_envelope.json` and late H224/H223/H222/H219 results first.** Use any valid result immediately; missing output proves nothing.
2. Exploit H227's **11 representative-sector stabilizers** (sizes `12,3,3,6,6,6,2,4,2,4,4`) to quotient A coefficient multisets and then shift realizations before exact general-family screening.
3. Build the exact globally consistent shift-level screen on those quotient states, reusing H226's envelope theorem as a necessary pre-filter.
4. For every surviving actual design, run exact `n3<=2` separation; timeout never validates a design.
5. If H226 rejects all patterns in all needed representative sectors, close the entire H225 general cyclic-affine family by H226+H227 symmetry.
6. If any restricted exact result returns zero survivors, separately close H212 under H221.
7. Reopen current `Kick Back with Keno` only on materially new primary evidence.
8. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H227_APPEND.md`.
Latest case: `research/h227_general_sector_hypergraph_symmetry.md`.
