# H067a — live scrappage market + pre-purchase verification gate

Updated: 2026-08-17
Status: **LIVE DISCOUNT MARKET SIGNAL FOUND; NOT YET TERMINAL SUCCESS**

## Goal
Advance H067 from a legal/mechanical arbitrage theorem toward an executable current transaction.

Two questions matter most:
1. Does a real current market exist at a price below the fixed 1,050-AZN M1/N1 cash redemption?
2. Can authenticity + unused status be checked before irreversible payment?

## 1. Live market signal — strong new evidence
A current Lalafo listing (ID `73753310`) from a PRO seller, created 2025-10-31 and updated **2026-06-30**, states:

`Utilizasiya boş kuzalarin qebulu. baki. hemin gun 900m 1 ay 1050m`

The indexed listing therefore publicly offers the economic choice:
- **900 AZN same day**; or
- **1,050 AZN after one month**.

Source:
- https://lalafo.az/baku/ads/sedan-avtomobil-kuzovu-skelet-id-73753310

Interpretation:
- This is the first concrete market evidence in the project that participants are willing to exchange the delayed 1,050-AZN utilization value for materially less immediate cash.
- Implied liquidity/time discount: **150 AZN = 14.2857% of 1,050**.
- The listing does **not** prove that an already-issued confirmation document itself can be bought for 900 AZN, nor that the intermediary transfers the certificate rather than running the surrender/redemption process itself.
- It does show that a seller-side acquisition market below statutory redemption exists in practice, which materially strengthens H067d (seller-authorized surrender) and the economic plausibility of H067a.

## 2. Current statutory / operator mechanics reconfirmed
Primary sources current as indexed in August 2026:
- Waste law Article 14-8: confirmation document is valid 3 years, single-use, **unnamed**, and may be used by another person.
- Təmiz Şəhər: confirmation documents are issued only by registered utilizers and are tracked by the operator.
- Təmiz Şəhər payment workflow: bearer/presenter enters certificate information in `nvu.gov.az`, then presents the original certificate, ID and own bank details; operator pays within 30 working days.
- The operator explicitly maintains accounting (`uçot`) of confirmation documents.

Sources:
- https://frameworks.e-qanun.az/3/f_3186.html
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/tesdiqedici-senedler-barede
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/fond/tesdiqedici-senedler-uzre-odenisler
- https://tamizshahar.az/az/neqliyyat/sual-cavab

## 3. Verification architecture — narrowed but not completed
The public FAQ states that each confirmation document is a strict-accountability form with a **special series and number**. The operator's functions include accounting of confirmation documents.

The one-time-payment flow requires the user to:
1. log into `nvu.gov.az` personal cabinet;
2. choose the confirmation-document usage section;
3. select one-time payment;
4. add information about the certificate(s);
5. then present the originals to the operator.

This strongly implies that the portal/operator has a certificate-record lookup/validation step, but the public materials do **not** explicitly state that a prospective buyer can obtain a binding pre-purchase confirmation that a specific serial is authentic, unused, non-state-exception and cash-eligible.

The currently downloadable NVU citizen guide is focused on creating a vehicle-surrender application and does not document a transferable-certificate pre-purchase verification screen. Direct public fetch of `nvu.gov.az` timed out in this runtime.

Therefore H067b remains open on one narrow question:

> Can a buyer/presenter enter a certificate series/number before payment and receive an authoritative state showing `valid + unused + cash eligible`, without consuming/locking the document?

## 4. Economic screen
For an M1/N1 certificate:
- statutory cash redemption: `R = 1,050 AZN`;
- observed immediate-market benchmark: `P = 900 AZN`;
- gross spread before all costs/tax: `150 AZN`;
- gross spread / redemption: `14.2857%`;
- gross spread / acquisition cost: `16.6667%`.

Terminal condition remains:

`R - P - verification_cost - contract_cost - bank_cost - tax - other_execution_cost > 0`

and every gate must be locked before `P` becomes irreversible.

The 150-AZN observed spread is large enough that the route is economically worth continuing, but tax treatment of a secondary acquisition/redemption spread and exact transaction costs remain unresolved. No tax exemption is assumed.

## 5. Atomic transaction design — current best form
A safe candidate structure is now:
1. seller presents original certificate or vehicle/authority package;
2. buyer and seller jointly verify series/number with operator/NVU or registered utilizer;
3. operator confirms document is valid, unused, transferable and cash-eligible;
4. buyer creates/validates redemption application in own NVU cabinet if possible **before** releasing funds;
5. physical original transfers simultaneously with payment using a written assignment/sale acknowledgement recording series/number, price and seller warranty against prior use/duplicate disposal;
6. buyer immediately submits original to operator and receives a stamped/registered receipt;
7. only structures with a hard all-in cost below 1,050 AZN qualify.

If step 3/4 cannot be made authoritative pre-payment, direct certificate purchase does **not** meet the project guarantee criterion because counterfeit/double-use risk remains.

## 6. Strong fallback — compete with the observed 900-AZN intermediary model
The live listing demonstrates that at least one market participant values immediate surrender below 1,050 AZN. A lawful competing model could offer >900 but <1,050 minus costs, **provided payment is contingent on successful certificate issuance/verification**.

This is structurally stronger than buying an already-issued paper from an unknown seller because the buyer can participate in the issuance workflow and reduce double-spend/counterfeit risk.

However no concrete owner transaction is currently locked, so this is not terminal SUCCESS.

## Current conclusion
**H067 is materially stronger after this run.** A real current market signal now shows a 900-now / 1,050-later discount, validating the economic premise rather than merely the statute.

Still **NO SUCCESS** because the project lacks both:
- a concrete locked seller/certificate transaction; and
- an authoritative pre-purchase unused/authenticity verification workflow.

## Next highest-value tests
1. Recover exact NVU certificate-use screen or operator instructions that reveal serial validation behavior.
2. Search for already-issued certificate listings using colloquial terms (`kupon`, `utilizasiya kuponu`, `1050 sənəd`) and local classifieds.
3. Search for end-of-life car/empty-body sellers willing to take <=900–950 AZN under payment-after-certificate terms.
4. Resolve whether one-time redemption or certificate resale creates withholding/income-tax leakage for an individual arbitrageur.
5. Only claim SUCCESS when a specific transaction is pre-verifiable and has strictly positive all-in locked spread.
