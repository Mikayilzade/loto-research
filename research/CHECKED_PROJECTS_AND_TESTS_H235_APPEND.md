# H235 audit append — H234-augmented exact H232 rescreen

Date: 2026-08-24
Scope: lottery combinatorial coverage / H225 general cyclic-affine family only.

## New evidence consumed
H234 returned exact unrestricted balanced counterexamples for **44/44** selected real H232 shift-level survivor designs, with **0 inconclusive jobs** and **44 unique balanced witnesses**. Therefore none of those 44 selected survivors is universal.

## H235 test
The 44 H234 witnesses are each expanded by the full affine symmetry `x -> u*x+v (mod 16)` for odd `u`, giving 44×128 = **5,632** valid balanced witness instances before full-signature deduplication. They are appended to the exact H232 witness bank. The H228 306,450 quotient coefficient-state partition, 11 sectors × 4 chunks, envelope predicate, and exact globally consistent legal-shift CSP remain unchanged.

Files:
- `src/loto_research/h235_h234_augmented_exact_shift_rescreen.py`
- `.github/workflows/h235-h234-augmented-rescreen.yml`
- target `data/derived/h235_h234_augmented_exact_shift_rescreen.json`

## Interpretation rule
- If merged H235 reports `exact_shift_surviving_coefficient_states = 0`, H225 general cyclic-affine family is exactly closed by finite counterexample certificate.
- If survivors remain, H235 quantifies how much the 44 unrestricted counterexamples cut the H232 survivor mass; only actual survivors may be sent to the next unrestricted `n3<=2` separator.
- Missing merged output or a failed shard is **inconclusive**, never evidence of survival or impossibility.

Status at checkpoint creation: computation packet installed/triggered; merged authoritative result must be read before drawing the H235 conclusion.
