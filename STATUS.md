# STATUS

Updated: 2026-08-11
Branch: `research-work`

## Current stage
**Stage 1 — universe, exact baseline and source/data model**

## Completed
- GitHub repository connected and inspected.
- Dedicated working branch `research-work` exists.
- `START_HERE.md`, `PROJECT_RULES.md` and `AGENTS.md` establish handoff, scientific and engineering rules.
- `RESEARCH_PLAN.md` defines the staged research program and validation ladder.
- `catalog/games.csv` contains the first representative universe across Azerbaijan, US, UK/Europe and historical Cash WinFall.
- `catalog/sources.csv` records official/primary sources and retrieval dates.
- `schemas/DATA_MODEL.md` defines rule-version, draw, prize-tier and experiment schemas.
- `research/HYPOTHESES.md` contains the first 13 explicit hypotheses plus anti-hypothesis controls.
- `src/loto_research/probability.py` implements exact hypergeometric/multi-pool probabilities, baseline EV helpers and an expected jackpot-sharing baseline.
- `tests/test_probability.py` contains regression tests for Beşdə 5, Super Keno, 4+4, Powerball, Mega Millions and sharing math.
- Local regression run on 2026-08-11: **8 tests passed**. No GitHub Actions workflow was enabled.
- `research/azerbaijan_baseline.md` contains the first exact economic baseline.

## Current findings
### Beşdə 5
Using the current published 5/36 prize table and treating the 50,000 AZN top prize as fully paid on every 5-match variant (a favorable upper-bound assumption):
- exact 5-match odds: **1 in 376,992**;
- gross expected payout per 1 AZN variant: **0.535555131 AZN**;
- baseline net EV before tax/sharing: **-0.464444869 AZN** (~-46.44%).

Actual EV can be lower because the official rule splits a total 100,000 AZN among 3+ top-winning variants and taxes can apply.

### Super Keno
Using the displayed base 1-AZN prize table (10 selected from 70, 20 drawn):
- exact gross expected payout: **0.598555794 AZN**;
- baseline net EV before tax: **-0.401444206 AZN** (~-40.14%).

The official page advertises up to 1,000,000 AZN while showing 100,000 AZN as the base 10-match tier; published multiplier mechanics appear to account for the difference. Multiplier pricing still needs full normalization.

### Research interpretation
- No profitable strategy has been validated yet.
- The local baseline gaps are large enough that ordinary hot/cold-number pattern hunting would need a very strong, reproducible predictive edge to become economically relevant.
- Structural payout rules, promotions, sharing, multiplier pricing, roll-downs and implementation anomalies remain higher-priority targets.

## In progress
- Exact prize/EV model for 4+4.
- Super Keno multiplier/stake normalization.
- Discovery of official historical-results/API endpoints for automated ingestion.
- Historical Cash WinFall reconstruction from primary Massachusetts material.
- Current Must Be Won / roll-down comparison.

## Next actions
1. Capture 4+4 full prize table and compute exact EV.
2. Discover Azərlotereya archive network/API calls and build first collector.
3. Download/normalize Beşdə 5, 4+4 and Super Keno historical draws.
4. Add rule-version-aware draw validation tests.
5. Reconstruct Cash WinFall economics as a known positive-EV benchmark.
6. Build progressive jackpot threshold model including sales-dependent winner sharing.
7. Add instant/scratch games where official batch size and prize fund are published.

## Handoff rule
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md` when code work is involved, then verify the factual state of `research-work` in GitHub before continuing.
