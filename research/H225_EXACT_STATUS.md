# H225 EXACT FAMILY STATUS

Updated: 2026-08-24
Namespace: `H225-X*` (separate from the global numbered lottery H-stream)
Terminal state: **OPEN / NOT CLOSED**

## Authoritative baseline
H235 exact augmented rescreen over all 306,450 quotient coefficient states:
- exact shift-surviving coefficient states: **303,802**
- exact surviving legal shift tuples: **90,425,060**
- H225 family closed: **false**

## H225-X1 — COMPLETE
Legacy exact output label/file: `H240`, retained only for reproducibility.
Authoritative alias: `data/derived/h225_x1_exact_separator_summary.json`.

Result:
- selected actual H235 survivor designs: **44**
- exact unrestricted balanced n3<=2 counterexamples: **44/44**
- inconclusive jobs: **0**
- unique counterexamples: **44**
- duplicates against H234: **0**
- genuinely new witnesses: **44**
- all sampled designs broken: **true**

The legacy H237 exact attempt is non-authoritative: all 44 separator artifacts existed, but its merge failed because SciPy was not installed in the merge job. H225-X1 reran the task with a corrected merge and completed successfully.

## H225-X2 — RUNNING
Legacy implementation/output filenames use `h241_h240_incremental_exact_rescreen*`; interpret them as H225-X2, not as the global numbered H241 packet.

Input:
- H235 witness universe
- all 44 H234 cuts
- all 44 genuinely new H225-X1 cuts, each affine-expanded through 128 symmetries

Task:
- unchanged H228 quotient universe
- all 44 chunks
- all 306,450 quotient coefficient states
- exact legal-shift CSP

Target legacy merged file:
`data/derived/h241_h240_incremental_exact_rescreen.json`

Interpretation:
- zero exact survivors = exact finite closure of H225 general cyclic-affine family
- positive survivors = continue separator/cut loop
- missing output = pending/inconclusive only

## H225-X3 — ARMED
Workflow is prepared and triggers only when the X2 merged file appears.
It selects one actual survivor from every still-positive X2 chunk; zero-survivor chunks are explicit skips. Returned witnesses are deduplicated against both H234 and H225-X1.

Files:
- `src/loto_research/h225_x3_survivor_separation.py`
- `.github/workflows/h225-x3-survivor-separation.yml`

Expected outputs:
- `data/derived/h225_x3_survivor_separation.json`
- `data/derived/h225_x3_new_witnesses.json`

## NEXT ACTION
1. Check H225-X2 merged output.
2. If zero survivors, record exact closure of H225 and stop this family lane.
3. If positive, let armed H225-X3 finish and inspect active chunks / new witnesses.
4. Continue future family iterations only under `H225-X4`, `H225-X5`, ...; never consume global H-numbers again.
