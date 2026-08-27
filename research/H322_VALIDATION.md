# H322 VALIDATION

Validated: 2026-08-28
Packet: **H322**
Result: **CLOSED / CAP-AND-RANDOM-ALLOCATION-BLOCKED**

## Independent arithmetic checks

Inputs reproduced from the live page / governing rules:

- total identifiers = 500,000;
- per-person cap = 2,000;
- deterministic first-ticket subsidy = one free ticket;
- advertised instant-credit identifiers = 50,000;
- advertised cash-prize count = 5;
- identifier assignment = random from remaining pool; specific identifier choice prohibited.

Player-favourable disjoint-prize upper bound:

- maximum prize-bearing identifiers = 50,000 + 5 = **50,005**;
- minimum residual zero-instant identifiers = 500,000 - 50,005 = **449,995**;
- 449,995 >= 2,000, so the residual set can contain every ticket permitted to one player.

Therefore a legal allocation exists with zero instant cash for the player's entire allowed portfolio. The first-ticket-free discount does not alter that existence proof.

The main draw cannot restore a guaranteed floor because one player cannot control the full pool and valid external-winner states remain possible while the competition is open.

## Consistency checks

The competition UI includes a `Manual` control, but the controlling Competition Rules and Terms explicitly say ticket numbers are allocated randomly and entrants cannot choose specific numbers. H322 therefore does **not** treat the UI label as selectable ticket-ID evidence.

The result is robust to overlap among prize classes: overlap would reduce, not increase, the number of distinct prize-bearing identifiers and therefore strengthen the zero-floor proof.

## Closure criterion

H322 requires no CI or stochastic simulation. Closure follows by exact counting plus the published cap/allocation rules.

Strict withdrawable-cash floor: **£0**.
