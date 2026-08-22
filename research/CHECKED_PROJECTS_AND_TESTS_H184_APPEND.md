# H184 audit append — exact rejection of current H183 master candidate

Updated: 2026-08-22
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H184 H175/H183 4,336-play balanced transversal gate** | exact MILP separator on current recorded master ids `[[3,16,94],[1],[9],[16]]` | HiGHS status **Optimal**; explicit balanced witness `[[1,5,7,14],[4,6,9,13],[2,3,9,15],[1,8,11,15],[2,4,11,15]]` completes exactly **n3=2** transversal triples | **CURRENT MASTER CANDIDATE REJECTED EXACTLY**; `research/h184_h183_current_master_exact_rejection.md` |
| **H184 persistent continuation delta** | add the new exact witness to H183's 254-cut bank | known necessary-cut count becomes **255** after merge | **OPEN restricted family**; delta `data/derived/h184_h183_new_witnesses.json` |

Conclusion: no universal `n3>=3` construction yet. Do not retest the rejected H183 candidate; merge the H184 delta with H183's persisted bank and re-solve the symmetry-reduced master.
