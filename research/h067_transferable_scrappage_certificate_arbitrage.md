# H067 — Azerbaijan transferable vehicle-scrappage certificate arbitrage

Updated: 2026-08-17
Status: **MECHANISM MUCH STRONGER THAN H066; fixed-cash bearer-like claim validated, but no live below-redemption certificate acquisition locked**

## Discovery
The vehicle-utilization confirmation document (`təsdiqedici sənəd`) is not merely a benefit tied to the original vehicle owner.

Primary law / operator sources:
- Waste law, Article 14-8: https://frameworks.e-qanun.az/3/f_3186.html
- Təmiz Şəhər — confirmation documents: https://tamizshahar.az/az/neqliyyat-utilizasiyasi/tesdiqedici-senedler-barede
- Təmiz Şəhər — payments: https://tamizshahar.az/az/neqliyyat-utilizasiyasi/fond/tesdiqedici-senedler-uzre-odenisler
- Təmiz Şəhər — surrender process: https://tamizshahar.az/az/neqliyyat-utilizasiyasi/utilizasiyaya-verilme-prosesi

The law states that the confirmation document:
1. is valid for 3 years;
2. is usable once;
3. is **unnamed (`adsızdır`)**;
4. **may be used by another person**;
5. may be presented for the alternative one-time cash payment;
6. results in the operator transferring the cash to the account of the **person presenting the confirmation document** within 30 working days.

The operator's current public instructions independently state that the applicant for the one-time payment submits the confirmation document, ID and the applicant's own bank details.

This changes the economics materially. The relevant asset can be the confirmation document itself rather than the underlying vehicle.

## Fixed cash redemption values
Current one-time payment = 70% of the class discount:
- M1/M1G, N1/N1G: **1,050 AZN**;
- M2/M2G, N2/N2G, T/TK/TT: **1,400 AZN**;
- M3/M3G, N3/N3G, H/HT/HK: **2,100 AZN**;
- L class: 140 AZN.

## Direct certificate-arbitrage theorem
Let:
- `R` = fixed one-time redemption amount encoded by a valid unused certificate;
- `P` = purchase price paid for that certificate;
- `C` = all verification, contract, banking, tax and execution costs;
- `M` = required strictly positive margin.

Then a terminal cash arbitrage exists if, before paying `P`, we can irrevocably verify that the document is authentic, unused, transferable and redeemable, and:

`P + C + M < R`.

For an M1/N1 certificate:

`P_max = 1,050 - C - M`.

Unlike H066 vehicle acquisition, this route has no vehicle purchase, ownership-change registration, plate, physical inspection, towing or deregistration expense after acquisition of the already-issued certificate.

## Why this can satisfy the project guarantee criterion in principle
Once a valid unused certificate is acquired below redemption value and the operator's statutory payment obligation is applicable, there is no lottery draw, resale market, biological event, sports result or consumer demand branch. The cash amount is fixed by class and the law directs payment to the presenter within the statutory window.

Therefore H067 is a genuine **deterministic-cash arbitrage class**, not merely positive EV.

## Remaining pre-commitment gates
A terminal SUCCESS still requires a concrete transaction proving all of:
1. a currently valid certificate is offered at `P < R - C`;
2. authenticity and unused status can be checked before irreversible payment;
3. no portal/account binding prevents the buyer from adding/using an acquired unnamed certificate;
4. the particular certificate is not one of the state-owned/state-surrender exceptions whose cash goes to the state budget;
5. transfer/sale of the unnamed certificate is not contractually prohibited by another applicable rule;
6. payment can be made to the buyer/presenter bank account as the public operator instructions state;
7. taxes/fees on acquisition or redemption do not erase the spread;
8. seller cannot consume/revoke the certificate after verification/payment (atomic handover or equivalent control required).

## Current market search
Fresh public web searches on 2026-08-17 for Azerbaijani/Russian phrases equivalent to `utilization confirmation document for sale`, `utilization certificate for sale`, and combinations with the 1,050-AZN cash amount did **not** return a concrete current secondary-market listing.

This is absence of indexed evidence, not evidence that no private market exists. A document holder can already obtain 70% cash directly, so a seller would rationally accept a discount mainly for liquidity/time/convenience. Any profitable spread is therefore likely to be modest unless the holder does not understand the cash alternative or values immediate liquidity strongly.

## Seller-authorized surrender route (important fallback)
The waste law also permits a person other than the owner to surrender the vehicle when that person has a power of disposition. Current ASAN pricing for a disposal power of attorney to a non-relative is:
- state duty 30 AZN;
- service fee 4.50 AZN;
- total **34.50 AZN**.

The surrender process accepts such authority. The certificate is issued to the person who surrendered the vehicle, and the certificate is unnamed/transferable.

Therefore a possible structure is:
1. owner grants valid power of disposition;
2. vehicle is deregistered for utilization;
3. authorized person surrenders it and receives the confirmation document;
4. seller payment is contractually contingent on successful certificate issuance;
5. certificate holder redeems fixed cash.

This route can avoid the H066 unrelated-party title-transfer cost stack. It is **not yet terminal SUCCESS** because no live owner has agreed to an enforceable contingent-price transaction and transport/deregistration/compliance costs for a concrete vehicle remain unbounded.

## H066b cost correction / refinement
Current law also improves the ordinary title-transfer model:
- registration plate is normally retained with the vehicle when it is transferred, so a new standard plate fee is not automatically required;
- for passenger cars over 10 years old and <=2,000 cc, the ownership-transfer registration duty is `engine_cc * 0.05 * 0.3` under current state-duty rules;
- current registration certificate fee is 30 AZN;
- technical inspection associated with changes in technical-accounting data / buyer-request inspection is 30 AZN;
- unrelated-party notarial transfer remains 80.50 AZN.

Example for a >10-year-old 1,300 cc M1 car, before transport and any other required item:
- notary: 80.50;
- registration duty: 19.50;
- certificate: 30;
- inspection: 30;
- standard retained plate: 0 incremental plate fee;
- subtotal: **160.00 AZN**.

Thus a 900-AZN vehicle already reaches **1,060 AZN** before transport/other costs and cannot beat a 1,050-AZN M1 cash payment through ordinary ownership transfer. The direct-certificate or authorized-surrender route is therefore economically much more important.

## Current conclusion
**H067 is now the strongest deterministic-cash mechanism in the project.** The law creates a transferable, unnamed, fixed-redemption claim. A verified unused M1/N1 document bought for less than 1,050 AZN minus all transaction costs would produce a deterministic positive cash spread.

However no live current certificate offered below redemption value has been located and atomically verified. Therefore: **NO SUCCESS; NOT EXHAUSTED**.

## Next test
1. Search non-indexed/local channels and classifieds for live unused confirmation documents.
2. Determine whether `nvu.gov.az` exposes a pre-purchase certificate validity/unused-status check by serial number.
3. Recover the current certificate form / serial structure and exact operator verification flow.
4. Search for clean owner-authorized end-of-life vehicles where payment can be made only after certificate issuance, avoiding title transfer.
5. Build an atomic transaction checklist; claim SUCCESS only after a concrete certificate/vehicle path has a strictly positive all-in locked spread.
