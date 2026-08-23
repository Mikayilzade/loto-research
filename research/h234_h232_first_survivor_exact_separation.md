# H234 — exact unrestricted separation of actual H232 survivors

Date: 2026-08-24
Scope: Rhode Island Keno H175 / H225 general cyclic-affine construction only.

## Trigger
H232 completed its strict 44-way merge and did **not** close the H225 family. The exact merged result screened all 306,450 H228 quotient coefficient states but retained **306,098** coefficient states and **139,869,763** legal shift tuples against the stored witness bank. Therefore the stored witness bank is only a necessary screen and is currently much too weak for family closure.

## H234 question
Do actual H232 shift-level survivors fail the original unrestricted universal condition once the full balanced-draw space is searched, rather than only the stored witnesses?

The target property remains: every balanced draw selecting exactly four values from each of the five 16-element groups must complete at least three design triples (`n3 >= 3`). A counterexample is any balanced draw with `n3 <= 2`.

## Deterministic packet
H232 has 44 disjoint `(sector, chunk)` jobs. H234 selects exactly one actual stored H232 survivor per chunk:
1. the first `first_exact_survivors` coefficient state in that chunk;
2. the first legal `first_shift_examples` tuple stored for that state.

This yields 44 concrete normalized H225 designs spanning every H232 execution partition. Each design contains six affine layers (three A layers plus normalized B/C/D), hence 1,536 triples.

## Exact separator
For each selected design H234 calls the unrestricted H180 MILP separator over all 80 draw variables. It enforces exactly four selected values in each of five groups and searches for a balanced draw completing at most two of the design's 1,536 triples.

A returned feasible witness is exact and breaks that selected design. It is also a legitimate new necessary cut for every future candidate because any universally valid design must have `n3 >= 3` on that balanced draw.

A timeout or a solver run with no feasible incumbent is **inconclusive**. It is never treated as validation.

## Execution and certificate discipline
H234 is sharded into 44 independent jobs, one per H232 chunk. The merge requires all 44 job identities exactly once. It records:
- selected actual designs;
- exact counterexamples found;
- inconclusive jobs;
- deduplicated balanced witnesses.

Outputs:
- `data/derived/h234_h232_first_survivor_separation.json`
- `data/derived/h234_new_witnesses.json`

Even if all 44 selected designs are broken, H234 alone does **not** prove the entire H225 family impossible. The resulting witness packet must be fed back into a family-wide H228/H232-style exact screen. Conversely, any unbroken job without an exact infeasibility proof remains open.

## Status at packet creation
H232 result: strongly negative for the current witness-bank screen, but not a surviving universal construction. H234 exact separation launched; result pending.
