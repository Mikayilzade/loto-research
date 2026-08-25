# H225 EXACT FAMILY STATUS

Updated: 2026-08-25 06:25 +04
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
| H225-X11 | — | — | **44/44 broken; 44 new cuts; 0 inconclusive** |
| H225-X12 | **110,487** | **6,180,594** | full 44-way rescreen validated; positive survivors remain |
| H225-X13→X14 | RUNNING | RUNNING | workflow run `32801267776` |

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

## H225-X13 → X14 — LAUNCHED
Because validated X12 remains positive, the next generation was built strictly from the actual X12 artifact and prior immutable witness history.

Implementation:
- `src/loto_research/h225_x13_survivor_separation.py` — commit `14fa389ae1bdd8eb9a9f7fa3b330f07c55a3658c`;
- `src/loto_research/h225_x14_incremental_rescreen.py` — commit `626ec8c8c90741fba1fc0def390167a6aad4b7df`;
- `.github/workflows/h225-x13-x14.yml` — commit `963fcb6f7ba485c95f50112821f4a7944ba686df`;
- trigger `data/derived/h225_x13_trigger.json` — commit `f26eb975f15e11aa5480d2f693e4d0b47e816bbb`.

Workflow run: `32801267776`.
Initial observation after trigger: **queued**.

Strict gates:
1. X13 consumes X12 merged artifact `9545748723` from run `32796246076`, not any repository placeholder.
2. X13 also imports authoritative X11 witness artifact `9544974539` so deduplication/history is complete through X11.
3. X13 is accepted only with `inconclusive_active_jobs == 0` and `counterexamples_found == active_survivor_chunks`.
4. X14 runs only if X13 produces genuinely new cuts.
5. X14 merge requires 44 unique chunks, 11 sectors, exactly **306,450** states, and survivor/shift-tuple sector sums matching top-level totals.
6. Zero X14 exact survivors rigorously closes H225. Positive X14 survivors require X15/X16 from the actual validated X14 packet.

## NEXT ACTION
1. Validate run `32801267776` stage-by-stage.
2. Require zero inconclusive X13 active jobs before accepting X13.
3. If X14 runs, validate 44 shards / 306,450 states and exact sector sums before interpreting survivors.
4. If X14 reaches zero exact survivors, record rigorous H225 closure and stop this lane.
5. If X14 remains positive, prepare H225-X15/X16 only from the actual validated X14 survivor packet.
