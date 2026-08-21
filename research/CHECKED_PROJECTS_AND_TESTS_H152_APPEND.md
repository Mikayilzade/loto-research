# H152 audit append — Nebraska Quarter Mania cross-city + La Vista subsidy

Updated: 2026-08-21
Scope: LOTTERY ONLY
Terminal state after packet: **NO SUCCESS; NOT EXHAUSTED**

This append is an authoritative addition to `research/CHECKED_PROJECTS_AND_TESTS.md`.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| H152 Omaha Quarter Mania | H149 exact complete k-subset coverage, Pick 1-16, $0.25/way | best = Pick 1 **75.0000%**; Pick 2 66.1392%, Pick 3 63.8267% | **CLOSED below H151 benchmark**; `research/h152_nebraska_quarter_crosscity_and_lavista_subsidy.md` |
| H152 Lincoln Quarter Mania | H149 exact complete k-subset coverage, Pick 1-16, $0.25/way | best = Pick 1 **75.0000%**; Pick 2 72.1519%, Pick 3 69.3768% | **CLOSED below H151 benchmark**; same file |
| H152 La Vista current $5 free-play | grant full $5 cash-equivalent against H151 Quarter Madness Pick-2 full cover | $790 face -> $785 effective external cost; deterministic gross $617.50; net **-$167.50**; effective ratio **78.6624%** | **REJECTED as break-even subsidy**; current $5 covers only 0.6329% vs 21.8354% hurdle |
| H152 Big Red Keno app architecture | withdrawable Play+ balance + pre-start ticket void + saved-ticket reuse | execution architecture remains favorable if a future paytable/subsidy crosses 100% | **VALIDATED SUPPORTING MECHANISM, NO EDGE BY ITSELF** |

Reproducibility:
- `src/loto_research/h152_nebraska_quarter_crosscity.py`
- `data/derived/h152_nebraska_quarter_crosscity.csv`

Primary/current sources used:
- La Vista Quarter Madness: https://www.lavistakeno.com/quarter-madness
- La Vista events/free-play: https://www.lavistakeno.com/events
- Big Red Keno App FAQ: https://www.lavistakeno.com/frequentlyaskedquestions
- Omaha official paybook: https://bigredkeno.com/Content/Media/File/Document/Locations/omaha_paybook.pdf
- Lincoln official paybook: https://bigredkeno.com/Content/Media/Image/Paybooks/Lincoln/BRK_LincolnPaybook_06-19-2018.pdf

Important freshness note: Omaha/Lincoln paybook documents are official operator-hosted files but are not treated as proof of an August-2026 monthly special; they are exact cross-city fixed-paytable benchmarks only.
