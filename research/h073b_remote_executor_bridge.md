# H073b — remote-executor bridge for German Pfand arbitrage

Updated: 2026-08-18
Status: **GEOGRAPHY BLOCKER PARTIALLY REMOVED; EXACT EXECUTOR/TRANSFER QUOTE STILL UNLOCKED; NOT SUCCESS**

## Goal
Reopen H073 only with genuinely new execution evidence. The question is no longer whether German one-way deposit redemption works; that was already validated. The question here is whether a user in Azerbaijan can outsource the physical German leg while preserving a strictly positive worst-case cash floor.

## Live inventory refresh
A current Kleinanzeigen index again shows the exact title:
- `600 Bierpfanddosen leer mit Pfand`;
- seller text says all cans carry EUR 0.25 deposit and are not dented;
- ask: **EUR 30**;
- current indexed location: **32584 Loehne**.

Source:
- https://www.kleinanzeigen.de/s-pfand-dosen/k0

Mechanical face value:
`600 * EUR 0.25 = EUR 150`.

Gross spread before outsourced execution:
`EUR 150 - EUR 30 = EUR 120`.

Therefore an outsourced version remains strictly positive whenever all irreversible service, reimbursement, transfer and other fixed costs are locked below EUR 120.

## Redemption strengthened
Current Verbraucherzentrale guidance states:
- one-way deposit is EUR 0.25;
- retailers selling the same material must take qualifying containers back;
- refund is not conditional on a new purchase;
- the shop must pay the Pfand amount;
- even where a machine rejects damaged packaging, staff may have a manual-return duty if deposit eligibility remains identifiable.

DPG's current collector FAQ separately says that larger quantities are normally accepted and that a return time window can be coordinated with the retailer.

Sources:
- https://www.verbraucherzentrale.de/wissen/umwelt-haushalt/abfall/fragen-und-antworten-alles-zum-einwegpfand-und-dosenpfand-11505
- https://dpg-pfandsystem.de/de/faq-ruecknehmer.html

This reduces the earlier concern that a 600-unit lot might be practically unredeemable merely because of quantity.

## New remote-execution bridge
### Taskrabbit
Taskrabbit currently lists **Bielefeld** as an active service city and offers shopping, errands, pickup/delivery and personal-assistance tasks. Its Germany pages state that:
- clients can select taskers by price/reviews;
- same-day booking can be possible;
- shopping/pickup tasks are supported;
- where a Tasker pays for an item, expenses can be sent through the app;
- payment for the task occurs through the platform after completion.

Current sources:
- https://www.taskrabbit.de/locations/bielefeld
- https://www.taskrabbit.de/dienstleistungen/einkauf-lieferung
- https://www.taskrabbit.de/dienstleistungen/kontaktlose/lieferservice
- https://support.taskrabbit.com/hc/de/articles/46260499891355-Wie-viel-kostet-es-einen-Tasker-zu-buchen

Taskrabbit's own 2025 Germany price guide reports typical category prices and says Trust/Support fees are usually around 5–15% of task price, while exact hourly rates are visible before booking. This is useful for budgeting but is **not** an actual Loehne quote.

Source:
- https://www.taskrabbit.de/blog/wie-viel-kostet-es-einen-tasker-zu-beauftragen/

### Co-Tasker
Co-Tasker currently advertises errands, package pickup/drop-off and custom errands across Germany, including Bielefeld among supported cities. It explicitly lets the client post a task free, receive competing offers, set a budget, and reserve payment in a wallet until the task is completed.

Sources:
- https://de.co-tasker.com/errands
- https://de.co-tasker.com/how-it-works

This creates a second independent market for obtaining a fixed local-executor quote rather than relying on an informal friend.

## Cash repatriation bridge to Azerbaijan
Western Union Germany currently provides Germany -> Azerbaijan transfers, including bank account, cash pickup, mobile-wallet and debit-card receiving modes, and exposes fees/exchange rate before transfer.

Source:
- https://www.westernunion.com/de/de/send-money-to-azerbaijan.html

This removes the earlier conceptual blocker that the executor would have no formal route to return redeemed value to the Azerbaijan user. It does **not** yet lock the fee for this specific transaction.

## Nearby redemption infrastructure
Current local-business indexes show multiple full supermarkets in 32584 Loehne that sell/accept metal cans, including EDEKA/PENNY/Combi/Marktkauf-class stores. A final execution should identify one >200 m2 outlet and have the executor confirm bulk acceptance/time-window before purchase.

## Strict remote theorem
Let:
- `R = EUR 150` validated statutory refund;
- `P = EUR 30` seller price;
- `E = fixed tasker invoice + platform fees`;
- `T = locked Germany->Azerbaijan transfer cost`;
- `X = other irreversible fixed execution costs`.

Then:
`profit_floor = 150 - 30 - E - T - X`.

Strict success on this lot requires all of the following **before seller payment**:
1. seller confirms the 600-unit lot still exists at EUR 30;
2. tasker/executor accepts an all-in fixed maximum `E`;
3. executor inspects/counts units and verifies DPG/deposit markings before paying seller;
4. nearby qualifying retailer confirms return route, ideally a bulk-return time window;
5. transfer method and maximum `T` are known;
6. `E + T + X < EUR 120`;
7. contract/platform arrangement clearly assigns the EUR 150 redemption proceeds to the user and does not leave executor performance/payment discretionary after seller purchase.

A useful practical safety target is not merely EUR 119. For example, if all remote execution/transfer costs are capped at EUR 60, the pre-tax floor is EUR 60; at EUR 90 costs it is still EUR 30. Scenario table: `data/derived/h073b_remote_executor_budget.csv`.

## What changed this run
Before this packet, H073 was described as broadly geography-gated. That is now too pessimistic:
- live inventory is in Loehne;
- Bielefeld has established task marketplaces;
- supported task categories match pickup/purchase/errand work;
- a formal Germany-to-Azerbaijan payout channel exists;
- bulk Pfand return is explicitly contemplated by DPG.

So the remaining blocker is now **quote-level atomic execution**, not absence of infrastructure.

## Why this is still not terminal SUCCESS
No actual Taskrabbit/Co-Tasker offer for this exact Loehne task has been accepted, the marketplace seller has not been re-confirmed interactively, and transfer fees are not locked. Until those values are binding, the strict worst-case execution-cost bound required by PROJECT_RULES is not proven.

Status:
**MECHANISM VALIDATED / LIVE POSITIVE INVENTORY RECONFIRMED / REMOTE INFRASTRUCTURE VALIDATED / QUOTE-LEVEL EXECUTION UNLOCKED / NOT SUCCESS.**

## Reopen condition
Next H073 action should be interaction-level only: exact seller availability + fixed executor offer + fixed transfer cost. Do not repeat generic Pfand-law or task-market searches.
