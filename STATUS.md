# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## GO-mode
User message `го` means: continue the next highest-value research packet without clarification. Chat output stays minimal. After each meaningful packet:
1. save raw/derived data and/or code;
2. update the relevant research note;
3. update `research/CHECKED_PROJECTS_AND_TESTS.md`;
4. update this file when the strategic conclusion changes.

This file is the authoritative handoff checkpoint. Read `START_HERE.md`, `PROJECT_RULES.md`, `RESEARCH_PLAN.md`, `AGENTS.md` and `research/CHECKED_PROJECTS_AND_TESTS.md` before work.

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# Validated structural benchmark
## Cash WinFall
Historical 2011 roll-down benchmark:
- ticket $2;
- expected payout **$2.2137120403**;
- expected ROI **+10.6856%** before tax/execution.

Structural +EV has existed without predicting numbers, but this is not a current guaranteed-profit strategy.

# Azerbaijan baseline games
## Beşdə 5
- jackpot odds **1 in 376,992**;
- favorable gross baseline **0.535555131 AZN / 1-AZN variant**;
- net before tax/sharing about **-46.44%**.

## Super Keno — multiplier mechanics resolved
Files:
- `data/derived/az_superkeno_multiplier_ev.csv`
- `research/superkeno_multiplier_economics.md`

Gross payout ratio is invariant **59.8556%** across 1x/2x/5x/10x scaling. Favorable after-tax ratios fall slightly as multiplier rises. Conclusion: **no multiplier EV edge**.

# Azerbaijan 4+4 — top local state-dependent target, data-blocked
Strong empirical draw-table engine:
- III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U;
- draw #790 and #781 independently confirm structure;
- eight samples: mean `U/N_hat≈0.01000654`, median `≈0.00995289`;
- ordinary subtotal before II/jackpot ≈ **1.16215 AZN per assumed 2-AZN variant** (~58.11%).

H014 zero-winner carryover remains testing. Hidden archive/API and Telegram-card routes are currently blocked with available tooling. Kazakhstan 4/20 remains the validated comparator for zero-winner-pool → next-superprize accounting.

# H010 — Poz-Qazan remaining-prize edge
Initial sampled after-tax payout ratios remain ~63–70%, all negative. Registration-specific remaining-ticket denominator is not publicly recovered. Status: **testing / data-blocked**.

# H015 — crowd-sharing / anti-popularity edge
Files:
- `src/loto_research/crowd_choice.py`
- `tests/test_crowd_choice.py`
- `data/derived/h015_jackpot_collision_screen_6of59.csv`
- `data/derived/h015_shared_pool_intensity_sensitivity.csv`
- `data/derived/h015_synthetic_crowd_screen.csv`
- `research/h015_crowd_sharing.md`
- `research/h015_crowd_model_framework.md`

## Mechanism evidence
Large empirical ticket datasets support persistent non-uniform human selection including:
- low/birthday-number preference;
- lucky/salient/situational numbers;
- numeric sequences and visual patterns;
- representative/even-spacing preference;
- form-position / center / row bias;
- crowd composition changing toward more uniform selection as jackpots attract occasional players.

Exact-jackpot anti-popularity remains a bounded optimizer only. Lower-tier shared-pool competitor intensity is the more promising channel.

## NEW — crowd-choice framework implemented
`crowd_choice.py` provides:
- behavioral line scoring;
- biased crowd-line generation without full-space enumeration;
- draw simulation conditional on our line hitting a selected tier;
- competing-ticket tier-hit estimation with Monte Carlo standard error;
- anti-crowd candidate generation.

Local framework validation: **5/5 tests passed**.

Synthetic pipeline demonstration (not calibrated real EV):
- high-score 6/59 line `3 7 12 18 24 30`;
- low-score candidate `36 40 48 51 56 58`;
- condition: our line hits 3/6; estimate crowd competitor also hitting 3/6;
- 10 seeds × 10,000 simulations;
- mean high-score competitor probability ≈ **0.01664**;
- mean low-score competitor probability ≈ **0.00682**;
- mean relative intensity ≈ **0.414**.

Interpretation: simulator can express economically meaningful sharing differences, but weights were synthetic. **No real 0.414× edge is claimed.**

## H015 bottleneck now
The simulator is no longer the blocker. Need a **real target-game crowd calibration/proxy**:
1. pick a shared lower-tier target;
2. fit number/combination biases on training data/proxies;
3. validate out-of-sample;
4. estimate candidate-specific conditional competitor intensity;
5. combine with real sales/pool rules and structural EV.

Status: **mechanism validated; framework implemented; calibrated real edge not yet validated**.

# H002 — Powerball progressive threshold
File: `research/powerball_progressive_threshold.md`.

Current baseline already established in repo:
- fixed lower-tier EV ≈ **$0.31987825 per $2 play**;
- even under zero tax, zero sharing and full cash receipt, cash jackpot must exceed approximately **$490.934m** just to break even.

Real threshold will be higher after sharing, tax, sales response and execution. H002 remains **testing**.

# UK Lotto
H016 Wednesday Must Be Won remains **inconclusive/materially weakened** after demand-response stress testing.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` is the user-requested master list of checked games/projects, test variants, failures, blockers and remaining branches. Every future packet must add/update it.

# Safe next priorities
1. H015g: identify a **calibratable real shared-pool target / crowd-data proxy**; fit and out-of-sample validate the crowd model.
2. H002: extend Powerball into real tax+sharing+sales-response threshold; then Mega Millions / EuroMillions.
3. H014: exact 4+4 state accounting when a new data route/tool appears.
4. H010: registration-specific remaining-ticket denominator if a new official route appears.
5. H004/H005/H012 combinatorial/full-space/portfolio branches.
6. H006/H007 physical/RNG anomaly branches only after reliable histories are collected.
