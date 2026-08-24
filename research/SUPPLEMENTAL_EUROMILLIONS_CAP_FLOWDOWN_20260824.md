# Supplemental — EuroMillions cap-overflow lower-tier deterministic cover (2026-08-24)

This check is intentionally **unnumbered** because the global numbered lottery stream independently owns H255+.

Primary rules source: Irish National Lottery, EuroMillions Rules, Issue 5 (October 2024):
https://cdn1.lottery.ie/uploads/Issue_5_EUROMILLIONS_RULES_OCT_2024_29_10_2a527d4c18.pdf

Current game page:
https://www.lottery.ie/game-information/euromillions

## Mechanism
Rule 7.5(b)(ii)(A) sends Jackpot Pool money **above the Flow-down Cap** to the next lower prize tier with at least one winner for that draw. Unlike a fifth-cap-draw jackpot rolldown, this excess can flow down even when the jackpot tier itself has a winner.

Irish play is 5/50 main numbers + 2/12 Lucky Stars and costs €2.50 per line; §6.1 splits this into €2.20 EuroMillions + €0.30 mandatory Ireland Only Raffle, and the two cannot be played individually. Prize categories are pari-mutuel under §7.4(d).

## Exact minimum cover of Match 5+1
For each fixed exact five-main-number set, represent the 12 Lucky Stars as vertices of K12. A purchased Lucky-Star pair f yields Match 5+1 against winning pair e exactly when |e∩f|=1. We therefore need a total edge-dominating set of K12.

Lower bound: endpoints of selected edges must cover at least 11 vertices, otherwise an edge between two uncovered vertices is undominated. Also no selected edge may form a one-edge component, because it must itself have an adjacent selected edge. With m edges and components of at least two edges, at most m+floor(m/2) vertices can be covered. For m=7 this is 10, so m>=8.

Construction attaining 8: four disjoint two-edge paths
`(0,1),(1,2), (3,4),(4,5), (6,7),(7,8), (9,10),(10,11)`.
Every one of the 66 possible winning Lucky-Star pairs has a selected adjacent edge, so 8 is exact.

`C(50,5)=2,118,760`; therefore the minimum deterministic guarantee of at least one Match 5+1 play for every draw requires **16,950,080 lines**. At the mandatory Irish €2.50 price this costs **€42,375,200**. The full line space is 139,838,160.

## Strict-guarantee blocker
This mechanism is structurally interesting but still does not yield guaranteed profit:

- the rules specify the amount *above* the cap but no positive fixed minimum amount of excess;
- Match 5+1 is pari-mutuel, and the current Irish game page explicitly states its prize varies with prize-pool size and number of winners;
- without a hard pre-draw bound on external duplicate Match5+1 winning plays, our captured share has no positive execution-grade lower bound;
- the rules also allow restriction/prohibition of play deemed to interfere with other players' reasonable access, adding a practical execution blocker at 16.95m lines.

Result: **NO SUCCESS**. Reopen only with both a contractual minimum cap-excess amount and a hard bound on external sharing (or a fixed lower-tier payout).

Artifacts:
- `src/loto_research/supplemental_euromillions_cap_flowdown_cover.py`
- `data/derived/supplemental_euromillions_cap_flowdown_cover.json`
