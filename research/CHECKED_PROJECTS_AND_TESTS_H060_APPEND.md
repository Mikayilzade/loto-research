# H060 append — cross-border payment / funding cash credits

Updated: 2026-08-17
Merge these rows into `research/CHECKED_PROJECTS_AND_TESTS.md` when a safe patch/append route is available.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H060 Paysend Back to School 2026** | new customer, first two $100+ international transfers with `SEPT5` | $5-equivalent bonus per transfer + no Paysend transfer fee; bonus non-cash, FX margin/third-party fees possible; Azerbaijan not evidenced as sending country | **REJECTED strict guarantee**; `research/h060_crossborder_payment_cash_credits.md` |
| **H060 Paysend Global Summer 2026** | $200+ eligible Visa-card transfers | $6.50-equivalent per transfer up to $26; residence list excludes Azerbaijan; non-cash; global $500k pool can exhaust | **REJECTED strict guarantee**; same note |
| **H060 Paysend standard referral bonus** | withdrawable bonus from referred friend transfers | real withdrawable cash mechanism, but published eligible-country list excludes Azerbaijan and qualification depends on independent referral activity | **REJECTED current terminal guarantee** |
| **H060 Wise standard invite** | fee discount + referrer reward after qualifying referrals | basic Wise use broadly available, but reward is referral-dependent and Azerbaijan is not on current balance-holding country list | **REJECTED strict guarantee** |
| **H060 Remitly transfer offers** | new-customer fee waiver / welcome FX rate to Azerbaijan | cost reduction only; no fixed withdrawable cash reward | **REJECTED strict guarantee** |
| **H060 Western Union 2026 referral** | referral reward after invitee transfer | reward explicitly has no monetary value / cannot be redeemed for cash; program modifiable and third-party dependent | **REJECTED strict guarantee** |
| **H060 MoneyGram Invite Friends US** | $25 reward after referred first $50+ international transfer | reward usable as transfer discount, US-only checked program, third-party dependent | **REJECTED strict guarantee** |
| **H060 Skrill Money Transfer promotions** | promo credits / cash-reward controls | public promo-code batch expired 5 Aug 2026; other cash campaigns invitation-only/discretionary | **NO CURRENT PUBLIC GUARANTEE** |
| **H060 general payment-credit theorem** | principal recovery + cash reward - principal - worst-case costs | strict guarantee requires `R_min + B_min - P - C_max > 0`; non-cash/discretionary/zero-branch reward gives `B_min=0` | **VALIDATED necessary-condition gate**; `src/loto_research/payment_credit_gate.py` |
