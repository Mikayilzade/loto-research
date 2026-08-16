# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H044 Azerbaijan-accessible promo + external hedge screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H044 — Azerbaijan-accessible promotion + external hedge
Files:
- `research/h044_azerbaijan_accessible_promo_hedge.md`
- `data/derived/h044_azerbaijan_promo_contract_screen.csv`

## Strongest new local lead
Current eTopaz promotion text states:
- first-deposit new users receive a free bet equal to **15% of the first deposit**;
- minimum deposit **20 AZN**;
- first bet must settle, then the free bet is credited;
- free-bet stake is not returned; winnings are returned;
- free bet expires after 14 days;
- operator can change/cancel the promotion.

The indexed specific offer does not state a minimum qualifying first-bet amount or minimum odds. This creates a potentially favorable acquisition structure because token size is deposit-linked rather than explicitly stake-linked. Platform-level minimums/general terms are still unrecovered and therefore cannot be assumed away.

## Hedge venue gate
Betfair's current international Exchange page explicitly lists **Azerbaijan** among eligible countries and the ordinary Exchange supports peer-to-peer back/lay betting.

Important separation:
- Betfair's own risk-free promotion is **not** a terminal candidate because Betfair Standard Promotional Terms allow action where promotional play creates guaranteed/minimal-risk profit.
- ordinary non-promotional Exchange hedging is a separate class; retrieved general terms prohibit self-matching/collusion/manipulation, not a blanket independent external hedge.

## New decisive execution gate — settlement equivalence
Betfair's rules explicitly warn that related bets across Betfair products and/or third parties can diverge: one leg may be void while another stands.

Therefore a two-operator hedge is not a strict guarantee merely because normal-event payoffs are balanced. A terminal proof must establish matching settlement behavior for every cancellation, postponement, correction, dead-heat and void branch for the exact selected market pair.

## H044 economics
Necessary condition for eTopaz first-deposit route:

`rho * 0.15D > Cq + Cf`

where:
- `D` = first deposit;
- `rho` = worst-case cash conversion fraction of the free-bet token after hedge/commission;
- `Cq` = worst-case acquisition/qualifying-bet hedge cost;
- `Cf` = FX/withdrawal/fixed execution costs.

This is necessary, not sufficient. Terminal gates still require:
1. authoritative eTopaz general promo/account terms;
2. platform minimum qualifying stake/odds;
3. irrevocable entitlement after first bet settles;
4. current cash-in/out route and fees from Azerbaijan;
5. pre-exposure matched hedge liquidity;
6. all-branch settlement equivalence;
7. no applicable anti-hedge/clawback clause.

H044 status: **PROMISING ARCHITECTURE; NOT SUCCESS**.

# H043 — acquisition-first free-bet / credit screen
Files:
- `research/h043_acquisition_first_freebet_screen.md`
- `data/derived/h043_acquisition_contract_screen.csv`

H043 established that zero-incremental-cost stake-not-returned tokens are real, but no current Azerbaijan-executable acquisition + contract combination had been found. H044 improves this by identifying a current local deterministic-looking deposit-linked free-bet source plus an Azerbaijan-accessible hedge venue; remaining blockers are narrower contractual/settlement gates.

# H042 — contract-permitted matched-promotion scan
Files:
- `research/h042_contract_permitted_matched_promo_scan.md`
- `data/derived/h042_contract_gate_screen.csv`
- `src/loto_research/commission_subsidy.py`
- `tests/test_commission_subsidy.py`

H042 established that the contract gate is not universally impossible. Exchange token mechanics and commission subsidies are valid classes, but no deterministic free-bet source satisfying all execution gates was established.

# H041 — free-bet token matched conversion
Files:
- `research/h041_free_bet_matched_conversion.md`
- `data/derived/h041_free_bet_conversion_screen.csv`
- `src/loto_research/free_bet_conversion.py`
- `tests/test_free_bet_conversion.py`

Mechanical theorem remains valid: an already-earned stake-not-returned free-bet token can be converted into a positive all-outcome cash floor after compatible opposing liquidity is irrevocably matched. Promo clawback and settlement mismatch are independent terminal gates.

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
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the permanent master trail. Because the connector cannot safely append to that already-large file without replacing/truncating unseen content, newest H041–H044 dedicated notes plus this STATUS remain authoritative supplements until a safe append route is available. Do not delete or overwrite older ledger rows to force an append.

# Test/runtime note
Repository clone/network path remains unavailable from the local runtime, so GitHub connector writes are used directly. H044 is primarily a source/contract/jurisdiction classification packet; no live wager execution was attempted.

# Next priorities
1. **H045 eTopaz terms/minimums gate:** recover authoritative eTopaz Terms & Conditions and determine minimum stake/odds, promo-clawback language, withdrawal/KYC/payment restrictions, and whether entitlement survives terms changes once qualification settles.
2. **H045 settlement-equivalence proof:** identify one eTopaz market and matching Betfair Exchange market whose void/cancellation/settlement rules can be mapped exhaustively; reject any pair with asymmetric branches.
3. Quantify current Betfair Exchange commission and realistic matched depth from Azerbaijan if public endpoints become retrievable; combine with H041 conversion math and the 15% token.
4. Search deterministic **withdrawable cash** local rebates/rewards; cash removes the free-bet conversion gate.
5. H020 if raw public order books become retrievable; apply commission/rebate overlays to executable depth.
6. H037 broaden special-event controls / prepare autumn-2026 rule-change recalculation.
7. H019 only if capped-entry cash-floor economics materially improve.
8. H006/H007 only after reliable histories/machine metadata become obtainable.
9. H010/H014 if new authoritative data routes appear.
10. Before EXHAUSTED: additional current products, deterministic cash-rebate scans, Bayesian hidden-state inference, and causal implementation tests.
