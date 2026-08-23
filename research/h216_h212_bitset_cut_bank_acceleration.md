# H216 — H212 exact cut-bank bitset acceleration

## Scope
Lottery-only continuation of the unresolved Rhode Island Keno H175 restricted diagonal hybrid. No new promotion assumptions and no reopening of closed execution channels.

## Starting checkpoint
H215 re-triggered H213, but `data/derived/h213_h212_cut_bank_survivors.json` remained absent. This is not mathematical evidence.

## Bottleneck diagnosis
H213 loops over all `143,712` H212 representatives and, for each, scans up to `4,878` exact necessary cut rows in Python. The worst-case scalar-check count is exactly `701,027,136` row checks, before the six component additions per row. This explains why a result can fail to appear promptly without implying infeasibility or survival.

## Exact replacement
Added `src/loto_research/h216_h212_bitset_cut_bank.py`.

The scientific predicate is unchanged. For every stored balanced witness row and every H212 design, require `n3 >= 3`. H216 only changes representation:

1. Enumerate the same 3,992 H212 A-orbit representatives and the same 36 zero-shift ordered B/C coefficient pairs.
2. For each exact cut row compute A contribution (0..3) to every A representative.
3. Encode the sets `A>=1`, `A>=2`, `A>=3` as Python integer bitsets.
4. For a fixed B/C pair and row, compute `q = B + C + D`; then the row requires `A >= 3-q`.
5. Intersect the corresponding bitsets over all 4,878 rows. Remaining bits are exactly the H213 survivors for that B/C pair.

Therefore H216 is solver-independent and scientifically equivalent to H213; it merely replaces hundreds of millions of Python scalar checks with about `36 × 4,878` large-integer bitset intersections plus deterministic preprocessing.

## Execution
Added `.github/workflows/h216-bitset-cut-bank.yml`, which runs the exact H216 screen and commits `data/derived/h216_h212_bitset_survivors.json`.

At this checkpoint the result file was not yet visible, so no survivor count or family-closure claim is made.

## Decision rule
- `survivor_count = 0` closes the H212/H214 restricted family under the accumulated exact cut bank.
- `survivor_count > 0` leaves only those explicit designs for exact `n3<=2` separation; survival is not validation.
- Missing result remains inconclusive.
