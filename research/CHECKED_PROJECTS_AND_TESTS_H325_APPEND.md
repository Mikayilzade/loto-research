# CHECKED PROJECTS AND TESTS — H325 APPEND

## H325 — undersold guaranteed-draw residual takeover

Status: **CLOSED / TAKEOVER-BLOCKED**

Tested whether a heavily undersold finite draw that is guaranteed to run can be turned into a strict one-player profit by buying all remaining entries near cutoff.

Reusable closure theorem for single-winner pools:
- if any valid external identifier already exists, buying all remaining entries still leaves a legal external-winner outcome, so strict main-prize cash floor is zero;
- if no external entries exist yet, one-player deterministic takeover still requires `max_per_player >= N`;
- only after both conditions pass should `liability > acquisition cost` be tested.

Current screened candidates:
- Elite £101,000 Cash — 4,999,999 entries, £0.05, max/player 20,000;
- Clubhouse £250 Flash Cash — 499 entries, £1, max/player 49;
- Competition Go £500 — 180 entries, £5, max/player 12;
- Caddy £3k Mega Bundle — 21,999 entries, £0.33, max/player 1,467;
- Competition Go £1,000 TUI + 20×£100 instants — 21,600 entries, £0.25, max/player 1,510.

All had at least one already-existing entry in the checked snapshot and all had person caps below N. Even impossible full ownership returned only 40.40%–55.56% of full acquisition cost.

Do not repeat this class merely because a draw is undersold or guaranteed to run. Reopen only for a fresh zero-entry pool with full-support one-player reservability and deterministic liabilities above acquisition cost.
