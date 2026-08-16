# Checked projects and test variants

Updated: 2026-08-16
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
| **H023 UK Set For Life full-space** | buy every 5/47 + Life Ball/10 line at £1.50; value headline annuity at undiscounted nominal £3.6m | 15,339,390 lines; cost £23,009,085; deterministic nominal gross **£12,949,100 = 56.2782%**; top-prize cap can only worsen strict floor | **REJECTED guaranteed-profit full coverage**; `research/h023_uk_fixed_prize_full_coverage.md` |
| **H023 UK Thunderball full-space** | buy every 5/39 + Thunderball/14 line at £1 | 8,060,598 lines; deterministic gross **£4,262,568 = 52.8815%** | **REJECTED guaranteed-profit full coverage**; `research/h023_uk_fixed_prize_full_coverage.md` |
| **H024 UK Lotto HotPicks** | buy every k-subset for Pick 1–5 | deterministic return **41.95%–61.02%** | **REJECTED guaranteed-profit full coverage**; `research/h024_hotpick_daily_million_full_coverage.md` |
| **H024 UK EuroMillions HotPicks** | buy every k-subset for Pick 1–5 | deterministic return **31.46%–66.67%** | **REJECTED guaranteed-profit full coverage**; `research/h024_hotpick_daily_million_full_coverage.md` |
| **H024 Irish Daily Million** | buy all `C(39,6)=3,262,623` lines; grant our top line the full €1m despite sharing possibility | optimistic deterministic gross €1,786,800 = **54.7658%**; guaranteed pre-execution loss €1,475,823 | **REJECTED guaranteed-profit full coverage**; `research/h024_hotpick_daily_million_full_coverage.md` |
| **H025 Health Lottery Big Win + free £100k draw** | buy all `C(50,5)` Wednesday/Saturday lines; grant full £25k Match-5, value 198,660 free tickets at £1 face, grant full £100k auxiliary draw | cost £2,118,760; deliberately optimistic deterministic package value **£603,560 = 28.4865%** | **REJECTED guaranteed-profit full coverage**; `research/h025_health_lottery_full_coverage.md` |
| **H025 Health Lottery All Or Nothing** | buy all `C(24,12)` lines; grant both 12-match and 0-match own winners full £25k each despite sharing rule | cost £2,704,156; optimistic deterministic gross **£1,071,850 = 39.6371%** | **REJECTED guaranteed-profit full coverage**; `research/h025_health_lottery_full_coverage.md` |
| **H026 Millionaire for Life** | buy all `C(58,5)*5=22,910,580` plays at $5; grant full current $18m top cash and $2.2m to each of four 5-only winners, ignoring pari-mutuel deterioration | cost **$114,552,900**; optimistic deterministic gross **$60,584,320 = 52.8876%**; deficit $53,968,580 | **REJECTED guaranteed-profit full coverage**; `research/h026_millionaire_for_life_full_coverage.md` |
| **H027 Lotto America** | buy all `C(52,5)*10=25,989,600` $1 plays; exact published-table non-jackpot gross $6,991,428; July 18 2026 $34.12m annuity had $15,154,248 cash option | optimistic full-share cash gross **$22,145,676 = 85.2098%**, deficit $3,843,924; sole-winner cash hurdle $18,998,172; jackpot sharing/lower-tier pari-mutuel can only worsen guarantee | **REJECTED guaranteed-profit full coverage**; `research/h027_lotto_america_full_coverage.md` |
| **H028 Nebraska 2by2** | buy all `C(26,2)^2=105,625` plays; also test required seven-draw package with free Double Tuesday | normal optimistic terminal cash **$40,168 = 38.0289%**; 7-draw package **$321,344/$739,375 = 43.4616%** | **REJECTED guaranteed-profit full coverage**; top/set-prize liability reductions ignored in player's favor; `research/h028_nebraska_finite_coverage.md` |
| **H028 Nebraska MyDaY** | buy every valid MM-DD-YY calendar combination | 36,525 plays; exact all-state gross range **$17,580–$21,357 = 48.1314%–58.4723%** | **REJECTED guaranteed-profit full coverage**; `research/h028_nebraska_finite_coverage.md` |
| **H028 Nebraska Pick 5** | buy all `C(40,5)=658,008` plays; full published 4/5 and 3/5 cash tiers | deterministic non-jackpot cash **$141,050 = 21.4359%**; sole-winner jackpot hurdle **$516,958**; jackpot sharing and possible lower-tier pari-mutuel remain | **REJECTED current guaranteed-profit full coverage**; `research/h028_nebraska_finite_coverage.md` |
| **H029 Virginia fixed digit base games** | Pick 3 / Pick 4 / Pick 5 Exact, Any, 50/50, Combo/Pair menus under additive base rules | every checked base wager has gross EV only **48%–50%** (Pick 5 50/50 30-way 49.75%); full Exact coverage returns exactly 50%; any strict all-outcome positive portfolio would contradict expectation linearity | **REJECTED entire base-game additive guarantee class**; `research/h029_fixed_digit_games_impossibility.md`, `data/derived/h029_virginia_digit_base_ev.csv` |
| **H031 Georgia/Virginia Cash Pop Cover All** | buy all 15 numbers at $1/$2/$5/$10; operator explicitly guarantees a prize | full cost `15w`; legal minimum draw prize `5w`; strict gross floor **33.3333%** | **REJECTED guaranteed-profit coverage**; `research/h031_cash_pop_cover_all.md` |
| **H032 Canada DAILY GRAND** | buy every `C(49,5)*7=13,348,188` line at CAD 3 | favorable no-external-winner + Free-Play-face gross **44.3472%**; strict immediate-cash floor **36.2112%** | **REJECTED guaranteed-profit full coverage**; `research/h032_canada_daily_grand_compact_screen.md` |
| **H033 New Zealand Bullseye** | statutory 7/14-draw discount while owning all 1,000,000 selections | discount **28.5714%**, but divisions remain shared/capped and replay-based | **DISCOUNT VALIDATED, strict guarantee REJECTED**; `research/h033_nz_bullseye_discounted_coverage.md` |
| **H034 Ontario DAILY KENO Pick 2–10** | exact full-space identity under current fixed prize table | favorable uncapped full-space/EV return only **42.03%–55.07%** | **REJECTED additive/coverage guarantee class**; `research/h034_ontario_daily_keno_full_coverage.md` |
| **H035 Lotterywest Super66** | hypothetical unique cover all 1,000,000 six-digit strings | deterministic minimum-payout gross **54.3481%**; unique coverage not forceable | **REJECTED**; `research/h035_lotterywest_compact_games.md` |
| **H035 Lotterywest Cash 3** | exact partition cover all ordered outcomes | strict minimum gross **36.3636%** | **REJECTED**; same note |
| **H036 Irish Daily Million Plus** | full Plus-line coverage | optimistic gross **29.4732%**, strict non-top floor **14.1481%** | **REJECTED**; `research/h036_irish_plus_and_olg_targeted_bonus.md` |
| **H036 Irish EuroMillions Plus** | full Plus-line coverage | optimistic full-top gross **54.1826%**, non-top fixed cash **30.5839%** | **REJECTED**; same note |

