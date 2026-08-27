# H316 independent validation

Validated: 2026-08-27
Result: **PASS — H316 is closed; no strict guaranteed-profit takeover exists under the checked Punter Prizes postal-bundle mechanism.**

Checks performed independently of the narrative report:

- Live CASH DASH 3 pool size = 20,000 and price = £0.10, so exact paid full-pool cost = **£2,000**.
- Published prize face used in the favourable model = 10×£100 cash + 10×£100 ticket bundles = **£2,000**; no end prize is published.
- Therefore impossible-perfect paid ownership is only **100% gross**, not strict profit.
- Current Royal Mail 2nd Class letter price = **£0.91**.
- Punter's postal rule credits entries only up to postage value; at 10p each this is at most `floor(0.91/0.10)=9` entries per letter.
- Full postal takeover therefore needs `ceil(20,000/9)=2,223` letters costing **£2,022.93**, for **98.8664956%** face return.
- Snapshot sold/remaining values cross-check: 1,811 + 18,189 = 20,000.
- With two £100 prizes already claimed, the favourable remaining face is 18×£100 = **£1,800**.
- Buying all 18,189 remaining tickets costs **£1,818.90**, return **98.9609104%**.
- Postal acquisition of all remaining inventory requires 2,021 letters = **£1,839.11**, return **97.8734279%**.
- The free-entry route is non-atomic: each entry is separately posted, can miss cutoff/cap, and receipt/correctness is not acknowledged in advance.

Reusable inequality verified:

For ticket price `p>0`, postage `s>p`, and credited count `k=floor(s/p)`, `k*p <= s`, hence `s/k >= p`. Therefore an `up to postage value` bundle cannot reduce per-entry acquisition cost below the paid ticket price.

The model intentionally overvalues ticket bundles at 100% cash-equivalent face value. Any discount, wagering friction, or inability to monetize them only strengthens closure.
