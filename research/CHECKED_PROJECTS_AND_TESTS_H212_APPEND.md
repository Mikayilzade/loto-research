# H212 audit append — H175 affine-unit orbit quotient

Updated: 2026-08-23

| ID | Lottery/mechanic | Hypothesis / test | Method | Result | Status |
|---|---|---|---|---|---|
| H212 | Rhode Island Keno / H175 restricted diagonal hybrid | H210 residual translations can be safely enlarged by common odd-unit scaling of all five coordinates, materially shrinking the exact restricted family | Derive action `(a,c)->(a,u*c+(2a-1)t) mod16`; exhaustively canonicalize all `C(128,3)=341,376` A 3-subsets under all `8*16=128` transformations | Exact A orbit count **3,992** with profile `{16:344,32:640,64:1088,128:1920}`; conservative B/C combination gives **143,712** representatives, 5.3396x fewer than H211 | **VALIDATED SAFE QUOTIENT; NO SUCCESS**. Universal `n3>=3` still unresolved. Code: `src/loto_research/h212_h175_affine_unit_orbits.py`; note: `research/h212_h175_affine_unit_orbits.md` |

Do not repeat H212 orbit enumeration unless the parameter family or symmetry assumptions change. Next use the 143,712 representatives against the accumulated exact balanced witness/cut bank.
