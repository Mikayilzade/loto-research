# H166 — NC Pick 3 forced Double Draw: corporate tax salvage + liability-limit stress

Updated: 2026-08-22
Status: **PROMISING CONDITIONAL OVERLAY / NOT TERMINAL SUCCESS**

## Purpose
H164-H165 established a recurring lottery-specific architecture:
- on a forced Carolina Pick 3 Double Draw evening, a full 100-outcome Pair cover costs $50 at $0.50 each and guarantees $25 in each of two drawings = $50 gross prizes;
- a licensed NC retailer receives a statutory/current-contract 7% sales commission, conditionally adding $3.50 if the retailer's own valid store purchase is commission-bearing;
- NC retailers are not categorically barred from playing;
- the public cancellation window is up to 15 minutes or draw break, whichever comes first.

H165 showed that an individual-player structure is nearly erased by the 2026 90%-wagering-loss deduction rule. H166 therefore tests whether a corporate retailer/player structure could restore a positive after-tax floor and whether the edge can be safely scaled.

## Current primary-source facts
1. **Retailer compensation remains 7%.** G.S. 18C-142 says retailer compensation for sales is 7% of face value. The current retailer contract says NCEL shall pay 7% of the retail price of tickets/shares sold by the retailer. NCEL's Jan. 2, 2026 public accounting explanation likewise says businesses selling lottery tickets receive 7 cents for every dollar they sell.
2. **2026 wagering-loss rule:** IRS 2026 guidance states only 90% of wagering losses are deductible, limited to wagering gains.
3. **Federal C-corporation rate:** 21% under 26 USC 11.
4. **North Carolina C-corporation income tax rate for 2026:** 2.00%.
5. **Pick 3 liability limits are explicit.** Current NCEL FAQ and Pick 3 game rules say that if prize liability on a number exceeds a pre-determined NCEL limit, no further wager on that number is accepted; the limit can be changed at NCEL discretion.
6. **Pick 3 retail cancellation remains ticket-by-ticket:** up to 15 minutes or draw break, whichever is earlier.

Primary sources:
- https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/ByChapter/Chapter_18C.html
- https://nclottery.com/Content/Docs/Retailer_Contract_v1.pdf
- https://nclottery.com/NewsBlogDetails/2026/1/2/Where-does-the-money-go
- https://www.irs.gov/pub/irs-irbs/irb26-19.pdf
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title26-section11
- https://www.ncdor.gov/taxes-forms/corporate-income-franchise-tax/corporate-income-and-franchise-tax-rates
- https://nclottery.com/FAQGames
- https://nclottery.com/pick3-how-to-play

## Tax arithmetic if one C corporation is both retailer and ticket owner
Assume, strictly as a conditional tax screen, that:
- the licensed retail C corporation can lawfully own the retail Pick 3 tickets;
- its own store transaction is commission-bearing;
- all $50 prizes and the $3.50 commission are taxable to the same corporation;
- the 90%-wagering-loss rule applies to the corporation in the same numerical way;
- ignore any additional deductions/credits and use a deliberately conservative simple additive income-tax rate of 21% federal + 2% NC = 23%.

For a $50 face cover:
- wagering gains = $50;
- wagering cost = $50;
- deductible wagering loss at 90% = $45;
- residual taxable wagering income = $5;
- retailer commission = $3.50;
- simplified incremental taxable income = $8.50;
- tax at 23% = $1.955;
- pre-tax deterministic economic surplus = $3.50;
- simplified after-income-tax surplus = **$1.545 per completed $50 cover**.

For the $1 Pair denomination, the same structure doubles:
- face cover = $100;
- guaranteed Double Draw prizes = $100;
- commission = $7;
- simplified taxable increment = $17;
- income tax at 23% = $3.91;
- simplified after-income-tax surplus = **$3.09**.

The tax break-even rate remains `commission / (commission + 10%-of-face taxable wagering residue) = 7 / 17 = 41.1764706%`. A 23% C-corp income-tax screen is therefore comfortably below the individual high-bracket stress point.

