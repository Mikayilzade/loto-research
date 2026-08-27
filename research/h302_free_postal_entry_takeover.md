# H302 — UK free-postal finite-pool takeover screen

## Question

Can the legally required free-entry route on a capped UK prize competition reduce the effective cost of controlling the whole draw below the guaranteed cash prize?

This is a different mechanism from ordinary raffle buyout. The economic input is no longer the advertised paid ticket price; it is the unavoidable cost of each valid free-route entry.

## Candidate

SC Competitions publishes a `£100 Cash ONLY 100 Tickets` format with:

- 100 available Entry Numbers;
- £1.99 paid online price;
- £100 cash prize paid to a bank account;
- a free postal entry route governed by Schedule 1 of its competition terms.

The observed page showed `100 Left` and no ticket log at the time captured by the current web index. This is useful as a clean finite-pool example, but it is not treated as proof that the pool remains untouched at execution time.

## Free-route mechanics

SC's governing terms say that a compliant postal entry can be allocated one Entry Number. Each free entry must be a separate postcard; the entrant must already have a matching online account. Postal entries participate in the same winner selection as paid entries.

Royal Mail's current 2026 2nd Class standard-letter/postcard rate is £0.91.

Therefore the purely arithmetic all-postal full-pool cost is:

`100 × £0.91 = £91`.

Against a £100 cash prize, this gives a conditional surplus of **£9**, or **9.8901%** on unavoidable postage cost.

A mixed acquisition also becomes arithmetically positive once at least 92 of the 100 entries are postal:

`92×£0.91 + 8×£1.99 = £99.64`, leaving **£0.36** conditional surplus.

This is the first finite-pool screen in this lane where the free-entry mechanism itself can push the acquisition arithmetic above 100%.

## Exact execution blocker

The positive arithmetic is not a guarantee because ownership is not reserved when a postcard is posted.

The same terms state that:

- postal entries must be received before the Closing Date;
- the promoter accepts no responsibility for lost, mislaid, damaged or delayed postal entries;
- proof of posting is not proof of receipt;
- entries are processed as separate transactions;
- a raffle page may impose a maximum per entrant;
- conduct contrary to the spirit/intention can be disqualified at the promoter's discretion;
- postal entries compete for the same finite Entry Numbers as paid entries;
- if fewer than 100% of available Entry Numbers are allocated by the relevant cutoff, the promoter can use a percentage-of-ticket-sales prize instead of the advertised prize or extend the draw.

The promoter reserves some capacity for postal entries for at least four working days after a raffle goes live, but that does not guarantee acceptance of every postcard from one entrant.

Thus there exists a legal execution path in which at least one required postal entry is delayed/rejected or an external paid entrant consumes an Entry Number first. Once an external eligible Entry Number exists, there is a legal winner-selection outcome where that external number wins and the takeover portfolio receives no main prize.

## Result

**CLOSED / EXECUTION-BLOCKED.**

The free postal route is a real arithmetic improvement and should remain a search direction. It is not rigorous when acquisition depends on ordinary post and a shared live cap.

## Reopen criterion

Reopen this mechanism only for a competition where one of the following is documented:

1. free/discounted entries are electronically reserved immediately;
2. a single acknowledged transaction can reserve the entire finite eligible pool;
3. the entrant can lock all remaining identifiers before external entries can be accepted; or
4. every residual external/unsold state still pays a deterministic amount sufficient to keep the floor above acquisition cost.

## Sources

- SC Competitions raffle page: https://www.sccompetitions.co.uk/competition/100-cash-only-100-tickets-sc645-2/
- SC Competition Terms & Conditions / Schedule 1: https://www.sccompetitions.co.uk/competition-terms-conditions/
- SC FAQ: https://www.sccompetitions.co.uk/faqs/
- Royal Mail 2nd Class current prices: https://www.royalmail.com/sending/uk/2nd-class
