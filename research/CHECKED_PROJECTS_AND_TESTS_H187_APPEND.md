# H187 audit append — stronger support-(2,3,4) normalization

Updated: 2026-08-22
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H187 H175/H180 restricted diagonal cyclic-affine family** | group-wise affine relabeling with common odd scale on groups 0..3 and independent odd scale on group 4 | sole `(2,3,4)` layer can be normalized WLOG from arbitrary odd `a,c=0` to exactly `(a,c)=(1,0)` | **VALIDATED WLOG REDUCTION**; master orientations `22,547,202,048 -> 2,818,400,256` (additional exact 8x); `research/h187_h180_support4_coefficient_normalization.md` |
| **H187 concrete symmetry check** | normalize previously rejected candidate `[[18,54,111],[12],[88],[16]]` with `w/u=11` and restore B/C ordering by group-0/group-1 swap | equivalent normalized ids `[[18,54,111],[72],[84],[0]]`; transformed balanced witness has exact `n3=2` | **SYMMETRY MAP CHECKED**; not counted as a new rejection because H186 already rejected source candidate |
| **H187 normalized-master prototype** | hard-fix support `(2,3,4)` to id0; 12 fresh valid initial rows; adaptive candidate attack + 128-element safe affine witness orbit | **12/12** adaptive masters explicitly rejected, all at exact `n3=2`; active valid rows reached **1,172** | **PROMISING NEW FORMULATION; NOT INFEASIBILITY PROOF** |
| **H187 H185+H186 continuation code** | merge H185 297 stored witnesses with H186 189 new witnesses, regenerate valid affine-orbit union, solve under `D=id0` | reproducible continuation implemented | **NEXT EXACT SOLVE READY**; `src/loto_research/h187_support4_normalized_merged_master.py` |

Conclusion: no terminal success and no restricted-family impossibility proof yet. H187 removes seven of eight equivalent support-D coefficient orientations and should be used for the merged H185+H186 solve that follows H186's inconclusive timeout.
