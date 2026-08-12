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

Draw #790 was added after discovery and independently fits closely (U≈417.6), providing the first out-of-sample confirmation.

### V/VI coupling
Empirical sampled rule:
- if V winners <= VI winners, pools ≈ U/U;
- if V winners > VI winners, combined 2U is redistributed so per-winner V ≈1.5× per-winner VI.

Zero-winner V/VI behavior is not extrapolated.

### Independent U/N scale
Exact X/XI probabilities and observed fixed X=6 / XI=4 prizes provide a volume estimator. Across seven samples:
- mean `U/N_hat` ≈ **0.00996205**;
- median ≈ **0.00995043**;
- range ≈ **0.00953821–0.01050994**.

So `U≈0.01×sold_variants` emerges from draw-table data.

### IMPORTANT CORRECTION — winner stories are NOT direct U estimates
A prior pass treated official 4+2 winner stories (Samir 4,503 AZN; Orxan 4,381 AZN) as if `reported payout / 11 = U`.

That was too strong and is now corrected in:
- `research/4plus4_economics_inference.md`
- `data/historical/az_4plus4_official_winner_crosschecks.csv`

Reason:
- `III=11U` is the **total category-III pool** for a draw;
- an individual winner receives that pool divided among category-winning variants;
- a system ticket can aggregate multiple variants/categories.

Therefore ticket payout/weight cannot identify U without category winner count and ticket structure.

Primary control observations that exposed this:
- around Tiraj 25072: official Telegram reports `4+2 = 1,470 AZN`;
- around Tiraj 25082/25083: official Telegram reports `4+1 = 2,136 AZN`, jackpot >500k.

These are valuable match/payout observations, but they are not category-total observations.

**What remains strong:** the U-engine itself was inferred from full category totals and passed draw #790 out-of-sample. Only the claimed independent primary-story validation has been downgraded.

## Ordinary economic subtotal from currently stronger components
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

These prove each ticket contains at least one II variant, but do **not** reveal the pure II category pool by themselves.

## II≈20U working hypothesis — still only a pattern clue
Normalizations:
- Vəzir `10287/20=514.35`;
- Nizami `8609/20=430.45`;
- Ümüd `15986/40=399.65`.

After the winner-story correction above, these quotients must **not** be called U estimates. II≈20U remains interesting but unvalidated until a full draw table / category winner count / ticket structure is recovered.

Possible Ümüd explanations:
1. system-ticket aggregation;
2. category-II carryover/state;
3. other hierarchy/aggregation/reporting rules.

## Conditional II carryover scale screen
Assumptions only: II=20U, U=0.01N, N≈38k–50k, zero-winner pool survives intact.

Then P(no II winner) ≈76–81%, assumed II pool ~7,600–10,000 AZN, expected unpaid ~6,178–7,614 AZN/draw, or ~0.64m–0.79m AZN/year at 104 draws.

This only shows the proposed mechanism is large enough to matter if real. It does not validate II=20U or the transfer rule.

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

Example:
`226,866,699 + 248,580 + 132,678 = 227,247,957` KZT exactly.

Sampled state still ~55% return; mechanism real, sampled state not +EV.

# Corrected Azerbaijan jackpot chronology
- 530,359 AZN jackpot was won **08.07.2023**, not 2026;
- next jackpot 250k applied to that historical era.

Current accumulation lower bounds include >500k (Jan 2025), >800k, >1m, >1.3m, >1.5m, >1.8m.

External transfer mechanism is real: on 06.01.2025 operator announced an unwon final Meqa 5/36 jackpot would transfer to 4+4; outcome/amount unresolved.

Use:
`J_t = J_(t-1) + ordinary contributions + zero-winner transfers + external transfers - payouts/adjustments`.

# Archive/API discovery
Note:
- `research/azerlotereya_archive_api_discovery.md`

Bounded search completed without authoritative endpoint. Current-results page renders current data; archive exposes `Tiraj undefined` to crawler. Do not guess undocumented API URLs.

Revisit only with new evidence/tooling such as browser DevTools Network/HAR/browser network inspector.

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
1. Prioritize **full payout tables / category winner counts**, not more standalone winner-story arithmetic.
2. Use primary Telegram/news/result material to locate a draw where a rare category winner and total category payout are both recoverable.
3. Recover draw #780 or Vəzir 2025-09-19 through a new source/tool, not repeated blind search.
4. Recover Ümüd exact draw/previous draw and ticket structure if possible.
5. Obtain exact adjacent jackpot states and test Kazakhstan-style accounting.
6. Expand 4+4 history to 50–100 draws once collection is reliable.
7. Revisit archive API only with DevTools/HAR/network-capable tooling.
8. Resolve external-transfer amount and base-variant price.
9. Validate category II and zero-winner accounting before any forward EV trigger.
10. Then return to H015, Super Keno multipliers, scratch/instant inventory states and major progressive jackpots.
