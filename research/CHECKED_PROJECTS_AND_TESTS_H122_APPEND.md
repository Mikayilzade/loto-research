# CHECKED_PROJECTS_AND_TESTS — H122 append

Updated: 2026-08-20

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H122 Florida Millionaire Raffle 2026 undersubscription overlay** | Final observed sales `369,180 × $20`; fixed rule board = `4×$704,500 + $10m` | ticket revenue **$7.3836m** vs nominal prize board **$12.818m**; aggregate operator-funded overlay **+$5.4344m** | **STRONG HISTORICAL/RECENT +EV OVERLAY VALIDATED**; `research/h122_florida_millionaire_raffle_undersubscription_overlay.md` |
| H122 last-window ticket | Ticket eligible for fourth interim + final draw at observed final denominator | pre-tax EV **$28.9953 on $20**, ~**+44.9767%** expected ROI; pre-tax break-even denominator **535,225 tickets** | **POSITIVE EV VALIDATED / tax+execution dependent**; `data/derived/h122_florida_raffle_overlay.csv` |
| H122 terminal guarantee | Incomplete ownership of eligible tickets | external sold tickets can legally contain all winning numbers; strict portfolio payout floor = **$0** | **REJECTED guaranteed-profit claim** |
| H122 full acquisition from launch | buy all 2,000,000 tickets | cost **$40m** vs maximum fixed board **$22.818m = 57.045% gross** | **REJECTED buy-the-pot guarantee** |

Terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.

New reusable branch: monitor future official fixed-prize raffles for live undersubscription where a late ticket's remaining fixed-prize pool divided by projected eligible ticket count exceeds ticket price after tax/cost reserve. Reopen terminal guarantee only if complete eligible ownership or a deterministic minimum payout per portfolio/block is actually enforceable.
