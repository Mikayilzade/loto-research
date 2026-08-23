# H225 append — 2026-08-23

- Scope: lottery-only H175 Rhode Island Keno general cyclic-affine extension `z=a*x+b*y+c (mod16)`, odd `a,b`.
- H224 restricted-family exact result remained absent at packet start; no closure inferred.
- Proved exact affine-coordinate normalization of sole B/C/D layers to `D=(1,1,0)`, `B=(1,beta,0)`, `C=(1,gamma,0)` with 36 unordered odd `(beta,gamma)` sectors.
- Derived exact 2048-element residual stabilizer and its action on A layers; residual action preserves A coefficient pair `(a,b)` and moves only shift `c`.
- Used Burnside on 3-element A subsets without enumerating `C(1024,3)` designs.
- Exact normalized raw space: `6,423,588,864` classes.
- Exact canonical general cyclic-affine space after residual quotient + B/C swap treatment: **36,243,104** classes, a **177.236x** reduction.
- No heuristic or timeout used for this count.
- Status: **NO SUCCESS; NOT EXHAUSTED**. General family is now finite and materially smaller; exact cut-bank screening/separation remains to be done.
- Files: `research/h225_general_cyclic_affine_normalization_and_burnside.md`, `src/loto_research/h225_general_cyclic_affine_normalization.py`, `src/loto_research/h225_general_cyclic_affine_burnside.py`.
