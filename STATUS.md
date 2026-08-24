# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H247 — free Quick Pick / BOGO controlled-coverage subsidy closure**.
Latest completed exact-family packet: **H235**.
Current exact-family continuation: **H237**; expected merged outputs remain absent:
- `data/derived/h237_h235_first_survivor_separation.json`
- `data/derived/h237_new_witnesses.json`
Missing output proves nothing.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234: exact balanced counterexamples found for 44/44 sampled H232 survivors.
- H235: after adding H234 witnesses and affine symmetries, 303,802 coefficient states and 90,425,060 legal shift tuples still survive. H225 remains open.

### Recent lottery closures / blockers
- H236 RI Lucky 3 Spot: universal free 2X clears arithmetic threshold, but universal entitlement/execution not established.
- H238 RI Kick Back: exact current entitlement remains data-blocked.
- H239 Georgia/NC Keno Bonus Hours: rejected by exact full-coverage arithmetic.
- H240-H241 Missouri Club Keno Bonus Hours including Bulls-Eye variants: rejected by stronger-than-real +50% upper bounds.
- H242 Michigan Tripler Time: multiplier status is random, not deterministically allocable.
- H243 Illinois plus FIREBALL: exhaustive Straight-cover upper bounds remain below break-even.
- H244 WinTrillions Powerball discount: terms permit removal of the promotional enhancement in guaranteed-profit constructions.
- H245 UK Lotto current full-space: fixed-prize return too low and full coverage prevents the relevant rolldown branch.
- H246 LOTTO 6/49 Aug. 29 SuperDraw: even a deliberately favorable isolated-pool model returns only 46.5456% of full-cover spend.

### H247 — free Quick Pick / BOGO coverage-subsidy gate
Current primary examples:
- Kentucky Lottery, Aug. 1–31, 2026: $10+ Millionaire for Life purchase at Kroger gives two free $1 Cash Ball 225 **Quick Pick** plays.
- Hoosier Lottery coupon valid Mar. 23, 2026–Mar. 31, 2027: one free $5 Millionaire for Life ticket, **Quick Pick only**.

Exact worst-case result: an uncontrolled Quick Pick has **zero guaranteed marginal coverage**, because free selections may duplicate already-covered states; if the ticket can lose, its strict cash floor is also zero. Therefore a free Quick Pick cannot be counted as a deterministic discount to a controlled full-cover construction.

For Millionaire for Life the H026 controlled full-space requirement remains **22,910,580 plays / $114,552,900**, rather than a superficially discounted BOGO cover.

Files:
- `research/h247_free_quick_pick_coverage_gate.md`
- `src/loto_research/h247_free_quick_pick_coverage_gate.py`
- `data/derived/h247_free_quick_pick_coverage_gate.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H247_APPEND.md`

## NEXT ACTION
1. Check H237 merged output first.
2. If H237 returns new exact balanced witnesses, deduplicate against H234 and feed only new cuts into the next H225 exact rescreen.
3. Do not repeat H239-H247 without materially new rules/evidence.
4. Next independent lottery packet should prioritize active deterministic **player-selectable** discounts/subsidies or rolldowns with enough magnitude to cross an exact game-specific threshold.
5. Continue until lottery-specific SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H247_APPEND.md`.
