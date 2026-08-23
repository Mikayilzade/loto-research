# H226 — exact coefficient-envelope pre-screen for the H225 general cyclic-affine family

Date: 2026-08-23
Status: computation launched; no SUCCESS claim

## Scope
Lottery-only continuation of H175. H224 restricted-family output is still absent, so H226 advances the larger H225 general cyclic-affine branch instead of spending another packet on equivalent restricted-screen plumbing.

## New theorem
After H225 normalization, B, C and D are fixed within one of 36 normalized coefficient sectors:
- B=(1,beta,0),
- C=(1,gamma,0),
- D=(1,1,0), beta<=gamma.

The three A layers are general `z=a*x+b*y+c (mod16)` layers. There are 64 possible coefficient pairs `(a,b)` and 16 shifts per pair.

Ignore A shifts temporarily and fix only the multiset of the three A coefficient pairs. For every exact balanced witness, maximize A incidence over all legal distinct shifts compatible with that multiset:
- three distinct coefficient blocks: use the best shift in each block;
- multiplicity 2+1: use the two best distinct shifts in the repeated block plus the best shift in the other block;
- multiplicity 3: use the three best distinct shifts in that block.

If this optimistic maximum plus the fixed B/C/D incidence is below 3 on even one balanced witness, then **every** actual shift realization of that coefficient multiset has `n3<=2` on that witness and is impossible.

This is an exact necessary-condition theorem, not a heuristic bound. It respects the distinct-layer requirement even when coefficient pairs repeat.

## Search-space consequence
The H225 general family has 36,243,104 exact symmetry classes, but only `C(64+3-1,3)=45,760` A coefficient multisets per B/C sector. H226 therefore inserts a cheap mathematically safe layer before shift-level orbit enumeration: entire coefficient-pattern sectors can be deleted at once using the existing balanced-witness bank.

## General witness signatures
The old 4,878-row count was deduplicated under the restricted diagonal parameterization. H226 correctly recomputes/deduplicates the witness signatures under the full general A/B/C incidence data rather than assuming the old 4,878 count remains sufficient after enlarging the layer family. Thus no information is lost merely because two witnesses happened to be identical for `a=b` layers.

## Implementation
`src/loto_research/h226_general_coefficient_envelope_prescreen.py`:
1. rebuilds H185/H186 exact balanced witnesses and their safe affine images;
2. computes full general A incidence for all 64 coefficient blocks × 16 shifts;
3. computes normalized B/C/D incidences for all 8 odd beta/gamma values;
4. exact-deduplicates by the complete general signature;
5. evaluates all 45,760 coefficient multisets against all 36 B/C sectors with the distinct-shift rowwise upper bound;
6. outputs survivor counts and sample coefficient patterns for the next exact shift-level stage.

Target output: `data/derived/h226_general_coefficient_envelope.json`.

## Interpretation
A rejected H226 coefficient pattern is rigorously closed within the H225 normalized general family by an explicit stored balanced witness. A surviving pattern is not validated; it merely remains capable of reaching incidence >=3 on each stored witness under rowwise potentially different best shifts. It must next undergo exact globally consistent shift selection and finally exact `n3<=2` separation.

## Next action
Use H226 output to enumerate only surviving coefficient-pattern sectors, then apply H225 residual symmetry to their shift assignments and exact cut-bank screening. If H224 later returns zero restricted survivors, record restricted-family closure independently under H221.
