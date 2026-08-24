# H225 EXACT FAMILY STATUS

Updated: 2026-08-24 10:31 +04
Namespace: `H225-X*` (separate from the global numbered lottery H-stream)
Terminal state: **OPEN / NOT CLOSED**

## Authoritative baseline — H235
Full exact augmented rescreen over all **306,450** quotient coefficient states:
- exact shift-surviving coefficient states: **303,802**
- exact surviving legal shift tuples: **90,425,060**
- H225 family closed: **false**

## H225-X1 — COMPLETE
Authoritative alias: `data/derived/h225_x1_exact_separator_summary.json`.
Legacy output label/file is H240 and is retained only for reproducibility.

Result:
- selected actual H235 survivor designs: **44**
- exact unrestricted balanced n3<=2 counterexamples: **44/44**
- inconclusive jobs: **0**
- genuinely new witnesses vs H234: **44**
- all sampled designs broken: **true**

## H225-X2 — COMPUTATION COMPLETE / FULL CERTIFICATE REPUBLISHING
Legacy implementation/output filename: `h241_h240_incremental_exact_rescreen*`.

Authoritative compute run: `32693907822`.
All **44** sector x chunk shard artifacts exist. Merge-only rescue run `32697960407` audited all shards and produced:
- `H225_X2_SHARD_AUDIT_OK 306450`
- `H225_X2_MERGED_OK 295293 65921861`

Authoritative X2 totals:
- quotient coefficient states screened: **306,450 / 306,450**
- exact shift-surviving coefficient states: **295,293**
- exact surviving legal shift tuples: **65,921,861**
- H225 family closed: **false**

Improvement vs H235:
- coefficient states removed: **8,509** (`303,802 -> 295,293`)
- legal shift tuples removed: **24,503,199** (`90,425,060 -> 65,921,861`)

Compact authoritative certificate:
`data/derived/h225_x2_exact_rescreen_summary.json`

Infrastructure note: the legacy full merged path `data/derived/h241_h240_incremental_exact_rescreen.json` is currently an empty placeholder even though the runner-side merged certificate validated successfully. This is a publication defect only; a merge-only republish from the already completed 44 artifacts is in progress. X2 must not be recomputed merely to repair this file.

## H225-X3 — NEXT
One actual shift-level X2 survivor from each still-positive chunk is sent to unrestricted exact balanced n3<=2 separation. Zero-survivor chunks are explicit skips; timeouts/no incumbent are inconclusive, never validation. Returned witnesses are deduplicated against H234 and H225-X1.

Files:
- `src/loto_research/h225_x3_survivor_separation.py`
- `.github/workflows/h225-x3-survivor-separation.yml`
- outputs: `data/derived/h225_x3_survivor_separation.json`, `data/derived/h225_x3_new_witnesses.json`

The previous X2 -> X3 `workflow_dispatch` attempt failed because GitHub resolves workflow-dispatch definitions from the default branch while X3 exists only on `research-work`. X3 will therefore be started by a normal connector/user-token push after the full X2 certificate is republished.

## H225-X4 — PREPARED
Full 44-way incremental exact rescreen after any genuinely new X3 witnesses. Do not run if X3 yields zero new witnesses or X2 unexpectedly closes after certificate audit.

## NEXT ACTION
1. Republish and independently re-read the full X2 merged certificate from the completed 44 shard artifacts.
2. Trigger X3 by user-token push; inspect all active chunks and inconclusive jobs.
3. If X3 yields genuinely new witnesses, run X4 full 44-way rescreen.
4. Continue under H225-X5, X6, ... until exact zero survivors or the family remains demonstrably open.
