# H306 VALIDATION

Validated: 2026-08-27
Result: **PASS — current takeover blocked; no success claim**

## Checks

1. H225-X* terminal status was read before opening H306. H225-X20 remains 0 coefficient survivors / 0 legal shift tuples, so no X21/X22 work was created.
2. H306 does not duplicate H302-H305: it tests a distinct current **zero-price finite inventory** rather than paid/postal-discount acquisition or ordinary capped paid draws.
3. Current homepage evidence publishes a finite 1,000-ticket pool for the £100 cash draw and a positive sold percentage (16.2%).
4. Positive sold percentage implies at least one identifier has already been issued. Therefore one newly arriving entrant cannot own every eligible identifier in the current pool.
5. With at least one external eligible identifier, the draw outcome selecting that identifier is legal. The entrant's worst-case cash payout from this draw is therefore £0.
6. Published free-entry conditions independently state that free postal entries are not guaranteed by proof of posting and are rejected if the cap fills before receipt. This cannot certify atomic takeover of a fresh pool either.
7. No claim is made that 16.2% is an exact ticket count; the proof needs only `sold_pct > 0`.

## Terminal statement for this packet

**H306 is CLOSED / CURRENT-TAKEOVER-BLOCKED.** It is not a global exhaustion result. Reopen the mechanism only for a genuinely fresh finite pool with explicit same-inventory electronic free reservation and a per-player cap sufficient for full ownership.
