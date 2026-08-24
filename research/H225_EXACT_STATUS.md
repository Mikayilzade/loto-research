# H225 EXACT FAMILY STATUS

Updated: 2026-08-25 01:31 +04
Namespace: `H225-X*` (separate from the global numbered lottery H-stream)
Terminal state: **OPEN / NOT CLOSED**

## Authoritative progression

| Stage | coefficient survivors | legal shift tuples | separator result |
|---|---:|---:|---|
| H235 baseline | 303,802 | 90,425,060 | — |
| H225-X1 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X2 | 295,293 | 65,921,861 | — |
| H225-X3 | — | — | 44/44 broken; 44 new cuts; 0 inconclusive |
| H225-X4 | **288,176** | **50,626,368** | — |
| H225-X5 | — | — | **44/44 broken; 44 new cuts; 0 inconclusive** |
| H225-X6 | RETRIGGERED | RETRIGGERED | full 44-way rescreen V2 triggered |

All rescreen stages use the unchanged H228 quotient universe of **306,450** coefficient states. Zero exact survivors is the closure criterion.

## H225-X2 certificate
Authoritative compute run: `32693907822`; all 44 shard artifacts exist and were independently reconstructed.

Totals:
- states screened: **306,450 / 306,450**
- exact shift-surviving coefficient states: **295,293**
- exact surviving legal shift tuples: **65,921,861**

Compact certificate: `data/derived/h225_x2_exact_rescreen_summary.json`.
Survivor seed: `data/derived/h225_x2_survivor_seed.json`.
Full independently reconstructed merge SHA-256: `bd61f2fa7c3b5edaf4e793cdd9d33881fdb6d69cb6eb8badae47be5372d83e35`.

## H225-X3 — COMPLETE
- active chunks: **44/44**
- unrestricted exact balanced `n3<=2` counterexamples: **44/44**
- inconclusive: **0**
- unique balanced counterexamples: **44**
- genuinely new witnesses vs H234 + X1: **44**

Files:
- `data/derived/h225_x3_survivor_separation.json`
- `data/derived/h225_x3_new_witnesses.json`

## H225-X4 — COMPLETE
Full 44-way exact rescreen after affine-expanding the 44 X3 cuts through 128 symmetries.

Authoritative commit: `4778806680740aa6f01b2e6c0a61957b7061b06a` (`H225-X4 publish full incremental exact rescreen`).

Result:
- states screened: **306,450 / 306,450**
- exact shift-surviving coefficient states: **288,176**
- exact surviving legal shift tuples: **50,626,368**
- X3 raw new witnesses: **44**
- X3 affine instances: **5,632**
- H225 family closed: **false**

Improvement vs X2:
- coefficient states removed: **7,117**
- legal shift tuples removed: **15,295,493**

Note: connector `fetch_file` can show a very large merged JSON as empty; do not infer zero survivors from empty connector content alone. Validate by artifact/commit or independent shard reconstruction.

## H225-X5 — COMPLETE
Integrated run: `32707295388`.
Latest validated merged artifact: `9513550747`, digest `sha256:a94bde0d61f002d5496f2bc728854d10cace901b2ab8fcbd354ac552944e2d30`.

Result:
- active X4 survivor chunks: **44/44**
- exact unrestricted counterexamples: **44/44**
- inconclusive: **0**
- unique balanced counterexamples: **44**
- genuinely new witnesses vs H234/X1/X3: **44**
- all selected active designs broken: **true**

Files:
- `data/derived/h225_x5_survivor_separation.json`
- `data/derived/h225_x5_new_witnesses.json`

## H225-X6 — RETRIGGERED / RESULT NOT YET VALIDATED
X6 reconstructs the witness universe from immutable generations H226 + H234 + X1 + X3 + X5, affine-expanding all added cuts, then rescreens all **306,450** quotient states in **44 exact chunks**.

Original human-token trigger:
- `data/derived/h225_x6_trigger.json`
- trigger commit `a50321e30f2b9b28e712f8b2c6ee691516f039d8`

The previous checkpoint remained without a validated merged result far beyond the workflow's own 45-minute per-chunk timeout window. At 2026-08-25 01:28 +04 the same computation was retriggered via human-token push; workflow concurrency cancels any stale predecessor.

Authoritative retrigger:
- packet: `H225-X6-TRIGGER-V2`
- commit: `c7189841a7e1e0154f167be064cf1c6c4c810f46`

Expected merged output:
- `data/derived/h225_x6_incremental_exact_rescreen.json`

A zero-byte placeholder proves neither completion nor zero survivors. Do not infer a mathematical result until merged output/artifacts are validated.

## Downstream — PREPARED AS ONE INTEGRATED CHAIN
A single authenticated X7 trigger can continue multiple cutting-plane generations inside one GitHub Actions run, avoiding suppressed CI->push->CI recursion:

1. **H225-X7** — 44 unrestricted exact separators over actual positive X6 chunks; zero-survivor chunks are explicit skips; witnesses deduplicated against H234/X1/X3/X5.
2. **H225-X8** — full 44-way / 306,450-state exact rescreen after affine-expanding genuinely new X7 cuts.
3. **H225-X9** — 44 unrestricted exact separators over actual positive X8 chunks; witnesses deduplicated against H234/X1/X3/X5/X7.
4. **H225-X10** — full 44-way / 306,450-state exact rescreen after genuinely new X9 cuts.

Implemented files:
- `src/loto_research/h225_x7_survivor_separation.py`
- `src/loto_research/h225_x8_incremental_rescreen.py`
- `src/loto_research/h225_x9_survivor_separation.py`
- `src/loto_research/h225_x10_incremental_rescreen.py`
- `.github/workflows/h225-x7-survivor-separation.yml` — integrated X7 -> X8 -> X9 -> X10 artifact chain

Integrated-chain commit: `856d67c03357ba9a22df9068901838c611c61290`.

The chain has strict stop gates:
- X8 runs only if X7 produced genuinely new cuts;
- X9 runs only if X8 still has positive exact survivors;
- X10 runs only if X9 produced genuinely new cuts;
- every rescreen merge asserts 44 shards and 306,450 states.

## NEXT ACTION
1. Validate H225-X6 V2 merged output/artifacts when present; an empty placeholder proves nothing.
2. If X6 reaches zero exact survivors, record rigorous H225 closure and stop this family lane.
3. If X6 remains positive, create authenticated `data/derived/h225_x7_trigger.json`. The integrated X7->X10 chain then proceeds automatically through valid nonterminal gates.
4. If X10 still has positive survivors, continue H225-X11/X12 only after validating X10; never launch speculative separator stages against missing/empty merged inputs.
