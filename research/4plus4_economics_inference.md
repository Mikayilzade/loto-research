# 4+4 — empirical payout-engine reconstruction

Updated: 2026-08-12
Status: **strong empirical structure found; primary-rule confirmation still required**

## Why this pass matters
The previous 4+4 work established exact probabilities but left two critical unknowns:
1. whether the public 2 AZN ticket price is also the price of one base variant;
2. whether draw-to-draw lower-tier payouts are arbitrary/carryover-driven or follow a stable allocation formula.

This pass finds a strong hidden structure in preserved 2026 payout tables.

## Sources and confidence
Primary/current operator page:
- https://www.azerlotereya.com/lotereya/4-4
- states public ticket price **2 AZN**;
- states 11 prize categories and 5+5 / 6+6 combination options;
- does not expose the detailed prize-fund allocation formula in crawlable text.

Secondary draw tables used for empirical reconstruction are stored in:
- `data/historical/az_4plus4_payout_samples_2026.csv`

These rows are not yet authoritative. They are useful because the repeated numerical pattern is internally very strong and can later be reconciled against primary archive payloads.

## Hidden common unit U
For sampled draws 772, 774, 776, 777, 795 and 796, total paid amounts in categories III, IV, VII, VIII and IX closely follow:

- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**

In addition:

- V + VI = **2U**

Therefore categories III–IX together pay approximately:

**48U**

whenever those displayed pools are distributed.

The split between V and VI changes materially while their combined total remains almost exactly 2U. This is evidence that V/VI are coupled by an internal allocation rule rather than being independent fixed pools.

Examples:
- draw 795: U ≈ 408.01 AZN; V+VI = 816.00 AZN vs 2U ≈ 816.02;
- draw 776: U ≈ 415.57 AZN; V+VI = 831.11 AZN vs 2U ≈ 831.15;
- draw 777: U ≈ 430.97 AZN; V+VI = 861.88 AZN vs 2U ≈ 861.94.

Implementation: `src/loto_research/four_plus_four.py`.

## Price / sales inference
Categories X and XI are observed at fixed per-winner prizes:
- X (2+2): 6 AZN;
- XI (2+1 / 1+2): 4 AZN.

Their exact category probabilities are known from combinatorics:
- P(X) = 0.022083984318837523;
- P(XI) = 0.137411457983877900.

If U is interpreted under the working scale:

`U ≈ 0.01 AZN × number_of_variants`

then a draw with U ≈ 408 implies roughly 40,800 sold variants. The expected X/XI winner counts at that volume are close to observed counts in most sampled draws.

This scaling is economically equivalent to U being about 0.5% of gross sales if one base variant costs 2 AZN:

`0.5% × 2 AZN × N = 0.01 × N = U`.

This creates a strong consistency argument that **one base 4+4 variant is 2 AZN**, matching the operator's displayed ticket price. It is still classified as a high-confidence inference, not a primary-source confirmation, until the purchase flow/receipt or detailed registered rules explicitly state it.

A 1-AZN-per-variant interpretation is economically implausible in these samples because observed lower-tier payouts alone would meet or exceed inferred gross variant sales.

## Baseline payout implications
Exact expected contribution from the two observed fixed tail categories alone is:

`P(X)×6 + P(XI)×4 = 0.6821497378485368 AZN per variant`.

Under the working U scaling, categories III–IX distribute approximately:

`48U / N ≈ 0.48 AZN per variant`.

So before category II and jackpot value, the ordinary lower-tier crowd-average expectation is already approximately:

`0.68214973785 + 0.48 = 1.16214973785 AZN`

per 2-AZN base variant, or about **58.11% gross return** before category II/jackpot/tax effects.

This is still strongly negative in an ordinary state. A large structural overlay would be required to reach break-even.

## New interpretation of H014
The evidence changes H014 materially:

- ordinary variation in III/IV/V/VI/VII/VIII/IX payout-per-winner is largely explained by a stable draw-level pool unit U and winner counts;
- the variation is therefore **not, by itself, evidence of exploitable carryover**;
- the special V/VI coupling is real and should be reverse-engineered;
- the real state-edge test is now narrower: identify what happens when a low-probability variable category has **zero winners**, and whether its assigned pool carries forward, redistributes immediately, or moves elsewhere.

That is the decisive next question.

## Next data target
Collect 50–100 consecutive draws including every case where categories II–VI have zero winners. For each transition t -> t+1:
- infer U_t from stable categories;
- record winner counts and total pools;
- detect whether an unpaid category amount appears in its own next-draw pool, another category, or jackpot;
- infer U scaling against X/XI winner counts;
- reconcile at least a subset against official historical results/API payloads.

Only a pre-draw observable carryover can become a strategy signal.
