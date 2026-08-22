# H186 — H180 support-(2,3,4) coefficient normalization

Updated: 2026-08-22
Status: **NO SUCCESS; NEW EXACT 8x WLOG REDUCTION; CURRENT H185 MASTER REJECTED**

## Target
Continue the H175/H180 4,336-play doubled 3-spot balanced gate. The universal requirement remains: every balanced `4+4+4+4+4` draw must complete at least three of the six transversal layers (`n3>=3`).

Restricted layer family:

`z = a*x + a*y + c (mod 16)`, with odd `a`.

H183 already normalized the single layer on support `(2,3,4)` to `c=0`, leaving 8 possible odd coefficients `a`. H186 proves that coefficient itself can also be normalized WLOG.

## Exact new symmetry
Apply affine relabelings with a common odd scale `u` to groups 0,1,2,3, but an independently chosen odd scale `w` to group 4:

- groups `0..3`: `x'_g = u*x_g + v_g`;
- group `4`: `x'_4 = w*x_4 + v_4`.

For support `(0,1,2)`, both inputs and the output use scale `u`, so its diagonal coefficient `a` is unchanged.

For each support ending in group 4 — `(0,3,4)`, `(1,3,4)`, `(2,3,4)` — both inputs use scale `u` and the output uses scale `w`, so the coefficient becomes

`a' = (w/u) * a (mod 16)`.

Because every allowed `a` is an odd unit modulo 16, for the selected `(2,3,4)` layer one may choose

`w/u = a_D^{-1} (mod 16)`

and force `a_D'=1`.

Its transformed shift is

`c_D' = w*c_D + v_4 - a_D'*(v_2+v_3)`.

After coefficient normalization, choose `v_4` so that `c_D'=0`. Therefore **every universal design in the restricted family has an equivalent representative whose `(2,3,4)` layer is exactly `(a,c)=(1,0)`**, candidate id `0`.

Balanced 4-subsets are mapped bijectively, so the universal `n3>=3` property is preserved exactly.

The group-0/group-1 swap used by H183 still remains valid after this normalization, so the ordering constraint between the `(0,3,4)` and `(1,3,4)` single layers can be retained.

## Representative-space reduction
H183/H185 representative count:

`C(128,3) * [128*129/2] * 8 = 22,547,202,048`.

H186 fixes the final support to the single id `(1,0)`:

`C(128,3) * [128*129/2] = 2,818,400,256`.

Thus H186 gives an additional exact **8x WLOG reduction** relative to H183/H185, and about **254x** relative to H180's original 715,917,361,152 raw restricted designs.

## Exact attack on the current H185 master
H185 left unresolved ids

`[[18,54,111],[12],[88],[16]]`,

corresponding to:
- `(0,1,2)`: `(3,2),(7,6),(13,15)`;
- `(0,3,4)`: `(1,12)`;
- `(1,3,4)`: `(11,8)`;
- `(2,3,4)`: `(3,0)`.

An exact MILP separator was rebuilt independently with:
- 80 binary symbol variables;
- 1,536 binary hit variables;
- exactly four selected symbols per group;
- total completed transversal triples constrained to `<=2`.

HiGHS returned **Optimal**. Exact counterexample:

`[[1,5,8,13],[1,5,9,12],[3,7,11,15],[0,2,4,14],[0,10,12,14]]`

with exact **`n3=2`**.

So the current H185 master candidate is rejected; no timeout or heuristic score is being treated as proof.

## Normalized equivalent of the rejected H185 master
For its `(2,3,4)` coefficient `a_D=3`, choose `w/u=11`, since `3*11 = 1 (mod 16)`. Taking zero translations and then applying the allowed group-0/group-1 swap to restore the H183 ordering gives normalized ids

`[[18,54,111],[72],[84],[0]]`,

with parameters:
- `(0,1,2)`: `(3,2),(7,6),(13,15)`;
- `(0,3,4)`: `(9,8)`;
- `(1,3,4)`: `(11,4)`;
- `(2,3,4)`: `(1,0)`.

The transformed balanced witness

`[[1,5,9,12],[1,5,8,13],[3,7,11,15],[0,2,4,14],[0,4,10,14]]`

still has exact **`n3=2`**, directly checking the normalization on the concrete current candidate.

## Fresh normalized-master prototype
A deterministic prototype was also run with the new hard normalization `D=id0`.

Starting from 12 fresh balanced valid cuts, each rejected master supplied an explicit `n3<=2` witness; the full 128-element common-affine witness orbit `x -> u*x+v` was then added and deduplicated.

Completed adaptive cycles: **12**.

Results:
- 12/12 candidate masters explicitly rejected;
- exact-score histogram: `n3=2` for all 12;
- active unique rows grew from 12 to **1,172**;
- all 12 master solves returned feasible solver solutions before the explicit rejection.

This prototype is **new-method evidence only**, not a replacement for H185's authoritative 297-witness / 4,878-row bank and not an infeasibility proof.

## What H186 establishes
1. The H180 restricted family can be reduced WLOG by another factor of 8 by fixing the `(2,3,4)` single layer exactly to candidate id `0 = (a,c)=(1,0)`.
2. The current H185 unresolved master is exactly rejected at `n3=2`.
3. Its normalized representative is also explicitly rejected at `n3=2`.
4. A fresh 12-cycle normalized-master prototype rejected every adaptive candidate and produced 1,172 valid rows, supporting immediate migration of the persistent H185 bank into the stronger master.
5. The restricted family is **not yet proved impossible** because H185's full 4,878-row persistent bank has not yet been re-solved under the new `D=id0` normalization.

## Next action
1. Load H185's 297 stored witnesses / regenerate its 4,878 active rows, but replace the H185 `D:c=0` constraint with the stronger exact `D=id0` normalization.
2. Re-solve that persistent normalized master and immediately separate any survivor.
3. Continue with explicit `n3<=2` witnesses plus safe orbit rows until master infeasibility or independently certified exact-separator infeasibility.
4. If the diagonal family closes, expand to the general cyclic-affine `z=a*x+b*y+c` family while reusing all balanced witness cuts.

## Result
**ЕЩЁ НЕ УСПЕХ.** H186 gives a new exact 8x symmetry reduction and rejects the current H185 master at `n3=2`, but the full persistent normalized master has not yet been driven to infeasibility.