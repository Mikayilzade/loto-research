# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H025 Health Lottery fixed-space screens completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H025 The Health Lottery — NEW
Files:
- `research/h025_health_lottery_full_coverage.md`
- `data/derived/h025_health_lottery_full_coverage.csv`

## Big Win + Wednesday/Saturday Free Prize Draw — CLOSED
Current operator structure verified:
- choose 5 of 50;
- £1 per Big Win line;
- fixed lower cash tiers plus shared £25,000 Match-5 top prize;
- Wednesday/Saturday every paid Big Win line also receives a free second 5-of-50 entry for a £100,000 cash prize.

Full Big Win space = `C(50,5)=2,118,760` lines, cost **£2,118,760**.

For rejection the calculation is deliberately biased in the player's favor:
- grant our Match-5 line the entire £25,000 despite external sharing;
- value all **198,660** earned free-ticket outcomes at full £1 face value, despite not being withdrawable cash and being able to lose on replay;
- grant our full-space portfolio the entire **£100,000** auxiliary Free Prize Draw prize, again ignoring possible sharing.

Even then deterministic package value is only **£603,560 = 28.4865%** of cost.
Optimistic guaranteed deficit = **£1,515,200** before execution.

Status: **REJECTED guaranteed-profit full coverage**.

## All Or Nothing — CLOSED
Current structure verified: choose 12 of 24 for £1; prizes are symmetric for matching all/none and near-extreme match counts; top prize £25,000 is shared if multiple winners.

Full space = `C(24,12)=2,704,156` lines; cost **£2,704,156**.
For any winning 12-set, exact portfolio count with m matches is `C(12,m)^2`.

Again use an intentionally favorable bound by granting both our 12-match and 0-match tickets a full £25,000 each despite the sharing rule.
Optimistic deterministic gross = **£1,071,850 = 39.6371%**.
Optimistic deficit = **£1,632,306**.

Status: **REJECTED guaranteed-profit full coverage**.

# Fast-screen program to date
Closed current finite/fixed-payout coverage cases now include:
- Beşdə 5;
- ONLOTO bet types 1–10;
- UK Lotto HotPicks;
- EuroMillions HotPicks;
- Irish Daily Million;
- Irish Lotto 5-4-3-2-1;
- UK Set For Life;
- UK Thunderball;
- UK Health Lottery Big Win including deterministic free auxiliary draw;
- UK Health Lottery All Or Nothing;
- Austrian LottoPlus sampled fixed-pool promotion via H021 subsidy bound.

The strongest deterministic returns found among these remain materially below 100%; no terminal guarantee has emerged.

# Other active / blocked branches
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; current raw-book acquisition remains runtime/data blocked.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Previously closed highlights
- Cash WinFall: historical +EV mechanism validated, not current terminal guarantee.
- Powerball full-space: rejected due unbounded external jackpot sharing.
- Mega Millions full-space: rejected due cost/sharing/random multiplier.
- EuroMillions terminal-cap full coverage: rejected because full coverage itself guarantees a 5+2 winner and prevents no-winner rolldown.
- H008 cross-jurisdiction: EV differences validated; standalone guarantee rejected.
- H012a/H004 ordinary additive wheels: closed by expectation theorem.
- 4+4 single 5+5/6+6 systems: zero-payout outcomes exist; full-space theorem remains data-blocked.
- H015 anti-crowd standalone: closed as guarantee; useful overlay only.
- H005/H009 ordinary system discounts/random promos/free-play: screened; no terminal deterministic guarantee.
- H011 lawful visible pre-purchase decoder: screened NY/Virginia channels closed.

# Next priorities
1. Continue **fast analytic coverage/subsidy screens** on additional current fixed-payout/final-draw products; deep-dive only candidates approaching/exceeding 100% deterministic coverage return or with guaranteed external subsidy sufficient to cross takeout.
2. **H020 live-data arbitrage:** resume immediately if direct public raw REST/WebSocket books become available.
3. **H006/H007:** resume only if reliable ordered histories/machine metadata become obtainable.
4. H010/H014 if new authoritative data routes appear.
5. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
6. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.