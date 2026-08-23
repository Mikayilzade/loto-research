# H223 — streaming exact H175 restricted-family screen

Date: 2026-08-23
Status: INCONCLUSIVE / exact computation launched

## Why this packet is larger
H222's result remained absent, so this packet does more than another output check. It audits the scientific predicate, creates a third implementation with a different memory/execution shape, and hardens the CI write path.

## Exact predicate
For each of the 143,712 H212-normalized restricted designs, test all 4,878 stored exact balanced witness rows. A candidate survives the cut bank iff total selected-layer incidence is at least 3 for every row.

This is the same exact finite predicate as H219/H222. No sampling, heuristic, relaxed threshold, or new symmetry assumption is introduced.

## Independent execution shape
H223:
- rebuilds the 4,878 exact active rows once;
- enumerates the exact 3,992 H212 A-orbit representatives once;
- computes the A-incidence matrix once;
- checks each of the 36 normalized B/C classes;
- evaluates A candidates in blocks of 256 rather than one monolithic comparison;
- writes `data/derived/h223_streaming_survivors.json` only after all 143,712 classes are screened.

The block decomposition is logically exact because each candidate column is tested against the same complete set of 4,878 rows independently.

## CI hardening
Unlike H222, the result commit step performs `git pull --rebase origin research-work` before push. This removes one plausible non-scientific failure mode when other research commits advance the branch while the long screen is running.

The workflow timeout is raised to 120 minutes. Missing output or timeout remains inconclusive and is never interpreted as zero survivors.

## Interpretation
- `survivor_count = 0` with schema/count validation closes the H212-covered restricted diagonal family under H221.
- Positive survivors are only cut-bank survivors and require exact `n3<=2` separation.
- Missing output proves nothing.

## Next action
Check H223 first, while also accepting a late schema-valid H222/H219 result. If zero, close the restricted family and move immediately to the general cyclic-affine family. If positive, separate only survivors exactly.
