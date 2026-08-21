# H148 — Omaha August 2026 $2 Monthly Special: exact 3-Spot full-cover test

Updated: 2026-08-21
Status: **CURRENT NUMERIC SPECIAL RECOVERED / FULL-COVER GUARANTEE NEGATIVE / NO SUCCESS**

## Objective
Continue H147's highest-priority task by recovering a current numeric Nebraska Keno special and immediately testing it against the exact deterministic coverage theorem, rather than repeating the already-closed July Kearney Pick-1 3.00x check.

## Current official special recovered
The current Big Red Keno Omaha page exposes an August 1–31, 2026 promotion image at:

- https://bigredkeno.com/omaha
- https://bigredkeno.com/Content/Media/Image/Locations/omaha_monthly_keno_special.jpg

The official promotion graphic states:
- **$2 Monthly Special**;
- **August 1–31, 2026**;
- **3 Spot**;
- **Hit 3 — Win $102**;
- minimum ticket $1;
- Game ID K.

This is the first reliable current-August numeric Big Red special recovered after H146/H147.

## Exact full-space coverage
Nebraska-style Keno draws 20 numbers from 80. For a 3-Spot wager there are

`C(80,3) = 82,160`

possible unordered 3-number selections. If every 3-Spot is purchased for the same draw, exactly

`C(20,3) = 1,140`

of our tickets necessarily match all 3 drawn numbers, regardless of which 20-number draw occurs.

For the advertised **$2** special and **$102** Hit-3 prize:
- full-cover face cost = `82,160 * $2 = $164,320`;
- guaranteed number of Hit-3 winners = `1,140`;
- guaranteed gross = `1,140 * $102 = $116,280`;
- deterministic gross-return ratio = `$116,280 / $164,320 = 70.76436222%`;
- deterministic deficit = **-$48,040** before taxes, fees, limits or execution friction.

Equivalent multiplier form:

`R_3 = (102/2) * C(20,3)/C(80,3) = 51 * 1,140/82,160 = 70.76436222%`.

Therefore the current Omaha August special is **inferior to the already validated Virginia/Nebraska 75% Pick-1 target** for deterministic coverage.

## Subsidy threshold
To invert this exact special into a guaranteed pre-tax profit using a deterministic external subsidy, the player would need external cash outlay below the guaranteed gross of $116,280.

Relative to the $164,320 face cost, the necessary discount/free-credit fraction is:

`1 - 116,280 / 164,320 = 29.23563778%`.

So a pre-owned/locked subsidy must exceed **29.2356% of face spend** merely to cross pre-tax break-even. This is worse than the **25%** subsidy threshold of a 75% Pick-1 cover.

A small fixed coupon does not solve the large full-space requirement: even a $5 free-play credit changes the ratio negligibly at this scale.

## General theorem for single-tier k-Spot specials
For a Keno draw selecting `d=20` numbers from `N=80`, if a k-Spot special costs stake `s` and pays `P` only when all k selected numbers are drawn, complete coverage of all `C(N,k)` selections guarantees `C(d,k)` winners. The deterministic return is

`R_k = (P/s) * C(d,k) / C(N,k)`.

A special is standalone full-cover profitable iff

`P/s > C(N,k)/C(d,k)`.

For k=3 the required payout multiplier is:

`C(80,3)/C(20,3) = 72.07017544x`.

At $2 stake the break-even Hit-3 payout is therefore **>$144.14035**. Omaha's $102 is far below this threshold.

This formula gives a fast screen for future Nebraska special images before deeper execution analysis.

## Execution relevance
H147's withdrawable Play+ + pre-game void/refund architecture remains useful for a threshold-crossing special, but it cannot rescue negative deterministic arithmetic. Even perfect atomic acceptance/rollback would leave this Omaha August 3-Spot special at only 70.7644% gross.

The current special therefore should be closed without spending time on bulk-void, tax or wager-limit analysis.

## Result
- Current August 2026 Big Red Omaha numeric special: **RECOVERED**.
- Exact full-cover combinatorics: **VALIDATED**.
- Guaranteed gross ratio: **70.7644%**.
- Required deterministic subsidy to break even: **>29.2356%** of face spend.
- Standalone guaranteed-profit route: **REJECTED**.
- Better known deterministic target remains the 75% Pick-1 class from H142/H146.
- Terminal SUCCESS: **NO**.

## Next action
1. Use image search/current community pages to recover **other August 2026 Big Red specials** (Lincoln, Fremont, Norfolk, Kearney, La Vista and smaller communities), then apply the generalized k-Spot threshold formula immediately.
2. Prioritize Pick-1 specials above 4.00x, or any special whose exact `R_k > 1` before subsidy.
3. For specials with `0.75 < R_k <= 1`, search only if a genuinely pre-owned deterministic coupon/discount exceeds the exact deficit.
4. Continue H147 execution-lock analysis only after a mathematically threshold-crossing special is found.
