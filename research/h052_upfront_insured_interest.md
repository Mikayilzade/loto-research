# H052 — upfront interest + insured principal

Updated: 2026-08-17
Status: **PROMISING MECHANISM, NOT SUCCESS; both VTB and Expressbank are now narrowed mainly to product-specific agreements**

## Question
Can a currently available Azerbaijan deposit pay a positive cash reward immediately while the original principal remains protected by the Deposit Insurance Fund, creating a deterministic `principal + reward` terminal floor?

## Current products
### Expressbank — Əlavə fürsət
Official current product material states:
- AZN deposit;
- minimum 500 AZN;
- 12/18/24-month terms;
- interest paid **in advance**;
- current published rates 9.50% / 9.00% / 9.00%;
- the deposit amount is insured by the Deposit Insurance Fund;
- the product page advertises a free deposit card.

Primary sources:
- https://www.expressbank.az/az/deposit/elave-furset
- https://www.expressbank.az/az/news/expressbank-in-elave-furset-emaneti-ile-pulunuz-derhal-gelir-getirsin

### VTB Azerbaijan — Avans
Official current product material states:
- AZN deposit;
- minimum 500 AZN;
- 12–36 months;
- interest is available immediately after registration;
- current page observed 2026-08-17: 12m 9.25%, 18m 9.50%, 24m 8.75%, 36m 7.75%;
- product remains listed by VTB among retail deposits.

Primary sources:
- https://vtb.az/personal/deposits/advance-savings/
- https://vtb.az/personal/deposits/

## VTB — current general deposit agreement recovered
VTB's official documents page publishes the latest retail `Bank Xidmətlərinin Göstərilməsi haqqında Müqavilənin Ümumi Şərtləri`, effective **06.01.2025** and still the newest posted retail general-terms version on the 2026-08-17 documents page.

Primary source:
- https://vtb.az/about-bank/documents/
- linked PDF: `Bank Xidmətlərinin Göstərilməsi haqqında Müqavilənin Ümumi Şərtləri`, effective 06.01.2025.

### Clauses that matter
The deposit section says:
- **6.1**: deposit amount, rate, term, product and other important conditions are specified in the individual Application-Agreement (`Ərizə-Razılaşma`).
- **6.11**: the customer may demand the deposit before maturity; in that case it is returned according to law.
- **6.12**: the procedure and amount for paying deposit interest **early at the customer's request** are determined by the Application-Agreement.
- **6.13**: when the customer requests early return of the deposit, interest is recalculated according to the relevant Application-Agreement.
- **6.14**: when the 6.12 case occurs — explicitly described as **early withdrawal of the deposit** — previously paid deposit interest is deducted from the deposit amount under the General Terms/Application-Agreement, then the Application-Agreement is terminated.
- **6.18**: the deposit-account agreement is cancelled after the deposit is fully returned to the depositor.
- **6.21**: on an insurance event, if the depositor has a matured obligation to the bank, compensation is paid on the protected-deposit remainder after that unperformed matured obligation is deducted.

### VTB distinction
The recovered recoupment language is tied to **customer-requested early withdrawal**. It is not written as a general clause automatically recouping prepaid interest whenever the bank enters insolvency or whenever Deposit Insurance statutory maturity occurs.

The Deposit Insurance Law separately says an unexpired deposit is deemed **matured** on first publication of the compensation announcement. Statutory forced maturity is therefore not textually identical to the customer `vaxtından əvvəl` withdrawal branch in VTB 6.11–6.14.

This materially weakens the worst-case assumption that VTB necessarily has an insolvency-triggered claim for the entire unearned advance.

## NEW — Expressbank current publicly linked general terms recovered
Expressbank's official `Sənədlər toplusu` page currently links `Kredit və qeyri-kredit bank xidmətlərinin göstərilməsinin ümumi şərtləri`. The linked 30-page PDF contains a dedicated bank-deposit section.

Primary sources:
- https://www.expressbank.az/az/page/senedler-toplusu
- current linked PDF under `Kredit və qeyri-kredit bank xidmətlərinin göstərilməsinin ümumi şərtləri`.

### Expressbank clauses that matter
The publicly linked general deposit section states:
- **3.3.1–3.3.2**: the bank accepts the deposit and undertakes to return principal and pay interest; deposit type, amount, term and other necessary conditions are governed by the General Terms **and the relevant individual Agreement**.
- **3.3.4**: interest is ordinarily accrued from the day after funds enter the bank through the day before the principal is returned/removed, and is transferred to the customer's current account based on the customer's application.
- **3.3.6**: the bank must return at least one quarter of principal immediately on first demand and the balance within five bank days.
- **3.3.9–3.3.16**: the document describes Deposit Insurance participation, insurance-event compensation and the 100,000-AZN compensation ceiling; it also states that insurance compensates interest only through the insurance-event date.
- **3.3.17**: if principal is demanded before contractual maturity, interest is calculated according to the **relevant deposit Agreement**.

### Expressbank implication
The public general terms do **not** contain a general clause saying that a bank insolvency / Deposit Insurance event automatically makes already-paid advance interest repayable by the depositor, nor do they publicly create a lien equal to prepaid interest in the general deposit section.

