# H278 STATUS — Georgia Lottery deterministic 50% deposit subsidy

Updated: 2026-08-26
Branch: `research-work`
State: **CLOSED / REJECTED for checked routes**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## New checkpoint

H278 tested a genuinely deterministic external subsidy rather than another random raffle: Georgia Lottery Promotion 27012 gives eligible never-deposited iHOPE accounts a 50% first-deposit bonus, capped at $125. A fully matched $250 deposit therefore yields $375 of restricted lottery purchasing power, making **2/3 = 66.6666667%** the exact wager-return hurdle for strict cash profit under a favourable model where resulting prizes are fully cash-usable.

Exact results:
- Georgia FIVE: exact 100,000-play cover gross **$53,650 = 53.6500%**; matched-deposit equivalent **80.4750%**. Symmetry extends the average bound to every nonnegative additive portfolio.
- CASH POP: all 15 numbers guarantee a win, but the legal minimum assigned prize is only 5x a per-number wager against 15x cover cost; worst-case **33.3333%**, or **50.0000%** of deposited cash after the bonus.
- Base KENO: all exact full-combination covers for Spot sizes 1–10 were evaluated. Best is **7 Spot = 65.0263524%**, reaching only **97.5395286%** of deposited cash after the 50% bonus.
- KENO+BULLS-EYE: all Spot sizes 1–10 evaluated with exact BULLS-EYE containment counts. Best is **4 Spot = 64.3343998%**, or **96.5015997%** of deposited cash after bonus.
- KENO MULTIPLIER cannot improve a strict guarantee because it doubles cost and has a legal `None` multiplier branch.

Thus the current deterministic 50% subsidy is a real near-miss but does not create strict guaranteed profit for these compact exact-cover constructions.

Files:
- `src/loto_research/h278_georgia_deposit_bonus_cover_bound.py`
- `data/derived/h278_georgia_deposit_bonus_cover_bound.json`
- `research/h278_georgia_deposit_bonus_cover_bound.md`
- `research/H278_VALIDATION.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H278_APPEND.md`

## NEXT ACTION

Continue outside H225. Two high-value directions remain:
1. screen another deterministic promotion/subsidy materially above 50%, or one stackable with a game whose rigorous worst-case return exceeds its subsidy hurdle;
2. continue the Georgia-promotion lane only with a different game family and a strict worst-case proof — do not repeat Georgia FIVE, CASH POP, or base/BULLS-EYE KENO exact covers.

Do not claim the entire Georgia Lottery catalogue exhausted from H278 alone.
