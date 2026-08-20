# CHECKED_PROJECTS_AND_TESTS — H126 append

Updated: 2026-08-20

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H126 Michigan Super Raffle 2025 undersubscription** | Reconstruct final sold pool from 18,515 published winning numbers; headline board $12.45m, $50 tickets | Largest winner 219,210; order-statistic reconstruction puts final denominator near ~219.2k, far below nominal break-even 249,000; headline nominal EV ~**$56.79/$50 = +13.59% ROI** | **STRONG HISTORICAL NOMINAL +EV OVERLAY VALIDATED**; `research/h126_michigan_super_raffle_undersubscription_reconstruction.md` |
| H126 cash-equivalent correction | Replace $6m/$1m annuity headlines with observed lump-sum values ~$4.1m and ~$693k each | Cash-equivalent board ~$9.936m; break-even 198,720; at ~219.2k sold cash EV ~**$45.33/$50 = -9.35% ROI** | **IMMEDIATE-CASH +EV REJECTED**; `data/derived/h126_michigan_super_raffle_thresholds.csv` |
| H126 strict guarantee | Full takeover / deterministic floor | Full 350k launch coverage costs $17.5m > $12.45m nominal board; incomplete late portfolio can lose entirely | **GUARANTEED-PROFIT TAKEOVER REJECTED** |

Terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.

Monitor implication: for every fixed-board raffle compute both the headline `N*_nominal` and a **cash-equivalent tax/cost-adjusted `N*_cash`**. H126 demonstrates that headline annuity undersubscription can look +EV while economically realizable cash remains negative.
