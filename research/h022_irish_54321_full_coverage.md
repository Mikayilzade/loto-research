# H022 — Irish Lotto 5-4-3-2-1 full-coverage theorem

Updated: 2026-08-15
Status: **REJECTED as guaranteed-profit full-coverage strategy**

## Goal
Screen a current finite fixed-payout side game where every selectable combination can be bought and the realized payout under full coverage is deterministic.

Target: Irish National Lottery **Lotto 5-4-3-2-1**.

Official current page (checked 2026-08-15):
- player selects k = 1..5 numbers;
- game can be based on either the 6 main Lotto numbers or the 7-number set including the Bonus Ball;
- base play starts at €1;
- to win, all selected numbers must match;
- current fixed €1-stake payouts:
  - 6-number game: k1 €6, k2 €45, k3 €550, k4 €6,000, k5 €125,000;
  - 7-number game: k1 €5, k2 €32, k3 €275, k4 €3,000, k5 €40,000.

Primary current source:
- https://www.lottery.ie/game-information/lotto-5-4-3-2-1

The operator also announced on 2026-07-16 that Lotto will move from 47 balls to 45 in autumn 2026. This future regime is stress-tested below **holding today’s 5-4-3-2-1 payout table constant**, which is deliberately favorable as a sensitivity analysis, not a claim about final future rules.

Source:
- https://www.lottery.ie/news/press-releases/national-lottery-unveils-exciting-changes-to-lotto-and-lotto-plus-games

## Exact full-space identity
For pool size N and selection size k, buy every k-subset exactly once.

Portfolio size / cost at €1 each:

`C(N,k)`.

If the winning target set contains d numbers (d=6 for main-number game, d=7 including Bonus), exactly

`C(d,k)`

of our tickets win, independent of which numbers are drawn.

Therefore deterministic full-space gross is:

`C(d,k) * fixed_payout(k)`

and deterministic return ratio is:

`C(d,k) * fixed_payout(k) / C(N,k)`.

No Monte Carlo, number-selection assumption, or crowd model is required.

## Current 47-ball regime
### 6-number game
| k | full-space cost (€) | winning tickets | deterministic gross (€) | return |
|---:|---:|---:|---:|---:|
|1|47|6|36|76.5957%|
|2|1,081|15|675|62.4422%|
|3|16,215|20|11,000|67.8384%|
|4|178,365|15|90,000|50.4583%|
|5|1,533,939|6|750,000|48.8937%|

### 7-number game including Bonus
| k | full-space cost (€) | winning tickets | deterministic gross (€) | return |
|---:|---:|---:|---:|---:|
|1|47|7|35|74.4681%|
|2|1,081|21|672|62.1647%|
|3|16,215|35|9,625|59.3586%|
|4|178,365|35|105,000|58.8681%|
|5|1,533,939|21|840,000|54.7610%|

Best current full-coverage return is only **76.5957%**, so every k and both game variants are guaranteed losses before execution friction.

## Announced 45-ball sensitivity
Assume only the pool shrinks from 47 to 45 and the current fixed payouts remain unchanged.

### 6-number game
returns by k=1..5:
- 80.0000%
- 68.1818%
- 77.5194%
- 60.4047%
- 61.3869%

### 7-number game
returns by k=1..5:
- 77.7778%
- 67.8788%
- 67.8295%
- 70.4722%
- 68.7533%

Even this favorable future sensitivity never reaches break-even; maximum is **80%**.

## Strategic conclusion
H022 is closed as a guaranteed-profit path.

This also provides a useful generic theorem for fixed-payout subset games: full coverage is trivial to screen analytically by comparing `C(d,k)*P_k` against `C(N,k)*stake`. Any candidate below 100% can be rejected without portfolio search.

Files:
- `src/loto_research/fixed_subset_coverage.py`
- `tests/test_fixed_subset_coverage.py`
- `data/derived/h022_irish_54321_full_coverage.csv`
