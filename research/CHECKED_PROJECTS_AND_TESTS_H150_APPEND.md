# CHECKED_PROJECTS_AND_TESTS — H150 append

Updated: 2026-08-21
Scope: LOTTERY ONLY

Authoritative append to `research/CHECKED_PROJECTS_AND_TESTS.md`.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H150 Missouri Club Keno Bulls-Eye** | exact full cover of every k-subset, k=1..10, with one distinguished winning ball; base/no-mark and Bulls-Eye/marked cases counted combinatorially | exact deterministic return ranges **55.0000%–60.6500%**; best 3-Spot **60.6500%** | **REJECTED guaranteed-profit fixed-paytable cover**; `research/h150_missouri_club_keno_marked_ball_cover.md` |
| **H150 Missouri Club Keno Double Bulls-Eye** | exact zero/one/two marked-ball decomposition for every k-subset, k=2..10 | best nominal return **65.3369%** on 9-Spot; $1m/$5m liability rules can only worsen strict floor | **REJECTED guaranteed-profit fixed-paytable cover**; same file |
| **H150 Missouri Club Keno Multiplier** | strict worst-case wheel state under full cover | legal 1x state remains while add-on doubles cost; best strict floor <= **31.2196%** | **REJECTED guaranteed-profit modifier**; same file |
| **H150 marked-ball Keno theorem** | one marked winner: `C(19,j)` / `C(19,j-1)`; two marked winners: `C(18,j)`, `2C(18,j-1)`, `C(18,j-2)` | exact draw-invariant gross for fixed non-shareable marked-ball paytables | **VALIDATED reusable theorem**; `src/loto_research/keno_marked_ball_cover.py`, `data/derived/h150_missouri_bullseye_full_cover.csv` |

Current terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.
