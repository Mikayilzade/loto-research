# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H022 fixed-subset full-coverage theorem implemented and Irish Lotto 5-4-3-2-1 current/future regimes screened**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H022 fixed-payout subset coverage — NEW
Files:
- `research/h022_irish_54321_full_coverage.md`
- `src/loto_research/fixed_subset_coverage.py`
- `tests/test_fixed_subset_coverage.py`
- `data/derived/h022_irish_54321_full_coverage.csv`

Generic identity: in an all-selected-numbers-must-hit game, if the universe has N numbers, the realized winning target has d numbers and we buy every k-subset, then exactly `C(d,k)` of our `C(N,k)` entries win for every legal outcome. Full-space return is therefore deterministic:

`C(d,k) * payout(k) / [C(N,k) * stake]`.

## Irish Lotto 5-4-3-2-1 — CLOSED
Current official 47-ball game, €1 base stake:
- 6-number variant full-space returns across k=1..5: **76.60%, 62.44%, 67.84%, 50.46%, 48.89%**;
- 7-number including Bonus returns: **74.47%, 62.16%, 59.36%, 58.87%, 54.76%**.

Every current variant is therefore a strict deterministic loss under full coverage.

The operator announced on 2026-07-16 that Lotto will move from 47 balls to 45 in autumn 2026. Holding today's 5-4-3-2-1 payout table fixed as a deliberately favorable sensitivity, the best full-space return rises only to **80%**. Therefore the announced pool-size reduction alone cannot create a guaranteed-profit coverage state.

Status: **REJECTED guaranteed-profit full coverage**.

# H021 forced-distribution / subsidy bound
Files:
- `research/h021_forced_distribution_subsidy_bound.md`
- `src/loto_research/forced_distribution.py`
- `tests/test_forced_distribution.py`
- `data/derived/h021_forced_distribution_screen.csv`

General necessary condition for a full-space/final-draw guarantee:

`B + E > (1-r)S + costs`

where `S` is our spend, `r` the strongest defensible fraction of our own spend available to prizes, `B` guaranteed external subsidy/carryover, and `E` external-player prize contribution that our portfolio is legally guaranteed to capture net of sharing. Ordinary uncertain external sales do **not** count toward a strict guarantee.

## UK Lotto Must-Be-Won — CLOSED
Verified current structure:
- 6/59, £2 per line;
- full space 45,057,474 lines => **£90,114,948** acquisition;
- official procedures: on average 50% of Lotto sales available for prizes; jackpot rolls five times then Must-Be-Won redistribution.

Even using favorable `r=0.50`, full coverage needs **>£45,057,474 guaranteed external subsidy** before sharing/execution just to pass the necessary condition. Must-Be-Won distribution alone does not provide such a hard subsidy/capture guarantee.

Status: **REJECTED as current standalone full-space guarantee**.

## Austrian Lotto + LottoPlus fixed-pool promotion — CLOSED
Verified current/recent structure:
- Lotto base €1.50 per 6/45 tip;
- LottoPlus €0.80 add-on from 6 July 2026, entering two LottoPlus draws;
- published payout shares: Lotto 48%, LottoPlus 45%;
- 2 Aug 2026 promo fixed €500k top-tier money in each LottoPlus draw, €1m total, guaranteed to be distributed.

Full 6/45 coverage requires 8,145,060 tips and at least **€18,733,638** acquisition with LottoPlus. Price-weighted player-funded payout allocation is €1.08 per €2.30 line => **€8,796,664.80** optimistic own-funded return. Takeout hurdle = **€9,936,973.20**. Even granting the entire €1m promotion as external subsidy leaves **-€8,936,973.20** optimistic net before sharing/costs.

Status: **REJECTED as guaranteed-profit full-space promotion**.

# H020 lawful two-sided hedging/arbitrage — advanced but runtime-blocked
Files:
- `research/h020_two_sided_hedging_arbitrage.md`
- `src/loto_research/two_sided_arb.py`
- `src/loto_research/live_complete_set.py`
- `tests/test_two_sided_arb.py`
- `tests/test_live_complete_set.py`
- `data/derived/h020_two_sided_arb_screen.csv`
- `data/derived/h020_fee_aware_pair_thresholds.csv`

For exhaustive mutually-exclusive outcomes with effective decimal odds `O_i`, equal-return dutching is strictly profitable iff `sum_i(1/O_i) < 1` after all costs. For binary complete-set tokens, `YES all-in + NO all-in < $1` is the equivalent gate.

Post-fill deterministic profit mechanism: **VALIDATED**. Fee/depth scanner: **IMPLEMENTED**. Current reproducible pre-trade opportunity: **NOT ESTABLISHED** because arbitrary raw live books remain unavailable in this runtime.

# Other active / blocked branches
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled current/recent instances fail cash-floor/full-cap test.
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
- Beşdə 5 and ONLOTO full coverage: guaranteed losses.
- 4+4 single 5+5/6+6 systems: zero-payout outcomes exist; full-space theorem remains data-blocked.
- H015 anti-crowd standalone: closed as guarantee; useful overlay only.
- H005/H009 ordinary system discounts/random promos/free-play: screened; no terminal deterministic guarantee.
- H011 lawful visible pre-purchase decoder: screened NY/Virginia channels closed.

# Next priorities
1. **Apply H021/H022 fast analytic screens** to additional current finite/final-draw/fixed-payout products; deep-dive only candidates approaching/exceeding 100% deterministic coverage return or whose guaranteed external subsidy can cross takeout.
2. **H020 live-data arbitrage:** resume immediately if direct public raw REST/WebSocket books become available.
3. **H006/H007:** resume only if reliable ordered histories/machine metadata become obtainable.
4. H010/H014 if new authoritative data routes appear.
5. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
6. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.