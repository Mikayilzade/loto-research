# H200 — RI Keno cart execution and operator-limit gate

Updated: 2026-08-23
Status: **NO SUCCESS; iLOTTERY CART EXISTS, STRICT EXECUTION GUARANTEE STILL BLOCKED**
Scope: LOTTERY ONLY.

## Target
Continue H199's Rhode Island Keno execution branch without repeating the rejected `$150 => 150 selections` shortcut. Determine whether current official iLottery documentation materially improves the same-draw bulk-execution case for H173/H175.

## Fresh official evidence
Current Rhode Island Lottery public materials establish several previously underused execution facts:

1. The official iLottery FAQ explicitly refers to **cart purchases** for draw games. It states that during draw-game offline/draw-break periods, wagers attempted as a result of cart purchases will not be accepted / will be voided.
2. The current site exposes a dedicated **Shopping Cart** page with Checkout and a purchase total.
3. The current Numbers purchase page exposes both **Add to cart** and **QTY** controls, proving that the cart is not merely decorative and that at least some draw-game wager flows support multi-wager purchase assembly.
4. The mobile-app page says users can **create and save favorite draw-game wagers**, replay favorites, and make **digital play slips** to scan at retailers.
5. Retailer News says the app can generate a **QR code** from wager selections; the QR can be scanned by a retailer terminal or self-service vending machine to purchase a draw-game ticket.

These points falsify the strongest version of H195's conservative model that every draw-game wager necessarily requires a fully independent manual purchase flow. Rhode Island has both cart-based iLottery checkout and retailer QR/digital-slip acceleration.

## New blocking evidence from current terms
The current official Rhode Island Lottery online terms/privacy text also states:

- the Lottery may **limit purchases of any game, ticket, and/or wager on a particular set of numbers at any time and without notice**;
- the Lottery is not liable for losses from a **delay in, or denial of, processing a purchase**;
- iLottery account play is subject to Lottery-set purchase limits in addition to user-defined responsible-gambling limits.

This is decisive for the terminal SUCCESS standard. Even if a cart can technically hold many Keno selections, a strategy that requires all 4,336 or 4,560 same-draw selections is not strictly guaranteed executable merely because they can be assembled in a cart. Before the entire basket is confirmed accepted for the target draw, the rules permit partial/denied/limited processing.

## Consequence for H173/H175
H173 requires 4,560 distinct same-draw 3-spot selections and H175 requires 4,336.

What H200 improves:
- multi-wager/cart infrastructure is real;
- saved favorites/replay and retailer QR generation reduce manual data-entry friction;
- H195's simple `4,336 separate Buy Now actions in four minutes` throughput estimate is no longer a safe lower bound.

What H200 does **not** establish:
- maximum Keno selections per cart;
- whether Keno exposes the same QTY semantics as The Numbers;
- whether one Keno cart can contain thousands of distinct manually specified selections;
- whether checkout is atomic (all accepted or none) for one target draw;
- a hard guarantee that purchase limits cannot intervene after partial basket acceptance;
- a retailer QR capacity large enough for the full H173/H175 basket.

## Strict-guarantee theorem for this route
For a coverage strategy whose profitability requires ownership of every member of a fixed same-draw basket `B`, the online route can support a strict guarantee only if, before exposure to the draw, there is authoritative evidence that either:

1. the complete basket is accepted atomically, or
2. the player can verify all members of `B` are accepted while still having enough time and a guaranteed right to repair any rejected subset.

Current RI terms explicitly reserve purchase-limitation and processing-denial powers, so neither condition is presently established.

## Verdict
**ЕЩЁ НЕ УСПЕХ.** H200 upgrades the execution model: Rhode Island iLottery does have draw-game cart purchases, favorites/replay and retailer QR play slips, but official terms reserve unannounced wager/purchase limits and processing denial. Therefore cart existence alone cannot certify guaranteed acquisition of the 4,336/4,560-play H175/H173 same-draw basket.

## Sources
- Rhode Island Lottery FAQ (cart purchases, favorites, online draw-game purchasing): https://www.rilot.com/en-us/player-zone/faqs.html
- Rhode Island Lottery Shopping Cart: https://www.rilot.com/en-us/shoppingcart.html
- Rhode Island Lottery The Numbers purchase page (QTY / Add to cart): https://www.rilot.com/en-us/the-numbers.html
- Rhode Island Lottery Mobile App page (favorites, digital play slips): https://www.rilot.com/en-us/player-zone/mobile-app.html
- Rhode Island Lottery Retailer News (QR wager selection scan at terminal/self-service): https://www.rilot.com/en-us/retailers-corner/retailer-news.html
- Rhode Island Lottery current online terms/privacy text (purchase limits; delay/denial): https://www.rilot.com/en-us/about-us/privacy-policy.html
