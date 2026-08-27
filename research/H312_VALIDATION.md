# H312 VALIDATION

Date: 2026-08-27
Result: **VALIDATED / CLOSED**

Independent arithmetic checks against the operator-published schedule:

- finite pool: 9,999 tickets;
- price: £1.99;
- exact full-pool cost: £19,898.01;
- published per-person maximum: 9,999;
- snapshot sold count: 254;
- favourable ring valuation: 3 × £2,150 = £6,450;
- cash tiers: £6,000 total;
- site-credit tiers valued at full face: £1,000 total;
- total favourable player-facing liability: £13,450;
- exact deficit: £6,448.01;
- exact gross ratio: 0.6759469916840931 = 67.5946991684%.

Validation logic:

1. The liability bound deliberately favours the player by treating insured ring value and site credit as cash-equivalent at full face.
2. It also grants impossible-perfect ownership of the entire pool, ignoring the 254 already-sold tickets and any allocation/checkout friction.
3. Since even this dominating upper bound has `liability < acquisition cost`, every realistic acquisition is below the strict guaranteed-profit threshold.
4. Therefore no CI/exact separator is warranted for this packet; closure follows from exact finite arithmetic.

Reproduce with:

`python -m loto_research.h312_diamond_winners_triple_ring_full_pool_bound`
