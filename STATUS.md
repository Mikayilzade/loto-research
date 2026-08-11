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
- `research/HYPOTHESES.md` now contains H001–H014 plus anti-hypothesis controls.
- `src/loto_research/probability.py` implements exact hypergeometric/multi-pool probabilities, 4+4 grouped category probabilities, baseline EV helpers and an expected jackpot-sharing baseline.
- `tests/test_probability.py` contains exact probability regression tests for Beşdə 5, Super Keno, 4+4, Powerball, Mega Millions and sharing math.
- `src/loto_research/collectors/azerbaijan.py` adds source-independent validation/normalization for Beşdə 5, 4+4 and Super Keno draw records.
- `tests/test_azerbaijan_collector.py` adds validation tests for canonicalization, duplicates, range errors, count errors and board structure.
- Previous local regression run before the newest additions: **8 tests passed**. GitHub Actions remains disabled. The newly added tests have not been represented as a GitHub Actions run.
- `research/azerbaijan_baseline.md` contains the first exact local economic baseline.
- `research/4plus4_baseline.md` contains the exact 4+4 probability model and the new state-dependent payout lead.
- `research/cash_winfall_benchmark.md` reproduces a historical positive-EV roll-down benchmark conservatively from cash-only prize tiers.

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

### 4+4
Official mechanics establish two independent 4-from-20 boards with 11 prize categories.
- exact jackpot odds: **1 in 23,474,025**;
- exact probability of any listed winning match-state: **0.186147241472223** (~18.6147%, 1 in 5.3721).

Important unresolved economic parameter: the official public page displays **2 AZN ticket price** but does not explicitly state one-variant price. Do not assume 1 AZN by analogy with Beşdə 5.

Secondary historical archives show materially variable per-winner payouts in categories III–IX across recent draws. This suggests a state-dependent/pari-mutuel or carryover model and makes H014 a high-priority target. It is not yet a profitability result.

### Cash WinFall benchmark
Historical Cash WinFall demonstrates the mechanism class we seek: jackpot roll-down redistribution made specific draws positive EV without predicting winning numbers.

For the preserved May 9, 2011 roll-down payouts, using exact 6/46 probabilities and **cash-only** tiers (5 matches $24,821; 4 matches $824; 3 matches $26):
- expected cash payout on a $2 ticket: **$2.2137120403**;
- conservative net EV: **+$0.2137120403**;
- conservative expected ROI: **+10.6856%** before tax/execution costs;
- the 2-match free-bet prize is intentionally valued at zero in this conservative benchmark.

H001 is therefore historically validated as a mechanism class. No current exploitable game has yet been validated.

## Data-collection status
- Official current-results page is crawlable.
- Official historical archive pages exist for Beşdə 5 and 4+4 but currently render draw data client-side; crawler-visible HTML shows `Tiraj undefined`.
- The underlying official historical-results API/network call has not yet been discovered.
- Do not hard-code a guessed endpoint. Future adapters must feed raw source data through `collectors/azerbaijan.py` validation.
- A secondary 4+4 archive is useful for reconstruction but must be reconciled against official results before normalized data is promoted to authoritative status.

## Research interpretation
- No current profitable strategy has been validated yet.
- Local fixed-prize baselines are strongly negative; ordinary hot/cold-number hunting is a low-priority path unless a reproducible physical/RNG mechanism survives forward testing.
- Structural payout rules, carryovers, promotions, sharing, multiplier pricing, inventory state and execution anomalies remain the highest-priority targets.
- 4+4 is now more interesting than the initial fixed-prize model because its lower-tier payout values appear draw-dependent.

## In progress
- Verify exact 4+4 per-variant price and rule-version prize-fund allocation from an official source or purchase artifact.
- Discover official Azərlotereya historical-results network/API calls.
- Reconstruct 50–100+ consecutive 4+4 draw payout states and infer carryover/allocation equations.
- Super Keno multiplier/stake normalization.
- Current Must Be Won / roll-down comparison.
- Scratch/instant-game remaining-prize denominator research.

## Next actions
1. Obtain/verify 4+4 official detailed rules and exact per-variant pricing.
2. Build first real history adapter once the official archive payload/API is identified.
3. Reconcile secondary 4+4 draws against official draw numbers/dates/numbers.
4. Reconstruct prize-pool state transitions and estimate forward-observable 4+4 EV thresholds.
5. Add rule-version-aware draw validation and source-confidence fields.
6. Model UK Lotto Must Be Won as the first current forced-redistribution comparator.
7. Build progressive jackpot threshold model including sales-dependent winner sharing.
8. Add instant/scratch games where official batch size and prize fund are published, then search for remaining-inventory data.

## Handoff rule
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md` when code work is involved, then verify the factual state of `research-work` in GitHub before continuing.
