# H279 STATUS — Kentucky 100% match + Pick 3 exact cover

Updated: 2026-08-26
Branch: `research-work`
State: **PROMISING / ARITHMETIC STRICT-PROFIT / EXECUTION NOT YET CERTIFIED**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## New checkpoint

H279 found the first current deterministic subsidy combination in this lane whose exact-cover arithmetic crosses 100% of original cash.

Current Kentucky Lottery August 2026 promotion:
- eligible first-ever deposit receives a 100% Bonus match;
- match capped at $250;
- Bonus funds are valid for KLC games purchased online;
- prize winnings are tracked separately and may be withdrawn under the account terms.

Exact Pick 3 constructions:
- **Front Pair 00-99 cover:** 100 × $0.50 = $50 wallet. Deposit $25 + $25 matched Bonus. Exactly one pair wins $30 in every draw. Conditional strict profit = **+$5 = +20% on cash deposit**.
- **Straight 000-999 cover:** 1,000 × $0.50 = $500 wallet. Deposit $250 + $250 matched Bonus. Exactly one Straight wins $300. Conditional strict profit = **+$50 = +20% on cash deposit**.

The arithmetic does not depend on probabilities, jackpot size, sharing, or historical data.

## Why global SUCCESS is not yet claimed

Complete same-draw acquisition is not yet rigorously guaranteed:
- online play requires Kentucky eligibility and physical location;
- Pick 3 rules permit an undisclosed prize-liability cutoff that can stop sales;
- iLottery terms reserve the right to refuse attempted purchases;
- no atomic/pre-validated bulk mechanism guaranteeing acceptance of all 100 Pair lines (or 1,000 Straight lines) has yet been established.

A partial cover destroys the deterministic floor, so the project standard requires resolving this execution gate before promoting H279 to SUCCESS.

Files:
- `src/loto_research/h279_kentucky_100pct_match_pick3_cover.py`
- `data/derived/h279_kentucky_100pct_match_pick3_cover.json`
- `research/h279_kentucky_100pct_match_pick3_cover.md`
- `research/H279_VALIDATION.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H279_APPEND.md`

## NEXT ACTION

Prioritize H279 execution certification while the Aug 1-31, 2026 promotion is live:
1. determine exact online Pick 3 multi-selection/bulk purchase mechanics and per-ticket/per-transaction limits;
2. determine whether a complete 100-pair cover can be pre-validated/accepted atomically or whether liability cutoff can interrupt it;
3. if complete acquisition can be guaranteed for an eligible account, promote to rigorous SUCCESS and stop inventing further research;
4. otherwise close H279 as execution-blocked and continue to another deterministic subsidy >50% or equivalent guaranteed external-value mechanism.
