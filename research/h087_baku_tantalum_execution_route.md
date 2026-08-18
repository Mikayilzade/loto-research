# H087 — Baku tantalum execution route / web-only seller discovery

Updated: 2026-08-19
Status: **WEB-DISCOVERY EXHAUSTED FOR CURRENT INDEXED SOURCES / EXECUTION-GATED / NOT SUCCESS**

## Goal
Push H086 from a generic break-even screen toward an executable Baku transaction by finding an indexed seller lot with enough pre-purchase information to lock both acquisition cost and buyer payout.

## Search performed
Fresh searches covered Azerbaijani/Russian variants of:
- `K52`, `К52`, `K52-1`, `К52-2`;
- `K53`, `К53`, `K53-1`, `К53-4`;
- `tantal / тантал`;
- `radio detallar / радиодетали`;
- Baku and Sumqayit seller listings on Tap.Az / indexed Azerbaijan sources.

### Result of exact-model search
No currently indexed Azerbaijan seller page was recovered that simultaneously exposes:
1. readable exact K52/K53 marking;
2. fixed ask for that exact marked unit;
3. available count/weight.

Generic `K52/K53` web search is heavily polluted by unrelated laptop model names and foreign capacitor stores, so this search mode is now low-value unless a new Azerbaijan source/index appears.

## Best live seller-side candidates

### Candidate A — Tap.Az #45905589, Baku
- displayed ask: **0.20 AZN**;
- explicitly advertises **tantalum** among capacitor types;
- retail + wholesale;
- delivery available.

Critical limitation: the page does not prove that the 0.20-AZN units are tantalum, or that a buyer may select a K52/K53 unit at that price.

Source:
- https://tap.az/elanlar/elektronika/komputer-avadanliqi/45905589

### Candidate B — Tap.Az #43791209, Baku / Narimanov
- displayed listing price: **5 AZN**;
- seller states there are many radio components and high/low-voltage capacitors;
- **20 listing images** are exposed by the page;
- seller explicitly says the buyer can identify the desired item and the seller will quote its price;
- listing was still indexed as active/recent.

This is operationally stronger than a normal generic listing because it explicitly supports **item-by-item selection + quote**, which is exactly what the H086 gate requires.

However, 5 AZN is only the listing-level displayed price; it is not proven to be the price of any exact tantalum capacitor.

Source:
- https://tap.az/elanlar/elektronika/komputer-avadanliqi/43791209

### Candidate C — Tap.Az #43793397, Baku / Sadarak
- displayed price: **3 AZN**;
- physical shop at Sadarak trade center;
- wholesale + retail microchips/capacitors;
- seller states daily opening hours 08:00–15:00.

Useful as a physical sourcing channel, but exact subtype/marking is not indexed.

Source:
- https://tap.az/elanlar/elektronika/audio-video/43793397

## Buyer-side route became materially stronger
Metal Investment AZE / ScrapTraffic exposes a Baku-specific buyer channel for K52/K53-related material.

Fresh current pages show:
- tantalum-capacitor indicative price around **174 AZN/kg** on the Baku table;
- dedicated K53-4 page: **price on request**;
- exact Baku acceptance point: **Kazima bey Zakira street 11**;
- Baku phone/WhatsApp contact published;
- seller can send photos to obtain a price;
- payment is described as immediate after evaluation, with financial documents available if needed.

This does **not** convert the public price into a binding quote, but it establishes a practical pre-purchase route:
`exact seller photos/marking -> buyer photo quote -> seller price lock -> same-day acquisition -> buyer payout`.

Sources:
- https://scraptraffic.com/baku
- https://scraptraffic.com/baku/kondensatoryi-tantalovyie
- https://scraptraffic.com/baku/niobievyie-kondensatoryi-k53-4-v-obolochke

## Quantitative execution thresholds
Using H086 identity:

`break_even_mass_g = 1000 * ask / buyer_rate_per_kg`

At 174 AZN/kg:
- 0.20 AZN -> **1.149 g** accepted lot mass per unit;
- 1 AZN -> **5.747 g**;
- 3 AZN -> **17.241 g**;
- 5 AZN -> **28.736 g**.

Therefore:
- Candidate A remains potentially attractive if exact tantalum units really are near 0.20 AZN;
- Candidates B/C are not buy signals at their displayed listing prices unless the exact selected unit is unusually heavy/valuable or the item-level quote is far below the listing headline.

## New operational theorem
For this class, more web browsing does not create a strict guarantee once the seller page withholds exact marking/price and the buyer page withholds a binding exact-lot payout.

The guarantee can only be locked by a **two-quote sequence before irreversible payment**:
1. seller sends exact marking/photo/count/weight and fixes the exact ask;
2. buyer sees those same details and fixes a payout valid long enough to execute;
3. all local transport/testing/fees are bounded;
4. execute only if `buyer payout > seller ask + all costs`.

If step 2 is merely an indicative website rate, the strategy is not guaranteed.

## Conclusion
H086 is not rejected economically; it is now **web-data-blocked at the exact transaction layer**.

The public web has supplied:
- a very low-price tantalum-advertising seller lead;
- an item-specific multi-photo seller lead;
- a local physical wholesale source;
- a local buyer accepting K52/K53/tantalum material with photo-based pricing and immediate payment.

What the web cannot supply is the final pair of binding numbers for the same exact lot. Do not repeat generic K52/K53 searches unless new indexed Azerbaijan listings appear.

## Next research move
Move systematic search to the next deterministic class while keeping H086 in an execution queue. Re-open H086 only when one of these appears:
- exact seller marking + fixed ask + count/weight;
- a direct seller response;
- a buyer binding quote for a named exact lot.
