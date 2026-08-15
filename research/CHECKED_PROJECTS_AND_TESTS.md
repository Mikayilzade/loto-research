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
| Azerbaijan Beşdə 5 | **full-space buy every 5-of-36 combination** | 376,992 AZN cost; deterministic gross 201,900 AZN even assuming full 50k jackpot and ignoring tax/sharing; net -175,092 AZN | **REJECTED as guaranteed-profit coverage** | `research/h012_full_space_coverage.md` |
| Azerbaijan Super Keno | base 1-AZN table EV | ~59.86% gross before tax | rejected as ordinary +EV | `research/azerbaijan_baseline.md` |
| Azerbaijan Super Keno | 1x/2x/5x/10x multiplier economics | proportional stake/payout; after-tax ROI slightly worsens as multiplier rises | no multiplier edge | `research/superkeno_multiplier_economics.md` |
| Azerbaijan ONLOTO | **full-space coverage bet types 1–10** | exact deterministic gross-return range **~76.59%–78.00%** across all ten base types | **REJECTED as guaranteed-profit coverage** | `research/h012_full_space_coverage.md`; `data/derived/h012_full_space_screen.csv` |
| Azerbaijan 4+4 | exact combinatorics | jackpot 1/23,474,025; any listed prize ~18.61% | validated math | `research/4plus4_baseline.md` |
| Azerbaijan 4+4 | draw-level payout-engine reconstruction | III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U | strongly reproduced; multiple out-of-sample rows | `research/4plus4_economics_inference.md` |
| Azerbaijan 4+4 | V/VI hierarchy split | combined 2U reallocated when needed to protect prize order | strong empirical rule | `research/4plus4_economics_inference.md` |
| Azerbaijan 4+4 | zero-winner II–VI carryover | potentially material; adjacent-state proof unavailable | testing/data-blocked | H014; `STATUS.md` |
| Azerbaijan 4+4 | category II ≈20U | suggestive only; winner-story arithmetic alone insufficient | unvalidated | `research/4plus4_category2_lead.md` |
| Azerbaijan 4+4 | **single 5+5 system as guarantee** | contains 25 base variants, but 1,863,225 legal draw pairs are 0+0 relative to selected sets (~7.94%); payout can be zero | **REJECTED as guaranteed-profit path regardless of positive system price** | `research/h012_full_space_coverage.md`; `tests/test_full_space.py` |
| Azerbaijan 4+4 | **single 6+6 system as guarantee** | contains 225 base variants, but 1,002,001 legal draw pairs are 0+0 (~4.27%); payout can be zero | **REJECTED as guaranteed-profit path regardless of positive system price** | `research/h012_full_space_coverage.md`; `tests/test_full_space.py` |
| Azerbaijan 4+4 | **full-space / buy-the-pot** | space = 23,474,025 base variants; exact guarantee theorem needs authoritative per-base/system pricing + II/carryover + pool response/sharing | **BLOCKED; no system-ticket discount evidence found** | `research/h012_full_space_coverage.md` |
| Azerbaijan 4+4 | hidden archive/API search | archive client-rendered; authoritative endpoint not recovered | blocked; do not repeat blind URL guessing | `research/azerlotereya_archive_api_discovery.md` |
| Azerbaijan 4+4 | Telegram result-card archive | official draw cards exist; current tooling cannot fetch Telegram CDN JPEG | blocked by tooling | `STATUS.md` |
| Kazakhstan 4/20 | zero-winner lower-pool -> next superprize transition | exact identity reproduced on 3 independent transitions | validated active mechanism | `research/kazakhstan_4x20_control.md` |
| Kazakhstan 4/20 | sampled-state EV | ~55% return; break-even superprize ~3.395bn KZT vs ~227m | mechanism real, sampled state negative | same note |
| UK Lotto pre-2026 | historical Must Be Won rolldown | July 2025 sampled rolldown still negative | no immediate +EV | UK Lotto research notes |
| UK Lotto 2026 | two-round Must Be Won | July 18 2026 sampled state ~£1.53/£2 | negative sampled state | `research/uk_lotto_regime_2026.md` |
| UK Lotto | Wednesday Must Be Won calendar edge | historical demand uplift usually exceeds break-even cushion | materially weakened | H016 |
| Shared-pool number choice | jackpot collision / unpopular-combination bound | exact-jackpot component can improve, but bounded; not standalone cure | useful optimizer only | `research/h015_crowd_sharing.md` |
| Shared-pool number choice | lower-tier competitor-intensity sensitivity | potentially large payout uplift if crowd intensity can be predictably reduced | mechanism promising; needs target calibration | H015 |
| H015 crowd behavior | birthday / low-number bias | repeatedly documented in large real-ticket datasets | validated mechanism class; target magnitude uncalibrated | `research/h015_crowd_model_framework.md` |
| H015 crowd behavior | lucky/salient/situational numbers | repeatedly documented; number 7 and personally meaningful numbers are common examples | validated mechanism class; target magnitude uncalibrated | same note |
| H015 crowd behavior | numeric sequences / visual patterns | strong over-selection documented | validated mechanism class; target magnitude uncalibrated | same note |
| H015 crowd behavior | representative / evenly-spaced sets | over-selection documented and costly in pari-mutuel games | validated mechanism class; target magnitude uncalibrated | same note |
| H015 crowd behavior | form-position / center / row bias | documented in Dutch/Israeli data | validated mechanism class; target-layout model uncalibrated | same note |
| H015 crowd behavior | jackpot-size changes crowd composition | large-jackpot participation becomes more uniform in Israeli data | validated mechanism class; static anti-crowd estimates can overstate large-jackpot edge | `data/derived/h015_empirical_anchor_summary.csv` |
| H015 crowd simulator | parameterized human-like mixture / softmax generator | implemented; birthday/lucky/center/consecutive/even-spacing features | implementation validated | `src/loto_research/crowd_choice.py` |
| H015 crowd simulator | conditional lower-tier competitor intensity | implemented: simulate draws conditional on our tier hit and estimate competing-ticket tier hits | implementation validated | `tests/test_crowd_choice.py` |
| H015 synthetic screen | popular-looking vs low-score 6/59 line, conditional 3/6 sharing | synthetic mean competitor intensity ~0.414× for low-score line under chosen uncalibrated weights | pipeline works; **not a real edge claim** | `data/derived/h015_synthetic_crowd_screen.csv` |
| H015 empirical anchor | Dutch 6/45 published marginal/pattern frequencies | 7/11 above uniform, 37/38 below; pattern class ~100× random frequency; sparse low-vs-high pair ratio ~0.402 | empirical sensitivity anchor implemented; not target calibration | `src/loto_research/crowd_empirical.py` |
| H015 standalone guarantee | anti-crowd number selection without coverage/overlay | positive-cost ticket still has losing outcomes; sharing optimization cannot remove them | **REJECTED as terminal guaranteed-profit path by necessary-condition proof** | `research/h015_crowd_model_framework.md` |
| Azerbaijan Poz-Qazan | initial-series exact after-tax EV | Prestij ~69.91%; Meqa 7 ~66.88%; Qoşa 2 ~66.31%; 4 Fəsil ~62.98% | ordinary initial states negative | `research/poz_qazan_remaining_prize_edge.md` |
| Azerbaijan Poz-Qazan | remaining-prize conditional EV | denominator exists institutionally but no public live registration-specific count found | testing/data-blocked | H010 |
| Azerbaijan Poz-Qazan | infer inventory from winner carousel | invalid because carousel mixes different registrations/eras | rejected method | H010 note |
| Powerball US 2026 | fixed lower-tier EV + no-sharing/no-tax cash-jackpot break-even floor | lower tiers ~0.31988 USD EV; cash jackpot must exceed ~490.93m USD even before tax/sharing | threshold baseline established; real threshold higher | `research/powerball_progressive_threshold.md` |

