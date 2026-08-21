# H159 audit append — fixed-board raffle residual forced-slot floor

Updated: 2026-08-21
Terminal state after packet: **NO SUCCESS; NOT EXHAUSTED**

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H159 residual fixed-board takeover theorem** | Buy every remaining ticket after `e` external sales; sort fixed prizes ascending | if `e>=W`, strict buyer prize floor `0`; if `e<W`, exact floor is sum of the `W-e` cheapest prizes because external tickets may occupy the highest `e` winning slots | **VALIDATED exact worst-case theorem**; `research/h159_residual_raffle_forced_slot_floor.md`, `src/loto_research/h159_residual_raffle_floor.py` |
| **H159 Virginia Commanders Golden Pass Raffle 2026** | `T=150,000`, $20/ticket, 3,506 winners: 3,000x$100 + 500x$500 + 5x$10,000 + 1x$950,000-value top prize | best strict residual state is `e=0`: $1.55m forced board vs $3m cost = **-$1.45m / 51.6667%**; any `e>0` worsens the floor | **REJECTED for every possible sales state**; `data/derived/h159_virginia_residual_raffle_floor.csv` |
| **H159 Virginia Capitals Career In A Year 2026** | same 150k-ticket / 3,506-winner / $20 design family | same residual-takeover economics and monotone failure | **REJECTED for every sales state** |
| **H159 Michigan online raffle architecture** | finite predetermined prize boards; random winners among sold tickets; no aggregate player purchase limit, cart supports up to 250 at a time with repeat additions | structurally favorable execution platform for a future all-remaining takeover, but fresh Aug-2026 public screen did not surface a current board/live state with `G(e)>0` | **MONITOR / NO CURRENT TERMINAL CANDIDATE** |

Next highest-value branch: apply H159 `G(e)` immediately to any live high-winner raffle with visible remaining inventory; in parallel continue deterministic Keno bundle/special-paytable monitor from H157-H158.
