# Checked projects/tests append — H283

## Pennsylvania iLottery Refer A Friend + PICK covers

Status: **CLOSED / EXECUTION-BLOCKED**.

Checked 2026-08-26 against official Pennsylvania Lottery / Pennsylvania Bulletin sources.

### Positive arithmetic confirmed

Original PICK 3 lead:
- referred new player through unique referral link + code `FRIEND` + $10+ first deposit -> $100 Bonus Money under the checked offer;
- PA Bonus Policy permits Bonus Money on Draw Games;
- Draw Game prizes won with Bonus Money are cash regardless of unfinished bonus play-through;
- PICK 3 Front Pair has 100 ordered outcomes and current $1 prize $50;
- exact $1 Pair cover `00`-`99` costs $100 and has invariant $50 gross;
- conditional cash profit versus the $10 external deposit is exactly **+$40**.

Fresh PICK 2 refinement:
- online PICK 2 supports FRONT DIGIT / BACK DIGIT;
- each costs $1 and pays $5 on a 1-in-10 digit match;
- a complete ten-digit Front Digit cover costs $10 and guarantees $5;
- ten complete draw/position covers funded by the $100 bonus would therefore guarantee $50 cash, again **+$40** versus the $10 deposit.

### Decisive blocker

The governing base-game notices expressly reserve selective stop-play authority:

- PICK 3, Pennsylvania Bulletin 45 Pa.B. 386, section 7(d): the Lottery may stop play on any number or combination at any time during the PICK 3 game.
- PICK 2, Pennsylvania Bulletin 45 Pa.B. 384, section 7(d): the Lottery may stop play on any number or combination at any time during the PICK 2 game.

A strict cover theorem requires every required number class to be acquirable. The published stop-play authority preserves a legal execution path in which at least one required class cannot be acquired; an incomplete cover has a legal zero-return draw outcome. Therefore the conditional positive arithmetic is not a guaranteed-profit strategy.

Permanent closure record: `research/H283_EXECUTION_CLOSURE_2026-08-26.md`.

Do not duplicate H283 in a new packet or reopen it merely on better cart-size evidence. Reopen only if authoritative later rules remove/override the relevant stop-play authority, or if a materially different subsidy mechanism does not require complete acquisition of a stoppable number set.
