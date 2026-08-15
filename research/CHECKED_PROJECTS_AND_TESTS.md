# Checked projects and test variants

Updated: 2026-08-15
Purpose: permanent audit trail. Do not remove failed paths; preserve enough detail to avoid repeating closed work.

Completion criterion:
1. find a reproducible executable **guaranteed positive net-profit** strategy after all costs/outcome branches; OR
2. exhaust the defensible registered edge classes and document why each fails or remains blocked.

Terminal status: **NO SUCCESS; NOT EXHAUSTED**.

## Structural / progressive jackpot work
| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| Cash WinFall | May 9 2011 roll-down reconstruction | ~+10.69% expected ROI before tax/execution | historical +EV mechanism validated; `research/cash_winfall_benchmark.md` |
| UK Lotto 2026 | two-round Must Be Won sampled state | ~£1.53/£2 on July 18 2026 sample | negative sampled state; `research/uk_lotto_regime_2026.md` |
| UK Lotto | Wednesday Must-Be-Won calendar/demand hypothesis | demand uplift usually erodes initial cushion | materially weakened; H016 |
| Kazakhstan 4/20 | zero-winner lower pools feed next superprize | identity reproduced on 3 transitions | validated mechanism; sampled state ~55% / negative; `research/kazakhstan_4x20_control.md` |
| Powerball current | exact fixed lower-tier EV | ~$0.31987825 per $2 play | baseline validated; `research/powerball_progressive_threshold.md` |
| Powerball H002 | no-tax/no-sharing cash break-even | ~$490.934m cash | quantitative threshold established |
| Powerball H002 | sharing curve | threshold ~$512.2m at 25m other lines, ~$579.7m at 100m, ~$785.3m at 300m, ~$1.025bn at 500m | modeled; `src/loto_research/powerball_threshold.py` |
| Powerball H002 | 2026 winner-count participation proxy | sampled ~12.7m–26.5m play scale; observed cash states far below break-even | sampled states negative; `research/h002_powerball_demand_proxy.md` |
| Powerball full-space | all 292,201,338 combinations | cost ~$584.403m; deterministic lower-tier gross ~$93.469m | identity validated |
| Powerball full-space guarantee | external jackpot sharing | no useful hard pre-draw cap on duplicate jackpot winners | **REJECTED terminal guarantee** |
| Mega Millions H002a current $5 format | exact lower-tier EV in fixed-prize jurisdictions | $1.1184749105 per $5 play; expected built-in multiplier 3.0 | quantified; `research/h002a_megamillions_threshold.md` |
| Mega Millions H002a | optimistic no-tax/no-sharing cash break-even | $1,127,475,660 cash | quantified; sampled 2025–2026 cash jackpots checked are far below |
| Mega Millions H002a | sharing curve | ~$1.147bn at 10m other lines; $1.227bn at 50m; $1.333bn at 100m; $1.808bn at 300m | modeled; `data/derived/h002a_megamillions_sharing_threshold_curve.csv` |
| Mega Millions full-space | all 290,472,336 combinations at $5 | cost $1.45236168bn | exact |
| Mega Millions full-space guarantee | worst legal 2x non-jackpot multiplier assignment + jackpot sharing | deterministic non-jackpot floor $216.59068m; sole-jackpot cash needed $1.235771bn; external jackpot-winner count unbounded by useful pre-draw rule | **REJECTED terminal guarantee**; `src/loto_research/megamillions_threshold.py` |
| **EuroMillions H002b current** | current 5/50 + 2/12; €2.50 Spain price; cap €250m | full combination space **139,838,160**, full-space cost **€349,595,400** | quantified; `research/h002b_euromillions_cap_rolldown.md` |
| **EuroMillions H002b terminal cap rolldown** | attempt to buy full space on terminal €250m cap draw | full coverage necessarily contains the realized 5+2 winner, so the required no-jackpot-winner condition for rolldown cannot occur | **REJECTED terminal guarantee by incompatibility theorem** |
| **EuroMillions H002b sharing** | full/partial coverage under shared main-game pools | full coverage costs €99.5954m more than jackpot cap before lower tiers; external winning-bet counts have no useful pre-draw hard cap; partial coverage leaves uncovered outcomes | **REJECTED terminal guarantee**; code `src/loto_research/euromillions_coverage.py` |

