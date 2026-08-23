# H242 — Rhode Island current rules: execution limits found, 3-spot paytable still unresolved

Date: 2026-08-24
Status: NOT SUCCESS, but major execution constraint resolved

## Objective
Replace the Ohio reference proxy with Rhode Island's current authoritative Keno economics and determine whether a future free 2X Lucky 3 Spot-style overlay could be executed at scale.

## Current official rule evidence
The current 2026 Rhode Island Lottery rules state for Keno:

- choose 1 to 10 spots from 80;
- 20 numbers are drawn;
- single-draw wagers may be $1, $2, $5, or $10;
- a player may wager on up to 15 consecutive draws;
- the maximum price for any Ticket or Registered Ticketless Play is $150, subject to stated exceptions for optional features.

This is important because it places a hard upper bound on how much coverage can be packed into one ordinary ticket/registered play. It also confirms that the current RI rules are not compatible with treating one ticket as an arbitrarily large batch container.

## Current RI website state
The official 2026 Keno page exposes a live purchase flow with number selection, wager per game, consecutive games, Keno Plus and Keno Overtime. It also contains a current `Keno Odds and Prizes` section, but the actual payout table is loaded dynamically and was not exposed in the searchable page text during this run.

Therefore the exact current RI 3-spot payout amounts have not yet been recovered from an authoritative source. The H240 +53.34% break-even threshold remains an Ohio-reference threshold and must not be labelled as the exact RI threshold.

## Operational implication
Even before the payout table is recovered, the current rules materially constrain the historical Lucky 3 Spot full-coverage thesis:

- 82,160 distinct 3-spots cannot be placed as one ordinary $82,160 ticket;
- at a $150 maximum ticket price, at least ceil(82,160/150) = 548 ordinary $1-wager ticket-equivalents would be needed even if each $1 play could be packed efficiently on a ticket;
- the 15-consecutive-draw feature does not solve same-draw combination coverage because repeating one selection over later draws is different from entering many distinct 3-spots into one draw;
- a future Lucky 3 Spot promotion would still need enough terminal throughput and enough allowed distinct boards/plays per ticket to submit the required construction during the qualifying window.

## New highest-value next step
Do not continue assuming full 82,160 coverage is the practical target. Re-open the compressed-design line and combine it with the newly established RI $150/ticket and 15-draw constraints. The correct target is now:

> find the smallest distinct 3-spot design whose worst-case doubled payout exceeds total stake, then test whether that design fits real RI ticket/transaction throughput.

This links the combinatorial survivor work from H232/H234 back to an executable promotion model.

## Verdict
NOT SUCCESS. The exact current RI 3-spot paytable remains unresolved because the official page renders it dynamically. However, H242 establishes a concrete current rule constraint: ordinary RI Keno tickets/registered plays are capped at $150 and up to 15 consecutive draws. This makes compressed same-draw designs substantially more important than brute-force 82,160-combination coverage.

## Sources
- Rhode Island Lottery current Keno page: https://www.rilot.com/en-us/keno.html
- Rhode Island Lottery 2026 Rules and Regulations (Keno section): indexed official rules search result under rilot.com/content/dam/interactive/ilottery/pdfs/about-us/
