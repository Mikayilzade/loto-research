# H231 — 11-way sector-sharded exact global-shift CSP

Date: 2026-08-23
Status: INCONCLUSIVE / exact computation launched

## Motivation
H230 is mathematically strong enough to close the full H225 general cyclic-affine family if it returns zero exact shift survivors, but its single-process result remained absent. H231 changes execution granularity without weakening the predicate.

## Exact decomposition
H228 proves that the complete general cyclic-affine existence search is WLOG represented by 11 true ordered-sector orbits. These sectors are independent at the final existence quantifier: a design belongs to exactly one normalized sector orbit. Therefore H230's 306,450 quotient coefficient states can be partitioned exactly by sector and solved independently.

H231 runs one exact process for each representative:
`(1,1),(1,3),(1,5),(1,7),(1,9),(1,15),(3,5),(3,9),(3,13),(5,9),(7,9)`.

Inside each shard the mathematics is unchanged from H230:
1. reconstruct the full exact general witness signatures;
2. enumerate exactly one H228 coefficient-multiset orbit representative;
3. apply the H226 optimistic envelope;
4. for every envelope survivor enumerate every legal globally consistent A-shift tuple;
5. retain a design only if the same shift tuple satisfies all stored balanced witness constraints.

## Exact shift spaces
- three distinct coefficient blocks: 4,096 assignments;
- exactly one repeated block: 1,920 canonical assignments;
- all three blocks equal: 560 canonical assignments.

Ordering shifts only inside identical coefficient blocks removes duplicate permutations of identical A layers and does not remove distinct designs.

## Merge certificate
The merge step is deliberately strict. It refuses to write the authoritative result unless:
- exactly 11 shard JSON files exist;
- sector indices are exactly 0..10;
- representatives match the H228 canonical list in order;
- common witness/schema counts agree across all shards;
- quotient coefficient-state counts sum exactly to 306,450.

Only after those assertions does it sum envelope survivors, exact surviving coefficient states, and exact surviving shift tuples.

Thus `exact_shift_surviving_coefficient_states = 0` in the merged schema-valid file is equivalent to the H230 zero-survivor certificate and closes the entire H225 general cyclic-affine family under H228 symmetry. A missing shard, timeout, failed merge, or absent merged file is inconclusive.

## Execution improvement
H230 concentrates all 11 sectors in one long job. H231 isolates them using a fail-fast-disabled 11-way matrix. A difficult sector can no longer erase completed work in other sectors, and the merge only certifies when all sectors are present. Each sector has a 90-minute ceiling; merge has a separate 15-minute ceiling.

## Target
`data/derived/h231_exact_shift_csp_merged.json`

## Next action
Check the merged H231 file first. If zero exact states, close H225 general cyclic-affine. If positive, exact-separate only the reported actual shift designs and add new balanced witnesses. If some shards fail, inspect those specific sectors rather than redesigning the entire screen.
