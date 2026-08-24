# H255 — EuroMillions cap-overflow lower-tier deterministic cover

## Question
Can the EuroMillions **Flow-down Cap** mechanism avoid the usual full-cover paradox by sending money above the jackpot cap to a lower prize tier even when the jackpot itself has a winner?

## Rules evidence
Primary source: Irish National Lottery, *EuroMillions Rules*, Issue 5 (October 2024):
https://cdn1.lottery.ie/uploads/Issue_5_EUROMILLIONS_RULES_OCT_2024_29_10_2a527d4c18.pdf

Relevant rules:
- §6.1: an Irish play costs **€2.50** total: €2.20 EuroMillions + €0.30 Ireland Only Raffle; the two cannot be bought individually.
- §7.4(d): prizes are allocated within each EuroMillions prize category on a **pari-mutuel** basis.
- §7.5(b)(ii)(A): once the Flow-down Cap is reached, money in the Jackpot Pool **above the cap is not available to the jackpot tier and flows down to the next lower prize tier with at least one winner for that draw**. This clause is structurally different from a fifth-cap-draw jackpot roll-down because the excess can flow down even if the jackpot tier has a winner.

Current Irish game page confirms 5 numbers from 1–50, 2 Lucky Stars from 1–12, play from €2.50, and that Match 5+1 prize size depends on the prize pool and number of winners:
https://www.lottery.ie/game-information/euromillions

## Exact smallest cover of the first lower tier
The first tier below the jackpot is Match 5 + 1 Lucky Star.

For any fixed exact set of five main numbers, represent the 12 Lucky Stars as vertices of `K12`. A purchased Lucky-Star pair is an edge. For a winning Lucky-Star edge `e`, a purchased line is Match 5+1 exactly when its purchased edge `f` shares **exactly one** endpoint with `e`.

Therefore we need a set of edges such that every edge of `K12`, including selected edges themselves, has an adjacent selected edge: a total edge-dominating set.

### Lower bound: at least 8 selected star pairs
1. The endpoints of the selected edges must cover at least 11 of the 12 vertices. Otherwise two uncovered vertices form an edge that shares no endpoint with any selected edge.
2. A connected component consisting of one isolated selected edge is forbidden, because that selected edge itself would have no adjacent selected edge.
3. Hence every selected-edge component has at least 2 edges. With `m` selected edges, the maximum number of covered vertices is therefore `m + floor(m/2)` (achieved by disjoint 2-edge paths as much as possible).
4. For `m=7`, this is only `7+3=10 < 11`. So `m>=8`.

### Construction attaining 8
Four disjoint two-edge paths cover all 12 vertices:
`(0,1),(1,2), (3,4),(4,5), (6,7),(7,8), (9,10),(10,11)`.

Every possible winning Lucky-Star pair shares exactly one endpoint with at least one of these eight selected pairs. Thus **8 is exact and optimal**.

There are `C(50,5)=2,118,760` possible exact main-number sets. A deterministic guarantee of owning at least one Match 5+1 line for every possible draw therefore needs at least:

- lines: `2,118,760 × 8 = 16,950,080`;
- mandatory Irish purchase cost: `16,950,080 × €2.50 = €42,375,200`;
- EuroMillions core-game component alone would be €37,290,176, but it cannot be purchased separately from the raffle component.

The full EuroMillions line space remains `C(50,5)×C(12,2)=139,838,160`.

## Why this still does not create a strict profit guarantee
The mechanism is genuinely better than the zero-jackpot-winner rolldown class: our construction can guarantee that the first lower tier has one of our plays, while the above-cap excess is allowed to flow to that tier regardless of whether the jackpot is won.

However the strict cash floor is still not positive:

1. The rules define **the amount in excess of the cap** as the flow-down amount but do not give a positive fixed minimum size for that excess. A cap draw therefore does not expose a pre-draw deterministic subsidy amount large enough to compare with €42.3752m of acquisition cost.
2. Match 5+1 is pari-mutuel. External players can hold duplicate winning plays. Without an execution-grade hard upper bound on external winning tickets, our fraction of the lower-tier pool has no positive guaranteed lower bound.
3. The Irish rules also permit restriction/prohibition of participation when play is deemed to interfere with other players' reasonable access, which is an additional execution blocker for a 16.95m-line purchase.

## Result
**NO SUCCESS.** EuroMillions cap-excess flow-down is a materially new lower-tier subsidy mechanism and the minimum deterministic Match5+1 cover is exactly characterized, but the subsidy amount and captured pari-mutuel share are not bounded tightly enough for guaranteed profit.

Reopen only if a future capped draw/event provides both:
- a contractual **minimum excess amount**, and
- a hard pre-draw bound on external Match5+1 winning-ticket multiplicity (or a non-pari-mutuel fixed payout).

Artifacts:
- `src/loto_research/h255_euromillions_cap_flowdown_cover.py`
- `data/derived/h255_euromillions_cap_flowdown_cover.json`
