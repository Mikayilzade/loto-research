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
Files now include:
- `src/loto_research/crowd_choice.py`
- `src/loto_research/crowd_empirical.py`
- `tests/test_crowd_choice.py`
- `tests/test_crowd_empirical.py`
- `data/derived/h015_empirical_anchor_summary.csv`
- `data/derived/h015_synthetic_crowd_screen.csv`
- `research/h015_crowd_sharing.md`
- `research/h015_crowd_model_framework.md`

## Published-anchor calibration added
Dutch 6/45 empirical anchors:
- 11 = 16.5% vs uniform 13.333% => **1.2375×**;
- 7 = 16.3% => **1.2225×**;
- 37 = 10.3% => **0.7725×**;
- 38 = 10.5% => **0.7875×**;
- diagonal/vertical pattern class 0.9% actual vs 0.009% random => **~100× overrepresentation**.

Sparse independent sensitivity anchor:
`weight(37,38) / weight(7,11) ≈ 0.402119353` with four other positions held neutral.

Israeli 6/37 data independently confirms persistent crowd bias across 118 draws and also shows **bias attenuation toward uniform as jackpots/participation grow**. Static anti-crowd models therefore risk overstating benefit in the largest-jackpot states.

## H015 terminal result
Anti-crowd choice changes sharing conditional on a win; it does not remove losing draw outcomes. Therefore, with positive ticket cost and any zero-return outcome remaining, **anti-crowd selection alone cannot guarantee positive profit across all outcomes**.

H015 status:
- mechanism / EV overlay: **VALIDATED-MECHANISM, calibration still useful**;
- standalone guaranteed-profit path: **REJECTED by necessary-condition proof**.

This branch can return later only as an optimizer layered on top of H012/H005/H001-like structural states.

# H002 — Powerball progressive threshold
Current baseline already established in repo:
- fixed lower-tier EV ≈ **$0.31987825 per $2 play**;
- even under zero tax, zero sharing and full cash receipt, cash jackpot must exceed approximately **$490.934m** just to break even.

Real threshold will be higher after sharing, tax, sales response and execution. H002 remains **testing**.

# UK Lotto
H016 Wednesday Must Be Won remains **inconclusive/materially weakened** after demand-response stress testing.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` is the user-requested master list of checked games/projects, test variants, failures, blockers and remaining branches. Every future packet must add/update it.

# Safe next priorities
1. **H012 full-space coverage / buy-the-pot**: highest-priority branch because it can in principle satisfy the user's guaranteed-profit terminal criterion.
2. H012a/H004: partial covering / integer-programmed guaranteed payout floors.
3. H005: nonlinear portfolio/cap/guarantee interactions.
4. H002/H009: progressive and promotional overlays that could make coverage profitable.
5. H015: return only as sharing optimizer if another branch approaches break-even/guaranteed coverage.
6. H014/H010 when new data routes appear.
7. H006/H007 physical/RNG anomaly branches after reliable histories are collected.
