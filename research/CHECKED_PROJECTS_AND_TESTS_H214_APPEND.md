# H214 lottery audit append

Updated: 2026-08-23
Scope: lottery-only.

| ID | Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|---|
| H214 | RI Keno H175 restricted diagonal hybrid | Exact joint quotient of H212 affine-unit A-layer action with H191 exceptional full-S3 coordinate stabilizer | H212 has 3,992 A orbits, exactly 9 wholly in `a=15`; generic orbits retain 36 B/C classes while exceptional orbits use 15 legal S3 classes; exact safe joint count `3,983*36 + 9*15 = 143,523`, saving 189 (0.1315%) vs H212 | **VALIDATED safe quotient; NO SUCCESS**. Universal `n3>=3` remains open. `research/h214_h212_h191_joint_symmetry_audit.md`, `src/loto_research/h214_h212_h191_joint_symmetry_audit.py`, `data/derived/h214_h212_h191_joint_symmetry_summary.json` |

Do not re-test whether H212 and H191 can be combined: H214 closes that compatibility question exactly. Next useful work is exact accumulated-cut screening of the 143,523 joint representatives and exact separation of survivors.
