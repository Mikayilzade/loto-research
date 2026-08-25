# H280 STATUS — New Hampshire 200% promo lead + Pick 3 exact cover

Updated: 2026-08-26
Branch: `research-work`
State: **CLOSED / OFFER+EXECUTION NOT CERTIFIED**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## Why this lead was tested

A current third-party promotion page (last verified Aug. 15, 2026) advertises code `NHMAX` for new New Hampshire iLottery players: **200% first-deposit match up to $100**, minimum $10, plus free games. This is materially stronger than H278/H279 subsidies and therefore deserved immediate exact-cover screening.

Official New Hampshire sources independently confirm:
- promotional Free Bonus Money and promo codes exist;
- cash prizes resulting from bonuses can be cashed out after at least one deposit;
- draw games can be bought through iLottery and the published minimum draw-game cart is $5;
- Pick 3 Front Pair pays **$50 on a $1 bet** and there are 100 possible front pairs.

## Exact conditional arithmetic

One-copy Front Pair cover:
- selections: 00 through 99 = **100** wagers;
- cost: **$100** at $1 each;
- exactly one Front Pair wins for every Pick 3 result;
- guaranteed prize if the whole cover is accepted: **$50**.

Under the advertised 200% match, a whole-dollar $34 first deposit would receive a conditional $68 bonus and create $102 wallet value. Buying the $100 full pair cover would then guarantee a $50 cash prize, i.e. **$16 strict cash profit / +47.0588% versus the $34 deposit**, conditional on the advertised offer and full-cover acceptance.

The arithmetic is probability-free and reproduced in:
- `src/loto_research/h280_nh_200pct_match_pick3_cover.py`
- `data/derived/h280_nh_200pct_match_pick3_cover.json`

## Why H280 is not SUCCESS

Two independent certification blockers remain and are strong enough to close this packet under the project guarantee standard.

### 1. Offer-specific authority blocker
The 200% `NHMAX` terms were found on a current third-party promotion page, not in an authoritative New Hampshire Lottery offer document. Official NH terms say promo codes/offers are discretionary, may be cancelled without notice, and each code has its own terms. Therefore the precise 200% entitlement, eligible game set, expiry, and playthrough conditions are not rigorously established from Lottery-controlled material.

### 2. Complete-acquisition blocker
Official NH iLottery purchase terms explicitly reserve the right to refuse any attempted purchase for any reason and to limit purchases of any game, ticket, and/or wager on a particular set of numbers at any time without notice. Thus public rules do not guarantee that all 100 pair wagers can be acquired for the same drawing. A partial cover has no deterministic positive floor.

These clauses mirror the decisive H279 execution issue and prevent a rigorous profitable-strategy claim even if the third-party offer description is accurate.

## Verdict

**H280 CLOSED as a strict-guarantee candidate under current public evidence.**

Reopen only if both conditions become bindingly established:
1. authoritative Lottery-controlled terms confirm the 200% match and permit its bonus to fund the target draw-game cover; and
2. a binding all-or-none reservation/acceptance mechanism guarantees the complete 00-99 cover despite general purchase-limit/refusal clauses.

## NEXT ACTION

Do not repeat Kentucky/New Hampshire ordinary iLottery cart-based Pick 3 subsidy constructions unless the acquisition-right problem changes. Continue toward mechanisms where the subsidized asset itself is finite/reservable or where the promotion grants a deterministic cash-equivalent after purchase, so no large all-number transaction must be guaranteed.
