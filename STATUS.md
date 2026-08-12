# STATUS

Updated: 2026-08-12
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## Work-session rule
Research runs in short packets. After every meaningful discovery or roughly 2–4 substeps:
1. save raw/derived data;
2. update the relevant research note;
3. update this file when the strategic conclusion changes.

This file is the authoritative handoff checkpoint. Read `START_HERE.md`, `PROJECT_RULES.md`, `RESEARCH_PLAN.md` and `AGENTS.md` before code work.

# Validated structural benchmark
## Cash WinFall
Historical 2011 roll-down benchmark using exact 6/46 probabilities and cash-only tiers:
- ticket: $2;
- expected payout: **$2.2137120403**;
- expected ROI: **+10.6856%** before tax/execution.

Conclusion: structural +EV lotteries have existed without predicting numbers.

# Azerbaijan baseline games
## Beşdə 5
- jackpot odds **1 in 376,992**;
- favorable gross baseline **0.535555131 AZN / 1-AZN variant**;
- net before tax/sharing about **-46.44%**.

## Super Keno — multiplier mechanics resolved
Files:
- `data/derived/az_superkeno_multiplier_ev.csv`
- `research/superkeno_multiplier_economics.md`

One variant supports **1x / 2x / 5x / 10x** payment and proportional prize scaling. The advertised 1m maximum is the 10x version of the 100k base top tier, not a free overlay.

Gross displayed-table payout ratio is invariant at **59.8556%**. Favorable single-variant after-tax payout ratios are approximately:
- 1x **59.1807%**
- 2x **59.1266%**
- 5x **58.9036%**
- 10x **58.6982%**.

Top-prize sharing is ignored in these favorable bounds. Conclusion: **no multiplier EV edge; 1x is best on after-tax ROI absent promotion**.

# Azerbaijan 4+4 — top local draw-game target, currently data-blocked for state accounting
Strong empirical draw-table engine:
- III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U;
- draw #790 and #781 independently confirm the structure;
- eight samples give mean `U/N_hat≈0.01000654`, median `≈0.00995289`;
- ordinary subtotal before category II and jackpot ≈ **1.16215 AZN per assumed 2-AZN variant** (~58.11%).

Standalone winner-story payouts are not category totals; prior payout/weight U interpretation was corrected.

H014 zero-winner carryover remains testing but manual archive/API routes are exhausted until new tooling/source appears. Kazakhstan 4/20 remains the validated comparator for zero-winner-pool → next-superprize accounting.

# H010 — Poz-Qazan remaining-prize edge
Current-series initial after-tax payout ratios:
- Prestij **69.9060%**
- Meqa 7 **66.8758%**
- Qoşa 2 **66.3051%**
- 4 Fəsil **62.9775%**.

The live remaining-ticket denominator exists institutionally through required sales/inventory tracking, but no public registration-specific counter has been recovered. H010 remains **testing / data-blocked**.

# H015 — crowd-sharing / anti-popularity edge: first magnitude bound complete
Files:
- `data/derived/h015_jackpot_collision_screen_6of59.csv`
- `research/h015_crowd_sharing.md`

Large empirical lottery datasets show that player number choices are strongly non-uniform; human-selected tickets overuse personal/birthday numbers, salient numbers, sequences and visual patterns. This establishes a real sharing mechanism, not a draw-probability effect.

## Exact 6/59 jackpot collision screen
For `M=C(59,6)=45,057,474` and `n` other lines, a combination with crowd-popularity multiplier `a` has exact duplicate probability `q=a/M`. Conditional expected jackpot share is `E[1/(1+X)]` for `X~Binomial(n,q)`.

At **10m other lines**:
- uniform combination: expected jackpot share ≈ **89.68%**;
- 0.2×-popular combination: ≈ **97.81%**, about **+9.07%** to the jackpot component vs uniform;
- theoretical no-duplicate upper bound: **+11.51%** vs uniform;
- 5×-popular combination: ≈ **60.41%**, about **−32.64%** vs uniform;
- 10×-popular: ≈ **40.16%**, about **−55.22%** vs uniform.

Across 5m–15m other lines, perfect uniqueness can improve the jackpot component by only about **+5.65% to +17.57%** versus uniform.

## H015 interpretation
**Anti-popularity is real but not a standalone +EV strategy.** It protects shared-prize value and is especially useful for avoiding severe dilution from crowd-magnet combinations. The upside from perfect uniqueness is bounded because a uniform exact combination already often wins alone.

Best use: **overlay optimizer** on top of an already favorable jackpot/rolldown/promotion state.

The unresolved higher-value piece is lower-tier shared pools, where many competing winners can create a larger sharing effect than exact jackpot duplicates.

# UK Lotto
H016 Wednesday Must Be Won remains **inconclusive/materially weakened** after demand-response stress testing.

# Current priorities
1. **H015 lower-tier shared-pool magnitude** — next bounded packet; quantify whether crowd bias can materially change rolldown-category payout.
2. H010 registration-specific denominator if a new official data route appears.
3. H014 4+4 state accounting when new archive/network tooling appears.
4. Progressive jackpot thresholds / promotional overlays.
5. High-frequency RNG diagnostics only after reliable historical collection.
