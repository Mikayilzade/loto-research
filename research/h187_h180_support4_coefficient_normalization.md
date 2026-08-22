# H187 — H180 support-(2,3,4) coefficient normalization

Updated: 2026-08-22
Status: **NO SUCCESS; NEW EXACT 8x WLOG MASTER REDUCTION**

## Starting checkpoint
H186 is the authoritative previous packet. It produced 189 new explicit balanced `n3<=2` witnesses, 18,952 unique H186-only affine-orbit rows, rejected two restricted diagonal cyclic-affine candidates, and then reached a master time limit with no incumbent. Per project rules that timeout is inconclusive.

H187 targets that exact bottleneck: reduce the restricted master further before merging/re-solving H185+H186 rows.

The H175 requirement remains universal `n3>=3` for every balanced `4+4+4+4+4` draw. Restricted layers are

`z = a*x + a*y + c (mod 16)`, with odd `a`.

## New exact WLOG symmetry
H183 already normalized the single layer on support `(2,3,4)` to `c=0`, leaving 8 possible odd coefficients `a`.

H187 proves that coefficient can also be normalized WLOG.

Apply affine relabelings with a common odd scale `u` to groups 0,1,2,3 but an independently chosen odd scale `w` to group 4:

- groups `0..3`: `x'_g = u*x_g + v_g`;
- group `4`: `x'_4 = w*x_4 + v_4`.

For support `(0,1,2)`, both inputs and the output carry scale `u`, so its diagonal coefficient remains `a`.

For each support ending in group 4 — `(0,3,4)`, `(1,3,4)`, `(2,3,4)` — the transformed coefficient is

`a' = (w/u) * a (mod 16)`.

Every allowed `a` is an odd unit modulo 16. For the selected `(2,3,4)` layer choose

`w/u = a_D^{-1} (mod 16)`

to force `a_D'=1`.

The transformed shift on `(2,3,4)` is

`c_D' = w*c_D + v_4 - a_D'*(v_2+v_3)`.

Choose `v_4` so that `c_D'=0`. Thus **every universal design in the restricted family has an equivalent representative whose `(2,3,4)` layer is exactly candidate id `0 = (a,c)=(1,0)`**.

The transformation is a bijection on local symbols, hence maps balanced four-subsets bijectively and preserves the universal `n3>=3` property exactly.

The H183 group-0/group-1 swap remains valid after this normalization, so the ordering constraint between the `(0,3,4)` and `(1,3,4)` single layers can still be used.

## Master-space reduction
H183/H185/H186 WLOG representative count:

`C(128,3) * [128*129/2] * 8 = 22,547,202,048`.

H187 fixes the `(2,3,4)` layer to the single id `(1,0)`:

`C(128,3) * [128*129/2] = 2,818,400,256`.

This is an additional exact **8x reduction** relative to the master used through H186, and approximately 254x fewer representative orientations than H180's original 715,917,361,152 raw restricted designs.

## Concrete sanity check
H185's recorded candidate `[[18,54,111],[12],[88],[16]]` has `(2,3,4)` coefficient `a_D=3`. Since `3^{-1}=11 (mod 16)`, choose `w/u=11`. With zero translations, then applying the allowed group-0/group-1 swap to restore the ordering convention, an equivalent normalized representative is

`[[18,54,111],[72],[84],[0]]`.

Parameters:
- `(0,1,2)`: `(3,2),(7,6),(13,15)`;
- `(0,3,4)`: `(9,8)`;
- `(1,3,4)`: `(11,4)`;
- `(2,3,4)`: `(1,0)`.

The known balanced witness transforms to

`[[1,5,9,12],[1,5,8,13],[3,7,11,15],[0,2,4,14],[0,4,10,14]]`

and has exact `n3=2` for the normalized representative. This is a direct computational check of the symmetry map; H186 had already independently rejected the original candidate, so H187 does not count this as a new candidate rejection.

## Fresh normalized-master prototype
A deterministic prototype was run with the stronger hard constraint `(2,3,4)=id0`.

Starting from 12 fresh valid balanced rows, each adaptive master candidate was attacked; each explicit witness was exactly rescored and its safe 128-element common-affine orbit `x -> u*x+v` was added/deduplicated.

Completed cycles: **12**.

Results:
- **12/12** adaptive masters explicitly rejected;
- exact score histogram: `n3=2` ×12;
- active unique valid rows grew from 12 to **1,172**;
- all 12 master calls returned feasible candidates before those candidates were explicitly rejected.

This is new-method evidence only, not an infeasibility proof and not a substitute for the authoritative H185/H186 witness banks.

## Why this matters after H186
H186's 18,952-row follow-up solve timed out without an incumbent. H187 removes seven of the eight possible `(2,3,4)` coefficient choices **without excluding any possible universal design**. Therefore the next merged H185+H186 solve should use this normalized master rather than spending solver effort across all eight equivalent coefficient orientations.

## Next action
1. Merge H185's 297 stored witnesses with H186's 189 new witnesses, deduplicating across packets.
2. Regenerate the full valid affine-orbit union.
3. Re-solve under the stronger H187 constraint `(2,3,4)=id0`, retaining the H183 B/C ordering symmetry.
4. If feasible, attack the survivor with explicit `n3<=2` separation and persist the new witness; if certified infeasible, the entire restricted diagonal family is closed.
5. Never interpret timeout/no-incumbent as infeasibility.
6. If the diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c` using the accumulated balanced witness bank.

## Result
**ЕЩЁ НЕ УСПЕХ.** H187 cuts the restricted master by another exact 8x and directly targets H186's solver bottleneck, but the merged persistent master has not yet been certified infeasible.