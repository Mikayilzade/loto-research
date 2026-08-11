# 4+4 — empirical payout-engine reconstruction

Updated: 2026-08-12
Status: **strong empirical structure + first out-of-sample confirmation; primary-rule confirmation still required**

## Why this matters
The exact draw probabilities were easy. The hard part was reconstructing how sales become category pools and how those pools are divided among winners. This pass now recovers a large part of that hidden payout engine from preserved draw tables.

Primary/current operator page:
- https://www.azerlotereya.com/game/fourplus
- publicly states ticket price **2 AZN**, two 4/20 boards and 11 prize categories;
- detailed category-allocation percentages are not exposed in crawlable text.

Secondary draw-level evidence is stored in:
- `data/historical/az_4plus4_payout_samples_2026.csv`

Secondary sources remain non-authoritative and must eventually be reconciled with the operator archive/API.

## 1. Common pool unit U
Across the fitting sample, total category payouts follow one draw-level unit `U`:

- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Therefore III–IX jointly distribute approximately **48U**.

This corresponds to very clean revenue-share candidates if a base variant is 2 AZN and U is approximately 0.5% of revenue:
- III ~5.5% of revenue;
- IV ~2.5%;
- V+VI ~1.0%;
- VII ~4.5%;
- VIII ~7.0%;
- IX ~3.5%;
- III–IX total ~24.0%.

Those percentage labels are an inference from the data, not yet an official rule statement.

## 2. First out-of-sample check: draw 790
The 11/5/9/14/7 + combined-2U pattern was inferred before draw 790 was added to the reconstruction dataset.

Draw 790 (2026-07-07) secondary table:
- III total: 4,593.40
- IV: 2,087.91
- V: 592.41
- VI: 243.04
- VII: 3,758.96
- VIII: 5,847.84
- IX: 2,923.20

The independent stable-category estimates are approximately:
- III/11 = 417.582
- IV/5 = 417.582
- VII/9 = 417.662
- VIII/14 = 417.703
- IX/7 = 417.600

Median `U = 417.6`.

Observed V+VI = **835.45** versus predicted `2U = 835.20`.

So the formula survives a first small out-of-sample test rather than only describing the rows used to discover it.

## 3. V/VI coupling algorithm
The V and VI pools contain another reproducible rule.

Start from an apparent base allocation `U` to V and `U` to VI.

When the number of category-V winners is **not greater** than category-VI winners, sampled draws leave the totals approximately U/U.

When category V has **more winners** than VI, equal U/U pools would make the higher category pay too little per winner. In every such sampled case, the fixed combined `2U` pool is redistributed so that:

**per-winner payout in V ≈ 1.5 × per-winner payout in VI.**

For winner counts `w5` and `w6`, the reconstructed split is:

`T5 = 2U × (1.5 w5) / (1.5 w5 + w6)`

`T6 = 2U - T5`

Examples:
- draw 776: U≈415.573, winners V/VI=13/6; predicted totals 635.583 / 195.564 vs observed 635.57 / 195.54;
- draw 777: winners 7/4; prediction agrees within rounding;
- draw 790: winners 13/8; predicted 592.233 / 242.967 vs observed 592.41 / 243.04;
- draws 774 (4/7), 795 (8/15), 796 (6/6) remain approximately U/U.

This strongly suggests an internal prize-hierarchy protection rule rather than arbitrary draw-to-draw variation.

**Important:** zero-winner V/VI states are deliberately not extrapolated by the code yet. Those states are precisely where carryover/redistribution behavior must be observed rather than guessed.

Implementation:
- `expected_5_6_pool_split()` in `src/loto_research/four_plus_four.py`.

## 4. Independent sales-scale validation
Categories X and XI are observed as fixed per-winner prizes in the sampled tables:
- X (2+2) = **6 AZN**;
- XI (2+1 / 1+2) = **4 AZN**.

Their exact category probabilities are:
- P(X) = 0.022083984318837523;
- P(XI) = 0.137411457983877900.

Instead of assuming `U = 0.01 × N`, estimate sold variants independently from tail winners:

`N_hat = (W10 + W11) / (P10 + P11)`.

Then calculate `U / N_hat`.

Across seven sampled draws:
- mean `U/N_hat` ≈ **0.00996205 AZN per variant**;
- median ≈ **0.00995043**;
- range ≈ **0.00953821–0.01050994**.

Derived table:
- `data/derived/az_4plus4_pool_unit_validation.csv`

Thus the round `0.01 AZN per sold variant` coefficient emerges from the winner-count data rather than being chosen merely because it looks neat.

If the base variant is 2 AZN, `U≈0.01N` means one U is approximately **0.5% of gross variant sales**. This strongly supports the interpretation that the publicly displayed 2-AZN ticket is a 2-AZN base variant, but direct primary-rule confirmation is still required.

## 5. Ordinary EV implications
Exact expected contribution from fixed X/XI alone:

`P(X)×6 + P(XI)×4 = 0.6821497378485368 AZN per variant`.

With `48U` and empirical `U/N≈0.01`:
- III–IX aggregate crowd-average contribution ≈ **0.48 AZN / variant**;
- X/XI ≈ **0.68215 AZN / variant**;
- subtotal before category II and jackpot ≈ **1.16215 AZN per 2-AZN variant**;
- gross return subtotal ≈ **58.11%**.

So the ordinary game remains strongly negative. The previously exciting floating payout-per-winner values are mostly explained by the payout engine, not by a free carryover bonus.

## 6. Revised H014 target: zero-winner state transitions
The useful question is now much sharper.

When a variable category receives its normal allocation but has **zero winners**, where does that money go?

For each zero-winner event in II–VI:
1. infer `U_t` from stable categories;
2. reconstruct the ordinary assigned amount;
3. verify no payout occurred;
4. examine t+1, t+2...;
5. test whether the missing money appears in the same category, another category, jackpot, reserve or immediate redistribution;
6. determine whether any carried balance is public/observable **before** the next purchase.

Only a forward-observable balance can become an exploitable H014 state.

## 7. Current confidence
High confidence empirically, but not yet primary-authoritative:
- common U engine;
- 11/5/9/14/7 weights;
- V+VI combined 2U;
- conditional V/VI 1.5× per-winner correction;
- U/N around 0.01;
- ordinary lower-tier return far below break-even.

Still unresolved:
- primary detailed prize-allocation rules;
- exact treatment of zero-winner categories;
- category II economics;
- direct base-variant price statement;
- primary historical archive payload/API;
- taxes and self-impact for a large portfolio.

## Next milestone
Expand to 50–100 consecutive draws, with special priority on zero-winner III–VI events and their following draws. Do not claim carryover edge until a repeated t→t+1 state equation is demonstrated.
