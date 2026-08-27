# H315 — U Comps current instant-win identifier screen

Status: **CLOSED / TAKEOVER-BLOCKED**  
Snapshot: 2026-08-27

## Candidate

U Comps competition #143, `£50,000 Instant Win Competition`, is a finite current pool with publicly displayed instant-win identifiers.

Live-page snapshot:
- 175,000 total tickets;
- £0.49 base price;
- 500-ticket maximum per person;
- 38,626 tickets sold;
- 167 instant-win identifiers total;
- 137 instant wins still shown as available;
- multi-buy discount up to 24% at 500 tickets;
- closing date 14 September 2026.

Source: https://ucomps.co.uk/competition/143/ps50000-instant-win-competition

The page explicitly says instant wins occur when a purchased ticket number matches a listed instant-win ticket number. The currently unclaimed prize-bearing identifiers are published on the page.

## Why this looked interesting

A published unclaimed identifier carrying £10,000, £5,000, £2,500, £1,000, £100 or £50 would create an immediate deterministic profit if the player could reserve that exact identifier before payment at the displayed ticket price.

Therefore the critical question is not expected value. It is whether a player can deterministically acquire a listed winning identifier.

## Allocation / reservation evidence

The public U Comps terms describe buying a number of entries and impose the competition-specific per-person entry limit, but do not grant the player a right to reserve a particular identifier.

Source: https://ucomps.co.uk/policy/terms-and-conditions

The platform provider that showcases U Comps states its competition system uses **no ticket reservation** and that tickets are allocated **after purchase success**.

Source: https://ubercomps.com/

This is consistent with the live U Comps interface, which asks the user to select a quantity (`1, 5, 10, 50, 250, 500`) rather than an exact ticket identifier.

## Exact one-player worst-case bound

From the live snapshot:

- remaining tickets = `175000 - 38626 = 136374`;
- remaining instant-win identifiers = `137`;
- hence at least `136374 - 137 = 136237` remaining tickets are non-instant;
- one player may acquire at most `500` entries.

Since

`136237 >= 500`,

there exists a legal post-purchase allocation in which every one of the player's maximum 500 ticket identifiers is a non-instant identifier.

Therefore the instant-win component has strict one-player cash floor:

**£0**.

The separate end draw cannot repair the guarantee. A player capped at 500 cannot own all 175,000 possible identifiers, so there remains a legal final-draw outcome won by an external identifier. Thus the combined strict cash floor is also **£0**.

The 24% 500-ticket discount changes spend, not the zero floor. At the maximum displayed bundle discount:

`500 × £0.49 × 0.76 = £186.20`.

A legal outcome still returns £0.

## Conclusion

H315 is closed for strict guaranteed-profit purposes.

The useful reusable gate is:

> Publicly displaying prize-bearing identifiers is not exploitable when the entrant cannot reserve/select those identifiers before payment and the remaining zero-prize inventory is at least as large as the player's acquisition cap.

Reopen only if U Comps changes execution so that exact ticket identifiers can be selected and locked before checkout, or if a future competition makes every possible allocation within the permitted player cap carry a positive cash floor.
