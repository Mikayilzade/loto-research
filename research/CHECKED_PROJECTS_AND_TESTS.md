# Checked projects and test variants

Updated: 2026-08-15
Purpose: permanent audit trail of what has been tested, what worked, what failed, and what remains. Do not remove failed paths; append/revise status with evidence.

Completion criterion for the research program:
1. find a reproducible, executable **guaranteed positive net-profit** strategy after all costs and outcome branches; OR
2. exhaust the currently defensible project/edge classes and document why each fails or remains data-blocked.

Terminal status now: **NO SUCCESS; NOT EXHAUSTED**.

## Checked / active projects

| Project / mechanism | Test variant | Result | Status | Main evidence |
|---|---|---|---|---|
| Cash WinFall | historical roll-down, May 9 2011 cash-only EV | +10.69% expected ROI before tax/execution | validated historical +EV mechanism; not current guarantee | `research/cash_winfall_benchmark.md` |
| Azerbaijan Beşdə 5 | exact probability + full displayed prize-table EV | ~53.56% gross return upper-bound | rejected as ordinary +EV | `research/azerbaijan_baseline.md` |
| Azerbaijan Beşdə 5 | full-space buy every 5-of-36 combination | 376,992 AZN cost; deterministic gross 201,900 AZN even assuming full 50k jackpot and ignoring tax/sharing | REJECTED as guaranteed-profit coverage | `research/h012_full_space_coverage.md` |
| Azerbaijan Super Keno | base 1-AZN table EV | ~59.86% gross before tax | rejected as ordinary +EV | `research/azerbaijan_baseline.md` |
| Azerbaijan Super Keno | 1x/2x/5x/10x multiplier economics | proportional stake/payout; after-tax ROI slightly worsens as multiplier rises | no multiplier edge | `research/superkeno_multiplier_economics.md` |
| Azerbaijan ONLOTO | full-space coverage bet types 1–10 | exact deterministic gross-return range ~76.59%–78.00% | REJECTED as guaranteed-profit coverage | `research/h012_full_space_coverage.md` |
| H012a/H004 generic linear theorem | arbitrary additive wheel/partial covering/multi-ticket portfolio with EV≤0 tickets | strict all-outcome positive profit would imply positive EV, contradiction | REJECTED guarantee class under linear assumptions | `research/h012a_linear_portfolio_impossibility.md` |
| H005 generic system packaging | system/bundle merely aggregates constituent variants at additive price/payout | does not break linear theorem | REJECTED unless genuine price/payout nonlinearity exists | `research/h005_nonlinear_overlay_screen.md` |
| H005 random extra prize layer | second-chance/promotional draw with legal zero-prize outcome | cannot repair negative base floor in every outcome | REJECTED as standalone guarantee | same note |
| H005 nonwithdrawable free-play credit | bonus/rebate must be replayed and replay can lose | guaranteed cash value can be zero | REJECTED as standalone cash guarantee absent coverage | same note |
| H005 deterministic cashback filter | base cost C, floor F, withdrawable cashback B | guarantee requires F+B>C after all costs | necessary-condition filter established | same note |
| Lotto.com promotion archetype | first-order all-losing second chance, non-payable credit capped at $10 | state-dependent subsidy but terminal replay can lose; winning-but-subcost branch may receive no credit | REJECTED as guaranteed cash-profit offer | same note |
| Georgia Lottery July 2026 deposit match | 50% bonus up to $125 for never-deposit users, lottery-only/nonwithdrawable | real subsidy but expired by 2026-08-15 and no guaranteed cash conversion | not executable / no guarantee | same note |
| Azerbaijan promotional lotteries | Kia Qızıl Açar / ABB Şanslı Fərdi Sahibkar | entries may have near-zero marginal cost if underlying purchase/action already desired, but no-prize outcome remains | positive incremental EV possible; not guarantee | same note |
| Azerbaijan 4+4 | exact combinatorics | jackpot 1/23,474,025; any listed prize ~18.61% | validated math | `research/4plus4_baseline.md` |
| Azerbaijan 4+4 | draw-level payout-engine reconstruction | III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U | strongly reproduced | `research/4plus4_economics_inference.md` |
| Azerbaijan 4+4 | zero-winner II–VI carryover | potentially material; adjacent-state proof unavailable | testing/data-blocked | H014 |
| Azerbaijan 4+4 | single 5+5 system guarantee | legal 0+0 draw outcomes exist | REJECTED | `research/h012_full_space_coverage.md` |
| Azerbaijan 4+4 | single 6+6 system guarantee | legal 0+0 draw outcomes exist | REJECTED | same note |
| Azerbaijan 4+4 | full-space / buy-the-pot | exact theorem needs authoritative pricing + II/carryover + pool response/sharing | BLOCKED | same note |
| Kazakhstan 4/20 | zero-winner lower-pool -> next superprize transition | exact identity reproduced on 3 transitions | validated active mechanism | `research/kazakhstan_4x20_control.md` |
| Kazakhstan 4/20 | sampled-state EV | ~55% return; break-even superprize ~3.395bn KZT vs ~227m | sampled state negative | same note |
| UK Lotto 2026 | two-round Must Be Won | July 18 2026 sampled state ~£1.53/£2 | negative sampled state | `research/uk_lotto_regime_2026.md` |
| UK Lotto | Wednesday Must Be Won calendar edge | demand uplift usually exceeds break-even cushion | materially weakened | H016 |
| H015 anti-crowd standalone | unpopular selection without coverage/overlay | losing outcomes remain | REJECTED guarantee path | `research/h015_crowd_model_framework.md` |
| H015 crowd-sharing | lower-tier competitor-intensity optimization | potentially useful when layered on structural +EV state | validated mechanism / target calibration pending | H015 notes |
| Azerbaijan Poz-Qazan | initial-series after-tax EV | sampled games ~63–70% | ordinary initial states negative | `research/poz_qazan_remaining_prize_edge.md` |
| Azerbaijan Poz-Qazan | remaining-prize conditional EV | live registration-specific denominator unavailable | data-blocked | H010 |
| Powerball US 2026 | fixed lower-tier EV + optimistic cash-jackpot break-even floor | cash jackpot >~490.934m USD even before tax/sharing | threshold baseline | `research/powerball_progressive_threshold.md` |

