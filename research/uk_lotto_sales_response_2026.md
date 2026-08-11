# UK Lotto 2026 — jackpot-growth sales proxy and Wednesday Must Be Won lead

Updated: 2026-08-11
Status: **promising screening model; not a validated +EV strategy**

## Motivation
The current two-round Lotto format creates a useful structural question: can a Must Be Won draw become positive EV when a large inherited jackpot meets unusually low current-draw sales?

The first current-regime Must Be Won example tested (18 July 2026, Saturday) was negative. The next step is therefore to model the crowd before the draw rather than look only at the advertised jackpot.

## Rule facts
Primary Allwyn sources confirm that from 10 June 2026:
- one £2 line enters two independent 6/59 rounds;
- jackpots start at £2m;
- the jackpot can roll over up to five times before a Must Be Won event on the sixth draw;
- draws remain Wednesday and Saturday;
- the jackpot is shared across the two rounds.

Primary current-format sources:
- https://www.allwyn.co.uk/insights/double-your-luck-new-lotto-gives-players-two-chances-to-win-more-than-double-the-number-of-millionaires-expected-to-be-made
- https://www.allwyn.co.uk/insights/double-your-luck-delivers-new-lotto-creates-three-millionaires-in-first-weekend-and-over-3-1-million-winners-in-opening-draws

The indexed official National Lottery procedures are still Edition 20 (2024), i.e. the old one-round regime. They state that 9.79% of Lotto sales is allocated to the jackpot. A current independent Lotto Q&A also reports that the jackpot still receives 9.79% of ticket-sales revenue after the June-2026 redesign. We have not yet captured an updated primary procedure document confirming that percentage, so 9.79% is an **explicit research assumption** for the 2026 sales proxy, not a promoted fact.

Old primary procedure source:
https://www.national-lottery.co.uk/games/lotto/game-procedures

Current secondary cross-check:
https://www.national-lottery.com/lotto/questions-and-answers

## Sales proxy from jackpot growth
If the allocation fraction remains 9.79% and a ticket costs £2, each ticket contributes approximately:

`£2 * 0.0979 = £0.1958`

to that draw's jackpot allocation.

For an ordinary rollover transition with no reset/top-up adjustment, use:

`N_proxy = (J_t - J_(t-1)) / 0.1958`

The first 15 usable rollover increments from 13 June through 8 August 2026 are stored in:

`data/historical/uk_lotto_sales_proxy_2026.csv`

This is an inferred proxy. It is not official sales data and can be distorted by reserve-fund actions, jackpot estimation/rounding, special promotions or a changed allocation fraction.

## Strong weekday pattern
Across those 15 increments:

### Wednesday
- observations: 6
- mean implied tickets: **~5.008m**
- median: **~5.084m**
- range: **~4.661m to ~5.233m**

### Saturday
- observations: 9
- mean: **~8.785m**
- median: **~8.580m**
- range: **~7.621m to ~10.527m**

Excluding the special 4 July Millionaire Raffle draw:
- Saturday mean: **~8.567m**
- Saturday median: **~8.483m**

The day-of-week gap is therefore much larger than the short-run jackpot-size variation in this sample. Any useful pre-draw model must include Wednesday/Saturday and promotion state, not merely jackpot size.

### Promotion signal
4 July 2026 had a special event with ten £1m Millionaire Raffle winners. Its jackpot-growth proxy is approximately **10.53m tickets**, the highest point in the sample despite a jackpot of only about £4.06m. This is a warning that promotions can overwhelm ordinary jackpot-demand relationships.

## Why Match-2 winner counts are not an exact sales meter
A second possible proxy is:

`N_hat = Match2 round-winners / (2 * exact P(Match2))`

However, the same bought selections are entered into both rounds and some draws show very large Round-1/Round-2 differences in Match-2 counts. For example, the 24 June archive reports approximately 751,580 Match-2 winners in one round versus 470,345 in the other.

That difference is far too large to treat per-draw Match-2 counts as a clean binomial meter with uniform player selections. It is consistent with real player-number non-uniformity interacting with the particular winning numbers. This both weakens Match-2 as a single-draw sales estimator and strengthens the motivation for H015 (crowd-choice/sharing effects).

The jackpot-growth proxy is therefore currently the preferred screening proxy, but it still needs primary-rule and official-sales validation.

## Saturday Must Be Won screening
Using the observed regular current lower tiers (£1m / £1,000 / £50 / £10 / £1 per round), the non-jackpot fixed cash EV is approximately:

