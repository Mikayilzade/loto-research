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

## Super Keno
- displayed base-table gross EV **0.598555794 AZN / 1 AZN**;
- net before tax about **-40.14%**;
- multipliers pending.

# Azerbaijan 4+4 — still the top local draw-game target
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
- draw #790: **U≈417.6**, V+VI 835.45 vs predicted 835.20;
- draw #781 (2026-06-05): robust **U≈418.293**, V/VI ≈ U/U as expected.

With draw #781 added, eight samples give:
- mean `U/N_hat` ≈ **0.01000654**;
- median ≈ **0.00995289**.

So `U≈0.01×sold_variants` remains stable.

### V/VI coupling
Observed sampled rule:
- if V winners <= VI winners, pools ≈ U/U;
- if V winners > VI winners, combined 2U is redistributed so per-winner V ≈1.5× per-winner VI.

Zero-winner V/VI behavior is not extrapolated.

### Important correction: winner stories are NOT direct U estimates
`III=11U` is a **total category pool**, not one winner payout. Ticket-level winner stories cannot identify U without category winner count and ticket/system structure. Earlier `payout/11=U` interpretation was corrected in:
- `research/4plus4_economics_inference.md`
- `data/historical/az_4plus4_official_winner_crosschecks.csv`

The draw-table U-engine remains strong; only standalone winner-story validation was downgraded.

## Ordinary 4+4 subtotal
- X/XI exact expected payout: **0.682149737849 AZN / variant**;
- III–IX under empirical U/N scale: about **0.48 AZN / variant**;
- subtotal before category II and jackpot: **~1.16215 AZN per assumed 2-AZN variant** (~58.11%).

Ordinary state remains strongly negative.

## Category II / H014 — unresolved carryover lead
Exact II (`4+3 / 3+4`) probability:
- **0.000005452835634281** ≈ **1 in 183,390.82**.

Three primary one-number-short tickets exist (Vəzir 10,287; Nizami 8,609; Ümüd 15,986), proving category-II variants occurred, but ticket payouts do not reveal pure II pool totals.

`II≈20U` remains a **pattern clue only**, not a rule.

Conditional scale screen, assuming II=20U, U=0.01N and zero-winner transfer:
- P(no II winner) roughly **76–81%** at 38k–50k variants;
- hypothetical unpaid II amount roughly **6.2k–7.6k AZN/draw**;
- potential annual scale **~0.64m–0.79m AZN/year** at 104 draws.

This only shows the mechanism would be large enough to matter if real.

H014 proof still requires repeated adjacent-draw accounting showing unpaid pools enter a visible future state before purchase.

## Kazakhstan 4/20 comparator
Do not transfer its rules to Azerbaijan. Three independent transitions close exactly as:
`next superprize = previous superprize + unpaid lower pools + current ordinary contribution`.

This validates an active modern zero-winner-transfer mechanism class, but the sampled Kazakhstan state is only ~55% return and nowhere near +EV.

## 4+4 data blockers
- official historical archive API/payload not discovered;
- draw #780 full payout table unrecovered;
- Vəzir 2025-09-19 draw totals unrecovered;
- Ümüd exact date/draw unresolved;
- exact adjacent jackpot states unavailable;
- January-2025 external-transfer amount unknown;
- detailed registration no.336 allocation document unfound.

Manual web-index approaches are currently exhausted. Do not repeat blind API/draw #780 searches without new tooling. Best future route is browser DevTools/HAR/network inspection or new indexed detail pages.

# H010 — Poz-Qazan remaining-prize state edge
Files:
- `data/derived/az_poz_qazan_initial_ev_2026.csv`
- `research/poz_qazan_remaining_prize_edge.md`

## Exact initial after-tax baselines
1. **Prestij reg.317** — 10 AZN; 2.4m tickets; after-tax payout ratio **69.9060%**; EV **6.990595 AZN**; 2×500k top prizes.
2. **Meqa 7 reg.365** — 5 AZN; 4m tickets; after-tax ratio **66.8758%**; EV **3.34378775 AZN**; 2×100k.
3. **Qoşa 2 reg.383** — 2 AZN; 4m tickets; after-tax ratio **66.3051%**; EV **1.326102 AZN**; 40×4k.
4. **4 Fəsil reg.375** — 1 AZN; 20m tickets; after-tax ratio **62.9775%**; EV **0.629775 AZN**; 10×5k.

All ordinary initial states are materially negative EV.

## Denominator blocker — refined
No public live registration-specific counter was found for remaining unsold tickets or complete remaining-prize inventory.

However, official law/tax rules show the denominator **exists institutionally**:
- the lottery organizer is required to transmit ticket-sales data to the designated state information system **daily**;
- physical tickets carry number/series identifiers;
- unsold tickets are returned/destroyed under formal procedures;
- the organizer must announce the end of an instant lottery.

The State Tax Service public open-data page currently exposes no searchable lottery-ticket-sales dataset under `lotereya`, `bilet`, or `satış`.

A 2025 annual-report PDF exists on the tax-service report page, but the current tool timed out fetching it; it has **not** been analyzed and no series-level sales claim is made from it.

### Series-identity trap
Current Prestij reg.317 starts 12.06.2025, but current/history surfaces include Hüseyn Bünyatov's 500k Prestij win dated **22.07.2024**. Winner carousels therefore mix releases. Never decrement current inventory by game name alone.

Require exact registration/batch + valid winner date, ideally ticket serial/explicit operator linkage.

## H010 status
**testing / data-blocked**.

The math is straightforward once both remaining after-tax prize value and remaining purchasable tickets are observable. Current web research has not recovered that live denominator.

Higher-value next route is **official registration-specific data access** (operator/regulator request, batch-close/sales-progress report, or defensible serial/pack inventory source), not repeated generic web search.

# UK Lotto
H016 Wednesday Must Be Won remains **inconclusive/materially weakened** after demand-uplift stress test. H015 crowd-choice/sharing remains theoretical/unquantified.

# Next actions
1. **H010:** pursue registration-specific sold-ticket counts / sales-progress through official data channels; avoid further generic search for the same missing counter.
2. Match current large-prize winners to exact registration/batch before changing remaining-prize numerator.
3. If denominator becomes available, build exact after-tax conditional EV by registration and uncertainty bounds.
4. Keep 4+4 open but pause repetitive manual archive work until new tooling/source appears.
5. Next research class if no new H010 data: Super Keno multiplier economics, then H015 crowd-sharing and other promotion/progressive edges.
