# H224 — bulk-vectorized exact H175 restricted-family screen

Date: 2026-08-23
Status: INCONCLUSIVE / exact computation launched

## Scope
Lottery-only continuation of H175. H223 output was still absent at packet start.

## Bottleneck identified
H219/H222/H223 all call the same legacy `merged_active_rows()` path. That function evaluates active witness rows one witness at a time, repeatedly entering NumPy for each support and each affine image. The exact cut bank contains only 4,878 unique rows, but it is rebuilt from tens of thousands of affine witness instances using many small array operations. This setup cost is plausibly dominating the full screen.

## H224 method
H224 keeps the exact same witness set, H212 quotient and survivor predicate, but changes row construction:

1. Load the 297 H185 stored witnesses and 189 H186 witnesses.
2. Preserve the first 254 H183/H185 base witnesses exactly.
3. Apply all 128 proved-safe common affine maps to every later H185/H186 seed.
4. Materialize the resulting witness instances once as a numeric array.
5. In batches of 256 witnesses, compute all 128 layer incidences for each of the four supports simultaneously.
6. Concatenate to the exact 512-column row representation and deduplicate rows exactly with `np.unique(axis=0)`.
7. Assert that the recovered cut bank has exactly 4,878 rows.
8. Screen all `36 x 3,992 = 143,712` H212-normalized candidates with the same exact `n3>=3` predicate.

No sampling, heuristic pruning or relaxed constraint is used. The implementation records phase timings in the output so future runs can identify the real remaining cost instead of guessing.

## Proof interpretation
A schema-valid `survivor_count=0` closes the H212-covered restricted diagonal family under H221. Positive survivors remain only finite-cut survivors and require exact `n3<=2` separation. Missing output or timeout proves nothing.

## Execution hardening
The workflow rebases before pushing the result so branch advancement during a long run does not silently discard a completed exact computation.

Files:
- `src/loto_research/h224_bulk_vectorized_full_screen.py`
- `.github/workflows/h224-bulk-vectorized-screen.yml`
- target `data/derived/h224_bulk_vectorized_survivors.json`
