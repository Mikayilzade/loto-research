# H138 — cross-state >=100% lottery-bonus + compact fixed-prize coverage screen

Updated: 2026-08-21
Status: **NO TERMINAL SUCCESS / KENTUCKY REMAINS UNIQUE VALIDATED POSITIVE-COVER CASE / DELAWARE + NH DO NOT IMPROVE EXECUTABLE FLOOR**

## Goal
After H136/H137 proved that a >=100% player-owned subsidy can invert a compact fixed-prize lottery cover, screen other current state-lottery bonus environments for a stronger execution profile: either withdrawable principal, atomic pre-acceptance, a deterministic cover ratio >60%, or a larger deterministic subsidy.

## 1. Kentucky control — still the best validated current arithmetic
Kentucky currently publishes a 100% first-deposit match up to $250. The same August page also publishes a $20 referred-player Bonus after a qualifying referred player registers and deposits at least $10. H136/H137 established the conditional Pair-cover arithmetic:

- Pick 3 Pair face cover = 100 outcomes x $0.50 = $50;
- fixed winning payout = $30;
- base deterministic cover ratio = 60%;
- unstacked 100% match: $25 cash + $25 Bonus -> $30 gross -> +$5 pre-tax conditional;
- if referral stacks: $15 cash + $15 match + $20 referral -> $50 cover -> $30 gross -> +$15 pre-tax conditional.

Fresh official control still shows both August offers simultaneously live. However, KLC terms still state that deposited funds are non-withdrawable, purchases can be refused for any reason, and KLC may limit a wager on a particular set of numbers at any time without notice. Thus the fatal ex-ante acceptance gate remains.

Official sources:
- https://www.kylottery.com/apps/promotions/promotions.html
- https://www.kylottery.com/apps/funclub/terms.html?pane=terms
- https://play.kylottery.com/en-us/playnow/pick3.html

## 2. Kentucky cart/favorites/batch execution check
Fresh official interface pages materially improve the operational picture but do **not** solve the theorem.

Observed:
- Pick 3 online exposes `Add to cart`, `Buy Now`, and Favorites.
- The Shopping Cart supports a total transaction amount and a single `Purchase` action.
- The Pick 3 page says the player is not charged until confirming the purchase in the next step.
- Retail terminal documentation supports multiple Pick 3 plays/tickets per terminal command, but Kentucky Bonuses cannot be used for retail purchases.

This means a player can plausibly pre-build a multi-wager online basket before final confirmation. But the cart is **not a contractual reservation**: KLC terms expressly retain the right to refuse any attempted purchase and limit wagers on particular number sets. Therefore `basket assembled` != `all required outcomes irrevocably accepted`.

Execution conclusion: **cart/batch UI reduces practical friction, but does not remove the terminal pre-commitment branch.**

Official sources:
- https://play.kylottery.com/en-us/playnow/pick3.html
- https://play.kylottery.com/en-us/shoppingcart.html
- https://www.kylottery.com/apps/funclub/terms.html?pane=terms
- https://www.kylottery.com/export/kylmod/galleries/documents/Training_Documents/Retailer-Manual-8.7.24.pdf

## 3. Delaware iLottery — current 100% welcome bonus, but wrong product architecture
Delaware iLottery currently publishes a **Welcome Offer: 100% Deposit Bonus up to $100** valid through December 31.

However, the official Delaware iLottery product is centered on eInstant games. The official app-information page describes direct app play for approved eInstant games, while draw-game pages such as Play 3 remain part of the retail Delaware Lottery draw-game system rather than the iLottery eInstant wallet architecture.

The general Delaware iLottery Bonus Policy also states that Deposit Bonus promotions require playthrough of the qualifying deposit and/or Bonus Money a specified number of times before Bonus Money converts to cash. This is materially weaker than the Kentucky draw-game construction because the subsidy is not a simple one-pass fixed-prize draw credit.

Even if Delaware Play 3 were hypothetically bonus-eligible, its fixed cover is only 50%:
- 50-cent Straight pays $250;
- 1,000 outcomes cost $500 and guarantee $250;
- Front/Back Pair: 100 outcomes cost $50 and guarantee $25;
- deterministic ratio = 50%.

A pure 100% match therefore only reaches mathematical **break-even before tax/friction**, not positive profit:
`external cash d + bonus d = 2d face; 50% fixed cover -> d gross`.

Current Delaware conclusion: **100% subsidy validated, but no positive deterministic compact-cover path identified; draw-game access/playthrough architecture is weaker than Kentucky.**

Official sources:
- https://www.deilottery.com/bonuses-promotions
- https://www.deilottery.com/bonus-policy/
- https://www.deilottery.com/app-information/
- https://www.delottery.com/Drawing-Games/Play-3
- https://www.delottery.com/Drawing-Games/Play-3/Number-Of-Winners

## 4. New Hampshire compact fixed-prize screen
New Hampshire's official Pick 3 table gives:
- $1 Straight -> $500 at 1:1,000;
- $1 Front Pair -> $50 at 1:100;
- $1 Back Pair -> $50 at 1:100;
- $1 Single Digit -> $5 at 1:10.

Every exact partition cover therefore returns exactly **50%** of face spend. This is inferior to Kentucky's 60% Pair cover.

The official NH promotional terms allow fixed or percentage Free Bonus Money offers, but this packet did not locate an authoritative current statewide >=100% welcome offer with sufficiently favorable conversion/withdrawal rules to establish a deterministic positive cover. Third-party pages claim 100%-200% offers, but those are not sufficient evidence for a terminal theorem and are excluded from the validated result.

Current NH conclusion: **compact fixed-prize cover ratio = 50%; no authoritative current subsidy packet found that converts it to strict positive net profit.**

Official sources:
- https://www.nhlottery.com/game/pick-three
- https://faq.nhlottery.com/support/solutions/articles/156000372553-terms-conditions

## 5. Cross-state threshold theorem
For a deterministic fixed-prize partition cover with base gross ratio `r`, and a one-pass deterministic deposit bonus rate `b` usable directly on the cover, ignoring tax/friction:

`gross / external_cash = r * (1 + b)`.

Strict pre-tax positivity requires:

`b > 1/r - 1`.

Examples:
- Kentucky Pair `r=0.60` -> minimum bonus rate strictly > **66.6667%**;
- Delaware/NH Pair/Straight partition `r=0.50` -> minimum bonus rate strictly > **100%**.

Thus a 100% match is genuinely enough for Kentucky but only break-even for 50%-return digit games. This explains why H136 remains unusually strong.

## Result
- Kentucky cart/batch UI: **operationally helpful, not an atomic acceptance lock**.
- Kentucky H136/H137: **still best current validated positive-cover arithmetic, not terminal SUCCESS**.
- Delaware current 100% welcome bonus: **validated, but 50% digit cover reaches only break-even and iLottery is eInstant/playthrough oriented**.
- New Hampshire Pick 3: **50% deterministic partition ratio; no authoritative current >100% one-pass draw-game subsidy validated**.
- Terminal state: **NO SUCCESS; NOT EXHAUSTED**.

## Next high-value branch
1. Search current official state-lottery offers with **>100% deterministic one-pass bonus** attached to draw games, or >=67% bonus attached to a fixed-prize compact game with `r>=60%`.
2. Prioritize offers where deposits remain withdrawable until wager acceptance, or where a complete cart is contractually reserved before funding.
3. Search compact games with `r>60%`; every 5 percentage points of base cover materially lowers the required subsidy threshold.
4. Reopen H137 only on explicit official stackability or a true pre-acceptance lock.