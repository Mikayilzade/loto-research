# CHECKED_PROJECTS_AND_TESTS — H070 append

Updated: 2026-08-18

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H070 Azerbaijan interbank FX cross-arbitrage** | synchronized 31.07.2026 official-bank cash quotes; USD/EUR/GBP/RUB | best pre-fee round-trip gaps: USD **-0.294%**, EUR **-2.036%**, GBP **-2.974%**, RUB **-4.651%** | **VALID mechanism class; sampled synchronized state NEGATIVE**; `research/h070_azerbaijan_interbank_fx_cross_arbitrage.md` |
| H070 cashless screen | synchronized PAŞA Bank + AccessBank 31.07.2026 | USD **-0.294%**, EUR **-2.281%**, GBP **-2.278%**, RUB **-18.298%** before fees | **NEGATIVE sampled state**; `data/derived/h070_azerbaijan_fx_cross_screen_2026-07-31.csv` |
| H070 timestamp-control | compare non-synchronous indexed bank snapshots | stale dates can superficially create a positive RUB cross | **FALSE-POSITIVE CONTROL VALIDATED**; scanner forbids mixing date/channel buckets; `src/loto_research/fx_cross_arbitrage.py` |

Conclusion: no strict arbitrage in the synchronized sampled official-bank set. Reopen only with genuinely synchronized/live executable quotes or a bank/API feed that can lock both legs.
