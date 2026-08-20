# H136 — Kentucky 100% first-deposit bonus + Pick 3 deterministic coverage

Updated: 2026-08-21
Status: **PRE-TAX POSITIVE COVER IDENTIFIED / TERMINAL GUARANTEE REJECTED DUE PRE-COMMITMENT PURCHASE-ACCEPTANCE + TAX GATES**

## Why this packet matters
H135 established that a scalable ticket subsidy must exceed the exact deterministic coverage deficit. A fresh 2026 scan found a materially stronger subsidy: Kentucky Lottery currently advertises a **100% first-deposit match up to $250** for eligible Fun Club online players during August 1–31, 2026.

Official promotion page:
- https://www.kylottery.com/apps/promotions/promotions.html

Official iLottery terms:
- https://www.kylottery.com/apps/funclub/lottery-terms-and-conditions.html

The terms state that Bonuses can be used to play online, are deducted before deposited cash for purchases, and cannot themselves be withdrawn. Prize winnings from lottery play are tracked separately and may be withdrawn. Online purchase requires physical presence in Kentucky, identity verification, a valid U.S. address and other account requirements.

## Pick 3 deterministic cover
Kentucky Pick 3 is a fixed-prize compact game. The current Kentucky site shows a $600 top prize; the current play interface offers Pick 3 online. Current published game information gives a $0.50 minimum Straight wager and a $300 prize on a $0.50 Straight (equivalent to $600 on $1), with odds 1 in 1,000.

Official current Pick 3 page:
- https://play.kylottery.com/en-us/playnow/pick3.html

Current Kentucky winning-number page also labels the Pick 3 top prize at $600:
- https://www.kylottery.com/apps/draw_games/pastwinning.html

Prize/wager cross-check used for the exact current payout structure:
- https://www.lottery.net/kentucky/pick-3

### Full Straight cover
There are exactly 1,000 ordered outcomes (`000` through `999`).

At $0.50 per Straight:
- face spend for every outcome = **$500**;
- exactly one Straight wins for every draw;
- guaranteed gross payout = **$300**;
- base deterministic return = **60%**.

With a 100% deposit match capped at $250:
- player deposits **$250 cash**;
- receives **$250 Bonus**;
- purchasing power = **$500**;
- if all 1,000 distinct $0.50 Straights are accepted for one draw, every possible draw outcome is covered;
- guaranteed pre-tax payout = **$300**;
- guaranteed pre-tax surplus versus external cash deposited = **+$50 = +20%**.

This is the first current lottery packet in the project where a live operator subsidy is large enough to invert a fixed-prize full-coverage game into a mathematically positive deterministic **pre-tax** cash result.

## Smaller equivalent cover
The same 60% fixed-prize identity exists for a single Pick 3 Pair position:
- 100 ordered pair outcomes;
- $0.50 each = $50 face coverage;
- one winning pair pays $30;
- with a 100% matched $25 deposit, $50 purchasing power would return $30, a +$5 pre-tax surplus.

This reduces required transaction count/capital but does not cure the legal/operational gates below.

## Why this is NOT terminal SUCCESS
### Gate 1 — irreversible deposit occurs before complete-cover acceptance is locked
Kentucky's iLottery terms say deposited funds may not be withdrawn/refunded (except where required by law). The promotion requires a qualifying deposit before the Bonus is awarded.

But the same terms expressly reserve Kentucky Lottery's right to:
- refuse an attempted purchase;
- limit purchases of any game;
- limit a wager on a particular set of numbers at any time and without notice;
- terminate a game;
- change/cancel promotional offers under the applicable rules.

Therefore the sequence is currently:

`non-withdrawable deposit -> bonus credit -> attempt 1000-number cover`

not:

`lock complete 1000-number cover -> commit deposit`.

Without an operator mechanism that atomically accepts/reserves the whole cover before the $250 external cash becomes irreversible, there is a lawful branch where some required number wagers are refused after the deposit. In that branch the deterministic payout theorem disappears while the cash remains locked for lottery play.

This prevents a strict ex-ante guaranteed-profit claim.

### Gate 2 — 2026 federal tax treatment can erase the $50 margin
Lottery winnings are gambling income. For tax years beginning in 2026, current federal law limits wagering-loss deductions to **90% of wagering losses**, and taxpayers who do not itemize generally cannot claim the wagering-loss deduction.

Primary federal source:
- https://www.irs.gov/irb/2026-19_IRB
- https://www.irs.gov/publications/p505

Thus the +$50 pre-tax arithmetic is not a universal after-tax floor. Tax outcome depends on taxpayer status, deductible basis of cash/Bonus-funded wagers, itemization, other gambling activity and marginal rates. A terminal theorem would require a taxpayer-specific tax lock showing positive after-tax cash.

### Gate 3 — eligibility is geographically/account constrained
The current terms require, among other things:
- valid U.S. address and verified identity;
- online purchases only while physically located within Kentucky;
- compliance with Fun Club/iLottery terms;
- one account per person;
- offer eligibility as specified by the promotion.

This is a lawful but narrow execution set, not a globally accessible strategy.

## Strong conditional theorem
If all of the following can be locked **before external cash becomes irrecoverable**:
1. player is eligible for the current 100% match;
2. $250 Bonus is contractually guaranteed/credited;
3. all 1,000 distinct $0.50 Pick 3 Straight wagers for the same draw are atomically accepted;
4. fixed $300 winning payout is not reduced by any liability rule;
5. winnings from Bonus-funded tickets are withdrawable prize winnings;
6. all taxes/fees are fixed and total less than $50;

then the transaction has a strict positive net floor.

The mathematics is therefore **validated**. What is missing is an execution contract/order mechanism that locks conditions 2–6 before the non-withdrawable deposit.

## Result
- **100% deposit-match subsidy: VALIDATED current.**
- **Pick 3 60% deterministic full-cover ratio: VALIDATED.**
- **Combined pre-tax cover: +$50 guaranteed conditional on complete acceptance.**
- **Terminal SUCCESS: REJECTED today** because complete-cover acceptance is not locked before the irreversible deposit and 2026 tax treatment is not universally bounded below the margin.

## Next research
1. Search state lotteries with >=100% deposit/wallet bonus where deposited principal remains withdrawable or the full wager basket can be reserved before deposit.
2. Search fixed-prize compact games with deterministic coverage ratio materially above 60%, so the bonus margin survives 2026 tax drag.
3. Search Kentucky purchase/cart rules or an official batch-play mechanism capable of atomic 1,000-number Pick 3 acceptance; reopen H136 only if this pre-commitment gate is solved.
4. Test whether any current promo explicitly converts Bonus-funded game wins to ordinary withdrawable prize winnings with no separate promotional-winnings restriction.