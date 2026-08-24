# Super Keno history dataset status

Last updated: 2026-08-24

## Current validated set

- Valid draws: **195**
- Earliest recovered draw: **2022-12-21**
- Latest validated draw: **2026-08-23**
- Structure: `date, official_draw, internal_draw, n1..n20, source, source_url, note`
- Structural validation errors: **0**
- Duplicate dates in accepted set: **0**
- Duplicate 20-number combinations in accepted set: **0**

The recovered baseline contained 150 draws through 2026-06-21. Subsequent collection recovered 44 validated draws covering 2026-07-10 through 2026-08-22, plus **2026-08-23**, for a total of **195** validated draws.

The 2026-08-23 result was recovered from Magayo's 20 ball-image links; each link URL encodes the ball value in query parameter `p2`, yielding: `5,10,11,14,19,28,32,35,36,42,47,48,49,51,53,54,64,65,69,70`.

The 2026-08-21 result remains independently cross-checked against the official Azerlotereya results page: `1,7,12,22,23,28,29,30,31,37,40,41,45,46,47,48,52,53,62,70`, official draw **26345**.

Committed collection blocks:

- `data/super_keno_2026-07-10_2026-07-23.csv`
- `data/super_keno_2026-07-24_2026-08-22.csv`
- `data/super_keno_2026-08-23.csv`

A regenerated local master contains **195 rows** and passes structural validation. The persistent Library master still needs replacement with this regenerated version when Library mutation is available; GitHub preserves all newly collected rows meanwhile.

## Remaining priority gaps

1. **2026-06-22 through 2026-07-09** — contiguous 18-day gap immediately after the baseline.
2. Older historical gaps remain substantial, especially between isolated recovered blocks in 2022–2025 and within early/mid-2026.

## Latest search pass

- Rechecked the live Magayo results page: its currently exposed recent-history text reaches back only to **2026-07-10**, so it does not expose the 18 missing dates.
- Ran targeted web searches for individual dates in the 2026-06-22..2026-07-09 gap across Magayo, Eurooppalotto and Lucky Numbers wording/URLs.
- No complete 20-number result from that gap was found with sufficient provenance in this pass, so **0 rows were added** rather than guessing or accepting unrelated Keno results.

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

Close **2026-06-22 to 2026-07-09** using older cached/localized Eurooppalotto snapshots, archived result pages, or other verifiable historical feeds; then move backward into older gaps. Keep provenance and deduplicate by date, official draw number, and sorted 20-number combination.
