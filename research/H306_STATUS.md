# H306 STATUS

Updated: 2026-08-27
Packet: **H306 — On The Podium current zero-price finite-pool takeover screen**
State: **CLOSED / CURRENT-TAKEOVER-BLOCKED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Result

A genuinely useful mechanism was found: current On The Podium Prizes pages display several competitions at **Free per ticket** with a hard **1,000-ticket** finite pool. The strongest checked draw is `FREE TO ENTER £100 CASH!`.

However the current pool is already nonempty: the live homepage showed **16.2% sold**. Therefore at least one eligible identifier is already external. Even if a new entrant acquired every remaining identifier at £0, a legal draw outcome remains in which an external ticket wins, so the strict guaranteed cash floor is **£0**.

The published free-entry route also remains postal/non-atomic: proof of posting does not guarantee entry, and an entry is rejected if the finite cap is reached before receipt. Thus a hypothetical future fresh pool is not yet a rigorous takeover unless electronic same-inventory reservation and a full-pool per-user cap are explicitly established.

## Files

- `research/h306_onthepodium_current_free_pool_blocker.md`
- `research/H306_VALIDATION.md`
- `src/loto_research/h306_onthepodium_free_pool_blocker.py`
- `data/derived/h306_onthepodium_free_pool_blocker.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H306_APPEND.md`

## NEXT ACTION

Do not reopen this already-populated On The Podium pool. Search for a **fresh/zero-sold electronically reservable finite pool** satisfying all of:

1. zero-price or sufficiently discounted entries consume the same finite identifiers as paid entries;
2. one eligible player is allowed to reserve the entire (or mathematically sufficient) pool;
3. reservation is immediate/confirmed rather than postal or discretionary;
4. deterministic cash/cash-equivalent liabilities exceed acquisition cost.

H225-X* remains independently **CLOSED / EXHAUSTED** at X20 and must not be extended without changing the mathematical family.
