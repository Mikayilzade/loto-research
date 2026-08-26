# H283 STATUS — Pennsylvania referral Bonus Money + PICK 3 Pair cover

Updated: 2026-08-26
Branch: `research-work`
State: **PROMISING CONDITIONAL SUCCESS LEAD / EXECUTION GATE OPEN**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* was read first and remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## Current checkpoint

Current official PA iLottery Refer A Friend terms give a referred new player **$100 Bonus Money** after registration through a unique referral link, code `FRIEND`, and a first deposit of at least **$10**.

Current PA iLottery Bonus Policy allows Bonus Money to wager on Draw Games and explicitly states that prizes won on Draw Games with Bonus Money are paid in cash regardless of remaining play-through on the Bonus Money used.

Current PICK 3 rules give 100 ordered Front Pair outcomes. One $1 play on each `00`-`99` costs exactly **$100** and every draw has exactly one winning Front Pair paying **$50**.

Therefore, if an eligible account receives the referral bonus and the online system accepts the complete 100-Pair cover for one draw:
- external cash deposit: **$10**;
- Bonus Money: **$100**;
- full cover spend: **$100**;
- guaranteed cash prize: **$50**;
- guaranteed cash profit vs external deposit: **+$40**;
- guaranteed cash gross multiple vs deposit: **5.0x**.

The $0.50 cover is also positive: $50 spend -> $25 guaranteed cash -> +$15 vs the $10 deposit.

## 2026-08-26 execution-verification checkpoint

Fresh official evidence now establishes more of the execution chain:

1. PA iLottery Help explicitly says PICK 3 is playable online and lists FRONT PAIR as a supported play type.
2. Current binding PA iLottery Terms describe one purchase as containing a **number of Plays**, the price of the Play(s), and the **numbers/selections chosen on any Play**; initiating that purchase authorizes deduction of the cost of that purchase, and completed sales are final.
3. An official PA iLottery online-promotion rule explicitly had a PICK 3 wagering tier for **$100.00 or more**, proving that $100+ online PICK 3 wagering is contemplated by official rules, although not proving it occurs in one transaction.
4. Current 2026 retail PICK 3 documentation supports FRONT PAIR, ADD TO CART / BUY NOW and a **$100 maximum single PICK 3 ticket value**.
5. Current PA iLottery Terms still do not show a Kentucky/NH-style blanket right to reject a valid purchase merely because of selected numbers. Explicit refusal language located is tied to invalid geolocation/eligibility conditions.
6. Official PA Help also proves online play caps can be game-specific (Powerball/Mega Millions: five plays), so the absence of a published PICK 3 online cap cannot be converted into a 100-play assumption.

The detailed evidence matrix is in `research/H283_EXECUTION_VERIFICATION_2026-08-26.md`.

## Why SUCCESS is still not declared

The remaining gate is now very narrow and entirely operational. Public official material still has not proved all of the following simultaneously:

1. one online PICK 3 purchase may contain at least **100 distinct Front Pair plays for the same drawing**;
2. those 100 selections are committed **atomically / all-or-none**, rather than being separately accepted purchases;
3. no online-specific line/cart/payout-liability control can stop the acquisition after only a strict subset has been accepted.

A partial Pair cover has a legal zero-return draw outcome. Therefore the strong retail limit, the binding multi-play purchase language, and the historical $100+ online-wager evidence are not yet enough for a rigorous SUCCESS claim.

## Saved evidence

- `research/h283_pa_referral_pick3_pair.md`
- `research/H283_VALIDATION.md`
- `research/H283_EXECUTION_VERIFICATION_2026-08-26.md`
- `src/loto_research/h283_pa_referral_pick3_pair.py`
- `data/derived/h283_pa_referral_pick3_pair.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H283_APPEND.md`

## NEXT ACTION

Stay on H283 before opening another broad packet. Highest-value closure evidence is a current authoritative PA iLottery source or support confirmation that:
- one PICK 3 online checkout can hold **100 distinct $1 Front Pair selections for one drawing**; and
- checkout completion is all-or-none (a failed/rejected checkout cannot leave an unknowable partial subset purchased).

If that is rigorously established while the referral offer remains current, elevate H283 to **SUCCESS for eligible Pennsylvania referred-new-player accounts**. If official evidence instead reveals a lower online play/cart/liability limit or sequential partial acceptance, close H283 as execution-blocked and resume the global search.
