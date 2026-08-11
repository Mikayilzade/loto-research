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
- `catalog/sources.csv` records official/primary sources and now includes current UK Lotto Must Be Won mechanics, preserved rolldown samples and additional official 4+4 jackpot-state evidence.
- `schemas/DATA_MODEL.md` defines rule-version, draw, prize-tier and experiment schemas.
- `research/HYPOTHESES.md` now contains H001–H015 plus anti-hypothesis controls.
- `src/loto_research/probability.py` implements exact hypergeometric/multi-pool probabilities, 4+4 grouped category probabilities, baseline EV helpers and an expected jackpot-sharing baseline.
- `src/loto_research/uk_lotto.py` implements exact UK Lotto probabilities, crowd-average Must Be Won break-even math, historical sales estimation from category winner counts and published rolldown-schedule diagnostics.
- `tests/test_probability.py`, `tests/test_azerbaijan_collector.py` and `tests/test_uk_lotto.py` contain regression tests. GitHub Actions remains disabled. The newest tests have not been run through GitHub Actions; critical numeric expectations were independently cross-checked during the research pass.
- `src/loto_research/collectors/azerbaijan.py` adds source-independent validation/normalization for Beşdə 5, 4+4 and Super Keno draw records.
- `research/azerbaijan_baseline.md` contains the first exact local economic baseline.
- `research/4plus4_baseline.md` contains the exact 4+4 probability model, variable lower-tier payout lead and official jackpot-state observations.
- `research/cash_winfall_benchmark.md` reproduces a historical positive-EV roll-down benchmark conservatively from cash-only prize tiers.
- `research/uk_lotto_must_be_won.md` models a current forced-redistribution game and tests preserved 2025 rolldown examples.
- `data/historical/uk_lotto_must_be_won_2025.csv` stores four preserved 2025 UK Lotto rolldown schedules for further modelling.

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

New official state evidence:
- 530,359 AZN jackpot won on 2026-07-28;
- next jackpot reset to 250,000 AZN;
- prior 913,072 AZN jackpot referenced by the operator;
- official reports document >1,000,000 AZN and >1,300,000 AZN jackpot states.

Because jackpot odds are 1 / 23,474,025, jackpot-only EV contribution is only about 0.01065 AZN at 250k and 0.05538 AZN at 1.3m before tax/sharing. The lower-category allocation/carryover system is therefore the higher-priority 4+4 lead.

### Cash WinFall benchmark
Historical Cash WinFall demonstrates the mechanism class we seek: jackpot roll-down redistribution made specific draws positive EV without predicting winning numbers.

For the preserved May 9, 2011 roll-down payouts, using exact 6/46 probabilities and **cash-only** tiers (5 matches $24,821; 4 matches $824; 3 matches $26):
- expected cash payout on a $2 ticket: **$2.2137120403**;
- conservative net EV: **+$0.2137120403**;
- conservative expected ROI: **+10.6856%** before tax/execution costs;
- the 2-match free-bet prize is intentionally valued at zero in this conservative benchmark.

H001 is therefore historically validated as a mechanism class.

### UK Lotto Must Be Won
Current official procedures establish a real forced-redistribution mechanism: the jackpot can roll five times; on an unwon fifth rollover, Match 2 gets £5 cash plus the normal Lucky Dip and the remaining jackpot goes 3% / 5% / 7% / 85% to Match 5+Bonus / Match 5 / Match 4 / Match 3.

Exact ordinary fixed cash EV excluding Match 6 and the Match 2 Lucky Dip is:
- **£0.521453999 per £2 line**.

For a crowd-average Must Be Won benchmark, if J is the jackpot and N sold entries, the accumulated jackpot contributes roughly J/N of aggregate value per sold entry. Cash-only break-even therefore requires:
- **J/N >= £1.478546001 per entry**.

A generous model valuing every Match 2 Lucky Dip at its full £2 retail face value lowers the break-even ratio only to:
- **J/N >= £1.283578347 per entry**.

