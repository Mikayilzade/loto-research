# H291 independent validation

Date: 2026-08-26
Result: **VALIDATED — NO CURRENT PUBLIC STRICT-PROFIT QUALIFIER**

Independent checks performed after writing the H291 model:

1. Outcome-space count: three ordered decimal digits give exactly `10^3 = 1,000` Straight outcomes.
2. One-copy $0.50 Straight cover therefore costs exactly `1,000 × $0.50 = $500`.
3. In every draw state, exactly one covered Straight equals the drawn ordered triple, so the cover has exactly one winning Straight and no draw-state dependence in its Straight gross.
4. With a $250 payout for the $0.50 Straight, invariant gross is exactly `$250`, hence base deterministic return `250/500 = 1/2 = 50%`.
5. If a deposit match of fraction `m` is fully spendable, cash acquisition cost is `500/(1+m)`.
6. Strict guaranteed cash profit requires `250 - 500/(1+m) > 0`, equivalent to `m > 1`.
7. Boundary tests:
   - `m=0.40`: cash $357.142857..., gross $250, loss $107.142857..., recovery 70%.
   - `m=1.00`: cash $250, gross $250, exact break-even.
   - `m=1.01`: cash $248.756218..., gross $250, profit $1.243781..., recovery 100.5%.
8. The public Michigan Lottery bonus FAQ documents variable/account-specific offers and sample match rates, but does not establish a current universal match above 100%.
9. The same FAQ's sample `Play $25 → $5 Bonus Cash` is a 20% one-off example; no public rule establishes repeatability across the $500 exact cover. It therefore cannot be multiplied by 20 as a guaranteed subsidy.
10. Current official Michigan documentation does confirm that withdrawable Bonus Cash is a distinct bonus type, so H291 should be reopened if a specific current eligible offer crosses the derived threshold.

No closure claim is made for all possible personalized Michigan offers. The validated claim is narrower: **the currently public, auditable bonus evidence does not establish a strict-profit exact-cover construction; a >100% fully spendable match (or equivalent deterministic cash subsidy) is required for this Daily 3 cover.**

Sources:
- https://help.michiganlottery.com/support/solutions/articles/158000441667-types-of-online-bonus-offers
- https://faq.michiganlottery.com/account-information-d9a19100/online-bonuses-f2b270a4/types-of-online-bonus-offers-08356151
- https://faq.michiganlottery.com/en/mobile-app-information-052d5f4e/general-mobile-app-faq-8406c09a/michigan-lottery-mobile-app-faq-673b607c
- https://audgen.michigan.gov/wp-content/uploads/2026/03/2025-Michigan-Lottery-Annual-Comprehensive-Financial-Report.pdf
