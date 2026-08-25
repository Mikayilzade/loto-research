# H225 EXACT FAMILY STATUS

Updated: 2026-08-25 05:07 +04
Namespace: `H225-X*` (separate from the global numbered lottery H-stream)
Terminal state: **OPEN / NOT CLOSED**

## Authoritative progression

| Stage | coefficient survivors | legal shift tuples | separator result |
|---|---:|---:|---|
| H235 baseline | 303,802 | 90,425,060 | — |
| H225-X1 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X2 | 295,293 | 65,921,861 | — |
| H225-X3 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X4 | 288,176 | 50,626,368 | — |
| H225-X5 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X6 | 210,285 | 19,567,210 | full 44-way rescreen validated |
| H225-X7 | — | — | **44/44 broken; 44 new cuts; 0 inconclusive** |
| H225-X8 | **170,893** | **12,498,982** | full 44-way rescreen validated |
| H225-X9 | — | — | **44/44 broken; 44 new cuts; 0 inconclusive** |
| H225-X10 | **138,871** | **8,845,562** | full 44-way rescreen validated; positive survivors remain |
| H225-X11→X12 | RUNNING | RUNNING | workflow run `32796246076` |

All rescreen stages use the unchanged H228 quotient universe of **306,450** coefficient states. Zero exact survivors is the closure criterion.

## H225-X6 — COMPLETE / VALIDATED
Authoritative run `32784914783`, merged artifact `9541696415`, digest `sha256:76256ba6957894e7562098c1552c783dca26f3095a9954dba2a7edfc42b16635`.

Independent validation:
- 44 chunk artifacts + merged artifact;
- exactly 306,450 states;
- 11 sectors;
- exact survivors **210,285**;
- exact shift tuples **19,567,210**.

## H225-X7 → X10 — COMPLETE / VALIDATED
Integrated run `32791403782` completed with conclusion **success**.

### H225-X7 separator
Artifact `9543265692`, digest `sha256:0a4dc992bf93e98ceeac2516e18b80c67c703afe224a74884aca1c43403244d2`.
- total chunks: 44;
- active survivor chunks: 44;
- skipped-zero-survivor chunks: 0;
- counterexamples found: **44/44**;
- inconclusive active jobs: **0**;
- genuinely new balanced witnesses: **44**;
- all selected active designs broken: true.

### H225-X8 rescreen
Artifact `9543862728`, digest `sha256:9b1e04900acd47e369c86e34727e0457b4f7bb145a593a0e7aa9860d39b39c0b`.
Independent merged-artifact validation:
- `chunk_shards == 44`;
- exactly **11** sectors and **44** embedded chunks;
- sector quotient-state counts sum exactly **306,450**;
- exact survivor states sum/top-level = **170,893**;
- exact shift tuples sum/top-level = **12,498,982**.

Improvement vs X6:
- coefficient states removed: **39,392**;
- legal shift tuples removed: **7,068,228**.

### H225-X9 separator
Artifact `9543925306`, digest `sha256:e87ae780416db24ad9e17cd0d5a7acf6f7e7a8d2972a9f959bb1e78bfa90fe10`.
- total chunks: 44;
- active survivor chunks: 44;
- skipped-zero-survivor chunks: 0;
- counterexamples found: **44/44**;
- inconclusive active jobs: **0**;
- genuinely new balanced witnesses: **44**;
- all selected active designs broken: true.

### H225-X10 rescreen
Artifact `9544543215`, digest `sha256:761189ceb7afb6e8eaa338932dd18c26cadbf92976620b8ed916cd76cef3f343`.
Independent merged-artifact validation:
- packet `H225-X10`;
- `chunk_shards == 44`;
- exactly **11** sectors and **44** embedded chunks;
- sector quotient-state counts sum exactly **306,450**;
- exact survivor states sum/top-level = **138,871**;
- exact shift tuples sum/top-level = **8,845,562**;
- family closure flag is false because survivors remain.

Improvement vs X8:
- coefficient states removed: **32,022**;
- legal shift tuples removed: **3,653,420**.

The repository copy of a large merged rescreen JSON can appear empty through the connector. Artifact contents and the above independent sum checks are authoritative; never infer zero from an empty placeholder.

## H225-X11 → X12 — LAUNCHED
Because validated X10 remains positive, the next exact cutting-plane generation was implemented and triggered.

Implementation:
- `src/loto_research/h225_x11_survivor_separation.py` — commit `4da0376fd456287f6589cb6fe8281f6030f77a59`;
- `src/loto_research/h225_x12_incremental_rescreen.py` — commit `0bb88c3f85340e9eac0a3db6ea6dc6a76f50e19a`;
- `.github/workflows/h225-x11-x12.yml` — commit `665a01b85f03e0c8220e2cf81977033e42d8c951`;
- trigger `data/derived/h225_x11_trigger.json` — commit `449521551d60140c884ab9a719133746121d9928`.

Workflow run: `32796246076`.
Observed immediately after trigger: **queued**.

Strict gates:
1. X11 consumes the authoritative X10 merged artifact from run `32791403782`, not the repository placeholder.
2. X11 accepts a witness packet only with `inconclusive_active_jobs == 0` and `counterexamples_found == active_survivor_chunks`.
3. X12 runs only if X11 has genuinely new cuts.
4. X12 merge requires 44 unique chunks, 11 sectors and exactly **306,450** states; survivor and shift-tuple sector sums must equal top-level totals.
5. Zero X12 exact survivors rigorously closes H225. Positive X12 survivors require X13/X14, built only from the actual X12 packet.

## NEXT ACTION
1. Validate run `32796246076` stage-by-stage.
2. Require zero inconclusive X11 active jobs before accepting X11.
3. If X12 runs, validate 44 shards / 306,450 states and exact sector sums before interpreting survivors.
4. If X12 reaches zero exact survivors, record rigorous H225 closure and stop this lane.
5. If X12 remains positive, prepare H225-X13/X14 only from the actual validated X12 survivor packet.
