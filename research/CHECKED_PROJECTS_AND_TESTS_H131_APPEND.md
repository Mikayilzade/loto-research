# CHECKED_PROJECTS_AND_TESTS — H131 append

Updated: 2026-08-20

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H131 Florida Lotto Love 2026 statewide Nth coupon** | 52-draw base FLORIDA LOTTO purchase at $2/draw; $208 cash coupon on every Nth qualifying statewide ticket | qualifying cost **$104**; if coupon hits, coupon alone gives **$208 = 200% gross / +$104 net** before lottery winnings | **CONDITIONAL DETERMINISTIC CASH INVERSION VALIDATED; STRICT GUARANTEE REJECTED because statewide Nth position is not player-owned**; `research/h131_global_nth_coupon_allocation.md` |
| **H131 Florida PICK Midday 2026** | minimum $1 qualifying PICK purchase; $5 coupon; 200,000 coupons / $1m total; statewide Nth allocation | conditional coupon-only net **+$4**; external interleaving leaves lawful zero-coupon outcome | **REJECTED strict guarantee**; same note |
| **H131 Florida Fantasy 5 More Money March 2026** | $5 qualifying purchase; $10 statewide Nth coupon | conditional coupon-only net **+$5**; no player-local/tranche guarantee | **REJECTED strict guarantee**; same note |
| **H131 Florida X THE CASH / 500X 2026** | $100 cash coupons generated every Nth non-winning $50 ticket entered statewide | official rule says coupons are **randomly generated**, statewide, and odds depend on number entered | **REJECTED deterministic block ownership**; same note |
| **H131 global-Nth interleaving theorem** | finite player purchases under unrestricted external statewide qualifying transactions | external transactions can occupy every coupon-bearing statewide position; strict player coupon floor = **0** absent exclusive control of the counter/block | **VALIDATED structural closure**; `src/loto_research/nth_coupon.py`, `tests/test_nth_coupon.py`, `data/derived/h131_nth_coupon_screen.csv` |

Terminal lottery state remains: **NO SUCCESS; NOT EXHAUSTED**.
