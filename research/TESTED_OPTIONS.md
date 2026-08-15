# TESTED OPTIONS / EXHAUSTIVE RESEARCH REGISTRY

Updated: 2026-08-15

Purpose: persistent audit trail of every game/project class, strategy class and important test variant considered. Do not delete rejected branches; record why they failed. Add new branches whenever research reveals them.

Status legend:
- `UNTESTED` — defined but not yet evaluated.
- `TESTING` — active work/data collection.
- `BLOCKED` — valid test identified but required data/tool unavailable.
- `REJECTED` — tested and does not produce the claimed edge under tested conditions.
- `WEAKENED` — initially promising but stress test materially reduced plausibility.
- `VALIDATED-MECHANISM` — mechanism exists, but not necessarily profitable now.
- `POSITIVE-EV-HISTORICAL` — historical +EV confirmed, not currently executable.
- `SUCCESS` — guaranteed positive net profit proven under explicit executable conditions.

## A. Draw-lottery structural overlays
| ID | Project / game | Test variant | Result / current status |
|---|---|---|---|
| H001 | Massachusetts Cash WinFall | Roll-down / lower-tier redistribution | `POSITIVE-EV-HISTORICAL`: May 9 2011 cash-only reconstruction ≈ +10.69% EV before tax/execution. Proves structural +EV can exist without predicting numbers. |
| H002 | Powerball / Mega Millions / EuroMillions | Progressive-jackpot break-even threshold after cash value, tax, sharing and sales response | `UNTESTED` |
| H016 | UK Lotto Must Be Won | Generic Must-Be-Won / rolldown state | `TESTED`: specific sampled states negative. |
| H016a | UK Lotto | Wednesday sixth-draw / low-weekday-demand hypothesis | `WEAKENED`: historical Must-Be-Won demand uplift usually exceeded initial EV cushion. |
| H017 | Kazakhstan 4/20 | Zero-winner lower categories feed next superprize | `VALIDATED-MECHANISM`: three transitions reconcile exactly; sampled state still strongly negative EV. |
| H014 | Azerbaijan 4+4 | State-dependent lower-pool / carryover edge | `TESTING/BLOCKED`: payout engine substantially reconstructed; exact adjacent state accounting still data-blocked. |
| H014a | Azerbaijan 4+4 | Ordinary variable-pool engine III–IX | `VALIDATED-MECHANISM`: empirical U-engine survives independent draw checks and official winner cross-checks. |
| H014b | Azerbaijan 4+4 | Category II ≈20U | `TESTING`: multiple official one-number-short winner stories consistent with scale, but system-ticket aggregation vs carryover unresolved. |
| H014c | Azerbaijan 4+4 | External jackpot transfers from retired games | `VALIDATED-MECHANISM`: operator announced possible transfer from closing Meqa 5/36; exact amount/event outcome unresolved. |

## B. Crowd / prize-sharing optimization
| ID | Project | Test variant | Result / current status |
|---|---|---|---|
| H003/H015 | Shared jackpots | Avoid exact popular combinations to reduce jackpot splitting | `VALIDATED-MECHANISM`: expected retained jackpot share improves; magnitude bounded and not standalone +EV. |
| H015a | 6/59 generic | Exact-combination popularity sensitivity 0.2×..10× | `TESTED`: useful protection; theoretical perfect-uniqueness uplift only affects jackpot component. |
| H015b | Shared lower tiers | Competitor-intensity reduction | `TESTING`: potentially much larger percentage payout effect; requires calibrated crowd-choice model. |
| H015c | Crowd model | Birthday-number bias | `UNTESTED` |
| H015d | Crowd model | Geometric/visual line patterns | `UNTESTED` |
| H015e | Crowd model | Consecutive numbers / arithmetic patterns | `UNTESTED` |
| H015f | Crowd model | Salient/lucky/cultural numbers | `UNTESTED` |
| H015g | Crowd model | Human-like mixture model + anti-crowd optimizer, out-of-sample | `UNTESTED` — current highest-priority implementation. |

## C. Portfolio / combinatorial construction
| ID | Project | Test variant | Result / current status |
|---|---|---|---|
| H004 | Wheels / covering designs | Improve hit probability / variance for fixed budget | `UNTESTED` |
| H005 | Nonlinear payout portfolio | Duplicate-line, caps, guarantees, shared pools, multiplier interactions | `UNTESTED` |
| H012 | Full-space coverage / buy-the-pot | Cover all combinations when guaranteed retained payout exceeds all-in cost | `UNTESTED` |
| H012a | Finite-space partial coverage | Integer-programmed coverage targeting guaranteed lower-tier floor | `UNTESTED` |
| H012b | Syndicate execution | Ticket-printing limits, validation capacity, retailer/network constraints | `UNTESTED` |

