# H225 EXACT FAMILY STATUS

Updated: 2026-08-24 11:58 +04
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

## H225-X2 — COMPLETE / CERTIFICATE REPUBLISHED
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

Authoritative survivor seed:
`data/derived/h225_x2_survivor_seed.json`

The previous empty legacy path `data/derived/h241_h240_incremental_exact_rescreen.json` has now been replaced by an audited publication manifest carrying the validated totals, validation markers, compact-certificate pointers and SHA-256 of the runner-side full merge. X2 must not be recomputed.

## H225-X3 — COMPLETE
X3 took one actual shift-level X2 survivor from each of the **44 active chunks** and ran unrestricted exact balanced `n3<=2` separation.

Result:
- active survivor chunks: **44 / 44**
- exact counterexamples found: **44 / 44**
- inconclusive active jobs: **0**
- unique balanced counterexamples: **44**
- genuinely new witnesses after deduplication against H234 and H225-X1: **44**
- all selected active designs broken: **true**

Files:
- `data/derived/h225_x3_survivor_separation.json`
- `data/derived/h225_x3_new_witnesses.json`
- `src/loto_research/h225_x3_survivor_separation.py`

Interpretation: X2 still has a large exact survivor set, but every sampled active chunk again yielded a genuinely new unrestricted exact separator. This justifies another full incremental rescreen; it does **not** itself close the family.

## H225-X4 — TRIGGERED
X4 is the full 44-way incremental exact rescreen after adding the 44 genuinely new X3 witnesses.

The workflow accepts a `research-work` push trigger on `data/derived/h225_x4_trigger.json`, avoiding the default-branch `workflow_dispatch` resolution problem. Trigger commit was created after X3 publication.

Expected output:
- `data/derived/h225_x4_incremental_exact_rescreen.json`

No X4 result is inferred until that merged output is present and independently read.

## Downstream continuation — PREPARED / DORMANT
To avoid another orchestration delay, the next two stages are already implemented but **must not be triggered speculatively**:

- **H225-X5**: unrestricted exact separator over one actual survivor from every still-positive X4 chunk, with explicit zero-survivor skips and deduplication against H234, H225-X1 and H225-X3.
  - `src/loto_research/h225_x5_survivor_separation.py`
  - `.github/workflows/h225-x5-survivor-separation.yml`
- **H225-X6**: full 44-way / 306,450-state incremental exact rescreen after genuinely new X5 cuts, adding all X5 witnesses through the same 128 affine symmetries.
  - `src/loto_research/h225_x6_incremental_exact_rescreen.py`
  - `.github/workflows/h225-x6-incremental-rescreen.yml`

Neither X5 nor X6 has a trigger file at this checkpoint. Positive X4 survivors are required before X5 is triggered; genuinely new X5 witnesses are required before X6 is triggered.

## NEXT ACTION
1. Read and validate `data/derived/h225_x4_incremental_exact_rescreen.json` when present; missing output proves nothing.
2. If X4 reaches exact zero survivors, record H225 family closure and do **not** run X5/X6.
3. If X4 leaves survivors, create the authenticated `data/derived/h225_x5_trigger.json` and run X5.
4. Only if X5 returns genuinely new witnesses, create `data/derived/h225_x6_trigger.json` and run the next full exact rescreen.
5. Continue the cutting-plane cycle until exact zero survivors or a rigorously documented open-family blocker.
