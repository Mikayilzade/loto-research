# H178 — H175 mixed-isotopy adversarial screen

Updated: 2026-08-22
Status: **NO SUCCESS; H175 REMAINS OPEN**

## Target
Continue H175's 4,336-play Rhode Island conditional doubled-3-spot construction without repeating the rejected single affine realization.

The support allocation remains:
- three Latin/transversal layers on groups `(0,1,2)`;
- one layer on `(0,3,4)`;
- one layer on `(1,3,4)`;
- one layer on `(2,3,4)`.

H175 proved all non-balanced 20-number draw compositions strict-positive by pair counting. A balanced `4+4+4+4+4` draw is safe iff the six add-on layers contain at least three fully selected transversal triples (`n3 >= 3`). Any balanced witness with `n3 <= 2` rejects a concrete six-layer design.

## New family screened
Instead of reusing the first GF(16) affine construction, H178 generated 100 deterministic mixed-isotopy designs. Each of the six 16x16 Latin squares was independently built as a row/column/output relabelling of either:
- the cyclic table `r+c (mod 16)`, or
- the XOR table `r xor c`.

This is a materially broader concrete search than H175's first fixed affine realization: all six layers can use independent symbol relabellings and mixed cyclic/XOR bases.

Seeds are `178000..178099`; the adversarial local-search seeds are `991000..991099`.

## Adversarial local search
For each design, balanced selections contain exactly four symbols from each of five 16-symbol groups. Greedy within-group swaps minimize the exact number of complete add-on triples.

Across 100 designs the best values found were:

| best n3 found | designs |
|---:|---:|
| 1 | 5 |
| 2 | 36 |
| 3 | 42 |
| 4 | 16 |
| 5 | 1 |

Thus **41/100 designs were directly rejected** by explicit balanced witnesses with `n3<=2` using only the local adversary. The remaining 59 are *not* validated; their local minima are merely heuristic upper bounds on the true minimum.

## Exact MILP follow-up
To prevent a misleading conclusion from local-search traps, H178 formulated the exact balanced-counterexample feasibility problem with binary selection variables and one binary hit variable per one of the 1,536 transversal triples:

- exactly four selected symbols in each group;
- `x_a+x_b+x_c-y_t <= 2` for every transversal triple, forcing `y_t=1` when all three endpoints are selected;
- `sum(y_t) <= 2`.

Any feasible MILP solution rigorously rejects that candidate.

Three heuristic-hard candidates were exactly cracked within the completed run:

- seed `178001`: exact balanced witness with `n3=2`;
- seed `178004`: exact balanced witness with `n3=2`;
- seed `178059`: this was the strongest local-search candidate (`best n3=5`), yet exact MILP found a balanced witness with **`n3=2`**.

For seed `178059`, one exact witness (local symbol indices within each 16-number group) is:

- G0: `{1,10,12,15}`
- G1: `{1,5,6,11}`
- G2: `{2,3,14,15}`
- G3: `{2,12,14,15}`
- G4: `{4,11,12,15}`

Direct evaluation gives exactly two complete transversal triples, so the H175 payout is:

`4240 + 35*2 = 4310 < 4336`.

Therefore this apparently strongest sampled design is strictly losing in its adversarial balanced draw and is rejected.

## What is and is not proved
H178 materially weakens the natural mixed group-table/isotopy route and demonstrates that local minima of 3–5 cannot be treated as evidence of a valid universal cover.

It does **not** prove impossibility of:
- all isotopies of cyclic/XOR Latin squares;
- arbitrary non-isotopic Latin squares of order 16;
- arbitrary six-layer transversal systems satisfying Latin constraints;
- other sub-4,560 hybrid support allocations.

Accordingly H175 stays open. The correct next mathematical step is a design-level CP-SAT/MILP/cutting-plane search whose master variables choose the Latin layers and whose adversary separates balanced `n3<=2` witnesses, rather than simply sampling concrete layers.

## Reproducibility
Code: `src/loto_research/h178_h175_mixed_isotopy_screen.py`

The script deterministically regenerates the 100 sampled designs, repeats the balanced local adversary, and includes exact MILP feasibility checks for selected hard seeds.

## Result
**ЕЩЁ НЕ УСПЕХ.** A broader natural H175 construction family repeatedly admits balanced `n3<=2` counterexamples; no universal 4,336-play design has yet been proved or constructed.
