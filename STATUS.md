# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H037 six-event predictive calibration completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H037 — Irish Lotto Plus Million Euro Raffle
Files:
- `research/h037_lotto_plus_million_raffle.md`
- `data/derived/h037_lotto_plus_million_raffle_screen.csv`
- `data/derived/h037_event_calibration.csv`
- `src/loto_research/lotto_plus_raffle.py`
- `tests/test_lotto_plus_raffle.py`

## Strict guarantee — CLOSED
Published mechanics still defeat terminal guarantee:
- raffle numbers are assigned rather than chosen;
- all tickets with the winning raffle number enter a second random draw and one ticket owner gets the extra €1m;
- external qualifying tickets preserve a legal outcome where another player receives it.

Status: **REJECTED as strictly guaranteed-profit strategy**.

## Positive-EV overlay — substantially strengthened
Pre-autumn-2026 6/47 Plus-package baseline remains approximately **€0.41166460 expected payout per €1 Plus add-on** before the special million subsidy.

Break-even special-event participation remains about:
- **1,699,711 eligible Plus lines**, or
- **169.97 expected ordinary raffle winners** at 1/10,000 per line.

Six recovered special-event raffle-winner counts:
- 28 Sep 2024: **73**;
- 5 Jul 2025: **104**;
- 6 Sep 2025: **81**;
- 20 Dec 2025: **82**;
- 14 Mar 2026: **84**;
- 30 May 2026: **72**.

For every one of these six events, the exact-Poisson **95% upper implied Plus-line bound is still below 1.6997m break-even**. Modeled Plus EV at each event's 95% upper participation bound remains approximately **€1.205–€1.515 per €1 add-on**.

## Matched promotion-demand uplift
Adjacent ordinary Wednesday raffle-winner counts were recovered around all six events. Event / mean-adjacent ratios:
- 1.377x, 1.434x, 1.473x, 1.147x, 1.388x, 1.440x.

Mean promotion uplift ≈ **1.3766x (+37.7%)**; median ≈ **1.4115x**.

Interpretation: promotion-day demand does rise materially, but observed event demand remains far below the pre-change break-even threshold.

## Bayesian predictive screen
A transparent Gamma-Poisson helper is now implemented and tested.

For the six event counts:
- posterior common-rate mean = **82.75 raffle winners**;
- 95% posterior interval for common mean ≈ **75.63–90.19**;
- implied posterior-mean participation ≈ **827,500 Plus lines**;
- common-rate posterior predictive `P(next event >=170 winners) ≈ 1.7e-14`.

This is **model-conditional, not a guarantee**. Regime change, overdispersion, pricing/marketing changes and autumn-2026 Lotto changes can invalidate it.

Status: **strongest live +EV lottery overlay currently found; NOT terminal SUCCESS**.

# Recently closed branches
- H036 Daily Million Plus / EuroMillions Plus: full coverage strongly negative; OLG targeted bonus is real but capped/lottery-credit, not cash guarantee.
- H035 Lotterywest Super66/Cash 3: 54.35% / 36.36% coverage floors; rejected.
- H034 Ontario DAILY KENO Pick 2–10: favorable uncapped return only 42.03%–55.07%; rejected.
- H033 New Zealand Bullseye: real 28.57% multi-draw discount, but shared/capped payouts destroy strict guarantee.
- H032 Canada DAILY GRAND: favorable full coverage 44.35%, strict cash floor 36.21%.
- H031 Georgia/Virginia Cash Pop Cover All: guaranteed win but floor 33.33% of coverage cost.
- H029/H029b Virginia Pick 3/4/5 including FIREBALL: additive-family guarantee rejected.
- H030 Virginia Cash 5 + EZ Match: full-space route negative; sharing blocks strict guarantee.
- H021–H028 compact/fixed/full-space screens: sampled products rejected.
- Beşdə 5 and ONLOTO 1–10 full coverage: rejected.
- Powerball/Mega Millions/EuroMillions main-game terminal guarantees: rejected.
- H012a/H004 ordinary additive wheels: rejected by expectation theorem.
- H015 anti-crowd standalone: rejected as guarantee; overlay only.

# Other active / blocked branches
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; raw live-book acquisition remains runtime/data blocked.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Next priorities
1. **Deterministic subsidy/rebate scan:** prioritize uncapped, repeatable, withdrawable cash or guaranteed-value rebate mechanisms; H037 is +EV but cannot meet guarantee criterion.
2. H037: recover 21 Dec 2024 underlying €500 raffle-winner count; expand ordinary matched controls; fit overdispersed/hierarchical event-demand model.
3. H037: recompute immediately after autumn-2026 Lotto/Lotto Plus regime change becomes operative.
4. Revisit H020 live arbitrage immediately if raw public order books become retrievable.
5. H019 only when capped-entry cash-floor economics materially improve.
6. H006/H007 only after reliable histories/machine metadata become obtainable.
7. H010/H014 if new authoritative data routes appear.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. H037 authoritative evidence is in `research/h037_lotto_plus_million_raffle.md` and `data/derived/h037_event_calibration.csv`.
