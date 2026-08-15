# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H027 Lotto America full-space screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H027 Lotto America — NEW / CLOSED
Files:
- `research/h027_lotto_america_full_coverage.md`
- `data/derived/h027_lotto_america_full_coverage.csv`
- generic engine `src/loto_research/special_ball_coverage.py`
- regression tests extended in `tests/test_special_ball_coverage.py`

Current official structure verified from Minnesota/Iowa Lottery:
- 5 of 52 + Star Ball 1 of 10;
- $1 base play;
- $1 optional All Star Bonus, random 2x–5x on non-jackpot prizes;
- jackpot divided among multiple jackpot winners;
- lower-tier published prizes may be reduced pari-mutuel.

Full base space = `C(52,5)*10 = 25,989,600` lines; cost **$25,989,600**.
Deterministic published-table non-jackpot gross = **$6,991,428 = 26.9009%** before any pari-mutuel reduction.
Sole-winner cash-jackpot break-even hurdle = **$18,998,172** before tax/execution/sharing.

Strong recent stress test:
- July 18 2026 advertised jackpot: **$34.12m annuity**;
- Minnesota Lottery reported cash option: **$15,154,248**;
- even granting full cash jackpot to our portfolio plus unreduced lower tiers gives **$22,145,676 = 85.2098%** of full-space cost;
- optimistic deficit **$3,843,924**.

All Star Bonus full-space worst legal 2x state doubles cost to $51,979,200 and yields $13,982,856 non-jackpot floor; sole-winner cash hurdle rises to **$37,996,344**.

Status: **REJECTED guaranteed-profit full coverage**. A future high jackpot can create a conditional/EV lead, but strict guarantee remains blocked by external jackpot sharing, possible lower-tier pari-mutuel reduction, and execution friction.

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
- US Millionaire for Life;
- **US Lotto America**.

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
1. Continue **fast analytic coverage/subsidy screens** on additional current finite/final-draw products; prioritize small spaces and real cash jackpots/subsidies, and deep-dive only candidates approaching/exceeding 100% deterministic coverage return.
2. **H020 live-data arbitrage:** resume immediately if direct public raw REST/WebSocket books become available.
3. **H006/H007:** resume only if reliable ordered histories/machine metadata become obtainable.
4. H010/H014 if new authoritative data routes appear.
5. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
6. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
