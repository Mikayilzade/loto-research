# H191 audit append — exact A-set stabilizer classification

Updated: 2026-08-22
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H191 H175/H188 restricted diagonal A-set stabilizers** | exhaustively test all 128 A-layers under all 6 coordinate permutations | only identity and input swap preserve all 128 layers; the other four permutations preserve exactly the 16 slope-15 layers | **EXACTLY CLASSIFIED**; `research/h191_a_set_stabilizer_classification.md` |
| **H191 exceptional full-S3 A-sets** | classify three-layer A-sets admitting extra symmetry | iff all three layers have `a=15`; exactly `C(16,3)=560` of `C(128,3)=341,376` A-sets | **VALID** |
| **H191 safe representative count** | apply H189's 15 B/C coefficient orbits only to exceptional S3 A-sets; retain H188's 36 choices elsewhere | safe count `340,816*36 + 560*15 = 12,277,776`, saving only 11,760 = 0.09578% from H188 | **VALID but negligible acceleration** |

Conclusion: no universal H175 `n3>=3` construction or impossibility proof yet. The stabilizer-quotient route is now materially exhausted; next work should focus on stronger cuts/separation or direct exact pruning.