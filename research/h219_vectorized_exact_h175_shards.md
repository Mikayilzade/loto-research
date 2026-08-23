# H219 — vectorized exact H175 shard screen

## Scope
Lottery-only continuation of the H175 Rhode Island Keno hybrid proof search. No non-lottery branches considered.

## Question
Can the H217/H218 exact necessary-cut screen be made materially cheaper without changing the scientific predicate or proof standard?

## Result
Yes. H217 rebuilds 3 threshold masks for every one of 4,878 witness rows inside every B/C shard: 14,634 Python big-integer masks per shard. H219 replaces that representation with the exact incidence matrix already implicit in the calculation.

For each shard:
- exact stored witness rows: 4,878;
- H212 A-orbit representatives: 3,992;
- A incidence matrix shape: `4878 x 3992`;
- one normalized B/C pair and fixed D=0;
- survivor predicate is exactly `A(row,candidate)+B(row)+C(row)+D(row) >= 3` for every row.

The new code computes this predicate directly with NumPy broadcasting and `np.all(..., axis=0)`. Maximum incidence is 6, so `uint8` is exact and overflow-free.

This is a computational equivalence, not a new mathematical assumption. A zero merged survivor count would still be a cut-bank closure of the H212 normalized restricted family; any survivors still require exact `n3<=2` separation before validation. Timeout or missing output never validates a design.

## Execution
Added:
- `src/loto_research/h219_vectorized_bc_shards.py`
- `.github/workflows/h219-vectorized-bc-shards.yml`

The workflow runs all 36 B/C shards independently, requires every shard for merge, and commits `data/derived/h219_vectorized_merged_survivors.json` only after strict schema/count checks.

## Current checkpoint
At packet completion the H218 merged output was still absent. H219 therefore makes no survivor-count, restricted-family closure, or universal H175 claim yet.

Status: **INCONCLUSIVE / computational packet completed; exact merged result pending**.
