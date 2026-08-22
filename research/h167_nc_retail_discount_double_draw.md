# H167 — NC retailer-authorized discount + forced Pick 3 Double Draw

Updated: 2026-08-22
Status: **STRONG CONDITIONAL DETERMINISTIC OVERLAY / NOT TERMINAL SUCCESS**

## Purpose
H164-H166 required a retailer/player same-entity theory to convert the statutory 7% retailer commission into player-side edge. This packet finds a materially cleaner mechanism in NCEL's own draw-game rules: an authorized retailer may discount Draw Game tickets for promotional purposes while reporting the sale to NCEL at full gross sales value.

That means the retailer commission can be converted into an explicit, pre-agreed customer discount without requiring the retailer itself to own the ticket.

## Current authoritative facts
1. NCEL Draw Game Rules 2.02(J)(1) state that, subject to governing law/regulation, **Retailers may authorize sale of Draw Game Tickets at a discount for promotional purposes, provided discounted sales are reported to NCEL at full gross sales value**.
   Source: https://nclottery.com/Content/Docs/2.02_Draw_Ticket_Game-Rules.pdf
2. G.S. 18C-142 provides retailer compensation equal to **7% of face value** of lottery tickets/shares sold.
   Source: https://library.ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_18C/Article_5.html
3. Current NCEL retailer contract likewise provides **7% of retail price of tickets/shares sold**.
   Source: https://nclottery.com/Content/Docs/Retailer_Contract_Revised_041724.pdf
4. Current Carolina Pick 3 rules retain **Front/Back Pair = $25 prize on a $0.50 play, odds 1 in 100**.
   Source: https://nclottery.com/Content/Docs/2.04B%20Carolina%20Pick%203%20Game%20Rules.pdf
5. Retail Pick 3 tickets can be canceled at the terminal where issued within **15 minutes of purchase or before draw break, whichever comes first**.
   Source: https://nclottery.com/pick3-how-to-play
6. NCEL claim materials explicitly allow a claim form to be completed in the name of **one individual or legal entity**, and current NCEL game rules define Claimant broadly as a person or entity for several draw games. Thus legal-entity prize ownership is not categorically excluded by NCEL architecture.
   Sources: https://nclottery.com/ClaimPrizes ; https://nclottery.com/Content/Docs/PlayerPrizeClaimForm_%24600ormore.pdf

## Deterministic forced-Double-Draw cover
On an evening where the Double Draw promotion is already in a forced second-draw state under then-current published rules:
- cover all 100 ordered Front Pair outcomes;
- stake $0.50 each;
- face cost = **$50**;
- each Pick 3 draw necessarily contains exactly one covered Front Pair;
- each winning $0.50 Pair pays **$25**;
- two guaranteed drawings therefore produce **$50 gross prize cash**.

Base player cover = exactly 100% before any discount.

## Discount transfer theorem
Let `d` be the retailer promotional discount as a fraction of the $50 face basket.

Customer actual payment:
`C = 50 * (1-d)`

Guaranteed prizes in a forced Double Draw:
`P = 50`

Customer deterministic pre-tax surplus:
`P-C = 50d`

Retailer statutory commission at 7% of full face value is $3.50. If the retailer reports $50 full gross as required by NCEL and accepts discounted customer cash, the retailer's direct ticket margin before other costs is:
`50*(0.07-d)`.

Therefore any pre-agreed discount `0 < d <= 7%` can, in principle, split the statutory retailer economics between retailer and customer without requiring self-play. Examples:
- 3% discount: customer pays $48.50, guaranteed prize $50, pre-tax +$1.50; retailer retains ~$2.00 of 7% commission economics.
- 5% discount: customer pays $47.50, guaranteed prize $50, pre-tax +$2.50; retailer retains ~$1.00.
- 6% discount: customer pays $47.00, guaranteed prize $50, pre-tax +$3.00; retailer retains ~$0.50.
- 7% discount: customer pays $46.50, guaranteed prize $50, pre-tax +$3.50; retailer retains ~$0 before other retailer costs.

