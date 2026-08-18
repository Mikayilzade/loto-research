# H076 — zero-cost salvage -> deterministic scrap-cash arbitrage

Updated: 2026-08-18
Status: **MECHANISM VALIDATED / LIVE FREE INVENTORY VALIDATED / REMOTE EXECUTION NOT LOCKED / NOT SUCCESS**

## Goal
Test a new deterministic edge class outside lotteries: acquire legally transferable scrap/salvage for zero or very low price and immediately redeem/sell it to a buyer with a published fixed or weight-based cash bid.

This differs from ordinary resale because the exit value can be mechanically tied to material category/weight rather than finding a discretionary end-buyer.

Strict execution formula:

`profit_floor = locked_scrap_cash_bid - acquisition_price - pickup/transport/executor/payment/other_locked_costs`

A strict SUCCESS requires all variables to be locked before any irreversible spend and `profit_floor > 0`.

## Germany starter-battery control
### Live zero/low-cost supply exists
Kleinanzeigen currently indexes multiple old/defective car batteries offered free or near-free. Examples observed in the current search window include:
- defective starter batteries offered **zu verschenken** (free);
- three old car batteries offered free in one listing;
- old batteries commonly listed around EUR 5–10 each.

Sources:
- https://www.kleinanzeigen.de/s-zu-verschenken/autobatterie-auto/k0c192
- https://www.kleinanzeigen.de/s-defekte-autobatterie/k0
- https://www.kleinanzeigen.de/s-alte-auto-batterien/k0

### Published cash exits exist
A.V.M. Autoverwertung Meermann publishes a current Vechta buy price of **EUR 5 per car battery** for delivery to its yard (price page updated 2026-06-27). It also publishes EUR 0.30/kg for battery lead above 200 kg.

Source:
- https://avm-autoverwertung.de/pages/tagespreise-schrott-buntmetall

Schrott24 independently publishes current lead-battery buy prices starting around **EUR 0.30/kg from 50 kg**, rising with volume, while noting that lead batteries cannot be sent by ordinary parcel and that pickup service starts only at larger quantities.

Source:
- https://www.schrott24.de/altmetall-ankauf/blei/blei-batterien-aus-kfz-und-maschinen/

This validates a real conversion mechanism from zero-cost transferable salvage to positive cash value.

## Why the German statutory EUR 7.50 battery deposit is NOT a free extra arbitrage
Germany's current BattDG section 19 requires a EUR 7.50 starter-battery deposit when a dealer sells a new starter battery without simultaneous old-battery return. The dealer that collected the deposit is obligated to refund it on return of an old starter battery; distance sellers may refund against a recent return certificate.

Therefore a random used battery bought/free-collected from a third party does **not** by itself create an independent EUR 7.50 statutory claim against arbitrary dealers. The deposit refund is tied to the dealer/deposit transaction (and may depend on a deposit token or proof).

Primary law:
- https://www.gesetze-im-internet.de/battdg/__19.html
- https://www.gesetze-im-internet.de/battdg/__18.html

Conclusion: do not double-count statutory Pfand and scrap cash.

## Live economics screen
Examples demonstrate positive **gross** salvage value:
- acquisition EUR 0 + published scrap exit EUR 5 -> gross spread EUR 5 per qualifying battery;
- three free batteries -> gross EUR 15 if all qualify and can be delivered to a EUR 5/battery buyer;
- acquisition EUR 5 + EUR 5 fixed exit -> zero gross spread before execution and therefore rejected;
- larger batches can use weight-based bids, but transport/hazardous-goods handling becomes the dominant gate.

## Execution blocker
For a user located in Azerbaijan, the German candidates are not yet strict executable arbitrage because:
1. free/cheap batteries are local-pickup inventory;
2. lead batteries are heavy and regulated for transport;
3. ordinary parcel shipment is not allowed by the checked scrap buyer;
4. no specific local executor has been contractually locked at a cost below the scrap spread;
5. scrap-yard price pages reserve normal market/acceptance conditions and exact item eligibility must be confirmed before acquisition.

A single free battery with a EUR 5 exit is far too thin for remote execution. The class becomes more interesting only with a dense local batch, free pickup route, or an executor already traveling between seller and scrap buyer.

## Strategic result
H076 validates a broad deterministic class:

**zero-cost salvage + precommitted material buyer can create guaranteed gross value without predicting markets.**

But the current live German battery instances are **not terminal SUCCESS** for this project because the positive net floor after execution has not been locked.

### Reopen conditions
Reopen H076 only with one of:
- a geographically co-located free batch and published/binding buyer bid;
- a local executor quote below the full batch spread;
- Azerbaijan-local free salvage plus binding local scrap buyer quote;
- a higher-value material class (copper, catalytic cores, electric motors, alloy wheels, etc.) where the spread comfortably dominates logistics;
- seller-side free delivery to the accepting buyer or executor.

## Sources checked
- German BattDG sections 18–19 (official federal law)
- A.V.M. Autoverwertung Meermann current scrap price page
- Schrott24 lead-battery buy-price page
- Kleinanzeigen current free/old/defective battery indexes
