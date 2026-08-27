# H315 validation

Validated: 2026-08-27

## Arithmetic checks

- Total tickets: 175,000.
- Sold snapshot: 38,626.
- Remaining: 136,374.
- Remaining instant-win identifiers shown available: 137.
- Therefore remaining non-instant identifiers are at least 136,237.
- Per-person cap: 500.
- `136,237 >= 500`, so a zero-instant-win allocation of a maximum-size one-player purchase is feasible.
- Maximum displayed 500-ticket discount is 24%; discounted cost is `500 × 0.49 × 0.76 = £186.20`.

## Guarantee check

The live interface exposes quantity selection rather than exact identifier reservation. The U Comps terms do not grant exact identifier selection/reservation, and the underlying competition-platform provider describes no ticket reservation with allocation after purchase success.

Therefore no listed `Win Now` identifier may be treated as player-selectable for a rigorous guarantee.

Because one entrant can control at most 500 of 175,000 identifiers, the final draw also preserves legal external-winning outcomes.

## Result

- strict instant-win cash floor: **£0**;
- strict combined cash floor: **£0**;
- closure: **CLOSED / TAKEOVER-BLOCKED**.

No SUCCESS claim is warranted.
