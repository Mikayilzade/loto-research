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
- Status: **validated as a historical mechanism class; current-game exploitation untested**

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
- Critical unknowns: exact per-variant price, rule-version prize-fund allocation, whether/how lower category balances carry, pre-draw observability, sales volume and effect of our own tickets on winner shares
- Test: reconstruct consecutive draw state transitions and fit prize-pool allocation/carryover equations; require that any profitable signal is observable before purchase
- Status: **testing**

## Anti-hypotheses / controls
The following are not accepted as edges without extraordinary evidence:
- hot/cold numbers;
- "number due" logic;
- gambler's fallacy;
- numerology;
- pattern fitting on the same draws used to invent the pattern;
- martingale-style bet sizing that does not alter underlying EV;
- ML accuracy that does not beat a strict random baseline out-of-sample.
