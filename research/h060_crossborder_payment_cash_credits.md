# H060 — regulated cross-border payment / funding cash-credit screen

Updated: 2026-08-17
Status: **MECHANISM REAL; CURRENT PUBLIC SCREEN CLOSED; NO TERMINAL GUARANTEE**

## Goal
Find a current regulated payment-provider promotion where a self-controlled transfer/funding action mechanically vests a fixed, withdrawable cash reward while transfer principal remains recoverable, so the all-branch net cash floor is strictly positive.

Strict gate:

`guaranteed_net_floor = guaranteed_principal_recovery + guaranteed_withdrawable_cash_reward - committed_principal - worst_case_fees_FX_external_costs`

SUCCESS requires this quantity to be strictly positive under every contractually allowed branch, with entitlement already fixed before material risk is taken.

## 1. Paysend — current Back to School promotion (14 Aug–30 Sep 2026)
Official current promotion terms provide the strongest live public payment-rail lead found in this packet:
- new customers in supported **sending** countries outside UK/EEA/Canada can use code `SEPT5`;
- each of the first two eligible international transfers of at least USD 100 receives no Paysend transfer fee plus a USD 5-equivalent bonus;
- reward is credited to the Paysend Bonus Account within 24h after successful transfer;
- transfer uses a Paysend FX rate that may include a margin and third-party fees may apply;
- same-currency transfers are excluded;
- the promotion explicitly says the reward is non-transferable and **cannot be exchanged for cash**;
- failed/reversed/refunded/cancelled transfers do not qualify and Paysend retains anti-abuse/disqualification rights.

Primary terms:
- https://cloud.paysend.com/web/docs/Paysend_Back_to_School_Global_promo.pdf

Azerbaijan execution gate:
- Paysend's current supported-country page states Azerbaijan can **receive** USD/AZN to cards, but unlike the 49 sending countries it does not state that funds can be sent *from* Azerbaijan;
- therefore Azerbaijan is not evidenced as an eligible sending residence for this promotion.

Even ignoring geography, the bonus is not withdrawable cash and the cross-currency transfer has non-zero/variable FX and possible third-party costs. It cannot establish a strictly positive cash floor.

Result: **REJECTED as terminal guarantee; useful non-cash transfer subsidy only.**

## 2. Paysend — Global Summer promotion (through 31 Aug 2026)
Current terms advertise USD 6.50 equivalent per qualifying USD 200 international transfer, up to USD 26, but:
- residence is restricted to UK, Canada, Australia, EEA, Andorra, Macedonia, Montenegro, San Marino or Switzerland;
- Azerbaijan is outside the residence list;
- promotional bonus cannot be exchanged for cash;
- global USD 500,000 prize-pool exhaustion can reduce or eliminate later bonuses;
- FX margin/external cost and cancellation/anti-abuse branches remain.

Primary terms:
- https://cloud.paysend.com/web/docs/Paysend_Global_Summer_Promotion_Terms%26Conditions.pdf

Result: **REJECTED strict guarantee.**

## 3. Paysend standard referral bonus
Paysend currently has a genuine withdrawable referral bonus: up to USD 3-equivalent for each of a referred friend's first 12 transfers, and published material says bonus can be withdrawn to a bank card once the balance threshold is met.

However:
- the published eligible-country list for the standard Bonus program does not include Azerbaijan;
- qualification depends on an independent referred person's successful transfers, not a self-controlled principal-preserving action.

Primary sources:
- https://help.paysend.com/hc/en-us/articles/6330378397341-What-is-Paysend-Bonus
- https://paysend.com/bonus

Result: **REAL withdrawable-cash mechanism; REJECTED for current terminal guarantee due geography + third-party dependency.**

## 4. Wise invite / transfer discount
Wise's current standard invite program gives the invited user a transfer-fee discount/free transfer and rewards the referrer only after qualifying referrals transact. Exact reward depends on region. Same-currency transfers do not qualify.

