# H311 — Kilted Lucky Dips finite-pool takeover bound

Checked: 2026-08-27

## Why this candidate matters

This live competition is unusually close to the target structure. The operator publishes a finite pool of 10,000 tickets at £20 each, says all 10,000 are instant winners, advertises £200,000 worth of prizes, and separately states a £1,000 cash end prize. If one person could own the entire pool, a deliberately player-favourable interpretation would be £201,000 liabilities against £200,000 acquisition cost: 100.5% gross, a nominal £1,000 surplus.

This is therefore materially stronger than the earlier sub-100% finite-pool screens.

## Live operator facts

Source: https://www.kiltedcompetitions.co.uk/product/kilted-lucky-dips-200000-prize-pot-every-ticket-wins/

Snapshot facts from the live page:
- 10,000 total tickets;
- £20 per entry;
- maximum 499 tickets per person;
- tickets are randomly allocated after the order is placed;
- 10,000 instant wins are stated;
- £200,000 worth of prizes is stated;
- £1,000 cash end prize is stated separately;
- live snapshot showed 1,215 sold and 8,785 remaining;
- draw is guaranteed for 30 Aug 2026 even if not sold out.

## Exact arithmetic

Full paid pool cost:

`10,000 × £20 = £200,000`.

Player-favourable liability interpretation:

`£200,000 + £1,000 = £201,000`, hence

`£201,000 / £200,000 = 1.005 = 100.5%`.

If the £1,000 end prize is already included inside the £200,000 headline, the full-pool ratio is exactly 100%, so there is no strict profit even under full ownership. H311 intentionally uses the stronger additive reading, because the execution blocker below already closes the strategy.

## Strict takeover blocker

The published per-person cap is 499, so a single eligible player can control at most

`499 / 10,000 = 4.99%`

of the advertised identifier universe.

At the checked snapshot 1,215 tickets were already sold. Even under the impossible favourable assumption that the same player already owned the maximum 499 of those sold tickets, at least

`1,215 - 499 = 716`

sold identifiers must still be external.

The end draw selects a winning ticket number by RNG from entrants. Therefore an external identifier remains a legal end-draw winner. Full identifier ownership — the only simple way to turn the headline prize pool into a deterministic takeover — is forbidden by the published cap.

Random allocation also prevents targeted purchase of known favourable identifiers before checkout.

## Result

**CLOSED / TAKEOVER-BLOCKED.**

H311 is a useful positive-economics near miss: under the strongest reading, full-pool liabilities can reach 100.5% of face acquisition cost. But the actual rules cap one player at 499/10,000 identifiers, and already-sold external identifiers exist. Therefore the finite-pool takeover route cannot yield a strict guaranteed profit for one eligible player.

Reopen only if a future competition preserves >100% deterministic liabilities while allowing one eligible player to reserve/control the complete finite winning-identifier set (or an equivalent mathematically sufficient set).
