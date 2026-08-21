# H152 — Nebraska Quarter Mania cross-city screen + La Vista subsidy check

Updated: 2026-08-21
Status: **NO NEW COVER ABOVE H151 / CURRENT LAVISTA $5 FREE-PLAY FAR BELOW COVER HURDLE / NO SUCCESS**

## Objective
Continue the H151 fixed-paytable Keno branch without repeating already-closed states. Two questions were tested:
1. do other official Nebraska 25-cent `Quarter Mania` tables beat La Vista Quarter Madness's 81.0636% deterministic full-cover ratio?
2. does the currently advertised La Vista player promotion supply enough deterministic free play to cross the H151 compact-cover break-even threshold?

## Sources
Official Big Red Keno paybooks presently served/indexed:
- Omaha paybook: https://bigredkeno.com/Content/Media/File/Document/Locations/omaha_paybook.pdf
- Lincoln paybook: https://bigredkeno.com/Content/Media/Image/Paybooks/Lincoln/BRK_LincolnPaybook_06-19-2018.pdf

These are official operator documents, but their document/version dates are older than the current August-2026 run. They are therefore used as exact cross-city paytable benchmarks, **not** as proof that a monthly 2026 special is currently unchanged.

Current La Vista sources:
- Quarter Madness: https://www.lavistakeno.com/quarter-madness
- Events: https://www.lavistakeno.com/events
- Big Red Keno App FAQ / funding / void / withdrawal mechanics: https://www.lavistakeno.com/frequentlyaskedquestions

The current La Vista event page advertises a burger-linked promotion with **$5 FREE Keno Play** on qualifying Wednesdays. The page also advertises a $2 burger discount. Because a food purchase is required, the $5 cannot be treated as zero-cost cash; this packet nevertheless tests the most player-favorable case by granting the entire $5 as deterministic lottery subsidy.

## Method
Apply the H149 complete-cover theorem for standard 20-of-80 Keno:

`N(k,j)=C(20,j) C(60,k-j)`

and, for a fixed paytable at $0.25 per way:

`R_k = sum_j N(k,j) P_j / (C(80,k) * 0.25)`.

This is draw-independent under complete k-subset coverage.

Reproducible implementation:
- `src/loto_research/h152_nebraska_quarter_crosscity.py`
- `data/derived/h152_nebraska_quarter_crosscity.csv`

## Exact results — Omaha Quarter Mania
Best deterministic full-cover ratio across Pick 1-16 is:
- **Pick 1 = 75.0000%**.

Selected compact states:
- Pick 2 = **66.1392%**;
- Pick 3 = **63.8267%**;
- Pick 5 = **66.0336%**.

No Omaha state beats La Vista H151's **81.0636%** benchmark.

## Exact results — Lincoln Quarter Mania
Best deterministic full-cover ratio across Pick 1-16 is:
- **Pick 1 = 75.0000%**.

Other relatively strong states:
- Pick 2 = **72.1519%**;
- Pick 3 = **69.3768%**;
- Pick 9 = **68.8424%**;
- Pick 11 = **68.7165%**.

No Lincoln state beats La Vista H151's **81.0636%** benchmark.

## Current La Vista $5 free-play stress test
H151's most executable Quarter Madness complete cover is Pick 2:
- 3,160 ways;
- $0.25 per way;
- face cost = **$790.00**;
- deterministic gross payout = **$617.50**;
- deficit = **$172.50**;
- exact subsidy hurdle = **21.8354%** of face cost.

Even granting the current advertised **$5 FREE Keno Play** full cash-equivalent value:
- effective external cost = $785.00;
- deterministic gross = $617.50;
- deterministic net = **-$167.50**;
- effective gross/external-cost ratio = **78.6624%**.

Thus the current $5 promotion covers only `5/790 = 0.6329%` of the Pick-2 face cost, versus the required **21.8354%**.

For the theoretical best H151 8-Spot state, the face space is enormous, so $5 is even less relevant. For Pick 3, $5 is only 0.0243% of the $20,540 face cost.

The burger purchase requirement makes the real all-in economics strictly worse unless the meal has independent consumption value that would have been purchased anyway. The promotion therefore cannot be counted as a standalone deterministic arbitrage subsidy.

## Execution architecture note
The current Big Red Keno App FAQ remains useful for future overlay execution:
- account balance can be transferred out through Play+;
- tickets can be voided before the game starts;
- voided-ticket funds return to account balance;
- saved tickets can be prepared/replayed;
- actual wagering is geofenced to licensed Keno locations.

This architecture is materially better than irreversible-deposit lottery systems, but it does not create an edge by itself. A qualifying subsidy/paytable still must exceed the exact H149 deficit.

## Result
- **Omaha Quarter Mania exact cross-city screen: CLOSED below H151 benchmark.**
- **Lincoln Quarter Mania exact cross-city screen: CLOSED below H151 benchmark.**
- **Current La Vista $5 free-play: CLOSED as H151 break-even subsidy; short by $167.50 even under favorable valuation.**
- **La Vista Quarter Madness remains the best standard fixed-paytable Keno deterministic cover found: 81.0636%.**
- **Terminal SUCCESS: NO.**

## Next action
1. Recover other Nebraska/community 25-cent or special-rate paybooks, prioritizing current numeric tables and run them through H149.
2. Search for deterministic player-owned Keno subsidies at least **$172.51 per $790 Pick-2 cover** (or equivalent >21.8354% discount) that are fixed before purchase.
3. Search for a higher-paytable compact Pick-1/Pick-2 structure where the absolute full-cover deficit is small enough for $5-$25 promotions to matter.
4. If any table crosses 100% after subsidy, immediately test app ticket-count limits, payout caps, tax, promotional-play restrictions and atomic/rollback execution.
