# H307 — Salexmo visible instant-win identifiers vs random allocation

## Question
Can the published `Available!` instant-win numbers on a Salexmo competition be bought directly for a deterministic cash profit?

## Current candidate checked
Competition: `£300 CASH FOR 3P, PLUS CASH INSTANT WINS 11/9/26`.

The public competition page showed:
- £0.03 per ticket;
- 40,000 maximum entries;
- 10,000 maximum entries per user;
- 5,583 sold / 34,417 remaining at the checked snapshot;
- ten £30 instant-win identifiers, nine still marked `Available!`;
- examples of available instant-win identifiers included 765, 8740, 12133, 17990, 22567, 26244, 29294, 38818, and 39213;
- `Choose Your Tickets!` wording;
- ticket numbers are shown after order confirmation;
- free postal entries receive 29 tickets and are also eligible for instant prizes.

The naive apparent arbitrage would be enormous: if identifier 765 could be deliberately selected, £0.03 would deterministically purchase a £30 cash prize.

## Rule audit
That inference is invalid under the governing Terms & Conditions.

Salexmo Terms §4.1(B) states that all qualifying entrants are **randomly allocated an entry number on completion and payment**. Free-route entries use the same allocation method. The prize is triggered only when the allocated entry number corresponds to an instant-win number stated on the website.

The competition FAQ is consistent with this: ticket number(s) are disclosed after the order is confirmed. Thus the visible list is a transparency/status list, not evidence of pre-payment numerical selection.

## Exact adversarial bound
Snapshot values:

- remaining identifiers = 34,417
- remaining instant identifiers = 9
- remaining non-instant identifiers >= 34,408
- max entries per user = 10,000

Since `34,408 >= 10,000`, there is a valid random-allocation outcome in which every one of the player's maximum 10,000 entries receives a non-instant identifier.

The main end-prize does not provide a positive floor either. The player cannot acquire the whole 40,000-entry pool (user cap 10,000), and 5,583 identifiers were already sold at the snapshot. Therefore an external entry remains a legal main-draw winner.

So for any allowed H307 portfolio:

`minimum legal withdrawable cash payout = £0`.

This is stronger than an EV rejection; it is a strict worst-case impossibility for the targeting thesis.

## What would change the result
This family becomes interesting only if a competition provides all of the following:
1. numerical winning identifiers are published or otherwise deterministically known before purchase;
2. the user can **select and reserve that exact identifier before paying**;
3. the identifier remains prize-bearing after reservation/payment;
4. terms do not replace that selection with random allocation;
5. prize value strictly exceeds all acquisition/fee costs.

H307 therefore converts a promising visual/UI clue into a reusable screening rule: **published instant-win numbers are useless for deterministic arbitrage when entry numbers are randomly assigned after payment.**
