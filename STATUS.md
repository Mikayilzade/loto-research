# STATUS

Updated: 2026-08-11
Branch: `research-work`

## Current stage
**Stage 1 — universe, exact baselines, rule-versioning and structural-edge search**

## Completed foundation
- `START_HERE.md`, `PROJECT_RULES.md`, `AGENTS.md`, `RESEARCH_PLAN.md` establish handoff, scientific standards and engineering rules.
- `catalog/games.csv` and `catalog/sources.csv` hold the first game/source universe with rule-version notes.
- `schemas/DATA_MODEL.md` defines normalized game/rule/draw/prize/experiment data.
- `research/HYPOTHESES.md` contains H001–H016 plus anti-hypothesis controls.
- `src/loto_research/probability.py` implements exact combinatorial probability/EV helpers.
- `src/loto_research/collectors/azerbaijan.py` validates/normalizes Beşdə 5, 4+4 and Super Keno draw records.
- `src/loto_research/uk_lotto.py` explicitly separates pre-June-2026 one-round UK Lotto from the current two-round regime and now adds assumption-driven jackpot-growth sales proxies plus carryover break-even screening.
- Regression tests exist in `tests/test_probability.py`, `tests/test_azerbaijan_collector.py`, `tests/test_uk_lotto.py`. GitHub Actions remains disabled. Earlier baseline suite had 8 passing tests; newest UK-regime/sales-proxy tests have not been run in Actions, although critical numeric expectations were independently recomputed during research.

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

The free-bet prize is intentionally valued at zero. H001 is historically validated as a mechanism class: structural redistribution can create +EV without predicting winning numbers.

### UK Lotto — rule boundary and current format
The old one-round regime ended with 6 June 2026. Allwyn confirms that from 10 June 2026 each £2 line enters **two separate 6/59 rounds**, the jackpot is shared across both rounds, draws remain Wednesday/Saturday, jackpots start at £2m and can roll up to five times before a Must Be Won event on the sixth draw.

Exact two-round combinatorics:
- any-prize probability: **0.204956584524**;
- odds: **1 in 4.879082086**.

Contemporary result archives show regular lower tiers of £1m / £1,000 / £50 / £10 / £1 for Match5+Bonus through Match2. Using those observed values:
- non-jackpot fixed cash EV: **£0.728983386863 per £2 ticket**.

### UK Lotto — Saturday Must Be Won evidence
18 July 2026:
- advertised jackpot: **£9,559,451**;
- no Match6 winner in either round -> rolldown;
- realized uniform-line payout-schedule EV: **£1.533679184945 per £2 ticket**, negative.

8 August 2026 reached the sixth draw of the next captured cycle, but rolldown was avoided because **two Match6 tickets** won and shared the **£8,535,146** jackpot.

So current captured sixth draws are Saturday-aligned and have not produced a validated +EV opportunity.

### New sales-response work
`data/historical/uk_lotto_sales_proxy_2026.csv` stores 15 current-regime rollover jackpot increments from 13 June through 8 August 2026.

Screening assumption:
- old primary procedures allocate 9.79% of sales to the jackpot;
- a current independent Lotto Q&A also reports 9.79% continuing after the 2026 redesign;
- updated primary 2026 procedures confirming that percentage have NOT yet been captured.

Under that explicit assumption, jackpot growth implies a strong weekday demand pattern:
- Wednesday proxy: mean **~5.008m**, median **~5.084m**, range **~4.661m–5.233m** tickets;
- Saturday proxy: median **~8.580m** tickets;
- non-raffle Saturday median **~8.483m**;
- 4 July Millionaire Raffle proxy: **~10.53m**, showing promotion state can materially change demand.

Match2 winner counts are retained only as a noisy secondary proxy: large Round1/Round2 differences despite identical sold selections demonstrate that non-uniform player choices materially affect realized category winner counts.

### H016 — Wednesday Must Be Won calendar edge
This is now the highest-priority current-game lead.

