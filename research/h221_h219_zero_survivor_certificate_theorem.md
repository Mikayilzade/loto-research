# H221 — zero-survivor certificate theorem for the H175 restricted family

Date: 2026-08-23
Scope: lottery-only; Rhode Island Keno H175 mathematical branch.

## Question

If H219 eventually reports `survivor_count = 0` across its 143,712 H212-normalized classes, is a second family-level MILP infeasibility certificate required before the restricted diagonal family can be declared impossible?

## Result

**No.** A verified zero-survivor H219 output is itself a finite exact impossibility certificate for the H212-covered restricted family. A second master-MILP certificate would be redundant.

## Proof

Let `F` be the H175 restricted diagonal candidate family after the already-proved H187/H188 normalizations: D fixed to `(1,0)`, B/C zero shifts with coefficient ordering, and A containing three restricted diagonal layers.

H212 proves an exact 128-element residual affine action on A,

`(a,c) -> (a, u*c + (2a-1)t) mod 16`, with odd `u` and `t in Z/16Z`,

while preserving the normalized B/C/D structure and the universal `n3>=3` property. Enumerating this action gives exactly 3,992 A-orbits. Combined with the 36 normalized B/C coefficient pairs, every candidate in `F` is represented by one of exactly `36 * 3992 = 143,712` H212 classes.

For a fixed candidate representative, every H219 cut row is not a relaxation invented by the screen: it is the exact layer-incidence vector of an explicit balanced `4+4+4+4+4` draw witness reconstructed by H187 from the H185/H186 witness banks and safe common-affine witness orbits. The H219 predicate requires total incidence at least 3 on every such exact witness row.

Therefore, if a representative is rejected by H219, there exists an explicit balanced draw in the stored bank with `n3 <= 2` for that representative. Applying the inverse H212 symmetry maps that witness back to any original candidate in the same orbit while preserving `n3`. Hence every candidate represented by that rejected class also fails universal `n3>=3`.

If H219 reports zero survivors, all 143,712 normalized classes are rejected by at least one exact witness. Since those classes cover all of `F` modulo proved symmetries, no member of `F` can satisfy universal `n3>=3`.

This is exhaustive finite enumeration plus explicit counterexample coverage, not heuristic sampling. No separate solver-certified infeasibility result is logically necessary.

## What zero survivors would and would not prove

A verified zero result would close only the **restricted diagonal family** screened by H212/H219. It would not close the broader cyclic-affine family `z=a*x+b*y+c (mod 16)` with independently varying odd `a,b`, nor the unrestricted combinatorial H175 design space.

A positive H219 survivor count proves nothing universal: every survivor must still undergo exact `n3<=2` separation.

## Current state

At H221 time, `data/derived/h219_vectorized_merged_survivors.json` is still absent, so the antecedent of the theorem is not yet established. H221 makes no impossibility or SUCCESS claim.

## Next action

Check H219 output first. If a schema-valid merged file reports zero survivors, close the H212 restricted diagonal family immediately by this theorem and expand the mathematical search to general cyclic-affine `z=a*x+b*y+c (mod16)`, reusing the exact witness bank. If survivors remain, exact-separate only those survivors.
