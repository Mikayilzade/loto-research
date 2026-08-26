# H296 VALIDATION

Validated: 2026-08-26
Result: **PASS — packet arithmetic is internally consistent; all screened impossible-favourable takeover returns are below 100%.**

## Independent arithmetic checks

### USA Luge
- hard cap: 500 tickets
- ticket price: US$100
- takeover cost: US$50,000
- favourable prize valuation used: US$25,900
- return: `25,900 / 50,000 = 0.518 = 51.8%`
- deficit: US$24,100

### ECHO Mercedes
- hard cap: 1,000 tickets
- ticket price: US$100
- takeover cost: US$100,000
- explicit cash alternative: US$50,000
- return: `50,000 / 100,000 = 50%`
- deficit: US$50,000
- published sub-900 fallback is 50/50, so it cannot exceed the 50% perfect-buyout ratio.

### Mater Prize Home No.327
- published ticket-count range lower endpoint: 13,455,147
- cheapest published bundle unit price: A$1
- deliberately impossible-favourable acquisition lower bound: A$13,455,147
- counted liabilities: A$5,382,059 first prize + A$60,000 max book buyer + A$145,000 VIP + A$5,000 early-bird = **A$5,592,059**
- return: `5,592,059 / 13,455,147 = 0.4156074251734299`
- return percent: **41.5607425173%**
- deficit: **A$7,863,088**

The Mater cost bound intentionally combines the minimum possible issued-ticket count with the minimum bundle unit price even though those extrema need not coexist. It is therefore stronger in the player's favour than the real takeover economics and is safe for rejection.

## Closure gate
All three `favourable_liability < acquisition_cost` assertions hold. Therefore no execution/reservation assumption can turn these specific complete-pool takeover constructions into strict guaranteed profit under the checked economics.

H225-X* remains independently terminal at X20 with 0 coefficient survivors / 0 legal shift tuples.
