# H015 — crowd-choice / anti-popularity sharing edge

Updated: 2026-08-12
Status: **mechanism empirically real; exact-jackpot benefit bounded; lower-tier shared-pool sensitivity can be large but pre-draw crowd model remains missing**

## Question
Can choosing combinations that other players are less likely to choose improve expected payout enough to matter economically?

This does **not** change draw probability. The only mechanism is sharing: conditional on our ticket reaching a shared prize, fewer competing winning tickets means a larger expected share.

## Empirical basis: player choices are not uniform
Primary empirical literature using proprietary lottery-entry datasets finds substantial non-uniformity in player choices.

Wang, Potter van Loon, van den Assem & van Dolder, *Number Preferences in Lotteries*:
- millions of Lotto combinations;
- under uniform 6/45 choice each number should appear 13.33%; observed examples include 11 at 16.5%, 7 at 16.3%, versus 37 at 10.3% and 38 at 10.5%;
- birthday/personal numbers, smaller numbers, central positions and aesthetically attractive selections are over-used;
- many of the most popular exact combinations are numeric sequences or visual patterns;
- **0.9%** of played combinations were classified as diagonal/vertical patterns versus only **0.009%** expected under randomness — about 100× overrepresentation at the pattern-class level;
- with 5,108,343 combinations, under random choice there was only ~0.1% probability that any exact combination would occur more than ten times, yet many actual popular combinations appeared hundreds of times.

A 2026 study by Crack, Whigham & Wisen uses over 70m played New Zealand Lotto six-tuples / 400m individual played numbers. Its abstract reports that self-selected strategies can be value-destroying in a fixed prize pool and that prize sharing is a first-order feature of ticket valuation.

These studies establish the mechanism class. They do **not** establish the crowd distribution for UK Lotto or Azerbaijan games; jurisdiction-specific calibration remains required.

# 1. Exact jackpot duplicate model
For a 6/59 jackpot combination:

`M = C(59,6) = 45,057,474`.

If there are `n` other lines and our exact combination has popularity multiplier `a` relative to uniform:

`q = a/M`.

Conditional on our line winning:

`X ~ Binomial(n,q)`

and expected retained jackpot share is:

`E[1/(1+X)] = [1-(1-q)^(n+1)] / ((n+1)q)`.

Derived data:
- `data/derived/h015_jackpot_collision_screen_6of59.csv`

## Magnitude
At 10m other lines:
- uniform: expected share ≈ **89.68%**;
- 0.2× popularity: ≈ **97.81%**, +9.07% to jackpot component vs uniform;
- theoretical no-duplicate maximum: +11.51% vs uniform;
- 5× popular: ≈ **60.41%**, −32.64% vs uniform;
- 10× popular: ≈ **40.16%**, −55.22% vs uniform.

Across 5m–15m other lines, perfect uniqueness improves the jackpot component by only about **+5.65% to +17.57%** relative to uniform.

Interpretation: exact-combination anti-popularity is useful protection from dilution, but cannot by itself rescue a deeply negative ordinary game. Avoiding crowd magnets is more important than searching for a mythical perfectly unpopular line.

# 2. Lower-tier shared-pool sensitivity
Exact jackpot duplicates are a relatively weak sharing channel because expected number of other jackpot winners is small. A rolldown/shared lower category can have tens, hundreds, thousands or more competing winning variants.

Let `lambda` be the expected number of **other** winners in a shared category conditional on our ticket hitting that category. Approximate competitor count as:

`X ~ Poisson(lambda)`.

Then expected retained pool fraction is:

`E[1/(1+X)] = (1-exp(-lambda))/lambda`.

Suppose our ticket construction changes expected competitor intensity by factor `a`, so `lambda -> a*lambda`. Derived sensitivity:
- `data/derived/h015_shared_pool_intensity_sensitivity.csv`

For categories with many expected competitors (`lambda >= 100`), the relationship is essentially inverse:

| relative competitor intensity | approximate payout vs baseline |
|---:|---:|
| 0.5× | **2.00×** |
| 0.6× | **1.667×** |
| 0.8× | **1.25×** |
| 1.0× | 1.00× |
| 1.2× | 0.833× |
| 1.5× | 0.667× |
| 2.0× | 0.50× |

Thus, **if** a pre-draw construction can reduce expected crowd overlap in a shared lower category by 20%, expected payout from that category rises roughly 25%; a 40% reduction raises it roughly 67%.

This is a sensitivity result, not evidence that we can currently achieve those `a` values.

# 3. Strategic interpretation
### Stronger result than exact-jackpot anti-duplication
Lower-tier sharing can have much larger percentage sensitivity than exact jackpot sharing because the category contains many winners. This is precisely where H015 could matter during a Cash-WinFall-like / Must-Be-Won redistribution.

### The decisive unresolved problem is prediction of competitor intensity
We need a model that maps **our chosen line** to expected number of other tickets reaching the same match category conditional on our line hitting it.

This is harder than exact duplicate avoidance. A lower-tier competitor need not hold our exact combination; many different selections can match the drawn set at the same tier.

Therefore simple heuristics such as “pick high numbers” or “avoid birthdays” cannot yet be promoted into an expected-payout claim.

### Practical anti-crowd rules that are already defensible qualitatively
Empirical data strongly justify avoiding obvious human-choice magnets such as:
- visual lines/diagonals on the entry form;
- simple numeric sequences;
- culturally salient / personally meaningful patterns;
- combinations concentrated in common birthday ranges when the game extends well above 31.

These rules reduce obvious collision risk, but their exact expected-EV benefit must be calibrated game-by-game.

# 4. Next quantitative test
Build a synthetic/empirical crowd-choice generator with at least three populations:
1. uniform/random-generated tickets;
2. human-like tickets calibrated to published marginal/pattern biases;
3. deliberately anti-crowd tickets.

Then, for each possible or sampled draw:
- condition on our line reaching a target shared tier;
- count competing crowd winners;
- estimate payout multiplier vs random;
- test out-of-sample on an independent empirical dataset or current-game winner-count data;
- include our own portfolio self-collision.

The output should be a **distribution of relative payout uplift**, not a list of “lucky/unlucky numbers”.

## Current status
**H015 is now quantitatively promising as an overlay optimizer, not a standalone +EV strategy.**

Exact-jackpot benefit is bounded and modest. Lower-tier shared-pool sensitivity can be much larger, but the pre-draw crowd-overlap model is the remaining scientific bottleneck.
