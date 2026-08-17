# H067e — live execution thresholds and fresh market screen

Updated: 2026-08-17
Status: **PROMISING MECHANISM; NO SUCCESS — no live candidate yet clears document + all-in positive-floor gates simultaneously**

## Purpose
Move H067 from legal/mechanism proof toward a strict executable cash-floor test. The terminal condition is not merely `vehicle ask < 1,050 AZN`; it is a pre-locked transaction where every mandatory cost is bounded and the certificate/payment route is legally usable.

## Fresh market evidence checked 2026-08-17

### 1. Utilization-market liquidity / time-value signal
A currently indexed Lalafo listing in Bakı advertises vehicle-body utilization acceptance with the wording:

`hemin gun 900m 1 ay 1050m`

The listing is priced/displayed at 1,050 AZN and was updated 2026-06-30.

Source:
- https://lalafo.az/baku/ads/sedan-avtomobil-kuzovu-skelet-id-73753310

Conservative interpretation: this is **evidence of an active private market that values immediate realization around 900 AZN versus waiting for the official 1,050-AZN face**, not proof that the advertiser will buy an already-issued certificate under our exact terms. It supports liquidity and a roughly 150-AZN observed time/processing spread, but must not be treated as a guaranteed exit quote without counterparty confirmation.

### 2. Cheaper current vehicle candidate fails the document gate
A Tap.az LADA (VAZ) 2106, 1991 listing is indexed at **800 AZN** in Bakı, but the description explicitly says:

`Seneti yoxdu`

Source:
- https://tap.az/elanlar/neqliyyat/avtomobiller/45618711

Because permanent deregistration and utilization require ownership/disposal authority plus written deregistration information, a vehicle explicitly advertised without documents cannot be counted as an executable H067 asset without a separate recoverable-title route. Therefore the 800-AZN headline does **not** establish a 250-AZN guaranteed spread.

### 3. Parts/body listings are not automatically eligible vehicles
Fresh searches also return 700-AZN VAZ parts/body listings. These cannot be promoted into H067 candidates merely because the utilization act may record missing parts. Eligibility still requires a registered vehicle identity, owner/disposal authority and permanent deregistration. Parts inventory without a qualifying registered-vehicle legal identity is outside the proven route.

## Primary legal controls reconfirmed
Current statutory/official sources establish:
- before utilization, the vehicle must be permanently removed from state registration;
- registered-utilizer acceptance itself is free;
- the acceptance act records technical condition, completeness and missing parts;
- after acceptance the confirmation document is issued within two working days;
- the confirmation document is valid for three years, single-use, unnamed and usable by another person;
- its holder may elect the one-time payment equal to 70% of the category discount;
- for M1/M1G and N1/N1G the current one-time-payment face used in this project is **1,050 AZN**.

Primary sources:
- https://president.az/az/articles/view/60617
- https://president.az/az/articles/view/60613
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/tesdiqedici-senedler-barede
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/fond/tesdiqedici-senedler-uzre-odenisler
- https://tamizshahar.az/az/neqliyyat/sual-cavab

## Exact transaction thresholds
Let:
- `F = 1,050` AZN official M1/N1 one-time-payment face;
- `P = acquisition or post-issuance certificate-transfer price`;
- `T = unavoidable towing/transport cost borne by us`;
- `D = unavoidable deregistration/document cost borne by us`;
- `B = bank/payment charges borne by us`;
- `X = tax or other mandatory cash leakage borne by us`.

Strict cash floor:

`profit_floor = F - P - T - D - B - X`

SUCCESS requires a **hard pre-transaction proof** that:

`profit_floor > 0`

and all legal/eligibility gates are locked before irreversible payment.

### If the previous 20-AZN Bakı tow floor is achievable
- `P=950`, `T=20` leaves only **80 AZN** for all `D+B+X` and safety margin.
- A 25-AZN safety margin means `D+B+X <=55`.
- A 50-AZN safety margin means `D+B+X <=30`.

Thus the live 950-AZN candidate is economically thin. It is not enough to prove that statutory utilizer acceptance is free; the full owner-side deregistration and redemption leakage must be bounded.

### Stronger acquisition targets
With `T=20` and a desired 50-AZN safety margin:
- if `D+B+X <=30`, maximum `P = 950`;
- if `D+B+X <=50`, maximum `P = 930`;
- if `D+B+X <=80`, maximum `P = 900`.

Therefore **<=900 AZN with valid title/disposal authority** is the preferred live-asset search band unless authoritative research proves near-zero remaining mandatory costs.

## New decision rule for marketplace screening
Reject immediately if any of these is true:
1. listing explicitly says no documents / `sənəti yoxdur`;
2. only parts/body are sold with no evidence of registered-vehicle identity;
3. seller cannot permanently deregister for utilization;
4. arrest/encumbrance/final unpaid disqualifying obligations prevent deregistration;
5. seller demands irreversible payment before certificate issuance/verification and the vehicle route cannot independently clear a conservative all-in floor;
6. locked cost sum makes `1,050 - all costs <= 0`.

Promote to executable-candidate only when:
1. owner/disposal authority is verified;
2. VIN/chassis/identity data are usable;
3. deregistration eligibility is verified;
4. utilizer queue/acceptance path is available;
5. total costs are contractually/officially bounded;
6. original unused certificate is transferred atomically or we ourselves are the lawful holder after completion;
7. strict cash floor remains positive with a safety margin.

## Result
The fresh screen did **not** produce terminal SUCCESS.

Meaningful progress:
- active private-market evidence continues to support a roughly **900 AZN immediate-value** zone for the utilization process;
- a cheaper **800 AZN** vehicle exists but explicitly fails the documents gate, confirming why raw marketplace price alone is insufficient;
- the economic search target is now sharper: **documented, deregisterable M1/N1 <=900–930 AZN is materially stronger**, while 950 AZN remains viable only if remaining mandatory leakage is proven very low.

## Next H067 packet
1. authoritative utilization-specific permanent-deregistration state-fee search;
2. tax treatment of the one-time utilization payment for a natural person;
3. fresh market search specifically for `sənəti var`, `çıxdaş`, `utilizasiya`, `boş kuza` candidates <=900–930 AZN;
4. already-issued unused confirmation-document listings / explicit post-issuance transfer offers.
