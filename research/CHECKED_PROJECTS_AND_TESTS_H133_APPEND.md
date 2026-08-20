# CHECKED_PROJECTS_AND_TESTS — H133 append

Updated: 2026-08-20

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H133 Georgia Lottery 50% first-deposit bonus + Cash Pop full cover** | absorb max $125 bonus into repeated 15-number $1 covers | one cover costs $15 and guarantees $5; 25 covers cost $375 nominal, external cash at least $250, guaranteed cash $125 = **50% external-cash floor** | **REJECTED guaranteed-profit combination**; `research/h133_wallet_bonus_compact_coverage.md` |
| **H133 West Virginia $10 deposit -> $10 Free Play + Daily 3 exact full cover** | 1000 outcomes at $0.50 exact; use full $10 capped free play | full cover `C=$500`, guaranteed `P=$250`; external cash at least `$490`; strict profit floor **-$240** | **REJECTED current guaranteed-profit combination**; same note |
| H133 wallet-subsidy threshold | generic complete cover | strict pre-tax condition `P > C-B`, equivalently deterministic eligible bonus `B > C-P` | **VALIDATED screening theorem**; same note |

Terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.
