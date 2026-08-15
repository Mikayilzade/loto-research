# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H028 Nebraska finite-game full-coverage screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H028 Nebraska finite-game coverage — NEW / CLOSED
Files:
- `research/h028_nebraska_finite_coverage.md`
- `data/derived/h028_nebraska_full_coverage.csv`
- `src/loto_research/nebraska_coverage.py`
- `tests/test_nebraska_coverage.py`

## Nebraska 2by2
Current official structure verified:
- $1 play;
- choose 2 red of 26 and 2 white of 26;
- full space `C(26,2)^2 = 105,625` plays;
- published top/set cash plus free-play lower tiers;
- qualifying 7-draw packages get Double Tuesday;
- regulations allow top-prize division above ten winning plays and broader set-prize pari-mutuel reductions if reserves are insufficient.

Even granting full published cash values and ignoring all reductions:
- normal full-space gross = **$40,168 = 38.0289%** of $105,625 cost;
- full-space across seven qualifying draws, including doubled Tuesday, gross = **$321,344 / $739,375 = 43.4616%**.

Status: **REJECTED guaranteed-profit coverage**.

## Nebraska MyDaY
Current official structure verified:
- $1 per valid MM-DD-YY date;
- 36,525 valid combinations under published leap-year rule;
- prize categories exact date / partial month-day-year matches.

Exact all-state full-space calculation:
- cost = **$36,525**;
- minimum gross across every legal draw = **$17,580 = 48.1314%**;
- maximum gross = **$21,357 = 58.4723%**.

Status: **REJECTED guaranteed-profit coverage**.

## Nebraska Pick 5
Current official structure verified:
- 5 of 40 at $1;
- full space `C(40,5)=658,008`;
- 4/5=$500, 3/5=$9, 2/5=free Quick Pick;
- jackpot grows from $50,000 and is divided among multiple winners;
- lower tiers may become pari-mutuel in unusual circumstances.

Full-space published lower-tier cash = **$141,050 = 21.4359%** of cost.
Even assuming our jackpot line were the sole winner, jackpot cash would need to exceed **$516,958** merely to break even before tax/execution. Strict guarantee cannot assume sole winner because external jackpot sharing has no useful pre-draw hard cap.

Status: **REJECTED current guaranteed-profit coverage**; future very-large-jackpot states may be EV leads only.

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
- US Lotto America;
- **Nebraska 2by2 including Double Tuesday**;
- **Nebraska MyDaY**;
- **Nebraska Pick 5 current full-space structure**.

No terminal guarantee has emerged.

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
1. Continue **fast analytic coverage/subsidy screens** on additional current finite/final-draw products; prioritize unusually high fixed cash floors, compact spaces, and deterministic subsidies.
2. **H020 live-data arbitrage:** resume immediately if direct public raw REST/WebSocket books become available.
3. **H006/H007:** resume only if reliable ordered histories/machine metadata become obtainable.
4. H010/H014 if new authoritative data routes appear.
5. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
6. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
