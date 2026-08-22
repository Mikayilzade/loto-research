# H175 audit append — Rhode Island doubled-Keno hybrid transversal design

Updated: 2026-08-22

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| RI conditional free-2x 3-spot Keno | 5x16 clique base + six 256-block Latin transversal layers | total cost 4,336; exhaustive 5,005 layer-support allocations over 10 group triples and 10,451 draw-count compositions identify a 3+1+1+1 support allocation with non-balanced pair-only gross >=4,370; balanced gross is 4,240 + 35*n3 and needs universal n3>=3 | **PROMISING NEW SUB-4,560 DESIGN CLASS; NOT YET VALIDATED**; `research/h175_ri_keno_hybrid_4336_transversal_gate.md` |
| RI conditional free-2x 3-spot Keno | concrete GF(16) affine realization: coefficients 1,2,4 on support 012 and coefficient 1 on supports 034/134/234 | exact binary MILP over balanced 4-from-each-group draws finds minimum n3=0 | **REJECTED concrete affine realization**; `src/loto_research/h175_ri_keno_hybrid_transversal.py` |

Terminal state remains **NO SUCCESS; NOT EXHAUSTED**. Current RI promotion/paytable/execution gates from H172-H174 remain unresolved; H175 is a combinatorial continuation only.
