# H078 — Baku e-scrap PCB pre-quote arbitrage

Updated: 2026-08-18
Status: **LOCAL MECHANISM VALIDATED / LIVE 5-AZN BROKEN-BOARD INVENTORY EXISTS / EXACT WEIGHT+BUYER BID NOT LOCKED / NOT SUCCESS**

## Goal
Screen a lower-theft-risk, locally executable salvage class after H077: acquire legally owned non-working computer/laptop/phone circuit boards only after a local e-scrap buyer has classified and priced the exact board, then transfer it immediately.

Strict theorem:

`profit_floor = locked_buyer_payout - seller_price - pickup/inspection/preparation/payment/tax/other_locked_costs`

SUCCESS requires all terms to be locked before seller payment.

## Current local buyer evidence
### Fors Group — primary local buyer/process evidence
Fors Group in Baku explicitly states that it buys used, obsolete or surplus circuit boards from individuals and businesses, including:
- computer motherboards, graphics cards, RAM, HDD/SSD controller boards;
- mobile-phone/tablet boards;
- household-appliance boards;
- industrial-equipment boards.

It explicitly says functionality is not required: boards are evaluated for metal content/recyclability. Its stated process is acceptance/evaluation -> price offer -> immediate official payment and collection.

Source:
- https://forsgroup.az/en/services/1-buying-different-kinds-of-circuit-boards.html

### ScrapTraffic / Metal Investment AZE — market-price anchor, not binding bid
The current indexed Baku page advertises electronic-board purchasing up to roughly 61 AZN/kg and provides category descriptions/acceptance preparation. This is useful as a market ceiling/anchor but is not treated as a binding transaction-specific offer.

Source:
- https://scraptraffic.com/baku/elektronnyie-platyi

## Live/recent acquisition evidence
Baku marketplace results contain explicit broken-board inventory at very low asks:

1. HP ProBook 4525s laptop motherboard — 5 AZN.
   - seller states motherboard does not work; video chip is defective; sold for spare parts;
   - Baku/Bakikhanov location;
   - indexed page does not mark the board as functional, so it fits the buyer class in principle.
   Source: https://tap.az/elanlar/elektronika/komputer-avadanliqi/45934643

2. Generic used computer parts — 5 AZN each; seller states none works.
   Source: https://tap.az/elanlar/elektronika/komputer-avadanliqi/35129712

3. Search inventory also shows multiple 5-AZN damaged motherboard/parts listings, confirming that the 5-AZN level is not a one-off historical anomaly.

## Break-even weight screen
If a recycler truly locks payout `p` AZN/kg for the exact classified board and acquisition ask is 5 AZN, the zero-friction minimum board weight is:

`w_break_even = 5 / p`.

Examples:
- at 61 AZN/kg: 0.08197 kg = **82 g**;
- at 50 AZN/kg: **100 g**;
- at 30 AZN/kg: **166.7 g**;
- at 20 AZN/kg: **250 g**.

With 3 AZN total locked transaction cost and 5 AZN ask, thresholds become:
- 61 AZN/kg: **131.1 g**;
- 50 AZN/kg: **160 g**;
- 30 AZN/kg: **266.7 g**.

This makes the class potentially executable on a single local board if the board is complete enough to qualify and its buyer-assayed weight/category clears the threshold.

## Why this is stronger than generic salvage
- the asset is local and light, so logistics can be near-zero;
- non-working status is explicitly accepted by a real Baku buyer;
- buyer can classify/quote before acquisition;
- seller asks can be only a few AZN;
- provenance risk is lower than catalytic converters, although stolen-property controls still apply;
- a three-party/same-location or buyer-first inspection can make execution nearly atomic.

## Atomic execution design
1. Seller provides clear photos and confirms lawful ownership/origin.
2. Remove only items the buyer requires removed; do not alter the board before buyer confirms category.
3. Exact board is weighed and inspected/classified by buyer before seller is irreversibly paid, or buyer issues a fixed payout for that exact item.
4. Compute `locked payout - seller ask - all locked costs`.
5. Pay seller only if the worst-case floor is strictly positive.
6. Transfer exact board to buyer immediately and retain receipts.

Best design: seller meets at/near Fors Group or another recycler; recycler weighs/classifies exact board; seller is paid only after recycler's payout is fixed.

## Critical blockers
### Buyer price is not yet binding
Fors Group confirms the service and immediate payment but publishes no fixed category tariff on the page. ScrapTraffic's 61-AZN/kg figure is an index/market anchor, not a transaction-specific guaranteed bid.

### Exact board weight is unknown pre-inspection
A 5-AZN board is not automatically profitable. Weight after required removal of batteries/heatsinks/metal parts must be measured under the buyer's actual acceptance rules.

### Category/condition matters
A board may be incomplete, stripped of valuable components or classified into a much lower-paying category. Public headline maximum cannot be used as a floor.

### Active-listing freshness
Some indexed marketplace pages may become inactive quickly. SUCCESS must use a still-active seller offer at execution time.

## Current conclusion
H078 validates a **real local deterministic-arbitrage architecture** with unusually low acquisition cost and low logistics:

`5-AZN broken board -> exact local recycler classification/weight -> immediate official payout`.

The economics can be positive at surprisingly small weights if the actual buyer rate is near the current market anchor, but strict SUCCESS is not yet proven because no exact active board has simultaneously had:
- current seller ask locked;
- exact buyer classification/weight;
- transaction-specific immediate payout locked;
- all costs locked.

Status: **NOT SUCCESS**.

## Reopen condition
Reopen H078 only with transaction-level evidence: exact active board + seller ask + buyer-side weight/category + fixed payout before seller payment. Do not repeat generic marketplace searching without pairing the item to a buyer quote.
