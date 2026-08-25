# CHECKED PROJECTS AND TESTS — H265 APPEND

## H265 — New Jersey Pick-3 Green Ball terminal Double Draw

- Candidate class: terminal/elimination promotion with deterministic free second draw.
- Official 2026 promotion checked: July 6–August 3, 2026.
- Structural result: after six white-ball removals, the Green Ball is the only remaining promotion ball, so a free second Pick-3 draw can be known in advance in that terminal state.
- Exact portfolio bound: every published $0.50 base primitive has one-draw average return <=50%; two guaranteed base draws therefore have average return <=100%.
- Best no-FIREBALL terminal ratio: **100%** (Straight/Pair), not strictly above cost.
- Best with-FIREBALL terminal ratio: **77%**; FIREBALL doubles cost but is excluded from Green Ball second-draw determination.
- Proof class: `min legal-outcome gross <= average gross`; nonnegative mixtures, Straight/Box and Wheels inherit the primitive bound.
- Instant Match does not help strict guarantees because a legal nonwinning result gives zero worst-case contribution while adding cost.
- Status: **CLOSED / REJECTED under checked rules**.
- Reopen gate: future deterministic >2-draw benefit, payout increase, guaranteed subsidy, or discount that pushes terminal average strictly above 100%.

Files:
- `research/h265_nj_pick3_green_ball_terminal_bound.md`
- `research/H265_VALIDATION.md`
- `src/loto_research/h265_nj_pick3_green_ball_bound.py`
- `data/derived/h265_nj_pick3_green_ball_bound.json`
