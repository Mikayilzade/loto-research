# H300 STATUS

Updated: 2026-08-27
State: **CLOSED / NO GUARANTEED PROFIT**

## Result

Net-A-Deal's current August 2026 “£10,000 Instant Wins | Every Ticket Wins” mechanic does not provide a positive deterministic cash floor.

The checked live competition has 49,999 identifiers and a 1,000-entry per-person cap. Only 32 identifiers are immediate cash wins and 40 are £25 Site Credit. The remaining **49,927** identifiers only receive entry into a separate random £5,000 rewards competition.

Ticket numbers are randomly allocated. Since `49,927 >= 1,000`, there is a legal allocation in which every ticket owned by one maximally entered person lies in the residual class. The later rewards competition has a legal non-winning outcome for that person. Therefore the strict withdrawable-cash floor is **£0** even though the product is advertised as “Every Ticket Wins”.

## Reproducible records

- `src/loto_research/h300_netadeal_every_ticket_wins_floor.py`
- `data/derived/h300_netadeal_every_ticket_wins_floor.json`
- `research/h300_netadeal_every_ticket_wins_floor.md`
- `research/H300_VALIDATION.md`

## NEXT ACTION

Do not reopen this residual-entry structure unless a future competition converts every residual ticket into deterministic withdrawable cash/credit of sufficient value or makes profitable identifiers selectable/reservable.

Global research remains **NO SUCCESS; NOT EXHAUSTED**. Continue with a genuinely new mechanism, prioritizing hard-capped/reservable finite pools whose deterministic player-facing liabilities approach or exceed exact cheapest acquisition cost, or deterministic subsidies/cashback that survive a worst-case execution proof.
