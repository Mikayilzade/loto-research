# H066 — Azerbaijan vehicle-scrappage fixed-cash arbitrage screen

Updated: 2026-08-17
Status: **MECHANISM VALIDATED; executable positive all-in acquisition not yet locked**

## Goal
Test whether Azerbaijan's current vehicle-utilization program creates a fully controllable fixed-cash bounty that can exceed the all-in cost of acquiring an already-registered end-of-life vehicle.

This is materially stronger than lottery/promotional EV because the official program allows voluntary surrender of a vehicle regardless of technical condition and the one-time payment is fixed by vehicle class.

## Official mechanism
Primary official sources:
- Təmiz Şəhər FAQ / process: https://www.tamizshahar.az/az/neqliyyat/sual-cavab
- Təmiz Şəhər discount/payment table: https://www.tamizshahar.az/az/neqliyyat-utilizasiyasi/fond/guzest-ve-birdefelik-odenisler
- Təmiz Şəhər surrender process: https://www.tamizshahar.az/az/neqliyyat-utilizasiyasi/utilizasiyaya-verilme-prosesi
- Cabinet of Ministers Resolution No. 61 (31 Jan 2024): https://nk.gov.az/az/senedler/qerarlar/neqliyyat-vasitelerinin-utilizasiya-haqqinin-meble-7773
- Waste-law framework / payment right: https://frameworks.e-qanun.az/3/f_3186.html

Official facts relevant to a guarantee:
1. A person may voluntarily surrender a vehicle **at any time**.
2. **Any vehicle — new, old, crashed, fully serviceable, etc. — may be surrendered regardless of technical condition.**
3. Before surrender, the vehicle must be permanently removed from state registration.
4. Acceptance by a registered utilizer is in queue order and **free of charge**.
5. After acceptance, the utilizer issues one confirmation document per vehicle.
6. The confirmation document gives either a discount on a new locally produced vehicle or a **one-time payment equal to 70% of the class discount**.
7. The legal framework provides for payment from the Vehicle Utilization Fund to the document holder's account; the law states a 30-working-day transfer window after submission of the confirmation document.
8. The public FAQ/process does **not state a minimum ownership holding period** before voluntary surrender.

## Current fixed cash by class
Published discount schedule and 70% cash alternative imply:

| Class | discount AZN | one-time cash AZN |
|---|---:|---:|
| L | 200 | 140 |
| M1/M1G | 1,500 | **1,050** |
| N1/N1G | 1,500 | **1,050** |
| M2/M2G | 2,000 | 1,400 |
| N2/N2G | 2,000 | 1,400 |
| M3/M3G | 3,000 | 2,100 |
| N3/N3G | 3,000 | 2,100 |
| T/TK/TT | 2,000 | 1,400 |
| H/HT | 3,000 | 2,100 |
| HK | 3,000 | 2,100 |

For ordinary passenger cars (M1) the deterministic face payment is therefore **1,050 AZN per accepted vehicle**.

## Arbitrage theorem
For an acquired M1/N1 vehicle:

`net_floor = 1,050 - purchase_price - transfer_cost - registration/deregistration_cost - transport_cost - tax_cost - other_required_cost`

Strict terminal SUCCESS would require all components except `purchase_price` to be hard-bounded before purchase and the total to be **strictly below 1,050 AZN**, with entitlement legally locked.

A useful acquisition ceiling is:

`P_max = 1,050 - all_nonpurchase_costs - required_profit_margin`.

The mechanism is not random: once a legally transferable eligible vehicle is owned, deregistered, queued and accepted, the published one-time payment is fixed by class.

## Transaction-cost anchors
ASAN's current notarial page for transfer of a vehicle to an unrelated person shows:
- state duty: **70 AZN**;
- service charge: **10.50 AZN**.

Source: https://asan.gov.az/service/asan-xidmetler/notariat-fealiyyeti/eqdlerin-ve-etibarnamelerin-tesdiq-edilmesi/neqliyyat-vasitesinin-oezgeninkilesdirilmesine-dair-mueqavilenin-tesdiqi

This already reduces the M1/N1 acquisition ceiling from 1,050 to **969.50 AZN before** any registration certificate/plate, examination, transport, deregistration, tax or other costs.

