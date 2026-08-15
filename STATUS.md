# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural-edge search; cross-jurisdiction/shared-jackpot differences**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# NEW — H002b EuroMillions cap/rolldown guarantee path completed
Files:
- `research/h002b_euromillions_cap_rolldown.md`
- `src/loto_research/euromillions_coverage.py`
- `tests/test_euromillions_coverage.py`

## Current primary-rule anchors
Checked current operator material:
- Spain: 5/50 + 2/12, €2.50/simple bet, 50% of collection allocated to prizes, jackpot range €17m–€250m.
- FDJ 2026: €250m maximum; capped jackpot can be reoffered and on the terminal capped draw an unclaimed jackpot is redistributed to lower winning ranks.

## Exact full-space economics
Full combination space:

`C(50,5) * C(12,2) = 139,838,160` lines.

At €2.50/line:

**full-space cost = €349,595,400**.

Exact covered winner counts for every possible draw include:
- 5+2: 1
- 5+1: 20
- 5+0: 45
- 4+2: 225
- 4+1: 4,500
- 3+2: 9,900
- 4+0: 10,125
- 2+2: 141,900
- 3+1: 198,000
- 3+0: 445,500
- 1+2: 744,975
- 2+1: 2,838,000
- 2+0: 6,385,500.

The €250m jackpot cap is **€99.5954m below** full-space acquisition cost even before sharing/execution.

## Decisive H002b theorem
The terminal cap rolldown requires **no 5+2 jackpot winner**.

Complete coverage necessarily contains the realized 5+2 combination, hence guarantees at least one jackpot winner and therefore **prevents the rolldown condition itself**.

So the seemingly attractive construction “buy the whole space on the final €250m cap draw and collect the lower-tier rolldown” is logically impossible: buying the whole space stops the rolldown from occurring.

Partial coverage restores the possibility of no jackpot winner but also restores uncovered draw outcomes, so it cannot by itself satisfy an all-outcome profit guarantee. Shared-pool dilution by external winning tickets remains an additional obstruction with no useful pre-draw hard cap.

H002b terminal guaranteed-profit status: **REJECTED**.
EuroMillions cap/rolldown remains potentially useful only for EV/share optimization, not terminal guarantee.

# Previously closed / blocked highlights
- Powerball full-space guarantee: REJECTED because external jackpot sharing is not bounded by a useful pre-draw cap.
- Mega Millions full-space guarantee: REJECTED; $5 full space ~$1.452bn and sharing/random multiplier obstruct strict guarantee.
- H012a/H004 ordinary additive wheels: CLOSED by expectation theorem.
- Beşdə 5 and ONLOTO full coverage: guaranteed losses.
- 4+4 single 5+5/6+6 systems: zero-payout outcomes exist; full-space exact theorem remains data-blocked.
- H015 anti-crowd standalone: CLOSED as guarantee; useful overlay only.
- H005/H009 ordinary system discounts/random promos/free-play: screened; no terminal deterministic guarantee found.
- H010 Poz-Qazan remaining-state and H014 4+4 carryover: data-blocked.
- Cash WinFall: historical +EV mechanism validated, not current terminal guarantee.

# Next priorities
1. **H008 cross-jurisdiction EuroMillions** — same common jackpot, different ticket price, national raffle add-ons, taxes, claim rules and access constraints; screen for lawful valuation/arbitrage differences.
2. H012 finite/final-draw states only where accumulated guaranteed pools/subsidies break ordinary economics.
3. H006/H007 randomness branches after reliable histories are collected.
4. Advanced remaining classes before EXHAUSTED.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
