# CHECKED_PROJECTS_AND_TESTS — H074 append

Updated: 2026-08-18

This append is authoritative until the long master ledger is compacted/merged.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H074 Baku local gold-scrap arbitrage** | buy second-hand gold only after independent buyer assays fineness/weight and issues binding immediate-cash bid | deterministic formula `floor = binding_bid - seller_price - locked_costs`; local buyers advertise free testing/weighing and immediate cash | **MECHANISM VALIDATED; atomic execution gate required**; `research/h074_baku_gold_scrap_arbitrage.md` |
| H074 Candidate A | current Lalafo 585 / 1 g listing at 128 AZN vs 2026-08-05 Baku 585 purchase reference 129.5 AZN/g | only +1.50 AZN gross reference spread | **REJECTED as too thin without higher binding bid** |
| H074 Candidate B | current Lalafo 585 bracelet rendered as `423 g` at 170 AZN; marketplace metadata appears to omit decimal separators in many jewellery weights | if true tested weight is 4.23 g and bid is 129.5 AZN/g, reference gross spread would be 377.785 AZN | **PROMISING LIVE ANOMALY, NOT VERIFIED** — weight/authenticity and exact transaction-time bid must be locked before payment |
| H074 terminal gate | three-party/assay-first transaction: seller price fixed, buyer tests exact item, payable net weight determined, buyer makes binding immediate-cash bid, costs capped, only then seller paid | neutralizes fake fineness, stones, hollow weight, stale market quote and post-purchase repricing | **NO SUCCESS YET because no exact candidate has all gates simultaneously locked** |

Next H074 action only on new execution evidence: exact unambiguous listing + seller accepts pre-payment assay + binding buyer bid after assay + positive all-in safety margin. Do not repeat generic spot-vs-listing scans.