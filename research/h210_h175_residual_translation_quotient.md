# H210 — H175 residual translation quotient

Updated: 2026-08-23
Status: **NO SUCCESS; RESTRICTED DIAGONAL FAMILY STILL OPEN**

## Target
Continue H175/H191 exact pruning without repeating the data-blocked H209 promotion search. The unresolved mathematical gate remains universal `n3>=3` for every balanced `4+4+4+4+4` draw in the restricted diagonal cyclic-affine family.

## New exact symmetry
H188 normalized the three singleton supports B=(0,3,4), C=(1,3,4), D=(2,3,4) to zero shifts, with D fixed to `(a,c)=(1,0)`. H210 identifies a residual coordinate translation that preserves all those normalizations.

For any `t mod 16`, translate coordinates by:

- group 0: `x0 -> x0 - t`;
- group 1: `x1 -> x1 - t`;
- group 2: `x2 -> x2 - t`;
- group 3: `x3 -> x3 + t`;
- group 4 unchanged.

On B, C and D, the two translated input coordinates cancel, so their zero shifts remain zero and their coefficients are unchanged. On an A=(0,1,2) diagonal layer

`x2 = a*x0 + a*x1 + c (mod 16)`,

the induced parameter action is

`(a,c) -> (a, c + (2a-1)t mod 16)`.

Every allowed `a` is odd, hence every `2a-1` is also odd and invertible modulo 16.

## Free action on 3-layer A sets
For nonzero `t`, translation by `(2a-1)t` on the 16 possible shifts for each fixed `a` has cycle length

`16 / gcd(t,16)`,

which is one of `2,4,8,16`. Therefore a nonidentity translation has **no 1-cycles** and every orbit has even cardinality. An invariant 3-element subset cannot be formed as a union of such cycles.

Thus the `C16` action is free on all A-layer 3-subsets.

Exact counts:

- raw H188 A sets: `C(128,3) = 341,376`;
- residual-translation A orbits: `341,376 / 16 = 21,336`;
- H188 B/C normalized coefficient pairs: `36`;
- H210 exact representatives: `21,336 * 36 = 768,096`.

This is an exact **16x reduction** from H188's `12,289,536` representatives. It is also far stronger than H191's small stabilizer-only saving, although H210 does not yet combine the two quotient systems into a single further-reduced count.

## Validation
`src/loto_research/h210_residual_translation_orbits.py` explicitly constructs the parameter action, enumerates its cycle profiles for all 16 translations, asserts that every nonidentity cycle length is in `{2,4,8,16}`, and reproduces the exact counts above.

## Consequence
The restricted diagonal family is **not** proved impossible and no universal construction is validated. However, future exact cut enumeration/master work can operate on only 768,096 H210 translation classes rather than 12.29 million H188 representatives, without losing any universal solution.

## Next action
1. Canonicalize each A 3-set under the H210 `C16` action and enumerate the 768,096 representatives against the accumulated exact balanced witness/cut bank.
2. If no representative survives all valid cuts, obtain an independently reproducible exact infeasibility certificate for the restricted diagonal family.
3. If survivors remain, persist them and run exact `n3<=2` separation only on survivors.
4. Do not interpret timeouts as validation.

## Result
**ЕЩЁ НЕ УСПЕХ.** H210 safely reduces the exact restricted H175 search space by 16x to 768,096 representatives, but universal `n3>=3` remains unresolved.
