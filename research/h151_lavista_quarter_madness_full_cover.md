# H151 — La Vista Quarter Madness deterministic full-cover screen

Updated: 2026-08-21
Status: **NEW BEST FIXED-PAYTABLE KENO COVER FOUND / NO SUCCESS**

## Current official source
La Vista Keno currently advertises `QUARTER MADNESS` as available **all day every day**, with a $1 minimum ticket and **$0.25 minimum bet per way**. The current page exposes complete fixed paytables for 2- through 15-Spot play and states that Quarter Madness does not qualify for the progressive.

Official current page:
- https://www.lavistakeno.com/quarter-madness

Official paytable images were read directly from that page:
- q1: 2-6 Spot
- q2: 7-9 Spot
- q3: 10-13 Spot
- q4: 14-15 Spot

## Exact theorem
For standard 20-of-80 keno, buying every k-subset gives a deterministic number of tickets with exactly j hits:

`N(k,j)=C(20,j) C(60,k-j)`.

With per-way cost `c=0.25` and fixed payout `P_j`, full-cover ratio is

`R_k = sum_j N(k,j) P_j / (C(80,k) c)`.

This is outcome-independent because every possible 20-ball draw induces the same intersection-count profile over the complete k-subset universe.

## Results
Exact current Quarter Madness full-cover ratios:

- 2-Spot: **78.1646%**
- 3-Spot: **80.4771%**
- 4-Spot: **80.9456%**
- 5-Spot: **78.6903%**
- 6-Spot: **78.4873%**
- 7-Spot: **80.0471%**
- 8-Spot: **81.0636%**  ← best
- 9-Spot: **80.7279%**
- 10-Spot: **80.8705%**
- 11-Spot: **80.8032%**
- 12-Spot: **80.9141%**
- 13-Spot: **80.9388%**
- 14-Spot: **80.7551%**
- 15-Spot: **80.6413%**

The best state is therefore 8-Spot at **81.063553% deterministic gross return**, materially above the previous project benchmark of Virginia 1-Spot at 75%.

Required deterministic subsidy to cross break-even on the best Quarter Madness state is only:

`1 - 0.81063553 = 18.936447%`.

The more executable lower-cardinality candidates are:
- 2-Spot: 3,160 ways, cost $790, gross $617.50, subsidy hurdle **21.8354%**;
- 3-Spot: 82,160 ways, cost $20,540, gross $16,530, hurdle **19.5229%**;
- 4-Spot: 1,581,580 ways, cost $395,395, gross $320,055, hurdle **19.0544%**.

Thus La Vista reduces the subsidy threshold from Virginia's 25% to about **18.94%-21.84%** depending on execution scale.

## Secondary test: Penny Keno
La Vista also currently offers Penny Keno: 20 Four Spots + 190 Eight Spots on one $2.10 ticket. Official page:
- https://www.lavistakeno.com/penny-keno

Its paytable pays on a 4-Spot only when all four selected numbers hit, and on an 8-Spot at 7 or 8 hits. A legal 20-ball draw can select exactly one number from each of the twenty four-number groups. In that outcome:
- no four-number group has 4 hits;
- every union of two groups has only 2 hits;
- payout = **$0**.

Therefore Penny Keno has a strict zero floor and is rejected as a standalone guaranteed-profit structure despite its unusually dense way-ticket packaging.

## Why H151 is not SUCCESS
Quarter Madness is still below 100% with no external subsidy included. Full-cover 8-Spot is also astronomically large (`C(80,8)=28,987,537,150` ways), so execution is not practical. The useful discovery is the lower **break-even subsidy threshold**, especially the $790 2-Spot and $20,540 3-Spot covers.

No current deterministic, pre-owned La Vista coupon/discount >= the corresponding hurdle has yet been established. Food-linked free-play promotions are not counted unless the underlying purchase has independent value or the all-in incremental cost leaves a strict positive cash floor.

## Result
- **Quarter Madness fixed-paytable theorem: VALIDATED.**
- **New project-best standard deterministic Keno ratio: 81.0636%.**
- **Subsidy hurdle falls to 18.9364% best-case; 21.8354% on the compact $790 2-Spot cover.**
- **Penny Keno standalone guarantee: REJECTED by explicit zero-payout draw construction.**
- **Terminal SUCCESS: NO.**

## Next action
1. Search La Vista and Nebraska promotions for genuinely player-owned deterministic free play/discount >=21.8354% on a $790 2-Spot cover, or >=19.5229% on a $20,540 3-Spot cover.
2. Search other current quarter/penny/special-rate Keno paytables using the H149 formula; prioritize any fixed non-shareable table above 81.0636%.
3. If a subsidy crosses the hurdle, immediately verify ticket-count limits, batch entry, void/rollback, payout caps, taxes and whether promotional play can fund all required ways.