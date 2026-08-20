# CHECKED_PROJECTS_AND_TESTS — H134 append

Updated: 2026-08-20

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H134 guaranteed-prize subscription** | The Scotto Play Free Until September + 12-month guaranteed prize | 12 paid months at £11.50 = £138 mandatory cost; guaranteed prize floor £12; strict return **8.6957%**, profit floor **-£126** | **REJECTED guaranteed-profit route**; `research/h134_guaranteed_prize_and_free_ticket_subsidy_screen.md` |
| **H134 free-ticket subsidy** | Hoosier Murphy USA buy two $5 scratch tickets, may receive free $1 Scratch-off | free random ticket has legal $0 outcome; strict promo cash value **$0** | **REJECTED as deterministic subsidy**; same note |
| **H134 free-ticket subsidy** | Hoosier Village Pantry buy one $10 Scratch-off, may receive free $1 Scratch-off | free random ticket has legal $0 outcome; strict promo cash value **$0** | **REJECTED as deterministic subsidy**; same note |
| **H134 zero-cost free-roll** | Hoosier Lottery Day free $1 Scratch-off | external cost $0, but legal no-win state leaves strict profit floor $0 | **POSITIVE-EV FREE-ROLL VALIDATED / terminal strict-positive guarantee REJECTED**; same note |
| **H134 reusable theorem** | classify promo benefit before H133 threshold test | free random ticket / sweepstakes strict floor = 0; guaranteed future prize must be netted against all mandatory vesting cost; only deterministic player-owned subsidy counts toward `B_d` | **VALIDATED screening theorem**; `data/derived/h134_current_false_subsidy_screen.csv` |

Terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.
