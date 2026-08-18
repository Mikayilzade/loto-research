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

## Plausibility control — not a guarantee
The dedicated Baku buyer page says K52/K53 tantalum content varies widely and gives examples spanning very small to much larger units. External current buyer references independently show K52 family parts can have material per-unit scrap value, but subtype/year/state matter heavily. Therefore the ~1.1 g threshold is plausible to clear for some units, but no family-name inference is accepted as proof.

External cross-checks used only for classification plausibility, not execution value:
- Detaltorg K52-1: current July 2026 per-unit quote and stated Ta/Ag content;
- current Russian KM/K52 buyer tables showing large subtype dispersion.

## Fixed-cost extension
For `n` qualifying capacitors with total fixed execution cost `F` AZN, minimum average accepted mass is:

`m_avg_g > 1000 * (n*A + F) / (n*P)`

Equivalently:

`m_avg_g > 1000 * (A + F/n) / P`

Therefore bulk purchase matters. Example at `A=0.20`, `P=174`:
- with zero fixed cost: >1.149 g/unit;
- with 2 AZN total execution cost and 10 units: >2.299 g/unit;
- with 2 AZN and 50 units: >1.379 g/unit;
- with 2 AZN and 100 units: >1.264 g/unit.

## Strict acquisition protocol
Do not buy on the listing text alone. A candidate passes only when all are locked before payment:

1. seller identifies the exact units offered at the stated per-unit price;
2. exact marking is readable (`K52`, `K53`, or another buyer-recognized tantalum class);
3. exact count and total weight are measured;
4. local buyer sees the same photos/markings and gives a **binding payout for this lot**, not a website indicative rate;
5. quote validity lasts through immediate acquisition/resale;
6. `binding payout > seller payment + transport + testing/prep + tax/fees`;
7. seller payment occurs only after steps 1–6 are satisfied.

## Result
H086 does **not** establish SUCCESS because the two execution variables are still unbound:
- whether qualifying tantalum units are actually available at **0.20 AZN each** in listing #45905589;
- a binding Baku buyer quote for the exact selected lot.

However, H086 materially upgrades H085: the lead now has a concrete, low break-even threshold (~1.1 g/unit at the currently displayed Baku price range), so exact-photo / exact-weight screening is high priority and no longer a generic scrap search.

## Next move
1. Search indexed seller pages for readable K52/K53 markings and explicit per-unit asks.
2. Prefer lots where seller text allows selection/wholesale and weight/count can be locked.
3. If no exact marked Baku listing is indexed, expand to Sumqayit / nearby Azerbaijan only where transport remains inside the break-even equation.
4. Do not substitute external Russian buyer prices for a Baku binding payout.
