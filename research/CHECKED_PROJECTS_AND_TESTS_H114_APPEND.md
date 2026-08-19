# CHECKED_PROJECTS_AND_TESTS — H114 append

Updated: 2026-08-20
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H114 Azerbaijan TezLoto dynamic odds** | exact mathematical screen of all 159 published state × bet-type cells | best gross return only **78.2609%**; all other cells lower | **REJECTED base positive-EV route**; `research/h114_tezloto_dynamic_odds_exact_screen.md` |
| H114 complete coverage — Next exact ball | buy every remaining number at each state | deterministic gross ratio equals published/fair odds; max <1 | **REJECTED guaranteed-profit coverage** |
| H114 complete coverage — exact next-two set | buy every remaining unordered pair | exactly one pair wins; deterministic gross ratio <1 in every published state | **REJECTED guaranteed-profit coverage** |
| H114 complete coverage — 1 of next 6 | buy every remaining number | exactly six winning selections; max deterministic return <1 | **REJECTED guaranteed-profit coverage** |
| H114 complete coverage — 2 of next 6 | buy every remaining pair | exactly 15 winning selections; max deterministic return <1 | **REJECTED guaranteed-profit coverage** |
| H114 complete coverage — 3 of next 6 | buy every remaining triple | exactly 20 winning selections; max deterministic return <1 | **REJECTED guaranteed-profit coverage** |
| H114 / H007 RNG-bias hurdle | exploit persistent non-uniform virtual-ball probabilities | best base RTP 0.782609 implies required probability lift >**27.78%** above uniform just for positive EV | **OPEN ONLY WITH RELIABLE HIGH-FREQUENCY HISTORY + OUT-OF-SAMPLE VALIDATION** |

Terminal lottery state remains: **NO SUCCESS; NOT EXHAUSTED**.