This is materially cleaner than H166 because the customer can be independent of the retailer and the discount can be documented before ticket issuance.

## Conservative C-corporation player tax screen
To preserve continuity with H166, assume an independent lawful C-corporation ticket owner/customer, 21% federal + 2% NC simple income-tax screen, and the conservative 2026 wagering-loss rule treatment used in H166: only 90% of actual wagering cost is deductible against wagering gains.

For discount `d`, simplified taxable wagering increment is:
`T = 50 - 0.90*50*(1-d) = 5 + 45d`.

Simplified tax = `0.23*T`.

After-tax deterministic customer surplus:
`A(d) = 50d - 0.23*(5+45d)`
`= 39.65d - 1.15`.

Break-even discount:
`d > 1.15 / 39.65 = 2.9004%`.

Thus under this deliberately conservative simple C-corp tax screen:
- 3% discount -> about **+$0.0395** per $50 cover;
- 5% -> about **+$0.8325**;
- 6% -> about **+$1.2290**;
- 7% -> about **+$1.6255**.

A negotiated **>2.90% discount** is therefore enough to keep the forced cover positive after this simplified 23% income-tax stress.

## Why this is not terminal SUCCESS yet
### Gate 1 — forced promotion state must be current and irrevocably known before purchase
The Double Draw mechanism is promotional/cyclic. Execution must occur only after the then-current official rules make the second drawing guaranteed for that evening. Historical 2024 rules establish the cumulative draw-down architecture but terminal execution needs the active 2026/then-current promotion document and observable state.

### Gate 2 — discount agreement must be explicit and NCEL-compliant
The general Draw Game Rules expressly permit retailer discounts for promotional purposes, but a terminal strategy needs:
- a specific licensed retailer willing to publish/sign the exact discount before execution;
- confirmation that the chosen promotion requires no additional NCEL pre-approval under current retailer procedures;
- cash/payment method with no fee that erases the margin.

The general 2.02 rule is stronger than H166's self-commission theory, but it does not itself force any retailer to offer a discount.

### Gate 3 — atomic execution / rollback remains unresolved
The 100 Pair selections are not one all-or-none transaction. NCEL can refuse a number when prize-liability limits are reached. The 15-minute cancellation rule helps, but public rules still do not guarantee bulk rollback if terminal/power/network failure occurs after partial issuance.

A strict ex-ante guarantee therefore still requires either:
- whole-basket reservation/acceptance before payment; or
- a proven operational protocol under which every partial basket can always be fully canceled/refunded before draw break, including outage recovery.

### Gate 4 — exact tax/legal entity implementation
NCEL documentation allows legal-entity claims generally, but terminal execution needs the specific ticket-owning entity's tax treatment, claim mechanics, and all fixed/incremental entity costs. The numerical C-corp screen above is a stress model, not taxpayer-specific legal/tax advice.

## Result
- **Retailer-authorized draw-ticket discount:** VALIDATED in current official NCEL rules.
- **Commission-to-customer transfer architecture:** VALIDATED structurally; avoids the H166 own-store commission dependency.
- **Forced Pair cover:** remains exact 100% prize gross before discount.
- **Conservative simple C-corp tax threshold:** discount **>2.9004%** preserves positive modeled after-tax surplus; 5%-7% gives approximately +$0.83 to +$1.63 per $50 cover under the stated assumptions.
- **Terminal SUCCESS:** NOT PROVEN because a live forced state, specific compliant retailer discount, and atomic/guaranteed rollback still must be locked before cash becomes irrecoverable.

## Next action
1. Search current NCEL retailer procedures/manuals for whether ordinary Draw Game promotional discounts under Rule 2.02(J)(1) require separate pre-approval and how discounted sales are entered/accounted at terminal.
2. Recover the active 2026 Pick 3 Double Draw promotion rules/state and identify the next guaranteed second-draw evening.
3. Search retailer terminal manuals for multi-ticket/bulk cancellation and outage recovery; this is now the main execution blocker.
4. Search other NCEL cumulative-trigger states where base deterministic cover is 100% and fewer than 100 selections are needed, reducing atomicity risk.
