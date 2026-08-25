# H270 VALIDATION — ONCE 11/11 rollover-funding screen

Validated: 2026-08-25
Result: **PASS — mechanism rejected; no guaranteed-profit strategy found**

## Rule validation

Primary source: BOE-A-2026-9945 (7 May 2026).

Checks:
- 2026 draw date = 11 November 2026;
- sale start = 21 September 2026;
- coupon price = EUR 6;
- category 1 fixed prize = EUR 11,000,000;
- category 2 = eleven fixed EUR 1,000,000 prizes;
- paragraph 3.4 allows up to EUR 11,000,000 **of those already-defined awards** to be sourced from prior unsold prizes;
- paragraph 3.4 does not increase category 1 or category 2 prize amounts;
- paragraph 3.5 moves unsold current top prizes onward to later eligible draws, again confirming a funding-transfer mechanism.

Primary source URL: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-9945

## Arithmetic validation

Historical calibration only: official 2024 and 2025 11/11 emissions both used 120 series x 100,000 numbers x EUR 6 = EUR 72,000,000.

For 120 series, collision-free category upper bound:
- C1 = 11,000,000
- C2 = 11,000,000
- C3 = 119 x 50,000 = 5,950,000
- C4 = 11 x 119 x 2,000 = 2,618,000
- C5 = 9 x 120 x 1,200 = 1,296,000
- C6 = 90 x 120 x 120 = 1,296,000
- C7 = 900 x 120 x 12 = 1,296,000
- C8 = 9,000 x 120 x 6 = 6,480,000
- total = **EUR 40,936,000**
- total / EUR 72,000,000 = **56.8555555556%**

If the maximum EUR 11m is funded from prior unsold prizes:
- player-facing scheduled gross remains **EUR 40,936,000**;
- current-emission-funded component becomes **EUR 29,936,000**;
- EUR 29,936,000 / EUR 72,000,000 = **41.5777777778%**;
- additive player subsidy = **EUR 0**.

This is consistent with the official 2025 ONCE certificate describing a 41.6%–56.9% range depending on whether up to EUR 11m of the fixed top awards is funded from prior draws.

## Conservative direction

The reconstruction ignores possible overlap of non-accumulable lower categories across repeated complete extractions. Ignoring such collisions can only increase the reconstructed payout, so it is a player-favourable upper bound. The rejection therefore does not depend on undercounting lower prizes.

## Scope

H270 closes only the hypothesis that the ONCE 11/11 prior-unsold-prize clause is an **additive external subsidy** capable of lifting a complete-identifier takeover. It is not additive under the checked 2026 rule.

H225-X* remains untouched and rigorously CLOSED / EXHAUSTED at X20.
