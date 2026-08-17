# H067h — state-budget tax-exemption lead for scrappage one-time payment

Updated: 2026-08-18
Status: **materially stronger legal tax case; product-specific confirmation still required before SUCCESS**

## Question
Can the fixed one-time payment received by the holder of an unused transferable vehicle-utilization confirmation document qualify for Azerbaijan personal-income-tax exemption under Tax Code Article 102.1.4?

## New authoritative chain
### 1. The utilization payment is created by law
The current Waste Law (`İstehsalat və məişət tullantıları haqqında`) Article 14-8 provides that the holder of a valid confirmation document may choose a lower **one-time payment** instead of the new-vehicle discount. The operator must transfer this one-time payment from the vehicle-utilization fund within 30 working days after submission.

Primary law:
- https://frameworks.e-qanun.az/3/f_3186.html

### 2. The vehicle-utilization fund is explicitly inside the state budget
Presidential Order dated 27 January 2024 states explicitly:

`Azərbaycan Respublikası dövlət büdcəsinin tərkibində “Nəqliyyat vasitələrinin utilizasiyası fondu” yaradılsın.`

In English: create the Vehicle Utilization Fund **within the state budget of the Republic of Azerbaijan**.

Primary source:
- https://president.az/az/articles/view/63388

The Waste Law also defines the fund as a `məqsədli büdcə fondu` (targeted budget fund).

The Budget System Law defines targeted budget funds as funds formed within the state budget, Nakhchivan budget, or local budgets and states that such funds may have independent revenue sources. It also provides that their transactions are executed through Treasury.

Primary source:
- https://frameworks.e-qanun.az/1/f_1126.html

The current 2026 Cabinet of Ministers amendment to the Vehicle Utilization Fund rules also requires unused year-end balances to move to the single Treasury account, reinforcing the state-budget/Treasury character.

Current source:
- https://nk.gov.az/az/senedler/qerarlar/azerbaycan-respublikasi-nazirler-kabinetinin-dovle-9443

### 3. Tax Code Article 102.1.4 exempts individual one-time payments from the state budget
Current Tax Code Article 102.1.4 exempts from personal income tax, among other items, individual one-time payments or material aid made from state-budget funds on the basis of Azerbaijani laws / qualifying executive decisions.

Current Tax Code:
- https://frameworks.e-qanun.az/46/f_46948.html

The State Tax Service repeatedly applies Article 102.1.4 to state-budget one-time support payments and states that such amounts are exempt from personal income tax.

Official examples:
- https://www.taxes.gov.az/az/page/suallar-ve-cavablar?page=207
- https://taxes.gov.az/az/page/suallar-ve-cavablar?page=35

## Legal-fit argument
The H067 redemption payment appears to satisfy the three core factual limbs of Article 102.1.4:
1. **individual one-time payment** — the Waste Law expressly calls it `birdəfəlik ödəniş`;
2. **created by law** — Waste Law Article 14-8 establishes the entitlement/payment;
3. **paid from state-budget funds** — the Presidential Order explicitly creates the Vehicle Utilization Fund within the state budget, and the payment is made from that fund.

This is significantly stronger than the prior fallback analysis that assumed either 14% on gross receipt or 14% on gain.

## Why this is not yet terminal SUCCESS
The exact combination — a natural person who **purchased/transferred into possession** an unused unnamed confirmation document and then redeems it — has not been found in a published State Tax Service ruling/FAQ.

Two residual classification questions remain:
- whether Article 102.1.4 applies to any lawful holder of the confirmation document, including a transferee who did not surrender the original vehicle;
- whether the tax authority could treat acquisition and resale/redemption of multiple documents as business activity rather than a one-off personal receipt.

The first question matters to a single-arbitrage execution; the second mainly matters to scaling/repetition.

## Updated economics if exemption applies
For M1/M1G or N1/N1G fixed redemption `R = 1,050 AZN`:

`net redemption = 1,050 AZN` before execution costs.

If acquisition price is `A` and locked execution cost is `C`:

`profit = 1,050 - A - C`.

With `C = 20 AZN` and a required 50-AZN safety margin:

`A <= 980 AZN`.

Examples:
- A=900, C=20 -> profit **130 AZN**;
- A=950, C=20 -> profit **80 AZN**;
- A=970, C=20 -> profit **60 AZN**;
- A=980, C=20 -> profit **50 AZN**.

This makes the previously observed 900–950 AZN market band potentially executable if document validity and redemption entitlement can be locked before payment.

## Updated execution gate
Before irreversible payment require all of the following:
1. original unused confirmation document exists;
2. the document is within its 3-year validity and unused;
3. official/operator-side verification sufficient to rule out prior redemption/cancellation;
4. seller transfers the original document atomically against payment;
5. holder/transferee redemption entitlement is confirmed by operator procedure;
6. **written State Tax Service or operator/tax-agent confirmation that Article 102.1.4 applies to this one-time payment for the transferee**, or transaction price remains profitable under the previous adverse tax fallback;
7. all bank/transport/notary/verification costs are locked before payment;
8. worst-case cash floor after all locked costs is strictly positive with safety margin.

## Current conclusion
H067h materially upgrades the tax side. The strongest current legal reading is no longer merely `14% of net gain`; there is a credible direct statutory **income-tax exemption** because the payment is an individual one-time payment established by law and financed from a fund expressly created within the state budget.

However, do **not** mark SUCCESS until the transferee-specific application of Article 102.1.4 and document validity/redemption execution are locked in writing or by an authoritative product-specific source.
