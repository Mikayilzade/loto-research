# Project Status

Last updated: 2026-08-11

## Phase

`PHASE 0 — research infrastructure`

## Completed

- Repository connected and writable from ChatGPT.
- Project scope defined in `README.md`.
- Operating and evidence rules defined in `AGENTS.md`.
- Core principle fixed: search aggressively for positive-EV mechanisms, but do not label anything profitable/guaranteed without reproducible evidence.

## Current priorities

1. Build an initial registry of lottery and lottery-like products, starting with Azerbaijan plus major international games with accessible historical data.
2. Define normalized schemas for games, draws, prize tiers, ticket prices, jackpots, promotions, taxes and sources.
3. Identify the best official historical data sources and archive provenance.
4. Build first collectors/normalizers.
5. Implement a generic probability/EV engine.

## Research tracks

### A. Baseline mathematics
Status: `NOT STARTED`

Combinatorics, exact odds, prize expectation, jackpot sharing, tax/cost adjustments, variance and bankroll risk.

### B. Historical draw analysis
Status: `NOT STARTED`

Data validation, frequency tests, independence tests, mechanical bias tests where applicable, multiple-comparison-safe anomaly detection.

### C. Structural positive-EV search
Status: `NOT STARTED`

Roll-downs, overlays, jackpot thresholds, promotions, rebates, second-chance games, syndicate economics, payout-option effects and cross-market opportunities.

### D. Strategy laboratory
Status: `NOT STARTED`

Backtests, simulations, exhaustive searches where feasible, holdout validation and forward testing.

### E. Game universe expansion
Status: `NOT STARTED`

Lottery-like competitions, raffles, prize pools and other chance-based mechanisms whose economics can be modeled legally and reproducibly.

## First milestone

Produce a ranked table of at least 25 games/mechanisms with:

- exact rule source;
- ticket cost;
- theoretical odds;
- payout structure;
- available historical depth;
- normal-play EV estimate where calculable;
- special mechanisms that could change EV;
- research priority score.

## Open decisions

- Preferred storage format for large raw datasets once volume becomes significant (Git LFS vs compressed files vs external object storage).
- Whether to keep the repository public once detailed research and datasets accumulate.
- Which jurisdictions should be prioritized after Azerbaijan.

## Next action

Create the game registry/data schema, then begin source discovery and ingestion.
