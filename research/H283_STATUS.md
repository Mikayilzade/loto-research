# H283 STATUS — Pennsylvania referral Bonus Money + PICK covers

Updated: 2026-08-26
Branch: `research-work`
State: **CLOSED / EXECUTION-BLOCKED**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* was read first and remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## Terminal H283 result

The positive subsidy arithmetic is real but cannot be promoted to a strict guarantee under the published Pennsylvania game rules.

For the original PICK 3 construction:
- eligible referred new player: $10 first deposit -> $100 Bonus Money under the checked offer;
- Bonus Money may fund Draw Games and Draw Game winnings are cash under the checked Bonus Policy;
- 100 ordered $1 Front Pair plays `00`-`99` cost $100 and a completed full cover guarantees exactly one $50 Pair prize;
- conditional profit versus the $10 external deposit is therefore +$40.

However the governing PICK 3 game notice, Pennsylvania Bulletin 45 Pa.B. 386, section 7(d), expressly states that the Lottery may **stop play on any number or combination of numbers at any time during the course of the PICK 3 game**.

That authority is a decisive execution blocker. A strict guarantee needs every required Pair selection to be acquired. If even one required pair can legally be stopped before complete acquisition, an incomplete cover remains possible and has a legal draw outcome with zero Pair return. Therefore neither a large cart nor atomic checkout semantics alone can establish rigorous SUCCESS.

## Fresh lower-line-count test — PICK 2 Digit cover

The same run tested whether PICK 2 could remove the 100-selection problem.

Current official PA material supports online PICK 2, FRONT DIGIT / BACK DIGIT, $1 per play, and a $5 prize at 1-in-10 odds. A complete ten-digit Front Digit cover costs $10 and guarantees $5. In arithmetic terms the $100 referral bonus could fund ten complete draw/position covers and guarantee $50 cash, again +$40 versus the $10 external deposit.

But the governing PICK 2 notice, Pennsylvania Bulletin 45 Pa.B. 384, section 7(d), contains the same explicit right to **stop play on any number or combination of numbers at any time**. The smaller ten-selection cover is therefore still not guaranteed executable.

## Closure consequence

H283 is now **CLOSED / EXECUTION-BLOCKED** for both checked Pennsylvania PICK 3 Pair and PICK 2 Digit referral-bonus covers.

Do not reopen H283 merely because an online cart is shown to support 100 plays, $100+ purchases, or multi-play checkout. Reopen only if:
- an authoritative later rule removes/overrides the relevant stop-play authority; or
- a materially different Pennsylvania subsidy construction avoids dependence on complete acquisition of a stoppable number set.

## Permanent records

- `research/h283_pa_referral_pick3_pair.md`
- `research/H283_VALIDATION.md`
- `research/H283_EXECUTION_VERIFICATION_2026-08-26.md`
- `research/H283_EXECUTION_CLOSURE_2026-08-26.md`
- `src/loto_research/h283_pa_referral_pick3_pair.py`
- `data/derived/h283_pa_referral_pick3_pair.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H283_APPEND.md`

## NEXT ACTION

Resume the global lottery search outside H225-X* and outside H283. Highest-priority mechanisms remain deterministic external subsidy/cashback or hard-capped/reservable inventory where a strict positive floor does **not** depend on completing a number set that the operator can legally stop, refuse or selectively limit.
