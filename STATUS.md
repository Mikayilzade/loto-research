# STATUS

Updated: 2026-08-12
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## Foundation / code
- `START_HERE.md`, `PROJECT_RULES.md`, `AGENTS.md`, `RESEARCH_PLAN.md` define handoff and research standards.
- `catalog/games.csv`, `catalog/sources.csv`, `schemas/DATA_MODEL.md` define the first research universe and data model.
- `research/HYPOTHESES.md` contains H001–H016 and has been updated for the revised 4+4 H014 interpretation.
- `src/loto_research/probability.py` contains exact combinatorial probability/EV helpers.
- `src/loto_research/collectors/azerbaijan.py` validates/normalizes Azerbaijan draw records.
- `src/loto_research/uk_lotto.py` separates old/current UK Lotto regimes and includes Must-Be-Won screening helpers.
- `src/loto_research/four_plus_four.py` now reconstructs the 4+4 common pool unit, V/VI coupling and independent variant-volume estimates from tail winners.
- `tests/test_four_plus_four.py` includes fitted-sample checks plus draw #790 as a first out-of-sample payout-engine check.
- GitHub Actions remains disabled; critical numeric identities were independently recomputed during this research pass.

## Validated / strong findings
### Cash WinFall historical benchmark
Structural +EV is historically real. A preserved May 9, 2011 roll-down gives, using exact 6/46 probabilities and cash-only tiers:
- ticket: $2;
- expected cash payout: **$2.2137120403**;
- expected ROI: **+10.6856%** before tax/execution costs.

### Azerbaijan — Beşdə 5
- exact 5/5 odds: **1 in 376,992**;
- favorable baseline gross payout: **0.535555131 AZN per 1-AZN variant**;
- baseline net before tax/sharing: about **-46.44%**.

### Azerbaijan — Super Keno
- displayed base-table gross EV: **0.598555794 AZN per 1 AZN**;
- baseline net before tax: about **-40.14%**;
- multiplier economics remain pending.

## Azerbaijan — 4+4: current priority
### Exact mechanics
- two independent 4/20 boards;
- 11 grouped winning categories;
- jackpot odds: **1 in 23,474,025**;
- any listed winning-state probability: **18.614724%** (~1 in 5.3721);
- operator publicly displays **2 AZN ticket price**.

The public page still does not provide a separate crawlable sentence explicitly stating the base-variant price. Treat 2 AZN per base variant as high-confidence inference until detailed primary rules or purchase evidence confirms it.

### Common lower-tier pool engine — strongly reconstructed
Seven preserved 2026 draw tables are now stored in:
- `data/historical/az_4plus4_payout_samples_2026.csv`

Detailed derivation:
- `research/4plus4_economics_inference.md`

For ordinary sampled draws, one common unit `U` explains variable categories:
- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Therefore III–IX jointly distribute approximately **48U**.

### First out-of-sample confirmation
The pool weights above were inferred before draw #790 was added.

Draw #790 independently gives:
- III/11 ≈ 417.582
- IV/5 ≈ 417.582
- VII/9 ≈ 417.662
- VIII/14 ≈ 417.703
- IX/7 = 417.600
- median U = **417.6**
- observed V+VI = **835.45** vs predicted 2U = **835.20**.

This materially reduces the risk that the common-unit structure is simple sample overfit.

### V/VI internal redistribution algorithm discovered
The combined V+VI pool remains ~2U.

Empirical rule across the current sample:
- if category-V winners <= category-VI winners, totals remain approximately **U / U**;
- if category V has more winners, the 2U pool is redistributed so that per-winner V payout is approximately **1.5×** per-winner VI payout.

For `w5 > w6`:
- `T5 = 2U × (1.5 w5)/(1.5 w5+w6)`
- `T6 = 2U - T5`.

Examples 776, 777 and 790 match within source rounding. Zero-winner cases are intentionally NOT extrapolated; those are the next research target.

### Independent U/N validation and 2-AZN inference
Observed fixed tail prizes in sampled tables:
- X (2+2): **6 AZN**;
- XI (2+1 / 1+2): **4 AZN**.

Exact probabilities allow sold-variant volume to be estimated independently from winner counts:
- `N_hat = (W10 + W11)/(P10 + P11)`.

Then `U/N_hat` across seven sampled draws is:
- mean **0.00996205 AZN per variant**;
- median **0.00995043**;
- range **0.00953821–0.01050994**.

Derived data:
- `data/derived/az_4plus4_pool_unit_validation.csv`.

So `U ≈ 0.01 × sold_variants` emerges empirically rather than from a chosen round number. If the base variant is 2 AZN, one U is about **0.5% of gross sales**, producing clean candidate allocation percentages (III 5.5%, IV 2.5%, V+VI 1%, VII 4.5%, VIII 7%, IX 3.5%). These percentages are inferred, not yet official-rule facts.

### Ordinary 4+4 economics
Exact X/XI expected payout:
- **0.682149737849 AZN per variant**.

With `48U` and empirical `U/N≈0.01`:
- III–IX ≈ **0.48 AZN / variant**;
- X/XI ≈ **0.68215 AZN / variant**;
- subtotal before category II and jackpot ≈ **1.16215 AZN per 2-AZN variant**;
- subtotal gross return ≈ **58.11%**.

The ordinary game is therefore still strongly negative. Floating per-winner payout values are mostly explained by the prize-engine formula and winner counts, not by a free-standing carryover opportunity.

### H014 — live question is now zero-winner carryover
H014 remains **testing**, but is much narrower:
- find draws where a variable low-probability category (especially II–VI) has zero winners;
- reconstruct its normal assigned amount from U;
- track t→t+1 and later draws;
- determine whether unpaid money carries in that category, transfers elsewhere, moves to jackpot/reserve, or is redistributed immediately;
- require any accumulated balance to be observable **before** ticket purchase.

Only then can a forward EV trigger exist.

## UK Lotto result
H016 Wednesday Must Be Won calendar edge was stress-tested and downgraded:
- initial allowable demand uplift ~+33.77%;
- seven historical analogues show median uplift **+42.85%**;
- historical response exceeds the screen in 6/7 cases;
- status: **inconclusive / materially weakened**.

H015 crowd-choice/sharing remains theoretically interesting but unquantified.

## Data collection blockers
- Azərlotereya current results are crawlable.
- official 4+4 / Beşdə 5 archive interfaces are client-rendered; the underlying historical API/network payload remains undiscovered.
- indexed secondary draw pages are incomplete and inconsistent in availability; reconstruction is possible but slower than a direct archive payload.
- secondary data must be reconciled against primary operator results before authoritative promotion.

## Next actions
1. Expand 4+4 history toward **50–100 consecutive draws**, prioritizing zero-winner II–VI states.
2. Infer t→t+1 pool transitions and either validate or kill the carryover part of H014.
3. Find direct primary confirmation of the 2-AZN base variant and detailed prize-fund allocation.
4. Discover the official Azərlotereya historical API/payload and reconcile the secondary dataset.
5. Capture a real category-II winner to identify whether II is fixed, pooled or carryover-based.
6. Estimate full ordinary 4+4 EV including II and jackpot once mechanics are confirmed.
7. Quantify H015 crowd-choice/sharing.
8. Normalize Super Keno multiplier economics.
9. Add scratch/instant games with remaining-prize/inventory state.
10. Continue Powerball / Mega Millions / EuroMillions threshold work with demand/sharing response included from the start.

## Handoff rule
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md` when code work is involved, then verify the factual state of `research-work` before continuing.
