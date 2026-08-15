# H018 — Virginia Lucky Contestant hidden daily time-state

Updated: 2026-08-15
Status: **standalone guaranteed-profit path REJECTED; late-survival EV lead remains OPEN but requires unpublished mechanics / live execution data**

## Why this branch matters
Lucky Contestant is not a hot-number or historical-pattern hypothesis. Virginia Lottery publicly defines a causal, nonstationary jackpot probability process tied to a hidden selected time `T` each day. That makes time/state inference scientifically legitimate.

Primary current official source:
- https://www.valottery.com/lotteryonline/3850

Current Virginia lottery-game regulatory framework:
- https://law.lis.virginia.gov/admincode/title11/agency5/chapter41/

## Official facts recovered
The Virginia Lottery page states:
- plays cost **$0.20, $0.50, $1, $2, $5, $10, $20 or $30**;
- overall odds per game are **1 in 3.83** under the page's stated baseline convention;
- a Daily Jackpot is guaranteed to be won daily;
- each day a hidden time is randomly selected from a published weighted time prior;
- the jackpot can also be won **earlier at standard odds regardless of the selected time**;
- jackpot odds improve approaching selected time:
  - 60 minutes before `T`: **1 in 150,000**;
  - 30 minutes before `T`: **1 in 30,000**;
  - at `T`: **1 in 1**.

Published selected-time prior:

| interval | mass |
|---|---:|
| 01:00–02:00 | 10% |
| 02:00–08:00 | 10% |
| 08:00–14:00 | 10% |
| 14:00–18:00 | 10% |
| 18:00–20:00 | 15% |
| 20:00–21:00 | 15% |
| 21:00–22:00 | 15% |
| 22:00–23:45 | 15% |

The page does **not** publish in text:
- the exact probability interpolation between the 60m, 30m and T anchors;
- the time resolution of `T` / transaction matching;
- a standard-jackpot probability value;
- a complete causal rule for what happens after an early jackpot win;
- player-arrival intensity;
- a stake-to-jackpot-probability scaling rule beyond the listed allowed prices.

Those missing mechanics prevent a certified executable EV strategy.

## Public winner-list observation
The official page exposed historical jackpot winner amount/time rows in the rendered HTML during research. A deduplicated Jan 4–10, 2026 sample included:
- Jan 10 13:00 — $704
- Jan 9 21:51 — $1,293
- Jan 8 20:05 — $1,107
- Jan 7 20:20 — $1,868
- Jan 6 14:32 — $1,774
- Jan 5 06:10 — $3,383
- Jan 4 20:01 — $1,841
- Jan 4 17:59 — $15,525

The HTML rendered each listed event twice, so duplicate rows were removed. Importantly, Jan 4 contains two distinct amount/time events. This means we must **not assume one and only one jackpot award per calendar day** or a simple terminal state after the first win without additional operator documentation.

## 1. Prior / optimistic survival model
Code:
- `src/loto_research/lucky_contestant_time_state.py`
- `tests/test_lucky_contestant_time_state.py`

Derived screen:
- `data/derived/h018_optimistic_time_state_screen.csv`

Because the operator publishes only interval weights, the first model assumes a **uniform density inside each published interval**. This is explicitly a modeling assumption, not an official rule.

We then calculate an intentionally optimistic information bound:

`P(T in next Δ | T >= now)`.

This is stronger than what the public live-jackpot observation necessarily tells us, because the public rules explicitly allow earlier standard-odds wins and do not fully publish reset mechanics.

Illustrative concentration under that optimistic truncation:
- at 20:00: `P(T in next 30m | T>=20:00) ≈ 16.67%`;
- at 21:00: ≈ 25%;
- at 22:00: ≈ 28.57%;
- at 22:30: ≈ 40%;
- at 23:00: ≈ 66.67%; next 60m = 100%;
- at 23:15: all remaining prior mass is inside the next 30 minutes.

So **survival late in the day can, in principle, create very strong hidden-state concentration**. This keeps H018 scientifically interesting for EV research.

## 2. Jackpot-only break-even screen
For stake `c`, jackpot `J` and jackpot-hit probability `p`, ignoring every non-jackpot prize gives the conservative component:

`EV_jackpot = p * J - c`.

Necessary jackpot-only break-even:

`p >= c/J`.

For a representative `$600` jackpot:
- `$0.20` play requires `p >= 1/3000` from jackpot alone;
- `$1` requires `p >= 1/600`;
- `$30` requires `p >= 1/20`.

At the published 30-minute anchor (`1/30,000`), a $600 jackpot contributes only about **$0.02 expected jackpot value per play**. At the published selected time (`1/1`) it would dominate any listed stake, but `T` is hidden and the exact odds path/time-resolution is unpublished.

The minimum stake would be the natural EV probe **if** jackpot eligibility/probability is stake-invariant. That invariance is not yet established by the public text, so it is not promoted to a strategy claim.

## 3. Strict guaranteed-profit theorem — REJECTED
The terminal project criterion is stronger than positive EV: every legal outcome branch must produce positive net profit.

The official game description itself supplies a fatal branch for a strategy that relies solely on waiting near hidden `T`:
1. ticket cost is positive;
2. `T` is hidden;
3. the jackpot may be won by another player **before T at standard odds**;
4. ordinary game play has losing outcomes (overall win odds are 1 in 3.83, so not every play wins a prize);
5. therefore there exists a legal branch in which the target jackpot is unavailable to us and our paid play loses.

Hence the hidden-time mechanism **alone cannot guarantee positive profit across all outcomes**.

This conclusion does not depend on the exact interpolation to 1-in-1, target-time prior calibration, Bayesian model quality, or our ability to submit a play close to T.

A second obstacle is execution: even if an observer knew that T lies inside a very narrow remaining interval, a finite predetermined set of transaction times is not guaranteed to coincide with a hidden instant unless the operator specifies a discrete resolution / crossing rule that guarantees capture. No such public rule was recovered.

### H018 terminal-guarantee status
**REJECTED as standalone guaranteed-profit strategy.**

## 4. What remains valuable
H018 remains an **EV/state-estimation overlay**, not a terminal guarantee.

A real +EV test would need at least:
1. exact odds function between 60m, 30m and T;
2. T resolution and transaction timestamp semantics;
3. whether a jackpot win resets/restarts the same day's process, supported by authoritative rule text;
4. standard odds outside the ramp;
5. stake scaling of jackpot probability and prize eligibility;
6. live jackpot-state endpoint / latency characterization;
7. player-arrival intensity by time;
8. enough historical winner timestamps to estimate survival/hazard out of sample.

If those become available, fit a competing-risks model:
- latent selected-time process `T`;
- player-play arrival intensity `λ(t)`;
- standard early-win hazard;
- ramp-dependent jackpot hazard conditional on `T`;
- observable live jackpot state.

The correct output is then posterior jackpot probability / EV by time, with latency and execution costs — not a claim that the last minutes are automatically profitable.

## Strategic conclusion
H018 produced a useful new class: **operator-defined hidden time states can create genuine nonstationary lottery odds and potentially exploitable conditional EV**.

But for the project's strict terminal target it is closed: the explicitly allowed early-win-by-others branch plus ordinary losing outcomes prevents an all-outcome profit guarantee.

Next priority returns to the remaining open classes, led by H006/H007 randomness/implementation testing with reliable histories and strict forward controls, while H018 stays parked as an EV lead pending better operator mechanics/data.
