# H250 — courier-supported partial digit wagers and exact subsidy floor

Date: 2026-08-24
Result: **NOT SUCCESS / CURRENT SUBSIDY BLOCKED**

## Question
H249 found a very small exact lottery partition at retail: Tri-State Pick 3 Single Digit. H250 asks whether a lottery courier actually exposes the partial-digit bet menu, whether an even smaller/better deterministic partition exists among Single Digit / Pair / Straight variants, and whether any currently evidenced courier promotion crosses the exact subsidy hurdle.

## Primary/current game evidence

### Maine Lottery — retail baseline
Current Maine Pick 3 rules:
- wagers from $0.50 to $5;
- Single Digit pays $2.50 on a $0.50 wager and wins by matching one chosen digit in one exact position;
- Front/Back Pair pays $25 on $0.50;
- Straight pays $250 on $0.50;
- combinations of these bet types may be played on one ticket.

Source: https://www.mainelottery.com/games/pickThreeDailyNumbers.shtml

Current Maine Pick 4 also has a $0.50 Single Digit paying $2.50.
Source: https://www.mainelottery.com/games/pickFourDailyNumbers.shtml

Therefore exact full covers are:
- Single Digit: 10 lines × $0.50 = **$5 cost**, exactly one $2.50 winner → **50% deterministic return**;
- Pair: 100 lines × $0.50 = **$50 cost**, exactly one $25 winner → **50%**;
- Straight: 1,000 lines × $0.50 = **$500 cost**, exactly one $250 winner → **50%**.

Single Digit is therefore not a better return ratio than Pair/Straight, but it is the minimum-capital exact partition.

### Vermont and Minnesota confirm the structure is not Maine-specific
Current Vermont Pick 3 explicitly permits a Single Digit play, one selected digit in one selected position, from $0.50 to $5. Current displayed $0.50 payout is $2.50.
Source: https://vtlottery.com/games/pick-3

Current Minnesota Pick 3 explicitly offers First Digit, Front Pair, Back Pair and Straight. The official table gives First Digit $5 on a $1 ticket, odds 1:10, and retail play slips support $0.50 bets.
Source: https://www.mnlottery.com/games/lotto/pick-3

Thus the 10-cell exact-position partition recurs across multiple current state menus.

## Courier wager-menu evidence — blocker materially reduced
Lotto.com's current Maine Pick 3 page directly exposes:
- First Digit / Second Digit / Third Digit: **$5 prize**, odds **1:10**;
- Pair: $50, odds 1:100;
- wagers available at **$1, $2 or $5 per line**;
- up to **100 lines for each game**.

Source: https://me.lotto.com/tristatepick3/info/prizes

This is direct courier-side evidence that a controlled Single Digit partition is orderable in Maine. At Lotto.com's $1 minimum:
- 10 Single Digit lines cost **$10**;
- exactly one line pays **$5**;
- deterministic return = **50%**.

The 100-line Pair full cover also fits the public 100-line feature exactly: $100 spend → $50 deterministic gross. It has no better ratio, only higher capital.

Lotto.com also exposes Single Digit on Maine Pick 4.
Source: https://me.lotto.com/tristatepick4/info/rules

Jackpocket's current Maine state page lists Pick 3 as an orderable game, and its own Maine Pick 3 guide explicitly describes Single Digit mechanics. This is strong corroboration, although H250 does not treat the public blog alone as a machine-verifiable proof of the exact in-app bet selector.
Sources:
- https://jackpocket.com/states/maine-lottery
- https://blog.jackpocket.com/how-to-play-pick-3-in-maine/

## Exact subsidy thresholds
Let `B` be deterministic usable credit, `F` all courier/service/checkout fees, and `A` any irreversible cost required to acquire the promotion.

### Retail/Jackpocket-like $0.50 Single Digit cover
Cost = 5, deterministic gross = 2.50:

`G = 2.50 - max(0, 5-B) - F - A`

For `B <= 5`, strict profit requires:

`B > 2.50 + F + A`.

### Lotto.com $1 Single Digit cover
Cost = 10, deterministic gross = 5:

`G = 5 - max(0, 10-B) - F - A`.

For `B <= 10`, strict profit requires:

`B > 5 + F + A`.

For a percentage discount `d`, before fees/acquisition cost:

`G = 5 - 10(1-d) = 10d - 5`.

Strict profit therefore needs **d > 50%**. Exactly 50% only breaks even before fees; any positive fee makes it negative.

Consequences:
- 25% discount → $7.50 effective ticket cost, $5 gross → **-$2.50 before fees**;
- 20% discount → **-$3.00 before fees**;
- 10% discount → **-$4.00 before fees**.

## Current promotion scan
Lotto.com's current promotional terms state that percentage/fixed discounts and free-ticket offers remain subject to service fees and may be limited/cancelled. Its current Mystery Scratch (effective 2026-03-23) is random: listed possible rewards include $500/$20 site credit, Powerball BOGO, $2 bonus, 20% draw discount and 10% all-products discount. No reward is deterministic from participation, and even the listed 20% draw discount is far below the >50% Single Digit hurdle.

Source: https://www.lotto.com/promoterms

The previously studied public 25% Lotto.com draw discount is also below the exact hurdle even under the stronger assumption that it applies to the entire Single Digit cover.

Jackpocket has published promotions large enough to cross the raw arithmetic threshold, including Maine-eligible $5/$10 Lottery Credit offers. However the recovered strong offers are historical/expired (for example the $10 credit after a $1 order ended 2026-05-03), and current terms retain discretionary eligibility/withholding/cancellation provisions. Winnings from credit-funded winning tickets are withdrawable, so this remains a high-priority mechanism if a new current deterministic offer appears.

Sources:
- https://cms.jackpocket.com/tos/order-1-get-10/
- https://cms.jackpocket.com/tos/get-5-in-lottery-credits/

An evergreen Jackpocket funding-match rule page says offers may occur “from time to time”; it is not evidence of an active August 2026 offer. Its $10 deposit + $5 bonus version also requires ordering the deposit plus bonus amount before withdrawal, so applying a 50%-return exact partition to all $15 would guarantee only $7.50 of lottery winnings against $10 deposited before fees.
Source: https://cms.jackpocket.com/tos/funding-match-promotion-official-rules-10for5/

## Conclusion
H250 materially improves H249's execution evidence: **a courier-side controlled Single Digit wager menu is now directly proven on Lotto.com Maine**, and the exact finite cover is only ten lines.

But it does not produce SUCCESS. All verified partial-digit covers have a 50% deterministic base return. Therefore a strict guaranteed-profit conversion requires a deterministic effective subsidy **strictly above 50% after fees and acquisition costs**. No current public, player-selectable, non-discretionary August 2026 courier subsidy satisfying that condition was recovered.

Reusable watch condition: immediately reopen this lane whenever a courier serving Maine/Vermont/Minnesota (or another state with an exact-position digit wager) publishes a deterministic >50% draw-ticket discount, or fixed credit exceeding the corresponding `gross-loss + fees + acquisition` hurdle.
