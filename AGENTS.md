# AGENTS.md

This file defines how ChatGPT/Codex should work in this repository.

## Mission

Build a rigorous, reproducible research system for lotteries and lottery-like chance-based earning mechanisms. Search for structural conditions that can create positive expected value or true arbitrage, while rejecting unsupported pattern-finding and hindsight bias.

## Non-negotiable rules

1. Never claim a guaranteed profit unless every outcome is covered by a mathematically locked payoff and execution assumptions are verified.
2. Separate facts, assumptions, hypotheses and results.
3. Prefer official lottery/operator/regulator sources for rules and draw histories; record source URL, retrieval date and jurisdiction.
4. Never alter a strategy after seeing test-period outcomes without creating a new experiment/version.
5. Keep training/backtest data separate from validation/forward-test data.
6. Include ticket cost, taxes, fees, prize sharing, payout caps, rollover mechanics, transaction costs and liquidity/execution constraints in EV calculations.
7. Record failed ideas. Negative results are part of project memory and should not be silently retried under a new name.
8. Treat RNG/pseudorandomness claims skeptically. Statistical anomalies require multiple-testing correction, replication and a plausible mechanism.
9. Do not use quantum-physics terminology as an explanation unless it produces a concrete, testable mechanism relevant to the actual drawing system.
10. Reproducibility first: experiments should have fixed inputs, code version, parameters, seed where applicable, outputs and conclusion.

## Working pattern

Before major work:

1. Read `README.md`.
2. Read `STATUS.md`.
3. Read relevant files in `docs/` and the experiment folder.
4. Inspect existing datasets before recollecting them.

After major work:

1. Update `STATUS.md` with what changed, evidence, blockers and next actions.
2. Store new source metadata.
3. Store experiment configuration and result summary.
4. Commit meaningful checkpoints with descriptive messages.

## Preferred project structure

- `docs/games/` — one factual profile per game/operator.
- `docs/methods/` — mathematical and statistical methods.
- `docs/sources/` — source inventories and provenance.
- `data/raw/` — immutable source data.
- `data/processed/` — normalized data generated from raw data.
- `src/collectors/` — acquisition/parsing.
- `src/models/` — probability, EV and prize models.
- `src/analysis/` — statistical analysis.
- `src/sim/` — Monte Carlo/exhaustive simulation.
- `experiments/<id>/` — hypothesis, config, results and notes.
- `reports/` — consolidated findings.

## Candidate edge categories

Investigate at least:

- jackpot thresholds where EV changes materially;
- roll-down / rolldown distributions;
- guaranteed prize pools and overlays;
- promotions, rebates, cashback and second-chance drawings;
- syndicate/combinatorial coverage economics;
- prize-sharing effects and number popularity;
- taxes and jurisdiction differences;
- ticket bundles or subscription pricing;
- operator/rule mistakes or documented implementation flaws;
- historical physical-draw bias where a plausible mechanism exists;
- cross-game or cross-market arbitrage-like situations;
- payout timing / annuity-vs-cash effects;
- non-lottery prize competitions where entry economics can be modeled.

## Statistical safeguards

- Establish a null hypothesis before testing.
- Correct for multiple comparisons when scanning many patterns.
- Use holdout data.
- Report confidence intervals/effect sizes, not only p-values.
- Check data quality before interpreting anomalies.
- Distinguish prediction from explanation.
- Compare every strategy against simple random play and no-play baselines.

## Research output format

Every game profile should eventually include:

- jurisdiction/operator;
- accessibility/eligibility;
- game rules;
- ticket price;
- combinations/odds;
- prize tiers;
- jackpot mechanics;
- taxes/fees;
- historical-data source;
- theoretical RTP/EV;
- variance/tail risk;
- known special mechanics;
- candidate edges;
- current verdict and confidence.
