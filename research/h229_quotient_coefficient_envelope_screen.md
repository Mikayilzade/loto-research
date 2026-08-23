# H229 — exact H228-quotient coefficient-envelope screen

Date: 2026-08-23
Status: INCONCLUSIVE / exact computation launched

## Scope
Lottery-only continuation of H175 Rhode Island Keno / H225 general cyclic-affine family.

## Goal
Apply H226's exact coefficient-envelope rejection theorem directly to H228's corrected true-symmetry quotient rather than screening all 1,647,360 raw sector-pattern cases.

## Exact state space
H228 leaves 11 ordered-sector representatives. Under each sector's true stabilizer, the 45,760 3-multisets of A coefficient pairs reduce to a total of exactly **306,450 quotient coefficient states**.

H229 enumerates exactly one representative of each of those 306,450 states and applies H226's rowwise best-legal-distinct-shift upper bound on every stored balanced witness signature.

## Why quotient screening is safe
The H228 stabilizers are genuine automorphisms of the full support/design problem. If a representative coefficient state is killed by balanced witness W, every orbit mate is killed by the inverse-transformed balanced witness. Therefore one representative per stabilizer orbit is WLOG for existence/impossibility.

No assumption is made that the transformed witness must already occur as a separate stored row; the witness transformation itself is an exact balanced-draw certificate.

## Computation
For each representative sector:
- rebuild the full H226 general witness signatures;
- compute the best three distinct-shift incidences per A coefficient block;
- enumerate the exact coefficient-multiset orbit representatives under the true stabilizer;
- evaluate candidates in batches of 512;
- record survivor counts and a histogram of first killing witness rows.

Target result: `data/derived/h229_quotient_coefficient_envelope.json`.

## Interpretation
- If `envelope_survivor_count = 0`, the **entire H225 general cyclic-affine family is impossible** under the H175 universal `n3>=3` requirement, by H226 + H228.
- If survivors remain, they are only necessary-condition survivors. They still require globally consistent legal shifts and then exact `n3<=2` separation.
- Timeout or missing output proves nothing.

## Execution hardening
The workflow has a 180-minute limit and rebases before pushing the result so ordinary branch movement does not silently discard a completed computation.

## Next action
Read H229 result first. Zero closes the general cyclic-affine family. Positive survivors define the exact smaller state set for shift-level quotienting/search.
