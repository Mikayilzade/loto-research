# 4+4 — empirical payout-engine reconstruction

Updated: 2026-08-12
Status: **strong draw-table empirical structure with out-of-sample confirmation; winner stories are classification clues, not independent U estimates**

## Core result
From preserved draw-level payout tables, one draw-level common unit `U` explains a large part of the Azerbaijan 4+4 lower-prize engine:

- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Therefore III–IX jointly distribute approximately **48U**.

Primary/current operator page:
- https://www.azerlotereya.com/game/fourplus

Draw-level reconstruction data:
- `data/historical/az_4plus4_payout_samples_2026.csv`
- `data/derived/az_4plus4_pool_unit_validation.csv`

Official winner-story observations:
- `data/historical/az_4plus4_official_winner_crosschecks.csv`

## 1. Out-of-sample check: draw 790
The 11/5/9/14/7 + combined-2U pattern was inferred before draw 790 was added.

Draw 790 secondary table:
- III total: 4,593.40
- IV: 2,087.91
- V: 592.41
- VI: 243.04
- VII: 3,758.96
- VIII: 5,847.84
- IX: 2,923.20

Stable-category estimates:
- III/11 ≈ 417.582
- IV/5 ≈ 417.582
- VII/9 ≈ 417.662
- VIII/14 ≈ 417.703
- IX/7 = 417.600

Median `U = 417.6`.

Observed V+VI = **835.45** versus predicted `2U = 835.20`.

This remains the cleanest independent check of the discovered pool-weight formula.

## 2. V/VI coupling algorithm
The combined V+VI pool remains approximately 2U.

Empirical sampled rule:
- if category-V winners <= category-VI winners, totals remain approximately U/U;
- if V winners > VI winners, the combined 2U pool is redistributed so per-winner V payout is approximately **1.5×** per-winner VI payout.

For winner counts `w5`, `w6`:

`T5 = 2U × (1.5 w5)/(1.5 w5+w6)`

`T6 = 2U - T5`

Examples 776, 777 and 790 match within source rounding. Zero-winner V/VI states are deliberately not extrapolated.

Implementation:
- `expected_5_6_pool_split()` in `src/loto_research/four_plus_four.py`.

## 3. Independent sales-scale validation
Categories X and XI are observed as fixed per-winner prizes in sampled payout tables:
- X = **6 AZN**;
- XI = **4 AZN**.

Exact probabilities allow an independent sold-variant volume estimate:

`N_hat = (W10 + W11)/(P10 + P11)`.

Then compare `U/N_hat`.

Across seven sampled draws:
- mean ≈ **0.00996205 AZN per variant**;
- median ≈ **0.00995043**;
- range ≈ **0.00953821–0.01050994**.

Therefore `U≈0.01×sold_variants` emerges empirically. If one base variant costs 2 AZN, one U corresponds to about 0.5% of gross variant sales. Direct primary wording for the base-variant price remains missing.

## 4. Important correction — winner stories do NOT independently identify U
A prior pass treated official winner stories such as:
- Samir İmaməliyev: `4+2`, 4,503 AZN;
- Orxan Həsənov: `4+2`, 4,381 AZN;

as if dividing the reported payout by category weight 11 directly estimated U.

That interpretation was too strong.

The reconstructed rule `III=11U` describes the **total category-III pool for the draw**, while a winner story normally reports one ticket/player's payout. The relationship is approximately:

`per-winner category payout = category total pool / number of winning variants`

and a system ticket can additionally contain multiple winning variants/categories.

Therefore `reported_ticket_payout / 11` is **not** an independent U estimate unless we also know:
1. category-III winner count;
2. that the reported amount is the pure category-III payout;
3. ticket/system structure.

The same caution applies to category IV and category II winner stories.

### Primary control observations that exposed the issue
Official Telegram also contains older observations:
- around Tiraj 25072: `4+2 = 1,470 AZN`;
- around Tiraj 25082/25083: a player made `4+1` and won 2,136 AZN while jackpot was >500k.

Those observations are valuable match/payout evidence, but without category winner counts they cannot be converted directly into U. They demonstrate why winner stories must not be used as pool totals.

**Consequence:** the draw-table U-engine itself remains strong because it was inferred from total category payouts and passed an out-of-sample draw. What is downgraded is only the claimed independent primary-story validation of its U scale.

## 5. Category-II ~20U hypothesis remains suggestive, not validated
Three official tickets contain at least one category-II (`4+3 / 3+4`) variant because the operator says the player missed the jackpot by one number:
- Vəzir Quliyev: 10,287 AZN;
- Nizami Tağıyev: 8,609 AZN;
- Ümüd Hüseynov: 15,986 AZN.

Numerical normalizations such as:
- `8609/20 = 430.45`;
- `10287/20 = 514.35`;
- `15986/40 = 399.65`

are pattern clues only. They are **not U estimates** without draw-level category totals, winner counts and ticket structure.

Ordinary II≈20U remains a working hypothesis because it is structurally plausible and the numerical pattern is interesting, but the evidence threshold has not been met.

Detailed note:
- `research/4plus4_category2_lead.md`

## 6. Ordinary EV implications from validated components
Exact expected contribution from fixed X/XI:

`P(X)×6 + P(XI)×4 = 0.6821497378485368 AZN per variant`.

With `48U` and empirical `U/N≈0.01`:
- III–IX aggregate crowd-average contribution ≈ **0.48 AZN / variant**;
- X/XI ≈ **0.68215 AZN / variant**;
- subtotal before category II and jackpot ≈ **1.16215 AZN per assumed 2-AZN variant**;
- subtotal gross return ≈ **58.11%**.

This part does not depend on winner-story interpretation and remains the current ordinary-state baseline.

## 7. H014 target: zero-winner state transitions
When a variable category receives its normal allocation but has zero winners, determine where the money goes.

For each useful transition:
1. infer `U_t` from stable draw-table categories;
2. reconstruct ordinary assigned amount;
3. verify zero winners;
4. inspect t+1 and later states;
5. test whether missing money appears in same category, another category, jackpot, reserve or immediate redistribution;
6. require any carried balance to be observable before the next purchase.

Only a forward-observable balance can become an exploitable state signal.

## Current confidence
**Strong empirical evidence:**
- common U engine in sampled draw totals;
- weights 11/5/9/14/7 and V+VI=2U;
- V/VI hierarchy correction;
- U/N around 0.01 from X/XI winner-volume estimator;
- ordinary subtotal far below break-even.

**Unresolved / downgraded:**
- winner stories as independent U validation — **downgraded; insufficient without winner counts**;
- category II≈20U;
- zero-winner transfer rule;
- direct base-variant price statement;
- primary historical archive/API.

## Next milestone
Obtain a full draw payout table containing a category-II winner, or a winner story plus category winner count/ticket structure. Do not use ticket-level winner-story amounts as category pool totals.
