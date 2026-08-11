# STATUS

Updated: 2026-08-12
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## Foundation / code
- `START_HERE.md`, `PROJECT_RULES.md`, `AGENTS.md`, `RESEARCH_PLAN.md` define handoff and research standards.
- `catalog/games.csv`, `catalog/sources.csv`, `schemas/DATA_MODEL.md` define the first research universe and data model.
- `research/HYPOTHESES.md` contains H001–H016 plus anti-hypothesis controls.
- `src/loto_research/probability.py` contains exact combinatorial probability/EV helpers.
- `src/loto_research/collectors/azerbaijan.py` validates/normalizes Azerbaijan draw records.
- `src/loto_research/uk_lotto.py` separates old/current UK Lotto regimes and includes Must-Be-Won screening helpers.
- **NEW:** `src/loto_research/four_plus_four.py` contains empirical 4+4 pool-unit reconstruction helpers.
- **NEW:** `tests/test_four_plus_four.py` adds regression expectations for the discovered 4+4 payout structure.
- GitHub Actions remains disabled; critical new numeric identities were independently recomputed during the research pass.

## Validated / strong findings
### Cash WinFall historical benchmark
Historical structural +EV is real in principle. A preserved May 9, 2011 roll-down gives, using exact 6/46 probabilities and cash-only tiers:
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
- probability of any listed winning state: **18.614724%** (~1 in 5.3721);
- operator publicly displays **2 AZN ticket price**.

Official jackpot evidence includes a 250k reset after a win and historical jackpot states above 1m / 1.3m. Jackpot-only EV remains too small to explain a profitable ordinary state.

### NEW — hidden lower-tier payout engine found
Six preserved 2026 draw tables are stored in:
- `data/historical/az_4plus4_payout_samples_2026.csv`

Detailed derivation:
- `research/4plus4_economics_inference.md`

For sampled draws 772, 774, 776, 777, 795 and 796, categories III, IV, VII, VIII and IX follow an almost exact common-unit structure:
- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**

Additionally:
- V + VI = **2U**

So categories III–IX together distribute approximately **48U** per draw when those pools are paid.

The V/VI split changes materially while their combined total stays near 2U, proving these two categories are coupled by an internal allocation mechanism rather than simple independent fixed prizes.

### NEW — strong 2-AZN-per-variant inference
Observed fixed tail prizes remain:
- category X (2+2): **6 AZN**;
- category XI (2+1 / 1+2): **4 AZN**.

Their exact probabilities imply a fixed-tail EV contribution of:
- **0.682149737849 AZN per variant**.

The observed common pool unit U is strongly consistent with:
- `U ≈ 0.01 × sold_variants`.

That is equivalent to U being ~0.5% of gross sales if one base variant costs 2 AZN. The variant counts inferred this way closely match winner-count expectations for categories X/XI across most sampled draws.

Therefore **one base variant costing 2 AZN is now a high-confidence inference**, matching the operator's public 2-AZN ticket price. It is not yet promoted to primary-source fact until detailed rules, purchase flow or a receipt explicitly confirms it.

A 1-AZN variant interpretation is economically inconsistent with the observed lower-tier payouts in the sampled draws.

### NEW — ordinary 4+4 economics are less mysterious
Under the working U scaling:
- categories III–IX contribute about **0.48 AZN per 2-AZN variant** in aggregate;
- categories X/XI contribute exactly about **0.68215 AZN** in expectation;
- subtotal before category II and jackpot: **~1.16215 AZN / 2 AZN**, about **58.11% gross return**.

This means the ordinary draw remains strongly negative. Variable payout-per-winner values are mostly explained by a stable pool formula + changing winner counts, not by a free-standing exploitable anomaly.

### H014 revised
H014 remains **testing**, but the target is narrower.

Old interpretation: variable payouts themselves might indicate carryover edge.

New interpretation:
- ordinary III–IX variation is mostly explained by the stable U-engine;
- the decisive edge question is what happens when a low-probability variable category has **zero winners**;
- we need to determine whether its assigned pool carries to the same category, moves to another category/jackpot, or is redistributed immediately;
- only a balance observable before the next purchase can become a strategy signal.

## UK Lotto result
H016 Wednesday Must Be Won calendar edge was stress-tested and downgraded.
- initial allowable demand uplift: ~+33.77%;
- seven historical Wednesday Must-Be-Won analogues show jackpot-growth demand uplift median **+42.85%**;
- historical demand response exceeds the screen in 6/7 observations;
- H016 status: **inconclusive / materially weakened**.

H015 crowd-choice/sharing remains theoretically interesting but unquantified.

## Data collection blockers
- Azərlotereya current results are crawlable.
- official 4+4 / Beşdə 5 archive pages are client-rendered; the underlying historical API/network payload is still undiscovered.
- secondary archives can be used for reconstruction, but primary reconciliation is required before authoritative status.

## Next actions
1. Expand `az_4plus4_payout_samples_2026.csv` toward **50–100 consecutive draws**, prioritizing draws with zero winners in categories II–VI.
2. Infer t→t+1 pool transitions to identify true carryover/redistribution rules.
3. Find direct primary confirmation of **2 AZN per base 4+4 variant** and the registered detailed prize-fund rules.
4. Discover the official Azərlotereya historical API/payload and reconcile the secondary sample.
5. Estimate full ordinary 4+4 EV including category II and jackpot once their exact allocation/payment mechanics are confirmed.
6. Quantify H015 crowd-choice/sharing after the 4+4 state-transition pass.
7. Normalize Super Keno multiplier economics.
8. Add scratch/instant games with remaining-prize/inventory state.
9. Continue Powerball / Mega Millions / EuroMillions threshold work with demand/sharing response included from the start.

## Handoff rule
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md` when code work is involved, then verify the factual state of `research-work` before continuing.
