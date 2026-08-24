# CHECKED_PROJECTS_AND_TESTS — H254 append

Date: 2026-08-24
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H254 Irish Christmas Millionaire Raffle** | Buy entire maximum 600,000-ticket finite inventory at €25/ticket and collect every guaranteed published prize | Spend **€15,000,000**; guaranteed prizes **€6,342,500**; deterministic gross **42.2833%**; deficit **€8,657,500** before friction | **REJECTED strict guarantee**; finite space is coverable in principle but prize pool is far below total acquisition cost; `research/h254_irish_guaranteed_raffle_capture_screen.md` |
| **H254 EuroMillions Ireland Only Raffle special draw** | Attempt to capture guaranteed extra €1m reserve-funded prize by covering raffle entries through EuroMillions line purchases | External €1m overlay is real, but market-wide IOR codes are generated across all purchasers and cannot be deterministically monopolized at bounded cost | **REJECTED strict guarantee under current execution structure**; `research/h254_irish_guaranteed_raffle_capture_screen.md` |
| **H254 Lotto Plus Million Euro Raffle** | Attempt to capture guaranteed extra €1m by owning all tickets eligible after winning raffle number is drawn | Overlay is real, but all tickets sharing the winning raffle number cannot be deterministically owned pre-draw and external eligible-entry count has no useful hard cap | **REJECTED strict guarantee under current execution structure**; `research/h254_irish_guaranteed_raffle_capture_screen.md` |

Reopen only on a finite purchasable inventory with guaranteed cash pool above total remaining cost, deterministic control of all eligible raffle identifiers, or a hard external-entry cap yielding a positive worst-case floor.
