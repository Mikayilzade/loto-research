# CHECKED PROJECTS AND TESTS — H303 APPEND

## H303 — Birdie Tickets electronic reservation / free-entry takeover screen

Date: 2026-08-27
Result: **NOT SUCCESS; evidence-blocked**

Tested the H302 follow-up mechanism: a finite prize pool with electronically locked ticket identifiers and a no-purchase entry route.

Verified:

- hard entry cap published conceptually for each Birdie promotion;
- no-purchase route exists;
- paid ticket numbers are instantly confirmed and locked;
- random draw is reproducible/public-seed based;
- $1 winner-verification checkout.

Not verified from accessible authoritative rule text:

- free route is electronic rather than mail;
- free route draws from the same finite identifier pool;
- free route has no restrictive per-person cap;
- free identifiers are locked immediately;
- current live draw's exact cap/price/prize values.

Conclusion: this candidate is structurally closer than H302, but no takeover/profit guarantee can be claimed until the AMOE payload is retrieved. Paid reservation behavior cannot be transferred by assumption to free entries.

Sources checked:

- https://birdietickets.com/trust
- https://birdietickets.com/
- https://birdietickets.com/tickets
- https://birdietickets.com/rules
