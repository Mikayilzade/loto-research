# RESEARCH PLAN

Updated: 2026-08-11
Branch: `research-work`

## Mission
Build a reproducible research system for lotteries and lottery-like games that can identify, quantify and validate any real positive expected-value or arbitrage condition that survives all costs, taxes, sharing risk and execution constraints.

The project does not assume that ordinary number prediction is possible. It explicitly searches for structural edges in game rules, payout mechanics, promotions, rollovers, roll-downs, ticket allocation, prize-sharing behaviour, implementation mistakes and statistically detectable non-random mechanisms.

## Stage 1 — Universe and data model
1. Build a catalog of current and historical games.
2. Record official sources and rule-version dates.
3. Normalize game mechanics, prices, prize tables, taxes, draw schedules and availability.
4. Prioritize 5–10 representative games covering different structures.
5. Define draw and payout schemas.

### Initial representative set
- Azerbaijan: Beşdə 5
- Azerbaijan: 4+4
- Azerbaijan: Super Keno
- Azerbaijan: Ekspres Keno
- US: Powerball
- US: Mega Millions
- UK: Lotto
- Europe/UK: EuroMillions
- Historical positive-EV case: Massachusetts Cash WinFall
- Instant/scratch category: one game with published payout/remaining-prize data

## Stage 2 — Baseline probability and EV engine
Create tested functions for:
- combinatorial odds;
- one-pool and multi-pool games;
- fixed-prize and pari-mutuel prizes;
- progressive jackpots;
- shared-jackpot probability;
- tax and commission adjustments;
- expected value, variance and probability of loss;
- bankroll/risk-of-ruin simulation.

Every game must first pass through the baseline model before any predictive or optimization strategy is tested.

## Stage 3 — Historical data ingestion
For each priority game:
1. Prefer official archives.
2. Store raw data unchanged.
3. Record retrieval date and source URL.
4. Normalize draws through reproducible code.
5. Validate record counts, date continuity and number ranges.
6. Flag rule changes so incompatible eras are not mixed.

Preferred storage:
- small metadata and samples in Git;
- larger datasets in Parquet/DuckDB when volume grows.

## Stage 4 — Edge discovery
Research streams:

### A. Structural payout edges
- roll-down / rolldown mechanics;
- must-be-won draws;
- guaranteed pools and overlays;
- progressive-jackpot thresholds;
- second-chance and bonus mechanisms;
- promotions, cashback and discounts;
- stale or incorrectly calibrated prize tables.

### B. Sharing / crowd behaviour
- birthday-number bias;
- sequences and visually popular patterns;
- avoidance of common selections;
- expected jackpot share conditional on winning;
- ticket-space coverage by syndicates.

### C. Coverage optimization
- wheels and covering designs;
- integer programming;
- portfolio construction across prize tiers;
- variance reduction under a fixed budget;
- full-space or partial-space coverage feasibility.

### D. Randomness / implementation testing
- frequency and chi-square tests;
- serial dependence;
- runs tests;
- entropy and spectral diagnostics;
- physical-machine or ball-set effects where relevant;
- RNG implementation issues only where a plausible mechanism exists.

All findings must be corrected for multiple testing and validated out-of-sample.

## Stage 5 — Historical exploit case studies
Reconstruct known examples where players obtained an edge, including:
- Massachusetts Cash WinFall roll-down;
- full-combination / buy-the-pot strategies in suitable 6/49-style games;
- documented scratch-ticket information leaks or production flaws;
- any other verified rule or implementation anomaly.

For each case, reproduce the economics from first principles rather than relying on media descriptions.

## Stage 6 — Strategy validation ladder
Classify every candidate:

- **A — Arbitrage / formal guarantee:** all modeled outcomes profitable under stated execution assumptions.
- **B — Positive EV:** expected return > 0 after all costs, but realized loss remains possible.
- **C — Near-arbitrage:** very high probability of aggregate profit with quantified tail risk.
- **D — Optimization only:** improves variance, sharing or return relative to random play but EV remains <= 0.
- **F — Rejected / illusion:** no reproducible edge after proper testing.

## Stage 7 — Execution feasibility
Before any real-money conclusion, model:
- legal availability to the player;
- purchase limits and sales cutoffs;
- ticket-printing throughput;
- capital required;
- taxes and withholding;
- claim logistics;
- jackpot sharing;
- operator rule-change risk;
- currency conversion;
- failed/void ticket risk;
- operational labour and data costs.

## Immediate next work
1. Populate `catalog/games.csv` and `catalog/sources.csv`.
2. Create `schemas/DATA_MODEL.md`.
3. Create `research/HYPOTHESES.md`.
4. Add generic probability/EV code and tests.
5. Start deep model of Beşdə 5 and Super Keno.
6. Reconstruct Cash WinFall as the first historical positive-EV benchmark.
