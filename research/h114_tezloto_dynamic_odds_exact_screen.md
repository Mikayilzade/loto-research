# H114 — Azerbaijan TezLoto exact dynamic-odds screen

Updated: 2026-08-20
Status: **BASE ODDS + COMPLETE-COVERAGE ARBITRAGE CLOSED / BIAS BRANCH ONLY REMAINS / NO SUCCESS**

## Why this branch matters
TezLoto is unusually valuable for H007 because the official operator publishes a full state-dependent odds table while play remains open after each drawn ball. The game draws 35 of 48 virtual balls and lets the player bet on the next ball or on whether selected balls appear within the next 2 or next 6 balls.

Official source (current 2026):
- https://www.azerlotereya.com/lotereya/fast-loto
- registration no. 341 / 05.11.2025; validity 27.10.2025–27.10.2030
- minimum ticket price displayed: 0.2 AZN

The published table has rows 1–35 corresponding to the position of the next ball in the draw. Before position `j`, the number of balls still available is

`n = 49 - j`.

This interpretation exactly explains all five published odds columns and permits an exact fair-odds comparison.

## Exact fair probabilities
Assuming uniform sampling without replacement from the remaining `n` balls:

1. **Next ball, one exact number**
   - probability `1/n`
   - fair decimal payout `n`.

2. **Next 2 balls, two specified numbers both appear**
   - probability `1 / C(n,2)`
   - fair decimal payout `C(n,2)`.

3. **One specified number appears among next 6**
   - probability `6/n`
   - fair decimal payout `n/6`.

4. **Two specified numbers both appear among next 6**
   - probability `C(6,2) / C(n,2)`
   - fair decimal payout `C(n,2)/15`.

5. **Three specified numbers all appear among next 6**
   - probability `C(6,3) / C(n,3)`
   - fair decimal payout `C(n,3)/20`.

For every published state, expected gross return per 1-unit stake is simply

`RTP = published_odds / fair_odds`.

## Exhaustive published-table result
All **159 currently published state × bet-type cells** were evaluated exactly.

| Bet type | Minimum gross return | Maximum gross return | Mean gross return |
|---|---:|---:|---:|
| Next exact ball | 71.4286% | 78.0488% | 76.1452% |
| Exact two balls within next 2 | 75.0000% | 78.1609% | 77.1409% |
| One selected ball within next 6 | 76.9565% | **78.2609%** | 77.6659% |
| Two selected balls within next 6 | 74.5614% | 78.1513% | 76.8023% |
| Three selected balls within next 6 | 75.2137% | 78.2361% | 77.1023% |

The single best published cell is only **78.2609% gross return**, before tax/execution friction. No row or bet type is positive-EV under the stated uniform draw model.

Derived table:
- `data/derived/h114_tezloto_dynamic_odds_screen.csv`

## Complete-coverage theorem
The same calculation closes the obvious deterministic-arbitrage idea of betting every possible outcome at a given state.

### Next exact ball
Buy one ticket on every remaining number. Exactly one ticket wins.

- spend = `n`
- gross = `published_odds`
- return ratio = `published_odds/n = RTP < 1`.

### Exact next-two pair
Buy every unordered pair of remaining balls. Exactly one pair is the next-two set.

- spend = `C(n,2)`
- gross = `published_odds`
- ratio = `published_odds/C(n,2) < 1`.

### One-of-next-six
Buy one ticket for every remaining number. Exactly six tickets win.

- spend = `n`
- gross = `6 × published_odds`
- ratio = `published_odds/(n/6) < 1`.

### Two-of-next-six
Buy every remaining pair. Exactly `C(6,2)=15` tickets win.

- spend = `C(n,2)`
- gross = `15 × published_odds`
- ratio = `published_odds / [C(n,2)/15] < 1`.

### Three-of-next-six
Buy every remaining triple. Exactly `C(6,3)=20` tickets win.

- spend = `C(n,3)`
- gross = `20 × published_odds`
- ratio = `published_odds / [C(n,3)/20] < 1`.

Thus all five complete-coverage constructions are deterministic losses at every currently published state. Mixing such symmetric linear tickets cannot create an all-outcome positive guarantee without an external nonlinear subsidy/rebate.

## What remains open: H007 bias only
TezLoto is still a useful H007 target because it is high-frequency and state-dependent. A persistent non-uniform RNG/virtual-lototron distribution could in principle make a specific number positive-EV even though the base table is negative.

For a one-number next-ball bet with published decimal payout `o`, positive EV requires the true conditional probability to satisfy

`p(number | current state) > 1/o`.

At the best base cell, overcoming an RTP of 0.782609 requires roughly a **27.78% multiplicative probability lift above uniform** (`1/0.782609 - 1`). Other cells require still larger distortion.

That is a large bias hurdle. It must be demonstrated on a reliable draw history with train/test or forward validation. Hot/cold-number displays or in-sample frequency deviations are not enough.

A strict guaranteed-profit result would require an even stronger statement: a defensible lower bound on the conditional winning probability or a deterministic flaw, plus execution before odds change. No such evidence exists yet.

## Result
**H114 closes TezLoto's published base-odds, dynamic-state, and full-coverage routes as guaranteed-profit or positive-EV strategies.** The only defensible remaining TezLoto branch is empirical H007 RNG/virtual-draw bias testing if a sufficiently large reliable history can be collected.
