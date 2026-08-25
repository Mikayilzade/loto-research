# H225 EXACT FAMILY STATUS

Updated: 2026-08-25 08:26 +04
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
| H225-X12 | 110,487 | 6,180,594 | full 44-way rescreen validated |
| H225-X13 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X14 | 76,196 | 3,807,980 | full 44-way rescreen validated |
| H225-X15 | — | — | **44/44 broken; 44 new cuts; 0 inconclusive** |
| H225-X16 | **48,387** | **2,116,464** | **full 44-way rescreen validated; positive survivors remain** |
| H225-X17 | LAUNCHING | LAUNCHING | exact separator generation wired from authoritative X16 |
| H225-X18 | PENDING X17 | PENDING X17 | full rescreen wired behind strict X17 merge gate |

All rescreen stages use the unchanged H228 quotient universe of **306,450** coefficient states. Zero exact survivors is the closure criterion.

## Earlier validated chain
- X6 authoritative run `32784914783`: **210,285 / 19,567,210**.
- X7→X10 integrated run `32791403782`: X7 44/44, X8 **170,893 / 12,498,982**, X9 44/44, X10 **138,871 / 8,845,562**.
- X11→X12 run `32796246076`: X11 44/44, X12 **110,487 / 6,180,594**.
- X13→X14 run `32801267776`: X13 44/44, X14 **76,196 / 3,807,980**. Certificates: `research/H225_X13_VALIDATION.md`, `research/H225_X14_VALIDATION.md`.

## H225-X15 → X16 — COMPLETE / VALIDATED
Authoritative workflow run `32805383127` completed with conclusion `success`.

### X15
Merged artifact `9548040849`, digest `sha256:af5872c71b5c5c4ac39d7168b89fb4370a9507b5a9a537e4fe4a5aff65126678`.
Independent artifact validation established:
- exactly 44 ordered jobs;
- active chunks 44;
- counterexamples 44/44;
- inconclusive active jobs 0;
- all selected active designs broken;
- 44 unique balanced counterexamples and 44 genuinely new witnesses;
- witness history deduplicated through H225-X13.

### X16
Merged artifact `9548762247`, digest `sha256:16e55597261a820cd00561541cba10e5c1feeee3885b0a81b7520846be1f9d13`.
Independent artifact validation established:
- exactly 44 canonical `(sector, chunk)` shards = 11 sectors × 4 chunks;
- exactly **306,450** quotient coefficient states screened;
- sector quotient-state sums match top level;
- sector survivor sums match **48,387** exact coefficient survivors;
- sector shift-tuple sums match **2,116,464** legal shift tuples;
- X15 supplied 44 raw witnesses / 5,632 affine instances;
- closure flag false.

Improvement vs X14:
- coefficient states removed: **27,809**;
- legal shift tuples removed: **1,691,516**.

Permanent certificate: `research/H225_X15_X16_VALIDATION.md`.

## H225-X17 → X18 — IMPLEMENTED
Added:
- `src/loto_research/h225_x17_survivor_separation.py`;
- `src/loto_research/h225_x18_incremental_rescreen.py`;
- `.github/workflows/h225-x17-x18.yml`.

Strict gates:
1. X17 consumes authoritative X16 merged artifact from run `32805383127` and asserts source totals **48,387 / 2,116,464**.
2. X17 merge requires 44 ordered jobs, zero inconclusive active jobs, and every active selected design broken before witness acceptance.
3. X17 witnesses are deduplicated through H225-X15.
4. X18 runs only if X17 yields nonzero genuinely new cuts.
5. X18 merge requires 44 unique shards / 11 sectors / exactly **306,450** states plus exact sector-sum equality.
6. X18 zero survivors closes H225; positive survivors require H225-X19/X20 from the actual X18 packet.

## NEXT ACTION
1. Trigger and monitor H225-X17/X18 without duplicating a healthy run.
2. Validate X17 merged artifact: 44 ordered jobs, active chunks, `0 inconclusive`, balanced witness validity, deduplication through X15.
3. If X17 yields new cuts, validate X18 full rescreen on 44 shards / 11 sectors / exactly 306,450 states and matching sector sums.
4. If X18 survivors are zero, record rigorous H225 closure and stop this lane.
5. If X18 survivors remain positive, continue with H225-X19/X20 only from the actual validated X18 packet.
