# H195 audit append — Rhode Island Keno execution interface differential

Updated: 2026-08-23
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H195 RI iKeno bulk-cart execution** | compare current official Keno purchase UI against same-platform Mega Millions purchase UI | Keno exposes one `Pick your numbers` -> amount -> consecutive games -> options -> `Buy Now` flow with no visible `QTY` or `Add to cart`; Mega Millions explicitly exposes both `QTY` and `Add to cart` | **MATERIALLY WEAKENS BULK EXECUTION; NOT FORMAL IMPOSSIBILITY**; `research/h195_ri_keno_bulk_cart_interface_differential.md` |
| **H195 H175 throughput lower bound** | assume generously that all 4,336 independently specified selections may be submitted across a full 240-second Keno interval | requires **18.0667 completed submissions/sec**; H173 4,560-play cover requires **19.0000/sec** | **EXECUTION BLOCKER STRENGTHENED; undocumented batch/API/retailer mechanisms remain unexcluded** |
| **H195 current Kick Back promo control** | test whether homepage phrase `Get a free ticket when you buy 2` can safely be attributed to `Kick Back with Keno Promotion` | dynamic homepage/carousel mapping does not establish that association; recovered click resolved elsewhere | **DO NOT ASSUME subsidy terms; promo remains OPEN/data-blocked** |

Conclusion: no guaranteed executable lottery strategy yet. Public iKeno evidence now points more strongly toward per-selection submission rather than arbitrary same-draw cart packing, but hidden/batch execution has not been formally ruled out.