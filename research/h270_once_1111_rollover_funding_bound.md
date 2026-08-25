# H270 — ONCE 11/11 prior-unsold-prize funding screen

Date checked: 2026-08-25
Packet state: **CLOSED / REJECTED for additive rollover subsidy**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Why this mechanism was checked

The global NEXT ACTION asks for a hard-capped/reservable identifier pool or a genuinely external deterministic subsidy capable of pushing guaranteed payout above acquisition cost. The 2026 ONCE 11/11 rules contain an unusual clause allowing up to EUR 11,000,000 of top-prize money to come from prizes that were not sold in earlier lottery draws, so it superficially resembles exactly that kind of external subsidy.

## Current 2026 rules

Official BOE resolution BOE-A-2026-9945, published 7 May 2026, fixes:
- draw date: 11 November 2026;
- sales start: 21 September 2026;
- price: EUR 6 per coupon;
- category 1: one EUR 11,000,000 exact number+series prize;
- category 2: eleven EUR 1,000,000 exact number+series prizes;
- fixed lower categories of EUR 50,000 / 2,000 / 1,200 / 120 / 12 / 6 under the stated match rules.

Crucially, paragraph 3.4 is a **funding-source rule**, not a prize enhancement. It states that, of the already-defined category-1 and category-2 amounts, up to EUR 11,000,000 may *come from* unsold prizes from earlier draws. It does not say that another EUR 11,000,000 is added to the published prize values.

Source: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-9945

## Structural consequence

The apparent rollover is not additive from the player's perspective:

`published player payout = same category schedule whether prior-unsold funding is used or not`

Therefore:

`additive external subsidy available to a full-identifier takeover = EUR 0`

This closes the mechanism we were looking for. Prior unsold prize money can replace part of the funding of the already-promised EUR 11m + 11xEUR 1m awards, but it does not lift those awards above their stated amounts.

Paragraph 3.5 reinforces the direction of flow: if a top winning coupon in the 11/11 draw itself is unsold, up to EUR 3m may be moved onward to later eligible products. Again, that is movement of prize funding between draws, not an automatic enhancement of the current coupon holder's payout.

## Historical 120-series calibration

The exact 2026 Q4 issuance count was not found in the currently published material as of this check, so no unsupported 2026 series-count claim is made. For calibration only, the official 2024 and 2025 calendars both used **120 series x 100,000 numbers x EUR 6 = EUR 72,000,000** issuance for the 11/11 draw.

Using the current category table with 120 series, a collision-free upper-bound reconstruction gives:
- category 1: EUR 11,000,000;
- category 2: EUR 11,000,000;
- category 3: EUR 5,950,000;
- category 4: EUR 2,618,000;
- categories 5/6/7: EUR 1,296,000 each;
- category 8: EUR 6,480,000;
- total schedule upper bound: **EUR 40,936,000**;
- return versus EUR 72m complete issuance cost: **56.8555556%**.

If the full EUR 11m of top-prize funding is imported from earlier unsold prizes, the prize schedule is still EUR 40.936m; only current-emission funding falls to EUR 29.936m, or **41.5777778%** of EUR 72m. This matches the interpretation in the official 2025 ONCE certificate, which stated that the prize percentage of the emission could range from about 41.6% when EUR 11m came from previous draws to about 56.9% when it did not.

Historical official sources:
- 2025 120-series issuance: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-23203
- 2025 ONCE certificate explaining the 41.6%–56.9% funding percentages: https://www1.juegosonce.es/pdf/reglamentos/CEP_6_2025_3_3.pdf

The lower-category reconstruction is deliberately player-favourable: categories other than 1 and 2 are non-accumulable, and repeated complete extractions can make lower-tier coupon sets overlap. Ignoring those collisions is therefore an upper bound, which is sufficient for rejection.

## Result

**REJECTED for the target external-subsidy mechanism.** The 2026 11/11 prior-unsold-prize clause does not inject an extra EUR 11m into player payouts; it only changes where up to EUR 11m of already-fixed top awards are funded from. There is therefore no deterministic additive rollover subsidy to exploit.

This does **not** claim that every conceivable ONCE promotion or future extraordinary draw is closed. Reopen only if a future rule explicitly raises prize amounts above the published schedule by adding prior-draw money, rather than merely sourcing part of fixed prizes from prior unsold awards.

## Reproducibility

- `src/loto_research/h270_once_1111_rollover_funding_bound.py`
- `data/derived/h270_once_1111_rollover_funding_bound.json`
- `research/H270_VALIDATION.md`
- `research/H270_STATUS.md`