## Azerbaijan / finite-space coverage
| Project | Test | Result | Status |
|---|---|---|---|
| Beşdə 5 | exact displayed-table EV | ~53.56% gross | negative |
| Beşdə 5 | buy every 5/36 combination | 376,992 AZN cost vs deterministic gross 201,900 AZN | **REJECTED guarantee**; `research/h012_full_space_coverage.md` |
| Super Keno | base EV | ~59.86% gross | negative |
| Super Keno | 1x/2x/5x/10x | proportional stake/prize | no multiplier edge |
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
| **H036 OLG targeted LOTTO MAX buy-6-get-6 bonus** | 100% face-value subsidy at minimum spend but lottery-only value | **REJECTED standalone cash guarantee**; `research/h036_irish_plus_and_olg_targeted_bonus.md` |
| **H036 OLG targeted LOTTO 6/49 buy-3-get-3 bonus** | 100% face-value subsidy at minimum spend but non-cash conversion risk | **REJECTED standalone cash guarantee**; same note |
| **H036 OLG targeted LOTTO MAX buy-18-get-6 bonus** | 33.33% face-value subsidy; targeted/capped/non-cash | **REJECTED standalone guarantee**; same note |
| **H036 OLG birthday lottery bonus** | zero acquisition cost lottery-only bonus | targeted EV overlay, not guaranteed cash |
| **H037 Irish Lotto Plus Million Euro Raffle** | six special-event counts `73,104,81,82,84,72`; break-even ≈170 raffle winners; matched adjacent promotion uplift mean **1.3766x**; every event's 95% upper implied participation remains below break-even | **STRONG LIVE +EV OVERLAY; STRICT GUARANTEE REJECTED** because raffle code/final €1m selection remain random and external tickets exist; Gamma-Poisson posterior mean 82.75, model-conditional predictive `P(K>=170)≈1.7e-14`; `research/h037_lotto_plus_million_raffle.md`, `data/derived/h037_event_calibration.csv` |
| **H038 deterministic rebate / free-credit theorem** | cash spend `S`, minimum cash payout `m`, guaranteed cash rebate `R`, costs `C` | strict guarantee requires `m+R>S+C`; lottery-only credit keeps zero floor if downstream play can lose | theorem VALIDATED; sampled OLG/Virginia-style credits rejected as strict cash guarantees |
| **H039 Betfair Azerbaijan EXCN10 cash refund** | first Exchange bet risks €10; losing qualifying bet refunded €10 in cash; mechanical same-odds hedge has positive all-outcome floor | **MECHANICAL ARBITRAGE VALIDATED; STRICT GUARANTEE REJECTED** because incorporated Standard Promotional Terms allow invalidation/withholding when play guarantees profit with no/minimal risk; `research/h039_cash_refund_matched_betting_gate.md` |
| H039 general cash-refund matched-promo theorem | with full cash refund `R=S`, choose opposing lay `L=S-delta`; then win branch `delta(O-1)>0`, loss branch `S-delta>0` before costs | **VALIDATED constructive theorem**; future SUCCESS requires no anti-arbitrage clawback plus irrevocably matched compatible hedge legs |
| **H040 selective cash-refund theorem** | cash refunded only for a subset of losing states while at least one non-refunded losing state remains | **REJECTED as promo-created surebet**: strict positive floor requires an ordinary bookmaker/exchange price arbitrage even before refund; `research/h040_cash_refund_operator_scan.md`, `src/loto_research/promo_hedge.py` |
| **H040 operator contract screen** | bet365, Paddy Power, Sky Bet, BetVictor, BetMGM, FanDuel | true cash offers either retain anti-guaranteed-profit/abuse discretion or cover only selected loss states; several others pay nonwithdrawable free/bonus bets | **NO CURRENT TERMINAL CANDIDATE**; `data/derived/h040_cash_refund_contract_screen.csv` |
| H019 capped fixed-prize takeover | guarantee requires zero external entries, ability to own all entries, atomic closure, no free-entry channel, and fixed cash floor > acquisition cost | mechanism valid in principle; no current SUCCESS; `research/h019_capped_fixed_prize_saturation.md` |
| H019 current/recent UK screen | sampled full-cap economics ~28.6%–53.3% | **REJECTED sampled instances** |

