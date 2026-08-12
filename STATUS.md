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

## Historically validated structural +EV benchmark
Cash WinFall: preserved 2011 roll-down, exact 6/46 probabilities and cash-only tiers:
- ticket $2;
- expected payout **$2.2137120403**;
- expected ROI **+10.6856%** before tax/execution.

Structural +EV lotteries have existed without number prediction.

## Azerbaijan baselines
### Beşdə 5
- jackpot odds **1 in 376,992**;
- favorable gross baseline **0.535555131 AZN / 1-AZN variant**;
- net before tax/sharing about **-46.44%**.

### Super Keno
- displayed base-table gross EV **0.598555794 AZN / 1 AZN**;
- net before tax about **-40.14%**;
- multipliers pending.

# Azerbaijan 4+4 — current top local target

## Exact mechanics
Primary operator page establishes:
- two independent 4/20 boards;
- 11 grouped winning categories;
- jackpot odds **1 in 23,474,025**;
- any listed winning state **18.614724%** (~1 in 5.3721);
- public ticket price **2 AZN**;
- registration no. **336 / 17.01.2021**, valid through 31.12.2027;
- 5+5 / 6+6 system entries generate multiple variants and can win multiple categories;
- current schedule **Tue/Fri 19:45**.

Direct primary wording for one base-variant price remains missing. 2 AZN/base variant is a high-confidence empirical inference, not a direct rule fact.

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

### Out-of-sample confirmations
- Draw #790 was added after discovery and independently fits closely: **U≈417.6**, V+VI=835.45 vs predicted 835.20.
- **NEW draw #781 (2026-06-05)** was recovered from an indexed Statlotto detail page and independently fits again:
  - III/11 ≈ 418.211
  - IV/5 ≈ 418.212
  - VII/9 ≈ 418.293
  - VIII/14 ≈ 418.320
  - IX/7 ≈ 418.549
  - robust median **U≈418.293**
  - V total 418.22 and VI total 418.25 with V winners=2 <= VI winners=7, matching the expected U/U case.

The 11/5/9/14/7 + V/VI structure therefore survives more than one independent draw.

### V/VI coupling
Empirical sampled rule:
- if V winners <= VI winners, pools ≈ U/U;
- if V winners > VI winners, combined 2U is redistributed so per-winner V ≈1.5× per-winner VI.

Zero-winner V/VI behavior is not extrapolated.

### Independent U/N scale
Exact X/XI probabilities and observed fixed X=6 / XI=4 prizes provide a volume estimator.

With draw #781 added, eight samples now give:
- mean `U/N_hat` ≈ **0.01000654**;
- median ≈ **0.00995289**;
- draw #781 itself: N_hat≈40,540 variants and `U/N_hat≈0.010318`.

So `U≈0.01×sold_variants` remains stable after another independent row.

### IMPORTANT CORRECTION — winner stories are NOT direct U estimates
A prior pass treated official 4+2 winner stories as if `reported payout / 11 = U`. That was too strong.

Reason:
- `III=11U` is the **total category-III pool**;
- an individual payout is the pool divided among category-winning variants;
- system tickets can aggregate multiple variants/categories.

Primary control observations exposing this include an older official `4+2 = 1,470 AZN` and `4+1 = 2,136 AZN`. These are match/payout observations, not category totals.

The draw-table U-engine remains strong; only standalone winner-story arithmetic was downgraded.

## Ordinary economic subtotal
- X/XI exact expected payout: **0.682149737849 AZN / variant**;
- III–IX under empirical U/N scale: about **0.48 AZN / variant**;
- subtotal before category II and jackpot: **~1.16215 AZN per assumed 2-AZN variant** (~58.11%).

Ordinary state remains strongly negative.

# Category II — strongest unresolved lead
Files:
- `research/4plus4_category2_lead.md`
- `data/historical/az_4plus4_official_winner_crosschecks.csv`
- `data/derived/az_4plus4_category2_carryover_screen.csv`

Exact II (`4+3 / 3+4`) probability:
- **0.000005452835634281** ≈ **1 in 183,390.82**.

Three primary tickets described as one number short of jackpot:
- Vəzir Quliyev: **10,287 AZN**, 2025-09-19;
- Nizami Tağıyev: **8,609 AZN**, 2026-06-02 / working draw #780;
- Ümüd Hüseynov: **15,986 AZN**, jackpot >1.8m; date/draw unresolved.

