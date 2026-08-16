# H052 — upfront interest + insured principal

Updated: 2026-08-17
Status: **PROMISING MECHANISM; strict guarantee not yet proven because insurance-event accounting for prepaid interest is unresolved**

## Question
Can a currently available Azerbaijan deposit pay a positive cash reward immediately while the original principal remains protected by the Deposit Insurance Fund, creating a deterministic `principal + reward` terminal floor?

## Current products found
### Expressbank — Əlavə fürsət
Current official product material states:
- AZN deposit;
- minimum 500 AZN;
- 12/18/24-month terms;
- interest paid **in advance**;
- current indexed rate about 9.5% (official page has recently shown 9.5–10% depending crawl date);
- deposit amount is described as insured by the Deposit Insurance Fund, subject to statutory limits.

Official product page:
- https://www.expressbank.az/az/deposit/elave-furset

The bank's official 2022 launch note explicitly says the customer can receive the annual income **on the day the deposit is opened**.

### VTB Azerbaijan — Avans
Current official product material states:
- AZN deposit;
- minimum 500 AZN;
- 12–36 months;
- interest obtained immediately after the deposit is registered;
- current table: 1y 9.25%, 1.5y 9.5%, 2y 8.75%, 3y 7.75%.

Official product page:
- https://vtb.az/personal/deposits/advance-savings/

## Statutory insurance anchor
Current Azerbaijan Deposit Insurance Law defines a protected deposit and provides compensation equal to 100% of the insured deposit balance, subject to the current 100,000-AZN cap. Interest is compensated only in the amount accrued up to the insurance-event date.

Primary sources:
- https://www.cbar.az/law-5/law-on-deposit-insurance?language=en
- https://frameworks.e-qanun.az/12/f_12137.html

This fixes H051's ordinary-accrual problem only **if** the prepaid interest is already separately vested and the insured deposit balance remains the original principal.

## Guarantee identity
Let:
- `P` = cash deposited;
- `R` = net upfront cash interest actually credited and withdrawable at opening;
- `C` = minimum insurance/maturity principal recovery across every allowed branch;
- `F` = unavoidable fees/taxes/funding costs.

Worst-case terminal net profit:

`G = R + C - P - F`.

A strict guarantee requires `G > 0`.

If the prepaid reward is separately vested and `C=P`, then any `R>F` creates a deterministic positive floor.

If insolvency/early-termination accounting instead reduces the insured/recoverable balance to `P-R` (or permits clawback/setoff of `R`), then `G <= 0` before costs and the mechanism fails.

## Illustrative minimum-size screen
At 500 AZN:
- 9.5% one-year upfront interest = 47.50 AZN gross;
- even a hypothetical 10% tax on the reward leaves 42.75 AZN;
- if full 500 AZN principal is independently recoverable in every insurance branch and the reward cannot be clawed back, this would satisfy the numerical positive-floor condition before any account/withdrawal fees.

This is **not yet a SUCCESS claim** because the legal/accounting premise is unproven.

## Crucial unresolved contract question
The public product pages say both “interest paid in advance” and “deposit insured,” but they do not publish enough product-specific liquidation language to prove whether, after the upfront payment:
1. the bank ledger continues to show the full `P` as the protected deposit balance;
2. the prepaid interest is irrevocably the depositor's separate property;
3. an insurance event cannot trigger contractual/statutory setoff, recoupment, or a principal reduction equal to unearned prepaid interest.

Older/general Azerbaijan deposit forms show that some prepaid-interest products deduct already-paid interest from principal when the **customer voluntarily terminates early**. That does not automatically prove the same treatment in an insurance event, but it is enough to block a strict theorem without the current product contract or an authoritative written interpretation.

Expressbank's current general conditions confirm deposit-insurance mechanics and ordinary early-withdrawal rights, but the public general document defers product-specific early-interest recalculation to the individual deposit agreement. Therefore the decisive clause remains outside the currently retrieved public material.

## Result
**H052 is the strongest current principal-protection lead so far, but remains INCONCLUSIVE rather than SUCCESS.**

The next decisive evidence is narrow and practical: obtain the current Expressbank `Əlavə fürsət` and/or VTB `Avans` deposit agreement / standard information form, specifically the clauses for prepaid interest under bank insolvency, forced liquidation, insurance compensation, setoff and early termination. If the full insured principal survives after the upfront cash has vested, H052 can be promoted immediately to a candidate terminal guarantee after fees/tax are bounded.
