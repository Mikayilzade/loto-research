# H067b — issuance-contingent scrappage arbitrage

Updated: 2026-08-17
Status: **mechanism materially strengthened; concrete counterparty still missing; NO SUCCESS**

## Goal
Remove the largest fraud/verification weakness in H067: buying an already-issued transferable confirmation document from an unknown seller before knowing whether it is authentic and unused.

## Key new result: do not buy the paper first
The governing Azerbaijan waste law provides a safer structure.

For a privately owned eligible vehicle:
1. the owner, or another person with disposal authority, may surrender the vehicle for utilization;
2. the vehicle must first be permanently deregistered;
3. the registered utilizer accepts the vehicle and prepares a strict-accountability acceptance act;
4. **within 2 working days after acceptance, the utilizer must issue the confirmation document**;
5. one copy is given to the person who surrendered the vehicle and another is sent to the operator;
6. the confirmation document is valid for 3 years, single-use, **unnamed and usable by another person**.

Primary current law:
- https://frameworks.e-qanun.az/3/f_3186.html
- President publication of the 2023 amendment: https://president.az/az/articles/view/60617

This means an arbitrageur does not need to pay for an unverifiable secondary-market certificate. The transaction can instead be made contingent on successful official issuance.

## Strong transaction architecture
For an M1/N1 privately owned vehicle/certificate with 1,050 AZN cash redemption:

### Pre-commitment
- seller proves ownership / disposal authority and the vehicle's identity;
- vehicle is checked to be privately owned, not one of the state/public/abandoned categories whose one-time payment is transferred to the state budget;
- seller agrees in writing that compensation is payable only after a registered utilizer has accepted the vehicle and issued the confirmation document;
- purchase price is fixed at `P`, with no non-refundable deposit.

### Official surrender
- seller/authorized person completes permanent deregistration and the NVU workflow;
- vehicle is surrendered to a **registered utilizer**;
- registered utilizer issues the official acceptance act;
- no buyer capital becomes irreversible at this stage except explicitly bounded transport/document costs.

### Issuance gate
- wait for the confirmation document to be physically issued by the registered utilizer (statutory deadline: 2 working days after acceptance);
- confirm the document category/value and original strict-accountability form;
- only after official issuance does the buyer pay `P` and receive the original document under a written receipt recording series/number and price.

Because the certificate is unnamed and another person may use it, legal bearer substitution is built into the statute.

### Redemption
The current operator workflow states that the presenter:
- enters the confirmation-document information in the `nvu.gov.az` personal cabinet;
- chooses one-time payment;
- then provides the operator the original certificate, ID and own bank-account details;
- operator transfers the one-time payment within 30 working days after document submission.

Current operator payment page:
- https://www.tamizshahar.az/az/neqliyyat-utilizasiyasi/fond/tesdiqedici-senedler-uzre-odenisler

## Current registered execution venues
The operator's August-2026 indexed registry lists four registered utilizers, including two Baku/Absheron-area venues:
- Fors LLC — Baku, Mashtaga;
- Fast Track LLC — Absheron, Hokmeli;
- Semsan — Ganja;
- Eco Metal — Sumgait.

Source:
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/utilizatorlar/reyestrde-qeyde-alinan-utilizatorlar

The page states initial applications are accepted through `nvu.gov.az`.

## Economics
Current H067 market evidence remains:
- observed intermediary benchmark: 900 AZN immediate versus 1,050 AZN delayed;
- gross spread = 150 AZN;
- gross return on a 900-AZN acquisition = 16.6667% before costs.

The issuance-contingent structure changes risk rather than face economics: it moves payment after the official certificate exists, eliminating the need to assume an unknown secondary-market paper is genuine.

For any transaction:

`guaranteed_net = 1,050 - P - transport - deregistration/document costs - bank costs - taxes - other locked execution costs`

Terminal SUCCESS requires the entire right-hand cost side to be hard-bounded below 1,050 before payment.

