# H052 — upfront interest + insured principal

Updated: 2026-08-17
Status: **PROMISING MECHANISM, BUT STRICT GUARANTEE STILL UNPROVEN; new contract evidence materially weakens the favorable interpretation**

## Question
Can a currently available Azerbaijan deposit pay a positive cash reward immediately while the original principal remains protected by the Deposit Insurance Fund, creating a deterministic `principal + reward` terminal floor?

## Current products found
### Expressbank — Əlavə fürsət
Current official product material states:
- AZN deposit;
- minimum 500 AZN;
- 12/18/24-month terms;
- interest paid **in advance**;
- current rate table: 12m 9.50%, 18m 9.00%, 24m 9.00%;
- product page expressly says the **deposit amount** is insured by the Deposit Insurance Fund up to the statutory limit.

Primary source:
- https://www.expressbank.az/az/deposit/elave-furset

The bank's launch note also states that the annual income can be taken **on the day the deposit is opened**:
- https://www.expressbank.az/az/news/expressbank-in-elave-furset-emaneti-ile-pulunuz-derhal-gelir-getirsin

### VTB Azerbaijan — Avans
Current official product material states:
- AZN deposit;
- minimum 500 AZN;
- 12–36 months;
- interest is available immediately after registration;
- current page observed on 2026-08-17: 12m 9.0%, 18m 9.25%, 24m 8.5%, 36m 7.5%;
- same page states compensation under the Deposit Insurance Law is 100% of the insured deposit, capped at 100,000 AZN.

Primary source:
- https://vtb.az/personal/deposits/advance-savings/

## Statutory insurance anchor — strengthened
The current Azerbaijan Deposit Insurance Law gives several exact constraints:

1. `Deposit` means money accepted by the bank that it must repay under law/contract, including accrued interest.
2. Compensation is **100% of the insured deposit**, capped at 100,000 AZN per participant bank.
3. If, on the insurance-event date, the depositor has a **due obligation to the bank**, the unperformed amount is deducted from the protected deposit before compensation.
4. Interest is compensated only to the amount accrued by the insurance-event date.
5. Crucially, an unexpired deposit is deemed **matured** when the compensation announcement is first published.

Primary sources:
- https://frameworks.e-qanun.az/12/f_12137.html
- https://www.cbar.az/page-73/questions-and-answers

This is important because statutory forced maturity is not textually identical to a customer's voluntary early-withdrawal request. But it still does **not** prove that a product-specific prepaid-interest recoupment claim cannot become due at that point.

## New decisive warning evidence — prepaid interest can be secured against principal
A publicly indexed Azerbaijan general-offer form for a `Faizləri əvvəlcədən ödənilən müddətli əmanət` (prepaid-interest fixed deposit) contains a much stronger adverse mechanism than previously documented:

- all interest for the whole term is paid on placement day;
- an amount of principal equal to the prepaid interest is **blocked/encumbered in favor of the bank**;
- if the depositor demands the deposit early, the prepaid interest is deducted from principal without separate consent.

Indexed source:
- https://www.lawinsider.com/az/contracts/c0UFCKlTrfH

A related indexed general-offer version likewise states that already-paid interest is deducted from principal on early repayment:
- https://www.lawinsider.com/az/contracts/kn7gZJIdTZS

These documents are **not proven to be the current Expressbank or VTB contract**, so they cannot close those products directly. But they show that the favorable accounting assumption `upfront cash is independent of untouched principal` is not safe: Azerbaijan prepaid-interest products can legally implement the advance as a bank-secured amount against the deposit itself.

## Guarantee identity
Let:
- `P` = cash deposited;
- `R` = net upfront cash interest actually credited/withdrawable at opening;
- `C` = minimum principal recovery across every allowed branch;
- `F` = unavoidable tax/fees/funding/cash-out costs.

Worst-case terminal net profit:

`G = R + C - P - F`.

A strict guarantee requires `G > 0`.

### Favorable branch
If prepaid interest is independently vested and the insurance event leaves `C=P`, then:

`G = R - F > 0`

whenever reward exceeds costs.

### Adverse secured-advance branch
If the contract makes an amount `R` of principal security for the prepaid interest and that recoupment/setoff becomes due on forced termination/insurance event, then at best:

`C <= P-R`

and therefore:

`G <= R + (P-R) - P - F = -F`.

That branch destroys the strict guarantee even though the product is advertised as an insured deposit.

## Current tax/cost observations
Expressbank's current product page states:
- up to 200 AZN of monthly calculated AZN deposit-interest income per bank is tax-exempt under the current rule;
- AZN deposits of 18+ months have a broader exemption when principal is not paid earlier than 18 months;
- the product page advertises a deposit-type bank card with the deposit.

At the 500-AZN minimum, gross upfront interest is roughly 45–47.50 AZN depending product/rate. Even a 10% tax would not eliminate the numerical margin **if** full principal survival were proved. Therefore tax is secondary; the principal-recoupment clause remains decisive.

## Current conclusion
H052 is **not SUCCESS**.

The new evidence changes the state from `purely unknown` to `material adverse precedent exists`:
- prepaid interest can be legally implemented as an advance secured by a blocked portion of principal;
- Deposit Insurance Law deducts due obligations to the bank from compensation;
- therefore a strict theorem requires the **current product-specific Expressbank/VTB contract** to prove that forced maturity / bank insolvency does not activate recoupment, setoff, lien enforcement or principal reduction for prepaid unearned interest.

The fact that the public product page says `deposit amount is insured` is not sufficient by itself because insurance compensation is calculated after statutory deductions for due bank claims.

## Decisive next evidence
Recover one of:
1. current Expressbank `Əlavə fürsət` individual agreement / standard terms;
2. current VTB `Avans` agreement / general conditions;
3. written ADIF/bank interpretation explicitly answering whether full original principal remains compensable after prepaid interest has already been withdrawn and an insurance event occurs before contractual maturity.

A favorable explicit clause can still promote H052 immediately. An explicit lien/recoupment clause triggered by bank insolvency/forced maturity would reject H052 as a terminal guarantee.
