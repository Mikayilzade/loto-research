# H284 VALIDATION — Virginia Pick 3 50% subsidy bound

Validated: 2026-08-26
Packet state: **CLOSED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Independent checks

1. H225-X* was checked first and remains terminal at X20: 44 canonical shards, 11 sectors, exactly 306,450 quotient states, 0 coefficient survivors, 0 legal shift tuples. No X21/X22 work was created.
2. Repository branch head before H284 was `e9dc479580868cbeec3a13dc3516d0f195132fb1` (H283 terminal execution blocker); repository search returned no pre-existing H284 packet.
3. Virginia Lottery live Pick 3 page was checked for the current prize table and confirms $1/$0.50 base wagers, $500 Exact, $50 Pair, $160/$80 Any Order, $330/$290 50/50 exact totals and $500 Combo payouts.
4. Exact base primitive average-gross ratios recompute to 0.50, 0.50, 0.48, 0.48, 0.49, 0.49, 0.50 and 0.50 respectively. Maximum = exactly 0.50.
5. For any nonnegative additive mixture, linearity preserves average gross <= 0.50 of stake. Since minimum outcome <= average outcome, strict guaranteed gross above stake cannot occur.
6. Granting the currently advertised 50% first-deposit match in full multiplies playable balance by 1.5. Therefore the base-class worst-case cash recovery is bounded above by `1.5 × 0.50 = 0.75` of the original cash deposit.
7. FIREBALL stress deliberately grants a favorable 0.57 standalone gross ceiling. Equal-stake base+FIREBALL blend <= 0.535 average gross; after the 50% match this is <= 0.8025 of cash deposit, still below break-even.
8. The packet does not rely on the exact advertised bonus cap, atomic cart behavior, stop-play authority, or withdrawal details to reject the mechanism: even the stronger assumption that the full 50% match is immediately usable cannot cross the arithmetic hurdle.

## Closure criterion

H284 closes only the tested **Virginia Pick 3 + deterministic 50% playable-balance subsidy additive wager class**. It does not claim global lottery exhaustion.

Reopen only on material change: subsidy >100% for the base 50%-return class, materially improved fixed payouts, or a separate deterministic cash-equivalent reward outside wager-return symmetry.
