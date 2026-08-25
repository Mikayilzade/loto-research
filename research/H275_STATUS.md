# H275 STATUS — Singapore TOTO cascade/full-cover

Updated: 2026-08-25
Branch: `research-work`
State: **CLOSED / REJECTED for checked strict-guarantee construction**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Checkpoint
H225-X* remains rigorously closed at X20 (0 coefficient survivors / 0 legal shift tuples); no X21/X22 work was created.

H275 opened a genuinely new forced-distribution candidate from the global NEXT ACTION: Singapore Pools TOTO cascade.

Exact result:
- full ordinary space: **13,983,816** six-number selections;
- one-copy full-cover cost: **SGD 13,983,816**;
- fixed G5/G6/G7 full-cover gross: **SGD 3,372,250**;
- duplicate-robust fixed return: **24.1153773762%**;
- fixed-floor deficit: **SGD 10,611,566**.

Structural result:
- any nonempty portfolio has a legal own-Group-1 outcome, so it cannot guarantee the no-G1 condition required for cascade;
- a complete cover always creates Group 1 and therefore suppresses the cascade branch;
- Groups 1–4 are share-based and no hard monopolizable external-share cap was established, so they cannot supply a strict duplicate-robust guaranteed floor.

## Files
- `src/loto_research/h275_singapore_toto_cascade_bound.py`
- `data/derived/h275_singapore_toto_cascade_bound.json`
- `research/h275_singapore_toto_cascade_bound.md`
- `research/H275_VALIDATION.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H275_APPEND.md`

## NEXT ACTION
Do not reopen H225-X* or H275 under unchanged rules. Continue the global search with a different mechanism satisfying at least one of these stronger gates:
1. externally accumulated/promotional money paid as a **fixed amount per winning selection**, not a shareable pool;
2. terminal identifier set that is hard-capped and genuinely player-selectable/reservable before cutoff;
3. finite inventory where complete acquisition itself forces all external reserve/prize liabilities and deterministic cash exceeds full acquisition cost;
4. bonus/subsidy mechanism with an everywhere-positive deterministic value floor that materially exceeds the exact cover hurdle.
