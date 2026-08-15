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
| **H021 UK Lotto Must-Be-Won full-space subsidy bound** | `C(59,6)` coverage at £2, favorable 50% prize-allocation assumption | full-space spend £90,114,948; minimum guaranteed external subsidy hurdle >£45,057,474 before sharing/costs | **REJECTED current standalone guarantee**; `research/h021_forced_distribution_subsidy_bound.md` |
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
| EuroMillions H002b current | current 5/50 + 2/12; €2.50 Spain price; cap €250m | full combination space **139,838,160**, full-space cost **€349,595,400** | quantified; `research/h002b_euromillions_cap_rolldown.md` |
| EuroMillions H002b terminal cap rolldown | attempt to buy full space on terminal €250m cap draw | full coverage necessarily contains the realized 5+2 winner, so required no-jackpot-winner condition cannot occur | **REJECTED terminal guarantee by incompatibility theorem** |
| EuroMillions H002b sharing | full/partial coverage under shared main-game pools | full coverage costs €99.5954m more than jackpot cap before lower tiers; external winning-bet counts lack useful pre-draw hard cap; partial coverage leaves uncovered outcomes | **REJECTED terminal guarantee**; `src/loto_research/euromillions_coverage.py` |
| EuroMillions H008 cross-jurisdiction | Spain/France/Ireland/UK ticket price, bundled national raffle and tax treatment | material net-ticket differences exist | **EV difference VALIDATED; standalone guaranteed arbitrage REJECTED**; `research/h008_euromillions_cross_jurisdiction.md` |
| **H021 general forced-distribution subsidy bound** | full-space forced payout / final-draw screen | necessary condition `B+E > (1-r)S + costs`; forced payout alone does not erase takeout | **VALIDATED necessary-condition theorem**; `src/loto_research/forced_distribution.py` |
| **H021 Austrian Lotto+LottoPlus 2026 fixed-pool promo** | full 6/45 coverage with required €1.50 Lotto + €0.80 LottoPlus; 48%/45% payout shares; grant entire €1m promo as external subsidy | spend €18,733,638; optimistic own-funded return €8,796,664.80; takeout hurdle €9,936,973.20; after €1m subsidy still -€8,936,973.20 | **REJECTED promotion/full-space guarantee**; `data/derived/h021_forced_distribution_screen.csv` |
| **H022 Irish Lotto 5-4-3-2-1** | buy every k-subset for k=1..5 in both 6-number and 7-number fixed-payout variants | current 47-ball deterministic full-space return only **48.89%–76.60%**; announced 45-ball sensitivity (holding payouts fixed) still max **80%** | **REJECTED guaranteed-profit full coverage**; `research/h022_irish_54321_full_coverage.md` |

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
| Australia Oz Lotto System 8 | no discount | REJECTED |
| Poland Lotto systems 7–12 | constituent simple bets | no nonlinear edge |
| Poland fractional coupons | full underlying ticket paid first, prize split | capital sharing only / REJECTED |
| Poland current 13→12 PLN Quick Pick bundle | real ~7.69% deterministic discount but zero-payout outcome remains | **REJECTED guarantee**, EV discount only |
| Random second chance / extra draw | no-prize branch remains | REJECTED standalone guarantee |
| Nonwithdrawable replay/free-play credit | terminal replay can lose | REJECTED standalone cash guarantee |
| Deterministic cashback filter | guarantee requires payout floor + withdrawable cashback > cost | necessary-condition filter established |
| Georgia Lottery July 2026 deposit match | nonwithdrawable/lottery-only; expired | no executable guarantee |
| Azerlotereya current campaign index | no current deterministic subsidy at checkpoint | screened/closed for checkpoint |
| Virginia new-player bonus games | random bonus games; geofenced; bonus value not guaranteed cash | REJECTED guarantee |
| New York NYL+ | points/second-chance; no deterministic withdrawable cash floor verified | no guarantee candidate |
| Florida Bonus Play | chance-based promotion | REJECTED standalone guarantee |
| H019 capped fixed-prize takeover | buy every valid entry in one-winner capped competition | guarantee requires zero external entries, ability to own all entries, atomic closure, no unresolved free-entry channel, and fixed cash floor > full effective acquisition cost | mechanism valid in principle; no current SUCCESS; `research/h019_capped_fixed_prize_saturation.md` |
| H019 current/recent UK screen | Coast/Hot Comps/7days/Urban Draw/UKCC examples | cash alternative/full-cap revenue only ~28.6%–53.3%; most also have personal caps/free postal routes/external entries | **REJECTED sampled instances**; `data/derived/h019_capped_competition_screen.csv` |

