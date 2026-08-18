# CHECKED_PROJECTS_AND_TESTS — H073b append

Updated: 2026-08-18

This append is authoritative until the long master ledger is compacted/merged.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H073b Germany Pfand remote-executor bridge** | outsource purchase/inspection/redemption of 600-can live lot from Azerbaijan using a Germany task marketplace | current lot re-indexed at **600 × €0.25 = €150 face vs €30 ask** in **32584 Löhne**; Taskrabbit supports nearby Bielefeld plus shopping/errands/pickup; Co-Tasker offers competing local errand quotes; Western Union supports Germany→Azerbaijan transfer | **REMOTE INFRASTRUCTURE VALIDATED / exact quote not locked**; `research/h073b_remote_executor_bridge.md` |
| H073b bulk-redemption practicality | 600 units may be inconvenient for a supermarket | DPG current collector FAQ explicitly says larger quantities are generally accepted and a return time window can be coordinated | **BLOCKER MATERIALLY REDUCED** |
| H073b redemption cashability | concern that Pfand receipt might require new purchase | Verbraucherzentrale: refund is not tied to a purchase and store must pay the Pfand amount; same-branch voucher restrictions can be avoided by immediate redemption | **CASH REDEMPTION MECHANISM VALIDATED** |
| H073b strict remote floor | `profit_floor = 150 - 30 - E - T - X` | all-in executor+transfer+other cost <€120 yields positive pre-tax floor; €60 cap -> €60 floor, €90 cap -> €30 floor | **MECHANICALLY POSITIVE CONDITIONAL ON BINDING COSTS**; `data/derived/h073b_remote_executor_budget.csv` |
| H073b terminal gate | exact seller availability + fixed executor quote + inspection-before-buy + fixed transfer cost + assignment of redemption proceeds | no specific tasker quote or seller reconfirmation obtained in non-interactive research run | **NOT SUCCESS; now quote-level execution-gated rather than broadly geography-gated** |

Next H073 action only on interaction-level execution evidence. Do not repeat generic Pfand/task-platform searches.
