# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H020 two-sided arbitrage mechanism validated, live executable candidate still missing**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# NEW — H020 lawful two-sided hedging/arbitrage
Files:
- `research/h020_two_sided_hedging_arbitrage.md`
- `src/loto_research/two_sided_arb.py`
- `tests/test_two_sided_arb.py`
- `data/derived/h020_two_sided_arb_screen.csv`

## Main theorem
For exhaustive mutually-exclusive outcomes with effective decimal odds `O_i`, equal-return dutching is strictly profitable iff:

`sum_i(1/O_i) < 1`

after all commissions/taxes/costs.

For binary complete-set token markets, the equivalent gate is:

`Yes all-in cost + No all-in cost < $1 guaranteed redemption/merge value`.

## Mechanism validation
Smarkets' official documentation explicitly describes bookmaker/exchange arbitrage and gives back-to-lay examples where both outcome branches have equal positive profit. Reproduced published-style example:
- back 2.20, stake £200;
- lay 1.98, 2% exchange commission;
- equalizing lay stake ≈ £224.4898;
- profit = **£20 on either branch** after both legs are accepted.

This proves the mechanism class: **post-fill deterministic profit is real**.

## Why not SUCCESS yet
The cited odds are educational examples, not a live executable opportunity. Before both legs are fully matched, price movement, partial fills, bookmaker limits/rejection, liquidity, incompatible void/dead-heat rules, eligibility/geography, taxes and settlement mismatch can break the pre-trade guarantee.

Therefore H020 distinction:
- post-fill guarantee: **VALIDATED**;
- current repeatable pre-trade executable guarantee: **NOT YET ESTABLISHED**.

## Same-venue structural screens
### Kalshi
Official mechanics state opposing Yes/No participant investments combine to `$1`; fees are then charged. Buying both sides of one ordinary binary market therefore has no structural positive complete-set subsidy. Collateral return improves capital efficiency but does not increase payout.

Status: **same-market buy-both structural arb rejected; cross-market/live discrepancies remain conditional only**.

### Polymarket
Official CTF mechanics state `$1 pUSD -> 1 Yes + 1 No`, and equal Yes/No pairs merge back to `$1`. Thus a pair acquired below `$1` all-in would be deterministic arbitrage, but split/merge itself anchors the complete set to `$1`; fees/gas only worsen a non-crossed book. Negative-risk conversion is capital-efficient, not a payout subsidy.

Status: **complete-set arb condition validated; no structural same-market profit; live crossed-book opportunities require real-time screening**.

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
1. **H020 live-data arbitrage acquisition gate:** search public venues/APIs for a current price pair where all legs, fees and settlement definitions can be verified; avoid declaring SUCCESS until both-side executable conditions are proven.
2. **H012 additional finite/final-draw states:** only products where deterministic accumulated pool/subsidy can exceed full acquisition cost.
3. **H006/H007:** resume only if reliable ordered histories/machine metadata become obtainable.
4. H010/H014 if new authoritative data routes appear.
5. H018 conditional-EV calibration if exact operator mechanics/live endpoint become recoverable.
6. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
