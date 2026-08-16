# H052 — upfront interest + insured principal

Updated: 2026-08-17
Status: **PROMISING MECHANISM, NOT SUCCESS; VTB current general terms materially narrow the decisive gap**

## Question
Can a currently available Azerbaijan deposit pay a positive cash reward immediately while the original principal remains protected by the Deposit Insurance Fund, creating a deterministic `principal + reward` terminal floor?

## Current products
### Expressbank — Əlavə fürsət
Official product material currently states:
- AZN deposit;
- minimum 500 AZN;
- 12/18/24-month terms;
- interest paid **in advance**;
- current published rates 9.50% / 9.00% / 9.00%;
- the deposit amount is insured by the Deposit Insurance Fund.

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

## NEW — current VTB general deposit agreement recovered
VTB's official documents page publishes the latest retail `Bank Xidmətlərinin Göstərilməsi haqqında Müqavilənin Ümumi Şərtləri`, effective **06.01.2025** and still the newest posted retail general-terms version on the 2026-08-17 documents page.

Primary source:
- https://vtb.az/about-bank/documents/
- linked PDF: `Bank Xidmətlərinin Göstərilməsi haqqında Müqavilənin Ümumi Şərtləri`, effective 06.01.2025.

### Clauses that matter
The deposit section (section 6) says:

- **6.1**: deposit amount, rate, term, product and other important conditions are specified in the individual Application-Agreement (`Ərizə-Razılaşma`).
- **6.11**: the customer may demand the deposit before maturity; in that case it is returned according to law.
- **6.12**: the procedure and amount for paying deposit interest **early at the customer's request** are determined by the Application-Agreement.
- **6.13**: when the customer requests early return of the deposit, interest is recalculated according to the relevant Application-Agreement.
- **6.14**: when the 6.12 case occurs — explicitly described as **early withdrawal of the deposit** — previously paid deposit interest is deducted from the deposit amount under the General Terms/Application-Agreement, then the Application-Agreement is terminated.
- **6.18**: the deposit-account agreement is cancelled after the deposit is fully returned to the depositor.
- **6.21**: on an insurance event, if the depositor has a matured obligation to the bank, compensation is paid on the protected-deposit remainder after that unperformed matured obligation is deducted.

This is materially more informative than the prior generic adverse precedent.

## Important distinction created by the recovered VTB terms
The VTB recoupment language recovered in clause 6.14 is tied to a **customer-requested early withdrawal** under 6.12/6.13. It is not written as a general clause automatically recouping prepaid interest whenever the bank enters insolvency or whenever the Deposit Insurance Law matures the deposit by operation of law.

The Deposit Insurance Law separately says:
- insured compensation is 100% of insured deposit up to 100,000 AZN;
- due obligations of the depositor to the bank are deducted;
- interest is compensated only through the insurance-event date;
- an unexpired deposit is deemed **matured** on first publication of the compensation announcement.

Primary statutory sources:
- https://frameworks.e-qanun.az/12/f_12137.html
- https://adif.gov.az/az/insured-deposit

### Why this helps
A statutory insurance-event maturity is not textually the same event as the customer asking for `vaxtından əvvəl` return under VTB clauses 6.11–6.14. The current public VTB general terms therefore **do not themselves establish** that the prepaid amount becomes a due depositor obligation on the insurance-event branch.

This weakens the earlier worst-case assumption that VTB necessarily has an insolvency-triggered claim for the entire unearned advance.

### Why this is still not SUCCESS
Clause 6.1 makes the **individual Application-Agreement** decisive for product-specific important conditions, and clause 6.12 explicitly delegates the early-interest procedure/amount to that document.

The public search did not recover the current `Avans` Application-Agreement. That missing document could still contain any of:
- a lien/block over principal equal to prepaid interest;
- an automatic recoupment clause on any termination/maturity event;
- a definition making statutory forced maturity equivalent to early termination for prepaid-interest accounting;
- a separate due repayment obligation for unearned prepaid interest.

If any such obligation is already due on the insurance-event date, Deposit Insurance Law article 26.2 / VTB 6.21 permits deduction before compensation.

Therefore the public VTB general terms materially improve the candidate but are insufficient for the project's strict all-branches guarantee standard.

## Prior adverse precedent retained
A publicly indexed Azerbaijan general-offer form for a `Faizləri əvvəlcədən ödənilən müddətli əmanət` states that:
- full-term interest is paid on placement day;
- principal equal to prepaid interest is blocked/encumbered in the bank's favor;
- on early demand, prepaid interest is deducted from principal without separate consent.

Indexed sources:
- https://www.lawinsider.com/az/contracts/c0UFCKlTrfH
- https://www.lawinsider.com/az/contracts/kn7gZJIdTZS

These are not proven to be current Expressbank/VTB agreements. They remain a warning that product-specific terms cannot be inferred from the marketing page alone.

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
If the VTB Application-Agreement does **not** create a matured recoupment obligation on statutory insurance-event maturity, then `C=P` (within insurance limits) and:

`G = R - F`.

At the 500-AZN minimum and current 12-month 9.25% rate, gross upfront reward is roughly **46.25 AZN** before any applicable tax/costs. The numerical margin is large relative to ordinary account/card fees, so contract treatment — not arithmetic — is the bottleneck.

### Adverse secured/recoupment branch
If product-specific terms make `R` (or the unearned part of it) a due obligation at insurance event, then potentially:

`C <= P-R`

and:

`G <= R + (P-R) - P - F = -F`.

That branch destroys strict guarantee.

## Current conclusion
H052 remains **PROMISING / INCONCLUSIVE — not SUCCESS**.

The key new result is narrower than before:
- VTB's current official general deposit terms have now been recovered;
- they expressly recoup previously paid interest on **customer-requested early withdrawal**;
- they do **not publicly state in the general deposit section** that an insurance event itself triggers the same recoupment;
- statute separately treats unexpired deposits as matured for compensation;
- therefore the remaining uncertainty has collapsed mainly to the product-specific `Avans` Application-Agreement / authoritative bank-ADIF interpretation.

## Decisive next evidence
Recover one of:
1. current VTB `Avans` `Ərizə-Razılaşma` / individual deposit agreement;
2. current Expressbank `Əlavə fürsət` individual agreement / standard terms;
3. written VTB/ADIF interpretation explicitly answering whether previously paid `Avans` interest becomes a due depositor obligation when an insurance event occurs before the original contractual end date.

A favorable explicit clause preserving full compensable principal after the prepaid cash has vested would immediately trigger the final tax/fees/cash-out bound and could promote H052 to terminal SUCCESS. An insolvency/forced-maturity recoupment clause would reject the candidate.