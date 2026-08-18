# H074 — Baku local gold-scrap arbitrage

Updated: 2026-08-18
Status: **LOCAL DETERMINISTIC RESALE MECHANISM IDENTIFIED; LIVE BELOW-REFERENCE ANOMALIES FOUND; BINDING PRE-PAYMENT BID NOT YET LOCKED — NOT SUCCESS**

## Question
Can second-hand gold in Baku be acquired below a simultaneously locked scrap/buyer bid, with authenticity, fineness and weight verified before irreversible payment, so that resale produces a strictly positive cash floor?

This class differs from lottery EV and from speculative gold trading. A qualifying transaction can be deterministic if the resale buyer tests the item, weighs it, and gives a binding immediate-cash bid **before** the acquisition payment becomes irreversible.

## Current market anchors
A Baku jeweller quoted by BAKU.WS on 2026-08-05 reported a current purchase price of **129.5 AZN/g for 585 gold** and 165.76 AZN/g for 750 gold.

Source:
- https://baku.ws/social/qizil-alib-satmaq-isteyenlerin-diqqetine-bahalasdi

A current gold-buyer listing independently confirms the execution model needed for a strict transaction: free testing, weighing in front of the customer, and immediate on-site cash payment. Its 2026-05-30 posted 585 range was 135–142 AZN/g, but the exact web-posted rate is stale and must **not** be used as a present binding bid.

Source:
- https://lalafo.az/shirvan/ads/qizil-v-gumus-alisi-qiymtlr-yenilndi-30-may-2026-id-113473024

Another active Baku buyer advertises 585 purchase and immediate on-site cash, explicitly warning that prices change during the day. This supports the need for a transaction-time bid rather than a historical quote.

Source:
- https://lalafo.az/baku/ads/qizil-alisi-xidmti-id-51298069

## Current marketplace screen
Lalafo search pages crawled in August 2026 show several 585-gold offers that warrant an atomic in-person test.

### Candidate A — 1 g at 128 AZN
A current search result shows a **585, 1 g** bracelet at **128 AZN**.

Against the 2026-08-05 reference buy price of 129.5 AZN/g:
- gross reference spread = **1.50 AZN**;
- only **1.16%** of purchase price;
- this is too small to survive normal execution uncertainty and is **not** a strict candidate without a higher locked bid.

Search source:
- https://lalafo.az/baku/aksesuarlar/chasy-i-ukrasheniya/bilerzikler/q-585-qizilin-lom-qiymeti-2026

### Candidate B — metadata anomaly at 170 AZN
The same current marketplace repeatedly exposes a 585 bracelet at **170 AZN** with metadata rendered as `423 g`.

Search sources:
- https://lalafo.az/baku/aksesuarlar/chasy-i-ukrasheniya/bilerzikler/q-585-ayar-qizilin-qiymeti
- https://lalafo.az/baku/aksesuarlar/chasy-i-ukrasheniya/bilerzikler/q-585-qizilin-lom-qiymeti

The search index frequently renders decimal jewellery weights without the decimal separator (for example professional-store rows such as `950 g` at 2,380 AZN are economically consistent with 9.50 g, not 950 g). Therefore `423 g` may plausibly represent **4.23 g**, but this is only an inference and must not be treated as verified data.

If — and only if — the true tested net gold weight were 4.23 g at 585 fineness and a buyer simultaneously locked 129.5 AZN/g, then:

`locked resale = 4.23 * 129.5 = 547.785 AZN`

`gross spread = 547.785 - 170 = 377.785 AZN`

That magnitude is large enough to be economically interesting, but the listing anomaly is precisely why physical assay and weight verification are mandatory. The web row alone does not prove a real arbitrage.

## Strict atomic execution protocol
A terminal-success transaction must satisfy all gates **before paying the seller**:

1. Seller agrees to meet at a reputable gold buyer/assayer.
2. Buyer verifies authenticity and fineness (not merely the stamped hallmark).
3. Stones/non-gold parts are excluded from payable weight.
4. Buyer weighs the payable gold in front of both parties.
5. Buyer states a **binding immediate-cash bid** `B` for this exact item.
6. All irreversible transaction/transport/tax costs `C` are bounded.
7. Seller's final price `P` is fixed.
8. Proceed only when `B - P - C > 0` with a chosen safety margin.
9. Ideally settle as a three-party same-location transaction: buyer cash is available before seller payment is released.

This protocol neutralizes the largest failure modes: fake gold, lower fineness, hollow/stone weight, stale gold price, and a buyer changing the quote after the purchase.

## Deterministic formula
For one item:

`profit_floor = binding_buyer_bid - seller_price - irreversible_costs`

A strict guarantee exists only if all three values are locked before seller payment and:

`profit_floor > 0`.

For a per-gram bid `b`, verified payable gold weight `w`, seller price `P` and costs `C`:

`profit_floor = b*w - P - C`.

## Why this is not terminal SUCCESS yet
The mechanism is locally executable in Baku in principle and avoids H073's Germany/Azerbaijan geography problem. However the web evidence does not provide a **binding transaction-time buyer bid for the exact candidate item**, and Candidate B's indexed weight is ambiguous. Therefore no irreversible-purchase-safe positive floor has yet been proven.

Current classification:
- local buyer/testing/cash-exit mechanism: **validated**;
- live marketplace anomalies: **validated as leads**;
- exact candidate authenticity/weight: **unverified**;
- simultaneous binding buyer bid: **not locked**;
- terminal SUCCESS: **NO**.

## Reopen / advance condition
Advance H074 only with a genuinely new execution-level fact:
- an exact live listing with unambiguous weight/fineness and price;
- seller acceptance of pre-payment assay;
- transaction-time binding cash bid from the buyer after assay;
- all-in cost cap preserving a strictly positive margin.

Do not repeatedly compare marketplace asks with spot/reference prices without the atomic assay+bid gate.