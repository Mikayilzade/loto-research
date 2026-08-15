# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## Work-session rule
Research runs in short packets. After every meaningful discovery or roughly 2–4 substeps:
1. save raw/derived data;
2. update the relevant research note;
3. update this file when the strategic conclusion changes.

This file is the authoritative handoff checkpoint. Read `START_HERE.md`, `PROJECT_RULES.md`, `RESEARCH_PLAN.md` and `AGENTS.md` before code work.

## Permanent audit ledger
User-requested master list of checked projects, test variants, failures, blockers and remaining classes:
- `research/CHECKED_PROJECTS_AND_TESTS.md`

Every future packet must update that ledger or add a new checked path.

# Validated structural benchmark
## Cash WinFall
Historical 2011 roll-down benchmark:
- ticket $2;
- expected payout **$2.2137120403**;
- expected ROI **+10.6856%** before tax/execution.

Structural +EV has existed without predicting numbers.

# Azerbaijan baseline games
## Beşdə 5
- jackpot odds **1 in 376,992**;
- favorable gross baseline **0.535555131 AZN / 1-AZN variant**;
- net before tax/sharing about **-46.44%**.

## Super Keno — multiplier mechanics resolved
Files:
- `data/derived/az_superkeno_multiplier_ev.csv`
- `research/superkeno_multiplier_economics.md`

One variant supports 1x/2x/5x/10x payment and proportional prize scaling. The advertised 1m maximum is the 10x version of the 100k base tier, not a free overlay.

Gross payout ratio is invariant **59.8556%**. Favorable after-tax ratios:
- 1x **59.1807%**
- 2x **59.1266%**
- 5x **58.9036%**
- 10x **58.6982%**.

Conclusion: **no multiplier EV edge; 1x is best on after-tax ROI absent promotion**.

# Azerbaijan 4+4 — top local draw-game target, data-blocked for next state transition
Strong empirical draw-table engine:
- III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U;
- draw #790 and #781 independently confirm structure;
- eight samples: mean `U/N_hat≈0.01000654`, median `≈0.00995289`;
- ordinary subtotal before II/jackpot ≈ **1.16215 AZN per assumed 2-AZN variant** (~58.11%).

H014 zero-winner carryover remains testing; manual archive/API routes are exhausted until new tooling/source appears. Kazakhstan 4/20 remains the validated comparator for zero-winner-pool → next-superprize accounting.

# H010 — Poz-Qazan remaining-prize edge
Current initial after-tax payout ratios:
- Prestij **69.9060%**
- Meqa 7 **66.8758%**
- Qoşa 2 **66.3051%**
- 4 Fəsil **62.9775%**.

The live remaining-ticket denominator exists institutionally through required sales/inventory tracking, but no public registration-specific counter has been recovered. H010 remains **testing / data-blocked**.

# H015 — crowd-sharing / anti-popularity edge: two magnitude screens complete
Files:
- `data/derived/h015_jackpot_collision_screen_6of59.csv`
- `data/derived/h015_shared_pool_intensity_sensitivity.csv`
- `research/h015_crowd_sharing.md`

Empirical lottery-entry research shows strong non-uniform player choice. In one large 6/45 dataset, diagonal/vertical patterns were about **0.9% of actual entries vs 0.009% under random choice**, and many exact popular combinations appeared hundreds of times.

## Exact jackpot collision result
At 10m other 6/59 lines:
- uniform combination: expected conditional jackpot share ≈ **89.68%**;
- 0.2×-popular: ≈ **97.81%**, +9.07% to jackpot component vs uniform;
- no-duplicate theoretical upper bound: +11.51%;
- 5×-popular: ≈ **60.41%**, −32.64%;
- 10×-popular: ≈ **40.16%**, −55.22%.

Across 5m–15m lines, perfect uniqueness improves only the jackpot component by about **+5.65% to +17.57%** vs uniform. Exact-combination anti-popularity is useful protection, not standalone +EV.

## Lower-tier shared-pool sensitivity
For a shared category, let `lambda` be expected **other** winners conditional on our hit. With Poisson competitor count:

`E[share] = (1-exp(-lambda))/lambda`.

For categories with many competitors, payout is approximately inverse to competitor intensity. Generic sensitivity:
- 0.8× expected competitors -> **~1.25× category payout**;
- 0.6× -> **~1.667×**;
- 0.5× -> **~2.0×**;
- 1.2× -> ~0.833×;
- 1.5× -> ~0.667×;
- 2× -> ~0.5×.

Thus lower-tier crowd optimization can have substantially larger percentage impact than exact jackpot anti-duplication **if** a pre-draw ticket construction can reliably reduce competitor intensity.

## H015 scientific bottleneck
The mechanism and sensitivity are clear. Missing piece:
- a crowd-choice model mapping our chosen line to expected competing-winner count in a target lower tier.

Do **not** promote simplistic rules such as “take high numbers” to EV claims. Need calibrated human-like vs random vs anti-crowd generator, then conditional simulations / out-of-sample validation.

H015 status: **quantitatively promising as an overlay optimizer; not standalone +EV**.

# H002 — Powerball progressive threshold: first hard floor
File:
- `research/powerball_progressive_threshold.md`

Current US structure: $2 play, jackpot odds **1 in 292,201,338**, fixed lower tiers outside California.

Exact fixed lower-tier EV from official current prize/odds chart:
- **~$0.31987825 per $2 play**.

Therefore, under deliberately favorable assumptions of **zero tax, zero sharing and full cash receipt**, the cash jackpot must exceed approximately:
- **$490.934m cash value**

just to reach break-even.

This is an optimistic floor. Real break-even is higher once jackpot sharing, tax, sales response, jurisdiction and execution are modeled.

Captured official July-29-2026 state ($663m advertised / $290.4m cash) was far below this floor, hence negative even before tax/sharing.

H002 status: **testing; Powerball optimistic cash threshold baseline established**.

# UK Lotto
H016 Wednesday Must Be Won remains **inconclusive/materially weakened** after demand-response stress testing.

# Safe next priorities
1. Extend **H002** into real Powerball threshold curve with tax + sharing + sales response; then Mega Millions / EuroMillions.
2. Build the **H015 crowd-choice simulation framework** using parameterized human-bias inputs; keep calibration assumptions explicit.
3. H010 registration-specific denominator if a new official data route appears.
4. H014 4+4 state accounting when new archive/network tooling appears.
5. H004/H005/H006/H007/H008/H009/H011/H012 and additional games from the master ledger.
6. High-frequency RNG diagnostics only after reliable historical collection.
