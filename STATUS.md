# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H031 Georgia/Virginia Cash Pop Cover All completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H031 — Georgia/Virginia Cash Pop Cover All CLOSED
Files:
- `research/h031_cash_pop_cover_all.md`
- `data/derived/h031_cash_pop_screen.csv`
- `src/loto_research/cash_pop.py`
- `tests/test_cash_pop.py`

Both current official products use one winning number from 1–15 and allow all 15 numbers to be purchased. The operator explicitly markets this as a guaranteed win / Cover All construction.

Exact guarantee result for any wager `w`:
- full coverage cost = `15w`;
- minimum legal draw prize = `5w`;
- strict guaranteed gross floor = **33.3333%**;
- guaranteed net floor = `-10w`.

Thus $1/$2/$5/$10 Cover All costs $15/$30/$75/$150 while the legal minimum draw payout is only $5/$10/$25/$50.

Published-table EV cross-checks are also negative:
- Georgia draw EV ratios: **62.9670%, 65.1911%, 67.8803%, 70.4735%** for $1/$2/$5/$10;
- Virginia: **60.9823%, 64.0336%, 67.2277%, 70.0062%**.

Georgia's current retail instant-win overlay pays double wager only on a random qualifying event and has a legal no-instant-win branch, so its strict guaranteed contribution is zero.

Status: **REJECTED as guaranteed-profit path.** This is a useful control showing that an operator's literal “guaranteed win” can still imply a large guaranteed loss after cost.

# Recently closed branches
- H029/H029b Virginia Pick 3/4/5 including FIREBALL: additive-family guarantee rejected by expectation upper bound.
- H030 Virginia Cash 5 + EZ Match: current full-space route strongly negative; jackpot sharing prevents strict future guarantee without hard external-winner cap.
- Beşdə 5 and ONLOTO 1–10 full coverage: rejected.
- UK/Irish fixed-payout screens H022–H025: rejected.
- Millionaire for Life, Lotto America, Nebraska finite screens H026–H028: rejected.
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
1. Continue fast analytic screens on additional **current compact finite/fixed-payout products**, prioritizing unusually high deterministic payout floors, fixed inventories, or external deterministic subsidies near the H021 takeout hurdle.
2. H020 live-data arbitrage immediately if raw public books become retrievable.
3. H019 capped competitions only when cash floor/full-cap economics improve materially.
4. H006/H007 only after reliable histories/machine metadata become obtainable.
5. H010/H014 if new authoritative data routes appear.
6. H018 conditional-EV calibration if exact mechanics/live endpoint become recoverable.
7. Advanced controls before EXHAUSTED: more current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
