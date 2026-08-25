# H225 EXACT FAMILY STATUS

Updated: 2026-08-25 07:30 +04
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
| H225-X14 | **76,196** | **3,807,980** | full 44-way rescreen validated; positive survivors remain |
| H225-X15 | RUNNING | RUNNING | exact separator run `32805383127`; first shard artifacts published |
| H225-X16 | PENDING X15 | PENDING X15 | full rescreen wired behind strict X15 merge gate |

All rescreen stages use the unchanged H228 quotient universe of **306,450** coefficient states. Zero exact survivors is the closure criterion.

## H225-X6 — COMPLETE / VALIDATED
Authoritative run `32784914783`, merged artifact `9541696415`, digest `sha256:76256ba6957894e7562098c1552c783dca26f3095a9954dba2a7edfc42b16635`.

Independent validation: 44 chunk artifacts, 11 sectors, exactly 306,450 states, **210,285** exact survivors and **19,567,210** exact shift tuples.

## H225-X7 → X10 — COMPLETE / VALIDATED
Integrated run `32791403782` completed successfully.
- X7: artifact `9543265692`; 44/44 broken; 0 inconclusive; 44 genuinely new balanced witnesses.
- X8: artifact `9543862728`; 44 shards / 11 sectors / 306,450 states; **170,893 / 12,498,982** survivors/shift tuples.
- X9: artifact `9543925306`; 44/44 broken; 0 inconclusive; 44 genuinely new balanced witnesses.
- X10: artifact `9544543215`; 44 shards / 11 sectors / 306,450 states; **138,871 / 8,845,562** survivors/shift tuples.

## H225-X11 → X12 — COMPLETE / VALIDATED
Authoritative run `32796246076` completed successfully.
- X11 artifact `9544974539`: exactly 44 ordered jobs; 44/44 counterexamples; 0 inconclusive; 44 genuinely new balanced witnesses.
- X12 artifact `9545748723`: 44 shards / 11 sectors / exactly 306,450 states; **110,487** exact survivors and **6,180,594** exact shift tuples.

## H225-X13 — COMPLETE / VALIDATED
Authoritative run `32801267776`, artifact `9546611965`, digest `sha256:d605873ab023f4fbbdc6b4b1c66cde7870f7242c679b4b41e84ac8dc40203315`.

Independent validation: exactly 44 ordered jobs; 44 active survivor chunks; counterexamples **44/44**; inconclusive **0**; 44 unique balanced counterexamples and 44 genuinely new witnesses. Permanent certificate: `research/H225_X13_VALIDATION.md`.

## H225-X14 — COMPLETE / VALIDATED
The same authoritative run `32801267776` later completed successfully. Merged artifact `9547418136`, artifact digest `sha256:1707429da6ec71ad08d7bf04e9c2ee7756490a27d7b4dd5142e1fe1cf9c35316`.

The downloaded merged JSON was independently revalidated outside the workflow:
- packet `H225-X14`, source `H225-X13`;
- exactly **44** unique `(sector, chunk)` shards and exactly **11** sectors;
- sector quotient-state counts sum exactly **306,450** and match the top-level screened total;
- sector survivor counts sum exactly to **76,196**;
- sector legal-shift-tuple counts sum exactly to **3,807,980**;
- closure flag is false.

Permanent certificate: `research/H225_X14_VALIDATION.md`.

Improvement vs X12:
- coefficient states removed: **34,291**;
- legal shift tuples removed: **2,372,614**.

H225 therefore remains open and X15 is mandatory.

## H225-X15 → X16 — LAUNCHED
Implemented:
- `src/loto_research/h225_x15_survivor_separation.py`;
- `src/loto_research/h225_x16_incremental_rescreen.py`;
- `.github/workflows/h225-x15-x16.yml`;
- authenticated source trigger `data/derived/h225_x15_trigger.json` tied to validated X14 run/artifact/digest.

Workflow run `32805383127` was triggered from commit `be63830574a884bd4a2a7a5561f1dd7c505c1c93`. The 44-way X15 matrix is executing and has already produced initial shard artifacts (`h225-x15-j8`, `h225-x15-j35`), confirming the new lane is live rather than merely queued.

Strict gates encoded in CI:
1. X15 must consume the authoritative X14 artifact from run `32801267776` and assert source totals **76,196 / 3,807,980**.
2. X15 merge requires 44 jobs, zero inconclusive active jobs, and every active selected design broken before its witness packet is accepted.
3. X16 runs only if X15 yields nonzero genuinely new cuts.
4. X16 merge requires 44 unique shards / 11 sectors / exactly **306,450** quotient states and exact survivor/shift-tuple sector sums matching top-level totals.
5. X16 zero survivors rigorously closes H225; positive survivors require the next separator generation from actual X16 survivors.

## NEXT ACTION
1. Let run `32805383127` finish X15; do not duplicate/rerun while healthy.
2. Validate the X15 merged artifact: 44 ordered jobs, active chunks, 0 inconclusive, balanced witness validity, and deduplication history through X13.
3. If X15 produces new cuts, validate the automatically launched X16 full rescreen on 44 shards / 11 sectors / exactly 306,450 states and matching sector sums.
4. If X16 survivors are zero, record rigorous H225 closure and stop this lane.
5. If X16 survivors remain positive, continue with H225-X17/X18 only from the actual validated X16 packet.
