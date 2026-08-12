# HYPOTHESIS REGISTRY

Updated: 2026-08-12

Status values: `untested`, `testing`, `rejected`, `inconclusive`, `promising`, `validated`.

## H001 — Roll-down positive EV
**Claim:** A lottery with a roll-down / must-be-won mechanism can cross into positive expected value when accumulated jackpot funds are redistributed to lower tiers.
- Historical benchmark: Massachusetts Cash WinFall.
- Evidence: conservative cash-only May 9, 2011 reconstruction gives about **+10.69% expected ROI** before tax/execution.
- Status: **validated as a historical mechanism class; current-game exploitation unvalidated**.

## H002 — Progressive jackpot threshold
**Claim:** A progressive jackpot can reach a state where a ticket is +EV after cash-value, sharing, tax and sales response are included.
- Targets: Powerball, Mega Millions, EuroMillions.
- Status: `untested`.

## H003 — Number-popularity avoidance
**Claim:** Less-popular combinations do not increase draw probability but may improve conditional shared payout.
- Status: `untested`.

## H004 — Covering designs improve risk profile
**Claim:** Wheels/covering designs can improve target-tier hit probability or variance for fixed budget even when raw EV is unchanged.
- Status: `untested`.

## H005 — Nonlinear payout portfolio edge
**Claim:** Caps, guarantees, shared pools, duplicate-line effects or multipliers can make portfolio construction affect EV rather than only variance.
- Status: `untested`.

## H006 — Physical draw bias
**Claim:** A physical machine/ball process may have persistent bias large enough to survive multiple-testing correction and forward validation.
- Status: `untested`.

## H007 — High-frequency RNG implementation anomaly
**Claim:** High-frequency virtual games may provide enough samples to detect reproducible departures from the published random model if implementation is flawed.
- Targets: Ekspres Keno, Şanslı 6, ONLOTO and comparators.
- Status: `untested`.

## H008 — Cross-jurisdiction same-jackpot EV difference
**Claim:** Shared jackpot games can have materially different EV by jurisdiction because of price, lower tiers, tax and payout rules.
- First target: US vs UK Powerball.
- Status: `untested`.

## H009 — Promotional overlay
**Claim:** Cashback, free tickets, second-chance draws, loyalty rewards or bounded bonuses can turn a normally negative product +EV for a limited volume.
- Status: `untested`.

## H010 — Instant-ticket remaining-prize edge
**Claim:** If a physical instant-ticket series exposes both remaining after-tax prize value and a defensible remaining-purchasable-ticket denominator, late-stage conditional EV can differ materially from initial EV and may in principle cross positive.

### Initial Azerbaijan evidence
Current registered Poz-Qazan series expose enough information to compute exact initial after-tax EV:
- Prestij reg.317: **~69.906%** after-tax payout ratio;
- Meqa 7 reg.365: **~66.876%**;
- Qoşa 2 reg.383: **~66.305%**;
- 4 Fəsil reg.375: **~62.978%**.

All initial states remain negative EV.

### Decisive blocker
No public live registration-specific counter was found for remaining unsold tickets or a complete current remaining-prize table. Legal/tax rules show ticket-sales and unsold inventory are tracked institutionally, but no public live denominator has been recovered.

### Data-quality finding
Winner carousels can mix different historical releases with the same game name; inventory must be matched by exact registration/batch before decrementing prize counts.

- Data: `data/derived/az_poz_qazan_initial_ev_2026.csv`.
- Analysis: `research/poz_qazan_remaining_prize_edge.md`.
- Status: **testing / data-blocked; mechanism valid in principle, no executable Azerbaijan state yet**.

## H011 — Visible-ticket information leak
**Claim:** A physical instant-ticket design may reveal lawful pre-purchase information correlated with outcomes.
- Status: `untested`.

## H012 — Full-space coverage / buy-the-pot
**Claim:** Finite spaces can become profitable to cover when retained payout exceeds acquisition, sharing, tax and execution cost.
- Status: `untested`.

## H013 — Operator page/prize-table inconsistency signal
**Claim:** Apparent operator-page inconsistencies can reveal multiplier/bonus mechanics that materially alter EV models.

