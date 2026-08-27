# H320 STATUS — Prizle Grab A Prize guaranteed-win cash-floor bound

Updated: 2026-08-27
State: **CLOSED / ZERO-WITHDRAWABLE-CASH-FLOOR**

## H225 exact-family lane

H225-X* remains separately **CLOSED / EXHAUSTED** at X20. The full validated X20 rescreen covered 44 canonical shards / 11 sectors / exactly 306,450 quotient states and left **0 coefficient survivors / 0 legal shift tuples**. No X21/X22 continuation was created.

## H320 checkpoint

H320 tested a genuinely different finite mechanism: Prizle's current **Grab A Prize** advertises one instant prize for every one of its 8,000 instant identifiers.

Exact published inventory decomposition:

- **7,000 site-credit-only identifiers**;
- **971 cash identifiers**;
- **29 product/gift identifiers**;
- total = **8,000**.

The page caps one player at **1,000 entries**. On the current indexed snapshot, **6,985 site-credit-only identifiers remained available**, still far above that cap.

Therefore a legal allocation exists in which every one of a player's maximum 1,000 entries receives only site credit, while an external entry wins the separate £500 end draw. The strict **withdrawable-cash floor is £0**.

For a stronger stress, the 1,000 cheapest distinct currently-available site-credit identifiers total only **£161.80** face value against **£4,990** maximum paid spend = **3.24248497%**, and site credit is not itself withdrawable cash.

H320 is terminal for this construction.

## Files

- `research/h320_prizle_grab_a_prize_cash_floor.md`
- `research/H320_VALIDATION.md`
- `src/loto_research/h320_prizle_grab_a_prize_cash_floor.py`
- `data/derived/h320_prizle_grab_a_prize_cash_floor.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H320_APPEND.md`

## NEXT ACTION

Do not reopen H320 merely because an operator says `every ticket wins`. Continue with a genuinely different mechanism satisfying at least one of:

1. every possible prize-bearing identifier has a **positive deterministic withdrawable-cash floor**, not only site credit or another random-entry right;
2. a finite pool can be controlled far enough that all zero-cash/nonwithdrawable identifiers are eliminated under the real per-player cap;
3. site credit has a separately proven deterministic conversion path into withdrawable cash with worst-case value high enough to cross acquisition cost; or
4. a hard-capped/reservable pool has player-facing deterministic liabilities above exact acquisition cost.

Prefer fresh zero/near-zero-sold pools with electronic reservation and `max_per_player` large enough to control the mathematically necessary identifier set.