Historical 2025 rolldowns tested so far were still negative because sales rose with the advertised jackpot. For 2025-07-05:
- jackpot: £15m;
- Match 2 winners: 1,522,131;
- simple Match-2-based sales estimate: ~15.614m lines;
- jackpot / estimated entries: ~£0.9607;
- published rolldown cash schedule EV for a uniform fixed line: ~**£1.4371**;
- adding the full £2 face value of the Lucky Dip gives only ~**£1.6320**, still below the £2 ticket cost;
- cash-only break-even at that estimated crowd size would require roughly **£23.09m** jackpot.

Conclusion: **Must Be Won is not automatically +EV.** The correct trigger must include both jackpot size and sales/crowd response.

### New H015 lead — lower-tier crowd sharing
In a rolldown, lower-category funds are divided among actual winners. Therefore number-popularity avoidance may affect Match 3/4/5 sharing as well as jackpot sharing. This is potentially important because 85% of the residual UK Lotto rolldown jackpot is allocated to Match 3. The theoretical mechanism is plausible; empirical magnitude is not yet known.

## Data-collection status
- Official current Azərlotereya results page is crawlable.
- Official historical archive pages exist for Beşdə 5 and 4+4 but currently render draw data client-side; crawler-visible HTML shows `Tiraj undefined`.
- The underlying official historical-results API/network call has not yet been discovered.
- Do not hard-code a guessed endpoint. Future adapters must feed raw source data through `collectors/azerbaijan.py` validation.
- A secondary 4+4 archive is useful for reconstruction but must be reconciled against official results before normalized data is promoted to authoritative status.
- UK Lotto official procedures are primary authority for mechanics; historical 2025 rolldown payout schedules currently use preserved secondary archive pages and should be reconciled with any recoverable official historical snapshots.

## Research interpretation
- No current profitable strategy has yet been validated.
- Historical Cash WinFall proves that structural +EV is possible without predicting draw numbers.
- Current UK Lotto analysis shows why jackpot-size-only heuristics fail: player demand rises with jackpot size and can erase the overlay.
- Local fixed-prize baselines remain strongly negative; ordinary hot/cold-number hunting is low priority unless a reproducible physical/RNG mechanism survives forward testing.
- 4+4 remains a live local research lead because lower-tier payouts appear state-dependent, but its jackpot by itself is economically too small to create a large edge at observed levels.
- Crowd-choice/sharing, promotions, carryovers, multiplier pricing, inventory state and execution anomalies remain higher priority than number-frequency pattern hunting.

## In progress
- Verify exact 4+4 per-variant price and rule-version prize-fund allocation from an official source or purchase artifact.
- Discover official Azərlotereya historical-results network/API calls.
- Reconstruct 50–100+ consecutive 4+4 draw payout states and infer carryover/allocation equations.
- Build UK Lotto pre-draw sales-response model from historical jackpot, winner-count and rolldown data.
- Quantify H015 with a player number-choice / collision model.
- Super Keno multiplier/stake normalization.
- Scratch/instant-game remaining-prize denominator research.

## Next actions
1. Expand UK Lotto Must Be Won dataset across multiple years and infer sales response N(J, weekday, promotions).
2. Model a pre-draw decision threshold using conservative confidence bounds on final sales, not post-draw winner counts.
3. Build a crowd number-choice model and estimate whether anti-popularity selections can improve lower-tier rolldown sharing enough to matter.
4. Obtain/verify 4+4 official detailed rules and exact per-variant pricing.
5. Reconstruct 4+4 prize-pool state transitions from 50–100+ consecutive draws and test H014.
6. Build first real Azərlotereya history adapter once the official archive payload/API is identified.
7. Add instant/scratch games where official batch size and prize fund are published, then search for remaining-inventory data.
8. Continue progressive-jackpot threshold work for Powerball / Mega Millions / EuroMillions with sales-dependent sharing.

## Handoff rule
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md` when code work is involved, then verify the factual state of `research-work` in GitHub before continuing.
