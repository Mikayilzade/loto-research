# H051 — regulated deposit / e-money / broker fixed-reward screen

Updated: 2026-08-16
Status: **NO SUCCESS; statutory principal protection is real, but current positive-return products still lack an all-outcome strictly-positive floor**

## Goal
Search current Azerbaijan-accessible regulated products where principal is statutorily or contractually protected and a positive reward is fixed/vested by deterministic user-controlled actions.

This branch deliberately separates ordinary positive expected/nominal return from the project's terminal condition: **strictly positive net profit in every allowed outcome after execution and costs**.

## 1. Azerbaijan Deposit Insurance Fund — statutory principal protection is real
Current official ADIF material states:
- protected-deposit annual-rate ceiling: **12% in AZN**, **2.5% in foreign currency**;
- compensation for an individual's insured deposit is **100% up to 100,000 AZN per participating bank**;
- compensation includes interest accrued by the date of the insurance event, subject to the compensation cap;
- deposits above the published protected-rate ceiling are not protected.

Primary sources:
- https://adif.gov.az/az/insured-deposit
- https://adif.gov.az/
- https://adif.gov.az/az/news/milli-valyutada-qorunan-amanatlar-uzra-illik-faiz-daracasinin-yuxari

The January 28, 2026 ADIF decision kept the protected AZN ceiling at 12% after the fund's methodology observed a ~10% average long-term retail deposit rate in the second half of 2025.

## 2. Current bank controls
### Kapital Bank digital deposit
Current official help material advertises AZN digital-deposit rates up to **12%** and USD up to **2.5%**, with the statutory compensation framework referenced on the same product/help surface.

Source:
- https://www.kapitalbank.az/how-to/depozit/reqemsal-depozit/reqemsal-depozitin-faizleri-nece-odilir

### Bank Respublika term deposit
Current official product material shows fixed maturity-rate menus including:
- 6–11 months: 6.5% paid at maturity;
- 12–17 months: 9.5%;
- 18–23 months: 10%;
- 24–36 months: 10.5%.

The same page states early withdrawal returns principal but may reduce/erase interest depending on actual holding duration.

Source:
- https://bankrespublika.az/pages/muddetli-depozit

### XalqKart balance yield
A current July–December 2026 Xalq Bank campaign advertises:
- free card issuance / no initial deposit;
- **7% annual return on AZN balances** from 300 to 20,000 AZN through 2026-12-31;
- free domestic transfers up to the stated monthly threshold and free cash withdrawal up to the stated threshold.

Source:
- https://www.xalqbank.az/en/personal/campaigns/xalqkart-i-indi-pulsuz-elde-edin-en

These are useful low-risk nominal-income controls, but they do not satisfy the terminal guarantee theorem below.

## 3. Strict guarantee theorem for insured interest products
Let:
- `P` = starting principal;
- `I(t)` = interest accrued by time `t`;
- `C` = all unavoidable costs;
- `T` = planned maturity;
- `tau` = possible insurance-event / bank-failure time after opening.

If the statutory insurer guarantees principal plus only **interest accrued by the insurance-event date**, then worst-case protected terminal value is:

`floor = P + I(tau) - C`.

For a product whose interest accrues from zero after opening, allowed `tau -> 0+` implies:

`inf I(tau) = 0`.

Therefore:

`inf floor <= P - C`.

So **deposit insurance + ordinary accrued interest cannot by itself prove strictly positive profit in every allowed outcome**, even though it can make principal loss very small/legally protected under defined conditions.

This is a new general control: a fixed annual deposit rate is not the same thing as an all-outcome strictly-positive terminal floor when the protection mechanism only preserves accrued interest.

## 4. Search for separate deterministic fixed rewards
Current Azerbaijan-facing screening also checked the stronger shape:

`protected principal + upfront/vested cash reward`.

Findings:
- current bank campaigns surfaced card cashback, purchase bonuses, gamification, and chance-based bonuses rather than a current unconditional withdrawable cash reward attached to protected principal;
- Birbank's recent 50-bonus first-installment campaign ended 2026-07-31 and also required a >=500 AZN installment purchase; returned purchases trigger bonus clawback;
- current m10 offers pay bonuses on utility/merchant/QR spending, not an unconditional signup cash reward;
- AMarkets advertises referral/deposit bonuses, but it is an offshore trading product rather than statutory deposit protection and requires trading volume;
- local broker fee-waiver promotions reduce costs but do not create a positive terminal floor.

Representative sources:
- https://birbank.az/campaigns/ilk-taksit-50-bonus
- https://m10.az/en
- https://m10.az/en/qr-pay
- https://az.amarkets.com/promo/for-clients/refer-a-friend/
- https://uforex.az/en/xeberler/uforex-launches-a-special-offer-one-month-of-commission-free-and-swap-free-trading/

## 5. Result
### Validated
- Azerbaijan has a real statutory deposit-protection framework with clear current rate ceilings and compensation cap.
- Current retail deposits/balance products offer fixed or advertised positive nominal yields inside that framework.
- These products are materially stronger principal-floor candidates than unprotected lottery/betting/crypto risk.

### Rejected as terminal SUCCESS
**Ordinary insured deposit interest alone.** The insurance-event branch can occur before meaningful interest accrues, leaving principal-only recovery rather than strict profit.

### Not found in this packet
A current Azerbaijan-accessible product combining all of:
1. statutory/contractual principal floor;
2. deterministic separately vested cash reward or prepaid interest;
3. reward survives immediate issuer failure/closure after vesting;
4. no purchase/trading/random-outcome requirement;
5. no clawback/abuse discretion that can erase the reward;
6. funding/withdrawal/tax costs bounded below the reward.

## 6. New next branch
H052 should search specifically for **prepaid-interest / interest-in-advance deposits, deposit-opening cash gifts, government-backed savings certificates with upfront discount/redemption floor, and regulated account-switch/signup cash bonuses** accessible from Azerbaijan.

The key improvement over H051 is timing: the reward must vest at or before commitment, or otherwise be independently protected from the issuer-failure branch.