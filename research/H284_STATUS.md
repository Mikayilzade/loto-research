# H284 STATUS

Updated: 2026-08-26
State: **CLOSED / REJECTED for tested mechanism**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Mechanism tested
Virginia Lottery Pick 3 fixed-pay additive portfolios combined with a currently advertised **50% first-deposit playable-balance match**.

## Terminal arithmetic
- Best exact base-game average gross ratio among published primitive wager types: **50%**.
- 50% deposit match creates at most **1.5×** playable balance.
- Therefore any nonnegative base-play mixture has worst-case cash recovery `<= average <= 1.5×0.50 = 75%` of original cash deposit.
- Deliberately generous FIREBALL stress: assume add-on gross ratio as high as **57%**; equal-stake base+FIREBALL blend then averages at most **53.5%**, or **80.25%** of original cash deposit after the match.
- Strict guaranteed cash profit therefore cannot be reached by this class.

## Why this is substantive
The result closes the whole tested additive primitive class by symmetry/linearity, not merely a single chosen cover. It also remains negative under a player-favorable FIREBALL ceiling and does not depend on execution/cart limits.

## NEXT ACTION
Do not revisit ordinary Virginia Pick 3 under a 50% match. Search for one of:
1. deterministic subsidy materially above the 100% match hurdle for a 50%-return fixed-pay class;
2. a fixed-pay game with worst-case/average cover ratio materially above 2/3 under a 50% subsidy;
3. deterministic withdrawable cashback or cash-equivalent reward outside wager-return symmetry;
4. hard-capped/reservable inventory whose guaranteed external prize liabilities exceed complete acquisition cost.

Files:
- `research/h284_virginia_pick3_50pct_match_bound.md`
- `research/H284_VALIDATION.md`
- `src/loto_research/h284_virginia_pick3_50pct_match_bound.py`
- `data/derived/h284_virginia_pick3_50pct_match_bound.json`
