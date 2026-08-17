# H067c — live titled-asset and execution-margin screen

Updated: 2026-08-17
Status: **near-face titled M1 shell found; strict positive floor not yet established; NO SUCCESS**

## Goal
Move H067 from mechanism proof to a concrete executable acquisition screen. Search for currently indexed private M1 assets with ownership/document signals at or below the 1,050-AZN one-time redemption value, then bound the visible transport leg.

## Fresh live result — documented M1 shell at 1,000 AZN
A current Tap.az listing indexed on 2026-08-17:
- LADA (VAZ) 2106, 1991;
- Bakı;
- asking price **1,000 AZN**;
- description: `Ideal kuza isdeyenler buyursun boş kuza verilir elave hecne yoxdu . senedler qaydasindadi`;
- listing page showed it as current on the search date.

Source:
- https://tap.az/elanlar/neqliyyat/avtomobiller/47620075

This is materially stronger than generic `boş kuza` search noise because it combines:
1. an M1 passenger-car identity;
2. explicit empty-shell condition;
3. explicit `sənədlər qaydasındadı` ownership/document signal;
4. asking price below the 1,050-AZN M1 cash redemption face.

It is **not yet a qualified arbitrage asset** because only the registered utilizer / NVU process can establish whether this exact incomplete vehicle is accepted and whether the seller has the required disposal authority.

## Incomplete-vehicle legal signal
The governing utilization law requires the acceptance act to record:
- the vehicle's general technical condition and completeness;
- vehicle identification information;
- **missing parts**.

That language is consistent with incomplete vehicles entering the acceptance workflow; however it does not prove that every empty shell is eligible. Vehicle identity, documents, deregistration and utilizer acceptance remain transaction gates.

Primary law:
- https://president.az/az/articles/view/60617

## Current transport-price floor
Fresh Bakı classifieds show tow/evacuation service advertised **from 20 AZN**, including services for disabled vehicles and, in one listing, dismantled vehicle bodies/shells.

Examples:
- https://tap.az/elanlar/xidmetler/logistika/47724993 — city service from 20 AZN;
- https://lalafo.az/baku/ads/evakuator-xidmti-id-110149993 — 20 AZN; description explicitly includes dismantled vehicle bodies.

This is a market quote floor, **not a hard route-specific quote** to Mashtaga/Hokmeli. Actual pickup-to-utilizer distance must be priced before execution.

## Economics of the 1,000-AZN shell
M1 one-time redemption face: **1,050 AZN**.

At 1,000 AZN acquisition:
- gross face spread: **50 AZN**;
- after an advertised 20-AZN minimum tow: **30 AZN** remains;
- deregistration/document/bank/tax/route-specific transport costs are still unbounded.

Therefore the current 1,000-AZN candidate does **not** satisfy terminal SUCCESS.

A practical acquisition ceiling under a 20-AZN tow floor is:

`P_max = 1,050 - 20 - other_cost_bound - required_profit_margin`.

Even before requiring a positive safety margin, if `other_cost_bound > 30 AZN`, a 1,000-AZN purchase cannot be a strict arbitrage.

## Important category control — cheap motorcycles are not the same opportunity
Current official Təmiz Şəhər rules set the utilization discount for category **L** (quadracycles / fewer than four wheels) at only **200 AZN**. The one-time cash payment is 70% of the category discount, i.e. **140 AZN**.

Thus numerous current 500–950 AZN documented motorcycles/mopeds found in the same search are economically irrelevant to the 1,050-AZN M1 thesis.

Official source:
- https://www.tamizshahar.az/az/neqliyyat-utilizasiyasi/fond/guzest-ve-birdefelik-odenisler
- current FAQ confirms one-time payment = 70% of category discount: https://www.tamizshahar.az/az/neqliyyat/sual-cavab

## Market benchmark reconfirmed
The previously identified Lalafo utilization intermediary ad remains indexed/current enough to preserve the strongest observed liquidity benchmark:
- `hemin gun 900m 1 ay 1050m`;
- asking/display 1,050 AZN;
- updated 2026-06-30.

Source:
- https://lalafo.az/baku/ads/sedan-avtomobil-kuzovu-skelet-id-73753310

This continues to show that a **150-AZN time/liquidity discount exists in the market**, but it is an intermediary service/offering, not a locked seller willing to transfer a post-issuance certificate to us for 900 AZN.

## Current execution threshold
For an M1 transaction to qualify as a strict positive-floor candidate, before any irreversible payment we need:
1. private ownership/disposal authority verified;
2. permanent deregistration eligibility verified;
3. registered utilizer confirms acceptance of the exact vehicle condition/identity;
4. fixed acquisition price payable only after certificate issuance;
5. route-specific tow quote locked;
6. all document/bank/tax costs hard-bounded;
7. `1,050 - all_costs > acquisition_price` by a strictly positive amount.

Given the current 1,000-AZN live shell, the remaining 50-AZN gross cushion is too narrow to certify.

## Decision
H067 remains open and remains the strongest deterministic-cash branch, but the current live asset screen does **not** reach SUCCESS.

Best next search target is now more precise:
- titled/private M1/N1 vehicle or shell;
- <= **900–950 AZN** preferably Bakı/Absheron;
- seller willing to use the issuance-contingent structure rather than requiring full pre-payment;
- exact utilizer acceptance and tow cost checked before payment.
