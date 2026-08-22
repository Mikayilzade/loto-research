# H179 audit append — H175 intensified balanced-adversary screen

Updated: 2026-08-22

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| H175 RI conditional free-2x 3-spot Keno | Re-screen the fixed H178 bank of 100 mixed cyclic/XOR Latin-isotopy six-layer designs with 40 greedy balanced restarts and 60 swap-descent steps per restart | Explicit balanced `n3<=2` witnesses found for **63/100** designs; strengthened histogram `n3=1:3, 2:60, 3:33, 4:3, 5:1` | **63 CONCRETE DESIGNS REJECTED BY EXPLICIT LOCAL WITNESS; REMAINDER NOT VALIDATED**; `research/h179_h175_intensified_adversarial_screen.md` |
| H175 exact hard-candidate follow-up | Exact binary MILP feasibility for balanced 4-per-group witness with `n3<=2` | Seeds `178033`, `178042`, `178008` all yield exact feasible `n3=2` witnesses; each implies H175 gross `4310 < 4336` | **THREE HEURISTIC-HARD CANDIDATES REJECTED EXACTLY; UNIVERSAL DESIGN CLASS STILL OPEN**; `src/loto_research/h179_h175_intensified_screen.py` |

Terminal state remains **NO SUCCESS; NOT EXHAUSTED**. Next step: master-design CP-SAT/MILP/cutting-plane search or a combinatorial impossibility bound for the universal `n3>=3` condition.
