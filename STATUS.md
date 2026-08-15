# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H023 UK fixed-prize full-space screen completed for Set For Life and Thunderball**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H023 UK fixed-prize full coverage — NEW
File:
- `research/h023_uk_fixed_prize_full_coverage.md`

## Set For Life — CLOSED
Current structure verified from National Lottery: 5/47 + 1 Life Ball/10, £1.50 per line, fixed lower tiers plus £10,000/month for 30 years top prize.

Full space = `C(47,5)*10 = 15,339,390` lines.
Acquisition cost = **£23,009,085**.

Because every line is owned, winner counts by main-number matches and Life Ball status are deterministic for every draw. Even valuing the full top annuity at its undiscounted nominal **£3.6m** and the second tier at £120k, deterministic nominal gross is only **£12,949,100** = **56.2782%** of cost.

Guaranteed nominal loss before execution = **-£10,059,985**. The real guarantee is weaker because top-prize rules contain a capped-prize mechanism for multiple winners.

Status: **REJECTED guaranteed-profit full coverage**.

## Thunderball — CLOSED
Current structure verified from National Lottery: 5/39 + 1 Thunderball/14, £1 per line, published fixed prizes from £3 to £500,000; top prize is not shared.

Full space = `C(39,5)*14 = 8,060,598` lines.
Deterministic full-space gross = **£4,262,568**.
Return = **52.8815%**.
Guaranteed loss before execution = **-£3,798,030**.

Status: **REJECTED guaranteed-profit full coverage**.

# H022 fixed-payout subset coverage
Files:
- `research/h022_irish_54321_full_coverage.md`
- `src/loto_research/fixed_subset_coverage.py`
- `tests/test_fixed_subset_coverage.py`
- `data/derived/h022_irish_54321_full_coverage.csv`

Generic identity: in an all-selected-numbers-must-hit game, if the universe has N numbers, the realized winning target has d numbers and we buy every k-subset, then exactly `C(d,k)` of our `C(N,k)` entries win for every legal outcome. Full-space return is deterministic.

Irish Lotto 5-4-3-2-1 current 47-ball full-space returns remain only **48.89%–76.60%**; announced 45-ball sensitivity with today's payouts still maxes at **80%**. Closed.

# H021 forced-distribution / subsidy bound
General necessary condition for a full-space/final-draw guarantee:

`B + E > (1-r)S + costs`

where `S` is our spend, `r` the strongest defensible fraction of our own spend available to prizes, `B` guaranteed external subsidy/carryover, and `E` external-player prize contribution that our portfolio is legally guaranteed to capture net of sharing.

UK Lotto Must-Be-Won and Austrian Lotto+LottoPlus fixed-pool promotion are already closed by this bound.

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
1. Continue **H021/H022/H023 fast analytic screens** on additional current finite/final-draw/fixed-payout products; deep-dive only candidates approaching/exceeding 100% deterministic coverage return or with guaranteed external subsidy sufficient to cross takeout.
2. **H020 live-data arbitrage:** resume immediately if direct public raw REST/WebSocket books become available.
3. **H006/H007:** resume only if reliable ordered histories/machine metadata become obtainable.
4. H010/H014 if new authoritative data routes appear.
5. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
6. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.