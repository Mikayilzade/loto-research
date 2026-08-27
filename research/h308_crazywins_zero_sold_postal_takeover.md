# H308 — CrazyWins zero-sold finite-pool / postal free-entry takeover

Date checked: 2026-08-27

## Research question

Can a newly opened / zero-sold UK competition with a finite entry cap and a free-entry route be taken over cheaply enough to make the winner deterministic?

This directly follows H306-H307. H306 found a nominally free finite pool but already had external ownership; H307 found published instant-win identifiers but allocation was random after purchase. H308 tests the stronger case where the indexed candidate appears to begin at zero sales.

## Candidate evidence

CrazyWins' indexed competition list showed **HAMSTER FRENZY** with:

- closing date: 29 Aug 2026;
- paid price: £0.10;
- finite cap: 2,000 entries;
- indexed snapshot: 0 tickets sold.

CrazyWins Terms & Conditions state that a free route exists, but it is postal. Each free entry must be submitted separately; bulk free entries count as one. Proof of posting does not guarantee entry, and an entry is rejected if the competition cap is reached before the postal item is received.

The same Terms state that instant-win entry numbers are randomly allocated after paid completion/payment, and free entrants receive a number selected by RNG. They also permit competition-specific per-entrant maxima.

Current Royal Mail 2nd Class pricing lists £0.91 for a letter/postcard up to 100g.

Sources checked:

- CrazyWins competition index: https://crazywins.co.uk/
- CrazyWins Terms & Conditions: https://crazywins.co.uk/terms-conditions/
- Royal Mail 2nd Class current price: https://www.royalmail.com/sending/uk/2nd-class

## Exact cost test

Let N = 2,000.

### Paid route

`2,000 × £0.10 = £200.00`.

### Postal free-entry route

Ignoring postcard/material/time costs and counting only minimum current 2nd Class postage:

`2,000 × £0.91 = £1,820.00`.

So the nominally free route costs:

`£1,820 / £200 = 9.1×`

as much as the paid face-value route for a hypothetical complete 2,000-entry submission.

This alone makes the postal AMOE the wrong economic instrument for a cheap takeover.

## Stronger execution proof

The more important result is structural and does not depend on the prize value.

A rigorous full-pool takeover requires every identifier needed for the deterministic winner condition to be acquired with certainty before an outside entrant can obtain one.

The published CrazyWins postal process does not have this property:

- each free entry travels separately;
- receipt is not guaranteed by proof of posting;
- cap may fill before receipt;
- free-route identifiers are allocated by RNG;
- paid entries can continue to enter the same finite competition during the postal window.

Therefore even if the indexed snapshot is literally zero sold, there remains a legal path in which at least one required postal entry is absent or an external paid entry occupies an identifier first.

If at least one eligible external identifier remains, the final random draw has a legal outcome selecting that external identifier. Thus the player's guaranteed main-prize cash floor from takeover is zero.

## Why zero sold is insufficient

This packet establishes a reusable distinction:

**zero sold != electronically reservable full inventory.**

For takeover research, a zero-sold snapshot is useful only if the acquisition channel gives immediate, atomic or otherwise guaranteed reservation of the entire required identifier set. Postal AMOE language with explicit nonreceipt and cap-race clauses fails that criterion.

## Conclusion

H308 is **CLOSED / EXECUTION-BLOCKED**.

The next search should prioritize newly launched finite pools where free or discounted entries are credited electronically to the same capped inventory at confirmation, with a published per-player limit high enough for complete control. Postal free-entry routes should be deprioritized unless their economics and receipt guarantees are materially different.