## Hypothesis classes not yet fully tested

### Guaranteed-profit / combinatorial constructions — CURRENT PRIORITY
- H012: extend full-space coverage screen to other current finite games / final-draw states. **Beşdə 5 and ONLOTO 1–10 are rejected; single 4+4 5+5/6+6 systems are rejected; 4+4 exact full-space theorem is data-blocked.**
- H012a: partial-space / multi-ticket covering designs with a guaranteed lower-tier floor — **next priority**.
- H012b: real execution limits: printing speed, retailer/network caps, validation/claim logistics, capital lock-up.
- H005: nonlinear portfolio/cap/guarantee effects, especially system-ticket pricing vs constituent variants.
- H005a: own-ticket overlap minimization in shared/rolldown categories.
- H004: covering designs / wheels as risk-profile optimization.
- H004a: guaranteed `t`-match coverage for fixed bankroll.

### Progressive / structural payout states
- H002: full Powerball progressive threshold including tax, sharing and sales response.
- H002a: Mega Millions threshold under current $5 format / multiplier rules.
- H002b: EuroMillions threshold, jackpot cap/rolldown and country-specific tax/claim rules.
- H008: same/shared jackpot cross-jurisdiction differences, especially US vs UK Powerball.
- H009: promotions/cashback/free-ticket/second-chance/loyalty/coupon overlays.

