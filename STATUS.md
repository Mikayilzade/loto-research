# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H043 acquisition-first free-bet screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H043 — acquisition-first free-bet / credit screen
Files:
- `research/h043_acquisition_first_freebet_screen.md`
- `data/derived/h043_acquisition_contract_screen.csv`

## Main result
The H041/H042 architecture has now been screened from the acquisition side.

Required terminal gates remain:
1. deterministic promo/token acquisition;
2. all-outcome matched conversion;
3. no anti-guaranteed-profit / anti-hedge clawback branch;
4. lawful/executable access from Azerbaijan;
5. irrevocably matched compatible hedge legs before exposure.

### Strongest new structural lead: Spreadex
Current indexed Spreadex pages show account-targeted fixed-odds reward free bets, including a version described as risk-free and requiring **no qualifying bets**. This is a real zero-incremental-wager acquisition class once the token is actually allocated.

However Spreadex's current Restricted Territories page states fixed-odds services are licensed for **UK, Ireland and Denmark** and are restricted for residents outside those territories. The public reward page also does not guarantee allocation to every new account.

Status: **architecture-promising; fails Azerbaijan jurisdiction + deterministic-allocation gate**.

### Matchbook / PredictStreet
Matchbook standard promo mechanics remain comparatively permissive: free bets can be used on exchange markets. But the currently indexed `CHAMPIONS` offer requires a £20 bet on a team to win the **2025/26 Premier League**; by 2026-08-16 that competition is settled, so the qualifying market is no longer executable despite the page displaying an end date of 2026-08-31.

PredictStreet/Matchbook World Cup welcome pages are still indexed, but H042 recovered specific WC2026 terms ending **2026-07-30**. Treat front-end cards as stale until current specific terms prove otherwise.

Status: **no current deterministic acquisition route established**.

### Negative controls
- bet365: current welcome bonus exists, but general/promo terms explicitly permit action against arbitrage / all-outcome guaranteed-profit strategies.
- Betway: current promo terms classify equal/zero-margin and hedge constructions as irregular gaming.
- Rivalry: promo terms explicitly classify all-outcome / hedge / equal-margin play as irregular.
- Winz: sports welcome promotion explicitly excludes Azerbaijan.

## H043 conclusion
A zero-cost allocated stake-not-returned token would be mechanically convertible into a positive all-outcome cash floor under H041 once the opposing lay is irrevocably matched. The blocker is no longer conversion mathematics; it is finding **one current offer that simultaneously passes acquisition + contract + Azerbaijan-jurisdiction gates**.

H043 status:
- zero-incremental-cost token class: **REAL**;
- hedge-permitted conversion architecture: **REAL CLASS (H042)**;
- current Azerbaijan-executable combined candidate: **NOT FOUND**;
- terminal SUCCESS: **NO**.

# H042 — contract-permitted matched-promotion scan
Files:
- `research/h042_contract_permitted_matched_promo_scan.md`
- `data/derived/h042_contract_gate_screen.csv`
- `src/loto_research/commission_subsidy.py`
- `tests/test_commission_subsidy.py`

H042 established that the contract gate is not universally impossible. Matchbook-style exchange token mechanics and BETDAQ commission subsidies are valid classes, but no current deterministic free-bet source satisfying all execution gates was established. Commission rebates can only improve an existing pricing edge, not create a surebet from none.

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
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; raw live-book acquisition remains runtime/data blocked.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the permanent audit trail. H041/H042/H043 dedicated notes plus this STATUS are authoritative for these newest packets until the connector supports a safe append without risking deletion of earlier rows.

# Test/runtime note
Repository clone/network path remains unavailable from the local runtime, so GitHub connector writes are used directly. Formula identities were sanity-checked independently; H043 is primarily a source/contract/jurisdiction classification packet rather than new numerical code.

# Next priorities
1. **H044 Azerbaijan-accessible operator scan:** search operators/exchanges actually accepting Azerbaijan residents for allocated/no-deposit/free-token offers whose specific + incorporated terms do not prohibit an external hedge.
2. Search exchange-issued tokens where ordinary opposing trading against independent counterparties is explicitly permitted; distinguish prohibited self-matching/collusion from legitimate external risk offset.
3. Search deterministic **withdrawable cash** rebates/rewards accessible from Azerbaijan; cash removes the token-conversion gate entirely.
4. H020 if raw public order books become retrievable; apply current zero-commission/rebate overlays to actual executable depth.
5. H037 broaden special-event controls / prepare autumn-2026 rule-change recalculation.
6. H019 only if capped-entry cash-floor economics materially improve.
7. H006/H007 only after reliable histories/machine metadata become obtainable.
8. H010/H014 if new authoritative data routes appear.
9. Before EXHAUSTED: additional current products, deterministic cash-rebate scans, Bayesian hidden-state inference, and causal implementation tests.
