# H167 audit append — NC retailer promotional discount + forced Pick 3 Double Draw

Updated: 2026-08-22

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H167 NC Pick 3 forced Double Draw + retailer-authorized draw-ticket discount** | Use NCEL Draw Game Rule 2.02(J)(1) to transfer part of the statutory 7% retailer economics to an independent customer as a pre-agreed promotional discount; customer buys all 100 $0.50 Front Pair outcomes on a guaranteed Double Draw evening | Base cover: $50 face -> exactly $50 guaranteed prizes. Under simplified 21% federal + 2% NC C-corp tax screen with 90% loss deduction, after-tax surplus is `39.65*d - 1.15` dollars per $50 cover, so break-even discount is **2.9004%**. At 5% discount modeled after-tax surplus ≈ **$0.8325**; at 7% ≈ **$1.6255**. Retailer retains `7%-d` of face before other costs. | **STRONG CONDITIONAL OVERLAY / NOT SUCCESS.** Official NCEL rules validate retailer promotional discounts reported at full gross value, removing the H166 own-store commission dependency. Still unresolved: live forced-state lock, specific compliant retailer discount agreement, terminal/bulk rollback under partial issuance/outage, and taxpayer/entity-specific final costs. `research/h167_nc_retail_discount_double_draw.md`, `data/derived/h167_nc_discount_double_draw.csv`. |

Do not repeat H166's broad retailer-play legality test. H167 supersedes the need for retailer self-play if an independent customer discount can be contractually fixed before purchase.
