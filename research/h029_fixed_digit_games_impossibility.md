# H029 — fixed-odds digit games: additive-portfolio impossibility

Updated: 2026-08-16
Status: **Virginia Pick 3 / Pick 4 / Pick 5 base-game class closed as guaranteed-profit path under additive play rules**

## Goal
Close a broad class of finite daily digit lotteries without repeating full-space brute-force calculations game by game.

Target structure:
- a finite uniformly drawn digit outcome space;
- fixed cash payouts by wager type;
- arbitrary nonnegative portfolio of base-game wagers;
- no external deterministic subsidy or state-dependent jackpot overlay.

If every available wager has expected gross return below stake, then no portfolio composed only of those wagers can have strictly positive profit for every draw outcome.

## Impossibility theorem
Let a portfolio contain wagers `i=1..n` with stakes `c_i > 0` and outcome-dependent payouts `X_i(ω) >= 0`.

Portfolio profit is:

`P(ω) = Σ_i X_i(ω) - Σ_i c_i`.

If the portfolio were strictly profitable for every legal draw outcome, then:

`P(ω) > 0  for all ω`.

Taking expectation under the official uniform draw distribution gives:

`E[P] > 0`.

But if each constituent wager has `E[X_i] <= c_i`, then by linearity:

`E[P] = Σ_i E[X_i] - Σ_i c_i <= 0`,

contradiction.

Therefore **no nonnegative additive mixture of individually non-positive-EV fixed digit wagers can produce an all-outcome positive-profit guarantee**.

This theorem permits class closure once the current wager menu is checked.

## Current control: Virginia Pick 3
Official Virginia Lottery page (current July/August 2026 structure):
- digits `000..999`;
- $1 or $0.50 base play;
- Exact, Any Order, 50/50, Combo, Pair wager families;
- Exact $1 top prize $500, odds 1/1000.

Primary source:
- https://www.valottery.com/data/draw-games/pick3

Using exact combinatorics rather than rounded displayed odds, gross EV per $1-equivalent base stake is:

| wager | gross EV / stake |
|---|---:|
| Exact | 0.5000 |
| Any Order 3-way | 0.4800 |
| Any Order 6-way | 0.4800 |
| 50/50 3-way | 0.4900 |
| 50/50 6-way | 0.4900 |
| Combo 3-way | 0.5000 |
| Combo 6-way | 0.5000 |
| Pair | 0.5000 |

Example 50/50 3-way calculation: one exact ordering pays $330 and the other two permutations pay $80, so expected payout is `(330 + 2*80)/1000 = $0.49` per $1 play.

Result: every checked base wager is at most 50% gross EV.

## Virginia Pick 4
Official current page:
- digits `0000..9999`;
- $1 or $0.50 base play;
- Exact, Any Order, 50/50, Combo;
- Exact $1 prize $5,000, odds 1/10,000.

Primary source:
- https://www.valottery.com/data/draw-games/pick4

Exact base-game EV ratios:

| wager | gross EV / stake |
|---|---:|
| Exact | 0.5000 |
| Any Order 4-way | 0.4800 |
| Any Order 6-way | 0.4800 |
| Any Order 12-way | 0.4800 |
| Any Order 24-way | 0.4800 |
| 50/50 4-way | 0.4900 |
| 50/50 6-way | 0.4900 |
| 50/50 12-way | 0.4900 |
| 50/50 24-way | 0.4900 |
| Combo 4/6/12/24-way | 0.5000 |

Thus every current base wager is again <1 EV, in fact <=50% gross.

## Virginia Pick 5
Official current page:
- digits `00000..99999`;
- $1 or $0.50 base play;
- Exact, Any Order and 50/50 wager families;
- Exact $1 prize $50,000, odds 1/100,000.

Primary source:
- https://www.valottery.com/data/draw-games/pick5

Exact base-game EV ratios:

| wager | gross EV / stake |
|---|---:|
| Exact | 0.5000 |
| Any Order 5-way | 0.5000 |
| Any Order 10-way | 0.5000 |
| Any Order 20-way | 0.5000 |
| Any Order 30-way | 0.4950 |
| Any Order 60-way | 0.4800 |
| Any Order 120-way | 0.4800 |
| 50/50 5-way | 0.5000 |
| 50/50 10-way | 0.5000 |
| 50/50 20-way | 0.5000 |
| 50/50 30-way | 0.4975 |
| 50/50 60-way | 0.4900 |
| 50/50 120-way | 0.4900 |

Again no base wager reaches break-even.

## Full exact-space sanity checks
The simplest all-outcome cover using every Exact number once gives deterministic gross return:
- Pick 3: spend $1,000; exactly one Exact wins $500 -> **50%**;
- Pick 4: spend $10,000; exactly one Exact wins $5,000 -> **50%**;
- Pick 5: spend $100,000; exactly one Exact wins $50,000 -> **50%**.

The theorem above is stronger: adding/mixing Any, 50/50, Combo or Pair wagers cannot transform these negative-EV linear components into a strict all-outcome positive guarantee.

## FIREBALL scope
Virginia FIREBALL is a separate add-on that doubles the cost and creates additional replacement-number winning combinations. It is **not** silently included in the base-class theorem result here. It requires its own exact joint-outcome EV check because FIREBALL payouts can stack with base wins.

However, the official pages already show FIREBALL as an additional paid random wager, not a deterministic subsidy. It remains a separate H029b branch rather than a loophole assumed away.

## Conclusion
For current Virginia Pick 3, Pick 4 and Pick 5 **base games**, the entire additive portfolio class is closed as a terminal guaranteed-profit route. Every listed base wager has gross EV <= 0.50 of stake, so any strict all-outcome positive guarantee would contradict linearity of expectation.

Status: **REJECTED guaranteed-profit base-game class**.

Next useful extension: H029b exact FIREBALL joint-outcome analysis, or move to another genuinely nonlinear/state-subsidized product rather than repeating ordinary fixed-digit base games.