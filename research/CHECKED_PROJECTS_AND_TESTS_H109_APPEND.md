# CHECKED_PROJECTS_AND_TESTS — H109 append

Updated: 2026-08-19
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H109 Irish Millionaire Raffle fixed unique supply** | buy all 600,000 tickets at €25 | spend €15m; all 8,500 guaranteed prizes total €6.3425m; deterministic gross **42.2833%** | **REJECTED guaranteed-profit full takeover**; `research/h109_unique_issued_raffle_takeover.md` |
| **H109 fixed unique-raffle theorem** | full acquisition of capped unique ticket supply | strict profit requires total guaranteed prize pool `P > N*c + all costs`; otherwise full sweep deterministically loses | **VALIDATED necessary condition** |
| **H109 Canada LOTTO 6/49 Gold Ball** | dynamic unique 10-digit number per $3 play; winner selected from all issued entries | one external issued number creates legal branch where external number wins and buyer gets zero Gold Ball payout | **STRICT TAKEOVER GUARANTEE REJECTED** |
| H109 Gold Ball + full Classic coverage stress | buy all `C(49,6)=13,983,816` Classic combinations; external Gold Ball number wins | cost $41,951,448; deliberately favorable Classic upper bound only **$21,055,750.97 = 50.1908%** | **REJECTED guaranteed-profit package**; `data/derived/h109_unique_raffle_screen.csv` |
| H109 OLG WINTARIO50 2025 | historical dynamic unique-number issued-entry raffle | fixed prizes total $5.98m; player could not select unique numbers; winners drawn from eligible issued plays | **HISTORICAL STRUCTURAL CONTROL; NOT CURRENT** |

Lottery terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.
