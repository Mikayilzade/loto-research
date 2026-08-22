# H184 — exact rejection of the current H183 master candidate

Updated: 2026-08-22
Scope: LOTTERY ONLY
Status: **NO SUCCESS; CURRENT H183 CANDIDATE EXACTLY REJECTED**

## Target
Resume H183 from its persisted 254-cut checkpoint without repeating prior tests. The unresolved symmetry-reduced diagonal cyclic-affine master candidate recorded in STATUS was:

`[[3,16,94],[1],[9],[16]]`

with candidate parameters from

`PARAMS = [(a,a,c): a in {1,3,5,7,9,11,13,15}, c in 0..15]`.

Therefore the six transversal layers are:

- support `(0,1,2)`: `(a,c) = (1,3), (3,0), (11,14)`;
- support `(0,3,4)`: `(1,1)`;
- support `(1,3,4)`: `(1,9)`;
- support `(2,3,4)`: `(3,0)`.

The H175 guarantee gate remains universal `n3>=3` over every balanced draw choosing exactly four symbols from each of the five 16-symbol groups.

## Exact separator
An independent reconstruction of H183's separator MILP was run on this exact candidate.

Variables:
- 80 binary symbol-selection variables;
- 1,536 binary transversal-hit variables.

Constraints:
- exactly four selected symbols per each of five groups;
- hit variable can equal 1 only when all three symbols of its transversal triple are selected;
- total hit count `<=2`.

Solver: SciPy `milp` / HiGHS, presolve enabled, zero MIP relative gap, 30-second limit.

Result:

- solver status: **Optimal**;
- elapsed wall time in the run: about **2.43 s**;
- explicit balanced counterexample score: **`n3=2`**.

## Exact witness
Selected local symbols in groups 0..4:

```json
[
  [1,5,7,14],
  [4,6,9,13],
  [2,3,9,15],
  [1,8,11,15],
  [2,4,11,15]
]
```

Exactly two add-on triples are completed:

1. support `(0,1,2)`, first layer `(a,c)=(1,3)`: local triple `(7,9,3)`;
2. support `(0,1,2)`, second layer `(a,c)=(3,0)`: local triple `(1,4,15)`.

No other one of the 1,536 transversal triples is completed by the witness.

Thus the candidate violates the necessary H175 condition `n3>=3` and is rejected exactly.

## Consequence
This is a genuine new cut beyond H183's persisted 254-cut bank. It does **not** prove the symmetry-reduced diagonal cyclic-affine family infeasible, because the master must be re-solved after adding this witness. It also does not close arbitrary Latin/transversal designs.

The useful continuation state is now:

- prior persisted necessary cuts: 254;
- new H184 exact cut: 1;
- known necessary-cut total after merge: **255**;
- current recorded H183 master candidate: **REJECTED**.

A compact delta file is stored at `data/derived/h184_h183_new_witnesses.json`, so the next run can merge it with the H183 bank before solving the next master state.

## Reproducibility
- verifier: `src/loto_research/h184_h183_current_candidate_break.py`;
- delta witness: `data/derived/h184_h183_new_witnesses.json`.

## Result
**ЕЩЁ НЕ УСПЕХ.** The exact current H183 candidate is broken at `n3=2`; the restricted family remains open until the 255-cut master is re-solved and separated to infeasibility or a universally certified design.
