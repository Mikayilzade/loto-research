# H127 — Pennsylvania Millionaire Raffle weekly-cohort overlay

Updated: 2026-08-20
Status: **NEW COHORT-LOCAL OVERLAY MECHANISM VALIDATED / HISTORICAL 2025 COHORTS NEGATIVE / LIVE MONITOR CLASS OPEN / NO GUARANTEE**

## Goal
Extend H122-H126 beyond simple whole-game undersubscription. Test whether a raffle can create a positive-EV purchase cohort even when the final game later sells out, because an extra fixed prize board is allocated only among tickets sold during a short entry window.

## Primary architecture
Pennsylvania Millionaire Raffle XXXV (sales Nov. 4-Dec. 30, 2025) provides a clean example.

Official Pennsylvania Bulletin rules:
- ticket price: **$20**;
- maximum tickets: **500,000**;
- final draw samples **6,000 winners from tickets actually sold**;
- final cash board: 4 × $1,000,000; 4 × $100,000; 100 × $1,000; 5,892 × $100;
- all final prizes are one-time lump-sum cash payments;
- eight weekly drawings each award **2 × $50,000 = $100,000**;
- critically, in the ordinary unsold state each weekly drawing is drawn only from tickets sold in that weekly entry period.

Primary source:
- Pennsylvania Bulletin, Millionaire Raffle XXXV rules: https://www.pacodeandbulletin.gov/Display/pabull?file=%2Fsecure%2Fpabulletin%2Fdata%2Fvol55%2F55-44%2F1491.html

The fixed final cash board is:

`B_final = 4,000,000 + 400,000 + 100,000 + 589,200 = $5,089,200`.

For a ticket bought in a weekly cohort of size `w`, with eventual final sold count `N`, pre-tax expected cash value is:

`EV = B_final / N + 100,000 / w`.

This is different from an ordinary raffle. The second term depends on **local weekly sales**, not total final sales.

## Exact positive-EV boundary
At $20 ticket price, positive pre-tax EV requires:

`5,089,200 / N + 100,000 / w > 20`.

For `N > 254,460`, solve for the maximum weekly cohort size:

`w* = 100,000 / (20 - 5,089,200/N)`.

Examples:

| eventual final N | final-draw EV/ticket | weekly cohort must be below |
|---:|---:|---:|
| 500,000 | $10.1784 | **10,181.6** |
| 450,000 | $11.3093 | **11,506.6** |
| 400,000 | $12.7230 | **13,741.9** |
| 350,000 | $14.5406 | **18,316.9** |
| 300,000 | $16.9640 | **32,938.1** |
| 275,000 | $18.5062 | **66,942.6** |
| 260,000 | $19.5738 | **234,657.0** |

If final sales are `N <= 254,460`, the final fixed board alone is already positive pre-tax EV, so the weekly draw is additional overlay.

## Historical 2025 calibration
Contemporary reports quoting Pennsylvania Lottery provide actual cohort sizes:
- week 2 (Nov. 11-17): **44,200** tickets sold;
- week 3 (Nov. 18-24): **more than 47,500** tickets sold.

References:
- Nov. 24, 2025 report for week 2: https://www.yahoo.com/news/articles/winning-pa-lottery-ticket-worth-142710167.html
- Dec. 2, 2025 report for week 3: https://www.shorenewsnetwork.com/two-pennsylvania-players-strike-50k-in-holiday-raffle-surprise/

The game ultimately sold all **500,000** tickets by Dec. 30, 2025 (contemporary post-draw report):
- https://patch.com/pennsylvania/haverford/1m-winning-raffle-ticket-sold-havertown

At final `N=500,000`:
- week-2 ticket EV ≈ `$10.1784 + $100,000/44,200 = $12.4408`, gross **62.2042%**, ROI **-37.7958%**;
- week-3 ticket EV at exactly 47,500 ≈ `$12.2837`, gross **61.4183%**, ROI **-38.5817%** (actual >47,500 is slightly worse).

A prior 2024 weekly cohort reported about **54,400** tickets in one week; at a 500,000-ticket final denominator that architecture would yield only about **$12.0166** per $20 ticket.

Thus known historical Pennsylvania cohorts are far above the ~10.2k weekly break-even threshold when the game sells out.

## Why this matters
H127 identifies a reusable lottery-specific nonlinearity that simple whole-game `prize board / final sold count` monitoring misses.

A future raffle can become positive EV even if it later sells out when:
1. a fixed cash bonus is ring-fenced to a short purchase cohort;
2. that cohort is unusually undersubscribed;
3. the ticket remains eligible for a sufficiently valuable final fixed board.

The correct live-monitor state is therefore at least two-dimensional:
- projected/final total sold `N`;
- current cohort sold count `w`.

A monitor should compute `EV(N,w)` rather than only `EV(N)`.

## Guarantee analysis
Positive EV is not terminal SUCCESS. Any single ticket or incomplete block can still receive $0 from both weekly and final draws.

Buying an entire weekly cohort after external tickets have already sold is impossible; buying every ticket from the start of the weekly window would require controlling all retail sales, which the player cannot guarantee. Buying the entire 500,000-ticket game from launch costs $10m versus a final board of $5.0892m plus $0.8m weekly prizes, still far below cost.

Therefore H127 is:
- **a validated new positive-EV monitor class**;
- **historically negative in the recovered 2025 Pennsylvania cohorts**;
- **not a guaranteed-profit strategy**.

## Current / upcoming monitor implication
As of 2026-08-20, no new Pennsylvania New Year's Millionaire Raffle rules for the 2026-27 cycle were recovered in the fresh search. Historically this rule is published around the autumn sales launch. If the weekly-cohort architecture returns, monitoring should begin immediately because a weak first or later weekly sales period can be evaluated with the exact equation above before the final sales outcome is known.

The same scan should be applied globally to any raffle with:
- fixed final board;
- cohort-local early-bird/weekly cash boards;
- public or inferable cohort sales counts;
- deadline drawing even without sellout.

## Next test
1. Search current/upcoming 2026-27 fixed-board raffles for cohort-local prize windows.
2. Precompute `EV(N,w)` threshold grids before sales open.
3. Prefer official live counters or operator statements of cohort entry counts.
4. Pursue only states materially above cash/tax/cost break-even; do not confuse positive EV with guaranteed profit.
