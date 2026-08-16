# H050 — current principal-protected yield / make-whole screen

Updated: 2026-08-16
Status: **NO SUCCESS; strongest current retail products still fail strict positive-profit floor**

## Goal
Search current retail products that combine a principal redemption floor with a separately positive yield/reward, preferably accessible to Azerbaijan, and test the exact terminal guarantee rather than headline APR.

## 1. Bitget Cash Plus — strongest current retail principal-protection candidate

Official current Bitget support/product pages state:
- deposit USDT or USDC and receive Cash+ at **1:1**;
- redeem back to the originally deposited USDT/USDC at **1:1**;
- no transfer-in / transfer-out fee;
- instant redemption, up to 10M per person per day;
- principal is explicitly described as **protected**;
- yield compounds daily;
- launch APR is approximately 4%, but APR **adjusts dynamically** with market conditions.

Sources:
- https://www.bitget.com/support/articles/12560603889346
- https://www.bitget.com/finance/cash-plus
- https://www.bitget.com/academy/cash-plus-introduction

### Exact floor test
Let principal be P, realized positive/zero yield rate over the holding interval be r, and external funding/withdrawal/network/FX costs be C.

Under the published internal 1:1 redemption mechanics:

`terminal = P + P*r - C`

The product currently supplies a strong principal floor **inside Bitget**, but the retrieved rules do not establish a contractual positive lower bound `r_min > 0`. The FAQ says APR changes dynamically. Therefore a strict theorem `terminal > P` cannot be proved for every allowed state: an allowed future rate arbitrarily close to zero, or external costs, can eliminate the margin.

Additionally, platform/counterparty failure is not bounded by the product page. The marketing description of underlying Treasury-grade assets is not the same as a legally segregated/deposit-insured guarantee to the retail user.

### Result
**PROMISING / NOT SUCCESS.** Cash Plus is materially stronger than ordinary flexible earn because it explicitly provides 1:1 entry/redemption and protected principal, but it lacks a fixed strictly-positive yield floor that is irrevocably locked before capital is committed.

## 2. Bitget USDGO Convert + Simple Earn — compatibility still unproven

Current official pages confirm:
- the retail USDGO Convert slippage bonus has a stated end date **TBD**;
- eligible Convert users holding >=14 days can be made whole for conversion shortfall;
- interest earned during the holding period remains entirely the user's and does not reduce the make-whole bonus;
- the latest retail fixed holding-APR overlap ended **2026-08-01**;
- USDGO Simple Earn Flexible remains advertised with **up to 10% APR**, but its APR is floating and actual returns vary with market conditions.

Sources:
- https://www.bitget.com/support/articles/12560603888534
- https://www.bitget.com/support/articles/12560603867909

No retrieved current rule explicitly proves that USDGO transferred into Simple Earn continues to satisfy the Convert bonus's required holding state. Combining those programs would still be an unsupported assumption. Even if compatibility were proven, `up to` / floating APR does not create a strict positive minimum yield floor.

Status: **NOT SUCCESS; current overlap theorem incomplete**.

## 3. Bitget Shark Fin — apparent guaranteed-yield control, but caveat breaks strict theorem

Bitget's current evergreen Shark Fin help page describes the product as:
- principal-guaranteed;
- guaranteed minimum APR of 6%;
- principal + interest credited at settlement;
- APR range becomes fixed once interest accrual starts.

Source:
- https://www.bitget.com/support/articles/12560603826511

This superficially has the desired shape `P + positive fixed return` after subscription. However the same official FAQ states that in severe market fluctuations there may be slippage that **may lead to a decline in the final return**. Therefore the marketing phrase “guaranteed minimum APR” is not sufficient for a strict all-outcomes theorem unless the product's live subscription contract explicitly defines a non-reducible minimum cash/coin payout after slippage and fees.

Also, the current page does not establish Azerbaijan-specific availability, a currently subscribable series with fixed minimum APR, or a counterparty/default guarantee.

Status: **STRONG CONTROL / NOT TERMINAL SUCCESS**.

## 4. Why H050 does not reach SUCCESS

The current screen produced two stronger mechanism classes than ordinary lottery/betting overlays:
1. **1:1 protected principal + dynamic yield** (Cash Plus);
2. **principal-guaranteed structured product + advertised minimum APR** (Shark Fin).

But strict SUCCESS requires a simultaneously provable lower bound:

`redeemable terminal assets - all unavoidable costs > starting assets`

for every allowed outcome after entry. Current public rules still leave at least one unresolved branch:
- dynamic yield can fall toward zero (Cash Plus);
- stated slippage can reduce final return (Shark Fin);
- external funding/withdrawal/FX/network costs are not bounded by the product agreement;
- platform/counterparty failure is not contractually eliminated by these public help pages.

## New general rule
A product advertised as “principal protected” or “guaranteed APR” is not terminally sufficient. Before SUCCESS, capture the **live subscription contract/order terms after rate lock** and prove:
1. exact minimum redemption amount in the original asset;
2. exact minimum interest/reward amount or rate;
3. no slippage/fee clause can reduce that minimum;
4. entitlement is irrevocable after subscription;
5. geographic/account eligibility;
6. funding and withdrawal route with worst-case costs below the locked reward;
7. counterparty/default assumption explicitly scoped or independently insured/segregated.

## Next priority
H051: search regulated deposit / e-money / broker cash products and current fixed signup/deposit rewards where principal has statutory/contractual protection and the positive reward vests after user-controlled actions. This attacks the remaining counterparty + fixed-positive-floor gap more directly than crypto promotional APR.