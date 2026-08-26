# H286 STATUS

Updated: 2026-08-26
State: **CLOSED / REJECTED for tested mechanism**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Mechanism tested
Michigan Lottery Daily Spin to Win as a deterministic external subsidy.

## Terminal result
The current Michigan Lottery FAQ states that every spin wins a prize, but the legal prize set includes monthly giveaway entries in addition to in-store and online free play. A giveaway entry has a legal later drawing outcome in which it wins no cash, so its guaranteed withdrawable-cash value is exactly $0.

Therefore the strict per-spin cash floor is:

`min legal prize-class cash floor = $0`.

The phrase `every spin wins a prize` does not create a guaranteed-cash theorem. No checked public rule supplies a bounded elimination/terminal mechanic forcing Bonus Cash after finitely many spins.

## NEXT ACTION
Do not reopen the current Daily Spin mechanism unless the wheel/prize rules materially change. Continue with one of:
1. a guaranteed reward whose every legal outcome is withdrawable cash or cash-equivalent;
2. a bounded terminal promotion that forces positive Bonus Cash after finitely many steps;
3. deterministic cashback triggered by controllable spend and large enough to cross a proven exact-cover deficit;
4. hard-capped/reservable inventory with guaranteed liabilities exceeding acquisition cost.

Files:
- `research/h286_michigan_daily_spin_cash_floor.md`
- `research/H286_VALIDATION.md`
- `src/loto_research/h286_michigan_daily_spin_floor.py`
- `data/derived/h286_michigan_daily_spin_floor.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H286_APPEND.md`
