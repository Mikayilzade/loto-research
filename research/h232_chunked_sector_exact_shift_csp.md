# H232 — 44-way chunked exact sector CSP

Date: 2026-08-23
Scope: H175 Rhode Island Keno / H225 general cyclic-affine family only.

## Motivation
H231 keeps the exact H230 predicate but assigns one full H228 sector to one workflow job. A difficult sector can still hit a sector timeout and prevent the strict 11-sector merge. H232 changes only execution granularity, not mathematics.

## Exact partition
For each of the 11 true H228 ordered-sector representatives, H232 deterministically enumerates the exact quotient coefficient-representative list and partitions its ordered list into four contiguous integer slices using `floor(n*c/4):floor(n*(c+1)/4)`.

Exact H228 sector state counts are asserted before solving:
`7806, 23052, 23052, 23052, 23052, 23052, 45760, 23052, 45760, 23052, 45760`, total **306,450**.

Thus H232 has exactly 44 disjoint/exhaustive `(sector, chunk)` jobs.

## Predicate
Every chunk applies the same two exact stages as H230/H231:
1. H226 rowwise best-legal-distinct-shift envelope, which safely rejects coefficient states that cannot possibly satisfy a stored balanced witness.
2. For every envelope survivor, exhaustive globally consistent legal shift CSP over all legal shift tuples: 4,096 / 1,920 / 560 states for all-distinct / one repeated / all-equal coefficient blocks.

No timeout or missing chunk is interpreted as evidence.

## Certificate conditions
The merge refuses to produce a certificate unless:
- all 44 expected `(sector,chunk)` pairs exist exactly once;
- all common witness/schema counts agree;
- every representative matches the authoritative H228 sector list;
- each sector's four chunk ranges exactly cover its asserted H228 quotient state count;
- grand total screened states is exactly **306,450**.

If the schema-valid merged result has `exact_shift_surviving_coefficient_states = 0`, the full H225 general cyclic-affine family is finitely impossible under the stored balanced witness bank plus H228 automorphism transport. If positive survivors remain, only those actual designs require unrestricted exact `n3<=2` separation.

Target result: `data/derived/h232_exact_shift_csp_merged.json`.

Status at packet creation: result pending; no closure claimed.
