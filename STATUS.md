# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H045 eTopaz contract + settlement-equivalence gate completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H045 — eTopaz contract + settlement gate
Files:
- `research/h045_etopaz_contract_settlement_gate.md`
- `data/derived/h045_contract_settlement_gate.csv`

## Decisive contract result
The current authoritative eTopaz Terms & Conditions have now been recovered.

Material clauses include:
- account/services may not be used for commercial purposes, obtaining another income, or avoiding loss outside the agreement's permitted purpose (4.2.1);
- operator may cancel a subscription without giving a reason (4.5.3);
- operator/game rules and service scope can change (5.2.2 / 8.1 language);
- operator may set betting limits (5.2.3);
- the first-deposit promotion separately reserves the right to change/cancel the promotion at any time.

Under this project's strict-guarantee standard, those clauses prevent treating a deliberately externally hedged 15% first-deposit free bet as an irrevocable guaranteed subsidy.

## Settlement-equivalence proof also fails
Current eTopaz football rules use a **48-hour** suspended-match continuation boundary. Betfair Exchange football/general rules use a materially different reschedule/completion framework extending up to **three days** in relevant branches.

Concrete asymmetric state: event resumes after 48h but within the applicable Betfair continuation/reschedule window. eTopaz can void while Betfair stands.

The same mismatch class appears in table tennis/baseball screens, and Betfair explicitly warns that related third-party bets can have one leg void while another stands.

H045 result:
- H044 eTopaz -> Betfair matched-promo architecture: **REJECTED as strict guaranteed-profit route**;
- remains potentially relevant only as ordinary promotion/EV technique, not terminal SUCCESS.

# H044 — Azerbaijan-accessible promotion + external hedge
H044 previously identified:
- current eTopaz first-deposit free bet = **15% of first deposit**, minimum deposit 20 AZN;
- ordinary Betfair Exchange available as Azerbaijan-accessible hedge venue;
- mechanical free-bet conversion can create a positive normal-outcome floor.

H045 now closes the missing contract/settlement gates against strict guarantee.

# H043 — acquisition-first free-bet / credit screen
Files:
- `research/h043_acquisition_first_freebet_screen.md`
- `data/derived/h043_acquisition_contract_screen.csv`

Zero-incremental-cost stake-not-returned tokens are real, but no current Azerbaijan-executable acquisition + contract combination satisfying the strict guarantee gates has been established.

# H042 — contract-permitted matched-promotion scan
Files:
- `research/h042_contract_permitted_matched_promo_scan.md`
- `data/derived/h042_contract_gate_screen.csv`
- `src/loto_research/commission_subsidy.py`
- `tests/test_commission_subsidy.py`

Contract-permitted matched betting exists as a mechanism class, but no deterministic subsidy source satisfying all execution gates is established.

# H041 — free-bet token matched conversion
Files:
- `research/h041_free_bet_matched_conversion.md`
- `data/derived/h041_free_bet_conversion_screen.csv`
- `src/loto_research/free_bet_conversion.py`
- `tests/test_free_bet_conversion.py`

Mechanical theorem remains valid: an already-earned stake-not-returned token can be converted into a positive all-outcome cash floor after compatible opposing liquidity is irrevocably matched. H045 reinforces that promo contract and settlement identity are independent mandatory gates.

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
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the permanent master trail. Because connector writes require complete-file replacement and the ledger is already large, do not overwrite it from a truncated fetch. H045 dedicated note + data + this STATUS are authoritative until a safe full-file append route is available.

# New general gate established by H045
Any cross-operator matched-promotion SUCCESS must prove both:
1. **contract permission / irrevocability** — no relevant anti-arbitrage, income-seeking, loss-avoidance, clawback or discretionary subsidy-cancellation branch;
2. **settlement isomorphism** — every reachable event/void/resettlement state leaves combined payoff above total cost.

Matching normal-result odds alone is insufficient.

# Next priorities
1. **H046 deterministic withdrawable-cash subsidy screen:** search Azerbaijan-accessible rewards/rebates/referrals where cash is legally/contractually earned before any hedge and not conditional on risky replay.
2. **H046 same-clearing-venue arbitrage:** prioritize structures where opposing legs settle under one rulebook/clearing system, reducing H045 cross-operator void risk.
3. H020 live executable arbitrage if raw public order books become retrievable; combine fee/depth scanner with any deterministic cash/rebate overlay.
4. Search regulated exchange/rebate/commission-credit structures whose consideration is contractual rather than discretionary promotion credit.
5. H037 broaden special-event controls / prepare autumn-2026 rule-change recalculation.
6. H019 only if capped-entry cash-floor economics materially improve.
7. H006/H007 only after reliable histories/machine metadata become obtainable.
8. H010/H014 if new authoritative data routes appear.
9. Before EXHAUSTED: additional current products, deterministic cash-rebate scans, Bayesian hidden-state inference, and causal implementation tests.
