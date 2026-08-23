# H218 — exact H217 shard merge pipeline

## Scope
Lottery-only continuation of the H175 Rhode Island Keno 3-spot hybrid proof search.

## Starting checkpoint
H217 had split the H216 exact necessary-cut screen into 36 independent normalized B/C shards. At the start of H218 no shard result files were present in the repository, so no survivor count could be asserted.

## Work performed
H218 adds a strict merger, `src/loto_research/h218_merge_h217_shards.py`, and upgrades `.github/workflows/h217-bc-shards.yml` so the 36 shard artifacts are automatically downloaded and merged only after every shard succeeds.

The merger refuses partial evidence. It requires shards 0..35, checks `exact_cut_rows=4878`, `A_orbits=3992`, D=0 and per-shard survivor-count consistency, then emits one exact union file:

`data/derived/h218_h217_merged_survivors.json`

The screen size is exactly `36 * 3992 = 143,712` H212 normalized classes against the same 4,878 exact balanced-witness cuts used by H216/H217. Therefore H218 changes observability/completion only; it does not weaken or alter the scientific predicate.

## Result at checkpoint
The merge-enabled workflow was triggered by the workflow-file push. At this checkpoint the merged survivor file is not yet present on `research-work`, so no survivor count or mathematical closure is claimed.

## Proof control
- `survivor_count = 0` would close only the restricted H175 diagonal family against the accumulated exact necessary-cut bank.
- `survivor_count > 0` requires exact `n3<=2` separation on survivors; surviving the cut bank never validates a universal design.
- Missing/failed shards are inconclusive and the merger deliberately aborts instead of publishing a partial count.

## Status
**INCONCLUSIVE / COMPUTATION IN FLIGHT.** No SUCCESS and no EXHAUSTED state.
