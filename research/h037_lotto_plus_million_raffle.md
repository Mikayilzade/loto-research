# H037 — Irish Lotto Plus Million Euro Raffle

Updated: 2026-08-16
Status: **event-day data now supports a live positive-EV overlay; strict guaranteed-profit path rejected**

## Why this branch matters
The Irish National Lottery periodically runs a special Lotto Plus Million Euro Raffle. For every Lotto Plus line purchased, the player receives a four-digit raffle number. Tickets with the winning raffle number receive the ordinary €500 raffle prize; in the special event all such tickets enter a once-off random draw and one ticket owner receives an additional €1,000,000.

Official current / historical sources:
- Lotto Plus rules/info: https://www.lottery.ie/game-information/lotto-plus
- Million Euro Raffle terms: https://www.lottery.ie/game-information/lotto-plus/million-euro-raffle
- 2024 mechanics confirmation: https://www.lottery.ie/news/press-releases/4-millionaires-to-be-made-in-september-with-4-special-draws
- 5 July 2025 event result: https://www.lottery.ie/news/winners-stories/tipp-top-win-clerihan-lotto-player-becomes-14th-national-lottery-millionaire-of-2025
- 6 September 2025 event result: https://www.lottery.ie/news/winners-stories/treaty-county-triumph-limerick-lotto-player-becomes-irelands-18th-millionaire-of-2025
- 30 May 2026 event result: https://www.lottery.ie/news/winners-stories/bank-holiday-joy-lotto-player-in-louth-becomes-14th-national-lottery-millionaire-of-2026
- current pricing announcement confirms two Lotto lines cost €4 and two lines with Lotto Plus cost €6, so the Plus add-on is €1 per line.

## 1. Strict guarantee test — CLOSED
A terminal guarantee fails for two independent reasons.

### Random raffle-number assignment
Players do not choose the four-digit raffle number. Buying a finite number of lines cannot force deterministic coverage of all 10,000 raffle codes because duplicate assigned codes can occur.

### External qualifying tickets
The €1m is not automatically paid to every holder of the winning raffle number. All tickets with that number enter a second random draw and one ticket owner is selected.

Therefore any external qualifying ticket preserves a legal outcome where another player receives the €1m. No useful hard pre-draw cap or exclusion mechanism is published.

Conclusion: **H037 is REJECTED as a strict guaranteed-profit strategy.**

## 2. Incremental Plus EV baseline
Current pre-autumn-2026 6/47 fixed prize tables imply approximately:
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

## 3. NEW — actual event-day calibration
The earlier packet used the operator's generic statement that ordinary Lotto Plus Raffle draws typically produce 60–120 winners. We now have exact counts from two special €1m events:

### 5 July 2025 special event
Official winner story states **104 ticketholders** held the winning raffle number.

With raffle hit probability `p≈1/10,000`, the maximum-likelihood participation proxy is:

`T_hat = 104 / p ≈ 1,040,000 Plus lines`.

Under a Poisson approximation to raffle-winner count, exact 95% confidence limits for the mean winner count are about **84.98 to 126.01**, corresponding to about **0.850m–1.260m Plus lines**.

Even at the 95% upper participation bound, modeled incremental Plus payout is:

`0.4116646 + 1,000,000 / 1,260,134 ≈ €1.2052 per €1 add-on`.

### 6 September 2025 special event
Official winner story states **81 ticketholders** held the winning raffle number.

MLE participation proxy:

`T_hat ≈ 810,000 Plus lines`.

95% Poisson interval for the implied Plus-line count is about **0.643m–1.007m**.

At the 95% upper participation bound, modeled incremental Plus payout is still about:

`€1.4050 per €1 add-on`.

### Result
Both directly observed special-event winner counts are materially below the approximately **170 raffle winners** corresponding to Plus break-even.

This is stronger than the previous heuristic because it uses special-event outcomes themselves rather than ordinary-draw marketing language. On these two observed event days, the participation proxy is consistent with the €1 Plus add-on being substantially positive EV.

Data:
- `data/derived/h037_event_calibration.csv`

## 4. Line-level versus ticket-level mechanics — clarified
Official 2024 promotion language explicitly states: **for every Lotto Plus line purchased, players get a four-digit Raffle number.** This confirms that raffle exposure is generated at the line level.

The special €1m selection, however, is described as selecting one **ticket** among tickets with the winning raffle number. Therefore multi-line tickets can create multiple qualifying line codes but the final selection unit is described as a ticket owner/ticket. Without the full rules implementation details, one should not assume that placing many qualifying lines on one physical/interactive ticket is exactly equivalent to spreading those lines across separate tickets for the second-stage million draw.

For the aggregate subsidy calculation this distinction does not alter the fact that exactly €1m is distributed across the eligible population, but it can matter for an individual execution strategy and must be resolved before real-money sizing.

## 5. Interpretation
### Strong positive-EV lead
H037 now has actual event-day evidence supporting `T < 1.70m` in at least two special draws. This makes it one of the strongest currently documented live +EV lottery overlays in the project.

### Still not terminal SUCCESS
Positive EV is not the project's terminal criterion. A particular Plus line can still lose everything, and the €1m recipient is selected randomly. Therefore no guaranteed positive net profit exists from this mechanism alone.

### Remaining real-money caveats
- only two event-day exact winner counts have been recovered so far;
- special-event participation could vary materially across dates;
- autumn-2026 Lotto/Lotto Plus rule changes may alter prize probabilities/prices, so the pre-change EV model must not be blindly carried forward;
- ticket-level handling of the second-stage draw should be confirmed from the operative rules;
- account/spend limits, residency/location requirements and execution constraints apply;
- tax/prize-limit treatment must be checked for any deployable strategy.

## 6. Next high-value test
1. Recover exact raffle-winner counts for additional special dates: 21 Dec 2024, 28 Sep 2024, 20 Dec 2025, 14 Mar 2026, 30 May 2026 and other events.
2. Compare event-day winner counts with adjacent ordinary Wednesday/Saturday draws to estimate promotion-induced participation uplift.
3. Build a Bayesian / predictive distribution for `T` and probability that incremental Plus EV exceeds €1 before ticket cutoff.
4. Recompute under the announced autumn-2026 Lotto regime once exact new Lotto Plus tables/rules are effective.

## Files
- `src/loto_research/lotto_plus_raffle.py`
- `tests/test_lotto_plus_raffle.py`
- `data/derived/h037_lotto_plus_million_raffle_screen.csv`
- `data/derived/h037_event_calibration.csv`

## Current conclusion
**No terminal SUCCESS.** Strict guarantee remains impossible under published mechanics. However two actual special-event counts — 104 winners on 5 July 2025 and 81 on 6 September 2025 — place event-day participation well below the modeled ~170-winner break-even threshold, materially strengthening H037 as a live positive-EV overlay.
