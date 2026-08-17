# H067i — transferee redemption entitlement closure

Updated: 2026-08-18
Status: **operator-side transferee entitlement closed by primary law; tax interpretation strengthened but still not enough for terminal SUCCESS without live executable document acquisition / verification**

## Question
If a natural person acquires an already-issued unused vehicle-utilization confirmation document from another person, can the transferee/holder lawfully redeem it for the one-time payment, despite not being the original vehicle surrenderer?

## Primary-law closure
The current Waste Law, Article 14-8, contains all three required links:

1. The confirmation document is valid for 3 years, single-use, **unnamed**, and **may be used by another person** (`adsızdır və başqa şəxs tərəfindən də istifadə edilə bilər`).
2. A **person holding the confirmation document** may choose the one-time payment instead of the new-vehicle discount (`Təsdiqedici sənədə malik şəxs ... birdəfəlik ödəniş ala bilər`).
3. The operator must transfer the one-time payment from the Vehicle Utilization Fund to the account of the **person presenting the confirmation document** within 30 working days (`təsdiqedici sənədi təqdim edən şəxsin hesabına`).

Primary law:
- https://frameworks.e-qanun.az/3/f_3186.html

This is stronger than an inference from marketing/FAQ text: the statute itself does not condition cash redemption on being the original vehicle surrenderer.

## Operator procedure independently matches the statute
Təmiz Şəhər, the appointed operator, states that:
- a confirmation document is unnamed and may be used by another person;
- a person can choose the 70% one-time payment;
- for cash redemption the applicant enters the document information in the nvu.gov.az personal account and presents to the operator:
  - original confirmation document(s),
  - identity card,
  - applicant's bank-account details;
- the operator transfers the one-time payment to the **applicant's** account within 30 working days.

Operator sources:
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/tesdiqedici-senedler-barede
- https://www.tamizshahar.az/az/neqliyyat-utilizasiyasi/fond/tesdiqedici-senedler-uzre-odenisler
- https://www.tamizshahar.az/az/neqliyyat/sual-cavab

Notably, the published cash-redemption checklist does **not** require the original surrenderer's identity, title to the scrapped vehicle, a transfer contract, or proof that the applicant was the surrenderer. The original strict-accountability confirmation document itself is the entitlement instrument.

## Tax result strengthened
Current Tax Code Article 102.1.4 exempts, among other items, individual one-time payments made from state-budget funds on the basis of Azerbaijani laws / qualifying executive decisions.

Official State Tax Service guidance applies this clause to natural-person and even individual-entrepreneur recipients of qualifying state-budget support payments, instructing that such receipts are income-tax exempt. This supports a **payment-character** interpretation rather than an exemption tied to how the recipient obtained eligibility.

Sources:
- current Tax Code Article 102.1.4: https://frameworks.e-qanun.az/0/c_c_12.html
- State Tax Service Q&A: https://www.taxes.gov.az/az/page/suallar-ve-cavablar?page=207
- State Tax Service Q&A: https://www.taxes.gov.az/az/page/suallar-ve-cavablar?page=140

Combined with H067h's already-established chain that the Vehicle Utilization Fund is within the Azerbaijan state budget and the Waste Law expressly labels the redemption a `birdəfəlik ödəniş`, the tax-exemption case is now materially stronger.

### Remaining tax caveat
No published State Tax Service ruling was found addressing this exact arbitrage fact pattern: a natural person buys an unused unnamed confirmation document from another private person and redeems it. Therefore a terminal legal guarantee still should not rely solely on inference if the purchase price requires tax exemption to remain profitable.

## Execution / verification implications
The operator expressly keeps the accounting registry of confirmation documents. Cash redemption requires adding document information in the nvu.gov.az personal account and then presenting the original document. This suggests a strong practical pre-payment gate:

1. seller provides original document and series/number;
2. buyer/operator confirms document is recognized, within 3-year validity and unused before irreversible payment;
3. buyer confirms the document can be added for one-time-payment use in buyer's own nvu.gov.az account or obtains operator verification;
4. only then exchange payment against physical original;
5. submit original + buyer ID + buyer bank details;
6. operator pays buyer within statutory 30-working-day period.

The portal's behavior for a transferred document was not directly observed in this research runtime, so step 3 remains a live execution gate rather than a proven UI feature.

## Economics
For M1/M1G/N1/N1G redemption `R=1,050 AZN`:

`profit = 1,050 - acquisition price - locked costs - tax(if any)`.

If Article 102.1.4 exemption is accepted and locked costs are 20 AZN:
- buy at 900 -> 130 AZN gross execution profit;
- buy at 950 -> 80 AZN;
- buy at 970 -> 60 AZN;
- buy at 980 -> 50 AZN.

For a strict safety margin, prefer <=950 AZN unless tax treatment is confirmed product-specifically.

## Current conclusion
**Operator-side transferee cash-redemption entitlement is CLOSED in favor of the strategy by primary law and current operator procedure.**

H067 is now blocked mainly by execution, not by legal transferability:
- find a live already-issued unused document at a price leaving a positive all-in floor;
- verify validity/unused status before payment;
- verify the transferred document is accepted in the buyer's own portal/application workflow;
- lock tax treatment or retain enough price margin to survive an adverse tax interpretation;
- lock all incidental costs.

Do not mark SUCCESS until a currently executable acquisition satisfying those gates is identified and the worst-case cash floor is strictly positive.
