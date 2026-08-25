# H225 EXACT FAMILY STATUS

Updated: 2026-08-25 06:34 +04
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
| H225-X7 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X8 | 170,893 | 12,498,982 | full 44-way rescreen validated |
| H225-X9 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X10 | 138,871 | 8,845,562 | full 44-way rescreen validated |
| H225-X11 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X12 | **110,487** | **6,180,594** | full 44-way rescreen validated; positive survivors remain |
| H225-X13 | — | — | **44/44 broken; 44 new cuts; 0 inconclusive — VALIDATED** |
| H225-X14 | QUEUED | QUEUED | same workflow run `32801267776`; no shard artifact yet |

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
- total chunks 44; active 44; counterexamples **44/44**; inconclusive **0**; genuinely new balanced witnesses **44**.

### H225-X8 rescreen
Artifact `9543862728`, digest `sha256:9b1e04900acd47e369c86e34727e0457b4f7bb145a593a0e7aa9860d39b39c0b`.
- 44 shards / 11 sectors / exactly **306,450** states;
- survivors **170,893**; shift tuples **12,498,982**.

### H225-X9 separator
Artifact `9543925306`, digest `sha256:e87ae780416db24ad9e17cd0d5a7acf6f7e7a8d2972a9f959bb1e78bfa90fe10`.
- total chunks 44; active 44; counterexamples **44/44**; inconclusive **0**; genuinely new balanced witnesses **44**.

### H225-X10 rescreen
Artifact `9544543215`, digest `sha256:761189ceb7afb6e8eaa338932dd18c26cadbf92976620b8ed916cd76cef3f343`.
- 44 shards / 11 sectors / exactly **306,450** states;
- survivors **138,871**; shift tuples **8,845,562**.

The repository copy of a large merged rescreen JSON can appear empty through the connector. Artifact contents and independent sum checks are authoritative; never infer zero from an empty placeholder.

## H225-X11 → X12 — COMPLETE / VALIDATED
Authoritative workflow run `32796246076` completed successfully.

### H225-X11 separator
Merged artifact `9544974539`, digest `sha256:e498398c388046f018ef819addd1722a0c8a88687af4fa899357a34f7540510d`.
Independent artifact validation:
- packet `H225-X11`;
- exactly 44 ordered jobs (IDs 0..43);
- active survivor chunks **44**;
- counterexamples found **44/44**;
- inconclusive active jobs **0**;
- `all_selected_active_designs_broken == true`;
- witness packet contains exactly **44 genuinely new balanced witnesses**.

### H225-X12 rescreen
Merged artifact `9545748723`, digest `sha256:80fdcf201311903174a3b217b9059827f9a5eba0e26f5ab115afdb25f2820ac1`.
Independent artifact validation:
- packet `H225-X12`;
- `chunk_shards == 44`;
- exactly 11 sectors and 44 unique embedded chunks;
- sector quotient-state counts sum exactly **306,450** and equal top-level total;
- exact survivor states sector sum/top-level = **110,487**;
- exact shift tuples sector sum/top-level = **6,180,594**;
- closure flag is false because survivors remain.

Improvement vs X10:
- coefficient states removed: **28,384**;
- legal shift tuples removed: **2,664,968**.

## H225-X13 — COMPLETE / VALIDATED
Authoritative workflow run `32801267776`; merged artifact `9546611965`, digest `sha256:d605873ab023f4fbbdc6b4b1c66cde7870f7242c679b4b41e84ac8dc40203315`.

Independent merged-artifact validation:
- packet `H225-X13`, source packet `H225-X12`, source run `32796246076`;
- source X12 survivor totals exactly **110,487 coefficient states / 6,180,594 legal shift tuples**;
- exactly 44 ordered jobs (IDs `0..43`);
- active survivor chunks **44**;
- counterexamples found **44/44**;
- inconclusive active jobs **0**;
- unique balanced counterexamples **44**;
- genuinely new witnesses **44** after deduplication through X11 history;
- `all_selected_active_designs_broken == true`.

Permanent independent certificate: `research/H225_X13_VALIDATION.md`.

This rigorously passes the X13 separator gate but does **not** close H225. A full X14 rescreen remains mandatory.

## H225-X14 — WAITING FOR RUNNER / NO RESULT CLAIM
The integrated run `32801267776` currently reports workflow status **queued** after publishing all 44 X13 shard artifacts and the merged X13 artifact. At the latest artifact check there were **no X14 shard or merged artifacts yet**. Therefore no X14 survivor count is inferred or claimed.

Strict X14 gate:
1. consume the actual validated X13 witness packet;
2. require 44 unique chunk shards and exactly 11 sectors;
3. require sector quotient-state counts to sum exactly **306,450** and equal top-level total;
4. require survivor-state and legal-shift-tuple sector sums to equal top-level totals;
5. zero X14 exact survivors rigorously closes H225; positive survivors require X15/X16 from the actual validated X14 packet.

## NEXT ACTION
1. Recheck run `32801267776` for X14 execution/artifacts; do not rerun while it is merely queued.
2. If X14 fails, inspect the failing job/log and repair only the concrete CI fault before retrying.
3. If X14 completes, validate 44 shards / 11 sectors / exactly **306,450** states plus survivor and shift-tuple sector sums before interpreting the result.
4. If X14 reaches zero exact survivors, record rigorous H225 closure and stop this lane.
5. If X14 remains positive, prepare H225-X15/X16 only from the actual validated X14 survivor packet.
