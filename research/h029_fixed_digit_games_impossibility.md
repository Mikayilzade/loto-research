# H029 — fixed-odds digit games: additive-portfolio impossibility

Updated: 2026-08-16
Status: **Virginia Pick 3 / Pick 4 / Pick 5 base games AND FIREBALL paid add-ons closed as guaranteed-profit paths under additive play rules**

## Goal
Close a broad class of finite daily digit lotteries without repeating full-space brute-force calculations game by game.

Target structure:
- a finite uniformly drawn digit outcome space;
- fixed cash payouts by wager type;
- arbitrary nonnegative portfolio of paid wagers;
- no external deterministic subsidy or state-dependent jackpot overlay.

If every available constituent wager has expected gross return below stake, then no portfolio composed only of those wagers can have strictly positive profit for every draw outcome.

## Impossibility theorem
Let a portfolio contain wagers `i=1..n` with stakes `c_i > 0` and outcome-dependent payouts `X_i(ω) >= 0`.

Portfolio profit is:

`P(ω) = Σ_i X_i(ω) - Σ_i c_i`.

If the portfolio were strictly profitable for every legal draw outcome, then `P(ω) > 0` for all `ω`, hence `E[P] > 0`.

But if every constituent wager has `E[X_i] <= c_i`, linearity gives:

`E[P] = Σ_i E[X_i] - Σ_i c_i <= 0`,

a contradiction.

Therefore **no nonnegative additive mixture of individually non-positive-EV wagers can produce an all-outcome positive-profit guarantee**.

# A. Base games
## Virginia Pick 3
Official current page:
- digits `000..999`;
- $1 or $0.50 base play;
- Exact, Any Order, 50/50, Combo, Pair wager families;
- Exact $1 top prize $500, odds 1/1000.

Primary source: https://www.valottery.com/data/draw-games/pick3

Exact combinatorics give gross EV/stake:
- Exact 0.5000;
- Any Order 3/6-way 0.4800;
- 50/50 3/6-way 0.4900;
- Combo 3/6-way 0.5000;
- Pair 0.5000.

## Virginia Pick 4
Primary source: https://www.valottery.com/data/draw-games/pick4

Current base menu Exact, Any Order, 50/50 and Combo yields gross EV/stake only 0.48–0.50.

## Virginia Pick 5
Primary source: https://www.valottery.com/data/draw-games/pick5

Current Exact, Any Order and 50/50 menu yields gross EV/stake only 0.48–0.50; 30-way variants fall between.

## Full Exact-space sanity checks
Buying every exact number once gives deterministic 50% return:
- Pick 3: $1,000 spend -> $500;
- Pick 4: $10,000 -> $5,000;
- Pick 5: $100,000 -> $50,000.

The theorem is stronger: mixing other base wagers cannot turn the negative-EV linear components into a strict guarantee.

# B. H029b — FIREBALL exact rejection bound
Virginia's official pages state for Pick 3/4/5:
- a FIREBALL digit 0–9 is drawn after the base drawing;
- it may replace one Lottery-drawn digit, creating additional winning combinations;
- FIREBALL wins are separate and additional to base wins;
- **adding FIREBALL doubles the cost of the underlying play**.

This means the incremental FIREBALL stake equals the underlying base wager cost.

## Conservative method
The official prize tables publish a FIREBALL prize and an approximate `1 in N` odds value for each wager family.

For ordinary Exact/Any/Combo/Pair rows, compute:

`EV_fireball = prize / N`.

For 50/50 rows, the official page says the Exact prize includes the Any Order payout. Instead of reconstructing overlap exactly, this test deliberately **double-counts** the published Exact and Any rows:

`EV_upper = exact_prize/exact_odds + any_prize/any_odds`.

That overstates player value, so if even this upper bound is below the incremental FIREBALL cost, negative EV is proven without needing exact overlap mechanics.

Code: `src/loto_research/fireball_bounds.py`
Data: `data/derived/h029b_virginia_fireball_ev_bounds.csv`
Tests: `tests/test_fireball_bounds.py`

## Results — FIREBALL incremental EV upper bounds
Across every currently listed paid FIREBALL wager checked:
- Pick 3 maximum upper-bound FIREBALL EV/stake: **0.655999** (`50/50 3-way`, overlap deliberately overcounted);
- Pick 4 maximum: **0.628960** (`50/50 4-way`, overlap deliberately overcounted);
- Pick 5 maximum: **0.603587** (`50/50 5-way`, overlap deliberately overcounted).

All non-50/50 rows are lower; normalized Combo FIREBALL EV is also well below its incremental cost because Combo FIREBALL cost scales with the base Combo cost.

Since every base wager has EV/stake <= 0.50, the deliberately favorable combined base+FIREBALL upper bound is at most:

`(0.50 + 0.655999) / 2 = 0.5779995`.

So even the best overestimated current combined wager returns **<57.8% gross EV** per doubled stake. The true value is no higher and generally lower.

## Why this closes the entire paid Virginia Pick family
Treat every legal base-only wager and every legal base+FIREBALL wager as a constituent instrument. We have shown every constituent has EV <= stake, with a very large margin.

Any nonnegative portfolio of these instruments therefore also has non-positive expected profit. A portfolio that guaranteed strictly positive profit in every base-digit/FIREBALL outcome would necessarily have positive expected profit, contradiction.

Thus no amount of:
- exact-number coverage;
- combining Pick 3/4/5 wager types;
- mixing base-only and FIREBALL tickets;
- repeating tickets;
- day/night multi-draw packaging;

can manufacture a strict all-outcome positive-profit guarantee under the current additive pricing/payout rules. Multi-draw and Repeat merely replicate paid wagers and do not add a deterministic subsidy.

# Conclusion
**H029 and H029b are CLOSED.** Current Virginia Pick 3, Pick 4 and Pick 5, including their FIREBALL paid add-ons, cannot form a guaranteed-profit portfolio under additive play rules.

This is a class theorem, not merely a failed full-space example.

Future reopening condition: only a genuine nonlinearity such as deterministic withdrawable cashback, free guaranteed-value entries, pricing error, externally funded fixed subsidy, or materially changed payout rules would evade this proof.