# STATUS

Updated: 2026-08-11
Branch: `research-work`

## Current stage
**Stage 1 — universe, exact baselines, rule-versioning and structural-edge search**

## Completed foundation
- `START_HERE.md`, `PROJECT_RULES.md`, `AGENTS.md`, `RESEARCH_PLAN.md` establish handoff, scientific standards and engineering rules.
- `catalog/games.csv` and `catalog/sources.csv` hold the first game/source universe with rule-version notes.
- `schemas/DATA_MODEL.md` defines normalized game/rule/draw/prize/experiment data.
- `research/HYPOTHESES.md` contains H001–H015 plus anti-hypothesis controls.
- `src/loto_research/probability.py` implements exact combinatorial probability/EV helpers.
- `src/loto_research/collectors/azerbaijan.py` validates/normalizes Beşdə 5, 4+4 and Super Keno draw records.
- `src/loto_research/uk_lotto.py` now explicitly separates the pre-June-2026 one-round UK Lotto regime from the current two-round regime.
- Regression tests exist in `tests/test_probability.py`, `tests/test_azerbaijan_collector.py`, `tests/test_uk_lotto.py`. GitHub Actions remains disabled. Earlier baseline suite had 8 passing tests; newest UK-regime tests have not been run in Actions, although their critical numeric expectations were independently recomputed during this research pass.

## Current findings
### Azerbaijan — Beşdə 5
- 5/36; one variant 1 AZN, ticket minimum 2 AZN.
- exact 5/5 odds: **1 in 376,992**.
- favorable gross baseline: **0.535555131 AZN per 1 AZN variant**.
- net baseline before tax/sharing: about **-46.44%**.

### Azerbaijan — Super Keno
- choose 10/70; 20 drawn.
- displayed base-table gross EV: **0.598555794 AZN per 1 AZN**.
- net baseline before tax: about **-40.14%**.
- multiplier mechanics still require full normalization.

### Azerbaijan — 4+4
- two independent 4/20 boards; 11 winning match groups.
- jackpot odds: **1 in 23,474,025**.
- probability of any listed winning state: **18.614724%** (~1 in 5.3721).
- public ticket price is 2 AZN; exact per-variant price remains unverified.
- official jackpot-state evidence includes 250k reset, 530,359 AZN win, prior 913,072 AZN win, and >1m / >1.3m jackpot states.
- jackpot-only EV contribution is small (about 0.01065 AZN at 250k; 0.05538 AZN at 1.3m), so the higher-priority lead is the variable lower-category allocation/carryover mechanism.
- H014 status: **testing**.

### Cash WinFall historical benchmark
A preserved May 9, 2011 roll-down, using exact 6/46 probabilities and cash-only tiers, gives:
- ticket: $2;
- expected cash payout: **$2.2137120403**;
- net EV: **+$0.2137120403**;
- expected ROI: **+10.6856%** before tax/execution costs.

The free-bet prize is intentionally valued at zero. H001 is therefore historically validated as a mechanism class: structural redistribution can create +EV without predicting winning numbers.

### UK Lotto — pre-2026 historical regime
The one-round regime ended with the 6 June 2026 draw.
- old fixed cash EV excluding Match 6 and Match-2 Lucky Dip: **£0.521453999 per £2 line**.
- tested 2025 Must Be Won examples remained negative because sales surged with jackpot size.
- example 5 July 2025: £15m jackpot, estimated ~15.614m lines, realized schedule cash EV ~£1.4371; even valuing Lucky Dip at full £2 face gave ~£1.6320.

### UK Lotto — current two-round regime from 10 June 2026
Primary Allwyn sources confirm:
- one £2 line enters **two separate 6/59 rounds** every Wednesday/Saturday draw night;
- jackpot is shared across the two rounds;
- lower prizes are fixed cash prizes paid per round;
- Match 5+Bonus remains £1m;
- overall any-prize odds improve to about 1 in 4.9.

Exact combinatorics reproduce this:
- any-prize probability across two rounds: **0.204956584524**;
- odds: **1 in 4.879082086**.

Contemporary result archives consistently show regular lower tiers of £1m / £1,000 / £50 / £10 / £1 for Match 5+Bonus through Match 2. These are treated as observed secondary-source parameters until the updated primary procedures are captured.

Using those observed current lower tiers:
- non-jackpot fixed cash EV: **£0.728983386863 per £2 ticket**.

Current-regime Must Be Won example — 18 July 2026:
- advertised jackpot: **£9,559,451**;
- no Match 6 winner in either round;
- realized rolldown payouts: Match5 £1,000, Match4 £50, Match3 £24, Match2 £5; no Match5+Bonus winner;
- exact uniform-line post-draw payout-schedule EV: **£1.533679184945 per £2 ticket** -> negative;
- Match2 round-wins: 1,756,390 -> simple estimated sales **~9.009m tickets**;
- using observed regular fixed-prize baseline, crowd-average cash break-even at that crowd size is roughly **£11.450m jackpot**;
- actual jackpot was about **£1.89m below** that simple threshold.

Conclusion: the June-2026 redesign moves the economics, but **Must Be Won still does not automatically mean +EV**. Jackpot/overlay must be compared with final ticket volume and sharing.

### H015 — lower-tier crowd-sharing lead
In rolldowns, category funds are divided among actual winners. Unpopular number selections may therefore improve conditional sharing in Match3/4/5 as well as Match6. Mechanism is plausible; empirical magnitude remains untested.

## Data-collection status
- Azərlotereya current-results page is crawlable.
- official Beşdə 5 / 4+4 archive pages are client-rendered; underlying official historical API/network call remains undiscovered.
- do not hard-code guessed endpoints.
- secondary 4+4 history can be used for reconstruction only after reconciliation.
- UK Lotto 2025 and 2026 must be stored as separate rule regimes.
- `data/historical/uk_lotto_must_be_won_2025.csv` stores four old-regime rolldowns.
- `data/historical/uk_lotto_must_be_won_2026.csv` currently stores the 18 July 2026 current-regime rolldown sample.
- `research/uk_lotto_regime_2026.md` documents the current format and first threshold calculation.

## Research interpretation
- **No currently exploitable +EV strategy has been validated yet.**
- Historical Cash WinFall proves the target mechanism is real.
- Sales response is crucial: large advertised jackpots attract more tickets and can erase an apparent overlay.
- Current UK Lotto and Azerbaijan 4+4 are higher-priority structural targets than hot/cold-number pattern hunting.
- Promotions, carryovers, category sharing, multiplier pricing, scratch-ticket inventory state and implementation anomalies remain high priority.

## Next actions
1. Capture the updated primary UK Lotto 2026 procedures/player leaflet with exact lower-tier and Must Be Won rules.
2. Build a full post-10-June-2026 UK Lotto dataset and fit final-sales response vs jackpot/rollover/day/promotion state.
3. Create a **pre-draw** conservative EV trigger using confidence bounds on final sales rather than hindsight winner counts.
4. Quantify H015 with a crowd number-choice/collision model.
5. Verify 4+4 exact per-variant price and detailed prize-fund allocation.
6. Reconstruct 50–100+ consecutive 4+4 payout states and infer carryover equations.
7. Discover/ingest the official Azərlotereya historical API or payload.
8. Normalize Super Keno multiplier economics.
9. Add scratch/instant games where batch and remaining-prize information can support inventory-state EV.
10. Continue Powerball / Mega Millions / EuroMillions progressive-threshold work with sales-dependent sharing.

## Handoff rule
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md` when code work is involved, then verify the factual state of `research-work` in GitHub before continuing.
