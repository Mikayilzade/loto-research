# H263 — Spain Lotería de Navidad 2026 exact full-cover bound

## Question
Can a fixed-per-winning-number lottery avoid the sharing failure seen in pari-mutuel jackpots and become strictly profitable under complete number-space coverage?

## Official 2026 structure
SELAE's official fourth-quarter 2026 prize programme states that the 22 December 2026 Christmas draw has **205 series of 100,000 tickets at EUR200**, total issue EUR4.1bn, with **70% allocated to prizes** (EUR2.87bn). It also states that each series distributes **EUR14,000,000** and that tickets are divided into **EUR20 décimos**.

The official 2026 calendar independently lists draw 102 on 22 December 2026 with 205 series, 100,000 numbers per series and EUR4.1bn total issue. SELAE's play page confirms a décimo costs EUR20 and the player may choose a five-digit number subject to availability.

Official sources:
- https://www.loteriasyapuestas.es/f/loterias/documentos/Loter%C3%ADa%20Nacional/programas%20de%20premios/PROGRAMAS_PREMIOS_CUARTO_TRIMESTRE_2026_SABADOS.pdf
- https://www.loteriasyapuestas.es/f/loterias/documentos/Loter%C3%ADa%20Nacional/Calendarios/CALENDARIO_CUARTO_TRIMESTRE_2026_SABADO.pdf
- https://www.loteriasyapuestas.es/es/centro-de-ayuda/como-se-juega/jugar-a-loteria-de-navidad

## Exact domination test
Grant an execution condition stronger than reality: suppose we can buy exactly one EUR20 décimo for **every one of the 100,000 five-digit numbers in the same series**.

Cost:

`100,000 * EUR20 = EUR2,000,000`.

Because every number in that series is owned once at the décimo level, the draw merely permutes which owned number receives which fixed prize. A décimo is one tenth of a EUR200 full ticket, so this portfolio receives exactly one tenth of the complete EUR14,000,000 per-series prize schedule:

`EUR14,000,000 / 10 = EUR1,400,000`.

Therefore the full-cover return is exactly:

`EUR1,400,000 / EUR2,000,000 = 70%`.

Guaranteed deficit: **EUR600,000**. The base game therefore needs a deterministic effective subsidy/discount of **more than 30% of stake** merely to cross break-even.

This is stronger than an expected-value calculation: under the hypothetical complete cover the gross result is invariant across draw outcomes. External ticket holders do not dilute these fixed prizes in the manner of a shared jackpot; nevertheless the official payout fraction itself prevents strict profit.

## Execution note
Actual complete same-series acquisition is not assumed feasible. SELAE explicitly notes that a chosen number may be unavailable because it was already sold. That only weakens execution; it is unnecessary for the negative result because even impossible-perfect full coverage returns only 70%.

## Result
**REJECTED for strict guaranteed profit without an external deterministic subsidy.** Spain's 2026 Christmas Lottery is a useful example of a non-shareable, fixed-prize full-cover mechanism, but complete coverage locks in the official **70%** payout ratio rather than creating an arbitrage.

Reopen only if a deterministic discount/cashback/subsidy applicable to the whole required portfolio exceeds the exact 30% hurdle after all fees and eligibility constraints.
