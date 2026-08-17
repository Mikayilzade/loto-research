# STATUS

Updated: 2026-08-18
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H067 transferable vehicle-scrappage certificate arbitrage remains top priority. H067g materially improved the tax model: 14% of the entire 1,050 AZN is now only a harsh fallback, while general State Tax Service guidance supports taxing net gain after deductible acquisition cost if the certificate is treated as an asset/right.**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H067 — transferable scrappage confirmation document: TOP PRIORITY
Files now include:
- `research/h067_transferable_scrappage_certificate_arbitrage.md`
- `research/h067a_live_market_and_verification.md`
- `research/h067b_issuance_contingent_arbitrage.md`
- `research/h067c_live_titled_asset_screen.md`
- `research/h067d_live_950_candidate_and_acceptance_gate.md`
- `research/h067e_live_execution_thresholds.md`
- `research/h067f_deregistration_and_tax_gate.md`
- `research/h067g_tax_basis_and_deregistration_fee.md`
- `data/derived/h067_scrappage_certificate_redemption.csv`
- `data/derived/h067a_live_market_screen.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H067G_APPEND.md`

## Validated legal/economic mechanism
Azerbaijan's utilization confirmation document is valid 3 years, single-use, **unnamed and usable by another person**. Current fixed one-time redemption includes:
- M1/M1G or N1/N1G: **1,050 AZN**;
- M2/N2/T: **1,400 AZN**;
- M3/N3/H: **2,100 AZN**.

Registered-utilizer acceptance is free. Before utilization the vehicle must be permanently deregistered. The current utilization law requires the operator to transfer the one-time payment within 30 working days after the holder submits the confirmation document.

A June 19, 2026 program statement reports that more than 1m AZN has already been paid as one-time payments, so the redemption route is operational in practice.

## H067g — NEW tax-basis result
Authoritative current tax sources establish:
- Tax Code 101.2: **14%** tax rate for annual non-business income;
- State Tax Service guidance: for non-business income not taxed at source, taxable income is generally receipts minus deductible expenses under Chapter X;
- State Tax Service securities and crypto examples tax the **gain / increase over acquisition value**, not gross sale proceeds.

Therefore the previous model `1,050 * 0.86 = 903` must remain only a deliberately adverse fallback unless the exact utilization payment is specifically classified as fully taxable gross income.

For a purchased unused confirmation document at acquisition price `A`, the stronger general-law analogy is:

`tax = 14% * max(1,050 - A, 0)`

`post-tax redemption = 903 + 0.14A`

Examples:
- A=900 -> tax 21; post-tax redemption **1,029**; spread **129 AZN** before other costs;
- A=950 -> tax 14; post-tax redemption **1,036**; spread **86 AZN**;
- A=1,000 -> tax 7; post-tax redemption **1,043**; spread **43 AZN**.

With 20 AZN execution cost + 50 AZN required safety margin, gain-basis threshold is approximately **968.60 AZN**.

Under the harsh gross-tax fallback, the old <=833 AZN threshold remains.

### Meaning
The prior 800–830 AZN live-search band should **not** be treated as the only economically plausible band. Roughly 900–950 AZN certificates become materially interesting again if State Tax Service/operator confirms that documented acquisition cost of a transferred confirmation document is deductible, or confirms exemption/no withholding.

## Deregistration-fee update
Current State Duty Law enumerates fees for technical inspection/registration actions, but the searched current schedule contains no distinct utilization-specific permanent-deregistration duty. Traffic/DYP deregistration rules likewise describe the removal process without identifying a separate utilization deregistration fee.

This **strengthens**, but does not formally prove, a zero-separate-duty interpretation. Retain a residual execution-cost reserve until officially confirmed.

## Best transaction design
Prefer **post-issuance purchase of an already-issued unused original confirmation document** rather than buying a questionable vehicle first.

Before irreversible payment require:
1. original unused document exists;
2. validity/unused status is verified with operator/utilizer as far as the official process permits;
3. transfer is atomic against payment;
4. purchase price and related costs are documented;
5. tax treatment is confirmed in writing, or price is low enough to survive the gross-tax fallback;
6. redemption application is immediately executable.

## Current H067 blockers
1. **product-specific tax classification** of redemption by a natural person who purchased the transferable confirmation document;
2. explicit written confirmation whether certificate acquisition cost/related costs are deductible against the 1,050-AZN receipt;
3. formal zero/exact permanent-deregistration duty confirmation;
4. fresh live already-issued unused certificate or issuance-contingent seller within the appropriate price band;
5. seller-specific atomic verification/payment structure;
6. prove `net redemption - all locked costs > 0` with safety margin before irreversible payment.

# Other important open branches
- H065 2026 fallow-land subsidy: conditional lead; cashability/current entry unresolved.
- H052 upfront insured interest: product-specific agreement still missing.
- H020 two-sided arbitrage: mechanism validated; no fully vested live setup.
- H019 capped fixed-prize saturation: valid in principle; sampled instances fail economics.
- H007 high-frequency RNG: data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# General terminal gates
Any SUCCESS must prove contract/legal entitlement, complete execution, strictly positive worst-case cash floor, all taxes/fees/limits, and irreversibility only after all necessary eligibility gates are locked.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the master ledger. Connector-safe append packets are authoritative until merged; latest is `research/CHECKED_PROJECTS_AND_TESTS_H067G_APPEND.md`.

# Next priorities
1. **H067h product-specific tax clarification** — official State Tax Service/operator evidence on whether redemption of a purchased transferable confirmation document is taxed on gross receipt, net gain, or exempt, and whether withholding applies.
2. Fresh live search for **already-issued unused confirmation documents around 900–950 AZN**, now economically relevant under the gain-basis model, while preserving <=833 AZN as the gross-tax-safe band.
3. Formal deregistration-fee closure.
4. Search issuance-contingent sellers willing to transfer only after document issuance/verification.
5. If H067 cannot be locked, continue the next highest-value deterministic-cash class.
