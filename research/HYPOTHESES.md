# HYPOTHESIS REGISTRY

Updated: 2026-08-12

Status values: `untested`, `testing`, `rejected`, `inconclusive`, `promising`, `validated`.

## H001 — Roll-down positive EV
**Claim:** A lottery with a roll-down / must-be-won mechanism can cross into positive expected value when accumulated jackpot funds are redistributed to lower tiers.
- Historical benchmark: Massachusetts Cash WinFall.
- Evidence: `research/cash_winfall_benchmark.md` reproduces a conservative cash-only +10.69% expected ROI for a preserved May 9, 2011 roll-down.
- Status: **validated as a historical mechanism class; current-game exploitation unvalidated**.

## H002 — Progressive jackpot threshold
**Claim:** A progressive jackpot can reach a state where a ticket is +EV after cash-value, sharing, tax and sales response are included.
- Targets: Powerball, Mega Millions, EuroMillions.
- Status: `untested`.

## H003 — Number-popularity avoidance
**Claim:** Less-popular combinations do not increase draw probability but may increase conditional jackpot/share payout.
- Candidate crowd signals: birthdays, simple sequences, repeated endings, culturally salient numbers, visual patterns.
- Status: `untested`.

## H004 — Covering designs improve risk profile
**Claim:** Wheels/covering designs can improve target-tier hit probability or variance for a fixed budget even when raw EV is unchanged.
- Status: `untested`.

## H005 — Nonlinear payout portfolio edge
**Claim:** Caps, guarantees, shared pools, duplicate-line effects or multipliers can make portfolio construction affect EV rather than only variance.
- Status: `untested`.

## H006 — Physical draw bias
**Claim:** A physical machine/ball process may have persistent bias large enough to survive multiple-testing correction and forward validation.
- Status: `untested`.

## H007 — High-frequency RNG implementation anomaly
**Claim:** High-frequency virtual games may provide enough samples to detect reproducible departures from their published random model if an implementation problem exists.
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
**Claim:** Published remaining prizes plus a defensible remaining-ticket denominator can create state-dependent scratch-ticket EV.
- Requirement: remaining-prize counts alone are insufficient.
- Status: `untested`.

## H011 — Visible-ticket information leak
**Claim:** A physical instant-ticket design may reveal lawful pre-purchase information correlated with outcomes.
- Status: `untested`.

## H012 — Full-space coverage / buy-the-pot
**Claim:** Finite spaces can become profitable to cover when retained payout exceeds acquisition, sharing, tax and execution cost.
- Status: `untested`.

## H013 — Rule/prize-table inconsistency signal
**Claim:** Apparent operator-page inconsistencies can reveal multiplier/bonus mechanics that materially alter EV models.
- First target: Super Keno base 100k tier vs advertised up-to-1m outcome.
- Status: `promising as data-audit signal; profitability untested`.

## H014 — Azerbaijan 4+4 state-dependent pool/carryover edge
**Claim:** A pre-draw observable accumulated balance in one or more variable 4+4 prize categories may create unusually favorable or potentially +EV draw states.

### What is now established
- exact jackpot probability: **1 / 23,474,025**;
- exact probability of any of the 11 listed winning groups: **~18.614724%**;
- official public ticket price: **2 AZN**;
- fixed observed tail prizes: category X = 6 AZN, XI = 4 AZN in the sampled secondary tables;
- seven sampled 2026 draw tables, including draw 790 used as an out-of-sample check, reveal a highly stable common-unit payout engine.

### Empirical pool engine
For ordinary sampled draws, define a draw-level common unit `U`:
- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Therefore III–IX jointly distribute approximately **48U**. Draw 790 confirmed the pattern after it had been inferred from the earlier sample, reducing the chance that it is simple overfit.

### Economic implication
The working scale `U ≈ 0.01 × sold_variants` fits observed X/XI winner counts reasonably well and is equivalent to U being ~0.5% of revenue if one base variant costs 2 AZN. This makes **2 AZN per base variant a high-confidence inference**, consistent with the operator's displayed ticket price, but still not a direct detailed-rule statement.

Under that working scale:
- III–IX crowd-average contribution ≈ **0.48 AZN / variant**;
- X/XI exact expected contribution ≈ **0.682149738 AZN / variant**;
- subtotal before category II and jackpot ≈ **1.16215 AZN per 2-AZN variant** (~58.11% gross return).

Thus ordinary draw-to-draw variation in lower-tier payout per winner is **not itself an exploitable signal**; it is mostly explained by stable pool weights divided among changing winner counts.

### Revised carryover test
The decisive target is now a zero-winner state in a variable low-probability category (especially II–VI):
1. infer ordinary U for draw t;
2. calculate the category's expected assigned pool;
3. observe that it was not paid because there were zero winners;
4. inspect draw t+1 and later draws;
5. determine whether the unpaid balance carries to the same category, another category, jackpot, reserve, or is redistributed immediately;
6. require the balance/state to be observable **before** buying the next ticket.

Only that pre-draw state can become a real H014 strategy signal.

- Data: `data/historical/az_4plus4_payout_samples_2026.csv`.
- Model: `src/loto_research/four_plus_four.py`.
- Detailed analysis: `research/4plus4_economics_inference.md`.
- Status: **testing; ordinary-variable-payout interpretation weakened, zero-winner carryover hypothesis remains live**.

## H015 — Rolldown lower-tier anti-popularity edge
**Claim:** In shared/rolldown categories, less-correlated number choices can improve expected share even below jackpot level.
- Evidence: current two-round UK Lotto has large Round-1/Round-2 differences in winner counts despite the same sold selections entering both rounds, consistent with non-uniform crowd choices affecting realized sharing.
- Status: **promising theoretical mechanism; empirical economic magnitude untested**.

## H016 — Wednesday Must Be Won calendar edge
**Claim:** A Wednesday sixth-draw UK Lotto state might benefit from inherited carryover meeting lower weekday demand.
- Initial current-regime demand cushion: ~+33.77%.
- Seven old-regime Wednesday Must-Be-Won analogues show median demand uplift ~+42.85%; six of seven exceed the cushion.
- Stress-tested screening value falls to roughly £1.93–£1.95 per £2 at historical mean/median uplift.
- Status: **inconclusive / materially weakened; calendar effect alone is not a promising trigger**.

## Anti-hypotheses / controls
Do not accept as an edge without extraordinary forward evidence:
- hot/cold numbers;
- “number due” logic;
- gambler's fallacy;
- numerology;
- fitting and testing on the same draws;
- martingale/bet sizing that leaves underlying EV unchanged;
- ML that does not beat a strict random baseline out-of-sample.