### Crowd / sharing overlay — no longer standalone terminal path
- H015g-calibration: choose a real shared-pool target and fit the crowd model on a training period.
- H015g-validation: out-of-sample marginal-number, combination-feature and winner-count validation.
- H015g-optimizer: search lines that minimize conditional competing-winner intensity, not merely crowd score.
- H015g-EV: feed calibrated intensity into actual pool/share EV when combined with another structural overlay.
- Layout-specific visual-pattern models for target ticket forms.
- Cultural/local lucky-number effects for Azerbaijan / selected target jurisdiction.

### Randomness / implementation
- H006: physical draw bias with multiple-testing controls.
- H006a: ball/machine-set and position bias.
- H006b: change-point detection around machine/ball replacements.
- H007: high-frequency RNG anomaly tests: Ekspres Keno, Şanslı 6, ONLOTO.
- H007a: frequency/chi-square with correction.
- H007b: runs/serial correlation/lags.
- H007c: entropy/compression tests.
- H007d: spectral/periodic tests only where a causal implementation mechanism is plausible.
- H007e: cross-game correlated RNG streams.
- H007f: timestamp/seed dependence if public timing precision permits a falsifiable test.

### Instant tickets
- H010: recover registration-specific remaining-ticket denominator.
- H010b: store/pack-level depletion if lawful observable pack state exists.
- H011: lawful visible pre-purchase information leak.
- H011a: pack sequencing / prize spacing only if official pack rules expose a testable mechanism.

### Advanced methods / controls before EXHAUSTED
- Bayesian latent-state estimation for sales / carryover / hidden crowd intensity.
- Genetic/evolutionary search for nonlinear payout portfolios.
- ML crowd-choice prediction trained on human ticket data/proxies.
- ML winning-number prediction only with reliable histories and strict random out-of-sample baseline.
- Cross-product arbitrage among lawful lottery-adjacent prediction/raffle/promotional markets.
- Syndicate diversification: test ruin/variance effects without confusing them with EV.
- Additional current lotteries and lottery-like products outside the initial catalog.

## Permanent controls / already rejected as standalone edges

- hot/cold numbers;
- “due” numbers / gambler’s fallacy;
- numerology;
- martingale/bet sizing on negative EV;
- ML fitted and tested on the same draws;
- number-picking systems that do not alter probabilities or payout sharing;
- brute-force enumeration where it cannot change the underlying expectation;
- anti-crowd selection alone as a **guaranteed-profit** strategy when losing outcomes remain.

## Rule for future work
Every new research packet must either:
- add a row/result here; or
- update an existing row with stronger evidence/status.

The detailed hypothesis registry remains `research/HYPOTHESES.md`; this file is the human-readable audit ledger requested for later review.
