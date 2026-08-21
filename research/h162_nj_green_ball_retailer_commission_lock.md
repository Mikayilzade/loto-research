# H162 — New Jersey Green Ball: retailer commission entitlement materially strengthened

Updated: 2026-08-22
Status: **NO SUCCESS / 5% SALES COMMISSION RULE NOW PRIMARY-SOURCE LOCKED FOR PICK-3 GROSS SALES / SELF-PURCHASE CHARACTERIZATION + PROMO IRREVOCABILITY + ACTIVE-CYCLE GATES REMAIN**

## Objective
Resolve H161's highest-value question: whether the ordinary New Jersey retailer commission is sufficiently contractual/rule-based to count in the forced-Green-Ball Pick-3 Pair coverage arithmetic.

## New primary-source evidence
### 1. Official Pick-3 game rules expressly prescribe the commission
The current official Pick-3 rules (effective November 14, 2022) state in §8(b):
- **Retailers will receive a commission equal to five percent (5%) of the gross sales dollars.**
- **All Retailers paying out cash prizes up to $599.50 shall receive a commission equal to 1.25% of the money paid out in prizes.**

The same §8(e) says Pick-3 tickets may be cancelled at the time of purchase and **no commissions are payable on cancelled bets**. This is important because it ties commission entitlement to completed, uncancelled Pick-3 sales rather than a discretionary marketing page.

Official source:
- https://www.njlottery.com/content/dam/portal/pdfs/drawgames/pick3/Pick-3_Rules_Fixed_Prizes_APPROVED-06.16.22.pdf

Relevant official-rule facts:
- Pair wager: 1 in 100; $0.50 Pair pays $25.
- One Ticket may contain up to ten Plays.
- Tickets may be cancelled only at the time of purchase.
- Prize-liability limits may cause further wagers on a number to be refused.
- §8(b) uses mandatory `will receive` / `shall receive` language for the commissions.

### 2. Administrative rules support netting commissions from remittance
N.J.A.C. 17:20-6.1(c) says the agent remits ticket face value to the Lottery **less commissions, bonuses and reimbursements for redeemed tickets to which the agent is entitled**.

N.J.A.C. 17:20-6.3 likewise treats lottery sales proceeds as Lottery property held in trust and requires remittance of net lottery receipts.

Sources:
- https://regulations.justia.com/states/new-jersey/title-17/chapter-20/subchapter-6/section-17-20-6-1/
- https://regulations.justia.com/states/new-jersey/title-17/chapter-20/subchapter-6/section-17-20-6-3/

### 3. Retailer-owner purchase remains lawful on the public record
The prohibited-player regulation, N.J.A.C. 17:20-1.3, does not list ordinary licensed lottery retailers/owners among prohibited purchasers. It does prohibit commissioners, certain Lottery/vendor personnel and courier personnel.

H161 already recorded an official NJ Lottery winner release in which licensed retailer owner Jay Shortway personally bought a CASH4LIFE ticket at his own licensed location and was recognized as the winner.

Sources:
- https://regulations.justia.com/states/new-jersey/title-17/chapter-20/subchapter-1/section-17-20-1-3/
- https://www.njlottery.com/en-us/newsandevents/newsinput/2023/press-releases/C4L_GrandPrize_042123.html

### 4. Green Ball rules themselves contemplate retailer participation
The 2026 Green Ball rules say that by participating in the promotion **licensed retailers and Players** agree to comply with the rules. They also state that all retailers paying qualifying cash prizes receive the 1.25% payout commission.

However, the same rules let the Lottery disqualify a retailer from the promotion in its discretion and cancel/terminate/modify/suspend the promotion without prior notice.

Official source:
- https://www.njlottery.com/content/dam/portal/pdfs/drawgames/pick3/Pick-3-Green-Ball-Rules-Effective-07.06.2026_V1.pdf

## Deterministic forced-state arithmetic
At `k=6` (all six white balls removed before the next evening draw), the next Green Ball selection is mechanically forced.

Cover one Pair position:
- 100 ordered Pair outcomes;
- $0.50 each;
- face cost = **$50**;
- regular draw guarantees one $25 Pair prize;
- forced Green Ball second draw guarantees a second $25 Pair prize;
- guaranteed prize gross = **$50 = 100% of face**.

