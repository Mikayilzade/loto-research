# H077 — Baku catalytic-converter pre-quote arbitrage

Updated: 2026-08-18
Status: **LOCAL HIGH-VALUE/WEIGHT MECHANISM VALIDATED / LIVE LOW-ASK INVENTORY EXISTS / ATOMIC QUOTE NOT LOCKED / NOT SUCCESS**

## Goal
Test a higher-value salvage class than H076 batteries: acquire a legally owned used catalytic converter in Baku only after a recycler has quoted the exact unit, then immediately sell it into the pre-quoted local recycling exit.

Strict execution theorem:

`profit_floor = locked_recycler_payout - seller_price - inspection/pickup/payment/tax/other_locked_costs`

A terminal SUCCESS requires the exact converter identity, lawful provenance, recycler acceptance and cash payout to be locked before seller payment, with a strictly positive worst-case net floor.

## Why this class is materially stronger than H076
Catalytic converters concentrate platinum-group metals, so value per kilogram is much higher than ordinary battery or steel scrap. Current Baku recycling infrastructure is real and local:

- Dukata Recycling states that it buys catalytic converters throughout Azerbaijan, offers a quick transparent quotation, laboratory analysis, pickup/drop-off logistics and immediate payment. Initial consultation/quotation is free.
- Katalizator N1 publishes local buying ranges and offers on-site analysis plus immediate payment; its current public ranges include roughly 20–50 AZN for Lada iron units, 50–100 AZN for Lada ceramic, 50–200 AZN for foreign iron, and 100–1000 AZN for foreign ceramic units.
- ScrapTraffic's Baku market page also shows catalytic-converter buying and photo-based price enquiry, but its figures are treated only as secondary market evidence, not as a binding quote.

Sources:
- https://dukatarecycling.com/en/catalytic-converter-buying-recycling/
- https://katalizator-n1.ru/
- https://scraptraffic.com/baku/katalizatoryi

## Live inventory screen
Current/recent Baku marketplace indexing contains many used exhaust-category items. Important filter result: category labels alone are unreliable because many low-priced results are mufflers, sensors or shells rather than PGM-bearing converters.

Examples checked:
- a 2008 BMW item indexed at 80 AZN was opened and proved to be a muffler, therefore rejected;
- a Tap.az Priora listing at 130 AZN explicitly described a catalytic converter removed from the seller's own car, but the listing is now inactive;
- current Lalafo used-category pages show multiple nominally original exhaust/catalyst items around 150–250 AZN, but each must be individually opened and identified before valuation.

Sources:
- https://lalafo.az/baku/zapchasti/katalizatorlar-sesbogucular/used?page=2
- https://tap.az/elanlar/neqliyyat/ehtiyyat-hisseleri-ve-aksesuarlar/46601505

## Atomic execution design
The safe workflow is not “buy cheap then hope.” It is:

1. obtain seller photos of the complete unit, serial/code stamps and proof of lawful ownership/origin;
2. send those exact photos/codes to at least two local recyclers;
3. obtain a fixed immediate-cash quote conditional only on visual/serial verification already supplied, or arrange buyer inspection at the seller location;
4. require the recycler/buyer to inspect and confirm acceptance before money is irreversibly paid to the seller;
5. pay seller only if `locked buyer payout > seller ask + all locked costs`;
6. immediately transfer the same unit to the buyer and retain invoice/receipt/provenance trail.

The strongest practical variant is a **three-party same-location transaction**: seller + recycler/assayer + buyer funds. This eliminates inventory risk and most logistics.

## Critical blockers
### 1. Public price ranges are not binding exact bids
A range such as 100–1000 AZN for foreign ceramic catalysts does not prove a spread on a 150-AZN listing. Metal content varies heavily by serial/model and by whether the honeycomb is intact.

### 2. Marketplace false positives are common
The 80-AZN BMW control demonstrated that a listing in the catalytic-converter category may actually be a muffler. Search snippets cannot be treated as acquisition candidates without opening the listing and identifying the part.

### 3. Condition / empty-shell risk
An apparently genuine housing may have lost or had removed the precious-metal substrate. A strict guarantee therefore requires inspection/serial/photo valuation before purchase, ideally buyer-side physical verification.

### 4. Provenance / theft risk
Catalytic converters are high-theft-risk goods. The project must reject anonymous/provenance-poor units. Require seller ID, vehicle/document linkage or another credible ownership trail, and a written receipt. Profit does not override legal-title risk.

### 5. Quote finality
Dukata's public process includes laboratory analysis; a preliminary quote is not automatically an irrevocable payout. SUCCESS requires a transaction-specific buyer commitment that survives final inspection or a same-location physical assay before seller payment.

## Current result
H077 validates a much more promising local deterministic-arbitrage structure than H076:

**seller asks can be screened against free local recycler quotes, with minimal shipping and potentially hundreds of AZN gross value per unit.**

However no current exact unit has yet been paired with a binding recycler payout above its seller ask while all title/condition/cost gates are locked.

Status: **NOT SUCCESS**.

## Reopen / next-step conditions
Reopen H077 only for transaction-level evidence:
- exact active seller listing with clear converter serial/photos and lawful provenance;
- recycler quote for that exact unit, preferably from two buyers;
- physical pre-payment assay/inspection or written fixed payout;
- all pickup/payment/tax costs capped;
- strictly positive net floor.

Do not repeat generic marketplace searches without pairing a candidate with an exact recycler valuation.
