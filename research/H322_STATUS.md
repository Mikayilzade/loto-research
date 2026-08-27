# H322 STATUS — SOBO first-ticket-free random-allocation cap bound

Updated: 2026-08-28
State: **CLOSED / CAP-AND-RANDOM-ALLOCATION-BLOCKED**

## H225 exact-family lane

H225-X* remains separately **CLOSED / EXHAUSTED** at X20. The validated full rescreen covered 44 canonical shards / 11 sectors / exactly 306,450 quotient states and left **0 coefficient survivors / 0 legal shift tuples**. No X21/X22 continuation was created.

## H322 checkpoint

H322 tested a new live finite-pool subsidy construction: SOBO's `Instant Win Frenzy — 29p Tickets` combines a 500,000-ID pool, a first ticket free, electronic checkout holds, instant prizes, and a snapshot with only 1 ticket sold.

The governing rules defeat targeted takeover. Ticket IDs are allocated randomly from the remaining pool and cannot be chosen; hidden instant-win identifiers cannot be searched before purchase. The maximum is 2,000 entries per person.

Even granting the player the strongest reasonable prize-ID count — 50,000 advertised instant-credit IDs plus five cash-prize IDs all distinct — at least **449,995** identifiers remain zero-instant. Since 449,995 >= 2,000, a legal allocation exists in which every allowed player ticket receives zero instant prize. The separate draw also retains legal external-winner states because the player cannot control the full pool.

Therefore the strict withdrawable-cash floor is **£0**. The free first ticket changes price only; it does not eliminate zero-cash outcomes.

## Files

- `research/h322_sobo_first_ticket_free_cap_bound.md`
- `research/H322_VALIDATION.md`
- `src/loto_research/h322_sobo_first_ticket_free_cap_bound.py`
- `data/derived/h322_sobo_first_ticket_free_cap_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H322_APPEND.md`

## NEXT ACTION

Do not reopen random-allocation finite pools merely because they offer one free/discounted ticket. Continue with a genuinely different mechanism where at least one of these is true:

1. exact prize-bearing identifiers are selectable and electronically reserved before payment;
2. `max_per_player` is large enough to eliminate **all** zero-cash identifiers under the real allocation mechanism; or
3. every legal residual identifier has positive withdrawable-cash value and the exact worst-case aggregate value exceeds acquisition cost.

Prefer fresh zero/near-zero-sold pools with deterministic identifier control rather than random post-checkout allocation.
