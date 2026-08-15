# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H007 data-gated, H019 capped fixed-prize takeover screened**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# NEW — H019 capped fixed-prize competition saturation
Files:
- `research/h019_capped_fixed_prize_saturation.md`
- `src/loto_research/capped_competition.py`
- `data/derived/h019_capped_competition_screen.csv`

## Mechanism theorem
A one-winner capped competition can in principle become a deterministic buy-all opportunity only if one entrant can own **every valid entry** and the guaranteed cash floor exceeds total acquisition cost.

Strict necessary conditions include:
- zero already-owned external entries;
- no personal cap below the full entry pool;
- atomic acquisition/closure so a competing entry cannot enter during execution;
- no unresolved free/bonus entry channel;
- guaranteed fixed cash prize not reduced for undersell;
- `cash prize > max_entries × effective entry price + all costs`;
- eligibility/claim/cancellation terms cannot create a loss branch.

Buying merely the **remaining** tickets is not a guarantee if anyone else already owns a valid entry.

## Fresh market screen
A current/recent UK capped-competition sample was screened across Coast Competitions, Hot Comps, 7days Performance, Urban Draw and UKCC.

Cash-alternative / full-cap ticket-revenue ratios were approximately **28.6%–53.3%**, all below break-even even before fees. Strongest sampled ratio was a 7days Audi RS3 competition at about **53.33%** (£40,000 cash vs £74,999.75 full-cap ticket cost). Most examples also had entrant-specific caps and/or free postal entry routes.

A useful historical Coast page independently demonstrates guaranteed undersold draws (148/300 sold), but its £280 cash alternative versus £597 full-cap cost still makes full takeover a deterministic loss.

Status: **H019 not SUCCESS; ordinary capped fixed-prize takeover currently rejected by economics/entry-exclusivity filters.** Re-open only when a live candidate satisfies `guaranteed cash floor > total maximum-entry acquisition cost` or a deterministic subsidy pushes effective cost below that floor.

# H007 high-frequency RNG — still data-gated
File: `research/h007_rng_source_discovery.md`.

Official current mechanisms remain confirmed:
- Ekspres Keno: 80-number pool, 20 drawn, every 5 minutes; public archive UI exists.
- ONLOTO: 50 balls, 36 drawn, every 3 minutes.
- Şanslı 6: 48-number pool, 35 drawn plus random Clover positions and random x1.5/x2 multiplier stream.

Fresh search again did not recover a trustworthy machine-readable bulk official history. The public Ekspres Keno archive remains client-rendered with `undefined/NaN` placeholders in retrievable output. Do not run anomaly fishing until ordered timestamped consecutive history exists.

# H018 Virginia Lucky Contestant
Standalone guaranteed-profit path remains **REJECTED** because another player may win the jackpot before hidden selected time and ordinary paid play retains losing outcomes. Conditional-EV calibration remains data-gated.

# Previously closed / blocked highlights
- Cash WinFall: historical +EV mechanism validated, not current terminal guarantee.
- Powerball full-space guarantee: REJECTED because external jackpot sharing has no useful pre-draw cap.
- Mega Millions full-space guarantee: REJECTED; cost/sharing/random multiplier obstruct strict guarantee.
- EuroMillions terminal-cap full coverage: REJECTED because coverage itself prevents no-winner rolldown.
- H008 cross-jurisdiction: EV differences validated; standalone guarantee rejected.
- H012a/H004 ordinary additive wheels: CLOSED by expectation theorem.
- Beşdə 5 and ONLOTO full coverage: guaranteed losses.
- 4+4 single 5+5/6+6 systems: zero-payout outcomes exist; full-space theorem remains data-blocked.
- H015 anti-crowd standalone: CLOSED as guarantee; useful overlay only.
- H005/H009 ordinary system discounts/random promos/free-play: screened; no terminal deterministic guarantee found.
- H010 Poz-Qazan remaining-state and H014 4+4 carryover: data-blocked.
- H011 lawful visible pre-purchase decoder: screened NY/Virginia channels closed.

# Next priorities
1. **Lawful two-sided hedging/arbitrage:** identify structures where mutually exclusive sides can both be locked before outcome with explicit fees/limits and a positive minimum payoff.
2. **H012 additional finite/final-draw states:** only candidates where a deterministic accumulated pool/subsidy can exceed full acquisition cost.
3. **H006/H007:** resume only if reliable ordered histories / machine metadata become obtainable.
4. **H019 monitor condition:** re-open only on a numerical trigger `cash floor > full effective cap cost`, not generic raffle browsing.
5. H010/H014 if new authoritative data routes appear.
6. H018 conditional-EV calibration if exact odds interpolation/live-state mechanics become recoverable.
7. Advanced controls before EXHAUSTED: additional current products, Bayesian hidden-state inference and causal implementation tests.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
