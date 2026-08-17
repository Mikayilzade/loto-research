# H067g — tax-basis correction + deregistration-fee closure attempt

Updated: 2026-08-18
Status: **materially improved economics; strict guarantee still blocked on product-specific tax classification**

## Question
For a natural person who lawfully acquires an unused unnamed vehicle-utilization confirmation document and then redeems it for the fixed one-time payment, is the 14% Azerbaijani non-business income tax applied to the entire 1,050 AZN receipt or only to net economic gain after acquisition/related costs? Also, is there a separate state duty for permanent deregistration before utilization?

## 1. Authoritative tax-law baseline
Current Tax Code / State Tax Service sources establish:
- Tax Code Article 101.2: annual non-business income is taxed at **14%**.
- Tax Code Article 99.3 includes non-business income and specifically covers gains reflecting an increase in the initial value of assets when disposed.
- State Tax Service tax guide says that for non-business income not taxed at source, taxable income is generally the difference between taxable receipts and expenses deductible under Chapter X.
- State Tax Service FAQ on securities explicitly says acquisition cost and related expenses are deducted before applying 14%.
- State Tax Service crypto guidance likewise treats taxable income as the increase between acquisition and disposal value, not gross sale proceeds.

Primary sources:
- https://frameworks.e-qanun.az/46/f_46948.html
- https://www.taxes.gov.az/az/page/vergi-beledcisi
- https://www.taxes.gov.az/az/page/faq
- https://www.taxes.gov.az/az/page/suallar-ve-cavablar?page=4

## 2. Implication for H067 certificate arbitrage
The utilization law states that the confirmation document is:
- valid for 3 years;
- single-use;
- **unnamed**;
- usable by another person;
- redeemable by its holder for a one-time payment instead of the vehicle-purchase discount.

This makes the document economically similar to a transferable asset/right. However, no State Tax Service source was found that classifies this exact document or its redemption.

Therefore three tax scenarios must be kept separate:

### A. Explicit exemption / no tax
`net redemption = 1,050`

### B. 14% tax on economic gain after acquisition cost (currently the strongest general-law analogy)
If purchase price is `A` and deductible related costs are ignored for conservatism:

`tax = 0.14 * max(1,050 - A, 0)`

`net redemption after tax = 1,050 - tax = 903 + 0.14A`

Pre-other-cost profit:

`profit = 903 - 0.86A`

Examples:
- A=900 -> tax 21; net redemption 1,029; gross spread after tax **129 AZN**;
- A=950 -> tax 14; net redemption 1,036; spread **86 AZN**;
- A=1,000 -> tax 7; net redemption 1,043; spread **43 AZN**.

With 20 AZN execution cost + 50 AZN safety margin, required purchase price is:

`903 - 0.86A - 20 >= 50`

so:

`A <= 968.60 AZN`.

This is dramatically less restrictive than the prior gross-receipt stress model.

### C. 14% tax on entire 1,050 receipt (prior worst-case stress)
`net redemption = 903`.

With 20 AZN execution + 50 AZN safety margin:

`A <= 833 AZN`.

This remains the strict fallback until product-specific classification is locked.

## 3. Why the prior 800–830 search band should not be treated as the only economically plausible band
The State Tax Service's general non-business guidance says deductible costs normally reduce taxable income, and its securities/crypto examples tax gain rather than gross proceeds. Therefore taxing the full 1,050 receipt despite a documented purchase cost is a deliberately adverse stress case, not the best current tax-law model.

For research ranking:
- **<=833 AZN** remains safe under the harsh gross-tax stress;
- **~900–950 AZN** becomes economically attractive under the stronger gain-basis analogy;
- up to about **968 AZN** can still support a 50-AZN safety margin if total non-tax execution cost is only 20 AZN.

No SUCCESS claim is allowed until the State Tax Service/operator confirms that acquisition cost of a transferred confirmation document is deductible (or confirms exemption/no withholding).

## 4. Deregistration fee
Current official/legal sources confirm permanent deregistration is mandatory before utilization.

Current State Duty Law Article 18.65 enumerates fees for:
- technical inspection / changes to technical registration data;
- vehicle registration / transfer registration.

The searched current schedule does **not** expose a distinct state-duty line for permanent deregistration itself. The traffic-law / DYP deregistration rules describe surrender/removal from registration but do not identify a separate utilization-specific deregistration fee.

Sources:
- https://frameworks.e-qanun.az/2/f_2860.html
- https://frameworks.e-qanun.az/3/f_3423.html
- https://dyp.gov.az/index.php?/az/content/194/

Interpretation: evidence for a **zero separate deregistration duty is strengthened**, but absence from the searched schedule is not yet a formal agency confirmation. Do not budget a positive fee as fact; retain a small residual execution-cost reserve until confirmed.

## 5. Current legal-payment mechanism remains strong
The utilization law continues to establish:
- free acceptance by registered utilizer;
- confirmation document issued after surrender;
- unnamed/transferable nature;
- holder may choose the lower one-time payment;
- operator transfers the one-time payment within 30 working days after document submission.

Primary law:
- https://frameworks.e-qanun.az/3/f_3186.html

A June 19, 2026 public statement from the program reports more than 1m AZN already paid as one-time payments, confirming that the redemption channel is operational in practice.

Secondary current confirmation:
- https://report.az/ekologiya/utilizasiya-proqrami-cercivesinde-1687-nefere-yerli-istehsal-yeni-avtomobil-teqdim-edilib

## 6. Updated executable gate
Best transaction structure remains **post-issuance acquisition of an unused original confirmation document**, not buying a questionable vehicle first.

Before irreversible payment require:
1. original document exists and is unused;
2. document identity/validity is verified with operator/utilizer as far as official process permits;
3. seller transfers original document only against payment;
4. purchase price and transaction costs are documented;
5. tax treatment is confirmed in writing or worst-case gross-tax economics still leave positive margin;
6. redemption application is immediately executable.

## Current conclusion
H067 is **stronger than at H067f**. The earlier 14%-of-gross stress is not the strongest general-law interpretation once the certificate itself is purchased for consideration. General State Tax Service guidance supports a gain-basis model, which would make a 900–950 AZN certificate materially profitable after tax if confirmed.

But strict guaranteed profit is **not yet proven** because the exact utilization-document tax classification/deductibility has not been authoritatively answered.