## H020 lawful two-sided hedging / arbitrage
| Venue / structure | Test | Result | Status |
|---|---|---|---|
| Smarkets + bookmaker | back one outcome, lay same outcome, include 2% commission | official examples reproduce equal positive profit once both legs accepted; e.g. back 2.20 £200 / lay 1.98 gives £20 either way | **mechanism VALIDATED; no current live executable quote established**; `research/h020_two_sided_hedging_arbitrage.md` |
| Complete-set dutching | exhaustive mutually exclusive outcomes | strict surebet iff `sum(1/O_i) < 1` after all costs | theorem implemented; `src/loto_research/two_sided_arb.py` |
| Kalshi ordinary binary | buy both Yes and No | combined opposing participant investment `$1`; fees nonnegative | **same-market structural buy-both arb REJECTED** |
| Kalshi collateral return | mutually exclusive/directional linked positions | lowers collateral requirement | capital efficiency only; not payout subsidy |
| Polymarket standard binary | acquire Yes+No and merge | equal pair merges to `$1`; deterministic arb only if all-in pair acquisition cost `< $1` | condition VALIDATED, no structural same-market profit |
| Polymarket negative risk | convert one No into Yes in all other mutually-exclusive outcomes | atomic capital-efficient conversion | not itself a profit subsidy; live mispricing only |
| H020 fee-aware Polymarket gate | include current V2 fee `C*r*p*(1-p)` on both taker legs | near 0.50/0.50 raw pair must be below ~0.985 at r=.03, .980 at .04, .975 at .05, .965 at .07 before extra costs | quantified; `data/derived/h020_fee_aware_pair_thresholds.csv` |
| H020 executable depth | walk both ask books and cap quantity at matched profitable depth | top-of-book `<1` can fail with deeper levels/fees; largest profitable depth solved at book breakpoints | **IMPLEMENTED**; `src/loto_research/live_complete_set.py` |
| Kalshi crossed-book implication | derive market-buy YES+NO from bid-only complement book | complete-set cost `2-(best_yes_bid+best_no_bid)`; sub-$1 requires crossed `yes_bid+no_bid>1` | strengthened structural rejection |
| H020 live API acquisition | current raw Gamma/CLOB books | official public interfaces verified, runtime could not retrieve arbitrary raw live payloads | **DATA/EXECUTION BLOCKED IN CURRENT RUNTIME; scanner ready** |
| H020 terminal gate | current reproducible opportunity | requires all legs fully matched, compatible settlement, net min payout > capital, fees/tax/FX/limits/void risk cleared | **OPEN; post-fill guarantee validated, pre-trade repeatable guarantee not established** |

## Crowd / sharing
| Test | Result | Status |
|---|---|---|
| Exact jackpot anti-popularity | reduces expected splitting but only conditional on win | validated optimizer, not standalone guarantee |
| Lower-tier shared-pool competitor intensity | can materially improve shared payout if calibrated | mechanism promising / calibration pending |
| Human choice biases | documented in large real-ticket datasets | validated mechanism class |
| Synthetic crowd simulator | conditional competitor-intensity estimation implemented | implementation validated |
| Anti-crowd standalone guarantee | losing outcomes remain regardless of sharing optimization | **REJECTED terminal guarantee** |

