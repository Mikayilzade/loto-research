# H288 STATUS

Updated: 2026-08-26
State: **CLOSED / REJECTED for tested mechanism**
Global state: **NO SUCCESS; NOT EXHAUSTED**

H225-X* was checked first and remains rigorously **CLOSED / EXHAUSTED** at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## Mechanism tested
Current Georgia Lottery Promotion 27012 (50% first-deposit bonus, max $125) layered onto the current Cash 3 and Cash 4 fixed-pay wager families.

## Result
The promotion gives at most 1.5x playable balance per unit of deposited external cash. Exact full-result-space recomputation of every published primitive fixed-pay wager class gives:

- Cash 3 best: **1-Off = 50.60% average gross**;
- Cash 4 best: **1-Off = 50.28% average gross**;
- all other checked Straight / Box / Straight-Box / Combo / Pair classes are at or below 50%.

For any nonnegative additive portfolio, minimum legal-outcome gross cannot exceed average gross, and a mixture cannot beat the best component average. Therefore even under the full 50% bonus the strongest checked deposit-recovery upper bound is:

`1.5 * 50.60% = 75.90% < 100%`.

So the current Georgia bonus cannot create strict guaranteed cash profit from Cash 3 or Cash 4. This rejection is independent of cart limits, number cutoffs, taxes, or execution friction.

## NEXT ACTION
Do not repeat Georgia Cash 3/Cash 4 under the present 50% bonus. Continue outside H225 with a materially different externally funded/bounded mechanism. For a fixed-pay family with best rigorous average `r`, only prioritize deterministic subsidy multipliers greater than `1/r`; for Cash 3 specifically the subsidy would need to exceed about **97.63%** of deposit before execution details are even worth opening.

Files:
- `research/h288_georgia_cash3_cash4_bonus_bound.md`
- `research/H288_VALIDATION.md`
- `src/loto_research/h288_georgia_cash3_cash4_bonus_bound.py`
- `data/derived/h288_georgia_cash3_cash4_bonus_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H288_APPEND.md`
