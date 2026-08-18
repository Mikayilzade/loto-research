# CHECKED_PROJECTS_AND_TESTS — H084 append

Updated: 2026-08-18
Terminal state after this packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H084 Soviet relay current cash-price targeting** | Replace theoretical-metal ranking with a current model/passport buyer-price screen dated 18.08.2026 | highest published external buyer rows: DP-12 902/903/906 **6384.10 RUB/u**; RES-22 early **4788.08**; RES-32 354/355 **3830.46**; RPS-36 254/255/256/264 **3724.06**; RES-7 **2647.38**; early RES-8 **2470.89/1976.71** | **PROMISING SEARCH REFINEMENT / NOT SUCCESS**; external buyer table is not a binding Baku exit; `research/h084_current_relay_cash_price_targeting.md` |
| H084 passport sensitivity | compare prices within same relay family | RES-9 ranges from **55.88 RUB/u** for some later 01/02/06 to **1384.16 RUB/u** for high-value passport subsets; generic model-name search is unsafe | **VALIDATED: exact passport/year required**; `data/derived/h084_current_relay_cash_price_targets.csv` |
| H084 Azerbaijan live inventory screen | exact searches for RES-7/8/9, RPS-36 plus current mixed Soviet-radio-part listings | no indexed exact seller unit with readable qualifying passport/year + fixed ask recovered; mixed Tap.Az lots exist at 1 AZN / 5 AZN starting asks but markings are not index-readable | **EXECUTION-GATED**; reopen on exact marked unit + local binding buyer quote before payment |

Rule carried forward: prioritize **DP-12 → RES-22 → RES-32 → RPS-36 early → RES-7 → early RES-8 → only high-value RES-9 passports**. Do not repeat generic Soviet-relay searches without readable markings or a new buyer quote.