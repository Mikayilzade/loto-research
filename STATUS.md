# STATUS

Updated: 2026-08-12
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## Work-session rule
Research runs in short packets. After every meaningful discovery or roughly 2–4 substeps:
1. save raw/derived data;
2. update the relevant research note;
3. update this file when the strategic conclusion changes.

This file is the authoritative handoff checkpoint. Read `START_HERE.md`, `PROJECT_RULES.md`, `RESEARCH_PLAN.md` and `AGENTS.md` before code work.

# Validated structural benchmark
## Cash WinFall
Historical 2011 roll-down benchmark using exact 6/46 probabilities and cash-only tiers:
- ticket: $2;
- expected payout: **$2.2137120403**;
- expected ROI: **+10.6856%** before tax/execution.

Conclusion: structural +EV lotteries have existed without predicting numbers.

# Azerbaijan baseline games
## Beşdə 5
- jackpot odds **1 in 376,992**;
- favorable gross baseline **0.535555131 AZN / 1-AZN variant**;
- net before tax/sharing about **-46.44%**.

## Super Keno — multiplier mechanics resolved
Files:
- `data/derived/az_superkeno_multiplier_ev.csv`
- `research/superkeno_multiplier_economics.md`

Current operator/FAQ material establishes:
- one variant can be paid at **1x / 2x / 5x / 10x**;
- without multiplier the top tier is **100,000 AZN**;
- at 10x the top tier is **1,000,000 AZN**;
- cost and prize table scale together, so the advertised 1m is not a free overlay.

Exact displayed-table gross EV remains **0.598555794263 AZN per 1 AZN** and scales linearly, so gross payout ratio is the same **59.8556%** at all multiplier choices.

Under the current tax formula, for a single variant / single draw and favorably assuming full top-prize ownership:
- 1x: **0.591807033508 / 1 AZN = 59.1807%**
- 2x: **1.182532310259 / 2 = 59.1266%**
- 5x: **2.945177937565 / 5 = 58.9036%**
- 10x: **5.869824724606 / 10 = 58.6982%**

Larger multipliers are slightly worse after tax because the 500-AZN deduction is fixed. Top-prize sharing is ignored in these favorable upper bounds and can only lower real EV.

Conclusion: **no Super Keno multiplier EV edge. Under risk-neutral after-tax ROI, 1x dominates absent a separate promotion.**

# Azerbaijan 4+4 — top local draw-game target, data-blocked for next state transition
## Exact/current mechanics
Primary operator page establishes:
- two independent 4/20 boards;
- 11 grouped winning categories;
- jackpot odds **1 in 23,474,025**;
- any listed winning state **18.614724%** (~1 in 5.3721);
- public ticket price **2 AZN**;
- registration no. **336 / 17.01.2021**, valid through 31.12.2027;
- 5+5 / 6+6 system entries generate multiple variants and can win multiple categories;
- current schedule **Tue/Fri 19:45**.

Direct primary wording for one base-variant price remains missing. `2 AZN/base variant` is a high-confidence empirical inference, not a direct rule fact.

## Strong draw-table payout engine
Files:
- `data/historical/az_4plus4_payout_samples_2026.csv`
- `data/derived/az_4plus4_pool_unit_validation.csv`
- `research/4plus4_economics_inference.md`

For ordinary sampled draw totals:
- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Thus III–IX jointly distribute approximately **48U**.

Out-of-sample confirmations:
- draw #790: **U≈417.6**;
- draw #781: **U≈418.293**.

Eight samples give mean `U/N_hat≈0.01000654`, median `≈0.00995289`, so `U≈0.01×sold_variants` remains stable.

### Important correction
Standalone winner-story payouts are not category totals; `ticket payout / category weight` cannot identify U without category winner counts/ticket structure. This is already corrected in the research note and cross-check dataset.

## Ordinary 4+4 subtotal
- X/XI exact expected payout: **0.682149737849 AZN / variant**;
- III–IX under empirical U/N scale: about **0.48 AZN / variant**;
- subtotal before category II and jackpot: **~1.16215 AZN per assumed 2-AZN variant** (~58.11%).

## Category II / H014
`II≈20U` remains only a pattern clue. H014 zero-winner carryover remains testing and requires adjacent-draw accounting. Manual historical archive/API routes are currently exhausted; do not repeat blind draw #780/API searches without new tooling/source.

Kazakhstan 4/20 remains the validated methodological comparator where zero-winner lower pools feed the next superprize exactly, but the sampled state is ~55% return and not +EV.

# H010 — Poz-Qazan remaining-prize edge
Files:
- `data/derived/az_poz_qazan_initial_ev_2026.csv`
- `research/poz_qazan_remaining_prize_edge.md`

Current-series initial after-tax payout ratios:
- Prestij reg.317: **69.9060%**
- Meqa 7 reg.365: **66.8758%**
- Qoşa 2 reg.383: **66.3051%**
- 4 Fəsil reg.375: **62.9775%**

The denominator for current conditional EV exists institutionally (daily sales data and formal unsold-ticket tracking are required), but no public registration-specific live denominator has been recovered. H010 remains **testing / data-blocked**.

# UK Lotto
H016 Wednesday Must Be Won remains **inconclusive/materially weakened** after demand-uplift stress test.

# H015 — next bounded research target
**Rolldown/shared-pool anti-popularity edge.**

Question: how much can deliberately choosing combinations less popular with other players improve expected share of a jackpot or lower shared pool?

Required next work:
1. derive expected share under non-uniform crowd choice versus uniform baseline;
2. quantify realistic uplift using primary research / observed winner-count asymmetries;
3. separate jackpot sharing from lower-tier shared-pool sharing;
4. compare the maximum plausible uplift with the underlying negative EV, rather than treating “less popular numbers” as automatically profitable;
5. account for self-collision in a multi-ticket portfolio.

The likely outcome is that popularity avoidance can improve conditional payout but only becomes economically decisive when combined with a structural overlay/rolldown.

# Current priorities
1. **H015 crowd-sharing magnitude** — next short packet.
2. H010 official registration-specific denominator if a new data route appears.
3. H014 4+4 state accounting when new archive/network tooling appears.
4. Progressive jackpot thresholds / promotion edges.
5. High-frequency RNG diagnostics only after reliable historical collection.
