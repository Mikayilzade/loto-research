# H295 VALIDATION

Validated: 2026-08-26
Packet: H295

## Arithmetic checks
- Shopping raffle cap: 500.
- Shopping raffle ticket price: $50.
- Full acquisition cost: 500 × 50 = **$25,000**.
- Advertised prize: **$10,000**.
- Gross ratio: 10,000 / 25,000 = **0.4 = 40%**.

Mercedes favorable-value gate:
- advertised ticket price: **$10**;
- advertised MSRP: **$50,605**;
- largest integer N satisfying 50,605 > 10N is **5,060**;
- N=5,061 costs $50,610 and fails even before taxes or resale friction.

These identities are duplicated as executable assertions in `src/loto_research/h295_hollydays_raffle_takeover_gate.py` and recorded in `data/derived/h295_hollydays_raffle_takeover_gate.json`.

## Evidence checks
The 2026 official Hollydays/registration material checked this pass publishes the two raffle products, Shopping Spree prize/price, Mercedes price/MSRP, event date, emailed raffle ticket-number mechanism, and winner tax responsibility. No public hard maximum for Mercedes entries or guaranteed cash alternative was found in those current materials.

## Claim discipline
H295 does **not** infer a Mercedes cap from the existence of ticket numbers. It does **not** treat MSRP as withdrawable cash. It does **not** claim full acquisition is executable. Therefore no guaranteed-profit conclusion is asserted.

Validation state: **PASS — rejection/data-block conclusion is supported; SUCCESS is not supported.**
