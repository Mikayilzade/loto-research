# H225 EXACT FAMILY STATUS

Updated: 2026-08-25 09:35 +04
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
| H225-X15 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X16 | 48,387 | 2,116,464 | full 44-way rescreen validated |
| H225-X17 | — | — | **44/44 broken; 44 new cuts; 0 inconclusive** |
| H225-X18 | **3,300** | **71,392** | **full 44-way rescreen validated; positive survivors remain** |
| H225-X19 | LAUNCHING | LAUNCHING | exact separators implemented from authoritative X18 |
| H225-X20 | PENDING X19 | PENDING X19 | full rescreen wired behind strict X19 merge gate |

All rescreen stages use the unchanged H228 quotient universe of **306,450** coefficient states. Zero exact survivors is the closure criterion.

## Validated chain
- X6 run `32784914783`: **210,285 / 19,567,210**.
- X7→X10 run `32791403782`: X7 44/44; X8 **170,893 / 12,498,982**; X9 44/44; X10 **138,871 / 8,845,562**.
- X11→X12 run `32796246076`: X11 44/44; X12 **110,487 / 6,180,594**.
- X13→X14 run `32801267776`: X13 44/44; X14 **76,196 / 3,807,980**.
- X15→X16 run `32805383127`: X15 44/44; X16 **48,387 / 2,116,464**.
- X17→X18 run `32809156175`: X17 44/44; X18 **3,300 / 71,392**.

Permanent certificates include `research/H225_X15_X16_VALIDATION.md` and `research/H225_X17_X18_VALIDATION.md`.

## H225-X17 → X18 — COMPLETE / VALIDATED
Authoritative workflow run `32809156175` completed with conclusion `success`.

### X17
Merged artifact `9549487377`, digest `sha256:0279a59e00f7111475fa1b5d9242bc4c0fbc138c065afbea8376e5e83d41d230`.
Independent artifact validation established:
- exactly 44 ordered jobs;
- active chunks 44;
- counterexamples 44/44;
- inconclusive active jobs 0;
- all selected active designs broken;
- 44 genuinely new balanced witnesses;
- witness history deduplicated through H225-X15.

### X18
Merged artifact `9550091411`, digest `sha256:147b9b9a5e7ee1dc43ed9c37db84cd85edc7caaee7acbbe381923e4214207892`.
Independent artifact validation established:
- exactly 44 canonical `(sector, chunk)` shards = 11 sectors × 4 chunks;
- exactly **306,450** quotient coefficient states screened;
- sector quotient-state sums match top level;
- sector survivor sums match **3,300** exact coefficient survivors;
- sector shift-tuple sums match **71,392** legal shift tuples;
- X17 supplied 44 raw witnesses / 5,632 affine instances;
- closure flag false.

Improvement vs X16:
- coefficient states removed: **45,087**;
- legal shift tuples removed: **2,045,072**.

## H225-X19 → X20 — IMPLEMENTED
Added:
- `src/loto_research/h225_x19_survivor_separation.py`;
- `src/loto_research/h225_x20_incremental_rescreen.py`;
- `.github/workflows/h225-x19-x20.yml`.

Strict gates:
1. X19 consumes authoritative X18 merged artifact from run `32809156175` and asserts source totals **3,300 / 71,392**.
2. X19 merge requires 44 ordered jobs, zero inconclusive active jobs, and every active selected design broken before witness acceptance.
3. X19 witnesses are deduplicated through H225-X17.
4. X20 runs only if X19 yields nonzero genuinely new cuts.
5. X20 merge requires 44 unique shards / 11 sectors / exactly **306,450** states plus exact sector-sum equality.
6. X20 zero survivors closes H225; positive survivors require H225-X21/X22 from the actual X20 packet.

## NEXT ACTION
1. Trigger and monitor H225-X19/X20 without duplicating a healthy run.
2. Validate X19 merged artifact: 44 ordered jobs, active chunks, `0 inconclusive`, balanced witness validity, deduplication through X17.
3. If X19 yields new cuts, validate X20 full rescreen on 44 shards / 11 sectors / exactly 306,450 states and matching sector sums.
4. If X20 survivors are zero, record rigorous H225 closure and stop this lane.
5. If X20 survivors remain positive, continue with H225-X21/X22 only from the actual validated X20 packet.
