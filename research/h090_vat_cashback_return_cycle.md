# H090 — Azerbaijan VAT cashback + merchandise return cycle

Updated: 2026-08-19
Status: **EXACT CIRCULAR-ARBITRAGE REJECTION**

## Question
Can Azerbaijan's `ƏDV geri al` consumer VAT cashback be converted into deterministic profit by buying an eligible product, collecting the VAT refund, and then returning the product for the purchase price?

## Current official rule
The State Tax Service's current guidance states that eligible consumer purchases can receive a portion of VAT back after the statutory waiting period. Current published rates:
- cashless purchase: **17.5% of the VAT amount**;
- cash purchase: **5% of the VAT amount**.

The same official guidance explicitly addresses merchandise returns:
- if VAT cashback has **not** yet been returned, the full purchase amount is refunded;
- if VAT cashback **has already been returned**, the merchandise refund is reduced by the VAT-cashback amount already paid.

Primary source:
- https://taxes.gov.az/az/page/ticaret-ve-ya-iase-obyektlerinden-alinmis-mallara-gore-odenilmis-edv-nin-qaytarilmasi

## Exact identity
Let:
- `P` = purchase price paid;
- `R` = VAT cashback actually credited.

If the product is returned after cashback has already been paid, the official rule makes the merchant refund:

`P - R`

Total cash recovered across the two legs is therefore:

`R + (P - R) = P`.

Net cycle profit before any friction:

`P - P = 0`.

If there are any bank cash-out charges, transport, time cost, return restrictions, price differences or failed-return branches, the outcome becomes negative.

If the product is returned before cashback is paid, the full purchase amount is refunded but there is no retained cashback, so profit is again zero before friction.

## Conclusion
The apparent loop `buy -> receive VAT rebate -> return item` is **exactly neutralized by the return rule**. The state rebate and merchant refund are coordinated so the consumer cannot retain both the full purchase refund and the cashback.

Status:
- subsidy mechanism: **REAL**;
- circular buy/refund arbitrage: **REJECTED BY EXACT ACCOUNTING IDENTITY**;
- strict guaranteed positive profit: **NO**.

## Generalizable control
Whenever a cashback/subsidy is tied to a reversible purchase, always test whether cancellation/return settlement claws back or offsets the subsidy. A headline cashback percentage is not an arbitrage unless the principal-return leg is independent of the subsidy.
