# H302 STATUS

Updated: 2026-08-27
State: **CLOSED / EXECUTION-BLOCKED**

## Scope

H302 screened a genuinely new finite-pool mechanism: whether a UK prize competition's free postal entry route can lower the effective full-pool acquisition cost enough that a capped cash prize exceeds unavoidable entry costs.

Concrete screen: SC Competitions' `£100 Cash ONLY 100 Tickets` format. The page observed in the current 2026 site index showed a 100-ticket pool, £1.99 paid price, £100 cash prize, and a free postal route. SC's governing terms state that each compliant postcard can receive one Entry Number and that paid and postal entries participate in the same draw.

Royal Mail's current 2nd Class standard-letter/postcard price is £0.91.

## Arithmetic gate

For a 100-entry pool:

- paid-only full acquisition: `100 × £1.99 = £199.00`;
- hypothetical all-postal acquisition cost: `100 × £0.91 = £91.00`;
- cash prize: `£100.00`;
- conditional arithmetic surplus if every one of the 100 postal entries were accepted and allocated before any external entry: **£9.00**;
- mixed full takeover first crosses strict break-even at **92 postal + 8 paid entries**, costing `92×£0.91 + 8×£1.99 = £99.64`, a conditional £0.36 surplus.

So free-postal entry is materially different from the ordinary paid finite-pool screens: it can cross the arithmetic threshold.

## Why this is NOT SUCCESS

The execution guarantee fails under the same governing terms:

1. each postal entry is a separate transaction and must physically arrive before the Closing Date;
2. proof of posting is explicitly not proof of receipt, and the promoter accepts no responsibility for lost/delayed postcards;
3. paid entries can consume the finite cap before postal entries arrive;
4. the promoter may impose a per-person maximum on the raffle page;
5. conduct contrary to the spirit/intention of the raffle can lead to discretionary disqualification;
6. when less than 100% of available Entry Numbers are allocated, the promoter may substitute a percentage-of-ticket-sales payout or extend the competition.

Therefore the profitable arithmetic branch requires complete/near-complete postal acquisition that the rules do not make deterministic. A single external eligible Entry Number preserves a legal draw in which that external entry wins the main prize.

## H225-X* lane

Unchanged terminal state: **CLOSED / EXHAUSTED**. H225-X20 left 0 coefficient survivors / 0 legal shift tuples after the validated full 44-shard / 306,450-state rescreen. Do not create X21/X22 without broadening the mathematical family.

## NEXT ACTION

Continue outside H225. The new useful filter is to look for a finite competition where the low-cost/free entry route is **electronically reserved or otherwise deterministically acknowledged before competing entries can consume the cap**, rather than ordinary postal delivery. Do not treat postal dispatch alone as ownership.

## Sources checked

- SC Competitions cash raffle page: https://www.sccompetitions.co.uk/competition/100-cash-only-100-tickets-sc645-2/
- SC Competitions governing terms and postal-entry Schedule 1: https://www.sccompetitions.co.uk/competition-terms-conditions/
- SC Competitions FAQ: https://www.sccompetitions.co.uk/faqs/
- Royal Mail current 2nd Class price: https://www.royalmail.com/sending/uk/2nd-class
