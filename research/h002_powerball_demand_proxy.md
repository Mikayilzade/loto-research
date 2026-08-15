# H002 — Powerball observed demand / winner-count proxy

Updated: 2026-08-15
Status: **first empirical demand anchors added; useful for sharing scale, not yet a fitted sales-response law**

## Purpose
The sharing threshold model needs the number of other plays `n`. Official public result pages expose winner counts but not a simple nationwide ticket-sales field. Since Powerball's official overall odds of winning any prize are **1 in 24.87**, aggregate winner counts provide a noisy draw-level play-count proxy:

`estimated plays ≈ observed prize-winning tickets * 24.87`.

This is not exact sales data. Winner counts are random, the official odds denominator is rounded, and after the UK launch the US result-table coverage may not include UK lower-tier winners even though UK plays share the common jackpot. Post-UK estimates are therefore especially suitable as lower-bound / scale proxies, not exact global sales.

## Primary sources
Official Powerball prize chart:
- https://www.powerball.com/powerball-prize-chart
- overall odds 1 in 24.87.

Official nationwide result pages used:
- 2026-06-20: https://www.powerball.com/draw-result?date=2026-06-20&gc=powerball
- 2026-07-08: nationwide aggregate indexed result page
- 2026-07-25: https://www.powerball.com/draw-result?date=2026-07-25&gc=powerball
- 2026-07-29: https://www.powerball.com/draw-result?date=2026-07-29&gc=powerball

Official FAQ confirms UK ticket sales began July 21, 2026 and UK jackpot-winning tickets share the same pari-mutuel jackpot:
- https://www.powerball.com/faqs

## Observed anchors
Data file:
- `data/derived/h002_powerball_winner_count_sales_proxy.csv`

| draw | advertised jackpot | cash value | observed non-jackpot winning tickets | estimated base plays | sharing-only break-even cash |
|---|---:|---:|---:|---:|---:|
| 2026-06-20 | $300m | $135.8m | 579,759 | ~14.42m | ~$503.1m |
| 2026-07-08 | $435m | $195.0m | 511,306 | ~12.72m | ~$501.7m |
| 2026-07-25 | $613m | $268.4m | 1,067,515 | ~26.55m | ~$513.6m |
| 2026-07-29 | $668m | $292.5m | 840,242 | ~20.90m | ~$508.7m |

The sharing-only break-even column uses the exact binomial expected-share formula in `powerball_threshold.py` and assumes:
- uniform exact-combination popularity;
- zero tax;
- no execution cost;
- the proxy play count equals the relevant competing jackpot population.

## Interpretation
1. Realistic recent draw-scale participation is already large enough to move the optimistic no-sharing threshold upward by roughly **$10m–$23m** in these sampled states.
2. The observed cash jackpots ($135.8m–$292.5m) remain nowhere near even the sharing-adjusted zero-tax break-even values (~$502m–$514m).
3. Winner-count noise is large enough that four points cannot support a precise fitted `n(J)` curve. Demand is also affected by day-of-week, jackpot publicity and now UK participation.
4. After July 21, a US-result winner-count proxy can understate the global jackpot-sharing population because UK lower-tier prizes are separately administered while the jackpot is common.

## Strong conclusion from this packet
The recent 2026 run through at least July 29 is not close to a positive-EV state under any reasonable sharing correction. The cash value would have needed to be roughly **70%+ larger** than the observed $292.5m even in a zero-tax model.

## Remaining H002 work
- Collect a broader set of nationwide aggregate result pages, with clean separation of jurisdiction-filtered pages.
- Prefer direct official sales if an authoritative series becomes available.
- Fit a conservative demand band rather than a single regression.
- Combine with jurisdiction-specific tax/withholding and H015 anti-popularity only after sales scale is anchored.
- Then compare Mega Millions and EuroMillions, where ticket price/matrix/jackpot mechanics differ materially.
