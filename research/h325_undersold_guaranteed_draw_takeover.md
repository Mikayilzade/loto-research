# H325 — undersold guaranteed-draw residual takeover screen

Date: 2026-08-28
Status: **CLOSED / TAKEOVER-BLOCKED**

## Question

Can a heavily undersold, guaranteed-to-draw finite UK prize competition become a strict guaranteed-profit opportunity if one player buys all remaining entries shortly before the draw?

## Structural theorem

For a single-winner finite draw, buying all *remaining* entries is not enough if even one valid external entry already exists. That external identifier is still a legal winning outcome, so the buyer's strict main-prize cash floor remains zero.

A fresh one-player deterministic takeover therefore requires both:

1. zero already-existing external valid entries; and
2. `max_per_player >= N`, so the player can acquire every valid identifier.

Only after both gates pass is it meaningful to test `prize liability > full acquisition cost`.

This theorem is stronger than an expected-value or live-odds argument: an undersold draw can have excellent odds while still having zero strict guaranteed cash floor.

## Current live screen

Five current/near-current finite guaranteed-draw candidates were screened from live competition-index data on 2026-08-28.

| Draw | N | sold snapshot | max/player | price | generous liability | impossible full-buyout return |
|---|---:|---:|---:|---:|---:|---:|
| Elite £101,000 Cash | 4,999,999 | 1 | 20,000 | £0.05 | £101,000 | 40.4000% |
| Clubhouse £250 Flash Cash | 499 | 1 | 49 | £1.00 | £250 | 50.1002% |
| Competition Go £500 | 180 | 1 | 12 | £5.00 | £500 | 55.5556% |
| Caddy £3k Mega Bundle | 21,999 | 1 | 1,467 | £0.33 | £3,000 | 41.3242% |
| Competition Go TUI + 20×£100 instants | 21,600 | 1 | 1,510 | £0.25 | £3,000 | 55.5556% |

Every candidate fails both structural gates: at least one external entry already exists and the published per-player cap is far below the finite universe. Therefore each preserves a legal external-winner outcome and has strict one-player main-prize cash floor £0.

Even granting impossible ownership of the whole finite pool, all five remain below break-even. The best full-buyout upper bound is only 55.5556%.

## Sources checked

- Elite £101,000 Cash, 4,999,999 entries, £0.05, max/player 20,000, guaranteed £101,000 draw: https://www.competitionshowroom.com/competition/elite-competitions-101000-cash
- Clubhouse Friday 28 Aug £250 Flash Cash, 499 entries, £1, max/player 49: https://www.competitionshowroom.com/competition/clubhouse-competitions-auto-draw-friday-28th-august-250-flash-cash
- Competition Go £500, 180 entries, £5, max/player 12, guaranteed winner/no extensions: https://www.competitionshowroom.com/competition/competition-go-500-for-5-only-180-tickets-in-total
- Caddy 2026 Ping G440 £3k bundle, 21,999 entries, £0.33, max/player 1,467: https://www.competitionshowroom.com/competition/caddycomps-win-2026-ping-g440-3k-mega-bundle-32
- Competition Go £1,000 TUI + 20×£100 instants, 21,600 entries, £0.25, max/player 1,510: https://www.competitionshowroom.com/competition/competition-go-1000-tui-voucher-20x-100-instant-wins-just-25p-per-entry

Snapshot counts are time-sensitive and are used only as a blocker: once a valid external entry exists, later sales cannot restore deterministic one-player ownership.

## Exact checks

Reproducible model: `src/loto_research/h325_undersold_guaranteed_draw_takeover.py`

Derived data: `data/derived/h325_undersold_guaranteed_draw_takeover.json`

Assertions require all five screened pools to have:
- an existing-external-entry blocker;
- a per-player-cap blocker;
- no strict takeover;
- no strict guaranteed profit;
- full-buyout liability ratio below 100% even under impossible-perfect ownership.

## Conclusion

**H325 is closed.** "Guaranteed draw regardless of sellout" is not itself a guaranteed-profit mechanism. For a one-player strict guarantee, a candidate must be caught before any external valid identifier exists, allow one player to reserve the entire winning support, and still have deterministic liabilities above exact acquisition cost.

## NEXT ACTION

Search specifically for a **fresh zero-entry finite guaranteed draw** where `max_per_player >= N` (or another mechanism makes all external winning support impossible) and the exact deterministic prize/cash liability exceeds the cost of acquiring the whole support. Do not reopen ordinary undersold draws merely because live odds are favorable.
