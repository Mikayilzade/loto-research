# H245 — Irish Lotto full-cover dilution correction

Date: 2026-08-24
Status: NOT A SUCCESS

## Purpose

Correct the prior optimistic full-cover threshold and test how many external jackpot-winning lines a complete-coverage strategy can tolerate at the current Irish Lotto 6/47 jackpot cap.

## Official inputs

Current Irish Lotto 6/47 has C(47,6) = 10,737,573 possible lines and costs EUR 2 per line. The current official prize table lists Match 5 + Bonus EUR100,000; Match 5 EUR1,500; Match 4 + Bonus EUR150; Match 4 EUR50; Match 3 + Bonus EUR25; Match 3 EUR9; Match 2 + Bonus as a EUR3 Daily Million Quick Pick with Plus (2 lines). The current jackpot cap is EUR18.96m. The rules permit at most five successive cap draws; if the jackpot is still not won in the fifth cap draw, the jackpot pool rolls down to the next winning tier.

Sources:
- https://www.lottery.ie/game-information/lotto
- https://cdn2.lottery.ie/uploads/Issue_9_RULES_LOTTO_6_OF_47_OCT_2024_29_10_d1d5da4a58.pdf

## Exact complete-coverage counts for a fixed draw

- Match 6: 1
- Match 5 + Bonus: 6
- Match 5: 240
- Match 4 + Bonus: 600
- Match 4: 11,700
- Match 3 + Bonus: 15,600
- Match 3: 197,600
- Match 2 + Bonus: 148,200

Complete-coverage stake = 10,737,573 * EUR2 = EUR21,475,146.

Valuing the Match 2 + Bonus free-play award at its stated EUR3 face value, the non-jackpot prize value is:

6*100,000 + 240*1,500 + 600*150 + 11,700*50 + 15,600*25 + 197,600*9 + 148,200*3 = EUR4,248,000.

Therefore the jackpot share required merely to reach face-value break-even is:

EUR21,475,146 - EUR4,248,000 = EUR17,227,146.

This corrects the earlier ~EUR12.07m threshold, which was too low.

## Dilution at the EUR18.96m cap

If our full cover contains the guaranteed jackpot line and there are `m` external jackpot-winning lines, our jackpot share is approximately EUR18.96m/(m+1), before any rule-specific rounding or prize-pool details.

- m = 0: total face-value return ~ EUR23,208,000; margin ~ +EUR1,732,854.
- m = 1: total face-value return ~ EUR13,728,000; margin ~ -EUR7,747,146.
- m >= 1: strictly worse.

Thus the complete-coverage cap strategy tolerates **zero external jackpot-winning lines**.

## Important structural consequence

Complete coverage itself guarantees that the jackpot is won. Therefore a complete-cover player cannot simultaneously rely on the fifth-cap-draw 'no jackpot winner' roll-down mechanism: buying every combination creates a jackpot winner and prevents that no-winner branch from occurring.

The remaining positive-looking case is therefore not a deterministic roll-down arbitrage. It is a thin sole-winner jackpot-overhang case whose profitability disappears as soon as any outside player also holds the winning six numbers. Because outside jackpot duplication cannot be bounded to zero from public information, this is not a guaranteed-profit mechanism.

## Operational caveats

The EUR3 Match 2 + Bonus award is non-cash free-play value, so economic value may be below face value and execution friction would reduce the margin further. Retailer/online purchase limits, timing, ticket-printing throughput, account limits, and practical inability to buy 10.7m distinct lines are additional rejection factors even before financing cost.

## Verdict

NOT A SUCCESS. At the current cap, theoretical complete coverage is positive only in the sole-jackpot-winner face-value case. One external jackpot-winning line makes it decisively negative, and full coverage cannot exploit the fifth-cap no-winner roll-down because it guarantees its own jackpot hit.

## Next hypothesis

H246: search for roll-down/overlay products where the extra pool is distributed into lower tiers that can be covered with substantially less than full jackpot-space coverage, so profitability does not require being the unique top-prize winner.