## Why this materially improves H165
The 2026 tax rule does **not** automatically kill the NC overlay if a lawful same-entity C-corporation structure exists. The pre-tax 7% commission is large enough to survive a 21% federal + 2% NC corporate income-tax screen with about 3.09% of face remaining after those income taxes.

This removes the idea that H164 is necessarily tax-dead. It does **not** prove the required entity structure.

## New scaling blocker: NCEL number-liability limits
A tempting response to fixed retailer/franchise/operating costs is to scale the same complete cover many times. Current NCEL rules prevent treating that as guaranteed:
- Pick 3 combinations regularly sell out because of prize-liability limits;
- once the NCEL liability threshold for any number is reached, no further wagers on that number are accepted;
- the limit is not published as a hard amount and can change at NCEL discretion.

Therefore a repeated-cover scheme cannot assume unlimited duplication. Even a first full cover still requires all 100 Pair selections to remain available. H164's rollback protocol remains necessary.

The $200 minimum NC franchise tax also matters for a newly created standalone C corporation. At the simplified $1.545 profit per $50 cover, it would require roughly 130 successful $50 covers merely to offset a $200 fixed annual franchise-tax cost, before retailer/store setup and operating costs. At the $1 denomination, roughly 65 completed covers would be required. Because liability limits can block repeated identical coverage and forced Double Draw nights are intermittent, **creating a new retailer corporation solely for this strategy is not supported by the current evidence**.

The corporate tax improvement is therefore most relevant only to an **already-operating, already-licensed C-corporation retailer** for which ordinary fixed retailer/franchise costs are sunk and the exact own-ticket accounting treatment is confirmed.

## Remaining terminal gates
1. **Own-store commission attribution:** still no explicit NCEL accounting sentence found saying an owner/entity's personal/own ticket transaction is included in commission-bearing sales. Statute + contract + NCEL public language strongly imply commission on every recognized sale, but terminal proof needs the exact related-party treatment or a written NCEL confirmation.
2. **Corporate ticket ownership/player eligibility:** public NC claim materials support tax-identification reporting and bearer-ticket claims, but this packet did not recover sufficiently authoritative current NCEL language proving that the licensed C-corporation retailer itself can be the legal player/owner for this small-prize retail sequence. Do not treat the C-corp tax screen as executable until this is locked.
3. **Atomic execution:** cancellation is still ticket-by-ticket, not a guaranteed all-or-none transaction. A terminal/power/network failure can strand a partial cover before cancellation completes.
4. **Liability limits:** any required Pair can sell out before/during execution, and repeated scaling can trigger the limit. This is manageable only if incomplete baskets can always be fully rolled back, which is not yet proved under outage conditions.
5. **Promotion state:** the Double Draw must be in a publicly guaranteed second-draw state under then-current promotion rules.
6. **Other costs:** retailer operating costs, franchise tax if incremental, accounting costs, and any other taxes must be included for the actual entity.

## Result
- **C-corporation tax salvage:** VALIDATED as a numerical conditional screen. At 23% simplified federal+NC income tax, the 7% commission overlay remains positive: about +$1.545 per $50 face cover / +3.09% of face.
- **Standalone new-retailer strategy:** REJECTED on current evidence because fixed retailer/franchise costs plus liability-limited scaling are not bounded by the small edge.
- **Existing licensed C-corp retailer:** remains a strong conditional candidate, but own-store commission, corporate ticket ownership, atomic rollback and active forced-state gates remain unresolved.
- **Terminal SUCCESS:** NOT PROVEN.

## Next action
Highest-value next packet should seek one of:
1. authoritative NCEL retailer accounting/terminal documentation showing whether an own-store owner/entity ticket is included in commission-bearing gross sales;
2. current NCEL claim/retailer language proving a retailer legal entity may own/claim its own valid draw tickets;
3. terminal manual evidence for bulk/sequence cancellation and behavior after terminal interruption;
4. a different cumulative-trigger lottery promo that reaches >100% deterministic coverage without relying on retailer commission, avoiding these entity/tax gates entirely.
