# H287 STATUS

Updated: 2026-08-26
State: **CLOSED / REJECTED for tested mechanism**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Mechanism tested
Atlantic Lottery AL Rewards Promo Cash layered onto the current fixed-pay KENO Atlantic 2- through 10-Spot selection classes.

## Result
AL Rewards converts at 1,000 points = $1 Promo Cash. Using the published maximum 6 points per $1 as a player-favourable upper bound gives at most 0.6% extra playable balance. Promo-Cash-funded play earns no further points on that portion.

Exact hypergeometric recomputation of the current KENO Atlantic paytable finds the highest fixed-pay average at 7 Spot = 56.4211097144%. Including the full upper-bound Rewards rebate gives 56.7596363727%.

For the checked additive KENO class, minimum legal-outcome gross cannot exceed average gross, and mixtures cannot exceed the best component average. The tested mechanism therefore remains below break-even. The separate C$3m KENO prize cap was not needed for this rejection.

## NEXT ACTION
Do not reopen current AL Rewards + KENO unless the earning rate, redemption rate, or KENO paytable materially changes. Continue screening materially different externally funded, bounded, or hard-capped mechanisms identified by the global research plan.

Files:
- `research/h287_alc_rewards_keno_bound.md`
- `research/H287_VALIDATION.md`
- `src/loto_research/h287_alc_rewards_keno_bound.py`
- `data/derived/h287_alc_rewards_keno_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H287_APPEND.md`
