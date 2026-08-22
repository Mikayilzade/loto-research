# H188 audit append — exact B/C shift normalization

Updated: 2026-08-22
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H188 H175/H180 4,336-play balanced transversal gate** | after H187 fixes D=`(1,0)`, independently translate group0 and group1 to eliminate B/C shifts | every restricted design has an equivalent representative with `c_B=c_C=0` | **VALID exact WLOG theorem**; `research/h188_h180_bc_shift_normalization.md` |
| **H188 B/C swap symmetry** | swap groups0 and1 after zero-shift normalization | impose `a_B<=a_C`; 36 ordered odd-coefficient pairs remain | **VALID exact symmetry reduction** |
| **H188 restricted master size** | A chooses 3 of 128 ids; B/C choose 36 ordered zero-shift coefficient pairs; D fixed id0 | **12,289,536 representatives**, down from H187 2,818,400,256 (**229.33x**) and ~58,254x below H180 raw space | **VALID exact reduction**; `data/derived/h188_bc_shift_normalization.json` |
| **H188 merged-master implementation** | reuse all H185+H186 balanced cuts under the new canonical constraints | solver implementation persisted for next exact run | **OPEN; next packet**; `src/loto_research/h188_bc_shift_normalized_master.py` |

Conclusion: no universal `n3>=3` construction and no restricted-family impossibility proof yet. The next exact master solve should use the H188 canonical form; do not return to the weaker H187 parameterization.