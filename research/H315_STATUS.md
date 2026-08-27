# H315 STATUS

Updated: 2026-08-27
Status: **CLOSED / TAKEOVER-BLOCKED**

## Result

Current U Comps `£50,000 Instant Win Competition` (#143) publishes unclaimed instant-win identifiers, but the one-player acquisition cap and ticket-allocation mechanics prevent deterministic capture.

Snapshot exact gate:
- 175,000 total tickets;
- 38,626 sold;
- 136,374 remaining;
- 137 instant-win identifiers remaining;
- at least **136,237 remaining non-instant identifiers**;
- max **500 entries per person**.

Since 136,237 non-instant identifiers are available to absorb all 500 permitted entries, there is a legal allocation in which the player receives no instant-win identifier. Exact identifier reservation before checkout is not established; the platform provider states tickets are allocated after purchase success with no ticket reservation.

The final draw does not create a floor because 500 << 175,000 and external-winning identifiers remain legal.

**Strict guaranteed cash floor: £0.**

## Files

- `research/h315_ucomps_instant_win_cap_bound.md`
- `research/H315_VALIDATION.md`
- `src/loto_research/h315_ucomps_instant_win_cap_bound.py`
- `data/derived/h315_ucomps_instant_win_cap_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H315_APPEND.md`

## NEXT ACTION

Do not repeat published-identifier instant-win pools unless exact winning identifiers are selectable/reservable before payment. Search for a finite mechanism where the player can deterministically lock every zero-cash-threatening identifier, preferably electronically, within the per-player cap, and where the guaranteed liabilities exceed acquisition cost.