## Azerbaijan / finite-space coverage
| Project | Test | Result | Status |
|---|---|---|---|
| Beşdə 5 | exact displayed-table EV | ~53.56% gross | negative |
| Beşdə 5 | buy every 5/36 combination | 376,992 AZN cost vs deterministic gross 201,900 AZN under favorable assumptions | **REJECTED guarantee**; `research/h012_full_space_coverage.md` |
| Super Keno | base EV | ~59.86% gross | negative |
| Super Keno | 1x/2x/5x/10x | proportional stake/prize; larger multiplier slightly worse after tax | no multiplier edge |
| ONLOTO | full-space coverage types 1–10 | deterministic gross ~76.59%–78.00% | **REJECTED guarantee** |
| 4+4 | exact combinatorics | jackpot 1/23,474,025; any listed prize ~18.61% | validated math |
| 4+4 | payout-engine reconstruction | III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U | strongly reproduced |
| 4+4 | zero-winner II–VI carryover | potentially material | testing / data-blocked H014 |
| 4+4 | single 5+5 or 6+6 system | legal 0+0 outcomes exist | **REJECTED guarantee** |
| 4+4 | full-space buy-the-pot | exact theorem needs authoritative pricing + II/carryover + pool response/sharing | BLOCKED |
| Poz-Qazan | sampled initial after-tax EV | ~63–70% | ordinary states negative |
| Poz-Qazan | remaining-prize conditional EV | live registration-specific denominator unavailable | data-blocked H010 |

## Portfolio / systems / promotions
| Class / example | Result | Status |
|---|---|---|
| H012a/H004 additive wheels/partial covering | strict all-outcome positive profit would imply positive EV when all constituent tickets have EV≤0 | **REJECTED under linear assumptions**; `research/h012a_linear_portfolio_impossibility.md` |
| H005 generic system packaging | additive constituent pricing/payout cannot break linear theorem | REJECTED unless genuine nonlinearity |
| Australia Oz Lotto System 8 | 8 games × AUD1.65 = AUD13.20 system price | no discount / REJECTED |
| Poland Lotto systems 7–12 | constituent simple bets; no verified acquisition arbitrage | no nonlinear edge |
| Poland fractional coupons | full underlying ticket paid first, prize split | capital sharing only / REJECTED |
| Poland current 13→12 PLN Quick Pick bundle | real ~7.69% deterministic discount but zero-payout outcome remains | **REJECTED guarantee**, EV discount only |
| Random second chance / extra draw | no-prize branch remains | REJECTED standalone guarantee |
| Nonwithdrawable replay/free-play credit | terminal replay can lose | REJECTED standalone cash guarantee |
| Deterministic cashback filter | guarantee requires payout floor + withdrawable cashback > cost | necessary-condition filter established |
| Georgia Lottery July 2026 deposit match | 50% up to $125, nonwithdrawable/lottery-only; expired by checkpoint | no executable guarantee |
| Azerlotereya current campaign index | no current deterministic subsidy on checkpoint | screened/closed for checkpoint |
| Azerlotereya stale 10-play/10-bonus page | conflicting dates/index; even hypothetical bonus lacks all-outcome proof | stale-conflict / REJECTED current guarantee |
| Virginia new-player bonus games | random bonus games; geofenced; bonus value not guaranteed cash | REJECTED guarantee |
| New York NYL+ | points/second-chance; no deterministic withdrawable cash floor verified | no guarantee candidate |
| Florida Bonus Play | chance-based promotion | REJECTED standalone guarantee |
| Azerbaijan purchase-linked promo lotteries | near-zero marginal entry cost possible if purchase already desired, but no-prize outcome | not guarantee |

## Crowd / sharing
| Test | Result | Status |
|---|---|---|
| Exact jackpot anti-popularity | reduces expected splitting but only conditional on win | validated optimizer, not standalone guarantee |
| Lower-tier shared-pool competitor intensity | can materially improve shared payout if calibrated | mechanism promising / calibration pending |
| Human choice biases: low/birthday, lucky/salient, sequences, visual patterns, representative spacing, form-position | documented in large real-ticket datasets | validated mechanism class |
| Synthetic crowd simulator | implemented conditional competitor-intensity estimation | implementation validated |
| Empirical Dutch anchor | 7/11 over-selected, 37/38 under-selected; visual pattern class ~100× random | sensitivity anchor only |
| Anti-crowd standalone guarantee | losing outcomes remain regardless of sharing optimization | **REJECTED terminal guarantee** |

## Randomness / predictive controls
Permanent rejected standalone ideas unless extraordinary forward evidence appears:
- hot/cold or “due” numbers;
- gambler's fallacy / numerology;
- martingale / staking progression on negative EV;
- in-sample ML;
- number systems that do not alter draw probability or payout sharing;
- blind brute force.

Still open:
- H006 physical-machine/ball bias with strict multiple-testing and regime controls;
- H007 high-frequency RNG anomaly tests with reliable histories and causal implementation subtests.

## Current priorities
1. **H008 cross-jurisdiction** — lawful price/tax/payout differences for the same EuroMillions common jackpot and other shared-jackpot products.
2. H012 finite/final-draw states only where accumulated guaranteed pool/subsidy can break ordinary negative economics.
3. H010/H014 when new authoritative data routes appear.
4. H006/H007 after reliable histories are collected.
5. Advanced controls before EXHAUSTED: Bayesian hidden-state estimation, nonlinear portfolio optimization only where nonlinearity exists, strict out-of-sample ML/RNG tests, lawful lottery-adjacent arbitrage/hedging, additional current products.

## Rule for future work
Every research packet must update this ledger or add a linked detailed note. Detailed hypothesis registry remains `research/HYPOTHESES.md`.
