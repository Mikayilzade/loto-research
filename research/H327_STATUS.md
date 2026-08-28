# H327 STATUS

Updated: 2026-08-28
State: **CLOSED / RANDOM-ALLOCATION-AND-FREE-ROUTE-CAP BLOCKED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Result

H327 tested the current KRAZED `COSMIC CASH` pool because its postal route is a genuine deterministic acquisition subsidy: one £0.91 2nd Class postal entry receives 10 tickets that would cost £1.00 online, a **9% discount**.

The live finite pool has 99,999 identifiers. The exact published instant schedule contains **12,029 prize-bearing identifiers / £5,650 cash face value**. On the checked snapshot 316 tickets were sold and 41 instant prizes were already found, leaving:

- 99,683 tickets;
- 11,988 remaining instant-win identifiers;
- **87,695 remaining zero-instant identifiers**.

The free route allows only one postal entry per person per competition, i.e. 10 subsidised randomly allocated tickets. Since `87,695 >= 10`, there is a legal allocation in which all ten tickets land in zero-instant positions. Thus the strict guaranteed withdrawable-cash floor is **£0** despite the real 9% subsidy.

The ordinary paid cap is also only 999/99,999, so a one-player full takeover is impossible. Postal processing delay/cap-fill risk independently reinforces the closure.

## Files

- `research/h327_krazed_cosmic_cash_postal_subsidy.md`
- `research/H327_VALIDATION.md`
- `src/loto_research/h327_krazed_cosmic_cash_postal_subsidy.py`
- `data/derived/h327_krazed_cosmic_cash_postal_subsidy.json`

## H225 lane

`H225-X*` remains **CLOSED / EXHAUSTED** at X20 with 0 coefficient survivors / 0 legal shift tuples. Do not create X21/X22 from the unchanged family.

## NEXT ACTION

Do not reopen H327 unless the free-entry cap/allocation mechanics materially change. Prioritize a finite subsidized pool where the discounted/free acquisition amount is large enough to eliminate **all zero-cash identifier support**, or where prize-bearing identifiers can be selected and atomically reserved before purchase. In particular, look for `subsidized_bundle_size > remaining_zero_cash_support` or a selectable/reservable prize-ID mechanism, then test exact economics before execution friction.
