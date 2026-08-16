# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H042 contract-permitted matched-promotion scan completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H042 — contract-permitted matched-promotion scan
Files:
- `research/h042_contract_permitted_matched_promo_scan.md`
- `data/derived/h042_contract_gate_screen.csv`
- `src/loto_research/commission_subsidy.py`
- `tests/test_commission_subsidy.py`

## Main result
H041's free-bet matched-conversion mechanism has now been decomposed into three gates:
1. deterministic **acquisition** of the promo value;
2. fully matched **conversion** into an outcome-independent cash floor;
3. a **contract** that permits the qualifying/conversion hedge and has no no-risk/arbitrage clawback branch.

H041 already validates conversion mechanically. H042 shows the contract gate is **not universally impossible**:
- Matchbook's current standard promotion framework explicitly allows free-bet tokens on exchange markets and no generic Betfair-style guaranteed/minimal-risk prohibition was located in the retrieved standard terms;
- BetConnect explicitly operates as a matched-betting-friendly lay venue, though current signup is UK/Northern-Ireland gated;
- Betfair remains a negative control because its standard promo terms explicitly permit remedies against guaranteed/minimal-risk promotional profit.

The strongest concrete Matchbook 2026 free-bet offer recovered in this run expired on **2026-07-30** and also restricted trading of the qualifying selection. Therefore no current executable deterministic token source was established.

## Current BETDAQ subsidy theorem
BETDAQ currently advertises:
- 0% exchange commission for 100 days for eligible new UK/Irish customers through **2026-12-31**;
- DAQBACK first-month commission cashback as withdrawable cash.

These are real deterministic cost subsidies, but a commission-only rebate cannot create a surebet without a pre-commission pricing edge. If outcome profit before commission is `G`, commission is `C>=0`, and refund fraction is `r`, then:

`P = G - (1-r)C <= G`.

At 100% refund the result only returns to the zero-commission state. Thus this is an **H020 execution overlay**, not standalone SUCCESS.

H042 status:
- contract-permitted matched-betting architecture: **VALIDATED as a real class**;
- current exchange commission subsidy: **VALIDATED but insufficient standalone**;
- current deterministic hedge-permitted free-bet acquisition: **NOT FOUND**;
- terminal SUCCESS: **NOT YET**.

# H041 — free-bet token matched conversion
Files:
- `research/h041_free_bet_matched_conversion.md`
- `data/derived/h041_free_bet_conversion_screen.csv`
- `src/loto_research/free_bet_conversion.py`
- `tests/test_free_bet_conversion.py`

Mechanical theorem remains valid: an already-earned stake-not-returned free-bet token can be converted into a positive all-outcome cash floor after compatible opposing lay liquidity is irrevocably matched. Sky/Betfair-style anti-no-risk clauses prevent promoting that mechanical floor into a contractual guarantee.

# Strongest non-terminal positive-EV result
## H037 Irish Lotto Plus Million Euro Raffle
Six recovered special-event raffle-winner counts remain far below the modeled break-even participation threshold. Gamma-Poisson posterior and event-day upper bounds continue to support a strong +EV overlay, but the extra €1m recipient is random and external tickets remain, so strict guarantee is rejected.

# Other active / blocked branches
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; raw live-book acquisition remains runtime/data blocked. BETDAQ zero-commission / commission cashback can improve execution but cannot manufacture an arb.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the permanent audit trail. H041/H042 should be appended there; if connector replacement limitations prevent a safe append without risking deletion of prior rows, the dedicated H041/H042 notes and this STATUS are authoritative until the safe ledger write succeeds.

# Test/runtime note
H042 formula tests were added. Repository test execution remains dependent on a runnable checkout/network path; the current runtime could not clone GitHub directly. Formula identities were independently sanity-checked.

# Next priorities
1. **H043 acquisition-first search:** current fixed free-bet/credit offers whose specific + incorporated general terms do not prohibit an external hedge, with deterministic eligibility and withdrawable winnings. Prioritize jurisdictions actually executable from Azerbaijan; classify jurisdiction-limited findings separately.
2. Search exchange-issued tokens where the issuer itself permits normal opposing trading after token credit; distinguish prohibited self-matching from legitimate matching against independent counterparties.
3. H020 if raw public order books become retrievable; apply current zero-commission/rebate overlays to actual executable depth.
4. H037: broaden special-event controls / recover remaining event counts and prepare autumn-2026 rule-change recalculation.
5. H019 only if capped-entry cash-floor economics materially improve.
6. H006/H007 only after reliable histories/machine metadata become obtainable.
7. H010/H014 if new authoritative data routes appear.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scans, Bayesian hidden-state inference, and causal implementation tests.
