# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H035 Lotterywest compact-game screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H035 — Lotterywest Super66 + Cash 3 CLOSED as guarantees
Files:
- `research/h035_lotterywest_compact_games.md`
- `data/derived/h035_lotterywest_compact_screen.csv`
- `src/loto_research/lotterywest_compact.py`
- `tests/test_lotterywest_compact.py`

## Super66
Current official mechanics:
- AUD 1 per game;
- six-digit 000000–999999 outcome space;
- Division 1 minimum payout AUD 66,666;
- lower fixed prizes AUD 6,666 / 666 / 66 / 6.60;
- only the larger prize is paid when both ends / multiple divisions match;
- selections are automatically randomly generated for the player.

Hypothetical exact unique full-space counts:
- D1: 1
- D2: 18
- D3: 180
- D4: 1,800
- D5: 17,901.

At the minimum D1 payout, hypothetical unique full coverage costs AUD 1,000,000 and returns only **AUD 543,480.60 = 54.3481%**.
More decisively, the operator does not let the player force the exact one-million-string unique cover: numbers are automatically random. Any finite random purchase can contain duplicates and omit a possible winner, so deterministic all-outcome coverage is not executable.

Status: **REJECTED guaranteed-profit coverage**.

## Cash 3
Official fixed-odds base menu:
- Exact: AUD0.50 -> 250; AUD1 -> 500; odds 1/1000;
- Any Order 3-way: AUD0.50 -> 80; AUD1 -> 160;
- Any Order 6-way: AUD0.50 -> 40; AUD1 -> 80.

Exact all-outcome partition cover at AUD0.50:
- 10 all-equal outcomes -> 10 Exact wagers;
- 270 one-pair ordered outcomes -> 90 Any-Order-3 wagers;
- 720 all-distinct ordered outcomes -> 120 Any-Order-6 wagers.

Total cost **AUD110**. Guaranteed gross floor is only **AUD40 = 36.3636%** of cost. Expected gross is AUD52.90 = **48.0909%**. Negative additive expectation also rules out any strict positive-profit portfolio under ordinary linear wagers.

Status: **REJECTED guaranteed-profit additive/coverage class**.

# Recently closed branches
- H034 Ontario DAILY KENO Pick 2–10: favorable uncapped full-space/EV return only 42.03%–55.07%; rejected additive guarantee class.
- H033 New Zealand Bullseye: real 28.57% multi-draw discount, but shared/capped payouts and external duplicates destroy strict guarantee.
- H032 Canada DAILY GRAND: favorable full coverage 44.35%, strict cash floor 36.21%.
- H031 Georgia/Virginia Cash Pop Cover All: guaranteed win but floor 33.33% of coverage cost.
- H029/H029b Virginia Pick 3/4/5 including FIREBALL: additive-family guarantee rejected by expectation bound.
- H030 Virginia Cash 5 + EZ Match: current full-space route negative; jackpot sharing blocks strict guarantee.
- H021–H028 compact/fixed/full-space screens: sampled products rejected.
- Beşdə 5 and ONLOTO 1–10 full coverage: rejected.
- Powerball/Mega Millions/EuroMillions full-space terminal guarantees: rejected.
- H012a/H004 ordinary additive wheels: rejected by expectation theorem.
- H015 anti-crowd standalone: rejected as guarantee; overlay only.

# Other active / blocked branches
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; current raw-book acquisition remains runtime/data blocked.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Next priorities
1. Continue **H021–H035 fast analytic screens** on current finite/fixed-payout products, but favor candidates with deterministic discounts/rebates/subsidies or unusually high coverage return.
2. Search specifically for **deterministic discount + fixed non-shared cash payouts**; this remains the strongest structural combination not yet exhausted.
3. Revisit H020 live arbitrage immediately if raw public order books become retrievable.
4. H019 only when capped-entry cash-floor economics materially improve.
5. H006/H007 only after reliable histories/machine metadata become obtainable.
6. H010/H014 if new authoritative data routes appear.
7. H018 conditional-EV calibration if exact mechanics/live endpoint becomes recoverable.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
