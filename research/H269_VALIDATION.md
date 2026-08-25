# H269 validation — Svenska Spel Joker

Validated: 2026-08-25
Verdict: **REJECTED / CLOSED for fixed-plan full-identifier takeover**

## Source gates
Official Svenska Spel rules effective for draws from 3 Sep 2025 were used. They establish a 7-digit `0000000..9999999` Joker result space, optional arbitrary Joker-number entry in some play methods, mandatory combination with Lotto, SEK 10/20/30 Joker stakes, the fixed current prize schedule, and the non-reuse rule for matched digit positions.

Primary rules:
https://cdn1.svenskaspel.net/content/cms/documents/779afe3f-0363-4c36-b79c-1881549a8cbc/1.29/spelregler-lotto-och-joker.pdf

Current game guide / prices:
https://www.svenskaspel.se/lotto/spelguide/joker

## Independent arithmetic gates
The reproducible calculator `src/loto_research/h269_svenska_spel_joker_full_identifier_bound.py` enumerates all 128 exact-match masks. For a mask with `m` matching positions its multiplicity is `9^(7-m)`, so total multiplicity must equal `10^7`.

Assertions embedded in code and independently checked:
- identifier count: **10,000,000**;
- winning identifiers for any fixed draw: **544,870**;
- exact full-space fixed Joker gross: **SEK 39,664,000**;
- minimum Joker-only full-cover stake: **SEK 100,000,000**;
- exact Joker fixed-plan return: **39.664%**;
- minimum mandatory Lotto+Joker acquisition spend, even granting one SEK 4 Lotto row per Joker identifier: **SEK 140,000,000**;
- Joker fixed-plan gross / minimum combined spend: **28.3314285714%**.

Payout-count checksum:
`9,455,130 + 494,262 + 46,413 + 486 + 9 + 3,402 + 18 + 261 + 18 + 1 = 10,000,000`.

Payout checksum:
`40*494,262 + 80*46,413 + 120*486 + 160*9 + 500*3,402 + 540*18 + 10,000*261 + 100,000*18 + 10,000,000 = 39,664,000`.

## Scope guard
This validation closes the **literal full Joker identifier fixed-payout takeover**. It does not claim that every conceivable joint Lotto+Joker portfolio has been exhausted. Drömvinsten requires a same-play Lotto 7-right result plus a Joker win and therefore needs a separate joint covering proof before it can be counted as deterministic subsidy.

No H225-X continuation is involved; H225 remains rigorously exhausted at X20.
