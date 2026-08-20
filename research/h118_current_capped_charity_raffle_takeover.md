# H118 — current capped charity/hospital raffle takeover screen

Updated: 2026-08-20
Status: **CURRENT CAPPED-SUPPLY CLASS MATERIALLY CLOSED / NO SUCCESS**

## Question
Can a current fixed-supply charity/hospital lottery or cash-calendar raffle be bought out completely so that the buyer owns every eligible ticket and therefore captures the entire fixed prize board for less than total acquisition cost?

This is a high-value structural class because, unlike open 50/50 draws, a hard ticket cap plus fixed prizes can in principle create a deterministic all-outcome floor. The strict favorable upper bound is:

`gross_floor <= total fixed prize board / minimum cost to acquire all eligible tickets`

For screening, all advertised prize value is granted at full face/retail value, taxes and execution costs are ignored, and the buyer is unrealistically assumed able to acquire the whole authorized supply. Therefore any ratio below 100% is a terminal rejection for the strict takeover guarantee; real execution can only worsen it.

## Current 2026 official screens

### 1. Roughrider & Children’s Hospital Foundations Main Lottery — Saskatchewan
Official rules state:
- maximum **96,500** Main Lottery tickets;
- cheapest standalone large pack: **20 for CAD 495** = CAD 24.75 per ticket;
- total advertised prize value: **CAD 2,039,994.37**;
- ticket purchasers must be in Saskatchewan.

Full authorized-supply cost at the best standalone unit price:

`96,500 × 24.75 = CAD 2,388,375`

Even granting the buyer the **entire** advertised prize board, including prizes from deadlines already passed, the favorable upper-bound return is:

`2,039,994.37 / 2,388,375 = 85.4135%`

This is intentionally too favorable: on 2026-08-20 the VIP deadline/draw has already passed, so a new buyer cannot actually capture all 1,012 advertised prizes. The true current takeover ratio is therefore lower.

Official source: https://www.riderschildrenslottery.ca/rules

**Result: REJECTED.** This was the closest current capped main-lottery candidate in the packet and still misses break-even by >14.5 percentage points before tax/execution.

### 2. Roughrider & Children’s Hospital Cash Calendar — Saskatchewan
Official rules state:
- max **264,400** Cash Calendar tickets;
- cheapest large pack **50 for CAD 100** = CAD 2 per ticket;
- fixed cash prize board **CAD 105,000**;
- at least one qualifying Main Lottery ticket is required.

Favorable takeover cost ignoring most linkage friction:

`264,400 × 2 + CAD 100 minimum Main ticket = CAD 528,900`

Fixed prize-board ratio:

`105,000 / 528,900 = 19.8525%`

Official source: https://www.riderschildrenslottery.ca/rules

**Result: REJECTED.**

### 3. Alberta Cancer Foundation Main Lottery 2026
Official rules state:
- max **352,500** main tickets;
- cheapest large standalone pack **36 for CAD 695** = CAD 19.3056 per ticket;
- total advertised retail prize value **CAD 4,038,679.88**;
- purchasers must be in Alberta.

Full authorized-supply cost:

`352,500 × 695 / 36 = CAD 6,805,208.33`

Favorable prize-board ratio:

`4,038,679.88 / 6,805,208.33 = 59.3469%`

Official source: https://albertacancerlottery.ca/rules/

**Result: REJECTED.**

### 4. Alberta Cancer Foundation Win Daily Cash 2026
Official rules state:
- max **976,500** tickets;
- cheapest large pack **100 for CAD 135** = CAD 1.35 per ticket;
- fixed cash prize board **CAD 460,000**.

Full authorized-supply cost:

`976,500 × 1.35 = CAD 1,318,275`

Favorable fixed-prize ratio:

`460,000 / 1,318,275 = 34.8941%`

Official source: https://albertacancerlottery.ca/rules/

**Result: REJECTED.**

### 5. SickKids 2026 Main Lottery — Ontario
Current official rules/search-indexed rules state:
- max **145,000** main tickets;
- cheapest standalone large pack **15 for CAD 675** = CAD 45 per ticket;
- advertised total prize value **CAD 4,172,666.50**;
- purchasers must be in Ontario.

Full authorized-supply cost:

`145,000 × 45 = CAD 6,525,000`

Favorable prize-board ratio:

`4,172,666.50 / 6,525,000 = 63.9489%`

Official source: https://www.sickkidslottery.ca/rules-and-regulations

**Result: REJECTED.**

The Combo/Super Combo bundles do not rescue a strict guarantee. They attach 50/50 and Cash Calendar tickets, but the 50/50 supply is uncapped and thus cannot be exclusively captured; counting its value as guaranteed would be invalid. The Cash Calendar itself is screened below.

### 6. SickKids 2026 Cash Calendar — Ontario
Current official rules state:
- max **1,260,000** Cash Calendar tickets;
- cheapest large pack **200 for CAD 150** = CAD 0.75 per ticket;
- fixed cash prize board **CAD 515,000**;
- a validated SickKids Main Lottery ticket is required.

Favorable takeover cost with only one minimum CAD 100 main ticket added:

`1,260,000 × 0.75 + 100 = CAD 945,100`

Fixed prize-board ratio:

`515,000 / 945,100 = 54.4916%`

Official sources:
- https://www.sickkidslottery.ca/rules-and-regulations
- https://www.sickkidslottery.ca/faq

**Result: REJECTED.**

## Structural conclusion
A hard cap alone is not enough. For a takeover guarantee the operator-funded fixed prize board must exceed the **minimum all-ticket acquisition cost**, after accounting for any required base ticket, taxes and execution.

The six current 2026 capped products screened here span favorable upper-bound returns of only **19.85%–85.41%**. Because the calculation already gives the buyer every fixed prize at full advertised value and ignores operational costs, each is terminally below the 100% guarantee threshold.

This materially closes the current Canadian hospital/charity capped-supply model as a likely buy-the-pot source. The class should be reopened only when one of the following is observed:
1. fixed prize board / cheapest full-supply cost > 100% before costs;
2. a deterministic external sponsor subsidy/rebate materially raises the floor above 100%;
3. a late-stage unsold-inventory discount lowers the cost of **all remaining eligible supply** while previously sold tickets are legally excluded from the relevant prize pool;
4. an unusually structured drawing guarantees multiple fixed payouts to the purchaser of a complete remaining set.

Open 50/50 raffles are not substitutes: their prize is generally a percentage of sales and external tickets remain eligible, so they do not create a deterministic takeover floor.
