# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H029b Virginia FIREBALL and H030 Virginia Cash 5/EZ Match completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H029 / H029b — Virginia Pick 3/4/5 family CLOSED
Files:
- `research/h029_fixed_digit_games_impossibility.md`
- `data/derived/h029_virginia_digit_base_ev.csv`
- `data/derived/h029b_virginia_fireball_ev_bounds.csv`
- `src/loto_research/fireball_bounds.py`
- `tests/test_fireball_bounds.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H029B_APPEND.md`

Base-game theorem: every checked Exact/Any/50-50/Combo/Pair wager has gross EV <=50%, so no nonnegative additive portfolio can guarantee positive profit in every outcome.

FIREBALL extension is now also closed. Virginia states FIREBALL doubles the play cost and pays separate additional prizes. Using published prize/odds rows and deliberately **double-counting overlapping 50/50 rows** to create a player-favorable EV upper bound:
- Pick 3 max FIREBALL EV/stake upper bound: **65.5999%**;
- Pick 4: **62.8960%**;
- Pick 5: **60.3587%**.

With base EV <=50%, the best deliberately favorable combined base+FIREBALL EV ratio is below **57.8000%**. Therefore the entire current Pick 3/4/5 + FIREBALL paid additive family is **REJECTED as a guaranteed-profit path** by expectation linearity.

# H030 — Virginia Cash 5 with EZ Match CLOSED
Files:
- `research/h030_virginia_cash5_ezmatch.md`
- `data/derived/h030_virginia_cash5_ezmatch.csv`

Current official structure:
- 5/45; $1 per play;
- full space `C(45,5)=1,221,759`;
- deterministic fixed lower-tier cash under full coverage = **$177,800**;
- sole-winner jackpot break-even = **$1,043,959** before tax/execution;
- checkpoint advertised jackpot = **$210,000**;
- optimistic full-space return granting our line the entire $210k jackpot = only **31.7400%**.

The jackpot is explicitly split among multiple winning plays, so even a future jackpot above the sole-winner threshold does not create a strict guarantee without a useful hard pre-draw cap on external winners.

EZ Match costs an extra $1 and has approximate gross EV **$0.654615706 = 65.4616%** from the published prize/odds table. It is a paid random add-on and cannot rescue an additive guarantee.

Status: **REJECTED current guaranteed-profit route**.

# Fast-screen program to date
Closed current finite/fixed-payout or additive guarantee cases include:
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
- Virginia Pick 3 / Pick 4 / Pick 5 **including FIREBALL**;
- Virginia Cash 5 with EZ Match.

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
1. Continue fast analytic screens on additional **current compact finite/fixed-payout products**, prioritizing unusually high guaranteed cash floors, fixed finite ticket inventories, deterministic subsidies, or payout ratios near 100%.
2. H020 live-data arbitrage: resume immediately if direct public raw REST/WebSocket books become available.
3. H019 capped competitions: search for zero-external-entry / atomic-close cases with cash floor exceeding effective cap cost.
4. H006/H007: resume only if reliable ordered histories/machine metadata become obtainable.
5. H010/H014 if new authoritative data routes appear.
6. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
7. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference, causal implementation tests, and explicit scan for deterministic cash rebates/subsidies.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
H029b audit append saved separately as `research/CHECKED_PROJECTS_AND_TESTS_H029B_APPEND.md` to preserve the large ledger without destructive truncation; H030 details are in its dedicated research note and this checkpoint pending next safe ledger consolidation.
