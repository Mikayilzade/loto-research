# STATUS

Updated: 2026-08-18
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; strongest deterministic-cash leads are execution/data gated, and new deterministic classes are being screened instead of repeating blocked searches.**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H071 — statutory gift-card cash redemption: NEW VALIDATED MECHANISM, execution-gated
Key files:
- `research/h071_statutory_giftcard_cash_redemption.md`
- `src/loto_research/giftcard_cash_redemption.py`
- `tests/test_giftcard_cash_redemption.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H071_APPEND.md`

California SB 22 makes qualifying closed-loop gift cards/e-gift cards with balance **< $15** mandatorily cash-redeemable from **2026-04-01**. Therefore if a valid in-scope balance `B` is acquired only after all validity/redemption gates are locked, with all-in irreversible cost `P+C < B`, deterministic cash profit is `B-P-C > 0`.

The discounted secondary market is real and current, but this run did **not** prove a live qualifying `<$15` card at sufficient discount together with a pre-payment non-revocation/validity lock and a practical low-cost California redemption route from Azerbaijan. A 45-day marketplace buyer guarantee is risk mitigation, not the all-branches certainty required for terminal SUCCESS.

Status: **MECHANISM VALIDATED / CURRENT EXECUTION-GATED / NOT SUCCESS**.

Reopen H071 only with a current small-balance candidate, lockable validity/escrow, or a jurisdiction/operator that supports guaranteed remote statutory cash redemption.

# H070 — Azerbaijan interbank FX cross-arbitrage: synchronized sample negative
Key files:
- `research/h070_azerbaijan_interbank_fx_cross_arbitrage.md`
- `src/loto_research/fx_cross_arbitrage.py`
- `data/derived/h070_azerbaijan_fx_cross_screen_2026-07-31.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H070_APPEND.md`

Mechanism: a strict same-currency cross-bank arbitrage exists if a simultaneously executable bank bid exceeds another bank's ask after all fees/costs.

Synchronized official-bank screen for **31.07.2026** found no pre-fee cross:
- cash USD: **-0.294%** best round-trip gap;
- cash EUR: **-2.036%**;
- cash GBP: **-2.974%**;
- cash RUB: **-4.651%**;
- synchronized cashless rows were also negative.

A false-positive control was added: mixing bank quotes from different dates can superficially create a RUB arbitrage, so the scanner hard-buckets by exact date/channel/currency.

Status: **VALID MECHANISM CLASS / SAMPLED STATE NEGATIVE / NOT SUCCESS**.

Reopen H070 only with genuinely synchronized/live executable quotes or a feed/API that allows both legs to be locked before execution. Do not infer profit from cached search-index rates.

# H069 — damaged AZN statutory face redemption: VALIDATED MECHANISM, execution-blocked
CBAR rules provide deterministic face-value redemption for qualifying authentic damaged national banknotes. A real arbitrage requires acquiring a qualifying current-AZN note below face only after redemption eligibility is locked. No live discounted note or public binding pre-purchase eligibility route has been found.

Status: **MECHANISM VALIDATED / NO LIVE EXECUTABLE INSTANCE**.

# H068 — CBAR investment-coin mandatory buyback: PROMISING CLASS, sampled market negative
Appointed agents must repurchase eligible CBAR investment coins, with same-day payment and price tied to official gold value subject to the published haircut. Sampled secondary-market asks were above buyback reference levels.

Status: **VALIDATED REDEMPTION MECHANISM / NO POSITIVE LIVE INSTANCE**.

# H067 — transferable scrappage confirmation document: TOP EXECUTION-GATED LEAD
Waste Law Article 14-8 establishes a 3-year, single-use, unnamed, transferable confirmation document redeemable by the holder for fixed cash. Current M1/M1G or N1/N1G redemption is **1,050 AZN**. Transferee entitlement is validated; remaining blocker is locking unused validity before irreversible payment and finding enough margin.

Status: **MECHANISM/TRANSFEREE RIGHT VALIDATED / LIVE EXECUTION BLOCKED**.

# H052 — upfront insured interest: PUBLIC-WEB DATA-BLOCKED
Expressbank `Əlavə fürsət` and VTB `Avans` confirm advance-interest deposit products, but the decisive product-specific agreement needed to resolve insolvency/offset treatment is not public. Generic web searching is closed until genuinely new contract or authoritative interpretation appears.

Status: **PROMISING / DATA-BLOCKED**.

# H065 — 2026 fallow subsidy: NEW-ENTRY ROUTE CLOSED
Current 2026 rules require prior 3-year EKTIS history and passed declaration/application windows; a new entrant cannot create fresh 2026 entitlement now.

Status: **MECHANISM VALIDATED / 2026 NEW-ENTRY GUARANTEE REJECTED**.

# Other important open branches
- H020 two-sided arbitrage: mechanism validated; no fully vested live setup.
- H019 capped fixed-prize saturation: valid in principle; sampled instances fail economics.
- H007 high-frequency RNG: data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# General terminal gates
Any SUCCESS must prove contract/legal entitlement, complete execution, strictly positive worst-case cash floor, all taxes/fees/limits, and irreversibility only after all eligibility gates are locked.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the master ledger. Connector-safe append packets are authoritative until merged; newest append: `research/CHECKED_PROJECTS_AND_TESTS_H071_APPEND.md`.

# Next priorities
1. Do **not** repeat H067/H068/H069/H052/H071 generic searches without genuinely new execution evidence.
2. H070 only on new synchronized/live bank quotes or a lockable feed; no stale-rate comparisons.
3. Expand to another **new deterministic principal-preserving / statutory-redemption / fixed-cash edge class**.
4. H020/H019 only with genuinely new live executable instances.
5. Data-gated H007/H014/H010 only when new data routes appear.
6. Continue systematic class expansion until either a strict executable SUCCESS is proven or remaining defensible classes are exhausted.
