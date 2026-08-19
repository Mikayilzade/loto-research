# H094 — Azerbaijan export-cost compensation as deterministic subsidy

Updated: 2026-08-19
Status: **VALIDATED SUBSIDY MECHANISM / NOT STANDALONE GUARANTEE / RULES PENDING**

## Question
Can the new Azerbaijan SME export-support decrees create a strict positive cash floor by reimbursing export-related costs independently of sale outcome?

## Primary evidence
### Export customs-clearance compensation
Presidential Decree dated 2026-06-16 establishes compensation from the state budget for customs-clearance fees actually paid by micro, small and medium exporters when Azerbaijan-origin non-oil/gas goods are placed under the export customs procedure.

Key gates in the decree:
- exporter must be an SME;
- goods must be Azerbaijan-origin non-oil/gas goods, evidenced by certificate of origin;
- goods must actually be exported;
- compensation is paid after quarter-end on application;
- eligible goods/destination list, per-declaration cap, application rules and excluded transactions/persons are delegated for later normative acts;
- operative compensation provisions start 2026-09-01 and apply to qualifying export operations through 2031-09-30.

Primary source:
- https://president.az/az/articles/view/72749

### Transport-cost support
A separate 2026 presidential decree establishes state-budget support for transport costs of Azerbaijan-origin non-oil/gas exports. The published decree states that for rail, air, sea and Azerbaijan-registered road transport, the support amount is based on 70% of the qualifying transport cost paid cashlessly, subject to the product/destination/customs-value/transport-mode framework and implementing rules.

Primary source:
- https://president.az/az/articles/view/72713

## Deterministic accounting test
Let:
- `S` = cash sale proceeds irrevocably received from buyer;
- `G` = production/acquisition cost of exported qualifying goods;
- `T` = qualifying transport cost actually paid;
- `C` = qualifying customs-clearance fees actually paid;
- `R_T` = transport-support reimbursement;
- `R_C` = customs-clearance reimbursement;
- `O` = all other costs/taxes/fees.

Then:

`profit = S + R_T + R_C - G - T - C - O`.

The subsidies reduce `T` and `C`; they do not independently create a positive floor because both are reimbursements conditional on a real qualifying export and actual prior cost. A standalone loop with no profitable sale still requires:

`S - G - (T-R_T) - (C-R_C) - O > 0`.

Therefore the support is an **overlay**, not a self-contained arbitrage.

## Why this still matters
This is one of the strongest deterministic local overlays found so far because:
- it is statutory/state-budget backed rather than discretionary marketing cashback;
- it applies to real economic activity rather than chance;
- the transport-support percentage can be large enough to change the sign of marginal export trades;
- it creates a screenable future strategy: find a buyer with a binding prepaid/escrowed purchase contract where normal trade margin is slightly negative before subsidy but strictly positive after all published support and costs.

## Current execution blocker
As of 2026-08-19, the customs-clearance compensation starts only on 2026-09-01 and the delegated lists/caps/application/exclusion rules have not yet been found published in indexed official sources. Exact guaranteed-floor economics cannot be certified before those rules are available.

The transport-support decree is current policy evidence, but exact product/destination caps and the full implementing payment mechanics must be locked for any transaction-level guarantee.

## Reopen condition
Reopen H094 only when at least one of the following is available:
1. final official eligible-goods/destinations/cap/application rules;
2. a concrete Azerbaijan SME export transaction with binding buyer price, origin certificate eligibility, all-in production/acquisition cost, transport quote, customs fees and support amount;
3. a prepaid/escrowed sale where buyer payment is irreversible before support-triggering costs are incurred.

## Conclusion
**No terminal SUCCESS.** The new support is a real deterministic cost-offset class, but not a standalone guaranteed-profit strategy. It becomes strategically important only as an overlay on a separately locked export sale.
