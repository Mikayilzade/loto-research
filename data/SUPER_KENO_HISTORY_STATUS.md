# Super Keno history dataset status

Last updated: 2026-08-24

## Recovered baseline

A previously created Super Keno Azerbaijan dataset was recovered from the user's persistent file library.

- Valid draws: **150**
- Earliest recovered draw: **2022-12-21**
- Latest recovered draw in baseline: **2026-06-21**
- Structure: `date, official_draw, internal_draw, n1..n20, source, source_url, note`
- Structural validation: **150/150 OK**
- Duplicate dates: **0**
- Duplicate official draw numbers: **0**
- Duplicate 20-number combinations: **0**

Persistent master files are stored in the user's Library under:

- `/LotoResearch/super_keno_history_master.csv`
- `/LotoResearch/super_keno_history_master.xlsx`

## Validation rule

A draw is accepted only when it contains exactly 20 unique integers in the range 1..70. Conflicting source records must be flagged for review instead of guessed.

## Source priority

1. Azerlotereya official archive/results
2. Eurooppalotto mirrors
3. LotteryGuru
4. Lucky Numbers
5. Magayo
6. Other verifiable archives

## Next action

1. Fill the period after 2026-06-21 through the current date.
2. Identify and fill older gaps in the recovered timeline.
3. Deduplicate by date, official draw number and sorted 20-number combination.
4. Keep source URL/provenance for every row.
5. Sync a repository CSV once the master dataset is materialized for a GitHub write.

An hourly task is active to continue collection and validation.
