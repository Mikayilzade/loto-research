# H249 — Jackpocket lottery credits × Maine Pick 3 Single Digit full-cover conversion

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: **PROMISING MECHANISM / DATA-BLOCKED / NOT SUCCESS**

## Question
Can non-withdrawable lottery promotional credit be converted into a **strictly guaranteed positive cash payout** by spending it on a fully controlled finite lottery partition whose every draw produces a known winner?

## New finite-space target: Maine Pick 3 Single Digit
The current official Maine State Lottery Pick 3 page lists a **50¢ Single Digit** wager paying **$2.50**. A Single Digit bet selects one digit in one exact position of the three-digit draw.

For any fixed position, buy all ten digits `0..9`:

- controlled lines: `10`;
- face cost: `10 × $0.50 = $5.00`;
- exactly one line wins every draw;
- guaranteed gross cash prize: **$2.50**;
- base deterministic return: **50%**;
- base deterministic net: **-$2.50**.

This is much smaller than ordinary Pick 3 Straight full coverage and creates a low subsidy hurdle.

## Exact credit-conversion theorem for this cover
Let:

- `C = $5.00` face cost of the ten-line cover;
- `P = $2.50` guaranteed cash payout;
- `B` = deterministic promotional credit that can pay the controlled ticket face cost dollar-for-dollar;
- `F` = all service/checkout fees required for the cover;
- `A` = any irreversible cash acquisition cost required to obtain the promotion.

Then the strict guaranteed net is

`G = P - max(0, C-B) - F - A`.

For `0 <= B <= 5`, this becomes

`G = B - 2.50 - F - A`.

Therefore a qualifying credit converts this cover into positive guaranteed cash iff

`B > 2.50 + F + A`.

If `B >= 5`, the face stake can in principle be fully subsidized and

`G = 2.50 - F - A`.

Thus a genuine unrestricted **$5 draw-ticket credit** is arithmetically enough to create a positive cash floor before fees/acquisition costs. A $10 credit has additional arithmetic margin, but only if it is actually current, deterministic, eligible, usable on this wager type, and not clawed back.

## Jackpocket evidence
### 1. Maine Pick 3 is currently orderable through Jackpocket
Jackpocket's current Maine page lists Maine Pick 3 among the official games it offers and explains that orders are fulfilled through an official Maine lottery retailer. Its current Maine results page also exposes `ORDER NOW` for Pick 3 Day and Evening.

This establishes game-level availability, **not** that Jackpocket's order UI exposes Maine's Single Digit wager menu.

### 2. Promotional lottery credits can produce withdrawable winnings
Recent official Jackpocket promotion terms explicitly state that Lottery Credits themselves are nonwithdrawable/noncash, while **winnings earned from tickets ordered with Lottery Credits are unrestricted and may be withdrawn**.

A particularly relevant 2026 promotion gave eligible new customers **$10 in Lottery Credits** after a qualifying $5 deposit or $1 first order. Maine was an eligible jurisdiction. However that promotion ran only **2026-03-02 through 2026-05-03** and required the customer to receive the offer, so it is expired as of this packet.

A separately published funding-match rules page includes Maine and describes a $5 credit after a qualifying funding transaction, but it states that the promotion exists only `from time to time` with dates supplied in the particular offer; it is not evidence of a currently open universal promotion on 2026-08-24.

The generic new-customer free-ticket terms found in the current site index are also not a current executable proof: one dated version expired in 2025, while another template has offer/code-specific timing and broad operator discretion.

### 3. Service fee is real and presently unbounded for Maine
Jackpocket's current support page states that it charges a **service fee either at deposit or checkout**. The exact Maine fee applicable to this ten-line Pick 3 Single Digit construction was not recovered from public primary material in this run.

The arithmetic margin under a fully subsidized $5 face cost is only `$2.50 - F - A`, so the exact fee and any irreversible promo acquisition spend are terminal inputs.

### 4. Promotion-discretion gate blocks strict guarantee
Recent Jackpocket promotion terms reserve broad rights to determine promotion abuse/eligibility in Jackpocket's sole discretion, withhold rewards, and suspend/modify/cancel promotions. The published 2026 $10-credit offer contains this language explicitly.

For this research project's terminal standard, a construction cannot be called guaranteed if the operator can lawfully remove the subsidy in the very branch where the user deliberately converts credits through a sure-cover portfolio.

## Execution gates still missing
The arithmetic conversion is valid, but **SUCCESS is not established** because all of the following must be proven simultaneously:

1. a **currently active** deterministic public Jackpocket credit/discount of more than `$2.50 + F + A` for a qualifying user;
2. Maine eligibility for that exact active offer;
3. the Jackpocket Maine Pick 3 order interface allows **Single Digit** wagers, not merely Pick 3 Straight/Box;
4. all ten complementary digits for one fixed position can be placed for the same draw;
5. the promotional credit applies to those wagers and to enough of the order to satisfy the theorem;
6. exact service/deposit/checkout fees leave `G>0`;
7. no offer-specific playthrough or other requirement creates additional unavoidable loss;
8. reward/order cannot be lawfully withheld/cancelled under a promotion-abuse or discretionary clause after the sure-cover construction;
9. all ordinary jurisdiction, physical-presence, age, account and tax conditions are satisfied.

## Controls
- Maine Pick 3 Front Pair also has an exact partition, but `100 × $0.50 = $50` guarantees only `$25`; it needs a much larger subsidy and is inferior to Single Digit.
- Ordinary Pick 3 Straight cover is likewise much more capital-intensive and adds no advantage for credit conversion.
- Maine Cash POP has a `PLAY ALL` guaranteed-prize mechanic, but Jackpocket's current Maine offered-game list does not list Cash POP, so it was not imported into this courier-credit construction.

## Verdict
**NOT SUCCESS.** H249 identifies a new and unusually low subsidy hurdle: a controlled Maine Pick 3 Single Digit cover can turn sufficiently large draw-ticket credit into deterministic cash. Historical/recent Jackpocket credit offers were arithmetically large enough, and winnings from credit-funded tickets are withdrawable. But no current public offer on 2026-08-24 was proven to satisfy the necessary amount/eligibility conditions, exact Maine service fees are unresolved, Single Digit UI support is unproven, and Jackpocket promotion terms retain discretionary cancellation/abuse gates incompatible with a strict all-branches guarantee.

## Reopen condition
Reopen immediately if primary evidence shows a **current** Maine-eligible deterministic credit/discount and the actual order UI confirms Single Digit support. Then capture the exact checkout total/fee before purchase and the exact promotion contract. The numerical gate is already fixed: `B > 2.50 + F + A`.

## Sources
- Maine State Lottery Pick 3: https://www.mainelottery.com/games/pickThreeDailyNumbers.shtml
- Jackpocket Maine lottery page: https://jackpocket.com/states/maine-lottery
- Jackpocket Maine results/order page: https://lottery.jackpocket.com/en/lottery-results/maine
- Jackpocket 2026 order-$1/get-$10 terms: https://cms.jackpocket.com/tos/order-1-get-10/
- Jackpocket funding-match rules including Maine: https://cms.jackpocket.com/tos/funding-match-promotion-official-rules-10for5/
- Jackpocket current fee FAQ: https://support.jackpocket.com/jp/en/are-there-any-fees?id=kb_article_view&sysparm_article=KB0010131
- Jackpocket generic draw-credit/free-ticket terms: https://cms.jackpocket.com/tos/free-ticket-promo/
- Jackpocket promo-code FAQ: https://support.jackpocket.com/jp/en/how-do-i-apply-my-jackpocket-promo-code?id=kb_article_view&sysparm_article=KB0010015