## D. Randomness / implementation weaknesses
| ID | Project | Test variant | Result / current status |
|---|---|---|---|
| H006 | Physical ball draws | Persistent machine/ball bias | `UNTESTED` |
| H006a | Physical draws | Position/order bias | `UNTESTED` |
| H006b | Physical draws | Machine/ball-set regime changes | `UNTESTED` |
| H007 | High-frequency RNG games | Generic distribution anomaly | `UNTESTED` |
| H007a | RNG | Serial correlation / runs / lag structure | `UNTESTED` |
| H007b | RNG | Seed/time dependence / implementation leak | `UNTESTED` |
| H007c | RNG | Cross-game correlated RNG streams | `UNTESTED` |
| Control | Hot/cold / due-number logic | Frequency-chasing without causal mechanism | `REJECTED-AS-PRIOR`: do not promote absent strict forward evidence. |
| Control | Martingale / staking progression | Change bet size without changing underlying EV | `REJECTED`: cannot turn negative EV positive. |

## E. Instant / scratch products
| ID | Project | Test variant | Result / current status |
|---|---|---|---|
| H010 | Azerbaijan Poz-Qazan | Initial series EV | `TESTED`: sampled initial after-tax payout ratios ~63–70%; negative. |
| H010a | Poz-Qazan | Remaining-prize / remaining-ticket conditional EV | `BLOCKED`: operator tracks inventory but no public registration-specific live denominator recovered. |
| H010b | Poz-Qazan | Store-level pack depletion / known pack state | `UNTESTED` |
| H011 | Physical instant tickets | Lawful visible pre-purchase information leak | `UNTESTED` |
| H011a | Scratch packs | Pack sequencing / prize spacing from published pack rules | `UNTESTED` |

## F. Promotions / jurisdiction / tax / conversion overlays
| ID | Project | Test variant | Result / current status |
|---|---|---|---|
| H008 | Same/shared jackpot across jurisdictions | Price/tax/lower-tier differences | `UNTESTED` |
| H009 | Promotions | Cashback | `UNTESTED` |
| H009a | Promotions | Free-ticket / deposit / first-play bonus | `UNTESTED` |
| H009b | Promotions | Second-chance drawings | `UNTESTED` |
| H009c | Promotions | Loyalty points / rewards conversion | `UNTESTED` |
| H009d | Promotions | Retailer/platform coupons or bounded subsidy | `UNTESTED` |
| H013 | Operator-page inconsistency | Hidden multiplier/bonus mechanism | `TESTED`: Super Keno 1x/2x/5x/10x ambiguity resolved; no EV edge. |

## G. Current Azerbaijan game baselines
| Game | Variant tested | Result |
|---|---|---|
| Beşdə 5 | Exact fixed-table EV | `TESTED`: favorable gross baseline ≈53.56%; strongly negative. |
| Super Keno | Base exact EV | `TESTED`: gross ≈59.86%; negative. |
| Super Keno | Multipliers 1x/2x/5x/10x | `REJECTED-EDGE`: proportional scaling keeps gross ROI invariant; after tax larger multipliers slightly worse. |
| 4+4 | Exact match probabilities | `TESTED` |
| 4+4 | III–IX payout structure | `VALIDATED-MECHANISM` |
| 4+4 | II-category structure / carryover | `TESTING` |

## H. Meta / advanced-method branches to test before EXHAUSTED
These are not assumed useful; each must eventually be tested or rejected with rationale.
- Bayesian state estimation for latent sales / jackpot-growth processes — `UNTESTED`.
- Change-point detection for rule/machine/RNG regimes — `UNTESTED`.
- Information-theoretic entropy / compression tests on high-frequency RNG — `UNTESTED`.
- Spectral / Fourier diagnostics where a causal periodic mechanism is plausible — `UNTESTED`.
- Genetic/evolutionary search for portfolio construction under nonlinear payout sharing — `UNTESTED`.
- Integer programming / covering-design optimization for guaranteed minimum prize floors — `UNTESTED`.
- ML crowd-choice prediction trained on historical human tickets, not winning draws — `UNTESTED`.
- ML winning-number prediction — only test after reliable data collection; strict random out-of-sample baseline required — `UNTESTED`.
- Cross-product arbitrage among lottery-adjacent prediction/raffle/promotional markets where legally/operationally available — `UNTESTED`.
- Syndicate pooling / diversification to reduce ruin probability without confusing variance reduction with EV — `UNTESTED`.

## Terminal audit
- `SUCCESS` found: **NO**.
- Registry exhausted: **NO**.
- Current highest-value open branch: **H015g crowd-choice model**, followed by H014 exact state accounting when new data route appears.
