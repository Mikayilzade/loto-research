# H088 — K52/K53 material-classification gate

Updated: 2026-08-19
Status: **VALIDATED CORRECTION / EXECUTION-GATE HARDENED / NOT SUCCESS**

Fresh primary-source manufacturer data shows that `K53` does **not** uniquely identify tantalum. A family-level assumption can create a false-positive acquisition and destroy deterministic margin.

## Confirmed tantalum examples
Current AO Elecond product pages classify these as tantalum:
- K52-1, K52-19, K52-20, K52-21, K52-24, K52-26, K52-28, K52-30;
- K53-1A, K53-65, K53-68, K53-69.

## Confirmed counterexample
- K53-4 is an oxide-semiconductor **niobium** capacitor, not tantalum.

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
- https://elecond.ru/capacitor/k53-4/
- https://elecond.ru/capacitor/k53-65/
- https://elecond.ru/capacitor/k53-68/
- https://elecond.ru/capacitor/k53-69/
- https://elecond.ru/production/capacitors/niobium/

## Consequence for H086/H087
The H086 break-even formula remains valid only after exact material classification. Never assign the tantalum buyer rate from a generic `K53` marking.

Strict material gate before any purchase:
1. exact subtype readable;
2. manufacturer/datasheet classifies it as tantalum, **or** local buyer explicitly classifies the exact lot in a binding quote;
3. exact seller ask/count/weight locked;
4. buyer binding payout locked on the same lot;
5. payout > all-in cost before seller payment.

Generic `K53`, mixed-box, or seller-supplied metal labels are insufficient.

## Search result
Fresh exact-string Azerbaijan searches did not recover a current indexed seller lot with readable exact Soviet K52-x/K53-x subtype + fixed per-unit ask + count/weight. Generic K52/K53 search is heavily polluted by ASUS laptop model identifiers.

Result: no live transaction, but the acquisition screen is materially safer and more precise.
