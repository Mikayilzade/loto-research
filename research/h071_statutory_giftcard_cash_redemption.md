# H071 — statutory gift-card cash redemption arbitrage

Updated: 2026-08-18
Status: **MECHANISM VALIDATED / CURRENT EXECUTION NOT YET LOCKED / NOT SUCCESS**

## Question
Can a discounted closed-loop gift card be acquired below a statutory cash-redemption threshold and then redeemed for face-value cash, producing a deterministic positive cash floor?

## Current statutory anchor — California
California SB 22 amended Civil Code section 1749.5. The operative rule from **1 April 2026** requires a qualifying gift certificate / gift card / electronic gift card with a cash value **less than $15** to be redeemable in cash for its cash value.

Primary source:
- California Legislature, SB 22 (2025–2026): https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB22
- Civil Code definition includes electronic gift cards and excludes qualifying multi-seller cards: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1749.45.

Merchant implementation cross-check:
- McDonald's current cash-out table, stated current as of 2026-04-01, lists California threshold as **less than $15** and multiple other states with smaller mandatory thresholds: https://www.mcdonalds.com/us/en-us/arch-card-cash-out.html

## Arbitrage theorem
Let:
- `B` = valid redeemable card balance;
- `T` = statutory cash-redemption threshold;
- `P` = irreversible acquisition price;
- `C` = all execution/travel/payment costs.

If all of the following are locked before payment:
1. the card is in-scope under the statute;
2. `B < T` where the threshold is strict;
3. balance/authenticity is verified and cannot be clawed back after purchase;
4. the holder is legally entitled to cash redemption;
5. redemption is operationally available;
6. `P + C < B`;

then deterministic cash profit is:

`profit = B - P - C > 0`.

This is not EV and contains no lottery/random outcome once the gates are locked.

Code:
- `src/loto_research/giftcard_cash_redemption.py`
- `tests/test_giftcard_cash_redemption.py`

Example only: a valid California in-scope card with balance $14.99, acquired for $13.50 with $0.25 total execution cost, has a conditional cash floor of `$14.99 - $13.50 - $0.25 = $1.24`.

## Secondary-market evidence
A functioning discounted secondary market exists. CardCash states that it buys unwanted cards below face, resells them at a discount, verifies cards, and offers a 45-day buyer-protection process. Current pages show discounts across many brands, including double-digit discounts for some merchants.

Sources:
- https://www.cardcash.com/faqs/sell-gift-cards
- https://www.cardcash.com/buy-gift-cards/discount-american-girl-cards/
- https://www.cardcash.com/buy-gift-cards/discounted-health-beauty-cards/

Historical evidence also shows small denomination inventory can occur (e.g. a documented $10 AMC card at a discount), proving the economic configuration is not structurally impossible. However this historical listing is **not** treated as a current executable opportunity.

## Why this is not SUCCESS yet
The theorem is valid, but the current execution gate is not locked.

### 1. Current small-balance inventory is not proven
The public pages found today prove discounted inventory, but not a currently purchasable qualifying card with `B < $15` at a price sufficiently below balance after all costs.

A larger discounted card does not automatically create a standalone guarantee: spending it down to below $15 requires consuming goods/services or another conversion step, and that intermediate value cannot be treated as cash without its own guarantee.

### 2. Buyer protection is not the same as pre-payment irreversibility
CardCash describes a 45-day refund process if a purchased card has a balance discrepancy. That reduces risk but does not prove the card cannot later be invalidated, frozen, or disputed before cash redemption. Terminal SUCCESS requires the positive floor to survive all contractually allowed branches, not merely offer a probable refund remedy.

### 3. Geographic / in-person execution
The California statutory right is useful only if the holder can actually invoke it at an in-scope merchant. Public material does not establish a remote redemption route that is guaranteed for a buyer located in Azerbaijan. Travel would overwhelm small balances unless execution is delegated or bundled lawfully at near-zero incremental cost.

### 4. Scope exclusions matter
California's definition excludes certain multi-seller cards; donated/promotional cards can also receive different treatment. Any live candidate must be checked against the exact statutory scope and issuer terms before payment.

## Quantitative execution gate
For a qualifying balance `B`, the maximum all-in purchase price for strict positive profit is `< B - C`.

Examples:
- if `B=$14.99`, `C=$0.25`, buy price must be **< $14.74**;
- if `B=$10`, `C=$0.50`, buy price must be **< $9.50** (discount >5%);
- if incremental execution cost is effectively zero, **any strictly positive locked discount** below face is mathematically sufficient.

## Conclusion
H071 establishes a new deterministic redemption class stronger than ordinary cashback or lottery EV:
- statutory cash floor: **validated**;
- discounted secondary market: **validated**;
- mathematical arbitrage condition: **proved**;
- current qualifying small-balance live card + pre-payment validity lock + practical redemption path: **not yet proved**.

Status: **VALIDATED MECHANISM / EXECUTION-GATED / NOT SUCCESS**.

Do not repeat generic gift-card-law searching. Reopen only for:
1. a current live in-scope card below the statutory threshold;
2. a purchase/escrow mechanism that locks balance and non-revocation before irreversible payment;
3. a guaranteed low-cost California redemption route; or
4. a jurisdiction with remote/electronic mandatory cash redemption that removes the geography cost.
