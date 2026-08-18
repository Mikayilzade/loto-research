# H087 — K52/K53 material-classification gate

Updated: 2026-08-19
Status: **VALIDATED CORRECTION / EXECUTION-GATE HARDENED / NOT SUCCESS**

## Why this packet exists
H086 used `K52/K53` as search terms for tantalum-capacitor arbitrage. Fresh primary-source manufacturer data shows that this is too coarse: the prefix `K53` does **not** uniquely identify tantalum. A wrong family-level assumption can create a false-positive acquisition and destroy the deterministic margin.

## Primary-source classification
AO Elecond current product pages establish:

### Confirmed tantalum examples
- `K52-1` — electrolytic volumetric-porous **tantalum** capacitor.
- `K52-19`, `K52-20`, `K52-21`, `K52-24`, `K52-26`, `K52-28`, `K52-30` — current manufacturer pages classify these as volumetric-porous **tantalum**.
- `K53-1A` — oxide-semiconductor **tantalum** capacitor.
- `K53-65` — oxide-semiconductor **tantalum** capacitor.
- `K53-68` — oxide-semiconductor **tantalum** capacitor.
- `K53-69` — oxide-semiconductor **tantalum** capacitor.

Primary sources:
- https://elecond.ru/capacitor/k52-1/
- https://elecond.ru/capacitor/k52-19/
- https://elecond.ru/capacitor/k52-20/
- https://elecond.ru/capacitor/k52-21/
- https://elecond.ru/capacitor/k52-24/
- https://elecond.ru/capacitor/k52-26/
- https://elecond.ru/capacitor/k52-28/
- https://elecond.ru/capacitor/k52-30/
- https://elecond.ru/capacitor/k53-1a/
- https://elecond.ru/capacitor/k53-65/
- https://elecond.ru/capacitor/k53-68/
- https://elecond.ru/capacitor/k53-69/

### Confirmed non-tantalum counterexample
- `K53-4` — oxide-semiconductor **niobium** capacitor.

Primary sources:
- https://elecond.ru/capacitor/k53-4/
- https://elecond.ru/production/capacitors/niobium/

This is sufficient to reject the rule `K53 => tantalum`.

## Consequence for H086
The H086 break-even formula remains correct **only after exact buyer classification**:

`m_break_even_g = 1000 * ask_per_unit / binding_buyer_rate_per_kg`

But the input `buyer_rate_per_kg = tantalum-capacitor rate` cannot be assigned from a generic `K53` marking.

### New strict material gate
Before any break-even calculation using a tantalum buyer rate, one of the following must be true:
1. exact subtype is independently classified as tantalum by a primary manufacturer/datasheet; or
2. the local buyer gives a binding quote for the exact photographed/marked lot and explicitly accepts it under the quoted tantalum category.

A generic seller text such as `K53 capacitor`, `tantalum/niobium capacitor`, or a mixed box is **not enough**.

## Search allow-list for next execution stage
High-priority exact strings supported by current manufacturer evidence:
- `К52-1`, `K52-1`
- `К52-19`, `K52-19`
- `К52-20`, `K52-20`
- `К52-21`, `K52-21`
- `К52-24`, `K52-24`
- `К52-26`, `K52-26`
- `К52-28`, `K52-28`
- `К52-30`, `K52-30`
- `К53-1А`, `K53-1A`
- `К53-65`, `K53-65`
- `К53-68`, `K53-68`
- `К53-69`, `K53-69`

Explicit exclusion from automatic tantalum valuation:
- `К53-4`, `K53-4` — confirmed niobium.

Unknown K53 subtypes remain `UNKNOWN` until exact classification; do not infer metal from series prefix.

## Local-search result in this run
Fresh exact-string searches did **not** recover a current Azerbaijan/Tap.Az seller lot with a readable exact Soviet `K52-x`/`K53-x` subtype and fixed per-unit ask. Search results containing `K52`/`K53` were dominated by ASUS laptop-model identifiers and are false positives for this project.

A current Baku mixed-components listing at 3 AZN exists, but its indexed text does not expose exact capacitor subtype, count, weight or material classification, so it cannot pass the deterministic acquisition gate.

## Result
H087 does not produce a profitable transaction, but it materially improves the research process by removing a dangerous false-positive rule. The top-priority acquisition search is now **exact-subtype constrained**, not prefix constrained.

Next execution gate:
`exact subtype -> manufacturer material class -> seller ask/count/weight -> binding local buyer quote -> all-in net > 0 -> only then purchase`.
