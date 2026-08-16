# Audit-ledger continuation — H047

Updated: 2026-08-16
Parent ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`

The parent ledger is large and current connector reads are truncated. This shard preserves the H047 audit row without risking destructive replacement of the parent history.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H047 vested cash entitlement** | withdrawable exchange commission rebate (BETDAQ DAQBACK) | real withdrawable cashback exists, but is earned from settled commission; whole-market void yields no qualifying commission/rebate | **REJECTED as H046 strict-guarantee repair**; `research/h047_vested_cash_entitlement_screen.md` |
| **H047 loss cashback** | BETDAQ real-money 10% net-loss cashback | void/cancelled bets do not qualify; refund is partial and post-settlement | **REJECTED strict guarantee**; same note |
| **H047 Azerbaijan risk-free offer** | Betfair first Exchange bet refund if loss | Azerbaijan listed eligible, but unmatched/unsettled/voided bets do not qualify | **REJECTED strict guarantee**; same note |
| **H047 zero-stake positive cash floor** | Smarkets SailGP predictor paid £50 if correct / £25 if wrong | historical mechanism proves event-independent positive cash floor can exist, but offer expired and was UK/IE only with operator-discretion terms | **MECHANISM VALIDATED; not executable now**; same note |
| **H047 current free-prediction screen** | Betfair free prediction + cTrader Store campaign | Betfair prizes remain random/competitive; cTrader rewards are non-cash/discretionary | **REJECTED current universal cash floor**; same note |

Next registered branch: **H048 non-wagering contractual bounty/referral/action payments** where all qualifying acts are under the user's control and cash becomes owed before any random/event-dependent branch.
