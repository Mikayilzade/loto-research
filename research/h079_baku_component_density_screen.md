# H079 — Baku salvage component density screen

Updated: 2026-08-18
Status: **CLASS SCREENED / CPU+RAM PUBLIC-ASK PATHS WEAK / TRANSFORMER-COPPER PATH REMAINS EXECUTION-GATED / NOT SUCCESS**

## Goal
Screen the next local salvage classes after H078 using a common deterministic criterion:

`profit_floor = locked_buyer_payout - seller_price - all_locked_costs`.

Public headline scrap prices are treated only as optimistic anchors, not binding bids. A candidate can advance only if the exact item can be weighed/classified and its buyer payout fixed before seller payment.

## Current Baku buyer anchors
ScrapTraffic / Metal Investment AZE currently indexes:
- processors: up to about **64 AZN/kg** headline;
- RAM boards: yellow-contact RAM up to about **52 AZN/kg** in the electronic-board table;
- copper: about **14.1 AZN/kg**;
- complete electric motors: about **545 AZN/ton = 0.545 AZN/kg**.

The same site explicitly says published prices are generally indicative/dynamic rather than standing offers and that transaction-specific price fixation requires exact material details and agreement.

Sources:
- https://scraptraffic.com/baku/proczessoryi
- https://scraptraffic.com/baku/elektronnyie-platyi
- https://scraptraffic.com/baku
- https://scraptraffic.com/baku/elektrodvigateli

## Live/recent acquisition anchors
### CPU
Tap.az has a current/recent Intel Pentium G630 at **5 AZN**, and multiple Pentium-class CPUs around 5 AZN.

Optimistic zero-cost break-even at the *headline maximum* 64 AZN/kg:
`5 / 64 = 0.078125 kg = 78.1 g`.

That is already a demanding mass threshold for a single modern textolite CPU, and the 64-AZN/kg headline is not a guaranteed category price for the exact CPU. Therefore a 5-AZN ordinary Pentium is not a public-data arbitrage.

Source:
- https://tap.az/elanlar/elektronika/komputer-avadanliqi/42759442

### RAM
Tap.az has DDR3 1GB notebook RAM at **3 AZN retail / 2 AZN wholesale** in quantity and DDR2 1GB at 5 AZN.

At the optimistic 52 AZN/kg RAM-board anchor, a 2-AZN stick needs:
`2 / 52 = 0.03846 kg = 38.5 g`
just to break even before transport/preparation and before a buyer-specific downgrade.

This makes individual ordinary SO-DIMMs unattractive as a scrap conversion at current asks unless a substantially better exact buyer rate or unusually heavy/high-grade lot is locked.

Source:
- https://tap.az/elanlar/elektronika/komputer-avadanliqi/46623305

### Transformers / copper-bearing components
A Baku listing offers power-supply transformers from roughly **4–20 AZN**, with a 5-AZN displayed ask and quantity available.

If an exact 5-AZN transformer could be dismantled into qualifying copper at 14.1 AZN/kg with zero other cost, required recoverable copper is:
`5 / 14.1 = 0.3546 kg`.

This is materially more plausible than the CPU/RAM mass hurdle because transformer windings can contain substantial copper, but copper mass and preparation labor are unknown and the public copper price is not binding.

Source:
- https://tap.az/elanlar/elektronika/komputer-avadanliqi/44239062

### Complete motors
A complete motor sold for 10 AZN would need:
`10 / 0.545 = 18.35 kg`
at the published complete-motor scrap anchor, before any cost.

Therefore low-cost small appliance/automotive motors are not attractive as complete-motor scrap. Their only plausible path is dismantling into separately quoted copper/steel fractions, which reintroduces assay, labor and yield uncertainty.

## Ranking after screen
1. **Transformer / copper-rich component with buyer-first weigh/quote** — PROMISING but execution-gated.
2. H078 complete e-scrap PCB with buyer-first classification — still stronger low-capital architecture.
3. Ordinary low-end CPU at 5 AZN — weak/rejected on public-data economics.
4. Ordinary notebook RAM at 2–5 AZN — weak/rejected on public-data economics.
5. Small complete motors — weak unless acquired near-free or dismantled under a locked component quote.

## Reopen conditions
Reopen CPU/RAM only with one of:
- seller ask materially below the screened price levels;
- exact buyer classification/rate fixed for the item or lot;
- high-grade legacy/ceramic CPU or server/RAM lot whose locked payout clears all costs.

Reopen transformer/motor only with:
- exact item/lot;
- measured total and/or recoverable copper mass;
- buyer-specific fixed payout for prepared material;
- preparation/transport cost cap;
- seller paid only after the positive floor is locked.

## Conclusion
H079 prevents repeated generic searches of cheap CPUs/RAM/motors. The public-data economics do **not** establish arbitrage. The only branch worth carrying forward is **copper-rich transformer/component pre-quote execution**, where the item must be physically weighed/assayed before purchase.

Terminal state remains **NO SUCCESS; NOT EXHAUSTED**.
