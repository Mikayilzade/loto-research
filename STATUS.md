# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H026 Millionaire for Life fixed-space screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H026 Millionaire for Life — NEW / CLOSED
Files:
- `research/h026_millionaire_for_life_full_coverage.md`
- `data/derived/h026_millionaire_for_life_full_coverage.csv`
- `src/loto_research/special_ball_coverage.py`
- `tests/test_special_ball_coverage.py`

Current operator structure verified from MUSL/Powerball and Georgia Lottery:
- choose 5 of 58 white numbers + 1 of 5 Millionaire Balls;
- $5 per play;
- current top cash option $18m;
- second-prize cash option $2.2m;
- lower tiers $7,500/$500/$250/$50/$25/$8/$8;
- top level is pari-mutuel in specified circumstances.

Full space = `C(58,5)*5 = 22,910,580` plays; cost **$114,552,900**.

Using a deliberately player-favorable rejection bound — full $18m for our 5+MB line, full $2.2m for each of our four 5-only lines, no external sharing reduction, no tax/execution cost — deterministic gross is only **$60,584,320 = 52.8876%**.
Optimistic deterministic deficit = **$53,968,580**.

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
- Austrian LottoPlus sampled fixed-pool promotion via H021 subsidy bound;
- US Millionaire for Life.

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