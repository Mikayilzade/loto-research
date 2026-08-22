# H174 audit append — Rhode Island doubled-Keno partition exhaustion

Updated: 2026-08-22

| ID | Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|---|
| H174 | Rhode Island 3-spot Keno under free pre-locked 2x | Exhaustive disjoint clique-partition search for all nondecreasing integer partitions of 80 into k=1..8 groups; exact DP worst-case over every 20-hit allocation | **411,498** partitions tested. Cheapest strict-positive clique partition remains **20+20+20+20**, cost 4,560, worst gross 5,000, **109.6491%**. No positive clique partition exists for k=5..8; 5x16 is exactly 100%. | **H173 PROVEN OPTIMAL WITHIN TESTED CLIQUE-PARTITION FAMILY; cross-block designs remain open.** `research/h174_ri_keno_partition_exhaustion_and_plus_timing.md`, `src/loto_research/h174_ri_keno_partition_search.py`, `data/derived/h174_ri_keno_partition_summary.csv` |
| H174b | Rhode Island Keno Plus timing | Wait for Plus wheel result, then attempt same-draw purchase | Plus wheel is just prior to applicable Keno draw, but Plus must already be attached to the wager; official FAQ says iLottery wagering is unavailable during each game's draw-break period. No official same-draw post-wheel purchase path found. | **REJECTED as executable current exploit absent new official evidence.** Same H174 research file. |
