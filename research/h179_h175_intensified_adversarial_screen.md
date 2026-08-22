# H179 — H175 intensified balanced-adversary screen

Updated: 2026-08-22
Status: **NO SUCCESS; H175 REMAINS OPEN**

## Target
Continue the H175 4,336-play conditional doubled Rhode Island 3-spot Keno construction without repeating closed tests. The unresolved gate is unchanged: for every balanced `4+4+4+4+4` 20-number draw, the six H175 transversal layers must contain at least three complete add-on triples (`n3>=3`). Any balanced witness with `n3<=2` rejects a concrete design.

## New packet
H178 screened 100 deterministic mixed cyclic/XOR Latin-isotopy designs using 15 greedy restarts and exact MILP on three candidates. H179 materially strengthens the adversary on the same deterministic design bank rather than generating another shallow sample:

- 40 balanced greedy restarts per design;
- up to 60 within-group swap-descent steps per restart;
- independent adversary seeds `200000..200099`;
- exact MILP follow-up on newly heuristic-hard candidates.

This is a stronger test, not a validation method: local minima above 2 remain only heuristic upper bounds on the true minimum.

## Intensified local-search result
Across all 100 H178 designs, H179 found the following best `n3` histogram:

| best n3 found | designs |
|---:|---:|
| 1 | 3 |
| 2 | 60 |
| 3 | 33 |
| 4 | 3 |
| 5 | 1 |

Therefore **63/100** concrete designs now have explicit balanced `n3<=2` counterexamples from this intensified adversary, versus 41/100 in H178.

The remaining heuristic-hard set is 37/100 designs. Their local scores are not proofs of safety.

## Exact MILP follow-up
The H178 exact feasibility formulation was reused: five groups each select exactly four symbols, every completed transversal forces a hit variable, and `sum(hits)<=2`.

New exact results in H179:

- seed `178033` (local best `n3=4`) -> exact feasible balanced witness with `n3=2`:
  - G0 `{1,4,13,14}`
  - G1 `{3,4,11,14}`
  - G2 `{6,8,10,13}`
  - G3 `{1,2,5,14}`
  - G4 `{3,5,10,14}`
- seed `178042` (local best `n3=4`) -> exact feasible balanced witness with `n3=2`:
  - G0 `{1,2,9,14}`
  - G1 `{4,6,7,11}`
  - G2 `{3,8,10,14}`
  - G3 `{0,5,7,15}`
  - G4 `{1,7,12,15}`
- seed `178008` (local best `n3=3`) -> exact feasible witness with `n3=2`.

For each such witness the H175 gross is `4240 + 35*2 = 4310 < 4336`, so the candidate is strictly rejected.

Short exact runs on several other heuristic-hard seeds reached the solver time limit without a feasible witness. A timeout is **not** evidence of infeasibility and is not counted as validation.

## Interpretation
H179 increases direct concrete failures from H178's 41 local counterexamples to 63 local counterexamples, while exact MILP independently breaks additional locally hard candidates. The gap between local scores and exact feasibility remains large, reinforcing H178's conclusion that sampled local minima cannot certify H175.

This packet still does **not** prove impossibility of an arbitrary six-layer Latin/transversal design. The correct next step remains a master-design CP-SAT/MILP/cutting-plane search with adversarial balanced-witness separation, or a combinatorial impossibility theorem.

## Result
**ЕЩЁ НЕ УСПЕХ.** The natural H175 mixed-isotopy bank is substantially weaker than H178's first screen suggested, but the universal 4,336-play design class is not yet closed.
