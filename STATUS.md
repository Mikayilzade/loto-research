# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H029 Virginia fixed-digit base-game class completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H029 fixed-odds digit games — NEW / BASE CLASS CLOSED
Files:
- `research/h029_fixed_digit_games_impossibility.md`
- `data/derived/h029_virginia_digit_base_ev.csv`

## General theorem
For any finite uniform draw game with additive wagers, if every constituent wager has expected payout no greater than its stake, then no nonnegative portfolio of those wagers can produce strictly positive profit for every draw outcome. Otherwise the guaranteed positive profit would imply positive expected profit, contradicting linearity of expectation.

## Virginia Pick 3
Current base menu checked: Exact, Any Order 3/6-way, 50/50, Combo, Pair.
Gross EV ratios per $1-equivalent stake are only **48%–50%**.
Full Exact coverage costs $1,000 and deterministically pays $500.

Status: **REJECTED entire additive base-game guarantee class**.

## Virginia Pick 4
Current base menu checked: Exact, Any Order 4/6/12/24-way, 50/50, Combo.
Gross EV ratios are only **48%–50%**.
Full Exact coverage costs $10,000 and deterministically pays $5,000.

Status: **REJECTED entire additive base-game guarantee class**.

## Virginia Pick 5
Current base menu checked: Exact, Any Order 5/10/20/30/60/120-way, 50/50.
Gross EV ratios are only **48%–50%**; 50/50 30-way = 49.75%.
Full Exact coverage costs $100,000 and deterministically pays $50,000.

Status: **REJECTED entire additive base-game guarantee class**.

## FIREBALL remains separate
FIREBALL doubles the cost and adds replacement-number winning combinations; wins can stack with base payouts. H029 deliberately does not infer its exact EV from the base-game theorem. It remains **H029b OPEN** for exact joint-outcome analysis.

# H028 Nebraska finite-game coverage — CLOSED
- Nebraska 2by2: optimistic full-space 38.03%; seven-draw Double Tuesday package 43.46%.
- Nebraska MyDaY: exact full-space gross range 48.13%–58.47%.
- Nebraska Pick 5: deterministic non-jackpot cash 21.44%; sole-winner jackpot hurdle $516,958; external sharing prevents strict guarantee.

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
- Nebraska 2by2 including Double Tuesday;
- Nebraska MyDaY;
- Nebraska Pick 5 current full-space structure;
- **Virginia Pick 3 / Pick 4 / Pick 5 additive base wager families**.

No terminal guarantee has emerged.

# Other active / blocked branches
- **H029b FIREBALL:** next local analytic target; exact joint-outcome EV/guarantee check can potentially close the entire Virginia Pick family including add-ons.
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
1. **H029b Virginia FIREBALL exact joint-outcome analysis**; close full Pick 3/4/5 family if every paid add-on remains non-positive EV.
2. Continue **fast analytic coverage/subsidy screens** on additional current finite/final-draw products; prioritize unusually high fixed cash floors, compact spaces, and deterministic subsidies.
3. **H020 live-data arbitrage:** resume immediately if direct public raw REST/WebSocket books become available.
4. **H006/H007:** resume only if reliable ordered histories/machine metadata become obtainable.
5. H010/H014 if new authoritative data routes appear.
6. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
7. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
