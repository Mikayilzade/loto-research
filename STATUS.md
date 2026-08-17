# STATUS

Updated: 2026-08-17
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H067 transferable vehicle-scrappage arbitrage remains top priority, but tax stress tightens the executable M1/N1 search band to roughly <=800–830 AZN unless exemption is proven**

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
- `data/derived/h067_scrappage_certificate_redemption.csv`
- `data/derived/h067a_live_market_screen.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H067E_APPEND.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H067F_APPEND.md`

## Validated legal/economic mechanism
Azerbaijan's utilization confirmation document is valid 3 years, single-use, **unnamed and usable by another person**. Current fixed one-time redemption includes:
- M1/M1G or N1/N1G: **1,050 AZN**;
- M2/N2/T: **1,400 AZN**;
- M3/N3/H: **2,100 AZN**.

Registered-utilizer acceptance is free. Before utilization the vehicle must be permanently deregistered. The current `Yol hərəkəti haqqında` Article 27 IX-I gives the registration authority 3 working days to decide and specifies refusal gates including certain unpaid final fines and vehicle arrest/encumbrance. The utilization act records technical condition/completeness and missing parts, so incompleteness alone is not evidenced as a categorical rejection ground.

## H067e live market controls
1. A Bakı Lalafo utilization listing advertised `hemin gun 900m 1 ay 1050m`; this is market-liquidity/time-value evidence around 900 AZN immediate realization, not a guaranteed quote to buy our certificate.
2. A Tap.az LADA 2106 at 800 AZN explicitly said `Seneti yoxdu`; it fails the ownership/deregistration gate and is rejected.
3. Cheap parts/body listings without a registered-vehicle identity remain invalid inputs.

## H067f — NEW dominant tax gate
Authoritative sources confirm:
- permanent deregistration is mandatory before utilization;
- registered-utilizer acceptance itself is free;
- no separate explicit utilization-specific permanent-deregistration state-duty line was located in the current State Duty Law/MIA schedules searched, but zero fee is **not yet proven**.

The current Tax Code broadly includes residual income and applies a **14% rate to annual non-business income** unless a specific exemption applies. This run did **not** locate an explicit exemption or official State Tax Service clarification specifically for the vehicle-utilization one-time payment.

Therefore 14% must be carried as a conservative stress case, **not claimed as the actual tax treatment**:

`1,050 * 0.86 = 903 AZN stressed net redemption`.

At this stress level:
- 900 acquisition leaves only 3 AZN before any costs;
- 850 leaves 53 AZN;
- 800 leaves 103 AZN.

With a 20-AZN towing benchmark and 50-AZN safety margin, acquisition must be roughly **<=833 AZN before any additional leakage**.

### Updated search bands
- **<=900–930 AZN** only if authoritative evidence proves the 1,050 payment is received without 14% income-tax leakage and residual fees are tightly bounded;
- **<=800–830 AZN** documented/deregisterable M1/N1 under the conservative tax-stress case.

This demotes the prior 950-AZN candidate from near-terminal to non-executable unless tax exemption is proven.

## Preferred transaction design remains issuance-contingent
For a private eligible vehicle:
1. seller/authorized representative verifies disposal authority and permanent-deregistration eligibility;
2. seller takes utilizer queue before deregistration;
3. seller permanently deregisters and surrenders the vehicle;
4. registered utilizer issues the official confirmation document;
5. buyer pays only after official issuance/verification and receives the original unnamed unused document;
6. buyer applies for the one-time payment.

This avoids irreversible acquisition before the legal/issuance gates are locked.

## Current H067 blockers
1. **authoritative tax treatment** of the 1,050-AZN one-time payment to an ordinary natural person;
2. exact utilization-specific permanent-deregistration fee or explicit zero-fee authority;
3. find a **documented, deregisterable M1/N1 <=800–830 AZN** under tax stress, or <=900–930 only after tax exemption is proven;
4. route-specific towing if movement is required;
5. seller-specific post-issuance transfer commitment and atomic verification/payment;
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
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the master ledger. Connector-safe append packets are authoritative until merged; latest is `research/CHECKED_PROJECTS_AND_TESTS_H067F_APPEND.md`.

# Next priorities
1. **H067g tax clarification** — official State Tax Service/operator evidence on whether the one-time utilization payment is taxable to an ordinary natural person and whether any withholding applies.
2. **H067 deregistration-fee closure** — explicit authority for zero or exact charge.
3. Fresh live search for `sənəti var`, `çıxdaş`, `utilizasiya`, `boş kuza` candidates <=800–830 AZN under tax stress.
4. Search for already-issued unused confirmation documents below the stressed redemption floor.
5. If H067 cannot be locked, continue the next highest-value deterministic-cash class.
