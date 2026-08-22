# H173 audit append — Rhode Island reduced doubled-Keno cover

Updated: 2026-08-22

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| H173 Rhode Island Lucky-3-style free 2x Keno | Replace naive all-82,160-triples coverage with four disjoint 20-number groups; buy all C(20,3) triples inside each group | 4,560 plays; for any 20-number draw, doubled payout minimized at 5+5+5+5 group hits; strict minimum gross **$5,000** vs **$4,560** stake = **109.6491%**, +$440 pre-tax | **STRUCTURAL GUARANTEE VALIDATED CONDITIONALLY ON FREE PRE-LOCKED 2x + $25/$2.50 PAYTABLE; current executable SUCCESS not proven**; `research/h173_ri_keno_reduced_block_cover.md` |
| H173 execution reduction | Compare with H172 full C(80,3) cover | wager count falls **82,160 -> 4,560 (94.45% reduction)**; $150 monetary ticket-cap lower bound falls 548 -> 31 ticket-equivalents | **MATERIAL EXECUTION IMPROVEMENT**, but terminal selection packing / same-draw bulk acceptance still unproven |
| H173 equal-partition boundary | 5 groups x 16 numbers, all internal triples | 2,800 plays; exact worst doubled gross **$2,800 = 100%** | **BREAK-EVEN CONTROL**, not profit |
| H173 nearby partition screen | `(19,20,20,21)`, `(19,19,21,21)` and controls | positive but larger than equal 20/20/20/20; examples 4,579 plays -> $5,000 and 4,598 -> $5,000 | **20/20/20/20 best among tested nearby clique partitions** |

Open gates:
1. current 2026 `Kick Back with Keno` official mechanic;
2. current primary RI 3-spot paytable;
3. number of distinct Keno selections per terminal ticket/action and ability to target one common draw;
4. after-tax margin and promotion-discretion risk;
5. search smaller non-clique balanced/cyclic block designs.
