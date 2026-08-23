# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H226 — exact coefficient-envelope pre-screen for the H225 general cyclic-affine family**.

### H226 major result
H224's restricted-family exact output remained absent at H226 start, so no restricted-family closure was inferred. H226 instead advances the H225 general cyclic-affine branch with a new exact necessary-condition layer.

After H225 normalization, one B/C sector fixes `B=(1,beta,0)`, `C=(1,gamma,0)`, `D=(1,1,0)`. The three A layers draw from 64 odd coefficient pairs `(a,b)`, each with 16 shifts. H226 fixes only the multiset of the three A coefficient pairs and, for every exact balanced witness, computes the best possible incidence over legal distinct shifts. For repeated coefficient blocks it uses the top 2 or top 3 distinct shifts, so the envelope respects the distinct-layer constraint.

If even this optimistic rowwise envelope plus fixed B/C/D incidence is below 3 on any witness, every actual shift realization of that coefficient multiset is impossible. This is an exact theorem, not a heuristic.

The coefficient-pattern space is only `C(66,3)=45,760` patterns per normalized B/C sector, providing a much cheaper pre-screen before exact shift-level orbit enumeration of H225's 36,243,104 canonical designs.

Crucially, H226 recomputes/deduplicates witness signatures under the full general A/B/C incidence parameterization; it does not assume the old restricted-diagonal 4,878-row dedupe remains complete after enlarging the family.

Target result: `data/derived/h226_general_coefficient_envelope.json`. At this checkpoint the computation is launched/pending; missing output is inconclusive.

Files:
- `src/loto_research/h226_general_coefficient_envelope_prescreen.py`
- `.github/workflows/h226-general-coefficient-envelope.yml`
- `research/h226_general_coefficient_envelope_prescreen.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H226_APPEND.md`

### Preserved H225 general-family result
- General cyclic-affine layers `z=a*x+b*y+c (mod16)` with odd `a,b`.
- Exact WLOG normalization: D=(1,1,0), B=(1,beta,0), C=(1,gamma,0), beta<=gamma.
- Exact residual Burnside quotient: **36,243,104 canonical classes** from 6,423,588,864 normalized raw classes.
- No universal construction or general-family impossibility proof yet.

### Preserved H224/H221 restricted-family state
- H224 target `data/derived/h224_bulk_vectorized_survivors.json` remained absent at H226 start; missing output is inconclusive.
- H221 proves any schema-valid exact restricted screen with `survivor_count=0` over all 143,712 H212-normalized classes closes that restricted family without a second MILP.

### Preserved promotion/execution state
- Current RI `Kick Back with Keno Promotion` is officially visible, but exact mechanics remain unrecovered; do not repeat H209's exhausted searches without new evidence.
- Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist, but doubled tickets were explicitly non-cancellable.
- Current RI online/iLottery and ordinary retailer/SSVM remain closed as sole strict-guarantee execution channels under recovered public rules.

## NEXT ACTION
1. **Check `data/derived/h226_general_coefficient_envelope.json` first; also check H224/H223/H222/H219 restricted outputs.**
2. If H226 exists, use its surviving coefficient-pattern sectors to build an exact globally consistent shift-level screen, quotienting by the H225 residual stabilizer rather than enumerating all raw shifts.
3. If H226 rejects all coefficient patterns in all 36 sectors, close the entire H225 general cyclic-affine family immediately by the envelope theorem.
4. For every exact shift-level survivor, run exact `n3<=2` separation; timeout never validates a design.
5. If any restricted exact result returns zero survivors, separately close the H212 restricted diagonal family under H221.
6. Reopen current `Kick Back with Keno` only on materially new primary evidence.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H226_APPEND.md`.
Latest case: `research/h226_general_coefficient_envelope_prescreen.md`.
