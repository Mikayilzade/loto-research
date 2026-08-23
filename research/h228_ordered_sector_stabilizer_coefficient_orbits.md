# H228 — corrected ordered-sector symmetry and exact A-coefficient multiset quotient

Date: 2026-08-23
Status: NO SUCCESS; NOT EXHAUSTED

## Why H227 needed correction
H227 obtained the right 11 representative sector labels, but it canonicalized `(beta,gamma)` to `beta<=gamma` after every `S3 x S2` image and then treated the resulting 12 maps on 36 unordered representatives as a group action. That step is not rigorous: the beta/gamma swap subgroup is not normal inside the full S3 coordinate action, so quotienting first does not produce a well-defined group action on the 36 unordered representatives. Consequently the H227 orbit-size/stabilizer list on the 36-sector set is not valid as stated.

## Correct action
Work first on all 64 ordered normalized sectors `(beta,gamma)` with beta,gamma odd. The genuine order-12 group acts by projective S3 permutation of `(beta,gamma,1)` plus inversion from swapping groups 3/4. On this ordered set the action closes exactly and gives 11 orbits.

Representatives remain exactly:
`(1,1),(1,3),(1,5),(1,7),(1,9),(1,15),(3,5),(3,9),(3,13),(5,9),(7,9)`.

Correct ordered orbit sizes are:
`1,6,6,3,3,3,12,6,12,6,6`, summing to 64.
Corresponding stabilizer sizes are:
`12,2,2,4,4,4,1,2,1,2,2`.

Thus the useful H227 conclusion — only 11 sector representatives are needed for an existence/impossibility search — survives, but the earlier unordered-sector orbit/stabilizer arithmetic must not be reused.

## Exact action on A coefficient pairs
An A layer is written as
`a*x0 + b*x1 - x2 + c = 0`.
Under any permutation of groups 0,1,2, the coefficient triple `(a,b,-1)` is permuted and then multiplied by the unique odd unit that restores the output coefficient to `-1`. This maps the 64 odd coefficient pairs `(a,b)` bijectively to themselves. The group-3/4 flip leaves A coefficient pairs unchanged.

For each of the 11 ordered-sector representatives, H228 projects the exact sector stabilizer to its distinct actions on the 64 A coefficient pairs, then enumerates exact orbits of all `C(66,3)=45,760` three-multisets of coefficient pairs.

Exact orbit counts by representative:
- `(1,1)`: 7,806
- `(1,3)`: 23,052
- `(1,5)`: 23,052
- `(1,7)`: 23,052
- `(1,9)`: 23,052
- `(1,15)`: 23,052
- `(3,5)`: 45,760
- `(3,9)`: 23,052
- `(3,13)`: 45,760
- `(5,9)`: 23,052
- `(7,9)`: 45,760

Total exact coefficient-multiset states after the true sector-stabilizer quotient: **306,450**.

This reduces H227's 11-sector raw coefficient workload `503,360` by another **1.64255x**, and reduces the original H226 36-sector workload `1,647,360` by **5.37562x** before applying any witness envelope rejection.

## Scientific consequence
This is a safe WLOG reduction only. It does not prove universal `n3>=3`. H226's exact coefficient-envelope theorem can now be applied only to these 306,450 quotient states (or equivalently to representatives lifted as needed), then any surviving coefficient state requires globally consistent shift-level screening and exact `n3<=2` separation.

## Files
- `src/loto_research/h228_ordered_sector_stabilizer_coefficient_orbits.py`
- `data/derived/h228_ordered_sector_coefficient_orbits.json`

## Next action
Use the corrected ordered-sector representatives/stabilizers from H228, not H227's unordered stabilizer sizes. Build a representative-only H226 envelope screen over the exact quotient coefficient states. If all are rejected by stored balanced witnesses, the full general cyclic-affine family closes by symmetry; otherwise enumerate legal shift realizations only for survivors and exact-separate them.
