# H180 audit append — H175 master cutting-plane

Updated: 2026-08-22
Scope: LOTTERY ONLY
Terminal status: **NO SUCCESS; NOT EXHAUSTED**

| ID | Lottery mechanism / hypothesis | Test | Result | Status / evidence |
|---|---|---|---|---|
| H180 | Rhode Island Keno conditional doubled 3-spot H175 hybrid cover; balanced `n3>=3` gate | Build exact master MILP over diagonal cyclic-affine Latin layers `z=a*x+a*y+c mod 16`, 128 layers/support, choosing 3+1+1+1 layers; iteratively add exact balanced `n3<=2` separator witnesses | Restricted master universe contains `C(128,3)*128^3 = 715,917,361,152` designs. Deterministic seed 180180 completed 20 adaptive master/separator cycles; every chosen design had an exact balanced counterexample. Separator scores: 4 with `n3=0`, 1 with `n3=1`, 15 with `n3=2`. Master not yet infeasible. | **REJECTED 20 adaptive candidates; FAMILY STILL OPEN.** Stronger than H178/H179 random/fixed-bank screening but not a universal impossibility proof. `research/h180_h175_master_cutting_plane.md`; `src/loto_research/h180_h175_master_cutting_plane.py` |

Do not repeat H178/H179-style shallow sampling as the main next step. Continue persisted exact cutting-plane separation until restricted-family infeasibility or independently certified separator infeasibility, then expand to independent `(a,b)` cyclic-affine layers if needed.
