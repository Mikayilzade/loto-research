# H015 crowd-choice simulation framework

Updated: 2026-08-15

## Goal
Estimate how a chosen line changes the expected number of **other** winners in a shared prize category, conditional on our own line hitting that category. This is the missing bridge between documented human number-selection bias and actual pari-mutuel EV.

The framework does **not** predict winning numbers. It models the crowd.

## Primary empirical basis
1. Ding, *What Numbers to Choose for My Lottery Ticket? Behavior Anomalies in the Chinese Online Lottery Market* (2011): field evidence in a pari-mutuel lottery that players can be attracted toward numbers already shown as popular rather than strategically avoiding them.
   - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1926526
2. Lien & Yuan, *The Cross-Sectional Gambler's Fallacy: Set Representativeness in Lottery Number Choices* (2015): >1.6m tickets; over-selection of representative/evenly-spread number sets creates a cost under pari-mutuel sharing.
   - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2636121
3. Wang et al., *Number Preferences in Lotteries* (2016): proprietary datasets show personally meaningful and situationally available numbers, center-of-form attraction, and extremely popular numeric sequences/spatial patterns.
   - https://www.cambridge.org/core/journals/judgment-and-decision-making/article/number-preferences-in-lotteries/47BA27051627CEED421AD3AEE255521E
4. Polin, Ben Isaac & Aharon, *Patterns in manually selected numbers in the Israeli lottery* (2021): >800m manual selections; stable number preferences, strong low-number effect, form-position effect and demand-linked convergence toward more uniform selection.
   - https://www.cambridge.org/core/journals/judgment-and-decision-making/article/patterns-in-manually-selected-numbers-in-the-israeli-lottery/F7167C1DD46E4876DAFCDDD6CE8F238C
5. Crack, Whigham & Wisen, *Lotto Revealed* (2026): >70m played six-tuples / >400m individual played numbers; prize sharing is a first-order valuation feature and self-selected-number strategies can materially alter expected payoff.
   - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6572761

## Implemented code
`src/loto_research/crowd_choice.py`

Features currently parameterized:
- birthday/low-number attraction;
- lucky-number attraction;
- center-of-range attraction;
- consecutive-pair attraction;
- evenly-spaced / representative-set attraction.

The sampler uses a candidate-batch softmax rather than enumerating the full combination space. This is an engineering approximation, not an empirical calibration.

Core functions:
- score a line for synthetic crowd attractiveness;
- generate biased crowd lines;
- sample winning draws conditional on our ticket obtaining exactly `k` matches;
- estimate the probability an independently sampled crowd ticket hits a chosen competitor tier under that condition;
- rank candidate lines by low synthetic crowd-attraction score.

## Synthetic pipeline test — NOT a real-EV result
A deliberately biased illustrative 6/59 model was used only to verify that the framework can express a meaningful anti-crowd effect.

Parameters:
- birthday weight 0.6;
- lucky-number weight 0.8 (`7`);
- center weight 0.3;
- consecutive-pair weight 0.4;
- even-spacing weight 0.3;
- candidate batch 24.

Example lines:
- high crowd score: `3 7 12 18 24 30`, score ≈ 4.7372;
- low crowd score candidate: `36 40 48 51 56 58`, score ≈ 0.1725.

Conditional experiment:
- assume our line hits exactly 3/6;
- ask probability a crowd ticket also hits exactly 3/6;
- 10 independent seeds × 10,000 simulations each.

Observed synthetic probabilities:
- high-score line mean competitor probability ≈ **0.01664**;
- low-score line mean competitor probability ≈ **0.00682**;
- mean relative intensity ≈ **0.414**; median run ratio ≈ **0.392**.

Data: `data/derived/h015_synthetic_crowd_screen.csv`.

Interpretation: the pipeline can produce the kind of 0.4× competitor-intensity state that would be economically important in a shared lower tier. **This does not establish that any real lottery permits a 0.4× reduction.** The weights were not fitted to a target crowd.

