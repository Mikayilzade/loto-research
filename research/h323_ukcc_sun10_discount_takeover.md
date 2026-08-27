# H323 — UKCC SUN10 discounted finite-pool takeover screen

Checked: 2026-08-28
Status: **CLOSED / CAP-AND-ECONOMICS-BLOCKED**

## Why this candidate

The live UKCC VW Crafter Campervan + Mercedes GLC draw is a finite guaranteed-winner pool. A current Sun promotion supplies a deterministic price reduction: the ordinary ticket price is £0.79 and code `SUN10` reduces it to £0.71. The winner may choose a £140,000 tax-free cash alternative.

This is therefore a direct test of the current NEXT ACTION: can a documented deterministic discount push a finite-pool takeover through 100%?

## Published mechanics used

Live UKCC page snapshot:
- total identifiers: **499,999**;
- ordinary price: **£0.79**;
- cash alternative: **£140,000**;
- maximum entries per person: **950**;
- snapshot sold: **37,281**;
- winner guaranteed regardless of sellout.

The Sun promotion, published 24 Aug 2026, states that code `SUN10` reduces the ticket price from 79p to **71p** and that the competition closes 30 Aug 2026.

Sources:
- https://welcome.ukcarpcompetitions.co.uk/competition/vwglc
- https://www.thesun.co.uk/sport/38564587/win-car-competition-ukcc/

## Stronger-than-real exact takeover arithmetic

Give the player an impossible advantage: every one of the 499,999 identifiers is acquired at the promotional 71p price and the player takes the full £140,000 cash alternative.

- discounted full-pool cost = `499,999 × £0.71 = £354,999.29`;
- maximum deterministic cash liability = **£140,000**;
- gross ratio = `140,000 / 354,999.29 = 39.4366985917%`;
- deficit = **£214,999.29**.

Thus even perfect ownership of the entire finite pool at the documented promotional price is far below break-even.

The exact full-pool break-even ticket price would be only

`£140,000 / 499,999 = £0.28000056`.

Relative to the ordinary 79p price, a discount greater than **64.5569%** would be needed merely to reach break-even. Relative to the already-discounted 71p price, a further reduction greater than **60.5633%** would still be required.

## Independent cap blocker

The real maximum is only 950 entries per person:

`950 / 499,999 = 0.19000038%` of the advertised identifier space.

Therefore one player cannot take over the pool. The checked snapshot already had 37,281 sold entries, which is itself larger than the entire per-person allowance. There remains a legal outcome in which an externally held identifier wins, giving our portfolio **£0** from this competition.

## Conclusion

H323 is closed twice over:

1. **economics blocker:** even impossible-perfect ownership at the SUN10 price returns only 39.4367%;
2. **control blocker:** real max ownership is only 950/499,999, so a legal external-winner outcome necessarily remains.

The 10% media discount is genuine and deterministic but nowhere near the exact subsidy required for takeover profit.

## Reusable gate

For a finite one-prize pool with `N` identifiers, cash alternative `P`, and deterministic discounted unit price `c`, full takeover is worth further execution work only if `P > N*c`. Separately, a one-player strict takeover requires the applicable per-player cap to cover the necessary identifier set. H323 fails both tests by a wide margin.
