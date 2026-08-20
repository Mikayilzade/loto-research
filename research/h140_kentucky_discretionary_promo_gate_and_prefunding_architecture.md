# H140 — Kentucky discretionary-promotion gate + pre-funding acceptance architecture

Updated: 2026-08-21
Scope: LOTTERY ONLY
Status: **KENTUCKY H136-H139 TERMINAL GUARANTEE CLOSED UNDER CURRENT TERMS / PRE-FUNDING ARCHITECTURE CLASS REMAINS OPEN ELSEWHERE**

## Objective
Resolve the most important remaining H136-H139 question: whether exact stacking rules alone could turn the current Kentucky August 2026 deposit promotions + Pick 3 deterministic cover into a strict ex-ante guaranteed-profit strategy.

Result: **no** under the current Kentucky iLottery terms. A stronger contractual blocker exists upstream of the already-known basket-acceptance blocker.

## 1. Current Kentucky subsidy remains mathematically strong
The official Kentucky Lottery promotions page currently lists, during August 2026:
- 100% first-deposit match up to $250;
- Tiki Tuesday: $50 Bonus on a single $150+ deposit on specified Tuesdays, including Aug 25;
- Summer Fridays: 25% deposit match up to $50 on specified Fridays, including Aug 21;
- Referred Friend: $20 Bonus to a qualifying referred new player after the referred player deposits at least $10.

Current official promotions page:
- https://www.kylottery.com/apps/promotions/promotions.html

The H136-H139 Pick 3 Pair-cover identity remains exact:
- $50 face buys all 100 pair outcomes at $0.50 each;
- exactly one pair wins;
- guaranteed gross = $30;
- deterministic cover ratio `r = 0.60`.

General positive-floor condition for an external deposit `D` and deterministic usable Bonus `B` is:

`profit_pre_tax = r * (D + B) - D`

so positive pre-tax floor requires:

`B / D > (1/r) - 1 = 2/3 = 66.6667%`.

This is important because Kentucky's 100% first-deposit match already exceeds the mathematical threshold even without stacking.

## 2. New decisive blocker: promotional awards are expressly discretionary
The current Kentucky iLottery Terms of Use provide, under Promotional Offers / General Conditions, that promotional offers are **discretionary**, that the player has **no right to receive or redeem any specific offer**, and that promotional offers may be cancelled at any time and without notice. The same terms disclaim liability for delay, error, or failure to make or accept a promotional offer.

Official current terms:
- https://www.kylottery.com/apps/funclub/terms.html?pane=terms

Relevant current terms (web lines observed in this run):
- promotional offers discretionary / no right to specific offer / cancellable without notice: lines 393-398;
- Bonus only becomes an account asset after an award is actually made: lines 399-408.

This creates an ex-ante branch that H139 did not fully elevate:

`qualifying non-withdrawable deposit -> promotion is not awarded / is cancelled / is delayed -> insufficient balance for profitable full cover`.

Because the project SUCCESS standard requires strictly positive net profit across every lawful execution branch after external cash becomes irreversible, the current Kentucky promotion cannot support terminal SUCCESS merely by proving that multiple promotions are stackable.

### Consequence
Even if KLC later confirms that Tiki Tuesday, Summer Fridays, referral, and the first-deposit match can stack, the guarantee still fails unless the relevant Bonus amount is **irrevocably credited/locked before external deposit principal becomes nonrecoverable**.

Thus the unresolved `stackability` issue is now economically interesting but **not terminal-decisive**.

## 3. Deposit principal is irrevocable before award/coverage lock
The current Kentucky iLottery terms also state:
- ordinary deposited funds may not be withdrawn/refunded unless required by law;
- deposited funds cannot be withdrawn, returned, charged back, re-credited, or transferred;
- Kentucky Lottery reserves the right to deny deposits and does not guarantee processing timing.

Official terms:
- https://www.kylottery.com/apps/funclub/terms.html?pane=terms

Relevant observed lines:
- non-withdrawable deposit representation: 438-440;
- explicit no-withdrawal/no-transfer rule: 445-447.

This confirms the harmful ordering:

`commit external cash -> maybe receive promo -> attempt deterministic basket`.

A strict theorem needs the opposite risk order:

`lock subsidy + lock complete basket -> commit external cash`.

## 4. Existing second blocker also remains: wager acceptance is discretionary
Kentucky defines a wager as a **successful purchase**, reserves the right to refuse any attempted purchase for any reason, and may limit purchases of any game or a wager on a particular number set at any time and without notice.