Azerbaijan is not on Wise's unsupported-location list, so basic registration/sending may be possible; however Azerbaijan is absent from the current list of countries where residents can hold a Wise balance. More importantly, the reward requires independent referral behavior rather than a self-controlled transfer.

Primary sources:
- https://wise.com/help/articles/77zvWSO4tKdGobXrgHIJAA/how-does-the-standard-invite-program-work
- https://wise.com/help/articles/2813542/where-do-i-need-to-live-to-hold-money-with-wise

Result: **REJECTED terminal guarantee; referral/discount mechanism only.**

## 5. Remitly
Current Azerbaijan corridor pages show new-customer fee waivers / welcome FX offers and no receiver fee for receiving in Azerbaijan. These reduce transfer cost but do not create a fixed withdrawable positive cash reward. Sender geography is corridor-specific and Azerbaijan is documented here primarily as a receiving country.

Primary source:
- https://www.remitly.com/az/en/receive-money

Result: **REJECTED — cost reduction, not positive cash floor.**

## 6. Western Union / MoneyGram
Western Union's 2026 referral terms explicitly say referral rewards have no monetary value and cannot be redeemed for cash; the reward also depends on an independent invitee and the program can be modified/terminated.

MoneyGram's current US Invite Friends program gives the referrer a USD 25 reward usable as a discount on a future USD 50+ transfer; it is US-only for the checked corridor list and remains third-party dependent / transfer-credit rather than independent cash.

Primary sources:
- https://www.westernunion.com/us/en/legal/refer-a-friend-terms-and-conditions.html
- https://www.moneygram.com/us/en/help-center/faq/services/invite-friends-referral-program

Result: **REJECTED terminal guarantee.**

## 7. Skrill control
Skrill's current Money Transfer promotion terms show that this mechanism class exists as promo credits/top-ups, but the public promo-code batch found was valid only through 5 Aug 2026, while other cash-reward campaigns are invitation-only. Allocation/calculation of promo credits is stated to be at Skrill's discretion.

Primary source:
- https://www.skrill.com/en/footer/terms-conditions/smt/promo-terms/

Result: **no current public self-controlled guaranteed-cash route.**

## Necessary-condition theorem for this class
A transfer-credit campaign cannot be a strict guaranteed-profit strategy merely because `bonus > 0`.

For a cross-currency transfer of principal `P`, define:
- `R_min`: guaranteed cash amount recoverable from the transferred principal after all legal execution/settlement/return branches;
- `B_min`: guaranteed **withdrawable cash** promotional reward that survives all legal branches;
- `C_max`: worst-case mandatory fees, FX loss, third-party fees, taxes and withdrawal costs bounded by contract before commitment.

Then a strict guarantee requires:

`R_min + B_min - P - C_max > 0`.

If the reward is non-cash, discretionary, first-N/capped, referral-dependent, or can be zero after a valid cancellation/compliance branch, then `B_min = 0` for the terminal proof. If FX/external costs are not hard-bounded before commitment, a small nominal bonus cannot establish a positive all-branch floor.

## Current conclusion
H060 found multiple real payment-rail subsidy mechanisms and one live current public fixed-bonus campaign, but **none passes all terminal gates**:
1. Azerbaijan/current lawful sender eligibility;
2. self-controlled qualifying action;
3. principal recoverability;
4. fixed withdrawable cash reward;
5. deterministic vesting before material risk;
6. no pool-exhaustion/invite/discretion zero branch;
7. hard-bounded fees/FX/external costs;
8. strictly positive net floor after all costs.

H060 status: **CURRENT PUBLIC SCREEN CLOSED; NO SUCCESS.**

## Next high-value branch
H061 should search **same-currency / no-FX transaction credits and bank/e-wallet account-opening or funding rewards** where principal can remain in the user's own regulated account and a fixed cash reward vests after a deterministic self-controlled action. This removes the main H060 FX-loss channel and is the strongest remaining adjacent class.