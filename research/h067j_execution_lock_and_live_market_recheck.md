# H067j — execution lock / pre-payment verification / live market recheck

Updated: 2026-08-18
Status: **mechanism remains promising; public pre-payment verification endpoint not found; live already-issued <=950 AZN certificate not found in indexed market**

## Goal
Close the remaining execution question for H067: can a buyer verify that a transferred scrappage confirmation document is valid, unused and accepted into the buyer's own cash-redemption workflow **before** making irreversible payment?

## Primary-source findings
### 1. Operator keeps the authoritative document workflow
Current Təmiz Şəhər material says confirmation documents are issued only by registered utilizers and that each document is valid for 3 years, single-use, unnamed, and usable by another person.

Source:
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/tesdiqedici-senedler-barede

### 2. Cash-redemption begins inside the applicant's own nvu.gov.az account
The current operator payment procedure says that for the 70% one-time payment the **person/applicant** must log in to the personal account on `nvu.gov.az`, choose the one-time-payment application and **add the information for the confirmation document(s) intended for use**. The applicant then presents the original confirmation document, ID and applicant bank-account details.

Source:
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/fond/tesdiqedici-senedler-uzre-odenisler

This is important because the buyer-side portal is the natural candidate for an atomic verification gate: if the transferred document's data can be added/recognized in the buyer's account before payment, it would materially reduce fake/used/expired-document risk.

### 3. No public anonymous status-check endpoint found
Fresh searches across `nvu.gov.az`, Təmiz Şəhər and indexed Azerbaijani web did **not** surface a public page/API where an unauthenticated user can enter certificate series/number and receive a validity/unused-status result.

Therefore we cannot claim that series/number alone is safely independently verifiable over the public web.

### 4. Operator procedure does not publish a promise to pre-validate a private sale
The official pages explain how to redeem a document, but do not expressly state that Təmiz Şəhər will give a private buyer a binding pre-purchase validity/unused-status confirmation or reserve/lock the document before the original is surrendered.

Therefore the strongest safe transaction sequence remains a proposed execution design, not yet a proven operator service.

## Best execution design currently supportable
Do **not** pay merely for a photographed certificate or seller assertion.

Preferred sequence:
1. seller presents the **original** strict-accountability confirmation document;
2. record series, number, issue date and category;
3. buyer attempts to add that document to the buyer's own `nvu.gov.az` one-time-payment workflow while seller is present;
4. if the portal rejects it, transaction stops with no payment;
5. if the portal recognizes it, obtain operator-side confirmation where possible that the document is current and unused;
6. exchange payment only against the physical original after steps 3–5;
7. immediately submit the one-time-payment application and original document under buyer identity/bank account;
8. retain written sale/assignment evidence and payment trace even though statute makes the document unnamed, to document acquisition basis and dispute/tax history.

### Critical distinction
Portal recognition would be a strong execution signal, but **until directly observed or documented by the operator it is not proven to be a final binding unused-status lock**. The document may theoretically still be redeemable/consumable by another workflow between recognition and final original submission. This residual race/settlement risk prevents terminal SUCCESS.

## Fresh live-market recheck
Fresh indexed search on 2026-08-18 covered Azerbaijani classifieds/search results for:
- `utilizasiya sənədi` / `təsdiqedici sənəd`;
- 850/900/950 AZN certificate-sale language;
- vehicle-utilization services and low-price titled assets.

### Market evidence still visible
A Lalafo listing (created 2025-10-31, updated 2026-06-30) advertises roughly:
- **900 AZN same day**;
- **1,050 AZN after one month**;
for utilization/body-shell intake service.

Source:
- https://lalafo.az/baku/ads/sedan-avtomobil-kuzovu-skelet-id-73753310

Interpretation: this continues to support a real private-market time-value spread around the statutory 1,050-AZN M1/N1 redemption value. It does **not** prove the seller offers an already-issued transferable unused confirmation document to a buyer for 900 AZN.

### No live indexed already-issued certificate <=950 AZN found
The fresh search did not surface a current listing explicitly offering an **already-issued, unused original confirmation document** at <=950 AZN. This is a market-liquidity/data result, not evidence such trades do not exist privately/off-index.

## Updated guarantee gate
H067 can become terminal SUCCESS only if one concrete transaction satisfies all of the following before irreversible payment:
- already-issued original document is physically present;
- category/redemption amount locked (e.g. M1/N1 = 1,050 AZN);
- 3-year validity confirmed;
- unused status confirmed by an operator/portal method strong enough to rely on;
- buyer/transferee cash workflow accepts the document;
- purchase price + all fees/tax worst case < fixed redemption amount;
- no race/void/clawback branch can reduce redemption below total locked cost;
- payment and document handover are atomic enough that buyer does not pay for an unusable instrument.

## Current economics
If tax exemption applies and total incidental execution cost is 20 AZN:
- purchase 900 -> 130 AZN floor before residual execution risk;
- purchase 950 -> 80 AZN;
- purchase 980 -> 50 AZN.

Because pre-payment unused-status locking is still not proven, these are **conditional economics**, not guaranteed-profit figures.

## Conclusion
H067 remains the strongest current deterministic-cash lead, but **H067j does not reach SUCCESS**.

New information from this packet:
- buyer-side `nvu.gov.az` document-entry step is confirmed by current operator procedure and is the most promising atomic verification gate;
- no public anonymous certificate-status checker was found;
- no official binding private-sale prevalidation/reservation promise was found;
- fresh indexed market search did not find an already-issued unused certificate <=950 AZN;
- the 900-now / 1,050-later private utilization listing remains evidence that the economic spread itself is real.

Next H067 action should be limited to genuinely new evidence: direct operator/portal behavior, a live already-issued certificate, or a written tax/operator clarification. Do not repeat broad indexed searches without a new source route.
