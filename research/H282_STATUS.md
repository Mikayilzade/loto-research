# H282 STATUS — Kentucky CASH POP + August 2026 deposit bonuses

Updated: 2026-08-26
Branch: `research-work`
State: **CLOSED / NO STRICT GUARANTEED-PROFIT FLOOR**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* was read first and remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## New checkpoint

Kentucky CASH POP was tested as a smaller, native-cover alternative to H279 Pick 3. The official game supports `Cover All` over exactly 15 possible winning numbers, so the large 100-number Pair cart is not needed.

However, the payout structure gives a stronger impossibility result. For every allowed per-number stake ($1/$2/$5/$10), the minimum legal assigned prize is exactly 5x stake ($5/$10/$25/$50). For any portfolio with total stake `C`, strict coverage requires all 15 numbers. In the legal minimum-prize assignment branch the worst drawn number pays at most

`5 * C / 15 = C / 3`.

Therefore **every nonnegative CASH POP portfolio has strict worst-case gross <= 33.3333% of playable spend**. The proof is portfolio-wide and extends additively to multi-draw play.

The current Kentucky first-deposit offer matches 100% up to $250, so at most $2 playable balance is created per $1 cash deposited. CASH POP can therefore return at most `2/3 = 66.6667%` of the deposited cash in the strict worst case.

Even deliberately favorable current-offer stacking fails:
- $150 first deposit + $150 first-deposit match + $50 Tiki Tuesday bonus -> $350 playable -> CASH POP floor ceiling $116.67, only 77.7778% of cash deposit;
- 100% first-deposit match + 25% Summer Friday match -> CASH POP cash-recovery ceiling 75%.

So CASH POP closes on arithmetic before execution/checkout issues matter.

## Saved evidence

- `research/h282_kentucky_cashpop_bonus_bound.md`
- `research/H282_VALIDATION.md`
- `src/loto_research/h282_kentucky_cashpop_bonus_bound.py`
- `data/derived/h282_kentucky_cashpop_bonus_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H282_APPEND.md`

## NEXT ACTION

Do not reopen Kentucky CASH POP under the checked August 2026 offers unless deterministic playable subsidy exceeds the exact **200% bonus hurdle** (3x playable balance per cash dollar) or the minimum-prize schedule materially improves. Continue searching for deterministic withdrawable Bonus Cash/cashback, fixed-value rewards, or finite/reservable subsidized assets whose guaranteed external value crosses an exact cover deficit without relying on a large fragile cart.
