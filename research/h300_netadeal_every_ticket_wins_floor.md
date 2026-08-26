# H300 — Net-A-Deal “Every Ticket Wins” deterministic cash-floor audit

Checked: 2026-08-27
Status: **CLOSED / NO GUARANTEED PROFIT**

## Candidate

Two live Net-A-Deal August 2026 instant-win competitions advertise “Every ticket wins”. The checked #2 competition publishes:

- 49,999 total ticket identifiers;
- maximum 1,000 entries per person;
- £0.49 paid entry price;
- 10 × £500, 12 × £250, 10 × £100 cash instant wins;
- 40 × £25 Site Credit instant wins;
- every other ticket only receives an entry into a separate £5,000 rewards competition;
- ticket numbers are randomly allocated when ordering.

Source pages:
- https://www.net-a-deal.com/competition/10000-instant-wins-august-2-every-ticket-wins/
- https://www.net-a-deal.com/competition/10000-instant-wins-august-every-ticket-wins/

## Exact arithmetic

Cash-paying identifiers: `10 + 12 + 10 = 32`.

Site-credit identifiers: `40`.

Residual identifiers:

`49,999 - 32 - 40 = 49,927`.

The per-person maximum is only 1,000 entries. Therefore there are far more than 1,000 identifiers whose immediate outcome is neither cash nor site credit.

A legal allocation exists in which all 1,000 of one entrant's randomly assigned numbers lie among those 49,927 residual identifiers. Each such identifier only provides an entry into a later random £5,000 rewards draw. That later draw has a legal state in which none of the entrant's rewards entries wins.

Hence the strict guaranteed withdrawable-cash floor is:

`£0`.

The maximum paid spend at the per-person cap is:

`1,000 × £0.49 = £490`.

So the checked mechanic cannot guarantee positive cash profit. The “Every Ticket Wins” wording does not imply every paid ticket carries positive guaranteed cash value.

## Stronger observations

The conclusion does not depend on expected value, the total £9,000 instant cash prize amount, or the £1,000 site-credit face amount. It follows from a single legal worst-case assignment plus a legal non-winning outcome in the separate rewards draw.

Free postal entry does not repair the strict guarantee: the site states each postal entry must be sent separately, receipt/processing is not guaranteed once caps are reached, and the assigned ticket number remains uncontrolled.

## Reproducibility

- `src/loto_research/h300_netadeal_every_ticket_wins_floor.py`
- `data/derived/h300_netadeal_every_ticket_wins_floor.json`

## Decision

**CLOSED for the target deterministic guaranteed-profit mechanism.** Do not reopen this exact “Every Ticket Wins → residual rewards-draw entry” structure unless the residual outcome is changed into deterministic withdrawable cash/site credit with sufficient guaranteed value, or ticket identifiers become controllably selectable/reservable in a way that removes the legal zero-cash allocation.