### Super Keno result
The apparent `100,000 AZN base top tier` vs `up to 1,000,000 AZN` inconsistency is now **resolved**.

Current operator/FAQ material states that one Super Keno variant can be paid at **1x, 2x, 5x or 10x**. The 10x option costs 10x the base payment and scales prizes 10x, so the advertised 1m maximum is the 10x version of the 100k base top tier, not a free overlay.

Exact displayed-table gross payout ratio is invariant at about **59.8556%** before tax. Under the current tax formula, a single-variant favorable upper-bound after-tax payout ratio is approximately:
- 1x: **59.1807%**
- 2x: **59.1266%**
- 5x: **58.9036%**
- 10x: **58.6982%**

Larger multipliers are slightly worse after tax because the 500-AZN deduction is fixed while prize amounts scale. Top-prize sharing is ignored in these favorable bounds and can only lower real EV.

- Data: `data/derived/az_superkeno_multiplier_ev.csv`.
- Analysis: `research/superkeno_multiplier_economics.md`.
- Status: **validated as a useful data-audit finding; Super Keno multiplier ambiguity resolved, no multiplier EV edge found**.

## H014 — Azerbaijan 4+4 state-dependent pool/carryover edge
**Claim:** A pre-draw observable accumulated balance in one or more variable 4+4 prize categories may create unusually favorable or potentially +EV states.

Established:
- jackpot probability **1 / 23,474,025**;
- any listed winning group probability **~18.614724%**;
- strong empirical draw-level pool engine:
  - III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U;
- draw #790 and draw #781 provide independent checks;
- median `U/N` remains close to 0.01;
- ordinary subtotal before category II and jackpot about **1.16215 AZN per assumed 2-AZN variant**.

Important correction: standalone winner-story payouts are not category totals and cannot independently estimate U without winner counts/ticket structure.

The live test remains zero-winner II–VI state accounting across adjacent draws.
- Status: **testing; zero-winner carryover hypothesis remains live but unvalidated**.

## H015 — Rolldown lower-tier anti-popularity edge
**Claim:** In shared/rolldown categories, less-correlated number choices can improve expected share even below jackpot level.
- Evidence lead: current two-round UK Lotto has large Round-1/Round-2 differences in winner counts despite the same sold selections entering both rounds, consistent with non-uniform crowd choices affecting realized sharing.
- Requirement: quantify expected-share uplift under a defensible crowd-choice model and compare the uplift against the underlying negative EV; do not infer player preferences from draw frequencies.
- Status: **promising theoretical mechanism; empirical magnitude untested**.

## H016 — Wednesday Must Be Won calendar edge
**Claim:** A Wednesday sixth-draw UK Lotto state might benefit from inherited carryover meeting lower weekday demand.
- Stress test: seven historical analogues show median demand uplift above the initial break-even cushion.
- Status: **inconclusive / materially weakened; calendar effect alone is not a promising trigger**.

## H017 — Zero-winner lower-category funds feed the next superprize
**Claim:** In at least some active pari-mutuel draw lotteries, a lower category with no winners can feed its assigned fund into a visible cumulative superprize for the next draw.

Validated comparator: Kazakhstan Satty Zhuldyz 4/20.
Three independent transitions close exactly as:
`J_t = J_(t-1) + unpaid_lower_pools_(t-1) + ordinary_current_contribution`.

Example 1545→1546:
`226,866,699 + 248,580 + 132,678 = 227,247,957 KZT` exactly.

The sampled state remains strongly negative EV (~55% immediate return; static break-even superprize ~3.395bn KZT vs ~227m observed).

- Data: `data/historical/kz_4x20_transition_samples.csv`.
- Analysis: `research/kazakhstan_4x20_control.md`.
- Status: **validated active mechanism; current sampled state negative EV**.

## Anti-hypotheses / controls
Do not accept as an edge without extraordinary forward evidence:
- hot/cold numbers;
- “number due” logic;
- gambler's fallacy;
- numerology;
- fitting and testing on the same data;
- martingale/bet sizing that leaves underlying EV unchanged;
- ML that does not beat a strict random baseline out-of-sample.
