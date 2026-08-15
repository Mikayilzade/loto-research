# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H018 guarantee closed, H007 data acquisition / RNG controls next**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# NEW — H018 Virginia Lucky Contestant completed for terminal-guarantee question
Files:
- `research/h018_lucky_contestant_time_state.md`
- `src/loto_research/lucky_contestant_time_state.py`
- `tests/test_lucky_contestant_time_state.py`
- `data/derived/h018_optimistic_time_state_screen.csv`

## Validated mechanism
Virginia Lottery publicly defines a genuine hidden time-state process:
- hidden daily selected time from published weighted intervals;
- 60m before selected time: jackpot odds **1 in 150,000**;
- 30m before: **1 in 30,000**;
- at selected time: **1 in 1**;
- jackpot can also be won earlier at standard odds;
- plays cost $0.20–$30.

This is a causal nonstationary-odds mechanism, not hot/cold-number folklore.

## Bayesian/survival screen
Using an explicit uniform-within-published-bin assumption and the deliberately optimistic information bound `T >= now`, remaining selected-time mass becomes highly concentrated late in the day. Example:
- at 22:00: ~28.57% of remaining T mass lies in next 30m;
- at 22:30: 40%;
- at 23:00: 66.67% in next 30m and 100% in next 60m;
- at 23:15: all remaining prior mass is inside the next 30m.

This keeps H018 interesting as a future **conditional-EV** overlay if exact operator mechanics/live-state data can be recovered.

## Jackpot-only threshold
For representative $600 jackpot:
- $0.20 stake needs jackpot probability >= **1/3000** from jackpot alone;
- published 30m anchor `1/30,000` contributes only about $0.02 jackpot EV;
- selected time is 1/1, but T is hidden and exact interpolation/time resolution are unpublished.

## H018 terminal result
The official rules explicitly allow another player to win the jackpot **before hidden T at standard odds**. Ordinary play has losing outcomes (overall win odds 1 in 3.83). Therefore there is a legal branch where the target jackpot is unavailable and our positive-cost play loses.

**H018 standalone guaranteed-profit path: REJECTED.**

Public winner-list HTML also showed two distinct jackpot events on Jan 4, 2026 in a small deduplicated sample, so simple one-award-per-day/reset assumptions are unsafe without further rule text.

H018 remains parked only as an EV/data-acquisition lead.

# NEW — H007 high-frequency RNG source discovery started
File:
- `research/h007_rng_source_discovery.md`

Official current mechanisms confirmed:
- **Ekspres Keno:** 80-number pool, 20 drawn, every 5 minutes; public archive UI exists.
- **ONLOTO:** 50 balls, 36 drawn, every 3 minutes.
- **Şanslı 6:** 48-number pool, 35 drawn; random Lucky Clover positions and a random x1.5/x2 multiplier stream; operator states multiplier is active on average about **170 draws/day**.

These provide legitimate high-frequency random streams for H007, especially cross-stream tests on Şanslı 6.

Current blocker: the public Ekspres Keno archive is client-rendered and current retrieval exposes `undefined/NaN` placeholders rather than a reproducible bulk draw payload. No trustworthy machine-readable bulk endpoint was recovered in this packet.

H007 status: **OPEN / DATA-GATED**. Do not run anomaly fishing until ordered, timestamped, consecutive official history is acquired.

# Previously closed / blocked highlights
- Cash WinFall: historical +EV mechanism validated, not current terminal guarantee.
- Powerball full-space guarantee: REJECTED because external jackpot sharing is not bounded by a useful pre-draw cap.
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
- H018 hidden-time mechanism: standalone guarantee closed; conditional EV data path remains.

# Next priorities
1. **H007 data acquisition:** recover a reproducible official or independently verifiable bulk history for Ekspres Keno / Şanslı 6 / ONLOTO, including ordered outputs and timestamps; then run preregistered train/holdout RNG tests.
2. **H006 physical draw bias:** only with machine/ball-set metadata or enough regime-labelled history for causal change-point testing.
3. **H012 additional finite/final-draw states:** only where deterministic accumulated pool/subsidy can exceed full acquisition cost.
4. **Lawful two-sided hedging/arbitrage:** search only structures where both sides can be locked before outcome and all fees/limits are explicit.
5. H010/H014 when new authoritative data routes become available.
6. H018 conditional-EV calibration if exact odds interpolation, T resolution, reset mechanics or live endpoint become recoverable.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
