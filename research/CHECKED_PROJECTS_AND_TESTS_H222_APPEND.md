# H222 audit append

| ID | Lottery mechanism | Test / method | Result | Status |
|---|---|---|---|---|
| H222 | RI Keno H175 restricted hybrid | Exact single-process reformulation of H219: compute 4,878 witness rows, 3,992 H212 A-orbits and the `4878 x 3992` A-incidence matrix once, then evaluate all 36 B/C classes | Same exact 143,712-class predicate as H219, but removes 36-fold repeated orbit setup. Result file pending at packet creation. | **INCONCLUSIVE — exact H222 output pending**; `research/h222_single_process_exact_h175_screen.md`, `src/loto_research/h222_single_process_vectorized_screen.py` |

Zero survivors would close the H212-covered restricted family under H221; positive survivors still require exact `n3<=2` separation.
