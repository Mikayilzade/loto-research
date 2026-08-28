# H326 VALIDATION

Date: 2026-08-28
Verdict: **VALIDATED CLOSED / CAP-AND-EXECUTION-BLOCKED**

## Independent arithmetic checks

Inputs:
- total identifiers `N = 350`;
- cash liability `P = £350`;
- online price `£1.99`;
- current Royal Mail 2nd Class postage `£0.91`;
- max entries per person `M = 35`;
- checked sold snapshot `S = 10`.

Checks:
- full online cost = `350 * 1.99 = £696.50`;
- full online ratio = `350 / 696.50 = 0.502512562814...`;
- full postal cost = `350 * 0.91 = £318.50`;
- full postal ratio = `350 / 318.50 = 1.098901098901...`;
- impossible full-postal surplus = `£31.50`;
- remaining identifiers at snapshot = `350 - 10 = 340`;
- impossible all-remaining postal cost = `340 * 0.91 = £309.40`;
- impossible all-remaining ratio = `350 / 309.40 = 1.131221719457...`;
- cap share = `35 / 350 = 0.10`;
- identifiers necessarily uncontrolled even from a pristine zero-sold start = `350 - 35 = 315`.

All values agree with `data/derived/h326_llf_postal_takeover_bound.json`.

## Structural validation

The live operator page states a 350-ticket pool, £350 cash prize, 35-entry person cap, random ticket allocation, free postal entry, and a guaranteed draw date. The same terms state that each free entry requires its own postcard, entries are allocated only after arrival/validation, late/sold-out entries are not counted, and the operator reserves discretion to refuse entries.

For a single-winner random draw, leaving at least one valid identifier outside the player's control is enough to preserve a legal losing outcome. H326 necessarily leaves at least 315 identifiers uncontrolled because `M < N`.

Therefore:

**strict guaranteed one-player cash floor = £0.**

The >100% impossible full-postal economics are real but non-executable under the governing cap/acceptance rules.

## Source checks

Operator draw/rules:
https://llfgames.com/competition/win-350-cash-for-1-99-56/

Royal Mail current 2nd Class price:
https://www.royalmail.com/sending/uk/2nd-class
