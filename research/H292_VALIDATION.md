# H292 VALIDATION

Date: 2026-08-26
Result: **VALIDATED / NO STRICT-PROFIT FULL BUYOUT AMONG SCREENED POOLS**

Independent checks performed:

1. H225-X* was checked first and remains terminal at X20; no X21/X22 continuation was created.
2. Each H292 candidate has a public finite maximum ticket count in the checked raffle page/terms.
3. The calculation grants impossible-perfect ownership of every ticket and therefore removes draw randomness and external duplicate risk in the player's favour.
4. Cheapest published bundle rates were used where a 100-ticket bundle was available.
5. Ticket counts divide exactly by the applied bundle sizes for Waves & Wheels and The 6e Gold Rush, so no rounding or leftover-ticket assumption is needed.
6. Exact arithmetic:
   - Waves & Wheels: 125,000 / 100 * A$500 = A$625,000; A$481,993.59 / A$625,000 = **77.1189744%**.
   - The 6e Gold Rush: 65,000 / 100 * A$500 = A$325,000; return **34.3636923%**.
   - Bruthen FNC: 5,000 * A$25 = A$125,000; return **40.24%**.
   - Norwood FC: 30,000 * A$5 = A$150,000; return **38.9213333%**.
   - TRG: 2,500 * A$10 = A$25,000; return **24.072%**.
7. All five advertised prize pools are strictly less than perfect full-buyout cost.
8. The strongest checked return is Waves & Wheels at **77.1189744%**, deficit A$143,006.41.

Because this model is strictly more favourable than real execution, availability, residency, liquidity, non-cash valuation, transaction limits, or competitors cannot turn any of these five full-buyout constructions into a strict guarantee under unchanged economics.

Reproducible calculation:
- `src/loto_research/h292_raffletix_finite_pool_screen.py`
- `data/derived/h292_raffletix_finite_pool_screen.json`
