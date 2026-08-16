# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H037 event-day calibration materially strengthened**

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
- raffle numbers are assigned rather than chosen, so deterministic code coverage cannot be forced;
- all tickets with the winning raffle number enter a second random draw and one ticket owner gets the extra €1m;
- external qualifying tickets preserve a legal outcome where another player receives it.

Status: **REJECTED as strictly guaranteed-profit strategy**.

## Positive-EV overlay — materially strengthened by actual special-event data
Pre-autumn-2026 6/47 Plus package baseline remains approximately:
- Plus 1 fixed-prize EV: **€0.22902755/line**;
- Plus 2 fixed-prize EV: **€0.13263705/line**;
- normal €500 raffle EV: **€0.05/line**;
- ordinary Plus package EV: **€0.41166460 per €1 Plus add-on**.

Special €1m subsidy break-even is approximately **1,699,711 eligible Plus lines**, equivalent to about **170 ordinary raffle winners** at 1/10,000 odds.

Actual special-event calibration recovered:
- **5 Jul 2025:** 104 raffle-winning ticketholders => MLE ≈ **1.04m Plus lines**; exact-Poisson 95% implied interval ≈ **0.850m–1.260m**. Even at the upper bound, modeled Plus EV ≈ **€1.205 per €1 add-on**.
- **6 Sep 2025:** 81 raffle-winning ticketholders => MLE ≈ **0.81m Plus lines**; 95% implied interval ≈ **0.643m–1.007m**. At the upper bound, modeled Plus EV ≈ **€1.405 per €1 add-on**.

Both observed special-event counts are far below the ~170-winner break-even proxy. This is stronger than the prior generic 60–120 ordinary-draw statement because it directly samples promotion days.

Official promotion language also confirms **one four-digit raffle number per Lotto Plus line**. The final €1m stage is described in ticket/ticket-owner terms, so multi-line ticket handling still needs operative-rule confirmation before execution sizing.

Status: **strong live +EV overlay lead; NOT terminal SUCCESS because individual outcomes remain random**.

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
1. **H037 completion/calibration:** recover additional exact special-event counts (21 Dec 2024, 28 Sep 2024, 20 Dec 2025, 14 Mar 2026, 30 May 2026) and adjacent ordinary-draw counts; build predictive distribution for event-day Plus participation and promotion uplift.
2. Recompute H037 after autumn-2026 Lotto/Lotto Plus regime change once operative tables/prices are published/effective.
3. Continue deterministic subsidy/rebate scan, prioritizing **uncapped, repeatable, withdrawable cash** rather than lottery-only credit.
4. Revisit H020 live arbitrage immediately if raw public order books become retrievable.
5. H019 only when capped-entry cash-floor economics materially improve.
6. H006/H007 only after reliable histories/machine metadata become obtainable.
7. H010/H014 if new authoritative data routes appear.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. The H037 authoritative packet and `data/derived/h037_event_calibration.csv` contain this run's new evidence. The connector cannot safely replace the oversized ledger without risking truncation; preserve the ledger unchanged and merge this H037 packet into it on the next safe compaction/update path.
