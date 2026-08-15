# Audit append — H029b Virginia FIREBALL

Updated: 2026-08-16

This append preserves the H029b checked-test row pending consolidation into the large master ledger without dropping existing history.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H029b Virginia FIREBALL paid add-ons** | Current Pick 3 / Pick 4 / Pick 5 Exact, Any, 50/50, Combo/Pair FIREBALL menus; normalize Combo by incremental FIREBALL cost; deliberately double-count 50/50 overlapping published prize rows to create a player-favorable EV upper bound | maximum FIREBALL EV/stake upper bounds: Pick 3 **65.5999%**, Pick 4 **62.8960%**, Pick 5 **60.3587%**; with base EV/stake <=50%, best deliberately favorable base+FIREBALL combined ratio < **57.8000%** | **REJECTED entire current paid FIREBALL additive guarantee class** by expectation-linearity theorem; `research/h029_fixed_digit_games_impossibility.md`, `data/derived/h029b_virginia_fireball_ev_bounds.csv`, `src/loto_research/fireball_bounds.py` |

Primary current operator sources:
- https://www.valottery.com/data/draw-games/pick3
- https://www.valottery.com/data/draw-games/pick4
- https://www.valottery.com/data/draw-games/pick5
