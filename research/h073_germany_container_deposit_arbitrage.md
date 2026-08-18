# H073 — Germany mandatory container-deposit arbitrage

Updated: 2026-08-18
Status: **DETERMINISTIC REDEMPTION MECHANISM + LIVE BELOW-FACE OFFERS FOUND; REMOTE EXECUTION INFRASTRUCTURE NOW VALIDATED, EXACT QUOTE STILL GATED; NOT TERMINAL SUCCESS**

## Question
Can legally acquired empty German one-way beverage containers be bought below their mandatory deposit value and redeemed for a strictly positive cash floor?

## Current legal anchor
Germany replaced the old VerpackG with the Verpackungsrecht-Durchführungsgesetz (VerpackDG) effective 2026-08-12. Current §46 preserves the key mechanism:
- qualifying one-way beverage packaging carries a deposit of at least **€0.25 per unit**;
- distributors must take back emptied qualifying packaging and refund the deposit;
- the return duty is material-based for ordinary retailers, with the brand limitation applying to shops under 200 m².

Sources:
- current-law transition / old law repeal: https://www.gesetze-im-internet.de/verpackg/BJNR223410017.html
- current §46 text mirror / enactment reference: https://www.umwelt-online.de/regelwerk/abfall/verpack.vo/verpackdg26.htm
- DPG consumer FAQ: https://dpg-pfandsystem.de/en/faq-consumer-questions-environment.html
- BMUKN system explanation: https://www.bundesumweltministerium.de/faq/was-passiert-mit-pfand-das-nicht-eingeloest-wird-dem-sogenannten-pfandschlupf

DPG states that marked one-way packaging can be returned irrespective of where it was originally purchased, subject to the material/retailer rules. A clearly visible DPG marking matters; missing markings or foreign containers can fail eligibility.

## Strict mechanical condition
For `N` valid €0.25 containers acquired for purchase price `P`, with all irreversible execution costs `C`, the deterministic pre-tax cash floor is:

`profit_floor = 0.25*N - P - C`.

A strict positive floor therefore requires:

`P + C < 0.25*N`.

The important difference from lottery coverage is that the terminal cash receipt is not random once each container is validated as a qualifying redeemable unit.

## Live below-face marketplace evidence
Current Kleinanzeigen search results expose unusually strong offers.

### Offer A — 600 empty deposit cans for €30
Search result text:
- **“600 Bierpfanddosen leer mit Pfand”**;
- seller states all cans have **€0.25 deposit** and are **not dented**;
- ask **€30**.

Nominal refund:
- `600 * €0.25 = €150`.

Gross deterministic spread before execution/tax:
- `€150 - €30 = €120`;
- purchase is only **20% of face redemption value**;
- break-even all-in execution-cost budget = **€120**.

Marketplace source:
- https://www.kleinanzeigen.de/s-pfand-dosen/k0

### Offer B — 300 cans, stated deposit value €75, ask €48
Current search results also show:
- **“300 Dosen Pfand (Wert 75 €) zu verkaufen”**;
- 300 Red Bull/Coke Zero cans;
- stated deposit value **€75**;
- ask **€48**.

Gross spread before execution/tax:
- `€75 - €48 = €27`.

This independently confirms a live marketplace class where sellers value convenience/storage removal more than the full redemption amount.

## Pre-payment lock protocol required for a strict instance
Do **not** pay on description alone. Before irreversible payment:
1. inspect/count the lot in person;
2. verify every unit is empty and carries a clear German DPG/deposit marking;
3. exclude foreign-deposit, missing-label and materially damaged units;
4. identify a nearby >200 m² retailer selling metal one-way beverage packaging, so brand matching is not the limiting rule;
5. set a hard all-in incremental transport/execution budget below the observed spread;
6. only then pay and redeem.

The German consumer centre notes that dented containers or missing labels can cause practical refusal, so inspection is part of the entitlement lock rather than an optional quality check.

## Tax gate
The refund itself is a return of the statutory deposit, but systematic buy-below-face activity could create taxable profit depending on facts. German §22(3) has a €256 annual de-minimis threshold for certain miscellaneous service income, but this does **not** by itself classify deposit arbitrage. Therefore no blanket zero-tax assumption is made.

For Offer A, even a deliberately harsh 45% tax applied to the €120 spread would leave €66 before execution costs, so a local low-cost execution can remain positive. Product-specific tax classification would still be needed before scaling/repeating.

## H073b remote-executor bridge — 2026-08-18
New research removes most of the earlier conceptual geography blocker:
- the 600-can / €30 listing is now indexed in **32584 Löhne**;
- Taskrabbit currently supports nearby **Bielefeld** and explicitly offers shopping, errands and pickup/delivery tasks;
- Co-Tasker offers the same class of custom errands and lets clients receive fixed offers;
- DPG explicitly contemplates coordinated return of larger quantities;
- Western Union currently supports Germany → Azerbaijan transfers.

Full execution analysis:
- `research/h073b_remote_executor_bridge.md`
- `data/derived/h073b_remote_executor_budget.csv`

For this lot the remote theorem is:
`profit_floor = 150 - 30 - executor_cost - transfer_cost - other_locked_costs`.

Thus a strict positive remote result exists if every irreversible remote cost is contractually fixed below **€120** before seller payment. For example, a €60 all-in execution/transfer cap leaves a €60 pre-tax floor; a €90 cap leaves €30.

What is **not** yet locked is the exact seller availability, an exact executor quote for Löhne, and the exact transfer charge. Accordingly H073 has advanced from broad geography-gated to **quote-level execution-gated**, but not to terminal SUCCESS.

## Why this is not terminal SUCCESS for the current project
The live mechanism is much stronger than earlier execution-gated redemption leads. A formal remote execution route now exists in principle, but no specific tasker/Co-Tasker offer and no final remittance fee have been made binding for this exact lot. PROJECT_RULES requires those numbers to be locked before irreversible payment.

Therefore:
- **mechanism:** validated;
- **live below-face inventory:** validated;
- **remote execution infrastructure:** validated;
- **local/remote conditional arbitrage:** mechanically positive if pre-payment inspection + cost caps are satisfied;
- **strict executable setup for the user from Azerbaijan:** not yet quote-locked;
- **terminal SUCCESS:** not claimed.

## Reopen / advance condition
Advance H073 only on interaction-level evidence:
1. seller confirms exact inventory/price;
2. executor gives a fixed all-in quote and accepts inspect-before-buy protocol;
3. transfer cost is fixed;
4. total locked cost remains below face value, with a positive safety floor.

Do not repeat generic Pfand-law, generic marketplace or generic task-platform searches.
