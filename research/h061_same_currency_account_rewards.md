# H061 — same-currency account-opening / funding cash rewards

Updated: 2026-08-17
Status: **mechanism real; current Azerbaijan-executable public screen closed; no terminal guarantee**

## Goal
Search for a stronger class than cross-border transfer promotions: open/fund an account in the same currency, preserve principal in the user's own regulated account, and receive a fixed withdrawable cash reward from deterministic self-controlled actions.

Strict terminal form:

`guaranteed_net_floor = principal_recovery_min + vested_cash_reward_min - committed_principal - worst_case_fees`

SUCCESS requires the floor to be strictly positive before commitment, with no uncontrolled third party, lottery/ranking/quota uncertainty, discretionary eligibility, spend/consumption requirement, market exposure, FX exposure, or clawback branch that can reduce the reward to zero.

## Current Azerbaijan public screen
### Birbank
Current active campaign index (Aug 2026) is dominated by merchant discounts/installment offers, not fixed account-opening cash. The recent new-installment-card promotion offered 50 bonus after a first 500-AZN installment purchase, but it ended 31 Jul 2026 and the reward is tied to consumption; returns can claw the bonus back. This fails both currentness and principal-preservation.

Sources:
- https://birbank.az/campaigns
- https://birbank.az/campaigns/ilk-taksit-50-bonus

### ABB
The 2026 Open Banking campaign paid 5 AZN cashback only to the first 2,000 pre-selected customers after 20 AZN QR or 50 AZN POS retail turnover; it ended 9 May 2026. The first-N quota, pre-selection, spend requirement and expiry independently fail the gate.

The Tam Visa bus campaign offered 100% cashback for up to ten rides but ended 30 Jun 2026 and is reimbursement of consumed transport spend, not preserved principal.

Sources:
- https://abb-bank.az/en/aciq-bankciliq-kesbek-kampaniyasini-elan-edirik
- https://abb-bank.az/en/kampaniyalar/tamvisa-avtobus-kampaniyasi-basladi

### Yelo Bank
A July 2026 installment-card offer gave new customers a one-month Welcome cashback category, but it expired 31 Jul 2026 and requires merchant spending. It is not a fixed principal-preserving cash reward.

Source:
- https://www.yelo.az/en/news/commission-free-cash-withdrawal-campaign-on-yelo-installment-cards/

### Leobank
Leobank cashback is explicitly paid in real money and immediately, which validates the cash-settlement mechanism locally. But the reward is purchase-linked cashback, so qualifying spend consumes principal; there is no guaranteed positive cash floor from merely opening/funding the account.

Source:
- https://leobank.az/az/cashback

## Global controls
### Mox Bank — strong mechanism, wrong geography / quota
Current 2026 Hong Kong promotions show the desired mechanism class can exist: new customers can receive fixed cash rewards for opening/funding accounts or applying for products. One promotion advertises HKD200 instant cash rebate with no minimum spend for the first 3,000 new customers; another offered HKD2,500 after maintaining HKD250,000 in a time deposit. These validate the mechanism but are Hong-Kong-specific and quota/product dependent, not Azerbaijan-executable.

Source:
- https://mox.com/promotions/

### Payoneer — Azerbaijan was eligible historically, but current public reward not found
Payoneer previously ran a USD300 cashback campaign explicitly listing Azerbaijan among eligible territories after USD25,000 of eligible outgoing payments. However registrations closed 25 Aug 2025, self-funding was excluded, and Payoneer reserved change/termination discretion. This is valuable historical evidence that Azerbaijan-compatible cash reward programs can appear, but it is not current and not self-funding.

Source:
- https://pages.payoneer.com/unlock-global-growth/

Current 2026 Payoneer $130 cashback campaigns found in India/Philippines require USD5,000 of genuine client Request-a-Payment volume and exclude self-payment; they are geography-limited and third-party business-volume dependent.

Sources:
- https://pages.payoneer.com/en-in/get-paid-india/
- https://pages.payoneer.com/get-paid-philippines/

### Skrill / Neteller controls
Current/recent 2026 Skrill/Neteller cash-credit promotions show real account credits exist, but public examples are invitation-only, geography-specific, spend/merchant dependent, or expired. These fail deterministic pre-commitment eligibility or principal preservation.

Sources:
- https://www.skrill.com/en-us/lockable-balance-terms-inc-5/
- https://www.skrill.com/en/skrill-mission-deposit-bonus-terms/
- https://www.neteller.com/pl/merchant-withdrawers-tcs/

## H061 gate
A candidate is terminally admissible only if all are true before funding:
1. Azerbaijan resident/entity eligibility is explicit or independently established.
2. Reward amount is fixed, cash-withdrawable, and not `up to`, lottery, ranking, first-N, invite-only, or discretionary.
3. Qualification uses only actions fully controlled by the user.
4. No independent client/referral/employer/merchant outcome is required.
5. Principal remains legally redeemable in the same currency and is not consumed.
6. No market-price exposure is needed.
7. Fees and withdrawal costs have a hard upper bound below the reward.
8. Reward survives allowed closure, cancellation, reversal and compliance branches once the qualifying action is completed.
9. Terms cannot make the reward zero through ordinary anti-abuse discretion applied to the intended strategy.

## Conclusion
The mechanism class is real and stronger than ordinary cashback: fixed cash can coexist with preserved account principal. But the current public screen found **no Azerbaijan-executable, non-discretionary, self-controlled same-currency account-opening/funding reward with a strictly positive guaranteed cash floor**.

H061 status: **CURRENT PUBLIC SCREEN CLOSED; NO SUCCESS**.

## Next research priority
H062: search regulated **business-account onboarding / payroll / merchant-acquiring activation grants** where the underlying business receipt is independently owed and the bank/provider pays a fixed cash onboarding incentive. This may escape the consumer-spend problem while keeping principal preserved. Prioritize Azerbaijan/local banks and globally available business platforms; reject first-N, referral, lottery and discretionary schemes immediately.
