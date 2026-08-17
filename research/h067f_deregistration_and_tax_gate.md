# H067f — deregistration-cost and tax gate

Updated: 2026-08-17
Status: **execution corridor materially narrowed; tax treatment is now the dominant unresolved gate**

## Goal
Tighten H067 from a market-price lead into a strict guaranteed-profit theorem by bounding mandatory legal/administrative leakage around Azerbaijan vehicle utilization confirmation documents.

## 1. Permanent deregistration before utilization — authoritative rule
The current `Yol hərəkəti haqqında` law, Article 27 IX-I, requires the vehicle to be removed from permanent state registration before it is given for utilization. The registration authority has 3 working days to decide and may refuse where there are unresolved confiscation orders, certain unpaid final fines, arrest/encumbrance, or missing public-sector write-off approval.

Primary source:
- https://frameworks.e-qanun.az/3/f_3423.html

The waste/utilization law separately confirms that utilization requires written information from the registration authority showing permanent deregistration.

Primary source:
- https://frameworks.e-qanun.az/3/f_3186.html

### Important execution implication
A cheap vehicle cannot be treated as a valid arbitrage input merely because it physically exists and has a low ask. The seller/authorized disposer must pass the Article 27 IX-I legal gate first. This supports the issuance-contingent transaction design already adopted in H067.

## 2. Utilizer acceptance itself is free
The utilization law states that registered utilizers accept vehicles in queue order **free of charge**. After the vehicle is accepted, the utilizer issues the confirmation document within 2 working days if the statutory documentation is complete.

Primary source:
- https://frameworks.e-qanun.az/3/f_3186.html

This closes one previously uncertain cost bucket: there is no statutory utilizer acceptance fee in the core law.

## 3. Deregistration state-fee evidence
The general State Duty Law and current Ministry of Internal Affairs fee pages enumerate fees for registration, technical inspection, plates and registration certificates. They do not expose a separate explicit line item for utilization-specific permanent deregistration in the material recovered in this run.

Sources:
- https://frameworks.e-qanun.az/2/f_2860.html
- https://mia.gov.az/az/menu/30077/
- https://mia.gov.az/az/menu/29771/3/

This is **not yet proof of a zero deregistration fee**. It is a bounded finding: no separate utilization-deregistration duty was located in the authoritative fee schedules searched. Until an authority explicitly confirms zero cost, H067 must retain a conservative administrative-fee reserve.

## 4. Confirmation-document economics reconfirmed
The current utilization framework gives one confirmation document per eligible vehicle. The document is valid for 3 years, single-use, **unnamed and usable by another person**. The official operator guidance says the holder can choose the one-time payment equal to 70% of the corresponding discount amount.

Sources:
- https://frameworks.e-qanun.az/3/f_3186.html
- https://tamizshahar.az/az/neqliyyat-utilizasiyasi/tesdiqedici-senedler-barede

For M1/M1G/N1/N1G, the already established one-time payment is 1,050 AZN.

## 5. NEW dominant gate — tax treatment
The current Azerbaijan Tax Code has a broad residual-income rule: resident income includes other income except exempt income, and annual non-business income is generally taxed at 14% unless a specific exemption applies.

Primary source:
- https://frameworks.e-qanun.az/46/f_46948.html

This run did **not** locate an explicit Tax Code exemption or an official State Tax Service clarification specifically naming the vehicle-utilization one-time payment.

Therefore two scenarios must now be separated:

### Scenario A — payment exempt / outside taxable income
`F_net = 1,050 AZN`.

Then a 900-AZN acquisition leaves 150 AZN before towing/admin/bank leakage, and H067 remains potentially executable.

### Scenario B — standard 14% non-business income tax applies
`F_net = 1,050 * 0.86 = 903 AZN`.

Then before any towing/admin costs:
- 900-AZN acquisition leaves only **3 AZN**;
- 850 leaves **53 AZN**;
- 800 leaves **103 AZN**.

Under this conservative tax scenario the previously preferred <=900–930 band is no longer sufficient. To preserve a 50-AZN safety margin plus even 20 AZN towing, acquisition would need to be approximately:

`P <= 903 - 20 - 50 = 833 AZN`

before any further mandatory leakage.

### Scientific status
Do **not** assert that the 14% tax definitely applies. The correct current conclusion is:
- no specific exemption was found in this run;
- standard 14% is a defensible worst-case stress scenario;
- strict SUCCESS requires authoritative product-specific tax treatment or pricing that remains profitable even under the 14% stress case.

## 6. Updated H067 execution threshold
Until tax treatment is resolved, use two search bands:

1. **Tax-cleared band**: <=900–930 AZN only if authoritative evidence establishes the 1,050-AZN payment is received without 14% income-tax leakage and residual fees are bounded.
2. **Tax-stress band**: target **<=800–830 AZN documented/deregisterable** M1/N1 or an already-issued unused certificate acquired at a price that leaves margin after a 903-AZN net redemption assumption.

This materially changes candidate ranking. An 800-AZN titled candidate could be interesting; an 800-AZN no-document candidate remains invalid; a 950-AZN candidate is no longer near-terminal unless tax exemption is proven.

## 7. Next exact proof targets
1. Official State Tax Service / operator clarification: is the one-time utilization payment taxable to an ordinary natural person, and if so who withholds/remits it?
2. Explicit authority on utilization-specific permanent-deregistration fee (zero or exact amount).
3. Fresh live titled/deregisterable M1/N1 candidates <=800–830 AZN under the tax-stress case.
4. Already-issued unused confirmation documents priced below 800–830 AZN.
5. Seller-side issuance-contingent agreement so no acquisition payment is irreversible before deregistration + official confirmation issuance.

## Current conclusion
**NO SUCCESS.** H067 remains the strongest deterministic-cash lead, but the strict execution corridor is narrower than previously recorded. Tax treatment can erase almost all of the 900–950 AZN spread, so no candidate in that range may be promoted to guaranteed profit until this gate is resolved.
