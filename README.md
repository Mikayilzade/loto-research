# Loto Research

Evidence-first research project on lotteries, lottery-like games, promotions, prize pools and other chance-based earning mechanisms.

## Goal

Map the available game types, rules, costs, payout structures and historical results; collect reliable draw data; build reproducible mathematical models; and search for conditions where expected value (EV) can become positive after all costs.

The project does **not** assume that a guaranteed-profit strategy exists. Any claimed edge must survive independent verification, realistic costs, rule constraints and out-of-sample testing.

## Core questions

1. What games and mechanisms exist, and where are they legally accessible?
2. What are the exact rules, ticket costs, prize tables, taxes/fees and payout mechanics?
3. What is the theoretical EV and variance under normal play?
4. Do jackpots, roll-downs, promotions, syndicates, rebates, second-chance systems, pricing errors or rule interactions ever create positive EV?
5. Can historical data reveal non-randomness, implementation flaws or exploitable structural bias?
6. Can any candidate strategy be reproduced and remain profitable after execution constraints?

## Research standard

Every candidate strategy is classified as one of:

- `THEORY` — mathematical idea only.
- `BACKTESTED` — tested on historical data.
- `SIMULATED` — tested with Monte Carlo / exhaustive computation.
- `FORWARD_TESTED` — tested on unseen/future data without changing the rule afterward.
- `POSITIVE_EV_CANDIDATE` — positive EV under documented assumptions.
- `REJECTED` — no edge or invalid assumptions.
- `VERIFIED_EDGE` — independently reproducible edge after costs and constraints.

No strategy is described as guaranteed unless the payoff is mathematically locked (for example a genuine arbitrage) and all execution assumptions are verified.

## Repository map

- `AGENTS.md` — operating instructions for ChatGPT/Codex and future sessions.
- `STATUS.md` — current state and next actions.
- `docs/` — methodology, rules, source notes, legal/tax notes.
- `data/` — data dictionaries and collected draw datasets.
- `src/` — collectors, normalizers, models and simulation code.
- `experiments/` — reproducible strategy experiments.
- `reports/` — findings and comparison reports.

## Immediate roadmap

1. Build a lottery/game registry.
2. Define a normalized data schema.
3. Prioritize official/public historical draw sources.
4. Implement collectors and validation checks.
5. Compute theoretical EV for each game.
6. Backtest candidate mechanisms.
7. Stress-test surviving candidates with Monte Carlo and out-of-sample validation.

The project is research-driven: disproving a strategy is useful progress because it removes a false path from the search space.
