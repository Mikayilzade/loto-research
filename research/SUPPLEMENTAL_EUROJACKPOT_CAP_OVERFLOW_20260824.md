# Supplemental — EuroJackpot €120m-cap overflow to prize class 2 (2026-08-24)

This check is intentionally unnumbered because the global numbered lottery stream is advancing independently.

## Current official mechanics
Primary current source: LOTTO.de EuroJackpot Spielregeln:
https://www.lotto.de/eurojackpot/spielregeln

LOTTO.de currently states:
- game formula: **5 of 50 + 2 of 12**;
- stake: **€2 per field plus the respective state-lottery processing fee per play slip**;
- jackpot range: €10m to a maximum €120m;
- there is no ordinary forced jackpot payout; instead the jackpot is capped;
- if the class-1 allocation exceeds €120m, the excess is **added to prize class 2**;
- class 2 itself is capped at €120m, with further excess flowing to the next lower prize class containing winners.

Current prize-probability page:
https://www.lotto.de/eurojackpot/gewinnwahrscheinlichkeit

It identifies class 2 as **5 main numbers + 1 Euro number**, with an 8.60% standard allocation share and odds 1:6,991,908.

A current LOTTO.de review of 2024 explicitly confirms that when the €120m jackpot stayed at cap, accumulated **Überläufe** moved into the second prize tier and created unusually many million-euro class-2 winners:
https://www.lotto.de/ueber/neuigkeiten/eurojackpot/2025/pressemeldung-eurojackpot-20250106

## Exact deterministic cover of class 2
The combinatorics are the same `K12` total-edge-domination problem as the separately logged EuroMillions cap-flowdown check.

For each exact five-main-number set, a purchased Euro-number pair must share exactly one of the two winning Euro numbers in order to guarantee a class-2 (5+1) line. Eight selected pairs are necessary and sufficient:

`(0,1),(1,2), (3,4),(4,5), (6,7),(7,8), (9,10),(10,11)`.

Lower bound: selected-edge endpoints must cover at least 11 of 12 vertices, and no selected edge may be an isolated one-edge component because that selected edge itself needs an adjacent selected edge. With `m` selected edges in components of at least two edges, at most `m+floor(m/2)` vertices can be covered; `m=7` reaches at most 10, so `m>=8`. Four disjoint 2-edge paths attain 8.

Therefore:
- exact five-main-number sets: `C(50,5)=2,118,760`;
- minimum deterministic class-2 cover: **16,950,080 lines**;
- bare field stake at €2: **€33,900,160**, before mandatory per-slip processing fees;
- full line space remains 139,838,160.

## Strict-guarantee blocker
This is a genuine nonlinear lower-tier overflow mechanism and, unlike zero-winner rolldowns, owning a covering portfolio does not disable the trigger.

It still does **not** yield a guaranteed-profit construction:
1. The official rules expose no contractual positive **minimum overflow amount** large enough to cover acquisition cost; overflow can be much smaller than the required tens of millions.
2. Prize class 2 is a shared prize category. External 5+1 winning tickets dilute the amount captured by our class-2 line(s), and no hard pre-draw upper bound on external winning multiplicity is available.
3. The €33.90016m figure is only a lower bound on purchase cost because state processing fees are extra.
4. Our portfolio can itself contain a jackpot-winning line for some Euro-number outcomes, but class-1 winnings are also shareable with external jackpot winners; that does not create a strict lower bound sufficient to repair points 1–3.

## Result
**NO SUCCESS.** EuroJackpot cap overflow is now explicitly checked and should not be revisited without materially new evidence: a contractual minimum overflow large enough to cross the exact acquisition hurdle and a hard bound on external class-1/class-2 sharing (or fixed non-pari-mutuel lower-tier payouts).
