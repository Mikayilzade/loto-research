# CHECKED_PROJECTS_AND_TESTS — H078 append

Updated: 2026-08-18

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H078 Baku e-scrap PCB pre-quote arbitrage** | broken motherboards/boards acquired only after recycler classification and fixed payout | Fors Group explicitly buys non-working PC/phone/appliance/industrial boards and pays immediately after evaluation; live/recent Baku broken motherboard inventory exists at **5 AZN**; ScrapTraffic/Metal Investment market anchor reaches ~**61 AZN/kg** | **LOCAL MECHANISM VALIDATED / EXACT BOARD WEIGHT+CATEGORY+BINDING BID NOT LOCKED / NOT SUCCESS**; `research/h078_baku_e_scrap_board_atomic_arbitrage.md` |
| H078 break-even sensitivity | 5-AZN board, zero friction | threshold **82 g at 61 AZN/kg**, 100 g at 50, 166.7 g at 30, 250 g at 20 | economics potentially viable; `data/derived/h078_baku_e_scrap_board_screen.csv` |
| H078 +3 AZN locked-cost sensitivity | 5-AZN board + 3 AZN total execution cost | threshold **131.1 g at 61 AZN/kg**, 160 g at 50, 266.7 g at 30 | potentially viable only after exact buyer-side weight/category |
| H078 strict execution gate | seller + recycler/buyer same-location or buyer inspection before seller payment | `locked buyer payout > ask + all locked costs`; exact board must be complete/eligible and lawful provenance retained | **REOPEN ONLY WITH TRANSACTION-LEVEL BID/WEIGHT; generic search closed** |

Sources:
- https://forsgroup.az/en/services/1-buying-different-kinds-of-circuit-boards.html
- https://scraptraffic.com/baku/elektronnyie-platyi
- https://tap.az/elanlar/elektronika/komputer-avadanliqi/45934643
- https://tap.az/elanlar/elektronika/komputer-avadanliqi/35129712
