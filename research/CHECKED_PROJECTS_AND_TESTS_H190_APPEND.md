# H190 audit append — H189 S3 symmetry correction

Updated: 2026-08-22
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H190 H175/H189 restricted 4,336-play master** | exact audit of H189 claim that full `S3` permutations of groups `0,1,2` preserve the restricted diagonal A-layer family | exhaustive `128 A layers × 6 permutations`: only identity and input-swap preserve all 128 layers; the other four preserve only the 16 layers with `a=15` | **H189 GLOBAL S3 QUOTIENT REJECTED AS UNSAFE**; `research/h190_h189_s3_symmetry_correction.md` |
| **H190 canonical checkpoint rollback** | reassess exhaustive representative count after invalid quotient removal | H189 `5,120,640` count withdrawn; last globally justified count returns to H188 `C(128,3)*36 = 12,289,536` | **OPEN restricted family**; accumulated H183-H186 direct balanced witness cuts remain valid |

Conclusion: no universal `n3>=3` construction and no restricted-family impossibility proof yet. Future symmetry reduction must use the stabilizer of the actual three-layer A set, not full S3 unconditionally.
