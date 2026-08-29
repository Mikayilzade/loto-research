# H353 VALIDATION — NZ Lotto Strike terminal duplicate bound

Date: 2026-08-29

## Independent checks

1. **Universe** — ordered distinct 4-tuples from 40: `P(40,4) = 2,193,360`.
2. **Exact-position partition** recomputed by inclusion-exclusion: k=0 1,982,313; k=1 202,904; k=2 7,998; k=3 144; k=4 1. Sum = **2,193,360** exactly.
3. **Terminal trigger** — Lotto Rules 2025 rules 38–40 require no D1 winning selection for the Strike D1 pool to roll to the next-lowest winning division on a terminal/specified-date condition.
4. **Self-block theorem** — every nonempty portfolio has a member `s`; the legal draw `s` makes that member a D1 winner. Hence no nonempty portfolio guarantees the no-D1 trigger.
5. **Sharing** — rule 43 states that where a prize division has more than one winning selection, allocated prize money is shared equally.
6. **Current policy** — June 2024 Strike Jackpot Policy sets threshold **NZ$1.5m** and maximum jackpot games **9**; no later replacement policy was found in the current official search.
7. **Duplicate stress arithmetic** — with the rules-permitted 60% game-pool fraction and player-favourable NZ$1 valuation of each D4 bonus line: isolated complete cover = **NZ$2,405,166.3608 gross**, +NZ$211,806.3608; one external winning D1 duplicate = **NZ$1,655,166.73934 gross**, −NZ$538,193.26066.

## Validation flags

- full-universe partition: **PASS**
- terminal self-block proof: **PASS**
- one-external-duplicate below-cost witness: **PASS**
- arithmetic inconclusive: **0**
- closure-relevant inconclusive: **0**

Conclusion: **H353 CLOSED for strict terminal / Must Be Won guaranteed-profit construction.**
