# H188 — H180 B/C shift normalization

Updated: 2026-08-22
Status: **NO SUCCESS; NEW EXACT WLOG REDUCTION**
Scope: lottery-only continuation of H175/H180.

## Target
Reduce the remaining restricted diagonal cyclic-affine master for the H175 4,336-play doubled 3-spot gate.

The unresolved condition remains universal `n3>=3` on every balanced `4+4+4+4+4` draw.

Restricted layers are

`z = a*x + a*y + c (mod 16)`, with odd `a`.

Supports are:
- A = `(0,1,2)`, three layers;
- B = `(0,3,4)`, one layer;
- C = `(1,3,4)`, one layer;
- D = `(2,3,4)`, one layer.

H187 proved the exact WLOG normalization `D=(a,c)=(1,0)`.

## New exact symmetry
After H187, use pure translations of the 16 labels in groups 0 and 1 only:

`x_0' = x_0 + t0`,
`x_1' = x_1 + t1`,

with groups 2,3,4 unchanged.

Because every layer is diagonal affine, translations preserve the family and preserve balanced 4-subsets bijectively.

For B, whose equation is

`z_4 = a_B*x_0 + a_B*x_3 + c_B`,

the group-0 translation changes only its shift:

`c_B' = c_B - a_B*t0 (mod16)`.

Since `a_B` is odd, it is a unit modulo 16. Therefore choose

`t0 = a_B^{-1} c_B (mod16)`

to obtain **`c_B'=0`**.

This translation does not change C or D. It changes A shifts, but A shifts are unrestricted master variables, so no design is lost.

Likewise, independently translate group 1:

`c_C' = c_C - a_C*t1 (mod16)`.

Choosing

`t1 = a_C^{-1} c_C (mod16)`

gives **`c_C'=0`**. This does not change B or D; it only relabels A shifts inside the same unrestricted family.

Thus every universal restricted design has an equivalent representative with

- `D=(1,0)`;
- `B=(a_B,0)`;
- `C=(a_C,0)`.

## B/C coefficient ordering
Swapping groups 0 and 1 leaves every A layer `z=a(x0+x1)+c` unchanged, swaps B and C, and leaves D unchanged. Therefore impose the exact WLOG order

`a_B <= a_C`

using the ordered odd list `{1,3,5,7,9,11,13,15}`.

There are `8*9/2 = 36` allowed `(a_B,a_C)` coefficient pairs.

## Representative count
A still chooses 3 distinct parameter ids from 128:

`C(128,3) = 341,376`.

B/C now contribute only 36 ordered coefficient pairs, and D is fixed to id0.

Therefore the new exact representative master size is

`341,376 * 36 = 12,289,536`.

Compared with H187's `2,818,400,256` representatives, this is an additional

`229.333...x`

reduction.

Compared with H180's original `715,917,361,152` raw restricted designs, the representative count is smaller by about

`58,254.22x`.

## Why this is safe
The proof uses only bijective relabelings of the 16 labels inside groups. Balanced draws map bijectively to balanced draws, completed triples map one-for-one, and hence the universal `n3>=3` property is invariant. No probabilistic or heuristic assumption is used.

## Solver consequence
The merged H185+H186 witness bank should now be solved under these stronger canonical constraints:

- support D fixed to parameter id 0 `(1,0)`;
- support B restricted to ids `{0,16,32,48,64,80,96,112}` (odd coefficient, zero shift);
- support C restricted to the same zero-shift ids;
- coefficient-index order `B<=C`;
- A remains three distinct ids from all 128 possibilities;
- all accumulated valid balanced witness cuts remain reusable unchanged.

The new master is small enough that the next packet should attempt the full merged cut solve again before adding more heuristic candidate attacks.

## Result
**ЕЩЁ НЕ УСПЕХ.** H188 proves a new exact canonicalization that shrinks the restricted diagonal cyclic-affine representative search from 2.818B to 12.290M designs, but it is not itself an infeasibility proof or a universal construction.