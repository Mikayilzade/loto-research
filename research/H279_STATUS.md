# H279 STATUS — Kentucky 100% match + Pick 3 exact cover

Updated: 2026-08-26
Branch: `research-work`
State: **CLOSED / EXECUTION-BLOCKED**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## Arithmetic result retained

H279 found a current deterministic subsidy combination whose exact-cover arithmetic crosses 100% of original cash, conditional on complete acquisition.

Kentucky Lottery August 2026 promotion:
- eligible first-ever deposit receives a 100% Bonus match;
- match capped at $250;
- Bonus funds are valid for KLC games purchased online;
- prize winnings are tracked separately and may be withdrawn under the account terms.

Exact Pick 3 constructions:
- **Front Pair 00-99 cover:** 100 × $0.50 = $50 wallet. Deposit $25 + $25 matched Bonus. Exactly one pair wins $30 in every draw. Conditional strict profit = **+$5 = +20% on cash deposit**.
- **Straight 000-999 cover:** 1,000 × $0.50 = $500 wallet. Deposit $250 + $250 matched Bonus. Exactly one Straight wins $300. Conditional strict profit = **+$50 = +20%**.

## Terminal blocker

The current Kentucky iLottery Terms of Use (effective June 2026 v12.1) expressly reserve the right to refuse attempted purchases and to limit purchases of a game and/or wagers on a particular set of numbers at any time without notice. Pick 3 rules separately permit undisclosed prize-liability cutoffs that can stop sales for a drawing.

Therefore the public rules do not guarantee that the full 00-99 pair cover will be accepted for one draw. A multi-selection cart does not override those restrictions, and a partially accepted cover loses the deterministic profit floor.

**H279 is therefore closed under the strict guarantee standard, despite favorable conditional arithmetic.** Reopen only on binding evidence of an all-or-none reservation/acceptance mechanism that overrides the current restriction/refusal clauses.

Files:
- `src/loto_research/h279_kentucky_100pct_match_pick3_cover.py`
- `data/derived/h279_kentucky_100pct_match_pick3_cover.json`
- `research/h279_kentucky_100pct_match_pick3_cover.md`
- `research/H279_VALIDATION.md`
- `research/H279_EXECUTION_CHECK.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H279_APPEND.md`

## NEXT ACTION

Continue outside H225 and H279. Prioritize deterministic subsidy >50% or equivalent external-value mechanisms, but require both exact-cover arithmetic and binding complete-acquisition execution. New Hampshire iLottery is a high-priority lead because a currently advertised third-party code claims a 200% deposit match and the official NH terms permit promotional Free Bonus Money and online draw-game purchases; authoritative offer-specific eligibility/game-use terms still need certification before any SUCCESS claim.