### Commission scenarios
A. Player only:
- spend $50
- guaranteed prizes $50
- gross floor = **$0 profit**.

B. Licensed retailer owner; the $50 personal basket is treated as ordinary completed Pick-3 gross sales:
- spend $50
- guaranteed prizes $50
- Pick-3 sales commission = **$2.50**
- conditional pre-tax floor = **+$2.50 = +5.00%**.

C. Same retailer also validly cashes the two resulting sub-$600 Pair prizes at its licensed location:
- sales commission = $2.50
- cashing commission = 1.25% × $50 = **$0.625**
- conditional pre-tax floor = **+$3.125 = +6.25%**.

The important upgrade from H161 is that the 5% sales commission is no longer supported only by a generic retailer marketing page. It is written directly into the official Pick-3 game rules with mandatory language.

## What remains unproven
### Gate A — explicit self-sale classification
The rules say 5% of `gross sales dollars`; they do not contain a public sentence explicitly saying that a valid ticket personally purchased by the retailer/owner through that retailer's terminal remains commissionable gross sales.

The combination of:
1. lawful retailer-owner purchase,
2. official owner self-purchase example,
3. mandatory 5% commission on Pick-3 gross sales,
4. no public self-sale commission exception found,

is strong evidence, but terminal `SUCCESS` requires either an explicit rule/retailer agreement or written Lottery confirmation that such a personal purchase is commission-bearing.

### Gate B — whole-basket acceptance / rollback
One Pick-3 Ticket supports at most 10 Plays, so the 100-Pair cover requires at least 10 tickets. Pick-3 tickets may be cancelled only `at the time of purchase`, while liability limits can reject further wagers on particular numbers.

This improves H161 because a failed ticket transaction can potentially be cancelled immediately, but the public rules do **not** establish an atomic 10-ticket transaction or a guaranteed right to cancel all earlier tickets after a later ticket fails. Therefore a legal partial-cover branch still exists.

### Gate C — Green Ball promo irrevocability
The 2026 promotion rules reserve the right to cancel, terminate, modify or suspend the promotion at any time without prior notice and even disqualify a licensed retailer from participation. No public rule found in this packet states that an already-issued eligible ticket irrevocably retains the second-draw right after a later promotion cancellation/modification.

### Gate D — current executability
The latest Green Ball cycle ended August 2, 2026. The architecture is recurring but not active on 2026-08-22.

### Gate E — tax/entity floor
The economic margin is small. A licensed retailer/entity's tax treatment and 2026 federal wagering-loss limitation must be fixed before asserting positive **net** profit. H162 does not claim a universal after-tax floor.

## Result
- Official Pick-3 5% sales commission entitlement: **PRIMARY-SOURCE VALIDATED** for gross Pick-3 sales.
- Official 1.25% cashing commission: **PRIMARY-SOURCE VALIDATED** for retailers paying qualifying cash prizes.
- Retailer-owner lottery play: **not categorically prohibited; official self-purchase example preserved**.
- Forced-Green Pair coverage: **100% deterministic prize gross**.
- Conditional retailer-owner economics: **105.00% with sales commission; 106.25% if cashing commission also applies**.
- Strict terminal guarantee: **NOT YET PROVEN** because self-sale commission classification, multi-ticket atomicity/rollback, promo irrevocability, tax, and active-cycle gates remain.

## Highest-value next action
1. Search NJ retailer agreements/manuals, commission accounting documentation, audit guidance or official Q&A for an explicit self-purchase/self-sale commission rule.
2. Search for terminal transaction/batch functionality that can issue all 100 Pair selections as one reversible transaction or cancel a prior completed Pick-3 ticket before draw cutoff.
3. Search administrative/game rules for vested rights of already-issued promotional tickets after promotion modification/cancellation.
4. Monitor the next Green Ball cycle and only reopen execution when `k=6` is publicly observable.
5. Search other forced-trigger promotions where one-ticket or system-bet coverage avoids the multi-ticket atomicity problem and ordinary retailer commission is mandatory.