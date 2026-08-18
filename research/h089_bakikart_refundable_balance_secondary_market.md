# H089 — BakıKart refundable-balance secondary-market arbitrage

Updated: 2026-08-19
Status: **MECHANISM VALIDATED / LIVE SPREAD OBSERVED / CONTRACTUALLY REJECTED AS EXECUTABLE GUARANTEE**

## Question
Can a discounted secondary-market BakıKart with positive stored balance be bought below balance and immediately redeemed for cash at face value, creating a deterministic local arbitrage?

## Primary operator terms
Official BakıKart card terms (dated 2024-12-29 on the operator site) establish several unusually strong redemption properties for the unlimited-use physical card:

1. the card is anonymous;
2. any person holding/using a transferred card can become its user;
3. the balance of an unlimited-use card can be refunded;
4. refund is performed immediately after written application at BakıKart Card Analysis Centers, with card + identity document required;
5. balance loaded through the app is refunded cashlessly to the original bank card;
6. **resale of the card is explicitly prohibited**;
7. obtaining the card outside the methods/locations provided in the terms is also prohibited.

Primary source:
- https://www.bakikart.az/Home/CardTerms

These clauses mean the payout side is close to deterministic for a valid qualifying card/balance, but the discounted-acquisition side cannot be assumed lawful/contract-permitted when it relies on buying the card from a secondary seller.

## Live market observation
A currently indexed Lalafo listing from Baku (created 2025-12-15) advertised:
- BakıKart balance: **23 AZN**;
- ask: **20 AZN**;
- seller text: urgent sale and possible further discount.

Source:
- https://lalafo.az/baku/ads/bakikart-ictimai-nqliyyat-karti-id-79644640

Naive gross spread if secondary purchase and face-value refund were both permitted:

`23 - 20 = 3 AZN`

Gross return on acquisition cost:

`3 / 20 = 15%`

This is economically real evidence that positive-balance cards can appear below stored value in the local secondary market.

## Why this is NOT SUCCESS
The same operator terms that create the refund entitlement also block the obvious acquisition path:
- card resale is explicitly not allowed;
- acquisition outside the prescribed official channels is prohibited.

Therefore the transaction `buy discounted secondary-market card -> redeem balance` cannot be treated as a contract-compliant guaranteed arbitrage.

A free/gift transfer is conceptually different because the terms separately contemplate giving a card to another person and the recipient becoming a user. But no deterministic, scalable, contract-safe source of positive-balance cards for zero cost has been identified. Finding/discard recovery also raises ownership/legal-fact questions and is not accepted as a guaranteed strategy.

## Classification
- Deterministic redemption mechanism: **VALIDATED**.
- Live positive secondary-market spread: **VALIDATED OBSERVATION**.
- Contract-safe discounted acquisition: **REJECTED for resale route**.
- Strict executable guaranteed profit: **NO**.

## Generalizable lesson
Stored-value instruments can have deterministic face-value redemption while still blocking arbitrage through transfer/resale restrictions. Future stored-value screens must test both legs:

1. binding redemption entitlement;
2. permitted discounted acquisition / transfer.

A positive numerical spread is insufficient if the acquisition route violates the governing instrument terms.