However, they expressly delegate early-return interest accounting and other material product conditions to the relevant individual deposit Agreement. Therefore the same decisive uncertainty remains as at VTB: the `Əlavə fürsət` product-specific agreement could contain a recoupment, lien, block or set-off obligation that is absent from the public general terms.

The document also defines ordinary interest on a daily-accrual basis. This reinforces that the upfront payment is economically an advance against future accrual rather than proof that the entire annual interest is legally earned on day one. Without the individual agreement, it would be unsafe to assume the unearned part survives forced maturity.

## Deposit Insurance Law interaction
Current ADIF public material states:
- protected-deposit annual-rate ceiling: 12% in AZN;
- compensation: 100% of insured deposit up to 100,000 AZN;
- if the depositor has a matured obligation to the bank on the insurance-event date, that unperformed obligation is deducted from the protected amount;
- interest is compensated only through the insurance-event date.

Primary sources:
- https://adif.gov.az/az/insured-deposit
- https://adif.gov.az/az/secured-and-non-secured-deposit
- https://frameworks.e-qanun.az/12/f_12137.html

## NEW — minimum-size tax margin is not the bottleneck
Azerbaijan State Tax Service guidance on Tax Code article 102.1.22-3 states that up to **200 AZN of calculated monthly interest income per bank** on AZN deposits is exempt from income tax.

Primary source:
- https://taxes.gov.az/az/page/suallar-ve-cavablar (30.07.2025 answer concerning deposit-interest exemptions).

At the 500-AZN minimum:
- Expressbank 12m at 9.50% => gross advance ≈ **47.50 AZN**;
- VTB 12m at 9.25% => gross advance ≈ **46.25 AZN**.

Both are far below 200 AZN even if the whole annual amount is treated as received/calculated in a single month. Thus the minimum-size candidate has a large tax-exemption cushion; tax is unlikely to be the terminal blocker at the 500-AZN test size.

This does not prove the exact bank withholding implementation for prepaid interest, but even a hypothetical 10% withholding would leave ~41.6–42.8 AZN gross margin before other costs if full principal recovery were proven. Contractual recoupment remains overwhelmingly the decisive branch.

## Prior adverse precedent retained
A publicly indexed Azerbaijan general-offer form for a `Faizləri əvvəlcədən ödənilən müddətli əmanət` states that:
- full-term interest is paid on placement day;
- principal equal to prepaid interest is blocked/encumbered in the bank's favor;
- on early demand, prepaid interest is deducted from principal without separate consent.

Indexed sources:
- https://www.lawinsider.com/az/contracts/c0UFCKlTrfH
- https://www.lawinsider.com/az/contracts/kn7gZJIdTZS

These are not proven to be current Expressbank/VTB agreements. They remain a warning that product-specific terms cannot be inferred from marketing pages or generic terms alone.

## Guarantee identity
Let:
- `P` = cash deposited;
- `R` = net upfront cash interest actually credited and withdrawable at opening;
- `C` = minimum principal recovery across every allowed branch;
- `F` = unavoidable tax/fees/funding/cash-out costs.

Worst-case terminal net profit:

`G = R + C - P - F`.

Strict SUCCESS requires `G > 0` for every allowed branch.

### Favorable insurance-event branch
If the product-specific agreement does **not** create a matured recoupment obligation on statutory insurance-event maturity, then within insurance limits `C=P` and:

`G = R - F`.

At the minimum size, `R≈46.25–47.50 AZN` before any applicable cost. The numerical margin is large relative to ordinary retail account/card friction. Contract treatment — not arithmetic — is the bottleneck.

### Adverse secured/recoupment branch
If product-specific terms make `R` (or the unearned part) a due obligation at insurance event, then potentially:

`C <= P-R`

and:

`G <= R + (P-R) - P - F = -F`.

That branch destroys strict guarantee.

## Current conclusion
H052 remains **PROMISING / INCONCLUSIVE — not SUCCESS**.

New result this run:
- Expressbank's current publicly linked general deposit terms were recovered and reviewed;
- like VTB's general terms, they do not themselves state a blanket insolvency-triggered clawback of prepaid interest;
- Expressbank explicitly delegates early-return interest treatment to the individual deposit Agreement;
- therefore **both live Azerbaijan candidates have now collapsed to essentially the same product-specific-document gate**;
- the minimum 500-AZN tax arithmetic is favorable and not the main blocker.

The absence of a recoupment clause in generic terms is not evidence that none exists in the individual product contract.

## Decisive next evidence
Recover one of:
1. current VTB `Avans` `Ərizə-Razılaşma` / individual deposit agreement;
2. current Expressbank `Əlavə fürsət` individual agreement / standard terms;
3. written VTB/Expressbank/ADIF interpretation explicitly answering whether previously paid advance interest becomes a due depositor obligation when an insurance event occurs before original contractual maturity.

A favorable explicit clause preserving full compensable principal after the prepaid cash has vested would immediately trigger the final fee/cash-out bound and could promote H052 to terminal SUCCESS. An insolvency/forced-maturity recoupment or principal-lien clause would reject that candidate.