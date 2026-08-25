# H270 STATUS

Updated: 2026-08-25
Terminal state for packet: **CLOSED / REJECTED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Result

The 2026 ONCE 11/11 rules were screened because they appear to contain an external subsidy: up to EUR 11m of top-prize money may come from unsold prizes in earlier draws.

The mechanism is not additive. Category 1 is already fixed at EUR 11m and category 2 at eleven EUR 1m prizes; paragraph 3.4 only permits up to EUR 11m **of those stated amounts** to be funded from prior unsold prizes. It does not raise the winner-facing prize schedule.

Therefore the deterministic additive subsidy available to a full-identifier takeover is **EUR 0**.

Historical calibration using the official 120-series 2024/2025 structure reproduces a collision-free schedule upper bound of **EUR 40.936m** against **EUR 72m** issuance cost = **56.8556%**. If the full EUR 11m is sourced from prior unsold prizes, player payout is still EUR 40.936m; only the current-emission-funded component falls to EUR 29.936m = **41.5778%** of issuance.

The exact 2026 Q4 series count was not assumed because it was not found in currently published material as of this check; that uncertainty does not affect the semantic closure of the additive-rollover hypothesis.

## Validation

- primary current source: BOE-A-2026-9945, published 7 May 2026;
- sale start: 21 Sep 2026;
- draw: 11 Nov 2026;
- coupon price: EUR 6;
- prior-unsold funding cap: EUR 11m;
- additive prize increment under paragraph 3.4: EUR 0;
- lower-category historical reconstruction is deliberately an upper bound because non-top prizes are non-accumulable.

Files:
- `research/h270_once_1111_rollover_funding_bound.md`
- `research/H270_VALIDATION.md`
- `src/loto_research/h270_once_1111_rollover_funding_bound.py`
- `data/derived/h270_once_1111_rollover_funding_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H270_APPEND.md`

## NEXT ACTION

Continue outside the closed H225 family. Prioritize a rule where prior-draw money or promotional funding **increases the actual winner-facing payout above the base schedule**, or a hard-capped/reservable finite identifier pool whose guaranteed total prizes can exceed complete acquisition cost. Do not mistake prize-funding-source transfers for additive subsidies.
