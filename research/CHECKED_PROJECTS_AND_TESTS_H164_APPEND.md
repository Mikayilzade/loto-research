# H164 audit-ledger append — NC Pick 3 forced Double Draw retailer overlay

Updated: 2026-08-22
Terminal state after packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H164 NC Pick 3 Double Draw + retailer commission** | Wait for a forced Yellow-Ball state; cover all 100 ordered Pair outcomes at $0.50; add statutory/current-contract 7% retailer sales commission | $50 face spend; two guaranteed Pick-3 drawings each force one $25 Pair winner; prizes = **$50**. If own valid purchase is commission-bearing, 7% retailer commission = **$3.50**, conditional deterministic pre-tax total **$53.50 = 107%**, profit **+$3.50**. Retail Pick-3 cancellation is publicly allowed within **15 minutes** or before draw break, materially improving rollback versus NJ. | **PROMISING RECURRING DETERMINISTIC OVERLAY / NOT SUCCESS**. Latest 2026 promo ended July 31; no current forced state. Self-sale commission accounting is not explicit, rollback remains ticket-by-ticket rather than atomic under terminal outage, and after-tax floor is unresolved. `research/h164_nc_pick3_double_draw_retailer_overlay.md`, `src/loto_research/h164_nc_pick3_double_draw.py`, `data/derived/h164_nc_pick3_double_draw.csv` |

## New evidence preserved
- NC Lottery's 2026 Double Draw cycle was live in July 2026; official historical announcements explicitly identify evenings where two Pick-3 drawings are guaranteed because only the Yellow Ball remains.
- Current Pair prize table: $0.50 Pair costs $0.50 and pays $25 at odds 1:100.
- Exact forced-state identity: all 100 ordered Pair selections cost $50 and guarantee $25 per Pick-3 drawing; a guaranteed Double Draw therefore guarantees $50 prize gross.
- North Carolina statute G.S. 18C-142 and current NCEL retailer contract v. 05-27-2026 set retailer compensation at **7% of face value / retail price of tickets or shares sold by the retailer**.
- Official NCEL FAQ gives retail Pick-3 cancellation on the issuing terminal within **15 minutes of purchase or before draw break, whichever occurs first**.
- Public materials found no explicit blanket prohibition on an adult retailer owner personally purchasing tickets, but no explicit accounting sentence was found saying an owner-personal purchase remains commission-bearing sales.

## Reopen conditions / next proof steps
Reopen H164 immediately when Double Draw returns and the white-ball count approaches zero. Required proof gates:
1. current-cycle rules preserve the forced second-draw structure and pay normal prizes on both drawings;
2. NCEL retailer/accounting gives written confirmation that a retailer owner's own valid Pick-3 purchase counts in 7%-commission gross sales;
3. current terminal procedures establish reliable cancellation of all previously issued cover tickets after intervening transactions within the 15-minute window, or another pre-commitment/batch mechanism;
4. exact taxpayer/entity treatment leaves positive after-tax net profit.

Do not repeat generic Pair-cover arithmetic; it is exact and closed. Future work should target the four execution gates above.