# Super Keno history dataset status

Last updated: 2026-08-24

## Current validated set

- Valid draws: **194**
- Earliest recovered draw: **2022-12-21**
- Latest validated draw: **2026-08-22**
- Structure: `date, official_draw, internal_draw, n1..n20, source, source_url, note`
- Structural validation errors: **0**
- Duplicate dates in accepted set: **0**
- Duplicate 20-number combinations in accepted set: **0**

The recovered baseline contained 150 draws through 2026-06-21. The previous collection added 30 validated draws covering 2026-07-24 through 2026-08-22. This run added **14 more validated draws**, covering **2026-07-10 through 2026-07-23**, from Magayo's text results page. Magayo explicitly lists each date and all 20 winning numbers for that interval.

The 2026-08-21 result remains independently cross-checked against the official Azerlotereya results page: `1,7,12,22,23,28,29,30,31,37,40,41,45,46,47,48,52,53,62,70`, official draw **26345**.

Committed collection blocks:

- `data/super_keno_2026-07-10_2026-07-23.csv`
- `data/super_keno_2026-07-24_2026-08-22.csv`

A regenerated local master contains **194 rows** and passes structural validation. The persistent Library master still needs replacement with this regenerated version when Library mutation is available; the GitHub blocks and this status file preserve all newly collected data meanwhile.

## Remaining priority gaps

1. **2026-06-22 through 2026-07-09** — contiguous 18-day gap immediately after the baseline.
2. **2026-08-23** — do not ingest until 20 numbers are confirmed by a text/official source.
3. Older historical gaps remain substantial, especially between isolated recovered blocks in 2022–2025 and within early/mid-2026.

## Validation rule

Accept a draw only when it contains exactly 20 unique integers in the range 1..70. Conflicting source records must be flagged for review rather than guessed.

## Source priority

1. Azerlotereya official archive/results
2. Eurooppalotto mirrors
3. LotteryGuru
4. Lucky Numbers
5. Magayo
6. Other verifiable archives

## Next action

Close **2026-06-22 to 2026-07-09**, then confirm **2026-08-23** from a text/official source, and then move backward into older gaps. Keep provenance and deduplicate by date, official draw number, and sorted 20-number combination.
