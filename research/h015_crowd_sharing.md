# H015 — crowd-choice / anti-popularity sharing edge

Updated: 2026-08-12
Status: **mechanism empirically real; exact-jackpot benefit bounded and usually modest; lower-tier rolldown magnitude still open**

## Question
Can choosing combinations that other players are less likely to choose improve expected payout enough to matter economically?

This does **not** change draw probability. The only mechanism is sharing: conditional on our ticket reaching a shared prize, fewer competing winning tickets means a larger expected share.

## Empirical basis: player choices are not uniform
Primary empirical literature using proprietary lottery-entry datasets finds substantial non-uniformity in player choices.

Wang, Potter van Loon, van den Assem & van Dolder, *Number Preferences in Lotteries*:
- millions of Lotto combinations;
- individual Lotto numbers should appear 13.33% under uniform 6/45 selection;
- observed examples include number 11 at 16.5%, 7 at 16.3%, versus 37 at 10.3% and 38 at 10.5%;
- birthday/personal numbers, small numbers, central positions, odd/prime numbers and aesthetic patterns are favored;
- popular combinations often form numeric sequences or spatial patterns and are selected far more often than random choice would imply.

A 2026 study by Crack, Whigham & Wisen uses over 70m played New Zealand Lotto six-tuples / 400m individual played numbers. Its abstract reports that self-selected strategies can be value-destroying in a fixed prize pool and that prize sharing is a first-order feature of ticket valuation.

These studies establish the mechanism class. They do **not** establish the crowd distribution for UK Lotto or Azerbaijan games; jurisdiction-specific calibration remains required.

## Exact jackpot duplicate model
For an exact 6/59 jackpot combination:

`M = C(59,6) = 45,057,474`.

Suppose there are `n` other played lines. Under uniform choice, another line selects our exact winning combination with probability `1/M`.

If our chosen combination has crowd popularity multiplier `a` relative to uniform, use:

`q = a/M`.

Conditional on our line winning, number of other identical jackpot winners is approximated as:

`X ~ Binomial(n, q)`.

Expected fraction of jackpot retained is:

`E[1/(1+X)] = [1-(1-q)^(n+1)] / ((n+1)q)`.

This exact helper already exists in `src/loto_research/probability.py`.

Derived scenarios:
- `data/derived/h015_jackpot_collision_screen_6of59.csv`

## Magnitude screen
### 5m other lines
Uniform exact combination:
- expected conditional jackpot share: **94.65%**.

Theoretical no-duplicate upper bound relative to uniform:
- **+5.65%** to the jackpot component.

A combination selected at 0.2× uniform popularity:
- share ≈98.90%;
- about **+4.49%** relative to uniform.

A 5×-popular combination:
- share ≈76.75%;
- about **−18.91%** relative to uniform.

### 10m other lines
Uniform:
- share ≈**89.68%**.

Theoretical no-duplicate upper bound:
- **+11.51%** relative to uniform.

0.2× popularity:
- share ≈97.81%;
- **+9.07%** relative to uniform.

5× popularity:
- share ≈60.41%;
- **−32.64%** relative to uniform.

10× popularity:
- share ≈40.16%;
- **−55.22%** relative to uniform.

### 15m other lines
Uniform:
- share ≈**85.06%**.

Theoretical no-duplicate upper bound:
- **+17.57%** relative to uniform.

0.2× popularity:
- share ≈96.74%;
- **+13.74%** relative to uniform.

5× popularity:
- share ≈48.71%;
- **−42.74%** relative to uniform.

## Interpretation
This sharpens H015 considerably.

### What anti-popularity can do
- It can protect a jackpot winner from avoidable sharing.
- Avoiding highly popular exact combinations can be materially valuable when sales are high.
- In a large-jackpot / rolldown state, an extra ~5–15% on the **jackpot component** can matter.

### What it cannot do by itself
Even the theoretical no-duplicate upper bound is only about +6% to +18% on the jackpot component for 5m–15m other 6/59 lines. It is **not** a +6–18% improvement to total ticket EV unless the entire ticket value comes from the jackpot.

Therefore exact-combination anti-popularity cannot plausibly rescue a deeply negative ordinary lottery by itself. Its highest value is as an overlay optimizer once another mechanism has already made the draw unusually favorable.

### Popular selections are more dangerous than unpopular selections are magical
The downside from choosing a very popular combination is asymmetric and can be large: at 10m lines, a 5×-popular exact combination loses roughly one-third of its conditional jackpot share versus uniform, while the maximum upside from perfect uniqueness is only about 11.5%.

So a robust practical objective is first to **avoid known crowd magnets**, rather than claim that any specific “unpopular numbers” recipe creates +EV.

## Lower-tier shared-pool question remains open
The exact-duplicate jackpot model is not sufficient for shared lower tiers such as rolldown categories. There, many different played combinations can reach the same match class, and player-number biases interact with the drawn numbers.

Observed UK Lotto two-round winner-count asymmetries are consistent with this being economically meaningful, but they do not yet identify a pre-draw optimal portfolio.

Next H015 test:
1. build a crowd-choice model from empirical number/combination preferences;
2. simulate/derive expected competing-winner counts for lower shared match tiers;
3. compare random-generated lines, human-looking lines, and deliberately anti-crowd lines;
4. estimate payout uplift specifically in a forced-redistribution/rolldown state;
5. include self-collision for multi-line portfolios.

## Current status
**H015 remains promising as an overlay optimizer, not a standalone +EV strategy.**

The exact jackpot-sharing part is now bounded quantitatively. The unresolved high-value part is lower-tier shared-pool optimization during an already favorable structural state.