# Published-anchor calibration packet
New code: `src/loto_research/crowd_empirical.py`.
New data: `data/derived/h015_empirical_anchor_summary.csv`.

Wang et al. provide usable numerical anchors for Dutch 6/45 manual selections:
- uniform marginal frequency = 13.333%;
- number 11 = 16.5% => **1.2375× uniform**;
- number 7 = 16.3% => **1.2225×**;
- number 37 = 10.3% => **0.7725×**;
- number 38 = 10.5% => **0.7875×**;
- diagonal/vertical pattern class = 0.9% actual vs 0.009% random => about **100× class-level overrepresentation**.

Holding four otherwise-unmodeled numbers fixed, the sparse independent anchor gives:

`weight(37,38) / weight(7,11) ≈ 0.402119353`.

This is an empirical **collision-weight sensitivity anchor**, not a calibrated probability for a current game. It shows that even number-level choices alone can plausibly generate multi-fold relative crowd differences before adding birthday, layout and pattern effects.

Polin et al. provide a second large-data replication:
- nearly 115m manually chosen tickets / 805m individual selections across 118 draws;
- 7 was the most popular main number in every draw; 37 the least popular in every draw;
- manual-pick mean number was about 17.5–17.75 vs uniform expectation 19, confirming persistent low-number preference;
- each additional million NIS of jackpot correlated with about 33,000 additional manual guesses;
- as participation/jackpot increased, popular numbers became less popular and unpopular numbers became less unpopular: **crowd bias moves toward uniform in large-jackpot states**.

That last finding matters strategically: a static anti-crowd model will tend to **overstate** sharing benefit exactly when large jackpots attract extra occasional players. The new empirical module therefore exposes `shrink_anchor_toward_uniform()` as a sensitivity control, but does not invent a fitted shrinkage coefficient.

# Terminal guarantee screen for H015
Anti-crowd ticket choice changes only the amount retained **conditional on a winning outcome**. It does not change the set of draw outcomes in which a ticket loses.

Therefore, for any positive-cost ticket or portfolio that still has at least one zero-return outcome:

**anti-crowd choice alone cannot guarantee strictly positive profit across all outcomes.**

This is a necessary-condition proof, not an empirical claim. A guaranteed-profit construction would need an additional mechanism that eliminates losing outcome branches or makes their minimum payout exceed total cost — for example full-space/covering constructions, guaranteed overlays, or arbitrage. Those belong under H012/H005 rather than H015.

So H015 is now closed as a **standalone terminal-guarantee path** while remaining open as an EV-enhancing overlay for another structural edge.

## Scientific gate before real EV claims
H015 may advance beyond synthetic/published-anchor demonstration only after all of the following:
1. Select a target lottery with genuinely shared lower-tier pools / rolldown money.
2. Obtain player-choice data or an observable proxy rich enough to calibrate crowd behavior.
3. Fit number-level and combination-level biases on a training period.
4. Hold out later draws / ticket batches for out-of-sample validation.
5. Validate not only marginal number frequencies but combination features and winner-count distributions.
6. Compare anti-crowd candidate lines against uniform random and simple heuristics.
7. Convert predicted competitor intensity into expected retained pool share using the actual sales volume and prize-pool rules.
8. Model jackpot-size-dependent bias homogenization.
9. Only then combine the sharing uplift with the game's baseline structural EV.

## Current conclusion
- Human crowd bias and prize-sharing effects: **validated mechanism class**.
- Parameterized simulator: **implemented and tested**.
- Sparse published empirical anchors: **implemented**.
- Synthetic anti-crowd effect: **pipeline demonstration only**.
- Real calibrated lower-tier edge: **not yet validated**.
- H015 as standalone guaranteed-profit strategy: **REJECTED by necessary-condition proof**.
- H015 as overlay optimizer on a separate +EV/coverage mechanism: **still live**.
- Guaranteed profit: **not found**.
