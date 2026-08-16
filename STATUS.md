# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H040 cash-refund operator screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H040 — expanded cash-refund contract screen
Files:
- `research/h040_cash_refund_operator_scan.md`
- `data/derived/h040_cash_refund_contract_screen.csv`
- `src/loto_research/promo_hedge.py`
- `tests/test_promo_hedge.py`

## New selective-refund theorem
For a bookmaker back stake `S` at odds `O_b`, exchange lay stake `x` at lay odds `O_l`, and exchange commission `c`, if even one legal losing state receives **no refund**:

- win branch: `S*(O_b-1) - x*(O_l-1)`;
- non-refunded loss branch: `-S + x*(1-c)`;
- refunded loss branch: non-refunded branch + cash refund.

A strict positive all-outcome floor therefore requires simultaneously:

`x > S/(1-c)`

and

`x < S*(O_b-1)/(O_l-1)`.

Such an `x` exists iff:

`(O_b-1)*(1-c) > (O_l-1)`.

That is already an ordinary bookmaker/exchange price arbitrage **before counting the promotion**.

Conclusion: selected-place horse-racing money-back offers can improve EV/downside but cannot manufacture a surebet while any non-refunded losing finish remains.

## Current operator screen
- **bet365**: Azerbaijan-facing general terms explicitly prohibit arbitrage / all-outcome guaranteed-profit betting; promo value may be reclaimed. **REJECTED contract gate.**
- **Paddy Power**: genuine Money Back as Cash first-bet offer exists for UK/ROI new customers, but irregular-play terms permit invalidation/withholding when promotion enables guaranteed/minimal-risk profit. **REJECTED contract/access gate.**
- **Sky Bet**: current Money Back as Cash racing offers refund only selected finishing positions. Mechanical guarantee therefore fails by the theorem above. General promo terms are notable because they exclude no/limited-risk play **except where absence of risk is explicitly a key part of the promotion**; retain this wording as a future lead. **Current offer REJECTED.**
- **BetVictor**: First Bet Shield returns Free Bets, not withdrawable cash. **REJECTED refund-form gate.**
- **BetMGM**: losing first bet returns nonwithdrawable Bonus Bets. **REJECTED refund-form/access gate.**
- **FanDuel**: No-Sweat/Bet Back refunds are nonwithdrawable Bonus Bets and jurisdiction-restricted. **REJECTED refund-form/access gate.**

## H039/H040 strategic conclusion
The constructive full-cash-refund hedge remains mathematically valid, but the viable live target is now much narrower:
1. refund must cover **every losing outcome**;
2. refund must be **withdrawable cash**;
3. eligibility must be deterministic and lawful for the user;
4. both hedge legs must be irrevocably executable;
5. terms must explicitly permit the low-risk construction or omit any guaranteed-profit/arbitrage clawback;
6. commissions/tax/FX/settlement mismatches must leave every branch positive.

No currently verified offer in the expanded screen passes all gates.

# Strongest non-terminal positive-EV result
## H037 Irish Lotto Plus Million Euro Raffle
Six recovered special-event raffle-winner counts remain far below the modeled break-even participation threshold. Gamma-Poisson posterior and event-day upper bounds continue to support a strong +EV overlay, but the extra €1m recipient is random and external tickets remain, so strict guarantee is rejected.

# Other active / blocked branches
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; raw live-book acquisition remains runtime/data blocked.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` updated with H040 theorem and operator screen.

# Test/runtime note
The new algebra was sanity-checked in the Python runtime. A full repository test invocation could not be run in this automation environment because direct `git clone` DNS resolution was blocked; this is a runtime-network limitation, not a known test failure.

# Next priorities
1. Continue cash-refund search **only** for full-loss withdrawable-cash offers with contract wording that permits or cannot claw back low-risk matched play. Do not repeat partial/selective-refund offers closed by H040.
2. Search zero-cost/free-credit conversions only where the credit is large enough to completely cover a tiny outcome space with a positive withdrawable cash floor.
3. H037: broaden special-event controls / recover remaining event counts and prepare autumn-2026 rule-change recalculation.
4. H020 immediately if raw public order books become retrievable.
5. H019 only if capped-entry cash-floor economics materially improve.
6. H006/H007 only after reliable histories/machine metadata become obtainable.
7. H010/H014 if new authoritative data routes appear.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scans, Bayesian hidden-state inference, and causal implementation tests.
