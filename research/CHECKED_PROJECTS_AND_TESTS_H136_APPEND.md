# CHECKED_PROJECTS_AND_TESTS — H136 append

Updated: 2026-08-21
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H136 Kentucky 100% first-deposit match + Pick 3** | deposit $250 -> $250 Bonus; buy all 1,000 distinct $0.50 Straight outcomes for one draw | $500 face coverage; exactly one Straight pays $300; external cash cost $250; **+$50 / +20% guaranteed pre-tax conditional on complete cover acceptance** | **MATHEMATICAL COVER INVERSION VALIDATED; TERMINAL GUARANTEE NOT PROVEN** because deposit is non-withdrawable before all required wagers are locked, operator terms allow purchase/number limits/refusal, and 2026 tax treatment is taxpayer-specific; `research/h136_kentucky_100pct_bonus_pick3_cover.md` |
| H136 Kentucky smaller Pair cover | cover 100 ordered pair outcomes at $0.50 using $25 cash + $25 Bonus | $50 face coverage -> guaranteed $30 payout -> **+$5 pre-tax conditional** | same pre-commitment/tax blockers; `data/derived/h136_kentucky_bonus_pick3_cover.csv` |
| H136 Wyoming Cowboy Draw BOGO control | historical/current-promo-class 100% BOGO applied to complete 5/45 coverage; count only deterministic lower tiers | effective cash cost $1,527,198.75 vs deterministic non-jackpot payout $850,000 = **55.6574%** | **REJECTED strict guarantee**; jackpot is shared and lower-tier floor cannot cover cost |

Terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.

Key new fact: H136 is the first current lottery packet where a live operator subsidy is large enough to make an exact fixed-prize full-cover portfolio positive **before tax and execution uncertainty**. Future subsidy scans should prioritize mechanisms that solve the remaining pre-commitment gate: refundable principal, atomic basket reservation, or guaranteed acceptance of every required selection before cash becomes irreversible.
