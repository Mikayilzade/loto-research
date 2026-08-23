# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H230 — exact globally consistent shift CSP for the H225 general cyclic-affine family**.

### H230 major result
H229's result artifact was still absent at H230 start, so no general-family closure was inferred.

H230 materially strengthens H229/H226. H226's coefficient envelope is rowwise optimistic and can implicitly use different A shifts on different witness rows. H230 removes that relaxation: for every H228 quotient coefficient-state representative that passes the envelope, it enumerates the complete legal A-shift state space and requires one **globally consistent** shift tuple to satisfy every stored exact balanced-witness constraint.

Exact legal shift spaces per coefficient pattern:
- three distinct coefficient blocks: `4096`;
- one repeated coefficient block: `1920` canonical legal tuples;
- all three blocks equal: `560` canonical legal tuples.
Canonical ordering among identical coefficient blocks removes only permutations of identical A layers.

H230 still searches exactly the **306,450** H228 quotient coefficient states across 11 true ordered-sector orbits. If `exact_shift_surviving_coefficient_states=0`, every actual design in the full H225 general cyclic-affine family has a balanced `n3<=2` counterexample, directly for quotient representatives and by H228 automorphism transport for orbit mates. That would close the full general cyclic-affine family finitely.

Target result: `data/derived/h230_exact_shift_csp.json`.
At this checkpoint the result is absent, so no closure is claimed. Missing output/timeout remains inconclusive.

Files:
- `src/loto_research/h230_exact_shift_csp_screen.py`
- `.github/workflows/h230-exact-shift-csp.yml`
- `research/h230_exact_global_shift_csp.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H230_APPEND.md`

### Preserved H229/H228/H226/H225 general-family state
- H225 general cyclic-affine normalization/Burnside: 36,243,104 earlier within-sector canonical designs.
- H226 exact coefficient-envelope theorem remains valid.
- H228 corrected ordered-sector symmetry + stabilizer quotient: 306,450 coefficient states across 11 sector orbits.
- H229 exact quotient envelope screen launched; result absent through H230 start.
- H230 exact globally consistent shift CSP launched; result pending.
- No universal construction or general-family impossibility proof yet.

### Preserved restricted-family state
- H224/H223/H222/H219 exact restricted outputs have not produced an authoritative closure result at H230 start.
- H221 proves any schema-valid restricted exact screen with `survivor_count=0` over all 143,712 H212-normalized classes closes that restricted family without a second MILP.

### Preserved promotion/execution state
- Current RI `Kick Back with Keno Promotion` is officially visible, but exact mechanics remain unrecovered; do not repeat H209's exhausted searches without new evidence.
- Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist, but doubled tickets were explicitly non-cancellable.
- Current RI online/iLottery and ordinary retailer/SSVM remain closed as sole strict-guarantee execution channels under recovered public rules.

## NEXT ACTION
1. **Check `data/derived/h230_exact_shift_csp.json` first; also accept late valid H229/H226/H224/H223/H222/H219 outputs.** Missing output proves nothing.
2. If H230 has `exact_shift_surviving_coefficient_states=0`, validate schema/counts and close the entire H225 general cyclic-affine family immediately.
3. If H230 has survivors, run exact unrestricted `n3<=2` separation only on those actual shift-level designs; add every new balanced counterexample to the witness bank and iterate the exact screen.
4. If H229 independently has zero envelope survivors, it already closes the H225 general cyclic-affine family by H226+H228 and H230 is unnecessary for closure.
5. If any restricted exact result returns zero survivors, separately close H212 under H221.
6. Reopen current `Kick Back with Keno` only on materially new primary evidence.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H230_APPEND.md`.
Latest case: `research/h230_exact_global_shift_csp.md`.