## Hypothesis classes not yet fully tested

### Current priority
- H009: current deterministic promotions/subsidies/cashback/free-play; apply H005 filters before portfolio optimization.
- H005: jurisdiction-specific genuine system-ticket discounts, payout caps/floors and nonlinear shared-pool rules.
- H012: finite/final-draw states only where accumulated pool/subsidy breaks ordinary negative economics.
- H012b: execution limits for any candidate that survives economics.

### Progressive / structural payout states
- H002: full Powerball threshold including tax, sharing and sales response.
- H002a: Mega Millions current $5 format.
- H002b: EuroMillions jackpot cap/rolldown and country-specific tax/claim rules.
- H008: cross-jurisdiction differences.

### Randomness / implementation
- H006: physical draw bias with multiple-testing controls.
- H007: high-frequency RNG anomaly tests and causal implementation subtests.

### Instant tickets
- H010: registration-specific remaining-ticket denominator.
- H010b: lawful observable pack-state depletion.
- H011: lawful visible pre-purchase information leak / official pack sequencing only.

### Advanced controls before EXHAUSTED
- Bayesian latent-state estimation for hidden sales/carryover/crowd intensity.
- Genetic/evolutionary search only for nonlinear payout portfolios.
- ML crowd prediction and strictly out-of-sample RNG tests.
- Cross-product lawful lottery-adjacent arbitrage/hedging.
- Additional current lotteries and lottery-like products outside initial catalog.

## Permanent controls / rejected standalone edges
- hot/cold or due numbers; numerology; martingale;
- in-sample ML;
- number systems that do not alter probabilities/sharing;
- blind brute force;
- anti-crowd selection alone;
- ordinary additive wheels/coverings;
- random promotional entry alone;
- nonwithdrawable free-play face value treated as cash.

## Rule for future work
Every new research packet must add/update this ledger. Detailed hypothesis registry remains `research/HYPOTHESES.md`.