**F = £0.728983386863 per £2 ticket.**

If the jackpot allocation fraction is `f = 0.0979`, a £2 ticket contributes `f*2 = £0.1958` to the current jackpot. Let `P` be the jackpot carried into the Must Be Won draw before current-draw sales, and `N` be current sales.

A simple aggregate screening model is:

`gross EV ≈ F + P/N + 0.1958`

Break-even therefore requires:

`P/N >= £1.075216613137`

or equivalently:

`N <= P / 1.075216613137`.

This assumes the jackpot fund is fully distributable in aggregate and abstracts from updated 2026 capping/reserve details. It is a screening inequality, not proof of executable EV.

### 18 July 2026 Saturday Must Be Won
Prior jackpot on 15 July: **£7,663,813**.

The screening inequality allows at most about:

**7.128m current tickets**

for crowd-average break-even.

The jackpot-growth sales proxy for 18 July is approximately:

**9.682m tickets**.

So the observed Saturday crowd is comfortably above the screening threshold, consistent with the realized post-draw schedule also being negative.

### 27 June 2026 sixth draw
The jackpot was won rather than rolled down, but it reached the sixth draw in the cycle.

Prior jackpot on 24 June: **£7,357,143**.
- break-even max sales screen: **~6.842m**;
- current sales proxy: **~9.768m**.

Again, Saturday demand is too high under this screen.

## H016 — Wednesday Must Be Won calendar edge
This is the most interesting current lead found so far.

The sixth draw does not have to be a Saturday. Allwyn confirms that Must Be Won occurs on the sixth draw after a new jackpot cycle and draws alternate Wednesday/Saturday. Therefore:

- if a cycle resets on a **Wednesday**, its sixth draw is **Saturday**;
- if a jackpot is won/reset so the next £2m cycle starts on a **Saturday**, its sixth draw is **Wednesday**.

The current-regime cycles captured so far have produced Saturday sixth draws. On 8 August 2026, for example, the sixth draw did not rolldown because two Match-6 tickets shared the £8,535,146 jackpot.

A future cycle beginning on Saturday could therefore create the first clean Wednesday Must Be Won test in this regime.

### Median-path thought experiment
Use only the observed June-August 2026 proxy medians:
- typical Wednesday jackpot increment: **~£0.996m**;
- typical non-raffle Saturday increment: **~£1.661m**.

Starting from a £2m Saturday reset, an alternating five-draw path gives a rough prior carryover before a Wednesday sixth draw of:

**~£7.313m**.

With `P = £7.313m`, the screening break-even maximum current sales is:

**~6.801m tickets**.

Observed ordinary Wednesday sales-proxy values so far are only ~4.66m–5.23m, median ~5.08m. At the median, the screening model would imply gross crowd-average value around **£2.36 per £2 ticket**.

That is a materially positive screening result, but it is **not yet a strategy validation**. The central unknown is whether a Wednesday draw explicitly advertised as Must Be Won would attract enough extra demand to push sales above ~6.8m. Relative to the observed ordinary-Wednesday median, the threshold allows roughly a **34% sales uplift** before the screen loses break-even.

## Why this lead is stronger than 'big jackpot'
The structural opportunity is calendar-sensitive:

1. Saturday rollovers build the carryover quickly because Saturday demand is high.
2. If the cycle is aligned so the forced sixth draw lands on Wednesday, that inherited pot may meet a much smaller crowd.
3. The ratio `inherited carryover / current sales` is what matters economically.

This is exactly the kind of state-dependent mechanism the project is seeking: no prediction of draw numbers is required.

## What can invalidate the lead
Before any real-money conclusion, all of the following must be resolved:
- capture updated 2026 primary procedures and confirm the jackpot sales allocation;
- determine current Must Be Won redistribution/capping mechanics exactly;
- obtain official or otherwise robust sales data to validate the jackpot-growth proxy;
- estimate the **Must-Be-Won-specific** Wednesday sales uplift, not ordinary Wednesday demand;
- account for promotions (4 July shows they materially move demand);
- account for number-choice sharing/collisions and our own portfolio self-collision;
- use the final purchasable pre-cutoff jackpot estimate, not hindsight final jackpot;
- check legal/physical purchase constraints separately from mathematical EV.

## Status
**H016 is a promising current-game structural lead, not validated.**

The next decisive evidence is either:
1. a current-regime Wednesday Must Be Won draw, or
2. enough sales/marketing data to model what Wednesday Must Be Won demand would be before one occurs.
