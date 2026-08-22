# H183 audit append — H180 symmetry reduction and persistent exact counterexamples

Updated: 2026-08-22
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H183 H175/H180 4,336-play balanced transversal gate** | WLOG symmetry reduction of diagonal cyclic-affine master `z=a*x+a*y+c mod16` | common translation normalizes chosen `(2,3,4)` layer to `c=0`; group-0/1 swap permits ordering the `(0,3,4)` and `(1,3,4)` candidates; representative master shrinks from **715,917,361,152** raw designs to **22,547,202,048** orientations | **VALIDATED symmetry reduction**; `research/h183_h180_symmetry_reduced_persistent_cut_bank.md` |
| **H183 adaptive cutting-plane continuation** | resume H180 master and attack successive master candidates with explicit balanced witnesses; exact MILP fallback on heuristic-hard state | **246 additional master candidates rejected** with exact witness scores `n3=0:20`, `n3=1:45`, `n3=2:181`; one local `n3=3` hard candidate exactly broken at `n3=2` | **NO SUCCESS / restricted family still open**; persisted 254-cut bank in `data/derived/h183_h180_witness_bank.zlib.b64` |
| **H183 persistent checkpoint** | solve symmetry-reduced master after all 8 initial + 246 adaptive cuts | master remains feasible; current unresolved ids `[[3,16,94],[1],[9],[16]]` | **OPEN; next separator target**; `src/loto_research/h183_h180_symmetry_persistent_cuts.py` |

Conclusion: no universal `n3>=3` six-layer construction and no restricted-family impossibility proof yet. Do not repeat the first 254 cuts; load the persisted H183 witness bank and continue separation.