Official terms:
- https://www.kylottery.com/apps/funclub/terms.html?pane=terms

Relevant observed lines:
- wager = successful purchase / eligibility: 268, 283-284;
- purchase refusal: 485-488;
- number/game purchase limits without notice: 490-495.

Therefore even after Bonus credit, a required Pick 3 Pair selection can still be refused. One missing outcome destroys the all-outcome deterministic floor.

## 5. H136-H139 closure theorem under current Kentucky rules
Current Kentucky strict guarantee requires all three gates **before** external cash is irrecoverable:
1. Bonus entitlement locked and non-discretionary;
2. required Bonus amount actually credited/irrevocable;
3. all members of the complete Pick 3 cover accepted or atomically committed.

The current terms fail all three pre-commitment requirements:
- promotional offer remains discretionary before award;
- deposit is nonwithdrawable;
- purchases/number sets may be refused or limited.

Therefore:

**H136-H139 Kentucky current-offer path is CLOSED for terminal guaranteed profit under current published terms, even if future evidence proves promo stacking.**

Reopen only if Kentucky materially changes its terms/process or an official transaction state appears where the Bonus and the entire required wager basket are irrevocably locked before cash commitment.

## 6. Cross-state architecture control: Virginia shows a better funding order exists
The current Virginia Lottery FAQ states that draw-game tickets can be added to a shopping cart and paid at checkout using a one-time debit-card purchase (minimum $5). It also says the cart can be cleared before purchase. That is structurally better than forcing wallet funding before a basket is assembled.

Official Virginia FAQ:
- https://www.valottery.com/aboutus/faq

Observed current FAQ facts:
- draw games can be added to cart and paid at checkout by one-time debit purchase;
- wallet deposits are not necessary for that one-time draw-game checkout;
- player can clear the cart before completing purchase.

This does **not** create a SUCCESS candidate by itself. In this packet no current Virginia deterministic draw-game subsidy was found that both:
- exceeds the exact coverage subsidy threshold; and
- applies to the same one-time checkout transaction.

But it validates the architecture sought by NEXT ACTION: a state-lottery system can allow basket construction before external cash charge. Future searches should prioritize systems where a deterministic promo/discount is applied at **checkout** rather than only after a nonwithdrawable wallet deposit.

## 7. Updated search target
The strongest lottery-specific target class is now narrower:

### Class A — checkout-level deterministic subsidy
Required properties:
1. compact non-shareable fixed-prize game with deterministic cover ratio `r`;
2. player-owned discount/credit/free-ticket subsidy `s > 1/r - 1` relative to external cash;
3. full required basket can be assembled before payment;
4. checkout is all-or-nothing or failed selections do not charge external cash;
5. subsidy terms create enforceable/automatic entitlement at checkout, not discretionary post-deposit credit;
6. winnings are ordinary claimable cash; taxes/fees preserve positive floor.

For Kentucky Pick 3 Pair (`r=0.60`), required subsidy is >66.6667% of external cash. For a 2/3-cover game (`r=0.6667`), only >50% subsidy is required; for a 75% cover game, >33.3333% is enough.

### Class B — withdrawable-principal wallet subsidy
Alternative acceptable order:
`deposit -> Bonus award -> verify Bonus -> if basket cannot be completed, withdraw untouched principal`.

Kentucky fails because deposit principal is nonwithdrawable.

## 8. Result
- Kentucky H136-H139 conditional arithmetic: **still valid**.
- Kentucky stacking question: **no longer terminal-decisive**.
- Current Kentucky strict guarantee: **CLOSED by discretionary-promo + nonwithdrawable-deposit + purchase-refusal chain**.
- Pre-funding cart/checkout architecture: **VALIDATED as a real lottery-system design via Virginia**, but no matching current >threshold deterministic subsidy found in this packet.
- Terminal project state: **NO SUCCESS; NOT EXHAUSTED**.

## Next action
1. Search current state lotteries for checkout-level BOGO/percentage discounts or promo codes applying directly to draw-game carts, especially Pick 3/4/5.
2. Search fixed-prize compact games with deterministic cover ratio >60%; subsidy threshold falls rapidly as `r` rises.
3. Search online lottery wallets where cash deposits are withdrawable if unused and Bonus is credited before wagering.
4. Do not spend further runs resolving Kentucky stacking unless new official evidence changes the pre-commitment legal ordering.