These prove each ticket contains at least one II variant, but do not reveal pure category-II pool totals.

## II≈20U working hypothesis — pattern clue only
Normalizations such as 8609/20, 10287/20 and 15986/40 are suggestive but are **not U estimates** without full draw totals, category winner count and ticket structure.

Possible Ümüd explanations:
1. system-ticket aggregation;
2. category-II carryover/state;
3. other hierarchy/aggregation/reporting rules.

## Conditional II carryover scale screen
Assumptions only: II=20U, U=0.01N, N≈38k–50k, zero-winner pool survives intact.

Then P(no II winner) ≈76–81%, assumed II pool ~7,600–10,000 AZN, expected unpaid ~6,178–7,614 AZN/draw, or ~0.64m–0.79m AZN/year at 104 draws.

This shows only that the mechanism would be large enough to matter if real.

# H014 — zero-winner state edge
Status: **testing**.

Required proof:
1. infer ordinary assigned pool from full draw-table data;
2. observe zero winners;
3. obtain adjacent jackpot/category states;
4. show missing amount enters next state after normal/external contributions;
5. repeat multiple times;
6. require pre-purchase observability.

Only then build a forward EV trigger.

# Kazakhstan 4/20 comparator
Do not transfer rules to Azerbaijan. Same two-board 4/20 math is used as methodology control.

Three independent transitions close exactly as:
`next superprize = previous superprize + unpaid lower pools + current ordinary contribution`.

Sampled state still ~55% return; mechanism real, sampled state not +EV.

# Corrected Azerbaijan jackpot chronology
- 530,359 AZN jackpot was won **08.07.2023**, not 2026;
- next jackpot 250k applied to that historical era.

Current accumulation lower bounds include >500k (Jan 2025), >800k, >1m, >1.3m, >1.5m, >1.8m.

External transfer mechanism is real: on 06.01.2025 operator announced an unwon final Meqa 5/36 jackpot would transfer to 4+4; outcome/amount unresolved.

Use:
`J_t = J_(t-1) + ordinary contributions + zero-winner transfers + external transfers - payouts/adjustments`.

# Archive/API and Telegram-media discovery
Notes:
- `research/azerlotereya_archive_api_discovery.md`

Official archive API remains undiscovered; do not guess endpoints. Current-results renders data while historical archive shell exposes `Tiraj undefined` to crawler.

Official Telegram archive exposes `Tiraj XXXXX – Nəticələr` posts and direct image/CDN links, but the current web-cache/container cannot fetch those JPEG result cards. This is a promising future route if a browser/HAR/network-capable tool becomes available.

Secondary archive detail-page indexing is selective. A useful new route is the Statlotto mirror: draw #781 detail was indexed even though many neighboring draws are not. Exact-page searches for 782–785 and selected 786–794 produced no new detail pages in the latest bounded packet; do not immediately repeat identical queries.

# UK Lotto
H016 Wednesday Must Be Won is **inconclusive/materially weakened** after demand-uplift stress test. H015 crowd-choice/sharing remains theoretical.

# Current blockers
- official historical archive API/payload not discovered;
- draw #780 full payout table unrecovered;
- Vəzir 2025-09-19 draw-level category totals unrecovered;
- Ümüd exact date/draw unresolved;
- exact adjacent 4+4 jackpot values unavailable;
- January-2025 external-transfer amount unknown;
- detailed registration no.336 allocation document unfound;
- direct primary base-variant price wording missing;
- II≈20U unvalidated;
- secondary history requires primary reconciliation.

# Next actions
1. Continue **selective** recovery of full payout pages from mirrors/locales; add every new row and prioritize zero-winner III–VI states.
2. Do not repeat blocked draw #780/manual API queries unless new tooling or source appears.
3. Use primary Telegram/news/result material to reconcile any newly recovered secondary payout page.
4. Obtain exact adjacent jackpot states and test Kazakhstan-style accounting.
5. Expand 4+4 history toward 50–100 draws once collection is reliable.
6. Revisit archive API / Telegram cards only with DevTools/HAR/browser-network tooling.
7. Resolve external-transfer amount and direct base-variant price.
8. Validate category II and zero-winner accounting before any forward EV trigger.
9. Then return to H015, Super Keno multipliers, scratch/instant inventory states and major progressive jackpots.
