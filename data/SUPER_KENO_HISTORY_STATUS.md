# Super Keno history dataset status

Last updated: 2026-08-24

## Current validated set

- Valid draws: **180**
- Earliest recovered draw: **2022-12-21**
- Latest validated draw: **2026-08-22**
- Structure: `date, official_draw, internal_draw, n1..n20, source, source_url, note`
- Structural validation errors: **0**
- Duplicate dates in accepted set: **0**
- Duplicate 20-number combinations in accepted set: **0**

The recovered baseline contained 150 draws through 2026-06-21. This run added **30 validated draws** covering **2026-07-24 through 2026-08-22** from Magayo. The 2026-08-21 result was independently cross-checked against the official Azerlotereya results page and matched exactly: `1,7,12,22,23,28,29,30,31,37,40,41,45,46,47,48,52,53,62,70`, official draw **26345**.

The newly collected block is committed as:

- `data/super_keno_2026-07-24_2026-08-22.csv`

Working master artifacts for this run were regenerated locally as:

- `super_keno_history_master.csv` — 180 rows
- `super_keno_history_master_180.xlsx` — 180 rows

## Remaining priority gaps

1. **2026-06-22 through 2026-07-23** — contiguous 32-day gap after the previous baseline.
2. **2026-08-23** — Magayo confirms a draw date but renders the 20 numbers as images on the current page; do not ingest until a text/official source confirms the numbers.
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

Focus first on closing **2026-06-22 to 2026-07-23**, then confirm **2026-08-23** from a text/official source, and only then move backward into older gaps. Keep provenance and deduplicate by date, official draw number, and sorted 20-number combination.
