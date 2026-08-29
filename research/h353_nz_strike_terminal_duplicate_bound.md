# H353 — New Zealand Lotto Strike terminal / Must Be Won duplicate bound

Date: 2026-08-29
Branch: `research-work`
Result: **CLOSED for strict guaranteed-profit use of the terminal / Must Be Won mechanic**

## Why this candidate was checked

`STATUS.md` prioritises terminal/forced-distribution mechanics where accumulated money can cross the full-cover cost and where execution can be made deterministic. Lotto Strike is unusually close: the current policy sets a Strike 4 threshold of NZ$1.5m, while one complete ordered Strike cover costs only NZ$2,193,360.

## Binding current rules / policy

Primary sources:
- Lotto Rules 2025: https://assets.mylotto.co.nz/assets/uploads/485a1f58-9833-11f0-a22c-3ad4acd14bcf.pdf
- Lotto Strike Jackpot Policy (June 2024, effective after draw 2389): https://assets.mylotto.co.nz/assets/uploads/1693c42e-3727-11ef-9eda-005056817096.pdf

Relevant facts:
1. A Strike selection is 4 different numbers from 1..40, and the winning Strike numbers are the first four standard Lotto numbers in exact order.
2. The Strike game prize pool must be at least 60% of turnover.
3. After the fixed Division 4 prizes, the remaining ordinary pool is allocated 36.910% / 9.590% / 53.500% to Divisions 1/2/3.
4. Division 4 pays one bonus Strike selection; its rules-defined monetary equivalent is NZ$1.
5. When a terminal threshold / specified-date draw has no Division 1 winning selection, the D1 pool is reallocated to the next-lowest winning division.
6. More than one winning selection in a non-fixed division shares that division's prize money equally.
7. Current Strike policy sets the Strike 4 threshold at NZ$1,500,000 and the maximum jackpot-game count at 9.

## Exact one-copy ordered cover

The complete outcome space is

`P(40,4) = 40*39*38*37 = 2,193,360`

distinct ordered selections.

At NZ$1 per Strike line:
- entries: **2,193,360**
- acquisition cost: **NZ$2,193,360**

For every possible draw, exact-position multiplicities in the full cover are invariant:
- exactly 4 positions: **1**
- exactly 3 positions: **144**
- exactly 2 positions: **7,998**
- exactly 1 position: **202,904**
- exactly 0 positions: **1,982,313**

Total: **2,193,360 / 2,193,360**. Arithmetic inconclusive: **0**.

## Structural terminal blocker

The Must Be Won / terminal roll-down requires **no Division 1 winning selection**.

A complete cover contains exactly one Division 1 selection for every legal draw, so it always prevents the no-D1 trigger.

Stronger statement: any nonempty portfolio contains at least one legal ordered tuple. The draw equal to that tuple is a legal state in which the portfolio itself wins Division 1. Therefore **no nonempty Strike portfolio can guarantee the no-D1 branch across all legal draws**.

This alone closes the intended forced-roll-down construction.

## Exact duplicate stress

The candidate is still worth quantifying because it is close to profitable when isolated.

Using the rules-permitted 60% current-game prize-pool level, valuing every Division-4 bonus line at its NZ$1 monetary equivalent, granting our complete cover all D2/D3 pool allocations, and using a NZ$1.5m total Strike-4 threshold:

### No external D1 duplicate
- full-cover gross: **NZ$2,405,166.3608**
- net: **+NZ$211,806.3608**
- return: **109.6567076%**

So this is a real isolated >100% terminal-cover candidate.

### One external duplicate of the drawn Strike-4 tuple
One additional NZ$1 entry selecting the same winning ordered tuple is legal. Under the sharing rule the NZ$1.5m D1 amount is split two ways.

Including that extra ticket's turnover in the 60% pool:
- our gross: **NZ$1,655,166.73934**
- net: **−NZ$538,193.26066**
- return: **75.4626117%**

Thus a **single legal external D1 duplicate** destroys the strict guarantee in an otherwise player-favourable exact cover.

There is no binding pre-draw hard cap forcing external D1 duplicates to zero.

## Closure

H353 does not prove that every possible speculative Strike strategy has negative expectation. It closes the specific strict-guarantee mechanism targeted by the current research lane:

- terminal/no-D1 roll-down cannot be forced by any nonempty portfolio;
- the complete-cover isolated terminal arithmetic can exceed 100%;
- but only one legal external duplicate is enough to produce a below-cost state;
- exact partition validated;
- arithmetic inconclusive = **0**;
- closure-relevant inconclusive = **0**.

## NEXT ACTION

Prioritise terminal or special-event games where:
1. the accumulated subsidy remains payable even when our portfolio creates the top-tier winner; **and**
2. the subsidy is fixed per winning selection or duplicate-proof; **or**
3. all eligible top-tier identifiers can be exclusively reserved/monopolised before cutoff.

Do not repeat ordinary no-top-winner roll-down games without one of those structural improvements.
