# H155 — pre-announced Keno boost / multiplier timing screen

Updated: 2026-08-21
Status: **NO SUCCESS / SCHEDULED PROMOTIONS FOUND, BUT CURRENT BOOSTS ARE RANDOM-TICKET OR RANDOM-DRAW STATES, NOT PRE-PURCHASE FIXED OVERLAYS**

## Question
H154 found KenoGO Jackpot paytable states that would make complete 1-Spot coverage profitable if the enhanced state were known before entry. H155 searches for the missing execution order:

`enhanced state publicly fixed -> player buys complete cover -> draw`.

The key distinction is between a *scheduled promotion window* and a *guaranteed enhanced payout for every eligible ticket*. A promotion can be known in advance while the actual Doubler/Tripler remains randomly assigned after/at purchase, which does not create a strict floor.

## 1. Pennsylvania Keno — current August 2026 Doubler/Tripler promotion

Official Pennsylvania Lottery August 2026 retailer promotion sheet states that players buying any 4-SPOT Keno ticket, with or without Keno Multiplier, during specified Thu/Fri/Sat 8pm–midnight windows have **a chance** to have prizes doubled or tripled.

Source:
- https://www.palottery.pa.gov/PaLotteryWebSite/media/Retailer-Documents/Coupon-Promos/August2026_Coupon-Offers.pdf

The current PA game guide gives the $1 4-Spot paytable:
- 4/4 = $100
- 3/4 = $3
- 2/4 = $1
- otherwise $0

Source:
- https://www.palottery.pa.gov/PaLotteryWebSite/media/Page-Images/Game%20Guide/Game-Guide.pdf

For a uniform complete cover of every `C(80,4)` 4-Spot selection, deterministic return equals the single-ticket expectation by symmetry. Exact hypergeometric calculation gives base return:

`R_base = 0.6487183702373576 = 64.871837%`.

Therefore, if **every ticket in the cover were guaranteed** to receive a no-cost multiplier:
- universal 2x => **129.743674%**, a true pre-tax deterministic overlay before liability/tax/execution checks;
- universal 3x => **194.615511%**.

This proves the current PA paytable itself is strong enough for the desired mechanism.

However the current promotion wording is expressly *chance-based*. It does not announce that all eligible tickets in a future draw/time block receive 2x or 3x. Thus the known state is only `promotion active`, not `our basket multiplier = 2x/3x`. A lawful branch remains in which the purchased cover receives no boost, returning only 64.87%.

**Result: strong arithmetic lead, strict guarantee rejected for the current promotion.**

## 2. Maryland Keno Sprinkler — same ownership/timing failure

Maryland Lottery 2026 marketing material describes Keno Sprinkler promotions where Doubler/Tripler messages are produced on an **Nth-ticket basis**. If the player's numbers win, that ticket's winnings are doubled/tripled.

Current-period source showing the mechanism:
- https://www.mdgaming.com/wp-content/uploads/2026/02/Directors-Report-Sales-and-Marketing-February-PDF.pdf

Historical/current administrative reporting uses the same architecture: specific tickets receive Doubler/Tripler messages rather than a future draw being universally boosted.

Because unrelated statewide purchases can occupy Nth positions, the player cannot pre-own the enhanced state before committing to a complete basket. This is structurally analogous to H131 statewide Nth-ticket coupon failure.

**Result: rejected as strict deterministic subsidy.**

## 3. Connecticut KENO BONUS — multiplier is part of the draw, not a pre-entry state

Connecticut's official Keno rules define the Bonus Multiplier as a number selected by the lottery system prior to each drawing; the formal `Drawing` includes selection of the Bonus Multiplier and winning numbers. The current play page says the multiplier is randomly selected *just before each drawing* and tickets cannot be voided once printed.

Sources:
- https://www.ctlottery.org/Content/pages/55/Official%20Keno%20Game%20Rules-FINAL%20GO%20LIVE.pdf
- https://ctlottery.org/KENO/WatchDrawings/

Current CT 1-Spot base prize is $2.50 on a $1 play. Buying all 80 base 1-Spots costs $80 and guarantees 20 winners = $50, i.e. 62.5% base cover. Buying BONUS doubles the ticket cost, so a full BONUS cover costs $160. The strict permitted multiplier branch includes `1x/No Bonus`, so strict gross floor is only $50/$160 = **31.25%**.

Temporary promotions that merely add another possible multiplier (for example a 7x value) improve distribution/EV but do not remove the 1x branch. They therefore cannot create an all-state guarantee unless the multiplier itself is fixed and visible before ticket commitment.

**Result: hidden/random draw-state class rejected for strict guarantee.**

## 4. Oregon Special Keno — player-selectable and pre-fixed, but paytable remains sub-100%

Oregon provides a useful control because `Special Keno` is selected by the player before the draw and has a fixed alternative paytable at no additional base cost. That is the desired timing architecture.

Official/current sources:
- https://www.oregonlottery.org/jackpot/keno/
- https://secure.sos.state.or.us/oard/viewAttachment.action?ruleVrsnRsn=28986

But current published data show Special Keno overall payout around 64.09%, and its 1-Spot remains $2.50 on a $1 wager, so full 1-Spot cover is only **62.5%**. The enhanced upper-tier structure does not produce a deterministic >100% complete-cover portfolio.

**Result: execution architecture validated, economics rejected.**

## General timing theorem from H154-H155
A Keno promotion can create a strict full-cover overlay only if all of the following are true before irreversible purchase:
1. the exact enhanced paytable/multiplier for the target draw is publicly fixed;
2. the enhancement applies to **every required ticket** in the cover, not merely a random/Nth subset;
3. the boosted deterministic complete-cover ratio exceeds 100% after ticket cost;
4. the complete basket can be accepted under purchase/transaction limits;
5. liability caps / external winner prorating cannot reduce the floor below cost;
6. taxes and fees preserve positive net cash.

Current H155 cases fail at 1/2 (PA, MD, CT) or 3 (Oregon).

## Important quantitative trigger
Pennsylvania 4-Spot is now a high-value monitor target because the current base complete-cover ratio is **64.871837%**. Any future **universal, pre-announced no-cost 2x** period would mathematically produce **129.743674%** gross before secondary gates. This is a much lower threshold than many prior Keno targets.

## Conclusion
No current terminal SUCCESS.

The search did uncover a very actionable target class: **pre-announced universal Keno prize doublers on base paytables above 50%**. Pennsylvania 4-Spot already clears the required base threshold by a wide margin. Current August-2026 PA/MD mechanics, however, award enhancements only probabilistically/Nth-ticket, while CT resolves the multiplier as part of the draw and Oregon's deterministic selectable special paytable remains below 100%.

## Next action
1. Search official future-dated Keno promos for wording like `all prizes doubled`, `every ticket`, `2X all Keno prizes`, with no extra wager cost.
2. Prioritize jurisdictions with base fixed-paytable complete-cover >50%, especially PA 4-Spot (64.87%), Virginia 1-Spot (75%), La Vista special structures (81.06%).
3. For any universal doubler, immediately verify basket limits, same-draw ticket capacity, liability caps/proration, tax, and cancellation/acceptance timing.
4. Continue Nebraska/community scheduled-special recovery because a fixed future paytable is already the correct architecture.