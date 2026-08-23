# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H228 — corrected ordered-sector symmetry + exact A-coefficient multiset quotient**.

### H228 major result
H226's general coefficient-envelope result and H224 restricted exact result were still absent at H228 start, so no closure was inferred.

H228 audited H227 and found a rigor issue in the stated 36-sector action: canonicalizing `(beta,gamma)` to `beta<=gamma` after each `S3 x S2` image does not define a genuine 12-element action on the unordered sector representatives, because the beta/gamma swap subgroup is not normal in the full S3 coordinate action. Therefore H227's unordered-sector orbit sizes/stabilizer sizes must not be reused.

The useful H227 reduction survives after correction. Acting first on all **64 ordered** normalized sectors gives exactly **11 genuine group orbits**, with the same representative labels:
`(1,1),(1,3),(1,5),(1,7),(1,9),(1,15),(3,5),(3,9),(3,13),(5,9),(7,9)`.

Correct ordered-sector orbit sizes:
`1,6,6,3,3,3,12,6,12,6,6`.
Correct stabilizer sizes:
`12,2,2,4,4,4,1,2,1,2,2`.

H228 then derives the exact induced stabilizer action on general A coefficient pairs. Writing an A layer as `a*x0+b*x1-x2+c=0`, permutations of groups 0/1/2 permute `(a,b,-1)` and renormalize the third coefficient back to `-1`; this bijects the 64 odd `(a,b)` pairs. The 3/4 flip acts trivially on A coefficient pairs.

Exact enumeration of the 45,760 three-multisets of A coefficient pairs under each true sector stabilizer gives **306,450 total quotient coefficient states across the 11 representative sectors**.

Reduction:
- H226 original 36-sector coefficient workload: `1,647,360` cases.
- H227 representative-sector raw workload: `503,360` cases.
- H228 exact true-stabilizer quotient: **306,450** cases.
- Reduction vs H227: **1.64255x**.
- Reduction vs H226 raw: **5.37562x**.

Files:
- `src/loto_research/h228_ordered_sector_stabilizer_coefficient_orbits.py`
- `data/derived/h228_ordered_sector_coefficient_orbits.json`
- `research/h228_ordered_sector_stabilizer_coefficient_orbits.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H228_APPEND.md`

This is an exact WLOG search reduction, not universal `n3>=3` validation or impossibility.

### Preserved H226/H225 general-family state
- H226 target `data/derived/h226_general_coefficient_envelope.json` was absent at H228 start; missing output remains inconclusive.
- H226 exact coefficient-envelope theorem remains valid: if even rowwise best legal distinct A shifts cannot reach total incidence 3 on a stored balanced witness, the whole coefficient multiset is impossible.
- H225 general cyclic-affine normalization/Burnside result remains a valid earlier within-sector quotient, but H228 is now authoritative for cross-sector existence-search symmetry.
- H225 canonical-design count: 36,243,104 under its earlier residual quotient.

### Preserved restricted-family state
- H224/H223/H222/H219 exact restricted outputs have not produced an authoritative closure result at H228 start.
- H221 proves any schema-valid restricted exact screen with `survivor_count=0` over all 143,712 H212-normalized classes closes that restricted family without a second MILP.

### Preserved promotion/execution state
- Current RI `Kick Back with Keno Promotion` is officially visible, but exact mechanics remain unrecovered; do not repeat H209's exhausted searches without new evidence.
- Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist, but doubled tickets were explicitly non-cancellable.
- Current RI online/iLottery and ordinary retailer/SSVM remain closed as sole strict-guarantee execution channels under recovered public rules.

## NEXT ACTION
1. **Check H226 and late H224/H223/H222/H219 result artifacts first.** Missing output proves nothing.
2. Build an H228-corrected representative-only coefficient-envelope screen over the **306,450** exact quotient coefficient states using the true ordered-sector stabilizers.
3. If all quotient coefficient states are rejected by H226's exact witness envelope, close the full H225 general cyclic-affine family by H226+H228 symmetry.
4. Otherwise enumerate globally consistent legal shifts only for surviving coefficient states, quotient by their residual stabilizers, then run exact `n3<=2` separation on every actual design survivor; timeout never validates a design.
5. If any restricted exact result returns zero survivors, separately close H212 under H221.
6. Reopen current `Kick Back with Keno` only on materially new primary evidence.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H228_APPEND.md`.
Latest case: `research/h228_ordered_sector_stabilizer_coefficient_orbits.md`.
