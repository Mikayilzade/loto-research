# loto-research

Reproducible research project for lotteries and lottery-like games.

## Goal
Identify and rigorously validate any structural condition that can produce positive expected value or arbitrage after ticket cost, taxes, commissions, jackpot sharing and execution constraints. If a proposed edge does not survive exact math and out-of-sample testing, record it as rejected rather than recycling it later.

## Working branch
`research-work`

## Start here
Read in this order:
1. `START_HERE.md`
2. `PROJECT_RULES.md`
3. `STATUS.md`
4. `RESEARCH_PLAN.md`
5. `AGENTS.md` for code/Codex work

## Current structure

```text
catalog/
  games.csv           initial game universe
  sources.csv         official/primary source registry
research/
  HYPOTHESES.md       hypothesis registry
  azerbaijan_baseline.md
schemas/
  DATA_MODEL.md
src/loto_research/
  probability.py      exact combinatorial probability + baseline EV helpers
tests/
  test_probability.py
```

## Current research priorities
1. Azerbaijan draw games: Beşdə 5, 4+4, Super Keno and high-frequency virtual games.
2. Progressive-jackpot threshold models: Powerball, Mega Millions, EuroMillions.
3. Roll-down / Must Be Won mechanics: historical Cash WinFall and current comparable rules.
4. Crowd-selection and jackpot-sharing effects.
5. Instant/scratch games with published batch payout information.

## Validation standard
A strategy is not accepted because it looks good on historical data. It must have:
- a mathematical mechanism;
- reproducible code/data;
- a strict random or exact baseline;
- out-of-sample/forward validation where prediction is claimed;
- multiple-testing correction where many patterns are searched;
- net economics after all known costs.

## Tests
No GitHub Actions workflow is enabled. Local regression tests can be run with:

```bash
python -m unittest discover -s tests -v
```
