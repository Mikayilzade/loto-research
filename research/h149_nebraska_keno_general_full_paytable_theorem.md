# H149 — Nebraska Keno general full-paytable deterministic screen

Updated: 2026-08-21
Scope: LOTTERY ONLY
Status: **GENERAL EXACT SCREEN VALIDATED / NO CURRENT LIVE SPECIAL ABOVE BREAK-EVEN IDENTIFIED IN THIS PACKET**

## Purpose
H148 gave a fast formula for a special that pays only on Hit-k. This packet generalizes that result to an arbitrary fixed k-Spot paytable that can pay on several hit counts.

Nebraska-style Keno draws 20 numbers from 80. Suppose the player buys **every k-subset of the 80 numbers** at stake `s` per ticket. Let `P_j` be the cash payout for a k-Spot ticket that matches exactly `j` of the 20 drawn numbers.

For every possible draw, the number of our k-Spot tickets with exactly j hits is fixed:

`N(k,j) = C(20,j) * C(60,k-j)`

for feasible j. This is independent of which 20 numbers are drawn.

Therefore:

- number of purchased tickets = `C(80,k)`;
- face cost = `S = s * C(80,k)`;
- deterministic gross payout = `G = sum_j P_j * C(20,j) * C(60,k-j)`;
- deterministic gross-return ratio =

`R_k = G/S = [sum_j (P_j/s) * C(20,j) * C(60,k-j)] / C(80,k)`.

This is an exact all-outcome identity, not an EV approximation.

## Consequence
Any fixed Nebraska Keno special whose full paytable is known can now be classified immediately:

- `R_k > 1`: standalone deterministic positive pre-tax cover;
- `R_k = 1`: exact pre-tax break-even;
- `0.75 < R_k < 1`: stronger than the existing 75% Pick-1 benchmark but still needs a deterministic subsidy larger than `1-R_k`;
- `R_k <= 0.75`: inferior to the known Pick-1 target unless execution/capital constraints are materially better.

A deterministic pre-owned discount/credit fraction `d` of face spend inverts a fixed paytable iff `R_k + d > 1` when the credit reduces external cash dollar-for-dollar and does not alter payout eligibility.

## Hit-k-only thresholds
If the special pays only Hit-k with payout `P`, then H148 is recovered:

`R_k = (P/s) * C(20,k)/C(80,k)`.

Standalone break-even requires:

`P/s > C(80,k)/C(20,k)`.

Exact break-even payout multipliers:

| k | C(80,k) | C(20,k) winners in full cover | Break-even P/s |
|---:|---:|---:|---:|
| 1 | 80 | 20 | 4.000000x |
| 2 | 3,160 | 190 | 16.631579x |
| 3 | 82,160 | 1,140 | 72.070175x |
| 4 | 1,581,580 | 4,845 | 326.435501x |
| 5 | 24,040,016 | 15,504 | 1,550.568627x |
| 6 | 300,500,200 | 38,760 | 7,752.843137x |
| 7 | 3,176,716,400 | 77,520 | 40,979.313725x |
| 8 | 28,987,537,150 | 125,970 | 230,114.607843x |
| 9 | 231,900,297,200 | 167,960 | 1,380,687.647059x |
| 10 | 1,646,492,110,120 | 184,756 | 8,911,711.176471x |

For a $2 Hit-3 special the exact break-even payout is `$144.140351`, reproducing H148 and showing Omaha's current `$102` payout is decisively below threshold.

## Why this matters operationally
The search bottleneck is now **only live paytable recovery**, not combinatorics. A current image/menu can be transcribed into the formula and classified exactly in seconds. This also prevents wasting execution/tax research on attractive-looking specials that are mathematically incapable of a guaranteed cover.

The general formula is stronger than an EV screen because complete k-subset ownership fixes the count of every hit class for every legal draw. If the paytable itself is fixed/non-shareable, draw randomness disappears from gross cash.

## Limits
This theorem does not by itself solve:
- purchase limits or incomplete basket acceptance;
- cancellation/void rules;
- taxes;
- free-play restrictions;
- pari-mutuel or liability-capped payouts;
- a special being withdrawn before the cover is placed.

Those gates should be investigated only after `R_k` crosses the relevant arithmetic threshold.

## Result
**General arbitrary-paytable full-cover theorem: VALIDATED.**
No new live August special was numerically recovered in this packet because the fresh public-web search endpoint was temporarily unavailable during the run; this is a transient data-retrieval issue, not a terminal project blocker.

Next live search should prioritize current Nebraska special images/paytables and apply this exact formula immediately.
