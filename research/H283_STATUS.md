# H283 STATUS — Pennsylvania referral Bonus Money + PICK 3 Pair cover

Updated: 2026-08-26
Branch: `research-work`
State: **PROMISING CONDITIONAL SUCCESS LEAD / EXECUTION GATE OPEN**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* was read first and remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## Current checkpoint

Current official PA iLottery Refer A Friend terms give a referred new player **$100 Bonus Money** after registration through a unique referral link, code `FRIEND`, and a first deposit of at least **$10**.

Current PA iLottery Bonus Policy allows Bonus Money to buy Plays, including Draw Games under the checked offer/policy combination, while Draw Game prizes are cash winnings rather than locked deposit funds.

Current PICK 3 rules give 100 ordered Front Pair outcomes. One $1 play on each `00`-`99` costs exactly **$100** and every draw has exactly one winning Front Pair paying **$50**. The official 2026 retailer terminal guide states the maximum value of a single PICK 3 ticket is exactly **$100**.

Therefore, if an eligible account receives the referral bonus and the online system accepts the complete 100-Pair cover for one draw:
- external cash deposit: **$10**;
- Bonus Money: **$100**;
- full cover spend: **$100**;
- guaranteed cash prize: **$50**;
- guaranteed cash profit vs external deposit: **+$40**;
- guaranteed cash gross multiple vs deposit: **5.0x**.

The $0.50 cover is also positive: $50 spend -> $25 guaranteed cash -> +$15 vs the $10 deposit.

## 2026-08-26 execution-verification advance

Fresh official checks materially strengthen the lead:
- PA iLottery Terms explicitly define Draw products as sold through the PA iLottery System and contemplate a purchase containing a chosen **number of Plays** and chosen **numbers/selections**; purchases are final once made.
- PA iLottery currently advertises all PICK Games for online purchase.
- Unlike the Kentucky/New Hampshire execution-blocked cases, the checked PA iLottery Terms do **not** contain a broad clause allowing the Lottery to selectively refuse an otherwise valid purchase merely because of the chosen number.
- Official 2026 retail PICK 3 documentation supports FRONT PAIR, ADD TO CART / BUY NOW and a maximum single PICK 3 ticket value of **$100**.
- However, official PA iLottery Help proves that online limits can be game-specific (for example, Powerball/Mega Millions are explicitly capped at five plays), so the absence of a published PICK 3 online cap cannot be treated as proof that 100 online Pair plays are accepted.

Detailed evidence is saved in `research/H283_EXECUTION_VERIFICATION_2026-08-26.md`.

## Why SUCCESS is still not declared

The remaining gate is execution, not arithmetic. Public official material still has not proved all of the following simultaneously:
1. an online PICK 3 transaction may contain at least **100 distinct Front Pair plays** for one drawing;
2. those 100 selections can be committed **atomically / all-or-none**, rather than as separately accepted purchases;
3. no hidden online-specific line/cart/payout-liability cap can stop the acquisition after only a strict subset has been accepted.

A partial Pair cover has no positive worst-case floor. Therefore the retail $100 ticket limit and the general online multi-play language are strong compatibility evidence but are not enough for a rigorous SUCCESS claim.

## Saved evidence

- `research/h283_pa_referral_pick3_pair.md`
- `research/H283_VALIDATION.md`
- `research/H283_EXECUTION_VERIFICATION_2026-08-26.md`
- `src/loto_research/h283_pa_referral_pick3_pair.py`
- `data/derived/h283_pa_referral_pick3_pair.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H283_APPEND.md`

## NEXT ACTION

Continue H283 execution verification before opening another broad packet:
1. locate an official PA iLottery PICK 3 online help/manual/UI source stating the per-transaction play count or cart limit;
2. seek official confirmation that one checkout can contain all 100 distinct $1 Front Pair selections for one drawing;
3. verify whether checkout is all-or-none and whether any unpublished number-liability/payout cap can partially block the set;
4. if complete acquisition is rigorously established while the referral offer remains current, elevate H283 to **SUCCESS for eligible Pennsylvania referred-new-player accounts**; otherwise record the exact execution blocker and continue the broader search.
