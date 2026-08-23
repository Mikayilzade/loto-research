# H227 — exact cross-sector symmetry for the H225 general cyclic-affine family

Date: 2026-08-23
Status: VALIDATED mathematical reduction; NO lottery SUCCESS

## Question
Can the 36 H225 normalized B/C sectors be reduced further by symmetries of the 5-group support hypergraph, before spending compute on coefficient/shift screening?

## Support automorphisms
The six-layer H175 hybrid uses four support types for its affine layers:
- A = {0,1,2}
- B = {0,3,4}
- C = {1,3,4}
- D = {2,3,4}

The support hypergraph has automorphism group `S3 x S2` of order 12: arbitrary permutation of groups {0,1,2}, independently of swapping groups 3 and 4.

Because every general cyclic-affine layer has odd coefficients, every coefficient is a unit modulo 16. Therefore after permuting the three vertices of a support, the affine graph equation can always be solved for the newly designated output coordinate and remains a general cyclic-affine layer with odd coefficients. The family is closed under all 12 support automorphisms.

## Action on normalized B/C sectors
H225 normalization writes the three sole layers as
`x4 = xi + q_i*x3`, with projective triple `q=(beta,gamma,1)` for i=0,1,2.

A permutation of {0,1,2} permutes the three entries of q. Re-normalizing D to coefficient 1 divides all three q entries by the new third entry. Thus S3 acts projectively on `(beta,gamma,1)`.

Swapping groups 3 and 4 reorients `x4 = xi + q_i*x3` to an equivalent equation with coefficient proportional to `q_i^{-1}`. After the same H225 normalization, the induced action is inversion of the projective q triple.

The exact finite action is implemented in `src/loto_research/h227_general_sector_hypergraph_symmetry.py` and all 12 maps are distinct permutations of the 36 normalized sectors.

## Exact result
The 36 unordered H225 sectors collapse to exactly **11 cross-sector orbits** with orbit sizes:
`1,4,4,2,2,2,6,3,6,3,3`.

Representatives are:
`(1,1), (1,3), (1,5), (1,7), (1,9), (1,15), (3,5), (3,9), (3,13), (5,9), (7,9)`.

Thus an exhaustive sector-by-sector H226-style coefficient-pattern search needs only 11 representative sectors instead of 36. Since each sector has 45,760 coefficient multisets, the top-level sector-pattern workload falls exactly from
`36*45,760 = 1,647,360`
to
`11*45,760 = 503,360`, a **3.272727x** reduction before any coefficient-envelope rejection or residual shift quotienting.

This does not assume that survivor counts are equal between raw sectors; it is a WLOG equivalence of complete design spaces. If a universal design exists in any member of a sector orbit, applying the inverse support automorphism gives a universal design in the representative sector. Likewise, a counterexample/impossibility proof transported through the symmetry is valid for the whole orbit.

## Why this matters for H226/H225
H226's pending 36-sector coefficient envelope is still valid, but future exact general-family work should not repeat all 36 sectors. The 11 representatives are sufficient for existence/impossibility search. Their stabilizer sizes (12/orbit size) are also now known and can be exploited to quotient A coefficient/shift states inside each representative sector.

## Limits
This packet does **not** claim that H225's previous 36,243,104 canonical-design count simply divides by 36/11; stabilizers vary by sector, so an exact expanded-group Burnside count would need a separate calculation. H227 only proves the exact WLOG reduction needed for exhaustive search.

## Next action
Use the 11 representative sectors plus their stabilizers to build the next exact coefficient/shift quotient. Prefer a direct stabilizer action on A coefficient triples before any raw shift enumeration. Continue to accept a late H226/H224 result if it appears, but do not spend another packet only waiting for it.
