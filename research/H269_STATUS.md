# H269 STATUS

Updated: 2026-08-25
Terminal state for packet: **CLOSED / REJECTED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Result
Svenska Spel Joker was screened as a finite, partly player-selectable, fixed-payout identifier space.

Exact full one-copy coverage of all 10,000,000 seven-digit Joker identifiers gives an invariant Joker fixed-plan gross of **SEK 39,664,000** at the SEK 10 stake level.

Costs:
- Joker stakes alone: **SEK 100,000,000** -> **39.664%** return.
- Joker cannot be played standalone with Lotto. At the current minimum SEK 4 Lotto row price, even the impossible-favourable one-base-row-per-identifier acquisition floor is **SEK 140,000,000** -> Joker fixed-plan gross is only **28.3314286%** of combined spend.

This closes the literal fixed-plan full-Joker-identifier takeover mechanism. A joint Lotto+Joker/Drömvinsten construction would be a separate problem and has not been claimed closed by H269.

## Validation
- exact 128 mask enumeration represents all `10^7` identifiers;
- identifier count checksum = **10,000,000**;
- winning identifiers = **544,870**;
- fixed-plan payout checksum = **SEK 39,664,000**;
- current official rules effective from 3 Sep 2025 were used;
- H225-X lane remains rigorously closed at X20 and was not modified.

Files:
- `research/h269_svenska_spel_joker_full_identifier_bound.md`
- `research/H269_VALIDATION.md`
- `src/loto_research/h269_svenska_spel_joker_full_identifier_bound.py`
- `data/derived/h269_svenska_spel_joker_full_identifier_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H269_APPEND.md`

## NEXT ACTION
Continue outside H225 with the global mechanism search. Prioritize a genuinely external deterministic subsidy or hard-capped/reservable identifier pool whose total guaranteed payout can exceed complete acquisition cost. Do not repeat ordinary fixed-plan identifier covers with prize-fund ratios around 40% unless a separate deterministic subsidy crosses the gap.
