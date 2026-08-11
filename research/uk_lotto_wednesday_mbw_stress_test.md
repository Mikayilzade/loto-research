# UK Lotto — Wednesday Must Be Won historical stress test

Updated: 2026-08-11
Status: **H016 materially weakened; current-regime +EV not validated**

## Question
The first current-regime screening model suggested that a Wednesday Must Be Won draw could become positive EV if inherited carryover met ordinary Wednesday demand. The key risk was obvious: Must Be Won marketing itself may increase Wednesday sales.

Because the current two-round format began only on 10 June 2026 and no current-regime Wednesday Must Be Won draw has yet been captured, this file uses natural Wednesday sixth-draw states from the old one-round regime as a demand stress test.

This is not a direct EV backtest across rule regimes. It is a behavioural stress test: how much did a Wednesday sixth-draw / Must-Be-Won state increase demand relative to the previous ordinary Wednesday in the same jackpot cycle?

## Why jackpot growth is preferred to Match-2 winner counts here
Under the old regime, the primary National Lottery procedures state that 9.79% of Lotto sales was allocated to the jackpot. If that allocation and reserve treatment are stable within a rollover cycle, jackpot increment is proportional to sales:

`draw sales proxy ∝ J_t - J_(t-1)`

When comparing two Wednesdays in the same cycle, the 9.79% factor and ticket price cancel. Therefore the relative demand proxy is:

`uplift = (MBW jackpot increment / previous-Wednesday jackpot increment) - 1`

This is cleaner than Match-2 winner counts because Match-2 counts are affected by the winning-number composition and non-uniform player choices.

Caveat: jackpot estimates can still be affected by reserve-fund actions, rounding, special top-ups and procedure details. It remains a proxy, not official ticket sales.

## Historical sample
Stored in:

`data/historical/uk_lotto_wednesday_mbw_stress_old_regime.csv`

Seven natural Wednesday sixth-draw states were reconstructed:

| Date | Outcome | Jackpot-growth uplift proxy | Match-2 uplift proxy |
|---|---|---:|---:|
| 13 Dec 2023 | jackpot won | +42.85% | +30.36% |
| 8 May 2024 | rolldown | +35.30% | +20.01% |
| 4 Sep 2024 | jackpot won | +42.84% | +54.40% |
| 29 Oct 2025 | rolldown | +46.18% | +40.81% |
| 11 Feb 2026 | rolldown | +33.12% | +48.44% |
| 4 Mar 2026 | rolldown | +43.57% | +57.55% |
| 25 Mar 2026 | rolldown | +42.97% | +41.26% |

Jackpot and winner-count sources are preserved on the historical result/archive pages at lottery.co.uk. Examples:
- https://www.lottery.co.uk/lotto/results-13-12-2023
- https://www.lottery.co.uk/lotto/results-08-05-2024
- https://www.lottery.co.uk/lotto/results-04-09-2024
- https://www.lottery.co.uk/lotto/results-29-10-2025
- https://www.lottery.co.uk/lotto/results-11-02-2026
- https://www.lottery.co.uk/lotto/results-04-03-2026
- https://www.lottery.co.uk/lotto/results-25-03-2026

## Result
For the jackpot-growth demand proxy:
- observations: **7**;
- mean uplift: **+40.97%**;
- median uplift: **+42.85%**;
- range: **+33.12% to +46.18%**.

For the independent but noisier Match-2 winner-count proxy:
- mean uplift: about **+41.83%**;
- median uplift: about **+41.26%**;
- range: about **+20.01% to +57.55%**.

The two imperfect proxies therefore point in the same direction: a natural Wednesday Must Be Won state historically attracted materially more participation than an ordinary Wednesday.

## Impact on H016
The current 2026 median-path screen used:
- ordinary current-regime Wednesday demand proxy: **~5.084m tickets**;
- hypothetical inherited carryover before a Wednesday sixth draw: **~£7.313m**;
- screening break-even maximum current sales: **~6.801m tickets**;
- allowable uplift before losing break-even: **~+33.77%**.

Historical old-regime jackpot-growth uplift exceeds that +33.77% margin in **6 of 7** reconstructed states. The one exception, 11 February 2026, is only slightly below it at +33.12%.

Applying the historical uplift distribution mechanically to the current ordinary-Wednesday median gives:
- using historical mean uplift: projected current sales **~7.168m**;
- using historical median uplift: projected current sales **~7.263m**.

Both exceed the ~6.801m screening break-even limit.

With the original median-path carryover and current observed fixed-prize baseline, the simple aggregate screen becomes approximately:
- historical mean-uplift case: **~£1.95 gross value per £2 ticket**;
- historical median-uplift case: **~£1.93 gross value per £2 ticket**.

Thus the initial apparent +EV is not robust to historically observed Must-Be-Won demand response.

## Interpretation
H016 is **not rejected mathematically**, because the old and new Lotto formats differ and the current 2026 rules may change both player response and prize economics. But it is no longer reasonable to label the calendar effect alone as a promising +EV lead.

The hypothesis now requires at least one of the following to become attractive again:
1. a current-regime Wednesday Must Be Won draw whose sales uplift is materially below old-regime history;
2. a larger inherited carryover than the median-path scenario;
3. a verified current rule that increases distributable overlay beyond the screening assumptions;
4. measurable anti-popularity / sharing improvements from H015;
5. a promotion or purchase-price overlay that changes effective ticket cost.

## Decision
**Downgrade H016 from `promising` to `inconclusive / weakened`.**

This is a useful negative result: it prevents us from mistaking ordinary-Wednesday demand for Must-Be-Won demand and demonstrates why sales response must be modelled before calling a forced-redistribution state positive EV.

## Next test
Do not spend more effort trying to prove H016 from the same tiny current dataset. Priority shifts to:
- updated primary 2026 procedures;
- H015 crowd-choice/sharing model;
- Azerbaijan 4+4 lower-tier carryover reconstruction;
- broader search for current games where the overlay is less efficiently competed away.
