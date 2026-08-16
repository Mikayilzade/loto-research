# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H041 free-bet matched-conversion theorem completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H041 — free-bet token matched conversion
Files:
- `research/h041_free_bet_matched_conversion.md`
- `data/derived/h041_free_bet_conversion_screen.csv`
- `src/loto_research/free_bet_conversion.py`
- `tests/test_free_bet_conversion.py`

## Mechanical theorem
For stake-not-returned free-bet token `F` at bookmaker odds `O_b`, exchange lay odds `O_l`, and commission `c`, equal-profit lay stake is:

`x = F*(O_b-1)/(O_l-c)`

and after both legs are irrevocably accepted the cash floor is:

`P = F*(O_b-1)*(1-c)/(O_l-c) > 0`.

This is stronger than ordinary +EV: a valid free-bet token can be mechanically converted into positive outcome-independent cash when the opposing lay is fully matched under compatible settlement rules.

## Current Sky Bet + Smarkets screen
Sky Bet currently offers new customers **3 x £10 Free Bets** after a £5 deposit and a first qualifying **5p** bet at odds 2.00+; free-bet stakes are not returned.

Mechanical sensitivity for three £10 tokens plus the 5p qualifier:
- bookmaker/lay 2.00, 0% exchange commission: ~**£15.00** floor;
- bookmaker/lay 2.00, 2% commission: ~**£14.84798** floor;
- bookmaker 2.00 / lay 2.20, 2% commission: ~**£13.48119** floor.

Smarkets itself explicitly documents matched betting as using bookmaker free bets plus exchange lays to cover outcomes and lock in profit, independently validating the mechanism class.

## Why H041 is not terminal SUCCESS
Sky Bet's incorporated general promotion terms explicitly prohibit exploiting promotions through bets with **no or limited risk of loss**, except where absence of risk is a key feature of the promotion, and reserve power to withhold promotional amounts/free stakes/bonuses. The welcome offer also carries promotion-abuse discretion.

Therefore the settlement floor is not yet a contractual floor: a clawback/denial branch remains. The verified Smarkets 0%-commission promotion is also jurisdiction-limited.

H041 status:
- mechanical free-bet conversion theorem: **VALIDATED**;
- matched-betting operational mechanism: **VALIDATED**;
- current Sky/Smarkets example: **positive mechanical floor but REJECTED as strict contractual guarantee**;
- terminal SUCCESS: **NOT YET**.

# H040 — expanded cash-refund contract screen
Files:
- `research/h040_cash_refund_operator_scan.md`
- `data/derived/h040_cash_refund_contract_screen.csv`
- `src/loto_research/promo_hedge.py`
- `tests/test_promo_hedge.py`

Selective-refund theorem remains closed: if any legal losing state gets no cash refund, the promotion cannot create a surebet unless an ordinary bookmaker/exchange price arbitrage already exists.

Current screened operators (bet365, Paddy Power, Sky Bet, BetVictor, BetMGM, FanDuel) either retain anti-guaranteed-profit/abuse discretion, refund only selected losing states, or pay nonwithdrawable bonus bets. No terminal candidate found.

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
`research/CHECKED_PROJECTS_AND_TESTS.md` must include H041 before the next packet; if connector write limitations prevent the append in a run, `research/h041_free_bet_matched_conversion.md` and this STATUS are the authoritative H041 record until the ledger append succeeds.

# Test/runtime note
H041 formulas were independently sanity-checked in Python. Repository test execution remains dependent on a runnable checkout/network path; no known formula/test failure is present.

# Next priorities
1. **H041 contract-first search:** free-bet/token offers whose own terms explicitly permit matched betting/hedging or lack a no-risk/arbitrage clawback, with deterministic eligibility and withdrawable winnings. Do not repeat Sky-style offers closed by general promotion-abuse language.
2. Search zero-cost/free-credit awards only where the credit can be converted through a tiny fully hedgeable outcome space and the issuer contract permits the hedge.
3. H037: broaden special-event controls / recover remaining event counts and prepare autumn-2026 rule-change recalculation.
4. H020 immediately if raw public order books become retrievable.
5. H019 only if capped-entry cash-floor economics materially improve.
6. H006/H007 only after reliable histories/machine metadata become obtainable.
7. H010/H014 if new authoritative data routes appear.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scans, Bayesian hidden-state inference, and causal implementation tests.