Because draws alternate Wednesday/Saturday and the sixth draw is Must Be Won, a jackpot cycle that begins on **Saturday** can place its sixth draw on **Wednesday**.

Using the current observed fixed-prize baseline and the 9.79% sales-allocation screening assumption:
- break-even requires inherited carryover/current-sales >= **~£1.0752166 per ticket**;
- a median observed alternating path from a £2m Saturday reset implies prior carryover before a Wednesday sixth draw of **~£7.313m**;
- this gives a screening break-even maximum of **~6.801m current tickets**;
- ordinary Wednesday sales proxies observed so far are only **~4.66m–5.23m**, median **~5.08m**;
- at that median, the simple aggregate screen would imply roughly **£2.36 gross value per £2 ticket**.

This is NOT validated +EV. The decisive uncertainty is Must-Be-Won-specific Wednesday demand: advertising could lift sales by enough to erase the gap. Relative to the ordinary-Wednesday median, the screening threshold allows about **34% sales uplift** before break-even disappears.

Full derivation: `research/uk_lotto_sales_response_2026.md`.
H016 status: **promising current-game lead; no current-regime Wednesday Must Be Won sample yet**.

### H015 — lower-tier crowd-sharing lead
Large two-round differences in Match2 winner counts provide direct evidence that non-uniform player number choices materially change realized winner counts. This strengthens the case for modelling number-popularity avoidance in shared rolldown categories, but the economic magnitude remains untested.

## Data-collection status
- Azərlotereya current-results page is crawlable.
- official Beşdə 5 / 4+4 archive pages are client-rendered; underlying official historical API/network call remains undiscovered.
- secondary 4+4 history can be used for reconstruction only after reconciliation.
- UK Lotto 2025 and 2026 are stored as separate rule regimes.
- `data/historical/uk_lotto_must_be_won_2025.csv` stores four old-regime rolldowns.
- `data/historical/uk_lotto_must_be_won_2026.csv` stores the 18 July 2026 current-regime rolldown sample.
- `data/historical/uk_lotto_sales_proxy_2026.csv` stores the first current-regime jackpot-growth demand series.
- `research/uk_lotto_regime_2026.md` documents the current format.
- `research/uk_lotto_sales_response_2026.md` documents the weekday/promotion sales pattern and H016.

## Research interpretation
- **No currently executable +EV strategy has been validated yet.**
- Historical Cash WinFall proves the target mechanism is real.
- H016 is the first current-game state found whose screening economics can cross above ticket cost under observed ordinary-demand levels.
- The edge, if real, comes from inherited prize money meeting a smaller crowd — not from predicting numbers.
- Sales response, promotions, current-rule verification and category sharing are now more important than additional jackpot-only calculations.
- Azerbaijan 4+4 remains the highest-priority local structural target.

## Next actions
1. Find/capture the updated primary UK Lotto 2026 procedures/player leaflet, especially current jackpot allocation and Must Be Won redistribution/capping rules.
2. Search for any current-regime or comparable historical **Wednesday Must Be Won** draw and test H016 out-of-sample.
3. Build a full 2026 draw/cycle dataset and estimate Must-Be-Won-specific sales uplift versus ordinary Wednesday/Saturday demand.
4. Build a conservative **pre-draw** trigger using an upper confidence bound on final sales and lower bound on distributable carryover.
5. Quantify H015 with a crowd number-choice/collision model.
6. Verify 4+4 exact per-variant price and detailed prize-fund allocation.
7. Reconstruct 50–100+ consecutive 4+4 payout states and infer carryover equations.
8. Discover/ingest the official Azərlotereya historical API or payload.
9. Normalize Super Keno multiplier economics.
10. Add scratch/instant games where remaining-prize/inventory data can support state-dependent EV.

## Handoff rule
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md` when code work is involved, then verify the factual state of `research-work` in GitHub before continuing.
