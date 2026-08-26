# H283 STATUS — Pennsylvania referral Bonus Money + PICK 3 Pair cover

Updated: 2026-08-26
Branch: `research-work`
State: **PROMISING CONDITIONAL SUCCESS LEAD / EXECUTION GATE OPEN**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* was read first and remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## New checkpoint

Current official PA iLottery Refer A Friend terms give a referred new player **$100 Bonus Money** after registration through a unique referral link, code `FRIEND`, and a first deposit of at least **$10**.

Current PA iLottery Bonus Policy explicitly allows Bonus Money to buy Draw Games and explicitly pays prizes won on Draw Games **in cash regardless of remaining play-through requirements**.

Current PICK 3 rules give 100 ordered Front Pair outcomes. One $1 play on each `00`-`99` costs exactly **$100** and every draw has exactly one winning Front Pair paying **$50**. The official 2026 retailer terminal guide states the maximum value of a single PICK 3 ticket is exactly **$100**.

Therefore, if an eligible account receives the referral bonus and the online system accepts the complete 100-Pair cover for one draw:
- external cash deposit: **$10**;
- Bonus Money: **$100**;
- full cover spend: **$100**;
- guaranteed cash prize: **$50**;
- guaranteed cash profit vs external deposit: **+$40**;
- guaranteed cash gross multiple vs deposit: **5.0x**.

The $0.50 cover is also positive: $50 spend -> $25 guaranteed cash -> +$15 vs the $10 deposit.

## Why SUCCESS is not yet declared

The remaining gate is execution, not arithmetic. Public official material has not yet proved that the PA iLottery **online** cart permits all 100 distinct Pair selections for one drawing to be committed as a complete/atomic transaction without an online-specific line/cart cap or partial acquisition risk. The retail $100 single-ticket limit is strongly compatible but is not sufficient proof of the online checkout behavior.

## Saved evidence

- `research/h283_pa_referral_pick3_pair.md`
- `research/H283_VALIDATION.md`
- `src/loto_research/h283_pa_referral_pick3_pair.py`
- `data/derived/h283_pa_referral_pick3_pair.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H283_APPEND.md`

## NEXT ACTION

Prioritize H283 execution verification before opening another broad lottery packet:
1. find official PA iLottery online Draw Games/cart documentation, screenshots, help/FAQ, or system rules establishing the maximum number/value of PICK 3 plays per online ticket/cart;
2. determine whether a $100 online PICK 3 ticket can contain the complete set of 100 distinct $1 Front Pair selections for one drawing;
3. check for any online number-liability, purchase-rejection, anti-opposite-betting, or promotion-specific clause that can selectively block the completed cover;
4. if complete acquisition is rigorously established while the referral offer remains current, elevate H283 to **SUCCESS for eligible Pennsylvania referred-new-player accounts**; otherwise record the exact blocker and continue.
