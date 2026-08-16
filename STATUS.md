# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H038 deterministic rebate/free-credit theorem completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H038 — deterministic rebate / lottery-credit guarantee screen
Files:
- `research/h038_deterministic_rebate_guarantee.md`
- `data/derived/h038_rebate_promo_screen.csv`
- `src/loto_research/rebate_guarantee.py`
- `tests/test_rebate_guarantee.py`

## General theorem
For cash spend `S`, minimum portfolio cash payout `m`, guaranteed withdrawable cash rebate `R`, and execution costs `C`, strict guaranteed profit requires:

`m + R > S + C`.

If a purchased lottery portfolio can pay zero cash, a true cash rebate must exceed 100% of qualifying spend plus costs to create a standalone strict guarantee.

Lottery credit/free play is different: if it must be wagered on a product with a legal zero-cash outcome, its strict cash floor is zero regardless of face value.

## Current OLG buy-one-get-one offers — CLOSED as guarantees
Official current selected-account offers run June 22 2026–March 31 2027:
- LOTTO MAX: spend CAD 6 → CAD 6 LOTTO MAX Bonus;
- LOTTO 6/49: spend CAD 3 → CAD 3 LOTTO 6/49 Bonus.

OLG defines the bonus as lottery-specific/notional funds rather than withdrawable cash at award. Both original and bonus tickets retain legal zero-cash outcomes.

Strict package floors:
- LOTTO MAX promo: **-CAD 6** net;
- LOTTO 6/49 promo: **-CAD 3** net.

Status: **REJECTED as strict cash guarantees; EV subsidy only**.

## Strongest zero-cost subsidy found — OLG birthday bonus
Current OLG page publishes a **CAD 10 Lottery Bonus Birthday Gift** for July 1–December 31 2026.
No qualifying ticket purchase is stated; eligible account opts in and receives CAD 10 lottery-only bonus.

This is a real **zero-cash-cost free-roll / positive-EV subsidy** for an eligible account, but terminal SUCCESS still fails because downstream lottery bets can all lose.

Compact-conversion route checked:
- POKER LOTTO: CAD 2 Quick Pick hands; five bonus-funded hands can all lose;
- LIGHTNING LOTTO: CAD 2 gives three 5/49 selections; CAD 10 buys only 15 selections, nowhere near full coverage;
- MEGADICE: Quick Pick with losing outcomes.

No ≤CAD10 fully coverable current OLG product with positive cash floor was found in this screen.

Status: **positive-EV/free-roll overlay validated; strict positive-profit guarantee not established**.

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

## Bayesian predictive screen
For the six event counts:
- posterior common-rate mean = **82.75 raffle winners**;
- 95% posterior interval for common mean ≈ **75.63–90.19**;
- implied posterior-mean participation ≈ **827,500 Plus lines**;
- common-rate posterior predictive `P(next event >=170 winners) ≈ 1.7e-14`.

This remains model-conditional, not a guarantee.

Status: **strongest live +EV lottery overlay currently found; NOT terminal SUCCESS**.

# Recently closed branches
- H036 Daily Million Plus / EuroMillions Plus: full coverage strongly negative; OLG targeted bonus is real but lottery-credit, not cash guarantee.
- H035 Lotterywest Super66/Cash 3: rejected.
- H034 Ontario DAILY KENO Pick 2–10: rejected.
- H033 New Zealand Bullseye: discount real, strict guarantee rejected.
- H032 Canada DAILY GRAND: rejected.
- H031 Cash Pop Cover All: guaranteed win but insufficient floor.
- H029/H029b Virginia Pick 3/4/5 including FIREBALL: rejected.
- H030 Virginia Cash 5 + EZ Match: rejected.
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
1. **Zero-cost-credit conversion scan:** search current promotions/free-entry mechanisms where a deterministic free credit can completely cover a tiny outcome space and force positive withdrawable cash.
2. **True withdrawable cashback scan:** prioritize rebates paid as cash/withdrawable balance rather than free play; apply H038 theorem immediately.
3. H037: recover remaining event count(s), broaden controls, and recompute after autumn-2026 rule change.
4. H020 live arbitrage immediately if raw public order books become retrievable.
5. H019 only when capped-entry cash-floor economics materially improve.
6. H006/H007 only after reliable histories/machine metadata become obtainable.
7. H010/H014 if new authoritative data routes appear.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`; H038 authoritative note: `research/h038_deterministic_rebate_guarantee.md`.
