# H325 validation — undersold guaranteed finite draws

Validated: 2026-08-28
Result: **CLOSED / TAKEOVER-BLOCKED**

Independent checks against `data/derived/h325_undersold_guaranteed_draw_takeover.json`:

1. Every screened draw has at least one already-existing valid entry outside a hypothetical fresh buyer's control (`sold_snapshot = 1`). A single such identifier is sufficient to preserve a legal external-winner outcome in a single-winner draw.
2. Every published `max_per_player` is strictly below the finite universe `N`; therefore even at a zero-entry launch state none of these five could be completely monopolized by one player under the published cap.
3. Full-pool cost arithmetic:
   - Elite: 4,999,999 × £0.05 = £249,999.95; £101,000 / £249,999.95 = 40.40000808%.
   - Clubhouse: 499 × £1 = £499; £250 / £499 = 50.10020040%.
   - Competition Go £500: 180 × £5 = £900; £500 / £900 = 55.55555556%.
   - Caddy: 21,999 × £0.33 = £7,259.67; £3,000 / £7,259.67 = 41.32419242%.
   - Competition Go TUI+instants: 21,600 × £0.25 = £5,400; £3,000 / £5,400 = 55.55555556%.
4. Thus even an impossible-perfect full takeover is below break-even for every screened candidate; the structural external-entry/cap blocker is therefore not the only reason for closure.
5. No H225-X continuation was created. `research/H225_EXACT_STATUS.md` remains terminal at X20 with exactly 306,450 quotient states rescreened and 0 coefficient survivors / 0 legal shift tuples.

No success claim is warranted.
