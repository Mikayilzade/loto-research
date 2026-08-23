# H222 — single-process exact H175 cut-bank screen

## Scope
Lottery-only continuation of the Rhode Island Keno H175 restricted-family proof search.

## Why this packet exists
H219 is scientifically exact but repeats H212's expensive 128-map orbit enumeration independently in each of 36 B/C jobs. Its merged output had still not appeared through H221.

H222 preserves the exact same finite predicate while removing that repeated setup cost. It computes:
- the 4,878 exact H185+H186 witness rows once;
- all 3,992 H212 A-orbit representatives once;
- the exact `4878 x 3992` A-incidence matrix once;
- then all 36 normalized B/C classes in one process.

Thus it screens the same `36 * 3992 = 143,712` H212-normalized restricted classes. Candidate survival still means incidence `>=3` on every stored witness. Zero survivors has the H221 certificate meaning: the entire H212-covered restricted diagonal family is impossible. Positive survivors remain only cut-bank survivors and still require exact `n3<=2` separation.

## Files
- `src/loto_research/h222_single_process_vectorized_screen.py`
- `.github/workflows/h222-single-process-screen.yml`
- target output `data/derived/h222_single_process_survivors.json`

## Current result
At packet creation the target output is pending. No mathematical closure or universal H175 validation is claimed until the schema-valid result file exists.

Status: **INCONCLUSIVE — exact H222 result pending**.
