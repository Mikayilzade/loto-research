# H145 audit append — Nebraska Keno execution lock + coupon threshold

Updated: 2026-08-21

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| H145 Nebraska municipal Keno | Big Red/La Vista account-funding reversibility | Play+ balance is transferable out; external principal need not remain trapped | **VALIDATED current**; `research/h145_nebraska_keno_execution_lock_and_coupon_threshold.md` |
| H145 Nebraska municipal Keno | Incomplete-cover unwind | purchased ticket can be voided before game starts; funds return to account balance | **VALIDATED current execution safeguard** |
| H145 Nebraska municipal Keno | paytable lock | Nebraska rules require payout schedule known before selection; outside ticket identifies applicable paytable | **VALIDATED regulatory execution lock** |
| H145 coupon-adjusted Pick-1 | all 80 numbers at $0.25 + pre-owned $5 free-play | external cash $15; 3.00x payout = break-even; any fixed `p>3.00` becomes pre-tax positive | **THRESHOLD THEOREM VALIDATED**; `data/derived/h145_nebraska_pick1_coupon_thresholds.csv` |
| H145 La Vista $5 Keno Cash | public burger promotion | opened current page specifies July dates; not treated as live on 2026-08-21 | **EXPIRED / NOT CURRENTLY USABLE** |
| H145 Kearney 2026 special paytable | Kearney-specific table reported in use since early April 2026 | current community-specific paytable existence confirmed; exact numeric table not publicly recovered | **PROMISING / DATA CAPTURE BLOCKER** |

Terminal state after H145: **NO SUCCESS; NOT EXHAUSTED**.
