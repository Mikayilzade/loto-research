# H034 — Ontario DAILY KENO fixed-payout coverage

Updated: 2026-08-16
Status: **REJECTED as guaranteed-profit additive/coverage class**

## Goal
Screen a current compact fixed-payout game for a strict all-outcome profit construction, with special attention to whether fixed prizes and advance play create a deterministic coverage opportunity.

## Current official mechanics
Primary official OLG sources checked 2026-08-16:
- https://www.olg.ca/en/lottery/play-daily-keno-encore/daily-keno-game-conditions.html
- https://www.olg.ca/en/frequently-asked-questions/lottery-games/daily-keno.html

Current game conditions state:
- 20 numbers are drawn from 1–70;
- Pick categories 2 through 10 are available;
- stakes are CAD 1, 2, 5, or 10;
- prizes scale linearly with stake according to the published fixed table;
- only one prize is payable per selection;
- OLG caps aggregate payout **per prize category per draw at CAD 4,000,000**, with proportional reduction if the cap is exceeded;
- Advance Play is available, but the current public rules/FAQ show no deterministic price discount analogous to NZ Bullseye.

The category cap can only make a large-portfolio result worse than the nominal fixed table. Therefore the cleanest rejection test is deliberately favorable: ignore the cap completely.

## Exact full-space identity
For Pick `k`, buy every `k`-subset of 70 exactly once at CAD 1 each.

Total variants:

`C(70,k)`.

For any realized draw of 20 winning numbers, the number of our covered selections with exactly `m` matches is invariant:

`C(20,m) * C(50,k-m)`.

Thus nominal full-space gross payout is deterministic before the category cap.

Implementation:
- `src/loto_research/ontario_daily_keno.py`
- `tests/test_ontario_daily_keno.py`
- `data/derived/h034_ontario_daily_keno_full_coverage.csv`

## Results — favorable uncapped upper bound
| Pick | Full-space cost (CAD) | Nominal uncapped gross (CAD) | Gross return |
|---:|---:|---:|---:|
| 2 | 2,415 | 1,330 | **55.0725%** |
| 3 | 54,740 | 28,500 | **52.0643%** |
| 4 | 916,895 | 484,500 | **52.8414%** |
| 5 | 12,103,014 | 5,087,250 | **42.0329%** |
| 6 | 131,115,985 | 58,140,000 | **44.3424%** |
| 7 | 1,198,774,720 | 579,462,000 | **48.3379%** |
| 8 | 9,440,350,920 | 4,399,260,000 | **46.6006%** |
| 9 | 65,033,528,560 | 27,991,180,000 | **43.0412%** |
| 10 | 396,704,524,216 | 177,571,006,340 | **44.7615%** |

Best nominal full-space result is only Pick 2 at **55.0725%**.

For Pick 2 the own top-category nominal liability is only CAD 1,330, so the CAD 4m category cap is irrelevant to our own full coverage in isolation. For larger Pick categories some nominal own-category liabilities themselves become enormous; the statutory category cap would sharply reduce actual payout. Hence every figure above is an upper bound, not an understated result.

## Stronger additive impossibility result
Under the published base game:
- stake scaling is linear;
- every Pick category has gross expected value strictly below stake even **before** applying the CAD 4m category cap;
- by symmetry each base selection's gross EV/stake equals the corresponding full-space ratio above.

Any finite nonnegative additive portfolio of these selections therefore also has negative expected profit before cap/execution.

A portfolio that produced strictly positive profit in **every** legal draw outcome would necessarily have positive expected profit. That contradicts the negative expectation of every nonnegative additive mixture.

Therefore not only naive full-space coverage, but the entire ordinary additive DAILY KENO base-game portfolio class is rejected as a strict guaranteed-profit route unless a separate deterministic subsidy/discount is introduced.

## Advance Play / scaling
OLG currently permits Advance Play for consecutive draws and stakes of CAD 1/2/5/10. Public mechanics show linear stake scaling and no deterministic multi-draw discount. Repeating a negative-guarantee portfolio across draws cannot transform it into an all-outcome positive guarantee; each sequence still contains outcome paths whose aggregate payout is below aggregate cost.

## Conclusion
**Ontario DAILY KENO is closed as a current guaranteed-profit additive/coverage route.**

Reason:
- favorable uncapped gross return is only **42.03%–55.07%** across Pick 2–10;
- the CAD 4m category cap can only reduce large-portfolio payouts;
- no current deterministic advance-play discount was identified;
- expectation linearity rules out any ordinary nonnegative additive mixture as an all-outcome positive-profit construction.

This remains a useful control for future searches: fixed prizes alone are insufficient; the next high-value target should combine **non-shared fixed cash payouts with a large deterministic discount/subsidy** or have an exogenous guaranteed pool that is not diluted by our own coverage.