## Tax gate materially narrowed, not fully closed
The one-time utilization payment is financed from the Vehicle Utilization Fund, which is a targeted fund within the Azerbaijan state budget.

Tax Service guidance on Tax Code Article 102.1.4 states that individual one-time payments/material assistance paid from state-budget funds under Azerbaijan laws / qualifying state decisions are exempt from personal income tax.

Relevant sources:
- Vehicle Utilization Fund creation: https://president.az/az/articles/view/63388
- current Tax Service Article 102.1.4 explanation: https://www.taxes.gov.az/az/page/suallar-ve-cavablar?page=13

This creates a **strong tax-exemption argument for the 1,050-AZN fund payment itself**, because the payment is a statutory individual one-time payment funded from a state-budget fund. However no tax-authority page was found that applies Article 102.1.4 specifically to vehicle-utilization certificates. Therefore the project must not yet treat tax as conclusively zero for terminal SUCCESS.

Secondary-market/repeated trading could also create separate entrepreneurial-tax questions even if the state payment itself is exempt.

## New live-market search
Fresh indexed search reconfirmed the active Lalafo search result containing:
`Utilizasiya boş kuzalarin qebulu. baki. hemin gun 900m 1 ay 1050m`

The broader `boş kuza` marketplace also exposes cheap shell listings, including a 300-AZN empty-body listing in Shirvan. That 300-AZN listing is **not yet an arbitrage candidate**, because the public ad does not prove current registration/title, permanent-deregistration eligibility or that the shell can generate a confirmation document. It is evidence only that raw bodies can trade far below redemption face value.

A fresh titled/damaged-vehicle screen further narrows the acquisition route:
- a July-2026 Lalafo VAZ 2106 listing explicitly says `sənədləri var` and asks **2,000 AZN**;
- current indexed `qəzalı` passenger-car search exposes low examples around **1,900 AZN**;
- both are already above the 1,050-AZN M1/N1 cash redemption before transport/deregistration costs.

Therefore **buying an entire documented vehicle at ordinary classified-market prices is not the promising arbitrage leg**. The economically plausible route is seller-authorized surrender / revenue-sharing: the owner retains no need to sell the entire vehicle asset to us, but agrees to transfer the official certificate after issuance for an amount below face value.

Derived screen:
- `data/derived/h067b_live_asset_screen.csv`

## What is now proven
- transferable certificate mechanism: **PROVEN by statute**;
- certificate issuance after accepted private-vehicle surrender: **PROVEN**, within 2 working days;
- presenter can redeem for one-time payment via NVU/operator: **PROVEN operator workflow**;
- registered utilizers currently exist in Baku/Absheron/Ganja/Sumgait: **PROVEN current registry**;
- below-face immediate market valuation (900 vs 1,050): **OBSERVED live market signal**;
- issuance-contingent structure removes unknown-paper authenticity as a necessary pre-payment risk: **PROVEN transaction-design improvement**;
- ordinary documented-vehicle acquisition at current indexed prices is **economically inferior** to certificate/revenue-sharing acquisition.

## What still blocks SUCCESS
1. No specific vehicle owner has agreed to a price below `1,050 - all bounded costs` under **payment-after-official-issuance** terms.
2. Exact deregistration/transport/document costs for a concrete vehicle are not locked.
3. Tax treatment has a strong exemption argument but is not yet specifically confirmed for this payment by the State Tax Service.
4. No actual issued certificate is currently locked to the project.

## Decision
H067 remains the strongest current deterministic-cash path, and its verification problem is now substantially reduced.

The next highest-value step is no longer blind serial-number validation research or outright vehicle purchase. It is **counterparty discovery for a private owner willing to exchange the post-issuance certificate for <=900–950 AZN**, ideally using payment only after the registered utilizer has issued the original, plus a hard transaction-cost/tax confirmation.

Terminal state remains **NO SUCCESS; NOT EXHAUSTED**.
