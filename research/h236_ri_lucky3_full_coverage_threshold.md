# H236 — Rhode Island Lucky 3 Spot Keno doubled full-space threshold

Date: 2026-08-24
Scope: lottery-only; Keno promotion / combinatorial coverage.

## Primary evidence
Rhode Island Lottery historical Lucky 3 Spot rules (2024 and 2025) establish a real pre-draw nonlinear entitlement: only 3-spot Keno tickets can qualify; a qualifying ticket prints a visible Lucky 3 Spot message and, if it wins, the corresponding Keno prize is doubled. The 2025 rules also state that qualifying Lucky 3 Spot tickets cannot be cancelled and that retailers may not print Keno tickets in advance of sale.

The general Rhode Island Keno rules state that Keno selects 1–10 spots from 80, draws 20 numbers, permits $1/$2/$5/$10 wagers, and ordinarily allows same-day same-terminal cancellation before the draw (multi-draw only before its first draw).

As of the 2026-08-24 search, the official RI Lottery homepage visibly advertises a current `Kick Back with Keno Promotion`, but this packet did not recover its exact rules. Therefore no historical Lucky 3 mechanics are projected onto the current promotion.

Primary sources checked:
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/LaunchAlertRules-Lucky3SpotKenoBingoDoubler.pdf
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2024/Lucky3SpotKenoRule091224.pdf
- official RI Lottery Rules / Keno section indexed at https://www.rilot.com/en-us/about-us/lottery-rules.html
- current RI Lottery homepage https://www.rilot.com/en-us/home.html

## Exact full-space identity
Buy each 3-subset of 80 exactly once for one draw. There are

`C(80,3) = 82,160` lines.

For any realized 20-number draw, the number of purchased lines matching exactly `j` drawn numbers is fixed:

- 0/3: `C(20,0)C(60,3) = 34,220`
- 1/3: `C(20,1)C(60,2) = 35,400`
- 2/3: `C(20,2)C(60,1) = 11,400`
- 3/3: `C(20,3) = 1,140`

Thus the draw itself creates no variance for a full 3-spot cover.

Let `P2` and `P3` be the ordinary $1 payouts for 2/3 and 3/3. If **every one** of the 82,160 lines carried a true 2x Lucky entitlement, deterministic doubled gross would be

`G = 2*(11,400*P2 + 1,140*P3)`.

Strict pre-tax profit on the $82,160 ticket spend requires

`10*P2 + P3 > 36.03508771929825`.

This is an exact structural threshold, independent of the actual draw.

## Why this is not SUCCESS
The historical promotion proves that a printed pre-draw 2x entitlement can exist, but it does **not** prove an executable way to acquire the entitlement on all 82,160 distinct combinations.

The potentially interesting cancellation asymmetry is real: ordinary Keno tickets are generally cancellable before draw, while Lucky 3 Spot tickets explicitly are not. But the recovered promotion rules do not state that a player may repeatedly purchase arbitrary selections, cancel every non-Lucky ticket, and continue until obtaining Lucky status for every desired combination. They also prohibit retailer preprinting and constrain the promotion to a finite location/time window. No entitlement frequency, issuance algorithm, throughput guarantee, or right to repeated cancellation-for-selection is stated.

Therefore the exact doubled-coverage inequality is a **necessary mathematical opportunity condition**, not an executable guaranteed-profit strategy.

## Current Kick Back with Keno
Fresh official evidence confirms the promotion is currently advertised on the RI Lottery homepage. Exact mechanics remain unrecovered. Without current primary rules, it is invalid to assume the historical Lucky 3 Spot doubling/cancellation structure applies.

## Result
**NO SUCCESS.** H236 adds a reusable exact theorem for any 20/80 3-spot promotion that doubles prizes without doubling stake, and narrows the only interesting execution path to entitlement acquisition. Historical Lucky 3 Spot remains non-executable as a strict guarantee on recovered evidence; current Kick Back remains open only if materially new primary rules reveal a deterministic or fully controllable entitlement mechanism.
