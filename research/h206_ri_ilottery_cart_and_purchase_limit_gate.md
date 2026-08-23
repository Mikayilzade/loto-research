# H206 — Rhode Island iLottery cart batching and purchase-limit gate

Updated: 2026-08-23
Status: **NO SUCCESS; EXECUTION GATE TIGHTENED**
Scope: LOTTERY ONLY.

## Target
Continue the H173/H175 Rhode Island Keno execution branch without repeating the already-closed `$150 ticket cap -> bulk capacity` shortcut. The question for H206 is narrower:

1. Does the current official iLottery interface establish that draw-game/Keno purchases may be submitted through a cart rather than only one completed checkout per wager?
2. Does the same current official material expose another hard execution gate that must be satisfied before a 4,336- or 4,560-play same-draw construction can be called guaranteed executable?

## Primary-source evidence recovered

### 1. Official FAQ explicitly describes cart-submitted wagers
The current Rhode Island Lottery FAQ states that during iLottery maintenance, purchases for Powerball, Mega Millions, Wild Money, Millionaire for Life, The Numbers **and Keno** will not be accepted, and that wagers attempted as a result of **cart purchases submitted** during those hours will be voided. The FAQ separately says iLottery wagering is unavailable during each game's draw-break period.

Source: https://www.rilot.com/en-us/player-zone/faqs.html

This is stronger than the public Keno game page's single-selection-shaped flow. It proves a cart architecture exists in the current iLottery purchasing system and that Keno is within the set of games whose cart-submitted wagers are governed by the rule.

It does **not** publish:
- maximum Keno wagers/lines per cart;
- whether one cart may contain multiple independently selected Keno wagers for the same draw;
- whether a cart checkout is atomic (all accepted or all rejected);
- maximum cart monetary value;
- processing latency/capacity near a Keno draw break.

Therefore H205's conditional `4,336/240 = 18.0667` and `4,560/240 = 19` completed-purchases-per-second figures remain valid only under the explicit assumption that every distinct selection needs its own completed purchase. They are **not** unconditional execution lower bounds once the official cart architecture is taken into account.

### 2. Current official FAQ adds undisclosed system purchase caps
The same current FAQ states that Rhode Island Lottery has default **daily, weekly, and monthly Purchase Limits** for VIP Plus accounts. A player may set lower values, but user-selected limits must be less than or equal to the Lottery's own maximum limits. Increasing a user-set limit takes 24 hours.

Source: https://www.rilot.com/en-us/player-zone/faqs.html

The public FAQ does not state the numerical Lottery maximums.

For the H175 base construction, a single-player execution requires at least `$4,336` of accepted $1 Keno wagers in the target draw. H173 requires at least `$4,560`. If any required paid doubler/add-on applied, the corresponding purchase-limit requirement would be higher; the historical free-doubler branch does not itself add wager cost.

Thus a strict single-account execution proof now has an additional necessary condition:

`Lottery daily purchase maximum >= total same-day required paid wager amount`

and likewise no tighter weekly/monthly residual cap may bind.

Because the numerical maximums are not publicly recovered, this gate is presently unresolved rather than passed or failed.

### 3. Draw break makes the 240-second timing bound optimistic
The official FAQ says iLottery wagering is unavailable during each game's draw-break period. Keno draws are every four minutes. Therefore the actual available submission interval for a target Keno draw is **strictly less than or equal to 240 seconds** unless the platform allows wagers for that target draw to be staged earlier and held in cart/favorites without risk of draw rollover.

No current primary source recovered in H206 publishes the Keno draw-break duration or a guaranteed same-draw cart-lock mechanism.

Consequently, under a one-purchase-per-selection fallback model, `18.0667/s` and `19/s` are optimistic lower bounds; the true rate requirement would be higher if the break consumes positive time.

## Exact execution conditions after H206
For H175/H173 to become strictly executable through one current RI VIP Plus account, all of the following now need affirmative evidence:

1. The target Keno selections can be prepared and associated with one intended draw without rollover.
2. One or more carts/transactions can carry the required number of **distinct** same-draw Keno selections, or a proven processing path can submit them individually in time.
3. The Lottery's daily/weekly/monthly maximum purchase limits permit the total required paid wager amount.
4. The target draw's break/cutoff leaves enough time for acceptance.
5. Acceptance is sufficiently atomic/deterministic that a partially accepted basket cannot destroy the mathematical cover while still charging the accepted subset.
6. Any required pre-draw doubler/promotion entitlement is itself known and locked before exposure.

## Result
**ЕЩЁ НЕ УСПЕХ.** H206 proves that a current cart-submission architecture exists for iLottery draw-game/Keno wagering, so the H205 per-selection checkout-rate bound cannot be elevated to an unconditional blocker. But the same official FAQ exposes a new mandatory execution gate: undisclosed Lottery maximum daily/weekly/monthly purchase limits, plus an unpublished Keno draw-break duration and no published Keno cart line capacity/atomicity. The 4,336/4,560-play guarantee therefore remains unproved.

## Next action
1. Recover the numerical VIP Plus Lottery maximum purchase limits from current help/UI screenshots, archived support pages, app assets, or official terms.
2. Recover Keno cart capacity: number of independently selected Keno wagers/lines per cart and whether multiple same-draw Keno wagers are accepted atomically.
3. Recover Keno draw-break/cutoff duration and target-draw rollover behavior.
4. If these pass, recompute minimum carts/checkouts and exact execution margin for H175/H173.
