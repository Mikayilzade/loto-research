# H212 — H175 affine-unit orbit quotient

Updated: 2026-08-23
Status: **NO SUCCESS; RESTRICTED DIAGONAL FAMILY STILL OPEN**

## Target
Continue exact pruning of the H175 restricted diagonal RI Keno family from H211's 767,361 safe classes, without repeating closed promotion/execution searches.

## New safe symmetry
H210 used the residual translations

`(a,c) -> (a, c + (2a-1)t) mod 16`.

H212 observes that multiplying **all five group coordinates** by the same odd unit `u in {1,3,5,7,9,11,13,15}` also preserves the H188 normalization:
- B and C remain zero-shift singleton layers;
- D remains `(a,c)=(1,0)`;
- all layer coefficients are unchanged;
- balanced draws are mapped bijectively.

Combining common unit scaling with the H210 translation gives the exact action on every A layer

`(a,c) -> (a, u*c + (2a-1)t) mod 16`,

for 8 choices of `u` and 16 choices of `t`. These 128 maps are closed under composition and act as permutations of the 128 allowed A layers.

## Exact enumeration
`src/loto_research/h212_h175_affine_unit_orbits.py` exhaustively canonicalizes every `C(128,3)=341,376` A-layer 3-subset under the 128-element action.

Exact orbit profile:
- orbit size 128: 1,920 orbits;
- orbit size 64: 1,088 orbits;
- orbit size 32: 640 orbits;
- orbit size 16: 344 orbits;
- total exact A orbits: **3,992**.

A conservative combination with H188's 36 normalized B/C coefficient pairs therefore leaves

`3,992 * 36 = 143,712`

safe restricted-family representatives.

This is a **5.3396x reduction versus H211's 767,361 classes** and an **85.51x reduction versus H188's 12,289,536 classes**.

Nine H212 A-orbits lie wholly in the exceptional `a=15` sector. H212 deliberately does **not** multiply those by H191's 15 coefficient classes yet, because the combined affine-unit/S3 group action should be audited directly rather than assumed to factor. Thus 143,712 is conservative and safe.

## Consequence
No universal `n3>=3` construction and no impossibility certificate has yet been obtained. The next exact cut-bank enumeration can now operate on at most 143,712 representatives instead of 767,361.

## Next action
1. Canonicalize the 143,712 H212 representatives against the accumulated exact balanced witness/cut bank.
2. Persist exact survivor count/list.
3. Run exact `n3<=2` separation only on survivors; timeout/no-incumbent is inconclusive.
4. Separately audit the full combined affine-unit + exceptional S3 action for any additional safe quotient.

## Result
**ЕЩЁ НЕ УСПЕХ.** H212 safely shrinks the restricted H175 family to 143,712 representatives, but universal `n3>=3` remains unresolved.
