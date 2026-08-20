# CHECKED_PROJECTS_AND_TESTS — H129 append

Updated: 2026-08-20

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H129 fixed-board late takeover theorem** | Buy every unsold ticket after `E` external tickets already exist; assign external tickets the highest-value prize slots adversarially | Exact guaranteed floor `G(E)=max(0,total_board-sum(E highest prizes))`; if `E >= number_of_prize_slots`, strict floor is zero | **THEOREM VALIDATED**; `src/loto_research/raffle_takeover_floor.py`, `research/h129_nc_raffle_late_takeover_floor.md` |
| **H129 NC Celebrate America Raffle 2026** | Cap 25,000 × $10; board 20×$2,500 + 250×$250 + 2,000×$25; buy all remaining tickets for every `E` | Best strict takeover floor occurs at `E=0`: **$162,500/$250,000 = 65.0%**; declines thereafter; at `E>=2,270`, floor is zero | **REJECTED guaranteed-profit takeover**; `data/derived/h129_nc_raffle_takeover_floor.csv` |
| H129 NC undersubscription EV threshold | Fixed board / ticket price | pre-tax random-ticket +EV iff final sold count `<16,250`; official final sold count not recovered in this run | **MONITOR LEAD ONLY / HISTORICAL DENOMINATOR DATA-BLOCKED** |

Lottery terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.
