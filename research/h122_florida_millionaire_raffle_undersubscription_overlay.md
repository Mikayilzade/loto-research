# H122 — Florida Millionaire Raffle 2026 undersubscription overlay

Updated: 2026-08-20
Status: **HISTORICAL/RECENT +EV OVERLAY VALIDATED / STRICT GUARANTEE REJECTED / MONITORING CLASS OPEN**

## Question
Can a fixed-prize state-lottery raffle become structurally favorable when actual ticket sales finish far below the ticket cap, and can that overlay be converted into an all-outcome guaranteed profit?

## Primary-source facts
Florida Lottery Emergency Rule 53ER26-16 set:
- ticket price: **$20**;
- maximum supply: **2,000,000** tickets;
- four interim drawings, each paying **$704,500** across 2,498 winners;
- all tickets bought before a drawing remain eligible for all remaining drawings;
- final draw prize count depended on total ticket sales:
  - 1–1,000,000 sold -> **10 × $1,000,000**;
  - 1,000,001–1,500,000 -> **15 × $1,000,000**;
  - 1,500,001–2,000,000 -> **20 × $1,000,000**.

Official rules:
- https://secondchance.floridalottery.com/secondchance/millionaireraffle/rules.do

Florida Lottery's promotion page reported **369,180 tickets sold** when sales ended June 30, 2026.
- https://floridalottery.com/promotions/raffle

Official final results show exactly **10 $1,000,000 winners** on July 2, 2026, consistent with the <1,000,001 sales tier.
- https://secondchance.floridalottery.com/secondchance/raffle-winners.do?promotionId=149

## Aggregate overlay
Final ticket revenue:

`369,180 × $20 = $7,383,600`.

Fixed nominal prize board across all five drawings:

`4 × $704,500 + $10,000,000 = $12,818,000`.

Therefore the nominal prize board exceeded ticket sales revenue by:

`$12,818,000 - $7,383,600 = $5,434,400`.

This is a genuine operator-funded undersubscription overlay, not a player-funded jackpot illusion.

## Last-window ticket EV
A ticket bought during the final entry window before the fourth interim draw remained eligible for:
- fourth interim pool: **$704,500**;
- final pool: **$10,000,000**.

At final observed sales `N = 369,180`, pre-tax expected gross value per eligible ticket is:

`($10,704,500 / 369,180) = $28.99534`.

On a $20 ticket:

`pre-tax expected ROI = 28.99534 / 20 - 1 = +44.9767%`.

For the <=1,000,000-sales tier, the simple last-window pre-tax break-even sales count is:

`$10,704,500 / $20 = 535,225 tickets`.

Thus, if final sales can be observed/estimated below **535,225** while a ticket still qualifies for the fourth interim + final draw, the ticket is positive EV before tax, travel, claim friction and execution costs.

This is much stronger than ordinary jackpot-positive-EV states because the external subsidy is fixed by rule while the denominator can undershoot badly.

## Why this is NOT terminal SUCCESS
Positive aggregate overlay does **not** create an all-outcome player guarantee unless one controls enough of the eligible ticket set to force a minimum prize capture above acquisition cost.

### Full acquisition from launch
Buying all 2,000,000 available tickets would cost:

`$40,000,000`.

The maximum rule-defined fixed board at sellout is:

`$20,000,000 final + 4 × $704,500 interim = $22,818,000`.

Even total ownership from launch therefore returns at most **57.045% nominal gross** before tax/costs.

### Late buy of all remaining tickets
At the observed final undersubscribed state, unsold tickets simply expired; they were not eligible entries. A buyer could not retroactively acquire already-sold third-party tickets. Any late portfolio leaves external tickets in the draw pool.

Because the number of external tickets (369,180 in the final state) massively exceeded the number of prize-winning numbers (10 final millionaires and 2,498 fourth-draw winners), a legal outcome exists in which **all relevant winning numbers belong to external holders**. Therefore the strict prize floor for any portfolio that does not own all eligible sold tickets is zero.

The result is:
- **strong positive EV state:** validated;
- **strict all-outcome positive net floor:** rejected;
- **buy-the-pot guarantee:** impossible under the observed ownership structure.

## New reusable class
**Fixed-prize undersubscribed raffle overlay monitor.**

Screen future official raffles for all of the following:
1. prize board has a fixed minimum independent of sales;
2. live ticket-count is publicly observable before sales close;
3. ticket price and draw eligibility are fixed;
4. a late ticket enters one or more still-unplayed fixed-prize draws;
5. `remaining fixed prize pool / projected eligible ticket count > ticket price + tax/cost reserve`.

This can produce unusually strong +EV opportunities even when no guaranteed-profit takeover exists.

## Guarantee reopen condition
Only reopen as a terminal-guarantee candidate if a future raffle has one of:
- an assignable/unique finite ticket inventory where all **eligible sold tickets** can actually be acquired before draw;
- a deterministic minimum-prize allocation per block/pack of tickets;
- a rule ensuring every sufficiently large portfolio receives a minimum fixed payout;
- a fixed prize board exceeding the cost of complete eligible ownership.

Otherwise treat undersubscription as **EV-only**, not guaranteed arbitrage.

## Conclusion
Florida Millionaire Raffle 2026 is one of the strongest modern structural lottery overlays found in the project: the nominal fixed prize board exceeded final ticket revenue by about **$5.4344m**, and a final-window ticket had approximately **+$44.98% pre-tax expected ROI** at the observed final denominator. The mechanism nevertheless fails the project's terminal SUCCESS condition because external ticket ownership leaves a legal zero-payout branch for any incomplete portfolio.
