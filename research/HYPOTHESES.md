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
- Status: **partially quantified under H015; useful sharing optimizer, not standalone +EV**.

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

Current Azerbaijan registered-series initial after-tax payout ratios:
- Prestij reg.317: ~69.906%
- Meqa 7 reg.365: ~66.876%
- Qoşa 2 reg.383: ~66.305%
- 4 Fəsil reg.375: ~62.978%.

All initial states negative. Legal/tax rules show sales and unsold inventory are tracked institutionally, but no public live registration-specific denominator has been recovered. Winner carousels can mix historical releases, so exact registration identity is mandatory.

- Data: `data/derived/az_poz_qazan_initial_ev_2026.csv`.
- Analysis: `research/poz_qazan_remaining_prize_edge.md`.
- Status: **testing / data-blocked; no executable Azerbaijan state yet**.

## H011 — Visible-ticket information leak
**Claim:** A physical instant-ticket design may reveal lawful pre-purchase information correlated with outcomes.
- Status: `untested`.

## H012 — Full-space coverage / buy-the-pot
**Claim:** Finite spaces can become profitable to cover when retained payout exceeds acquisition, sharing, tax and execution cost.
- Status: `untested`.

## H013 — Operator page/prize-table inconsistency signal
**Claim:** Apparent operator-page inconsistencies can reveal multiplier/bonus mechanics that materially alter EV models.

Super Keno `100k base / up to 1m` ambiguity is resolved: one variant supports 1x/2x/5x/10x payment, with prizes scaling proportionally. Gross displayed-table ROI is invariant ~59.8556%; after tax the larger multipliers are slightly worse (~59.18% at 1x down to ~58.70% at 10x), before top-prize sharing.

- Data: `data/derived/az_superkeno_multiplier_ev.csv`.
- Analysis: `research/superkeno_multiplier_economics.md`.
- Status: **validated data-audit finding; ambiguity resolved, no multiplier EV edge**.

## H014 — Azerbaijan 4+4 state-dependent pool/carryover edge
**Claim:** A pre-draw observable accumulated balance in one or more variable 4+4 prize categories may create unusually favorable or potentially +EV states.

Established:
- jackpot probability **1 / 23,474,025**;
- any listed winning group probability **~18.614724%**;
- draw-level pool engine III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U;
- draw #790 and #781 independent checks;
- median `U/N` close to 0.01;
- ordinary subtotal before II and jackpot about **1.16215 AZN per assumed 2-AZN variant**.

Live test remains zero-winner II–VI state accounting across adjacent draws. Manual archive routes are currently data-blocked.
- Status: **testing; zero-winner carryover hypothesis live but unvalidated**.

## H015 — Rolldown/shared-pool anti-popularity edge
**Claim:** In shared prize pools, less-popular combinations can improve expected retained share conditional on winning; this may improve EV when layered on top of a structural overlay/rolldown.

### Empirical mechanism
Large proprietary lottery datasets show strong non-uniform player choice. In one 6/45 dataset, diagonal/vertical visual-pattern combinations represented **0.9%** of actual entries versus **0.009%** expected under random choice, while many specific popular combinations appeared hundreds of times. A 2026 New Zealand Lotto study using >70m played six-tuples identifies prize sharing as a first-order ticket-valuation feature.

### Exact-jackpot magnitude bound
For a 6/59 game (`M=C(59,6)=45,057,474`), at **10m other lines**:
- uniform combination: expected conditional jackpot share ≈ **89.68%**;
- 0.2×-popular: ≈ **97.81%**, about **+9.07%** to jackpot component vs uniform;
- theoretical no-duplicate upper bound: **+11.51%** vs uniform;
- 5×-popular: ≈ **60.41%**, about **−32.64%** vs uniform;
- 10×-popular: ≈ **40.16%**, about **−55.22%** vs uniform.

Across 5m–15m other lines, perfect uniqueness can improve the jackpot component by only about **+5.65% to +17.57%** versus uniform.

### Lower-tier shared-pool sensitivity
If `lambda` is expected competing winner count conditional on our lower-tier hit and `X~Poisson(lambda)`, expected pool fraction is `(1-exp(-lambda))/lambda`.

For large shared categories, changing relative competitor intensity approximately inversely changes payout:
- 0.8× competitor intensity -> **~1.25× payout**;
- 0.6× -> **~1.667× payout**;
- 0.5× -> **~2.0× payout**;
- 1.2× -> ~0.833× payout;
- 1.5× -> ~0.667× payout;
- 2× -> ~0.5× payout.

Thus lower-tier shared-pool optimization can have materially larger percentage impact than exact jackpot anti-duplication **if** we can predictably reduce competitor intensity before the draw.

### Interpretation
Anti-popularity is real and useful, but not a standalone cure for a deeply negative lottery. Exact-jackpot upside is bounded; lower-tier rolldown sharing is the more promising channel.

The scientific bottleneck is now a pre-draw crowd-choice model that maps our chosen line to expected competing-winner count in the target shared category. Simple heuristics such as “pick high numbers” cannot yet be promoted to EV claims.

- Data:
  - `data/derived/h015_jackpot_collision_screen_6of59.csv`
  - `data/derived/h015_shared_pool_intensity_sensitivity.csv`
- Analysis: `research/h015_crowd_sharing.md`.
- Status: **quantitatively promising as an overlay optimizer; jackpot benefit bounded, lower-tier sensitivity large but achievable crowd-intensity reduction unvalidated**.

## H016 — Wednesday Must Be Won calendar edge
**Claim:** A Wednesday sixth-draw UK Lotto state might benefit from inherited carryover meeting lower weekday demand.
- Stress test: seven historical analogues show median demand uplift above the initial break-even cushion.
- Status: **inconclusive / materially weakened; calendar effect alone is not a promising trigger**.

## H017 — Zero-winner lower-category funds feed the next superprize
**Claim:** In at least some active pari-mutuel draw lotteries, a lower category with no winners can feed its assigned fund into a visible cumulative superprize for the next draw.

Validated comparator: Kazakhstan Satty Zhuldyz 4/20. Three independent transitions close exactly as:
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
