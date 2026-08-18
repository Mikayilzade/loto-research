# H086 — Baku tantalum-capacitor break-even screen

Updated: 2026-08-19
Status: **PROMISING / EXECUTION-GATED / NOT SUCCESS**

## Goal
Turn H085's vague low-price capacitor lead into an explicit deterministic acquisition test that can be applied before paying a seller.

## Current seller lead
Tap.Az listing #45905589 in Baku currently shows a nominal ask of **0.20 AZN** and explicitly advertises multiple capacitor types including **tantalum** capacitors, retail/wholesale availability and delivery.

Source:
- https://tap.az/elanlar/elektronika/komputer-avadanliqi/45905589

Important: the indexed page does **not** prove that every capacitor costs 0.20 AZN, that the 0.20-AZN units are tantalum, or that the buyer may cherry-pick qualifying units. Treat 0.20 AZN as a candidate ask that must be confirmed for the exact marked unit.

## Current Baku buyer-side anchor
ScrapTraffic / Metal Investment AZE currently exposes Baku-specific tantalum-capacitor price discovery around **174–187 AZN/kg**. Its dedicated Baku tantalum-capacitor page states up to 187 AZN/kg and describes K52/K53 capacitor scrap as accepted without requiring the seller to extract the metal first; the general Baku table shows about 174 AZN/kg. The same site explicitly warns that displayed prices are dynamic / generally not binding offers, so an exact buyer quote remains mandatory.

Sources:
- https://scraptraffic.com/baku/kondensatoryi-tantalovyie
- https://scraptraffic.com/baku
- https://scraptraffic.com/baku/tantal

## H088 classification correction — mandatory
Do **not** infer tantalum from the generic `K53` prefix. Current primary-source manufacturer pages prove that the K53 family is mixed:
- `K53-1A`, `K53-65`, `K53-68`, `K53-69` are tantalum;
- `K53-4` is niobium.

`K52` examples checked in H088 are tantalum, but exact subtype is still required before acquisition.

Therefore the break-even formula below may use a tantalum buyer rate only after either:
1. exact subtype is independently classified as tantalum from a primary manufacturer/datasheet; or
2. the local buyer gives a binding quote for the exact photographed/marked lot under its quoted category.

See:
- `research/h088_k52_k53_material_classification.md`
- `data/derived/h088_k52_k53_material_classification.csv`

## Exact break-even identity
If a buyer commits to `P` AZN/kg for the whole classified capacitor lot, seller ask is `A` AZN per capacitor, and we temporarily ignore fixed execution costs, the minimum accepted gross mass per purchased unit is:

`m_break_even_g = 1000 * A / P`

A strict profit requires actual accepted mass **greater** than this threshold after allocating transport/testing/fees.

### Break-even mass table
| Seller ask per unit | 174 AZN/kg buyer rate | 185 AZN/kg buyer rate | 187 AZN/kg buyer rate |
|---:|---:|---:|---:|
| 0.20 AZN | 1.149 g | 1.081 g | 1.070 g |
| 1 AZN | 5.747 g | 5.405 g | 5.348 g |
| 3 AZN | 17.241 g | 16.216 g | 16.043 g |
| 5 AZN | 28.736 g | 27.027 g | 26.738 g |

This makes the **0.20-AZN lead qualitatively different** from the generic 1–5 AZN mixed-component leads: if an exact unit is accepted as tantalum-capacitor scrap and weighs only a little above ~1.1 g, gross resale can already exceed the nominal ask before fixed costs.

## Fixed-cost extension
For `n` qualifying capacitors with total fixed execution cost `F` AZN, minimum average accepted mass is:

`m_avg_g > 1000 * (n*A + F) / (n*P)`

Equivalently:

`m_avg_g > 1000 * (A + F/n) / P`

## Strict acquisition protocol
1. seller identifies the exact units offered at the stated per-unit price;
2. exact marking/subtype is readable;
3. exact subtype is manufacturer-classified as tantalum **or** buyer explicitly classifies the exact lot in a binding quote;
4. exact count and total weight are measured;
5. local buyer gives a **binding payout for this lot**;
6. quote validity lasts through execution;
7. `binding payout > seller payment + transport + testing/prep + tax/fees`;
8. seller payment occurs only after steps 1–7 are satisfied.

## Result
H086 does **not** establish SUCCESS because the execution variables remain unbound: exact qualifying unit/price, subtype/count/weight and a binding Baku buyer quote. H088 materially hardens H086 by preventing generic `K53` false positives.