## H011 visible pre-purchase information
| Channel | Result | Status |
|---|---|---|
| NY exposed scratch-ticket serial | separate credential is under scratch area; no official pre-purchase serial→prize decoder | **REJECTED as validated lawful decoder** |
| Virginia front-barcode scan | purchase first; owned unplayed ticket scan can reveal winner/nonwinner | **POST-PURCHASE only; REJECTED for pre-purchase guarantee** |
| Public scratch remaining-prize tables | game-level prize state, no unsold-ticket identity/location mapping | no deterministic ticket leak; overlaps H010 |
| Pack/ticket number or retailer location | no current official causal mapping to prize; NY material says prizes randomly distributed | no validated current edge |
| Ordinary online instant games | outcome status follows paid play; demo has no cash entitlement | no pre-purchase outcome leak |

## H018 Virginia Lucky Contestant hidden-time state
| Test | Result | Status |
|---|---|---|
| Official causal odds schedule | hidden weighted daily selected time; 60m=1/150,000, 30m=1/30,000, selected time=1/1; jackpot may also be won earlier | **VALIDATED mechanism**; `research/h018_lucky_contestant_time_state.md` |
| Optimistic Bayesian/survival concentration | uniform-within-published-bin + strongest `T>=now` truncation concentrates late remaining-time mass | EV lead only; explicit assumption; `data/derived/h018_optimistic_time_state_screen.csv` |
| $600 jackpot-only threshold | $0.20 stake needs jackpot p≥1/3000; 30m anchor contributes only ~$0.02 jackpot EV, T itself 1/1 but hidden | quantified necessary condition |
| Public winner-list sample | Jan 4–10 2026 page sample contains 8 deduplicated events and two distinct Jan 4 awards | reset/multiple-award mechanics must not be assumed |
| Standalone strict guarantee | other player may legally win jackpot before hidden T; ordinary play has losing outcomes | **REJECTED terminal guarantee** |
| Full EV strategy | exact interpolation, T resolution, standard odds, reset mechanics, stake scaling, live latency/player intensity incomplete | **OPEN/data-blocked overlay**, not SUCCESS |

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

Fresh H007 acquisition recheck on 2026-08-15 still failed to recover a trustworthy machine-readable bulk official history; public Ekspres Keno archive remains client-rendered/placeholder in retrieval. Do not run anomaly tests on incomplete samples.

## Other still-open / blocked classes
- H010 remaining-inventory instant-ticket state: blocked on public live denominator.
- H014 Azerbaijan 4+4 zero-winner carryover: data-blocked.
- H018 Lucky Contestant remains open only as conditional-EV/data-acquisition overlay; standalone guarantee closed.
- additional finite/final-draw games where **guaranteed external subsidy exceeds the H021 takeout hurdle**.
- H020 live executable arbitrage: scanner ready; resume where raw books/settlement can be fetched.
- H019 monitor only when `guaranteed cash floor > full effective capped-entry acquisition cost` or deterministic subsidy changes that inequality.

## Current priorities
1. Apply **H021/H022 fast analytic screens** to additional current finite/final-draw/fixed-payout products; deep-dive only candidates that approach or exceed 100% deterministic coverage return or have external subsidy sufficient to cross the takeout hurdle.
2. H020 live-data arbitrage if direct public raw-book access becomes available.
3. H006/H007 only after reliable histories/machine metadata become available.
4. H010/H014 when new authoritative data routes appear.
5. H018 conditional-EV calibration if exact mechanics/live endpoint become recoverable.
6. Advanced controls before EXHAUSTED: Bayesian hidden-state inference, additional current products.

## Rule for future work
Every research packet must update this ledger or add a linked detailed note. Detailed hypothesis registry remains `research/HYPOTHESES.md`.