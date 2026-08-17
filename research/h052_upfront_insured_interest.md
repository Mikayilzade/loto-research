# H052 — upfront interest + insured principal

Updated: 2026-08-17
Status: **PROMISING MECHANISM, NOT SUCCESS; current law materially narrows the unresolved branch to product-specific matured recoupment at insurance event**

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

Material clauses already recovered:
- **6.1**: deposit amount, rate, term, product and other important conditions are specified in the individual Application-Agreement (`Ərizə-Razılaşma`).
- **6.11**: customer may demand the deposit before maturity.
- **6.12–6.14**: early-return interest accounting is governed by the Application-Agreement; previously paid interest may be deducted when the **customer requests early withdrawal**.
- **6.21**: on an insurance event, a matured obligation owed by the depositor to the bank is deducted before compensation.

The public VTB recoupment branch is textually tied to customer-requested early withdrawal, not expressly to statutory insurance-event maturity. That distinction remains favorable but not sufficient without the Avans Application-Agreement.

## Expressbank — current general terms recovered
Expressbank's current official `Sənədlər toplusu` page links a general banking-terms document with a dedicated deposit section.

Primary source:
- https://www.expressbank.az/az/page/senedler-toplusu

Material clauses already recovered:
- **3.3.1–3.3.2**: principal/interest obligations plus product-specific Agreement controls necessary conditions;
- **3.3.4**: ordinary deposit interest is accrued daily until return/removal of principal;
- **3.3.6**: principal-return obligation on demand;
- **3.3.9–3.3.16**: Deposit Insurance mechanics;
- **3.3.17**: early-return interest treatment is delegated to the relevant individual deposit Agreement.

The public general deposit section does not state that insolvency itself automatically claws back prepaid interest, but the individual agreement remains decisive.

## NEW 2026-08-17 — current Deposit Insurance Law removes two older blanket exclusions
Fresh review of the current consolidated official law (`Əmanətlərin sığortalanması haqqında`, e-qanun) materially improves the legal map.

Current Article 2 shows old clauses **2.1.2.9** and **2.1.2.10** struck/repealed:
- old 2.1.2.9 had excluded deposits to the extent of a depositor's debt principal + interest regardless of maturity;
- old 2.1.2.10 had excluded deposits serving as security for obligations to the bank.

These are **not current blanket exclusions** in the consolidated text.

Primary current law:
- https://frameworks.e-qanun.az/12/f_12137.html

This matters because the historical adverse prepaid-interest precedent involved a blocked/encumbered principal amount. Under the current statute, mere existence of a lien/security-style structure is no longer, by itself, enough to prove the deposit is outside protection.

### What still survives and is decisive
Current Article **26.2** remains: if, on the insurance-event date, the depositor has a **matured obligation** to the participant bank, the unperformed portion is deducted from the protected deposit (including calculated interest) before compensation.

ADIF's current public insured-deposit page repeats the same rule and states that compensation is 100% of insured deposit up to 100,000 AZN; deposit interest is compensated only through the insurance-event date.

Primary sources:
- https://adif.gov.az/az/insured-deposit
- https://frameworks.e-qanun.az/12/f_12137.html

Therefore the H052 legal decision tree is now narrower:

1. **If prepaid interest does not become a matured depositor obligation on insurance-event/forced maturity**, the old security/debt blanket exclusions no longer independently destroy coverage, and `C=P` remains plausible within the insurance limit.
2. **If the product-specific agreement makes unearned prepaid interest immediately due from the depositor on insurance-event/forced maturity**, Article 26.2 permits that matured obligation to reduce compensation, destroying the strict positive floor to that extent.

This is a materially stronger and more precise result than the earlier generic “lien may destroy insurance” concern.

## Fresh product-agreement search result
Broad current searches for:
- VTB `Avans` + `Ərizə-Razılaşma` / contract / PDF;
- Expressbank `Əlavə fürsət` + individual agreement / contract;
- ADIF interpretation specifically addressing prepaid interest on insurance event

still did **not** surface either current product-specific agreement or an authoritative published interpretation resolving forced-maturity recoupment.

Current official product pages continue to confirm immediate/prepaid interest and insured-deposit marketing, but not the missing clause.

A historical secondary source on Expressbank states that early withdrawal carried a penalty. This is consistent with the general-term delegation to product-specific early-return accounting, but it is not current authoritative evidence about insurance-event treatment and is not used as a terminal conclusion.

## Tax margin at minimum size
State Tax Service guidance says up to 200 AZN of calculated monthly interest income per bank on AZN deposits is exempt under Tax Code 102.1.22-3.

At the 500-AZN minimum:
- Expressbank 12m 9.50% => ~47.50 AZN gross upfront;
- VTB 12m 9.25% => ~46.25 AZN gross upfront.

Both sit far below the 200-AZN monthly exemption threshold. Tax remains secondary to contractual recoupment.

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

At the minimum size, `R≈46.25–47.50 AZN` before applicable costs.

### Adverse matured-obligation branch
If product-specific terms make all or part of `R` a due obligation at insurance event, then Article 26.2 permits compensation offset. If the full advance becomes due:

`C <= P-R`

and

`G <= R + (P-R) - P - F = -F`.

That branch destroys strict guarantee.

## Current conclusion
H052 remains **PROMISING / INCONCLUSIVE — not SUCCESS**.

New result this run:
- current consolidated Deposit Insurance Law was re-checked;
- old blanket exclusions for depositor debt and deposits serving as security (former 2.1.2.9/2.1.2.10) are repealed in the current text;
- therefore a security/lien structure alone no longer closes H052;
- the decisive statutory risk is now specifically **Article 26.2 matured-obligation offset at the insurance-event date**;
- current web-accessible sources still do not expose the VTB Avans or Expressbank Əlavə fürsət individual agreement needed to decide whether prepaid interest becomes such an obligation.

## Decisive next evidence
Recover one of:
1. current VTB `Avans` `Ərizə-Razılaşma` / individual deposit agreement;
2. current Expressbank `Əlavə fürsət` individual agreement / standard terms;
3. written VTB/Expressbank/ADIF interpretation explicitly answering whether previously paid advance interest becomes a matured depositor obligation when an insurance event occurs before original contractual maturity.

A favorable explicit clause preserving full compensable principal after the prepaid cash has vested would immediately trigger the final fee/cash-out bound and could promote H052 to terminal SUCCESS. An insurance-event/forced-maturity recoupment clause would reject that candidate.