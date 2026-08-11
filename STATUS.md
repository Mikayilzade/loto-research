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
- `src/loto_research/uk_lotto.py` separates pre-June-2026 one-round UK Lotto from the current two-round regime and includes assumption-driven jackpot-growth sales proxies plus carryover break-even screening.
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
- multiplier economics still require full normalization.

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

### UK Lotto — current two-round regime
From 10 June 2026 each £2 line enters two separate 6/59 rounds; jackpot is shared across both rounds and the sixth draw of an uninterrupted cycle is Must Be Won.

Exact two-round any-prize probability:
- **0.204956584524**, or **1 in 4.879082086**.

Observed current fixed lower tiers imply non-jackpot cash EV:
- **£0.728983386863 per £2 ticket**.

Captured Saturday sixth-draw states remain unattractive:
- 18 July 2026 rolldown realized uniform-line schedule EV ~**£1.5337 / £2**;
- 8 August 2026 reached the sixth draw but two Match6 tickets won the jackpot, so no rolldown occurred.

### UK Lotto 2026 demand proxy
`data/historical/uk_lotto_sales_proxy_2026.csv` contains 15 current-regime rollover jackpot increments.

Under the explicit 9.79% jackpot-allocation assumption:
- ordinary Wednesday median demand proxy ~**5.084m** tickets;
- non-raffle Saturday median ~**8.483m**;
- promotions materially change demand (4 July raffle proxy ~10.53m).

### H016 — Wednesday Must Be Won calendar edge: downgraded
Initial current-regime screen:
- median-path inherited carryover before hypothetical Wednesday sixth draw ~**£7.313m**;
- break-even max current sales ~**6.801m**;
- ordinary Wednesday median ~**5.084m**;
- apparent allowable demand uplift before break-even: **~+33.77%**.

Historical stress test now stored in:
- `data/historical/uk_lotto_wednesday_mbw_stress_old_regime.csv`
- `research/uk_lotto_wednesday_mbw_stress_test.md`

Seven natural old-regime Wednesday sixth-draw states from 2023–2026 show jackpot-growth demand-proxy uplift relative to the previous ordinary Wednesday in the same cycle:
- mean **+40.97%**;
- median **+42.85%**;
- range **+33.12% to +46.18%**.

The historical uplift exceeds the current +33.77% screening cushion in **6 of 7** observations. Applying the historical median uplift to current ordinary-Wednesday demand projects ~**7.263m** tickets, above the ~6.801m break-even screen. The simple aggregate value falls to roughly **£1.93 / £2**. An independent but noisier Match2 proxy points in the same direction (median uplift ~+41.26%).

Conclusion: **H016 is now `inconclusive / materially weakened`; calendar effect alone is not a promising +EV trigger.** It remains open only because old/new rule regimes differ and no current-regime Wednesday Must Be Won sample exists yet.

### H015 — lower-tier crowd-sharing lead
Large two-round differences in Match2 winner counts provide direct evidence that non-uniform player number choices materially change realized category winner counts. This strengthens the case for modelling number-popularity avoidance in shared rolldown categories, but economic magnitude remains untested.

## Data-collection status
- Azərlotereya current-results page is crawlable.
- official Beşdə 5 / 4+4 archive pages are client-rendered; underlying official historical API/network call remains undiscovered.
- secondary 4+4 history can be used for reconstruction only after reconciliation.
- UK Lotto 2025 and 2026 are stored as separate rule regimes.
- `data/historical/uk_lotto_must_be_won_2025.csv` stores old-regime rolldowns.
- `data/historical/uk_lotto_must_be_won_2026.csv` stores the 18 July 2026 current-regime rolldown sample.
- `data/historical/uk_lotto_sales_proxy_2026.csv` stores current-regime jackpot-growth demand proxies.
- `data/historical/uk_lotto_wednesday_mbw_stress_old_regime.csv` stores the old-regime Wednesday stress sample.
- `research/uk_lotto_regime_2026.md`, `research/uk_lotto_sales_response_2026.md`, and `research/uk_lotto_wednesday_mbw_stress_test.md` document the current UK work.

## Research interpretation
- **No currently executable +EV strategy has been validated yet.**
- Historical Cash WinFall proves structural +EV is real in principle.
- The UK Lotto pass demonstrated a useful failure mode: an overlay that looks attractive under ordinary demand can be competed away by the demand response to the overlay itself.
- H016 should not be pursued further from the same small dataset; keep it available for future current-regime evidence.
- H015 crowd-choice/sharing and Azerbaijan 4+4 lower-tier carryover now rank above H016.
- Promotions, remaining-inventory states and other inefficiently competed structural overlays remain high priority.

## Next actions
1. Return to Azerbaijan **4+4**: verify exact per-variant price and detailed lower-tier prize-fund/carryover rules.
2. Reconstruct 50–100+ consecutive 4+4 payout states and infer state-transition equations.
3. Quantify H015 with a crowd number-choice/collision model, using current UK two-round winner-count asymmetries as calibration evidence.
4. Find/capture updated primary UK Lotto 2026 procedures; revisit H016 only when genuinely new current-regime evidence appears.
5. Discover/ingest the official Azərlotereya historical API or payload.
6. Normalize Super Keno multiplier economics.
7. Add scratch/instant games where remaining-prize/inventory data can support state-dependent EV.
8. Continue Powerball / Mega Millions / EuroMillions threshold work with demand and sharing response included from the start.

## Handoff rule
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md` when code work is involved, then verify the factual state of `research-work` in GitHub before continuing.
