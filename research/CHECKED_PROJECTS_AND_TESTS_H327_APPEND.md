# Checked project append — H327

## H327 — KRAZED COSMIC CASH postal subsidy / random-allocation bound

Checked: 2026-08-28
Status: **CLOSED / RANDOM-ALLOCATION-AND-FREE-ROUTE-CAP BLOCKED**

Current KRAZED COSMIC CASH gives one valid postal entry 10 tickets. At the current £0.91 Royal Mail 2nd Class price, this is a real 9% deterministic discount versus ten paid 10p tickets.

Exact live inventory check:
- 99,999 total IDs;
- 316 sold snapshot;
- 12,029 published instant-prize IDs in total;
- 41 already found;
- 11,988 remaining instant IDs;
- **87,695 remaining zero-instant IDs**.

Because the free route permits only one postal entry per person (10 randomly allocated tickets) and `87,695 >= 10`, there is a legal all-zero allocation for the entire subsidised bundle. Strict guaranteed withdrawable-cash floor = **£0**.

Reusable filter: a real deterministic bundle discount is still useless for strict guarantee when the zero-cash support is at least the maximum subsidised bundle size and ticket identifiers are random/unselectable.

Sources:
- https://krazed.co.uk/competition/cosmic-cash
- https://www.royalmail.com/sending/uk/2nd-class

Primary files:
- `research/H327_STATUS.md`
- `research/h327_krazed_cosmic_cash_postal_subsidy.md`
- `research/H327_VALIDATION.md`
- `src/loto_research/h327_krazed_cosmic_cash_postal_subsidy.py`
- `data/derived/h327_krazed_cosmic_cash_postal_subsidy.json`
