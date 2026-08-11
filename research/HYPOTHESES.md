# HYPOTHESIS REGISTRY

Updated: 2026-08-11

Status values: `untested`, `testing`, `rejected`, `inconclusive`, `promising`, `validated`.

## H001 — Roll-down positive EV
**Claim:** A lottery with a roll-down / must-be-won mechanism can cross into positive expected value when accumulated jackpot funds are redistributed to lower tiers.

- Class: structural payout edge
- Baseline: exact combinatorial EV under ordinary draw
- Test: reconstruct payout table before/after trigger and include taxes, ticket throughput and sharing
- Historical benchmark: Massachusetts Cash WinFall
- Current target: UK Lotto Must Be Won and any other current forced-redistribution game
- Evidence: `research/cash_winfall_benchmark.md` reproduces a conservative cash-only +10.69% expected ROI for a historical May 9, 2011 roll-down using exact 6/46 probabilities and preserved draw payouts; free-bet value is excluded
- New current-game evidence: `research/uk_lotto_must_be_won.md` shows that forced redistribution is real in UK Lotto but the tested 2025 rolldowns remained negative at observed crowd sizes; current 2026 work splits the two-round rule regime separately
- Status: **validated as a historical mechanism class; current-game exploitation unvalidated**

## H002 — Jackpot threshold positive EV
**Claim:** A progressive jackpot game can reach a jackpot size where a ticket has positive pre-tax or post-tax EV.

- Class: progressive jackpot
- Baseline: full prize-tier EV
- Critical adjustment: expected jackpot sharing must increase with sales; advertised annuity must be converted to comparable cash/present value
- Targets: Powerball, Mega Millions, EuroMillions
- Status: untested

## H003 — Number-popularity avoidance improves conditional payout
**Claim:** Choosing combinations less likely to be chosen by other players does not increase draw probability but may increase expected jackpot share conditional on winning.

- Class: crowd behaviour
- Baseline: random selection with identical win probability
- Candidate signals: birthdays 1–31, straight sequences, repeated digits, visual shapes, culturally salient numbers
- Test: require ticket-choice or winner-sharing data; avoid inferring popularity from draw frequencies
- Status: untested

## H004 — Covering designs improve risk profile
**Claim:** Wheels / covering designs can improve probability of reaching specified lower-tier prize conditions for a fixed portfolio, even when they do not change raw per-ticket EV.

- Class: combinatorial optimization
- Baseline: equal-budget random independent portfolio
- Metrics: EV, variance, lower-tail loss, probability of at least one target-tier hit
- Status: untested

## H005 — Nonlinear prize tables can make optimized portfolios superior in EV
**Claim:** If prize rules include caps, guarantees, duplicate-line effects, multipliers or shared pools, portfolio construction may affect expected return rather than only variance.

- Class: combinatorial optimization
- Baseline: random portfolio
- Method: integer programming / dynamic programming where possible
- Status: untested

## H006 — Physical draw bias
**Claim:** A physical ball/machine process may show persistent number-level bias large enough to have out-of-sample predictive value.

- Class: randomness testing
- Requirement: plausible mechanism plus rule-era segmentation
- Tests: chi-square, machine/ball-set conditional models, serial diagnostics, multiple-testing correction
- Reject criterion: effect fails out-of-sample or is too small to overcome house edge
- Status: untested

## H007 — High-frequency virtual games expose implementation anomalies
**Claim:** High-frequency RNG-based games can provide enough samples to detect reproducible departures from the published random model if an implementation issue exists.

- Class: RNG diagnostics
- Targets: Ekspres Keno, Şanslı 6, ONLOTO and similar games
- Requirement: do not assume predictability from frequency alone; search for reproducible mechanism, regime changes and forward prediction
- Status: untested

## H008 — Cross-jurisdiction same-jackpot EV differences
**Claim:** When jurisdictions share a jackpot draw but charge different ticket prices or use different lower-tier/tax rules, one jurisdiction may offer materially better EV.

- Class: jurisdiction arbitrage / comparison
- First target: US Powerball vs UK Powerball after the July 2026 UK launch
- Important: legal availability and purchase-location rules are execution constraints
- Status: untested

## H009 — Promotional overlay
**Claim:** Cashback, free tickets, loyalty points, deposit bonuses, second-chance draws or operator promotions can turn a normally negative-EV product into positive EV for a bounded number of entries.

- Class: promotion
- Test: value every benefit conservatively and model wagering/withdrawal conditions
- Status: untested

## H010 — Instant-ticket remaining-prize edge
**Claim:** For scratch/instant games that publish remaining prizes and remaining ticket inventory, late-stage game state can create unusually high or potentially positive EV.

- Class: inventory-state edge
- Requirement: denominator (remaining tickets or defensible estimate) is essential; remaining prizes alone are not enough
- Status: untested

## H011 — Visible-ticket information leak
**Claim:** Some physical instant-ticket designs may leak outcome-correlated information before purchase/scratch due to ticket-generation or printing structure.

- Class: implementation flaw
- Historical benchmark: documented scratch-ticket design flaws
- Requirement: only test lawfully observable information and current tickets; do not generalize a historical flaw to other games
- Status: untested

## H012 — Full-space coverage / buy-the-pot
**Claim:** In certain finite ticket spaces, buying every combination can create positive expected return when jackpot/pool conditions exceed total ticket and execution costs.

