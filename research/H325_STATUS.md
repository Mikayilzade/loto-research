# H325 STATUS

Updated: 2026-08-28
State: **CLOSED / TAKEOVER-BLOCKED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Result

H325 tested a genuinely different mechanism: buying all remaining tickets in a heavily undersold finite draw that is guaranteed to run regardless of sellout.

For a single-winner draw this does **not** create a strict guarantee if any external valid ticket already exists. One external identifier preserves a legal outcome where that identifier wins. A fresh deterministic one-player takeover therefore needs both `external_valid_entries = 0` and `max_per_player >= N` before economics are even relevant.

Five current candidates were screened. All have an existing-external-entry blocker and all have `max_per_player < N`. Even granting impossible full ownership, their generous full-buyout liability ratios are only **40.40%–55.56%**, so none crosses break-even anyway.

Best screened impossible-perfect ratio: **55.5556%**.
Strict guaranteed one-player cash floor from the main draw under the actual structural conditions: **£0**.

## Files

- `research/h325_undersold_guaranteed_draw_takeover.md`
- `research/H325_VALIDATION.md`
- `src/loto_research/h325_undersold_guaranteed_draw_takeover.py`
- `data/derived/h325_undersold_guaranteed_draw_takeover.json`

## H225 lane

`H225-X*` remains **CLOSED / EXHAUSTED** at X20. Do not create X21/X22 from the unchanged family.

## NEXT ACTION

Search for a fresh **zero-entry** finite guaranteed draw or equivalent reservable pool where one eligible player can control the entire winning support (`max_per_player >= takeover size`) and deterministic cash/withdrawable liabilities are strictly greater than exact acquisition cost. Do not reopen ordinary undersold draws solely because live odds are attractive.
