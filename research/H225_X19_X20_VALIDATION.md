# H225-X19 / X20 independent validation

Validated on 2026-08-25 against authoritative GitHub Actions run `32813117144` (`success`).

## X19 exact separation

Artifact: `h225-x19-merged` id `9550508802`, digest `sha256:c4c40fcc52b9ec1b10a0540e0ed36cf0cf737a53b502d3c3122f5487d3bd28df`.

Independent checks:
- exactly 44 ordered jobs (`0..43`) with the canonical 11 sector x 4 chunk mapping;
- X18 source totals are exactly 3,300 coefficient survivors and 71,392 legal shift tuples;
- 12 active survivor chunks and 32 zero-survivor chunks;
- all 12 active designs returned exact counterexamples;
- `inconclusive_active_jobs = 0`;
- all stored witnesses pass the H234 balanced predicate (5 groups, 4 distinct values per group, values in `0..15`);
- every active separator returned `n3 <= 2`;
- 12 genuinely new balanced witnesses after deduplication through H225-X17.

## X20 full exact rescreen

Artifact: `h225-x20-merged` id `9551144208`, digest `sha256:b1bf6cd78521a178b6f225c248027276dfb72b53910fc810e9615c0ca0914c20`.

Independent checks:
- exactly 44 canonical `(sector, chunk)` shards = 11 sectors x 4 chunks;
- chunk quotient-state totals sum to exactly **306,450**;
- sector quotient-state totals also sum to exactly **306,450**;
- every sector's chunk sum equals its sector total;
- all 12 X19 witnesses expand to 1,536 affine instances;
- exact surviving coefficient states = **0**;
- exact surviving legal shift tuples = **0**;
- every individual X20 chunk has zero exact survivors;
- `all_general_cyclic_affine_designs_rejected_by_augmented_witnesses = true`.

## Closure

**H225 exact cyclic-affine family is rigorously CLOSED / EXHAUSTED.**

This is a family-level impossibility result, not a profitable lottery strategy. The full H228 quotient universe of 306,450 coefficient states has now been eliminated at exact shift level by the accumulated balanced-witness cuts. No H225-X21/X22 continuation is warranted unless the mathematical family itself is deliberately broadened or changed.

Permanent machine-readable certificate: `data/derived/h225_x20_closure_certificate.json`.
