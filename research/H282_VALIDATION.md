# H282 VALIDATION — Kentucky CASH POP + August 2026 bonuses

Validated: 2026-08-26
Result: **CLOSED / NO STRICT GUARANTEED-PROFIT FLOOR**

## Independent rule checks

1. Kentucky Lottery currently advertises a **100% first-deposit match up to $250** for August 1-31, 2026.
2. Kentucky CASH POP uses exactly **15 possible winning numbers** and explicitly supports `Cover All`.
3. Permitted per-number wagers are **$1, $2, $5, $10**.
4. The minimum published prize amounts attached to those wagers are **$5, $10, $25, $50** respectively; therefore the minimum legal prize is exactly **5x stake** for every allowed stake size.
5. KLC iLottery Terms separately track deposits, Bonuses and prize winnings. Deposits and Bonuses are nonwithdrawable; eligible prize winnings may be withdrawn.

## Algebraic validation

For one draw, write `s_i >= 0` for total stake on CASH POP number `i`, `i=1..15`, and let `C=sum(s_i)`.

- If any `s_i=0`, outcome `i` gives gross 0, so no positive guarantee exists.
- Otherwise consider the legal branch where every prize assignment is the published minimum. Outcome `i` then pays `5*s_i`.
- Since `min_i s_i <= C/15`, the legal worst-case gross satisfies `G_min <= 5*C/15 = C/3`.

This is tight for equal stake across all 15 numbers. It applies to arbitrary ticket grouping and stake mixtures. Summing the same argument over draws proves the identical `1/3` ceiling for multi-draw portfolios.

## Subsidy validation

100% first-deposit match:
- playable spend per cash dollar <= 2;
- withdrawable CASH POP prize floor <= `2/3` cash dollar;
- therefore strict cash profit is impossible.

Favorable current-offer stress tests:
- grant a $150 first deposit both the $150 first-deposit match and the current $50 Tiki Tuesday Bonus: playable $350, strict prize-floor ceiling $116.6667 < $150 cash;
- grant both 100% first-deposit match and 25% Summer Friday match: strict cash-recovery ceiling = `2.25/3 = 75%`.

Both remain below break-even even before execution frictions.

## Validation gates

- [x] H225-X* terminal status read first; no X21/X22 created.
- [x] No existing H282 packet found before creation.
- [x] Exact state count = 15 possible winning numbers.
- [x] All four allowed wager/minimum-prize ratios independently reduce to 5.
- [x] Portfolio proof covers arbitrary nonnegative stake mixtures, not only one sample Cover All ticket.
- [x] Multi-draw extension checked additively.
- [x] 100% subsidy arithmetic checked exactly as `2/3 < 1`.
- [x] Stronger favorable Tiki / Summer Friday stacking scenarios remain below 100% cash recovery.
- [x] No SUCCESS claim made.

Reopen only after a material rules/promotion change that can push guaranteed playable value above the exact **3x cash** hurdle (equivalently deterministic bonus >200% of deposited cash) for funds usable on CASH POP, or after a payout-table change that raises the universal minimum-prize ratio.