## H020 lawful two-sided hedging / arbitrage
| Venue / structure | Test | Result | Status |
|---|---|---|---|
| Smarkets + bookmaker | post-fill back/lay equal-profit construction | official examples validate surebet after both legs accepted | **mechanism VALIDATED; no current live executable quote established** |
| Complete-set dutching | exhaustive mutually exclusive outcomes | strict surebet iff `sum(1/O_i) < 1` after costs | theorem implemented |
| Kalshi ordinary binary | buy both Yes and No | combined opposing investment $1; fees nonnegative | **same-market structural buy-both arb REJECTED** |
| Polymarket standard binary | acquire Yes+No and merge | deterministic arb only if all-in pair acquisition cost `< $1` | condition validated, no structural same-market profit |
| H020 fee-aware / executable depth | fee-aware thresholds + depth walk | scanner implemented | raw live-book acquisition blocked in current runtime |
| H020 terminal gate | fully matched compatible settlement with net min payout > capital | **OPEN; post-fill guarantee validated, pre-trade repeatable guarantee not established** |

## Crowd / sharing
| Test | Result | Status |
|---|---|---|
| Exact jackpot anti-popularity | reduces expected splitting but only conditional on win | validated optimizer, not standalone guarantee |
| Lower-tier shared-pool competitor intensity | can materially improve shared payout if calibrated | promising overlay |
| Human choice biases | documented in large ticket datasets | validated mechanism class |
| Anti-crowd standalone guarantee | losing outcomes remain | **REJECTED terminal guarantee** |

