# H295 — 2026 Hollydays finite-raffle takeover gate

Checked: 2026-08-26

## Question
Can either currently advertised 2026 Junior League of Baton Rouge Hollydays raffle be converted into a strict guaranteed-profit full-identifier takeover?

## Current official evidence
The official Hollydays event page advertises two raffles for the October 9, 2026 event:

- Lee Michaels $10,000 Shimmering Shopping Spree: $50 per raffle ticket. Current search-rendered official event data states only 500 tickets.
- 2026 Mercedes-Benz GLB 250 SUV: $10 per raffle ticket, advertised MSRP $50,605. Winner need not be present; the winner is responsible for taxes and must claim the vehicle. The current public page does not publish a maximum number of Mercedes raffle entries or a cash alternative.

Sources:
- https://www.juniorleaguebr.org/fundraisers/hollydays/
- https://www.juniorleaguebr.org/fundraisers/hollydays/tickets-events/
- https://vms.ajli.org/?nd=p_vms_registration_event_detail&registration_id=235735

## Exact arithmetic
### Shopping Spree
Even granting impossible-perfect ownership of all 500 entries:

- acquisition cost = 500 × $50 = **$25,000**;
- deterministic prize = **$10,000**;
- gross ratio = **40%**;
- deficit = **$15,000**.

Therefore this raffle is closed by arithmetic before any execution constraints matter.

### Mercedes raffle
Let `N` be the total number of valid Mercedes raffle entries. Under the deliberately player-favourable assumptions that one player owns all `N` entries, that the vehicle is worth the full stated MSRP to that player, and that taxes/resale friction are zero, strict positive gross requires:

`50,605 > 10 N`, hence **N <= 5,060**.

At N=5,061 the acquisition cost is $50,610, already above MSRP. Thus a published hard cap at or below 5,060 would be only the first necessary economics gate.

The public 2026 event materials checked in this pass publish the $10 entry price and $50,605 MSRP but no Mercedes-entry cap. They also describe the prize as a taxable vehicle rather than a cash alternative. The public purchase flow issues emailed ticket numbers but does not establish a bounded reservable universe that one player can guarantee acquiring in full.

## Rigorous conclusion
- **Shopping Spree: CLOSED / REJECTED.** Impossible-perfect full ownership returns only 40%.
- **Mercedes: CLOSED FOR CURRENT RIGOROUS-GUARANTEE PURPOSE / DATA-EXECUTION BLOCKED.** Without a published hard cap and guaranteed full acquisition of all eligible identifiers, a finite takeover cannot be certified. Even if a cap <=5,060 later appears, tax and realizable-cash-value gates would still need proof.

This is not a SUCCESS and does not exhaust global lottery research.
