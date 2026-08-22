# H178 audit append — H175 mixed-isotopy adversarial screen

Updated: 2026-08-22

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| H175 RI conditional free-2x 3-spot Keno | 100 deterministic six-layer mixed cyclic/XOR Latin isotopy designs under the H175 3+1+1+1 support allocation | Balanced local adversary found `n3<=2` counterexamples for 41/100 designs; best-found histogram: n3=1:5, 2:36, 3:42, 4:16, 5:1 | **41 CONCRETE DESIGNS REJECTED; OTHERS NOT VALIDATED**; `research/h178_h175_mixed_isotopy_adversarial_screen.md` |
| H175 exact hard-candidate check | Binary MILP searches for balanced 4-per-group witness with `n3<=2` | Seeds 178001, 178004 and heuristic-strongest 178059 all yield exact `n3=2` witnesses; seed 178059 payout = `4240+35*2=4310 < 4336` | **THREE ADDITIONAL/CONFIRMED CONCRETE DESIGNS REJECTED; H175 UNIVERSAL CLASS STILL OPEN** |

Terminal state remains **NO SUCCESS; NOT EXHAUSTED**. Next mathematical step is master-design CP-SAT/MILP with adversarial balanced-witness separation, not further reliance on local minima.
