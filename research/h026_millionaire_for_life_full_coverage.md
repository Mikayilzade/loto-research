# H026 — Millionaire for Life full-space coverage

Updated: 2026-08-15
Status: **REJECTED as guaranteed-profit full coverage**

## Target
Current US multi-state **Millionaire for Life** game.

Primary current sources:
- Powerball/MUSL game page: https://www.powerball.com/millionaire-for-life
- Powerball/MUSL prize chart: https://www.powerball.com/millionaire-for-life-prize-chart
- Georgia Lottery current game page: https://www.galottery.com/en-us/games/draw-games/millionaire-for-life.html

Current mechanics verified from operator sources:
- choose 5 white numbers from 1–58;
- choose 1 Millionaire Ball from 1–5;
- $5 per play;
- top prize: $1,000,000/year for life, current cash option $18,000,000;
- second prize: $100,000/year for life, current cash option $2,200,000;
- fixed lower tiers: $7,500, $500, $250, $50, $25, $8, $8;
- top prize is pari-mutuel and top-tier payouts can change in specified circumstances.

## Exact full-space portfolio
Number of distinct plays:

`C(58,5) * 5 = 22,910,580`.

Cost:

`22,910,580 * $5 = $114,552,900`.

For any realized winning white set, the number of our tickets with exactly m white matches is:

`C(5,m) * C(53,5-m)` for each fixed Millionaire Ball choice.

Because we buy all five Millionaire Ball choices, for each white subset count there is exactly one matching-ball ticket and four nonmatching-ball tickets.

Exact winning-ticket counts under full coverage:
- 5 + MB: 1
- 5 only: 4
- 4 + MB: 265
- 4 only: 1,060
- 3 + MB: 13,780
- 3 only: 55,120
- 2 + MB: 234,260
- 2 only: 937,040
- 1 + MB: 1,464,125

## Deliberately favorable rejection bound
To make rejection maximally favorable to the player:
- grant our single 5+MB winner the full current $18,000,000 cash option;
- grant **each** of our four 5-only winners the full $2,200,000 cash option;
- ignore any pari-mutuel reduction from external winners;
- ignore taxes, purchase/execution limits, financing and claim friction.

Gross under that optimistic bound:

`18,000,000`
`+ 4*2,200,000`
`+ 265*7,500`
`+ 1,060*500`
`+ 13,780*250`
`+ 55,120*50`
`+ 234,260*25`
`+ 937,040*8`
`+ 1,464,125*8`
`= $60,584,320`.

Return ratio:

`60,584,320 / 114,552,900 = 52.8876353%`.

Optimistic deterministic deficit:

`$114,552,900 - $60,584,320 = $53,968,580`.

## Conclusion
Even with assumptions strongly biased toward the player, full-space coverage returns only **~52.89%** of acquisition cost. Real pari-mutuel treatment, tax and execution constraints can only worsen the strict guarantee floor.

Therefore current Millionaire for Life full coverage is **REJECTED as a guaranteed-profit strategy**.

## Reusable result
This also strengthens the fast-screen heuristic for fixed-prize + one-special-ball games: exact full coverage can be evaluated without simulation from combinatorial match counts. Deep execution analysis is unnecessary when the optimistic deterministic return is already far below 100%.

Data: `data/derived/h026_millionaire_for_life_full_coverage.csv`
Code: `src/loto_research/special_ball_coverage.py`
Tests: `tests/test_special_ball_coverage.py`