## H011 visible pre-purchase information
| Channel | Result | Status |
|---|---|---|
| NY exposed scratch-ticket serial | no official pre-purchase serial→prize decoder | **REJECTED** |
| Virginia front-barcode scan | purchase first; scan only after ownership | **POST-PURCHASE; REJECTED** |
| Public scratch remaining-prize tables | game-level state only | no deterministic ticket leak |
| Pack/ticket number or retailer location | no current official causal mapping | no validated edge |
| Ordinary online instant games | outcome follows paid play | no pre-purchase leak |

## H018 Virginia Lucky Contestant hidden-time state
| Test | Result | Status |
|---|---|---|
| Official causal odds schedule | hidden weighted daily selected time; odds tighten to 1/1 at selected time | **VALIDATED mechanism** |
| Bayesian/survival concentration | late-time conditional EV can rise under assumptions | overlay only |
| Standalone strict guarantee | another player may win before hidden time; ordinary losing outcomes remain | **REJECTED terminal guarantee** |
| Full EV strategy | exact interpolation/reset/live intensity incomplete | **OPEN/data-blocked overlay** |

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

Fresh H007 acquisition recheck on 2026-08-15 still failed to recover a trustworthy machine-readable bulk official history; do not run anomaly tests on incomplete samples.

## Other still-open / blocked classes
- H010 remaining-inventory instant-ticket state: blocked on public live denominator.
- H014 Azerbaijan 4+4 zero-winner carryover: data-blocked.
- H018 Lucky Contestant remains open only as conditional-EV/data-acquisition overlay; standalone guarantee closed.
- additional finite/final-draw games where **guaranteed external subsidy exceeds the H021 takeout hurdle**.
- H020 live executable arbitrage: scanner ready; resume where raw books/settlement can be fetched.
- H019 monitor only when guaranteed cash floor exceeds full effective capped-entry acquisition cost.

## H051 regulated principal protection / fixed reward
| Test | Result | Status |
|---|---|---|
| Azerbaijan Deposit Insurance Fund current framework | protected-deposit ceiling 12% AZN / 2.5% FX; insured compensation 100% up to 100,000 AZN, including interest accrued by insurance-event date | **STATUTORY PRINCIPAL-FLOOR MECHANISM VALIDATED**; `research/h051_regulated_deposit_fixed_reward_screen.md` |
| Ordinary insured fixed-interest deposit | immediate insurance-event branch can leave accrued interest arbitrarily close to zero | **REJECTED terminal guaranteed-profit path** despite strong principal protection |
| Current Azerbaijan bank/e-money/broker reward scan | card cashback, purchase bonuses, random/gamified rewards, fee waivers and trading/referral bonuses found; no unconditional separately vested withdrawable cash reward attached to protected principal found | **NO CURRENT TERMINAL CANDIDATE** |
| Stronger reward-timing branch | prepaid interest, upfront deposit gift, protected discounted redemption, regulated signup/account-switch cash | **OPEN as H052** |

## Current priorities
1. **H052 prepaid/upfront protected reward:** search prepaid-interest deposits, interest-in-advance products, deposit-opening cash gifts, discounted government-backed savings instruments, and regulated signup/account-switch cash bonuses accessible from Azerbaijan.
2. Capture live subscription/order terms for any principal-guaranteed structured product with a locked non-reducible minimum return.
3. Bound Azerbaijan funding/withdrawal/tax/FX costs for candidates that pass the reward-timing gate.
4. H037: recover remaining event count(s), broaden matched controls, fit overdispersed/hierarchical demand, and recompute after autumn-2026 rule change.
5. H020 live-data arbitrage if direct public raw-book access becomes available.
6. H006/H007 only after reliable histories/machine metadata become available.
7. H010/H014 when new authoritative data routes appear.
8. Advanced controls before EXHAUSTED: Bayesian hidden-state inference, additional current products, deterministic cash-rebate scan, and causal implementation tests.