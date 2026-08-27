# H303 — Birdie Tickets electronic-reservation finite-pool screen

Updated: 2026-08-27
State: **OPEN / EVIDENCE-BLOCKED; NOT SUCCESS**

## Why this packet exists

H302 found a finite UK cash competition whose free postal route could cross the arithmetic break-even threshold, but physical delivery made ownership of the finite pool non-deterministic. H303 tests the next structural filter: a platform where entry identifiers are electronically locked immediately and the promotion is explicitly hard-capped, while a no-purchase route also exists.

Birdie Tickets is a current US sweepstakes platform for golf equipment. Its public Trust & Safety material says:

- each promotion has a number of entries **capped up front**;
- a no-purchase method is always available under the Official Rules;
- after entries close, the winner is selected by a reproducible random drawing;
- winners complete a $1 verification checkout to receive the prize.

Its public home/browse pages separately say paid tickets receive **instant confirmation** and the Birdie Ticket number(s) are **locked in**, with Stripe checkout and idempotent server-side webhooks.

This is the first checked mechanism after H302 that simultaneously exposes a hard finite cap, electronically locked identifiers, and an advertised free entry route.

## Structural takeover theorem

For a promotion with exactly `N` eligible entry identifiers and one positive-value prize `V`, if all of the following are true:

1. the free/no-purchase method receives identifiers from the **same finite N-entry pool**;
2. an entrant can submit at least `N` valid free entries (or enough free entries plus paid entries) without a per-person cap below N;
3. each accepted free entry is electronically acknowledged and reserves its identifier before later paid entrants can consume it;
4. all N identifiers can be acquired by one eligible player;
5. the promotion cannot create extra external identifiers after the cap is reached;

then complete ownership makes the winner deterministic. With zero-cost electronic AMOE, the acquisition cost can approach only the explicit winner-verification/claim friction; any strictly positive transferable prize value would then create positive arithmetic.

The theorem is materially stronger than H302 because it removes postal loss/delay **if** the free route itself has the same electronic reservation property.

## What is already verified

Public current Birdie material supports:

- finite cap: `Every Birdie Ticket is tied to a specific prize, with the number of entries capped up front`;
- free route existence: `No purchase is ever required—there is always a free method of entry`;
- paid electronic reservation: `Secure checkout, instant confirmation, and your Birdie Ticket number(s) locked in`;
- winner verification cost: `$1 winner verification checkout`;
- draw reproducibility: public seed / reproducible random process.

Sources:

- https://birdietickets.com/trust
- https://birdietickets.com/
- https://birdietickets.com/tickets
- https://birdietickets.com/rules

## Missing evidence / why this is NOT SUCCESS

The public crawl of `/rules` currently renders only `Loading Official Rules...`; it does not expose the loaded rule body. Therefore the critical free-entry terms could not be certified in this pass.

Specifically still unknown from an authoritative accessible rule body:

- whether the AMOE is online/electronic or postal/mail;
- whether free entries are assigned from the same capped identifier pool as paid tickets;
- free-entry frequency/per-person limits;
- whether free entries are acknowledged/locked immediately like paid tickets;
- whether promotion-specific caps or household limits prevent full ownership;
- exact current live-draw cap, paid price and prize/cash alternative for an arithmetic instance.

The existence of an electronic paid path is **not** enough: paid ticket locking cannot be imputed to the free route. Likewise, `No purchase necessary` does not imply unlimited free entries.

## Result

**NO SUCCESS.** Birdie Tickets passes more of the H302 structural filter than ordinary postal competitions, but the decisive AMOE reservation/cap terms are not yet publicly readable in the indexed rule body used here. No profitable takeover is claimed.

## NEXT ACTION

Continue H303 only if the actual Birdie Official Rules payload can be retrieved or an authoritative indexed copy exposes the AMOE details. The exact gates to extract are: free entry method, per-person/free-entry cap, whether free identifiers consume the same finite inventory, acknowledgement timing, and one live draw's `N / price / prize` economics.

If any of these gates shows postal-only AMOE, a per-person cap `< N`, non-reserved free entries, or external identifiers that can still be issued after our entries, close H303 as execution-blocked. If all gates pass, run the exact mixed free/paid takeover cost before any SUCCESS claim.
