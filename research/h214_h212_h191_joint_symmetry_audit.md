# H214 — joint H212 affine-unit + H191 exceptional-S3 symmetry audit

Updated: 2026-08-23
Status: **NO SUCCESS; NOT EXHAUSTED**
Scope: lottery-only continuation of H175 restricted RI Keno hybrid mathematics.

## Question
H212 reduced the restricted diagonal H175 family to 3,992 exact A-layer orbits and conservatively retained all 36 normalized B/C coefficient pairs, giving 143,712 representatives. H191 had previously proved that full coordinate S3 is legal only when all three A layers have slope `a=15`. H212 deliberately did not assume that the two quotients factor.

H214 audits the joint action exactly.

## Exact structure
For `a=15`, every A layer is

`x0 + x1 + x2 = c (mod16)`.

Thus every coordinate permutation in S3 fixes each individual exceptional A layer setwise. H212's affine-unit action maps only the shift parameter inside this same exceptional sector. Consequently the coordinate S3 action and the H212 A-orbit action are compatible at the set level; no generic A layer is granted the extra symmetry.

Exact H212 enumeration contains:
- 3,992 total A orbits;
- 9 A orbits lying wholly in the `a=15` exceptional sector;
- 3,983 generic A orbits.

For generic A orbits, retain all 36 normalized B/C coefficient pairs.
For each exceptional A orbit, the legal S3 coefficient renormalization gives the exact 15 classes already established by the H189 coefficient calculation and licensed by H191 only in this sector.

Therefore the safe joint count is

`3,983*36 + 9*15 = 143,523`.

This is a reduction of only 189 representatives from H212's 143,712, i.e. about 0.1315%.

## Interpretation
The joint symmetry issue left open by H212 is now closed: the exceptional H191 quotient can be combined safely with H212, but the improvement is negligible. It does not prove universal `n3>=3`, nor impossibility of the restricted family.

The highest-value next step remains direct exact screening of the **143,523** joint representatives against the accumulated 4,878 exact balanced witness rows, followed by exact `n3<=2` separation only for survivors.

## Reproducibility
- Code: `src/loto_research/h214_h212_h191_joint_symmetry_audit.py`
- Data summary: `data/derived/h214_h212_h191_joint_symmetry_summary.json`

## Result
**ЕЩЁ НЕ УСПЕХ.** H214 safely reduces the restricted H175 family to 143,523 joint symmetry classes; universal `n3>=3` remains unresolved.
