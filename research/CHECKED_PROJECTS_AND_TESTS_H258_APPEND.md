# CHECKED_PROJECTS_AND_TESTS — H258 append

Date: 2026-08-24
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H258 EuroMillions €250m cap flow-down** | Distinguish ordinary cap overflow flow-down from terminal no-jackpot roll-down; test complete 5/50+2/12 cover under the legal branch with exactly one external 5+2 duplicate; grant our portfolio the entire current-draw 50% prize allocation as a dominating upper bound | Full cover costs **€349,595,400**. One external 5+2 duplicate caps our jackpot share at **€125m**. Even adding **all €174,797,701.25** of current-draw prize money from our cover + that external line yields only **€299,797,701.25 = 85.7556%**, net **-€49,797,698.75** | **REJECTED strict guaranteed-profit full coverage**. Mechanism nuance validated: cap overflow can flow to rank 2 even when rank 1 has a winner, so H002b's terminal roll-down incompatibility does not eliminate this branch; nevertheless one legal external jackpot duplicate is decisive. `research/h258_euromillions_cap_flowdown_external_duplicate_bound.md` |

Reopen only with an execution-grade hard exclusion/bound on external 5+2 duplicates or a separately guaranteed non-shared subsidy large enough to survive that branch.
