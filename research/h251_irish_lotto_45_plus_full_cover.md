# H251 — Irish Lotto 6/45 Lotto Plus full-cover additive closure

Date: 2026-08-24
Scope: LOTTERY ONLY

## Question
Can the September 2026 Irish Lotto refresh create a guaranteed-profit full-cover route by adding Lotto Plus 1 + Lotto Plus 2 to every main-game 6/45 combination?

## Current primary facts
Official Irish National Lottery material states that the enhanced format starts on **Saturday 5 September 2026**, tickets go on sale **Thursday 3 September**, the matrix falls from 47 to 45 numbers, the minimum Lotto purchase remains two lines for €4, and two lines with Lotto Plus remain €6. Therefore the Plus add-on remains **€1 per line** and enters the same chosen Lotto line in both Plus draws.

The official announcement also states Lotto Plus 1 remains a €1,000,000 top prize and Lotto Plus 2 rises from €250,000 to **€1,000,000**. Current official Lotto Plus tables give the lower fixed prizes used here; H251 treats the announced €1m Plus 2 top prize as the only changed Plus 2 amount. If final September rules make any lower tier larger, rerun this packet.

Sources checked 2026-08-24:
- https://www.lottery.ie/news/press-releases/the-national-lottery-announces-first-draw-date-with-new-lotto-game-changes
- https://www.lottery.ie/news/press-releases/national-lottery-unveils-exciting-changes-to-lotto-and-lotto-plus-games
- https://www.lottery.ie/game-information/lotto-plus

## Exact full-space identity
For one 6/45 draw there are `C(45,6) = 8,145,060` possible six-number lines. Owning every line gives deterministic category counts against any six winning numbers plus one bonus ball:

- Match 6: 1
- Match 5 + Bonus: 6
- Match 5: 228
- Match 4 + Bonus: 570
- Match 4: 10,545
- Match 3 + Bonus: 14,060
- Match 3: 168,720
- Match 2 + Bonus: 126,540

Because the Plus add-on costs €1 for each underlying Lotto line and covers **both** Plus draws, the incremental full-cover Plus spend is exactly **€8,145,060**.

## Deterministic Plus payouts
Using the official fixed Plus 1 table and the announced €1m Plus 2 top prize while retaining the currently published lower Plus 2 table:

- Plus 1 deterministic cash + valuing each Match-2+Bonus Daily Million prize at its full €2 face value: **€2,283,240**.
- Plus 2 deterministic cash + the same generous €2 face valuation: **€2,021,240**.
- Combined deterministic gross: **€4,304,480**.
- Incremental Plus cost: **€8,145,060**.
- Net: **-€3,840,580**.
- Deterministic return: **52.847738%**.

The Daily Million prizes are not cash for retail players, so valuing them at full face value is deliberately favorable to the candidate.

## Conclusion
**REJECTED for guaranteed-profit full coverage.** The September 2026 Plus 2 top-prize increase is far too small to rescue the Plus add-on: under the published/announced fixed tables the add-on destroys about 47.15% of its incremental stake deterministically. Therefore any future full-cover analysis of the refreshed Irish Lotto should evaluate the main Lotto separately; adding Plus to every covered combination cannot improve the strict guarantee under these prize tables.

Reopen only if final September rules materially increase lower Plus prizes enough to exceed the exact €8,145,060 additive cost, or if a deterministic subsidy discounts the Plus add-on itself by more than the remaining exact deficit after fees.
