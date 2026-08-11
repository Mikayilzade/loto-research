# AGENTS.md

## Project context
This repository is a reproducible research project for mathematical and statistical analysis of lotteries and lottery-like games.

## Before doing work
Read, in order:
1. `START_HERE.md`
2. `PROJECT_RULES.md`
3. `STATUS.md`
4. `RESEARCH_PLAN.md` if present

Then inspect the current `research-work` branch before changing anything.

## Engineering rules
- Prefer Python for collectors, probability models, simulations and analysis unless another language is clearly better.
- Keep raw source data immutable.
- Make every transformation reproducible from code.
- Record source URLs, retrieval dates and rule-version dates.
- Separate data collection, cleaning, modelling and reporting.
- Add tests for probability calculations, parsers and important transformations.
- Use deterministic random seeds for reproducible simulations when appropriate.
- Avoid brute-force enumeration when analytical reduction or efficient algorithms can solve the same problem.

## Research rules
- Treat draws as random unless evidence survives appropriate statistical testing.
- Correct for multiple testing / data snooping.
- Use out-of-sample or forward validation for predictive claims.
- Compare every predictive model with a strict random baseline.
- Quantify uncertainty and include all known costs in economic calculations.
- Do not describe a method as guaranteed profitable unless a formal proof covers all relevant outcomes and execution assumptions.

## Documentation
After meaningful work, update `STATUS.md` with:
- what changed;
- files/data added;
- tests run;
- findings;
- next action.
