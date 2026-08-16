# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H039 cash-refund matched-betting contract gate completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H039 — cash-refund / matched-betting guarantee gate
Files:
- `research/h039_cash_refund_matched_betting_gate.md`
- `data/derived/h039_cash_refund_promo_screen.csv`
- `src/loto_research/promo_hedge.py`
- `tests/test_promo_hedge.py`

## Constructive theorem
For a qualifying back bet `S` at odds `O`, an opposing lay stake `L`, and a withdrawable cash refund `R` paid only if the qualifying back bet loses:
- backed outcome wins: `P_win = (S-L)(O-1)` before commission;
- backed outcome loses: `P_lose = -S + L + R`.

If `R=S`, choose `L=S-delta` for any `0<delta<S`:
- `P_win = delta*(O-1) > 0`;
- `P_lose = S-delta > 0`.

Therefore a genuinely unconditional full-cash-refund promo can be mechanically converted into strict positive profit once both hedge legs are irrevocably matched and all costs/settlement branches are covered.

## Live Betfair Azerbaijan offer — mechanism real, strict guarantee BLOCKED
Fresh official page retrieved 2026-08-16 states:
- Azerbaijan is explicitly eligible;
- promo code `EXCN10`;
- first Exchange bet within 30 days must risk at least €10 and settle;
- if it loses, Betfair refunds €10 **in cash**.

However Betfair General/Standard Promotional Terms contain an explicit irregular-play clause: if a promotion enables guaranteed wins/profits with no or minimal risk, Betfair may invalidate transactions, withhold winnings and/or close the account.

Thus the precise hedge that creates mathematical sure profit also creates a contractual clawback branch. Under PROJECT_RULES this prevents terminal SUCCESS.

Status:
- cash-refund matched-betting arbitrage mechanism: **VALIDATED**;
- current Betfair Azerbaijan offer as strict executable guarantee: **REJECTED/BLOCKED by anti-guarantee promo terms**.

## Contract-first gate for future offers
A future matched-promo candidate may qualify for SUCCESS only if:
1. eligibility is deterministic and already satisfied;
2. both hedge legs can be fully matched before event risk;
3. void/settlement mismatch is eliminated or separately hedged;
4. refund is withdrawable cash;
5. refund amount/timing are fixed;
6. no guaranteed-profit / minimal-risk / arbitrage clawback term applies;
7. all commissions, taxes, FX and transfer costs leave every branch positive;
8. no one-sided account/market limit can arise after the first leg is irrevocable.

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
Current OLG page publishes a lottery-only birthday bonus for July 1–December 31 2026.
No qualifying ticket purchase is stated; eligible account opts in and receives lottery-only bonus value.

This is a real **zero-cash-cost free-roll / positive-EV subsidy** for an eligible account, but terminal SUCCESS still fails because downstream lottery bets can all lose.

Compact-conversion route checked:
- POKER LOTTO: Quick Pick hands can all lose;
- LIGHTNING LOTTO: bonus amount cannot fully cover the 5/49 space;
- MEGADICE: losing outcomes remain.

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

Matched adjacent promotion-demand uplift mean ≈ **1.3766x (+37.7%)**; median ≈ **1.4115x**.

Gamma-Poisson posterior:
- posterior common-rate mean = **82.75 raffle winners**;
- 95% posterior interval for common mean ≈ **75.63–90.19**;
- implied posterior-mean participation ≈ **827,500 Plus lines**;
- model-conditional predictive `P(next event >=170 winners) ≈ 1.7e-14`.

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
1. **Contract-first cash-refund scan:** search other current cash-refund/cashback offers, prioritizing operators whose terms do NOT claw back guaranteed/minimal-risk play; H039 mechanical hedge theorem is ready.
2. **Zero-cost-credit conversion scan:** only pursue credits large enough to completely cover a tiny outcome space with positive withdrawable cash floor.
3. H037: recover remaining event count(s), broaden controls, and recompute after autumn-2026 rule change.
4. H020 live arbitrage immediately if raw public order books become retrievable.
5. H019 only when capped-entry cash-floor economics materially improve.
6. H006/H007 only after reliable histories/machine metadata become obtainable.
7. H010/H014 if new authoritative data routes appear.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`; newest authoritative research note: `research/h039_cash_refund_matched_betting_gate.md`.