The DYP registration rules require ownership changes to be re-registered and allow inspection at the vehicle location for an additional fee if technical condition prevents presentation. Therefore a non-running vehicle can be legally processed, but that extra service/transport cost must be included.

Source: https://dyp.gov.az/index.php?/az/content/194/

## Current market screen — evidence that the threshold is near real market supply
Public classifieds were searched for very low-priced registered/end-of-life vehicles.

### Sample 1 — Daewoo Damas 2007, 900 AZN
Tap listing observed at **900 AZN**. It describes an old non-running/problem vehicle, but states technical inspection/power-of-attorney/insurance have expired and that the owner has died, so title must be changed by the buyer. This is **not executable enough for a guarantee** without resolving inheritance/title.

Source: https://tap.az/elanlar/neqliyyat/avtomobiller/47867278

If it were cleanly transferable and classed M1/N1, face spread before transaction costs would be only:

`1,050 - 900 = 150 AZN`.

After the known 80.50-AZN unrelated-party notarial transfer cost, only **69.50 AZN** remains for every other cost. This is too thin to call a strict profit without exact DYP/deregistration/transport/tax bounds.

### Sample 2 — LADA 2106 listings around 1,000 AZN
Multiple classified examples around **1,000 AZN** exist, including shells/parts vehicles; several explicitly have no documents, while one current-looking 1,000-AZN shell listing says documents are in order. At 1,000 AZN the face spread is only 50 AZN, already less than the 80.50-AZN unrelated-party notarial transfer cost, so it fails even before other costs.

Representative source: https://tap.az/elanlar/neqliyyat/avtomobiller/47620075

### Important negative evidence
The search found cheap physical vehicles, but the very cheapest frequently have one of the exact defects that invalidate an arbitrage purchase: no documents, inability to re-register, deceased owner, or incomplete ownership chain. The bounty is therefore not equivalent to a free 1,050-AZN scrap-metal floor for any physical shell; **clean legal title is the scarce attribute**.

## No ownership-duration gate found in public rules
This is the strongest structural fact from this packet. The current Təmiz Şəhər FAQ says the person may surrender a vehicle at any time and lists deregistration, portal application, queue and delivery requirements, but does not publish a minimum ownership duration.

That keeps the buy-cheap-and-scrap idea alive in principle. However absence from the public FAQ is not enough to certify that every ownership-change edge case will be accepted operationally; the nvu/application and DYP steps must still be completed.

## Tax / repeated-business issue
A one-off disposal by an individual is not automatically equivalent to running a repeated scrappage-acquisition business. If the activity becomes systematic entrepreneurial trading, Azerbaijan tax registration/tax obligations can arise. The Tax Service notes, for vehicle retail activity, simplified tax can be 2% of gross receipts if that regime applies, or income tax under the applicable regime.

Source: https://taxes.gov.az/az/page/suallar-ve-cavablar?page=43

A terminal scalable strategy must therefore include the chosen legal/tax form rather than assuming repeated bounties are tax-free.

## Current conclusion
**H066 vehicle scrappage is the strongest controllable fixed-cash bounty found in the local idle-asset screen so far.** The payment mechanism itself is validated and does not depend on a lottery draw, biological success, customer demand, or resale.

But it is **NOT SUCCESS yet** because no currently purchasable vehicle has been simultaneously verified to satisfy all of:
- clean transferable title;
- correct eligible class;
- purchase price low enough;
- exact all-in transfer/re-registration/deregistration/transport/tax cost below the remaining spread;
- acceptance/queue operationally locked before irreversible capital commitment.

Current public sample at 900 AZN leaves at most 69.50 AZN after known notarial transfer cost and has a title defect. The 1,000-AZN clean-document shell is already negative after known notarial cost.

## Next test
1. Derive exact DYP ownership-change, certificate/plate and deregistration charges for a retained-plate vs new-plate path.
2. Determine whether a confirmation document/cash payment can be secured through seller-authorized surrender without a full ownership transfer, and who legally receives the payment. Do **not** assume this route.
3. Screen live listings specifically for **<=850 AZN, clean title, owner available, M1/N1**, preferably near an active utilizer to cap transport.
4. For any candidate, produce an all-in transaction sheet and require a positive margin after a conservative contingency reserve.
5. Confirm repeated-transaction tax treatment before scaling.
