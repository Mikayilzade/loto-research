# H289 — Kentucky Keno stacked-bonus exact-cover candidate

Date checked: 2026-08-26
Status: **conditional positive mathematics; NOT rigorous success**

## Why this packet exists

H225-X* is already rigorously exhausted and must not be extended without changing the mathematical family. H289 therefore tests a genuinely different mechanism: a deterministic promotional subsidy combined with a small exact fixed-pay Keno cover.

Kentucky Lottery's current promotions page lists, for August 1–31, 2026, both a first-ever-deposit 100% match up to $250 and a Refer-A-Friend promotion under which an eligible referred new player who registers and deposits at least $10 receives $20 in Bonuses. Public material does not explicitly establish that those two awards may be stacked on the same account, so stacking is treated as an open gate rather than an assumption in the final conclusion.

Official sources checked:
- Promotions: https://www.kylottery.com/apps/promotions/promotions.html
- Keno rules: https://www.kylottery.com/export/kylmod/galleries/documents/KYLottery_terms/Keno-RULES-3.29.24.pdf
- iLottery Terms: https://www.kylottery.com/apps/funclub/terms.html?pane=terms

## Certificate A — 80-play Spot-1 full cover

Kentucky Keno draws 20 distinct winning numbers from 1 through 80. A Spot-1 base play on one selected number costs $1, and a one-number match pays $2.

Buy exactly one $1 Spot-1 play on each number 1..80 for the same draw:
- plays: 80;
- cost: $80;
- every legal draw contains exactly 20 of those selected numbers;
- therefore exactly 20 plays win;
- fixed gross: 20 x $2 = **$40 in every outcome**.

Conditional promotional funding:
- cash deposit: $30;
- 100% first-deposit match: $30;
- referred-player award: $20;
- total playable funds if both promotions stack: $80.

Thus, conditional on both bonuses being simultaneously awarded and the entire cover being accepted before the draw:

**$30 external cash -> $80 cover -> exactly $40 prize gross -> +$10 versus deposited cash.**

This is a +33.3333% strict cash-profit certificate under those two execution assumptions.

## Certificate B — independent Spot-2 clique cover

A second construction avoids relying on the Spot-1 identity alone. Partition the 80 Keno numbers into six disjoint groups of sizes:

`14, 14, 13, 13, 13, 13`.

Buy every unordered pair within each group as a $1 Spot-2 play. The number of plays is:

`2*C(14,2) + 4*C(13,2) = 494`.

For any set of 20 drawn numbers, the minimum possible number of pairs lying inside these six groups occurs when the draw is distributed as evenly as possible, namely `4,4,3,3,3,3`. Hence the number of winning Spot-2 pairs is at least:

`2*C(4,2) + 4*C(3,2) = 24`.

The official Spot-2 base payout for matching both selected numbers is $11, so guaranteed gross is at least:

`24 x $11 = $264`.

Conditional funding:
- deposit $237;
- 100% match $237;
- referral bonus $20;
- playable funds $494.

Conditional strict floor: **$264 - $237 = +$27** versus deposited cash. This construction is mathematically valid but requires 494 accepted plays and is therefore execution-heavier than Certificate A.

## Why H289 is not SUCCESS

Two independent gates remain.

### 1. Promotion-stack gate

The current promotions page lists both August offers, but the public first-deposit rules state that a deposit promotion cannot be combined with other deposit promotional offers. The Refer-A-Friend award is not clearly classified in the checked public material for purposes of that clause. Therefore the required `$30 match + $20 referral` stack is not yet an authoritative entitlement.

### 2. Complete-acquisition gate

Kentucky iLottery Terms reserve the right to refuse an attempted purchase for any reason and separately allow the Lottery to limit purchases or wagers on a particular set of numbers at any time and without notice. A strict cover proof requires every required number selection to be accepted for the same draw. Because that acquisition is not guaranteed by the governing terms, the mathematical cover cannot currently be promoted to rigorous executable profit.

This blocker applies even though Spot-1 needs only 80 plays and the arithmetic itself is exact.

## Conclusion

H289 is a **high-value conditional candidate, not a success**. It demonstrates that a real currently advertised promotional stack would cross the guaranteed-profit threshold for an extremely simple exact Keno cover if both awards stack and the full cover is accepted. The next H289 action is narrow: obtain authoritative stacking compatibility plus an execution mechanism that removes/refutes the refusal/number-limit gate. If either fails, close H289 as execution-blocked and continue to a new mechanism rather than weakening the success standard.
