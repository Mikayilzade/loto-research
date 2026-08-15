# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H020 post-fill arbitrage validated and fee/depth scanner implemented, but direct live executable quote acquisition is runtime-blocked**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H020 lawful two-sided hedging/arbitrage — advanced
Files:
- `research/h020_two_sided_hedging_arbitrage.md`
- `src/loto_research/two_sided_arb.py`
- `src/loto_research/live_complete_set.py`
- `tests/test_two_sided_arb.py`
- `tests/test_live_complete_set.py`
- `data/derived/h020_two_sided_arb_screen.csv`
- `data/derived/h020_fee_aware_pair_thresholds.csv`

## Mechanism
For exhaustive mutually-exclusive outcomes with effective decimal odds `O_i`, equal-return dutching is strictly profitable iff `sum_i(1/O_i) < 1` after all costs. For binary complete-set tokens, `YES all-in + NO all-in < $1` is the equivalent gate.

Smarkets official examples still validate genuine equal positive profit after both hedge legs are accepted. Kalshi/Polymarket same-market complete-set mechanics do not provide a structural subsidy.

## NEW — live acquisition math is no longer the blocker
Current official Polymarket documentation exposes:
- public active-market discovery and token IDs;
- public full orderbooks;
- per-market fee parameters;
- taker fee formula `C * feeRate * p * (1-p)`.

`live_complete_set.py` now:
- walks executable ask depth;
- includes per-level taker fees and external costs;
- finds the largest profitable complete-set quantity at orderbook breakpoints;
- models Kalshi bid-only YES/NO complement arithmetic.

Important screening result at prices near 0.50/0.50: raw YES+NO asks must be below roughly 0.985 for 3% fee rate, 0.980 for 4%, 0.975 for 5%, and 0.965 for 7%, before builder/gas/FX costs. Thus many apparent `<1` crosses are false positives after fees.

This runtime could verify current official API interfaces but could not retrieve arbitrary raw live Gamma/CLOB payloads through its network path. No current quote is fabricated. H020 is therefore **execution/data-access blocked in this environment, not modeling blocked**.

Status:
- post-fill deterministic profit mechanism: **VALIDATED**;
- fee/depth execution filter: **IMPLEMENTED**;
- current reproducible pre-trade opportunity: **NOT ESTABLISHED**.

# H019 capped fixed-prize competition saturation
A one-winner capped competition can be deterministic only if one entrant owns every valid entry, no external/free entry can survive, closure is atomic, and guaranteed cash floor exceeds full acquisition cost plus all costs. Current/recent UK sample cash-floor/full-cap ratios were only ~28.6%–53.3%; no SUCCESS.

# H007 high-frequency RNG — data-gated
Official mechanisms for Ekspres Keno, ONLOTO and Şanslı 6 remain confirmed, but no trustworthy ordered bulk official history has been recovered. Do not anomaly-fish incomplete data.

# H018 Virginia Lucky Contestant
Standalone guarantee rejected because another player may win before hidden selected time and ordinary paid play retains losing outcomes. Conditional-EV work remains data-gated.

# Previously closed / blocked highlights
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
- H010 Poz-Qazan remaining-state and H014 4+4 carryover: data-blocked.
- H011 lawful visible pre-purchase decoder: screened NY/Virginia channels closed.

# Next priorities
1. **H012 additional finite/final-draw states:** search current products only where deterministic accumulated pools, final-draw forced distribution, fixed cash floors, or external subsidies could exceed complete acquisition cost.
2. **H020 live-data arbitrage:** resume immediately if a runtime gains direct public REST/WebSocket access; scanner is ready and should require real fillable depth + exact fee/settlement compatibility.
3. **H006/H007:** resume only if reliable ordered histories/machine metadata become obtainable.
4. H010/H014 if new authoritative data routes appear.
5. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
6. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
