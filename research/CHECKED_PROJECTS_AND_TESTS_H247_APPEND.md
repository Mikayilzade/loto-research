# CHECKED_PROJECTS_AND_TESTS — H247 append

Date: 2026-08-24
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H247 free Quick Pick / BOGO coverage subsidy** | Test whether current/recent operator promotions that issue free random Quick Pick tickets can reduce the deterministic paid line count needed for full combinatorial coverage | Exact worst-case theorem: uncontrolled free Quick Picks may all duplicate already-covered states and may all lose; guaranteed marginal coverage = **0**, guaranteed cash floor = **0**. For Millionaire for Life, guaranteed controlled paid coverage therefore remains **22,910,580 plays / $114,552,900**, not a 50%-discounted cover | **REJECTED strict controlled-coverage subsidy class**; active Aug. 2026 Kentucky Kroger offer gives two Cash Ball 225 Quick Picks after $10 MFL purchase; current Indiana MFL coupon is explicitly Quick Pick-only; `research/h247_free_quick_pick_coverage_gate.md` |

Reopen only if primary promotion rules give player-selectable free combinations or a deterministic non-duplicating assignment covering specified missing states.
