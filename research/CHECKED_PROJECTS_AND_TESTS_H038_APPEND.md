# Audit append — H038

Updated: 2026-08-16

This packet is part of the permanent checked-project audit trail and should be merged into `research/CHECKED_PROJECTS_AND_TESTS.md` on the next full-ledger maintenance pass.

| Class / example | Result | Status / evidence |
|---|---|---|
| **H038 deterministic withdrawable rebate theorem** | strict guarantee requires `minimum cash payout + guaranteed withdrawable cash rebate > qualifying spend + costs` | **VALIDATED necessary-condition filter**; `research/h038_deterministic_rebate_guarantee.md`; `src/loto_research/rebate_guarantee.py` |
| **H038 nonwithdrawable lottery-credit theorem** | if credit must be wagered on a product with a legal zero-cash outcome, advertised face value has strict cash floor 0 | **VALIDATED guarantee filter** |
| OLG LOTTO MAX buy-1-get-1 (current selected-account offer) | spend CAD 6 → CAD 6 lottery-specific bonus; original and bonus tickets can both return zero | **REJECTED strict guarantee; EV subsidy only** |
| OLG LOTTO 6/49 buy-1-get-1 (current selected-account offer) | spend CAD 3 → CAD 3 lottery-specific bonus; zero-cash joint outcome remains | **REJECTED strict guarantee; EV subsidy only** |
| **OLG CAD 10 Birthday Lottery Bonus** | zero qualifying cash spend; lottery-only credit | **VALIDATED zero-cost free-roll / positive-EV overlay; NOT strict positive-profit guarantee** |
| Birthday bonus → POKER LOTTO | CAD 10 buys 5 Quick Pick hands; all five can legally lose | **REJECTED guarantee conversion** |
| Birthday bonus → LIGHTNING LOTTO | CAD 10 buys 5 plays / 15 selections; far below complete 5/49 outcome coverage | **REJECTED guarantee conversion** |
| Birthday bonus → MEGADICE | Quick Pick with losing outcomes | **REJECTED guarantee conversion** |
| California SuperLotto Plus 2026 2nd Chance bonus draw | random cash winners, no deterministic individual cash floor | **REJECTED standalone guarantee class** |

Next branch: zero-cost-credit conversion scan across compact lottery products, then true withdrawable cashback/rebate scan.
