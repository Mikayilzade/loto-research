# H075 — Germany refundable gas-bottle deposit arbitrage

Updated: 2026-08-18
Status: **DETERMINISTIC REDEMPTION MECHANISM + LIVE SECONDARY-MARKET DISCOUNT VALIDATED / ACQUISITION-LEGALITY + LOCAL-EXECUTION GATES REMAIN / NOT SUCCESS**

## Question
Can an empty branded gas Pfandflasche be acquired on the secondary market for less than the issuer/dealer redemption amount and then returned for deterministic cash profit?

This is structurally different from ordinary commodity resale. The exit price is not a speculative market bid; it is a published deposit-return mechanism.

## Primary issuer evidence — WestfalenGas
Current WestfalenGas pages state:
- red propane, black Grillmeister and blue Conneo bottles are **Pfandflaschen**;
- the bottles remain property of Westfalen;
- an empty Westfalen Pfandflasche can be returned to a Westfalen dealer without taking a full bottle and the **Pfandbetrag is paid back**;
- the current return page gives approximate gross deposit guidance:
  - 5 kg red: **€26**;
  - 8 kg Grillmeister: **€40**;
  - 11 kg red Brenngas: **€30**;
  - 11 kg red Treibgas: **€30**;
  - 11 kg Conneo: **€30**;
  - 19 kg red: **€50**;
  - 33 kg red: **€68**;
- only Westfalen bottles can be returned to a Westfalen dealer;
- the published return instructions do not state a receipt requirement on the Westfalen return page.

Primary sources:
- https://westfalen.com/de/de/pfandrueckgabe
- https://westfalen.com/de/de/gase-energie/unsere-produkte/fluessiggas-propan/propan-in-gasflaschen-flexible-energie

OBI's current WestfalenGas 11 kg product page independently states that the empty Westfalen bottle can be returned for reimbursement of the deposit amount and that other suppliers' bottles are not accepted.

Source:
- https://www.obi.de/p/1899624/westfalengas-propan-fuellung-11-kg-pfandflasche-fuellung

## Live secondary-market evidence
Kleinanzeigen search results indexed in 2026 show a specific listing in **55767 Hattgenstein**:
- title: `Westfalen leere Flasche, Pfandflasche`;
- description: `Leere Westfalen Flasche 12,1 kg Nur Abholung`;
- observed ask: **€10** after reduction from €15 on one current index snapshot; another cached result still shows €15.

Source index:
- https://www.kleinanzeigen.de/s-haus-garten/sonstiges/pfandflaschen-abholung/k0c87

The same current marketplace also shows additional Westfalen-branded 11 kg and 19 kg empty Pfandflaschen, including current `VB` listings in Ahaus. This proves that a secondary market for the branded deposit bottles exists; those VB listings are not used for a numeric guaranteed-profit claim because the actual accepted price is unknown.

## Mechanical spread
For a confirmed 11 kg red Westfalen Pfandflasche:

`published_redeem ≈ €30`.

At €15 acquisition:

`gross_spread ≈ €15`.

At €10 acquisition:

`gross_spread ≈ €20`.

Strict transaction floor:

`profit_floor = locked_dealer_refund - seller_price - pickup/executor_cost - transport_cost - payment/remittance_cost - other_irreversible_costs`.

Therefore the Hattgenstein candidate becomes mechanically positive only if all irreversible execution costs are locked below roughly €15–€20, depending on actual seller price and exact dealer refund.

## Stronger features than ordinary resale
1. **Exit mechanism is issuer/dealer redemption**, not an uncertain resale bid.
2. Westfalen publishes a Germany-wide dealer network and says an empty bottle returned without replacement receives the deposit back.
3. The issuer publishes approximate refund amounts by bottle type.
4. Secondary-market asks can be materially below the published refund guidance.

## Why this is NOT terminal SUCCESS yet
### 1. Westfalen retains ownership
Westfalen explicitly says the Pfandflaschen remain its property. A private seller therefore appears to be transferring possession/use position rather than clean title to the physical bottle.

The public redemption page strongly suggests the current holder can return the bottle, but the project cannot call a private acquisition strictly guaranteed/legal without resolving whether buying a Westfalen-owned bottle from a third party creates any contractual/property-law problem or dealer refusal branch.

### 2. Published amounts are approximate
The official return page calls the listed Pfandsummen **Richtwerte** and says individual deviations can occur. A strict guarantee requires the exact receiving dealer to bind the cash refund for the exact bottle before irreversible purchase.

### 3. Local execution costs can consume the spread
The €10–€15 candidate is pickup-only. Remote execution therefore needs a local agent or seller-to-dealer handoff. A €15–€20 gross spread is much thinner than H073's €120 container spread.

### 4. Exact bottle identity/condition must be locked
Before seller payment, executor must verify:
- genuine Westfalen Pfandflasche, correct returnable type;
- not a grey Nutzungsflasche (those are not refunded);
- physically acceptable for dealer return;
- exact dealer acceptance and refund amount.

## Atomic execution design
A strict candidate should use a local Westfalen dealer and seller in one route:
1. identify exact bottle and seller price;
2. identify nearby Westfalen dealer accepting that bottle type;
3. obtain dealer confirmation of exact cash refund for that specific type/condition;
4. executor inspects bottle before seller payment;
5. ideally seller/executor meet at or near dealer;
6. buy only if `confirmed_refund - all_locked_costs - seller_price > 0`;
7. immediately redeem and settle executor/remittance.

## Current conclusion
H075 establishes another **real deterministic-redemption arbitrage class**. The numeric secondary-market anomaly is stronger than a theoretical lead: a Westfalen empty bottle has been indexed at **€10–15** against a published circa-€30 refund for an 11 kg red Pfandflasche.

However this is **not SUCCESS** because exact dealer refund is non-binding in the public table, ownership remains with Westfalen, and the small spread requires a local atomic execution with all costs locked.

### Reopen rule
Do not repeat generic searches. Reopen H075 only with one of:
- exact seller availability + exact accepted price;
- exact receiving Westfalen dealer confirmation for that bottle and exact payout;
- legal/contract evidence resolving third-party possession/acquisition;
- a higher-spread 19/33 kg Westfalen candidate with fixed price;
- an executor quote low enough to preserve a positive locked floor.
