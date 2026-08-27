# H323 independent validation

Checked: 2026-08-28

## Input assertions

- Total finite identifiers: 499,999.
- Published ordinary unit price: £0.79.
- Published SUN10 promotional price: £0.71.
- Published cash alternative: £140,000.
- Published maximum per person: 950.
- Checked live-page snapshot sold count: 37,281.

## Arithmetic re-check

- Base full-pool cost: `499,999 × 0.79 = £394,999.21`.
- SUN10 full-pool cost: `499,999 × 0.71 = £354,999.29`.
- Impossible-perfect gross ratio: `140,000 / 354,999.29 = 0.3943669859170704`.
- Impossible-perfect deficit: `£354,999.29 − £140,000 = £214,999.29`.
- Exact break-even unit price: `140,000 / 499,999 = £0.28000056000112`.
- Required discount from £0.79 to break even: `64.5568911391%`.
- Required further discount from £0.71 to break even: `60.5633014083%`.
- Maximum one-person advertised-space control: `950 / 499,999 = 0.0019000038000076` = `0.19000038%`.

## Strict conclusion checks

`£354,999.29 > £140,000`, so even impossible-perfect discounted full ownership is below cost.

`950 < 499,999`, so real one-player full takeover is impossible under the published cap. The live snapshot already contains more sold tickets (37,281) than the player's total allowed entries (950), so a legal external-winner outcome exists regardless of allocation details.

Therefore H323 is correctly classified **CLOSED / CAP-AND-ECONOMICS-BLOCKED**. No success claim is justified.
