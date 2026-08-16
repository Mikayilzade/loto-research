# H037 — Irish Lotto Plus Million Euro Raffle

Updated: 2026-08-16
Status: **six-event data strongly supports a live positive-EV overlay; strict guaranteed-profit path rejected**

## Why this branch matters
The Irish National Lottery periodically runs a special Lotto Plus Million Euro Raffle. For every Lotto Plus line purchased, the player receives a four-digit raffle number. Tickets with the winning raffle number receive the ordinary €500 raffle prize; in the special event all such tickets enter a once-off random draw and one ticket owner receives an additional €1,000,000.

Primary mechanics / event sources:
- https://www.lottery.ie/game-information/lotto-plus
- https://www.lottery.ie/game-information/lotto-plus/million-euro-raffle
- https://www.lottery.ie/news/press-releases/4-millionaires-to-be-made-in-september-with-4-special-draws
- https://www.lottery.ie/news/winners-stories/tipp-top-win-clerihan-lotto-player-becomes-14th-national-lottery-millionaire-of-2025
- https://www.lottery.ie/news/winners-stories/treaty-county-triumph-limerick-lotto-player-becomes-irelands-18th-millionaire-of-2025
- https://www.lottery.ie/news/winners-stories/an-early-christmas-surprise-for-lotto-player-in-dublin-7-who-just-became-irelands-newest-millionaire
- https://www.lottery.ie/news/winners-stories/lotto-player-in-cork-becomes-4th-national-lottery-millionaire-of-2026
- https://www.lottery.ie/news/winners-stories/bank-holiday-joy-lotto-player-in-louth-becomes-14th-national-lottery-millionaire-of-2026

Historical draw-count source used where the operator winner story confirms the event/code but does not print the underlying number of €500 raffle winners:
- https://irish.national-lottery.com/irish-lotto/

## 1. Strict guarantee test — CLOSED
A terminal guarantee fails for two independent reasons.

### Random raffle-number assignment
Players do not choose the four-digit raffle number. Buying a finite number of lines cannot force deterministic coverage of all 10,000 raffle codes because duplicate assigned codes can occur.

### External qualifying tickets
The €1m is not automatically paid to every holder of the winning raffle number. All tickets with that number enter a second random draw and one ticket owner is selected.

Therefore any external qualifying ticket preserves a legal outcome where another player receives the €1m. No useful hard pre-draw cap or exclusion mechanism is published.

Conclusion: **H037 is REJECTED as a strict guaranteed-profit strategy.**

## 2. Incremental Plus EV baseline
Pre-autumn-2026 6/47 fixed prize tables imply approximately:
- Plus 1 fixed-prize EV: **€0.22902755 per line**;
- Plus 2 fixed-prize EV: **€0.13263705**;
- ordinary €500 raffle EV at 1/10,000: **€0.05**;
- combined ordinary Plus package EV: **€0.41166460 per €1 add-on**.

Let `T` be total eligible Plus raffle entries in the special event. Under entry symmetry, the extra million contributes:

`€1,000,000 / T`

per eligible Plus line in expectation.

Incremental Plus expected payout:

`0.4116645959 + 1,000,000/T`.

Break-even:

`T ≈ 1,699,710.73 eligible Plus lines`.

Equivalent expected ordinary-raffle winner count:

`T / 10,000 ≈ 169.97`.

## 3. Six directly calibrated special events
`data/derived/h037_event_calibration.csv` now contains six special events with recoverable raffle-winner counts:

| Event | Raffle winners | Implied Plus lines (MLE) | 95% upper implied lines | Plus EV at upper line bound |
|---|---:|---:|---:|---:|
| 28 Sep 2024 | 73 | 0.730m | 0.918m | **€1.501** |
| 5 Jul 2025 | 104 | 1.040m | 1.260m | **€1.205** |
| 6 Sep 2025 | 81 | 0.810m | 1.007m | **€1.405** |
| 20 Dec 2025 | 82 | 0.820m | 1.018m | **€1.394** |
| 14 Mar 2026 | 84 | 0.840m | 1.040m | **€1.373** |
| 30 May 2026 | 72 | 0.720m | 0.907m | **€1.515** |

Important source distinction:
- 2025-07-05 and 2025-09-06 counts are explicitly stated in official National Lottery winner stories;
- official pages confirm mechanics/date/winning code for the other events, while the archived result pages provide the underlying ordinary €500 raffle-winner count.

### Result
All six observed special-event counts are far below the approximately **170** ordinary raffle winners corresponding to incremental Plus break-even.

More strongly, for **each individual event**, the exact-Poisson 95% upper confidence limit for implied Plus entries remains below the 1.6997m break-even line count. Thus the positive-EV conclusion is no longer driven by one or two unusually quiet event days.