- Class: syndicate / complete coverage
- Baseline condition: total expected retained prizes minus sharing/taxes > total acquisition cost
- Research references: Moffitt & Ziemba buy-the-pot / trump-ticket analyses
- Status: untested

## H013 — Operator page/prize-table inconsistency as research signal
**Claim:** Apparent inconsistencies between advertised maximums and base prize tables can reveal multiplier, bonus or rule details that materially change EV models.

- Class: data/rule audit
- First target: Super Keno currently advertises up to 1,000,000 AZN while the displayed base top tier is 100,000 AZN; multiplier mechanics appear to bridge the difference
- Status: promising as a data-quality finding; profitability not tested

## H014 — 4+4 category-pool / carryover state edge
**Claim:** The Azerbaijan 4+4 game may have draw states in which accumulated jackpot and/or lower-tier prize-pool money makes the draw materially better value, potentially analogous in mechanism (not necessarily magnitude) to a roll-down game.

- Class: state-dependent / pari-mutuel payout edge
- Evidence so far: official rules confirm two independent 4-from-20 boards, 11 prize categories and a rolling jackpot; secondary draw archives show materially varying per-winner payouts across lower categories
- Exact math: jackpot odds 1 in 23,474,025; any listed prize-state probability ~18.614724%
- New official state evidence: after a 530,359 AZN jackpot win on 2026-07-28 the operator said the next jackpot would be 250,000 AZN; official articles also document 913,072 AZN, >1,000,000 AZN and >1,300,000 AZN jackpot states
- Interpretation: jackpot accumulation alone contributes only about 0.01065 AZN EV at 250k and 0.05538 AZN at 1.3m per variant before tax/sharing, so lower-category state is the more important lead
- Critical unknowns: exact per-variant price, rule-version prize-fund allocation, whether/how lower category balances carry, pre-draw observability, sales volume and effect of our own tickets on winner shares
- Test: reconstruct consecutive draw state transitions and fit prize-pool allocation/carryover equations; require that any profitable signal is observable before purchase
- Status: **testing**

## H015 — Rolldown lower-tier anti-popularity edge
**Claim:** In forced-redistribution games where fixed category funds are divided among actual winners, choosing combinations that are less correlated with other players' choices can increase expected payout not only for the jackpot but also for lower rolldown tiers.

- Class: crowd behaviour + pari-mutuel sharing
- First target: UK Lotto Must Be Won
- Mechanism: every fixed line has the same raw match probability, but payout per winning entry can depend on how many competing entries land in the same prize category
- Important distinction: draw-number frequencies cannot estimate this edge; we need player-choice/collision data or a defensible crowd-choice model
- 2026 evidence: very large Round-1/Round-2 differences in Match-2 winner counts occur even though the same sold selections enter both rounds, demonstrating that non-uniform player selections materially affect realized winner counts
- Validation: compare expected category share for uniform/random or deliberately unpopular portfolios against a crowd-choice model, including self-collision
- Status: **promising theoretical mechanism; empirical magnitude untested**

## H016 — Wednesday Must Be Won calendar edge
**Claim:** Under the current two-round UK Lotto format, a Must Be Won draw that lands on Wednesday could cross into positive crowd-average EV because inherited carryover is built across preceding draws including high-sales Saturdays while ordinary Wednesday demand is materially lower.

- Class: calendar/state-dependent forced-redistribution edge
- Rule basis: Allwyn states jackpot starts at £2m, can roll five times and the sixth draw is Must Be Won; draws alternate Wednesday/Saturday
- Current-regime data: `data/historical/uk_lotto_sales_proxy_2026.csv` contains 15 rollover increments from 13 June through 8 August 2026
- Initial screen: Wednesday ordinary-demand proxy median ~5.08m tickets versus non-raffle Saturday median ~8.48m; median-path inherited carryover ~£7.313m; break-even max current sales ~6.801m
- Initial apparent margin: ordinary Wednesday demand could rise about **+33.77%** before the screen loses break-even
- Historical stress dataset: `data/historical/uk_lotto_wednesday_mbw_stress_old_regime.csv` reconstructs seven natural old-regime Wednesday sixth-draw states from 2023–2026
- Cleaner old-regime jackpot-growth uplift proxy: mean **+40.97%**, median **+42.85%**, range **+33.12% to +46.18%** relative to the previous ordinary Wednesday in the same cycle
- Result: the historical jackpot-growth uplift exceeds the current +33.77% screening margin in **6 of 7** samples; applying the historical median uplift to current ordinary-Wednesday demand projects ~7.263m tickets, above the ~6.801m break-even screen
- Independent noisy Match-2 proxy points the same direction (median uplift ~+41.26%)
- Mechanical stress result: with the original median-path carryover, historical mean/median demand uplift would reduce the simple current-regime screening value to roughly **£1.95 / £1.93 per £2 ticket**
- Caveats: old/new rule regimes differ; jackpot increments can include reserve/top-up effects; no current-regime Wednesday Must Be Won sample exists yet; updated primary 2026 allocation/rolldown procedures remain missing
- Full stress test: `research/uk_lotto_wednesday_mbw_stress_test.md`
- Status: **inconclusive / materially weakened; calendar effect alone is not a promising +EV trigger**

## Anti-hypotheses / controls
The following are not accepted as edges without extraordinary evidence:
- hot/cold numbers;
- "number due" logic;
- gambler's fallacy;
- numerology;
- pattern fitting on the same draws used to invent the pattern;
- martingale-style bet sizing that does not alter underlying EV;
- ML accuracy that does not beat a strict random baseline out-of-sample.
