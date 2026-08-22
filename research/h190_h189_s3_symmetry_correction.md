# H190 — correction of H189 full-S3 canonicalization

Updated: 2026-08-22
Status: **NO SUCCESS; H189 REDUCTION REJECTED AS UNSAFE**

## Target
Audit H189 before building the proposed 5,120,640-representative master. The unresolved lottery target remains H175's 4,336-play doubled 3-spot hybrid and its universal balanced-draw requirement `n3>=3`.

## H189 claim under audit
H189 treated all permutations of groups `0,1,2` as symmetries of the restricted diagonal cyclic-affine family. This is true at the support-set level for the B/C/D supports, but a WLOG quotient also has to preserve the allowed **layer family** on A=`(0,1,2)`.

A restricted A layer is

`x2 = a*x0 + a*x1 + c (mod 16)`, with odd `a`.

The equality of the two input coefficients is part of the restricted family.

## Exact counterargument
Swap an A input with the A output, for example groups 0 and 2. With

`new_x0 = old_x2`, `new_x1 = old_x1`, `new_x2 = old_x0`,

the old equation becomes

`new_x2 = a^{-1}*new_x0 - new_x1 - a^{-1}*c (mod 16)`.

Its two input coefficients are `a^{-1}` and `-1`, which are equal only when `a=15 (=-1 mod 16)`. For a normal allowed value such as `a=3`, the image is a general cyclic-affine layer with unequal input coefficients, not a member of H180's restricted diagonal family.

Therefore a permutation that moves group 2 into an input position is not a global symmetry of the restricted diagonal family.

## Exhaustive verification
`src/loto_research/h190_a_support_s3_symmetry_audit.py` enumerates all 128 restricted A parameters `(a,c)` and all six coordinate permutations, compares the exact 256-triple image of every layer against all 128 allowed diagonal layers, and persists the result in `data/derived/h190_a_support_s3_symmetry_audit.json`.

Exact counts:

| permutation | diagonal A layers mapped back into family | global symmetry? |
|---|---:|---|
| `(0,1,2)` identity | 128/128 | yes |
| `(1,0,2)` swap the two inputs | 128/128 | yes |
| `(0,2,1)` | 16/128, only `a=15` | no |
| `(1,2,0)` | 16/128, only `a=15` | no |
| `(2,0,1)` | 16/128, only `a=15` | no |
| `(2,1,0)` | 16/128, only `a=15` | no |

Thus the global permutation subgroup preserving the whole restricted A family has order 2, not 6.

## Consequence
H189's quotient from H188's 36 normalized B/C coefficient pairs to 15 full-S3 orbits is **not a safe WLOG reduction for arbitrary A triples**. The claimed 5,120,640 exhaustive representative count is withdrawn.

H188 remains the last currently justified global canonical checkpoint:

`C(128,3) * 36 = 12,289,536` representatives,

subject to H187/H188's already-audited normalizations and B/C input-swap ordering.

The 15 H189 coefficient representatives can still be useful in special A subfamilies invariant under a larger permutation stabilizer (notably layers with `a=15`), but they cannot replace the global H188 master.

This correction does **not** invalidate the accumulated H183-H186 balanced witness cuts: those are direct legal balanced-draw necessary inequalities and do not depend on H189's quotient.

## Next action
1. Resume from H188's 12,289,536 globally justified canonical designs, reusing the full H185+H186 cut bank.
2. Seek additional symmetry only by computing the stabilizer of each actual three-layer A set; quotient B/C/D only under permutations that map that A set back into the restricted family.
3. Alternatively formulate the exact H188 master directly and separate feasible candidates; solver-certified infeasibility would close the restricted diagonal family.
4. Never treat H189's 15-orbit global quotient as exhaustive unless the A-stabilizer condition is explicitly proved for the candidate/subfamily.

## Result
**ЕЩЁ НЕ УСПЕХ.** H190 catches and corrects an unsafe symmetry reduction: the restricted H175 diagonal family is not globally invariant under full S3 on groups 0,1,2, so the authoritative exhaustive count returns to H188's 12,289,536 representatives.