## 4. Promotion-demand uplift from matched adjacent draws
For each special Saturday event, compare raffle-winner count with the ordinary Wednesday draw immediately before and after it. Because the raffle code hit probability is fixed at 1/10,000 per Plus line, winner counts provide a direct noisy proxy for Plus participation.

Matched windows:
- 28 Sep 2024: event **73** vs adjacent **55 / 51** -> **1.377x**;
- 5 Jul 2025: **104** vs **69 / 76** -> **1.434x**;
- 6 Sep 2025: **81** vs **56 / 54** -> **1.473x**;
- 20 Dec 2025: **82** vs **62 / 81** -> **1.147x**;
- 14 Mar 2026: **84** vs **59 / 62** -> **1.388x**;
- 30 May 2026: **72** vs **48 / 52** -> **1.440x**.

Mean matched promotion uplift = **1.3766x**, or about **+37.7%** versus the local adjacent-draw average. Median uplift is about **1.4115x**.

Interpretation:
- promotion advertising does measurably raise Plus participation;
- the uplift is large enough that ordinary-draw demand cannot simply be copied into a special-event model;
- however observed promotion-day demand is still nowhere near the ~170-winner break-even threshold.

This matched comparison is observational, not causal proof: jackpot size, holidays, weekday effects and other promotions may also affect demand.

## 5. Bayesian predictive screen
Implemented in `src/loto_research/lotto_plus_raffle.py` using a transparent Gamma-Poisson model over the six observed special-event winner counts.

Counts:

`73, 104, 81, 82, 84, 72`

With a Jeffreys-style Gamma(0.5, 0) prior for a common special-event Poisson mean:
- posterior shape = **496.5**;
- posterior rate = **6**;
- posterior mean special-event raffle winners = **82.75**;
- 95% posterior interval for the common mean ≈ **75.63–90.19** winners;
- corresponding mean implied Plus participation ≈ **827,500 lines**.

Under this deliberately simple common-rate model, posterior predictive probability that the next event reaches/exceeds **170 raffle winners** is about:

`1.7e-14`.

### Critical caveat
That tiny probability is **model-conditional, not a real-world guarantee**. Six events cannot rule out regime shifts, marketing changes, jackpot effects, pricing changes or overdispersion. It should be read as: *the observed historical event regime is very far from the current break-even demand level*, not as a promise that a future event cannot cross it.

## 6. Line-level versus ticket-level mechanics
Official promotion language states that **for every Lotto Plus line purchased, players get a four-digit Raffle number**. This confirms raffle exposure is generated at line level.

The special €1m selection is described in ticket/ticket-owner terms. Therefore multi-line ticket handling can matter for an execution strategy and should be confirmed from operative rules before real-money sizing.

For aggregate subsidy EV, exactly €1m is still distributed across the eligible special-event population, so this distinction does not alter the total-subsidy calculation.

## 7. Strategic interpretation
### Strongest live +EV lottery overlay currently found
H037 now has six observed special-event participation proxies across 2024–2026, all comfortably below the modeled pre-change break-even level. Matched ordinary draws show the promotion itself raises participation by roughly 38% on average, but the resulting special-event counts remain materially below break-even.

### Still not terminal SUCCESS
The project requires **guaranteed positive net profit across all legal outcomes**, not merely positive expected value. A Plus line can lose and the €1m recipient is selected randomly. Therefore H037 remains non-terminal.

### Real-money caveats
- sample is only six special events;
- one event count source can be secondary even where official pages confirm the event and code;
- autumn-2026 Lotto/Lotto Plus rule changes can alter price/probabilities and invalidate this pre-change break-even;
- ticket-level second-stage handling requires operative-rule confirmation;
- account/spend limits, residency/location and execution constraints apply;
- any deployable strategy requires current tax/rule verification.

## 8. Next high-value tests
1. Recover the missing underlying €500 raffle-winner count for the 21 Dec 2024 special event from an authoritative or independently consistent archive.
2. Expand matched ordinary-draw controls beyond ±1 Wednesday to estimate weekday/jackpot/seasonality effects.
3. Fit an overdispersed / hierarchical event-demand model rather than relying only on common-rate Poisson.
4. Recompute immediately when the autumn-2026 Lotto/Lotto Plus regime becomes operative.
5. Continue the broader search for **deterministic** subsidy/rebate mechanisms because H037 cannot meet the project's guarantee terminal condition.

## Files
- `src/loto_research/lotto_plus_raffle.py`
- `tests/test_lotto_plus_raffle.py`
- `data/derived/h037_lotto_plus_million_raffle_screen.csv`
- `data/derived/h037_event_calibration.csv`

## Current conclusion
**No terminal SUCCESS.** Strict guarantee remains impossible under published mechanics. But six special-event counts and matched adjacent-draw controls now make H037 a much stronger positive-EV finding: observed event participation is consistently and materially below the pre-change break-even threshold even after promotion-induced demand uplift.
