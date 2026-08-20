# CHECKED_PROJECTS_AND_TESTS — H125 append

Updated: 2026-08-20

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H125 Jersey Hospice Million Pound Lottery 2026** | fixed-board late-entry sensitivity using verified £300 price, £1.3m board, indexed `2,500 tickets remaining`, and recent 7,000-ticket architecture as explicit continuity assumption | break-even denominator **4,333.33**; 7,000-cap sensitivity implies 4,500 sold, EV **£288.89/ticket = 96.2963% gross**, ROI **-3.7037%** | **NEAR-THRESHOLD NEGATIVE / monitor-calibration only**; 2026 total cap not directly recovered; `research/h125_fixed_board_raffle_near_threshold_calibration.md` |
| **H125 Minnesota Millionaire Raffle 2026** | exact fixed prize board vs 1,000,000 × $10 sold-out supply | exact board **$5,149,150**; `N*=514,915`; realized sellout gross **51.4915%**; sold out in 14 days | **REJECTED undersubscription edge / high-demand negative control**; same note + `data/derived/h125_fixed_board_raffle_calibration.csv` |
| **H125 Michigan online raffle architecture** | current official limited-supply, predetermined-prize, deadline-or-sellout architecture | structurally monitorable; no crawlable active game with both live denominator and prize board recovered in this packet | **MONITOR OPEN / no live EV claim**; same note |

Terminal lottery state remains: **NO SUCCESS; NOT EXHAUSTED**.
