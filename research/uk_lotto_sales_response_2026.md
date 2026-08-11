# UK Lotto 2026 — sales response and Must Be Won screening

Updated: 2026-08-11
Status: **screening model retained; Wednesday calendar edge materially weakened by historical demand stress test**

## Current-rule context
Primary Allwyn sources confirm that from 10 June 2026:
- one £2 line enters two independent 6/59 rounds;
- jackpot starts at £2m;
- it can roll up to five times before a sixth-draw Must Be Won state;
- draws remain Wednesday and Saturday;
- jackpot is shared across the two rounds.

Primary current-format sources:
- https://www.allwyn.co.uk/insights/double-your-luck-new-lotto-gives-players-two-chances-to-win-more-than-double-the-number-of-millionaires-expected-to-be-made
- https://www.allwyn.co.uk/insights/double-your-luck-delivers-new-lotto-creates-three-millionaires-in-first-weekend-and-over-3-1-million-winners-in-opening-draws

The indexed official National Lottery procedures are still the old pre-June-2026 edition. They state that 9.79% of Lotto sales is allocated to the jackpot. A current independent Lotto Q&A also reports 9.79% after the redesign. Until updated primary 2026 procedures are captured, this project treats 9.79% as an explicit modelling assumption, not a confirmed current rule.

Old primary procedure:
https://www.national-lottery.co.uk/games/lotto/game-procedures

Current secondary cross-check:
https://www.national-lottery.com/lotto/questions-and-answers

## 2026 jackpot-growth sales proxy
Under the 9.79% assumption, a £2 ticket contributes approximately £0.1958 to the current-draw jackpot allocation. For an ordinary rollover transition without reset/top-up adjustment:

`N_proxy = (J_t - J_(t-1)) / 0.1958`

The first 15 usable current-regime rollover increments from 13 June through 8 August 2026 are stored in:

`data/historical/uk_lotto_sales_proxy_2026.csv`

This is an inferred demand proxy, not official sales data. Reserve-fund actions, jackpot estimation/rounding, promotions or a changed allocation fraction can distort it.

### Weekday pattern
Across those 15 increments:

Wednesday:
- n = 6
- mean ~5.008m implied tickets
- median ~5.084m
- range ~4.661m–5.233m

Saturday:
- n = 9
- mean ~8.785m
- median ~8.580m

Excluding the 4 July Millionaire Raffle draw:
- Saturday mean ~8.567m
- Saturday median ~8.483m

The day-of-week effect is therefore much larger than the small jackpot-size variation in this short sample. Promotion state also matters: 4 July's special ten-millionaire raffle produced the highest proxy in the sample (~10.53m) despite only a ~£4.06m jackpot.

## Match-2 counts are only a secondary proxy
The same purchased selections enter both rounds, yet some 2026 draws show very large Round-1/Round-2 differences in Match-2 winner counts. This demonstrates that player number selections are not uniform enough to treat Match-2 winners as a clean per-draw binomial sales meter.

This weakens Match-2 as a sales estimator but strengthens H015: crowd number-choice behaviour can materially affect category winner counts and therefore sharing.

## Aggregate Must Be Won screening equation
Using the observed regular current lower tiers (£1m / £1,000 / £50 / £10 / £1 per round), the non-jackpot fixed cash EV is approximately:

**F = £0.728983386863 per £2 ticket.**

If `f = 0.0979`, current sales contribute `£0.1958` per ticket to the jackpot. Let `P` be inherited carryover before current-draw sales and `N` be current sales.

Simple aggregate screen:

`gross EV ≈ F + P/N + 0.1958`

Break-even:

`P/N >= £1.075216613137`

or

`N <= P / 1.075216613137`.

This assumes the jackpot-derived fund is fully distributable in aggregate and ignores current reserve/capping details. It is a screening inequality, not a profit proof.

## Saturday sixth-draw evidence
### 18 July 2026
Prior jackpot: £7,663,813.
- screening break-even max sales: ~7.128m
- jackpot-growth proxy for current draw: ~9.682m
- realized no-jackpot rolldown schedule EV: ~£1.5337 per £2 ticket

Negative under both the pre-draw-style screen and realized post-draw schedule.

### 27 June 2026
Prior jackpot: £7,357,143.
- screening break-even max sales: ~6.842m
- current sales proxy: ~9.768m

The jackpot was won rather than rolled down, but Saturday demand again exceeds the screen.

### 8 August 2026
The cycle again reached its sixth draw, but two Match-6 tickets shared the £8,535,146 jackpot, so no rolldown occurred.

## H016 — Wednesday Must Be Won idea
Calendar logic allows a sixth draw to land on Wednesday if the jackpot cycle begins on Saturday.

Using only the ordinary June-August 2026 demand medians:
- typical Wednesday jackpot increment ~£0.996m
- typical non-raffle Saturday increment ~£1.661m
- rough inherited carryover before a hypothetical Wednesday sixth draw ~£7.313m
- screening break-even max sales ~6.801m
- ordinary Wednesday median proxy ~5.084m

If Must Be Won did not alter demand, the screen would show about £2.36 gross value per £2 ticket. Ordinary Wednesday sales could increase about **+33.77%** before this apparent advantage disappeared.

That initial result was deliberately subjected to a historical demand stress test rather than accepted as an edge.

## Historical Wednesday Must Be Won stress test
Full analysis:

`research/uk_lotto_wednesday_mbw_stress_test.md`

Dataset:

`data/historical/uk_lotto_wednesday_mbw_stress_old_regime.csv`

Seven natural old-regime Wednesday sixth-draw states from 2023–2026 were reconstructed. Because old primary rules explicitly used the 9.79% jackpot allocation, relative jackpot-growth increments provide a useful same-cycle demand proxy.

Relative to the previous ordinary Wednesday in the same cycle, jackpot-growth uplift was:
- mean **+40.97%**
- median **+42.85%**
- range **+33.12% to +46.18%**

The current H016 screen only tolerates about **+33.77%** uplift. Historical uplift exceeds that margin in **6 of 7** observations.

Applying the historical uplift distribution mechanically to the current ordinary-Wednesday median gives:
- mean-uplift projected sales ~7.168m -> screen ~£1.95 gross / £2 ticket
- median-uplift projected sales ~7.263m -> screen ~£1.93 gross / £2 ticket

An independent but noisier Match-2 comparison points in the same direction, with historical median uplift around +41.26%.

## Decision on H016
The calendar effect alone is **not robust**. H016 is downgraded from `promising` to **`inconclusive / materially weakened`**.

It is not formally rejected because:
- the 2026 two-round product differs from the old one-round regime;
- updated current jackpot-allocation and rolldown procedures are still missing;
- reserve/top-up effects can distort jackpot-growth proxies;
- no current-regime Wednesday Must Be Won observation exists yet.

However, the historical evidence now says that assuming ordinary Wednesday demand is too optimistic.

H016 becomes interesting again only if at least one additional edge appears, such as:
- unusually large inherited carryover;
- lower current-regime Must-Be-Won demand response than historical behaviour;
- more generous verified current redistribution mechanics;
- measurable H015 anti-popularity/sharing advantage;
- promotion/cashback/effective-price overlay.

## Priority shift
Do not spend more effort trying to prove H016 from the same small current dataset. Higher-value next work:
1. capture updated primary 2026 Lotto procedures;
2. quantify H015 crowd-choice/sharing effects;
3. return to Azerbaijan 4+4 lower-tier carryover reconstruction;
4. search other current games for structural overlays that are less efficiently competed away.
