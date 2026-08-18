# H084 — current relay cash-price targeting

Updated: 2026-08-18
Status: **PROMISING SEARCH REFINEMENT / NOT SUCCESS**

## Goal
Turn H082 from a broad precious-metal-content search into a **model/passport buyer-price targeting screen**. The key question is no longer only “which relays contain valuable metals?” but “which exact markings have a currently published cash-buyer price high enough to justify hunting low-ask Azerbaijan inventory?”

## Fresh current buyer table
RadiodetaliPlus publishes a relay purchase table explicitly dated **18.08.2026**. This is not a Baku binding quote and therefore cannot itself prove an executable Azerbaijan trade, but it is useful as a current external price-discovery/ranking signal.

High-value entries recovered:

| Model / passport | Eligibility | Published buyer price, RUB/unit | Search priority |
|---|---|---:|---|
| ДП-12 902/903/906 | through 1990 | 6,384.10 | VERY HIGH |
| РЭС-22 unified 200–299 | through 1974 | 4,788.08 | VERY HIGH |
| РЭС-32 unified 354/355 | through 1982 | 3,830.46 | VERY HIGH |
| РПС-36 254/255/256/264 | through 12/1979 | 3,724.06 | VERY HIGH |
| РЭС-22 200–299 | through 1982 | 3,724.06 | VERY HIGH |
| РЭС-7 | all passports/years | 2,647.38 | HIGH / easiest identification |
| РЭС-8 050/051/052 | through 12/1966 | 2,470.89 | HIGH |
| РЭС-8 050/051/052 | through 12/1971 | 1,976.71 | HIGH |
| РПС-36 251/252/253 | through 1991 | 1,525.23 | MEDIUM-HIGH |
| РЭС-9 213/215/216/217/218 | through 1982 | 1,384.16 | MEDIUM-HIGH |
| РЭС-9 09/11/12/13/14 | 1982–1990 | 1,384.16 | MEDIUM-HIGH |
| РЭС-9 201/202/207/208 | through 1982 | 564.77 | MEDIUM |

Important asymmetry discovered: **passport matters enormously even within the same relay family**. Example: RES-9 entries range from only 55.88 RUB/unit for some later 01/02/06 passports to 1,384.16 RUB/unit for 213/215/216/217/218 or 09/11/12/13/14. A generic “RES-9” listing is therefore not enough.

## Local execution relevance
Fresh Azerbaijan web search still did not recover an indexed exact RES-7/RES-8/RES-9/RPS-36 seller listing with readable passport/year and fixed ask. Tap.Az does, however, currently show:
- a generic `Радиодетали` listing at **1 AZN** with multiple photos and varied prices;
- a `Radio detallar kondensatorlar` listing at **5 AZN** with many photos;
- an active Baku buyer/pickup listing explicitly accepting Soviet radio components, boards, starters, transistors, etc.;
- ScrapTraffic Baku explicitly lists RES-8, RES-9 and RPS-36 as platinum-bearing relay examples accepted by quote.

These listings are **lead pools**, not proven arbitrage. Search-index text does not expose enough markings from the photos to classify the pieces safely.

## New deterministic search rule
Do not buy a mixed lot because it “looks Soviet.” For every candidate:
1. identify exact model;
2. read passport code and production date from the body/photo;
3. map it to a current buyer-price row or a Baku model-specific quote;
4. require buyer-side classification/payout lock before seller payment;
5. require payout > ask + transport + prep/assay + tax/fees;
6. reject unknown or unreadable markings.

## Priority update
The best search order is now:
1. **DP-12 902/903/906**;
2. **RES-22 200–299 early production**;
3. **RES-32 354/355**;
4. **RPS-36 254/255/256/264 <=12/1979**;
5. **RES-7** (lower buyer value than top rows but simpler because all passports/years qualify in this buyer table);
6. early **RES-8 050/051/052**;
7. high-value **RES-9 passport subsets**, not generic RES-9.

This is a material refinement over H082, which prioritized mainly RES-7/early RES-8 by theoretical contained-metal value.

## Why this is not SUCCESS
The current price table is an external Russian buyer, not a binding local Baku payout. Cross-border shipment/payment legality, shipping cost, assay/reclassification and counterparty settlement risk prevent using it as a guaranteed exit. No exact Azerbaijan seller unit has yet been paired with a binding Baku buyer quote before purchase.

## Sources
- RadiodetaliPlus current relay purchase table, prices stated valid 18.08.2026: https://www.radiodetaliplus.ru/cennoct/rele-tsena.php
- ScrapTraffic Baku platinum/radio-component buyer page: https://scraptraffic.com/baku/platina
- Tap.Az current `Радиодетали` listing #46423754.
- Tap.Az current `Radio detallar kondensatorlar` listing #43791209.
- Tap.Az current `Radiotexnikaların utilizasiya xidməti` listing #34280223.

## Next move
Search Azerbaijan listings/images specifically for the new high-value markings above. First exact qualifying unit with fixed seller ask must then be paired with a **local binding buyer quote** before any irreversible payment. Do not repeat generic Soviet-component searches without readable markings.