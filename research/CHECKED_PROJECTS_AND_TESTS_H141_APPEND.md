# CHECKED PROJECTS AND TESTS — H141 APPEND

Updated: 2026-08-21
Scope: LOTTERY ONLY

| ID | Project / mechanism | Test | Result | Status / evidence |
|---|---|---|---|---|
| H141 | North Carolina checkout-level Lottery Offers | Verify whether official terms support whole-cart purchase subsidy applied before checkout completion | NCEL terms explicitly allow Lottery Offers on whole cart; qualifying Discount Offer immediately discounts ticket | **ARCHITECTURE VALIDATED**; `research/h141_north_carolina_checkout_offer_architecture.md` |
| H141 | 2026 NCEL cart promo precedent | Official `M4LDEAL26`: enter promo code on Shopping Cart page, then complete $10 purchase, receive free $5 ticket; repeatable in separate qualifying transactions | Proves purchase-level promo-code architecture exists, but offer expired July 1, 2026 and targets progressive/shareable game | **CONTROL VALIDATED / NOT CURRENT SUCCESS** |
| H141 | NC Pick 3 Exact complete cover | 1,000 outcomes × $0.50; winning Exact pays $250 | $500 face -> $250 guaranteed gross = **50%** deterministic cover | **100% deposit match only break-even before tax** |
| H141 | NC Pick 3 Pair complete cover | 100 pairs × $0.50; winning Pair pays $25 | $50 face -> $25 guaranteed gross = **50%** deterministic cover | **100% deposit match only break-even before tax** |
| H141 | Current NCEL Welcome Offer | 100% first-deposit match up to $50 usable on draw games including Pick 3 | mathematically insufficient for positive Pick 3 deterministic floor; also remains deposit/promo based rather than immediate cart discount | **REJECTED as terminal guarantee** |
| H141 | General checkout discount theorem | For cover ratio `r`, purchase discount `q` must satisfy `q > 1-r` for positive pre-tax floor | r=.50 needs >50%; r=.60 >40%; r=2/3 >33.33%; r=.75 >25% | **VALIDATED threshold**; `data/derived/h141_nc_checkout_thresholds.csv` |

Terminal status after H141: **NO SUCCESS; NOT EXHAUSTED**.

Next priority: current player-owned checkout Discount/BOGO offers paired with compact non-shareable games having deterministic cover ratio >60%.
