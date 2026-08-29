# H354 — Spanish Lotería Nacional finite unique-series cover

Date: 2026-08-29
Result: **CLOSED — below break-even**

## Why this candidate mattered

Recent packets repeatedly failed because a nominally attractive top prize could be diluted by external duplicate winners. Spanish Lotería Nacional is structurally cleaner: a `number × series × fraction` décimo is a finite physical/issued identifier, and prizes attached to the billete are not shared with unrelated holders of the same number in other series.

The current Thursday product was confirmed active by SELAE results dated 27 Aug 2026. A 2026 official Thursday draw dossier specifies:
- 6 series;
- 100,000 billetes per series;
- €30 per billete;
- each billete divided into ten €3 décimos;
- €18,000,000 total issue;
- €12,600,000 total prizes, exactly 70%.

## Exact takeover screen

Choose one series and one fraction index, and acquire that fraction for every number 00000–99999.

This gives exactly **100,000 unique décimos** and costs:

`100,000 × €3 = €300,000`.

Because a series contains one billete of every participating number and every billete is divided equally into ten décimos, this portfolio owns one tenth of the complete prize allocation of one series, irrespective of the draw result.

Total prize allocation per series:

`€12,600,000 / 6 = €2,100,000`.

Our one-tenth fraction therefore receives exactly:

`€2,100,000 / 10 = €210,000`.

Thus:
- guaranteed gross: **€210,000**;
- cost: **€300,000**;
- guaranteed net: **−€90,000**;
- exact return: **70.0000%**.

There is no arithmetic uncertainty and no external duplicate-dilution branch to model. The entire issuance itself supplies a stronger upper-bound sanity check: buying all 6,000,000 décimos would cost €18m and the complete prize budget is only €12.6m.

## Closure

H354 is closed. This finite-ID construction solves the duplicate-control problem but fails the economics before acquisition friction, taxes, availability, or operational constraints are considered.

The useful pruning rule is stronger: for finite unique-ID lotteries, first compare the **entire guaranteed prize budget plus binding external subsidies** with the minimum complete-control acquisition cost. If that ratio is below 100%, deeper exact-cover work cannot create strict guaranteed profit.

Sources:
- SELAE 9 Apr 2026 Thursday dossier: https://www.loteriasyapuestas.es/f/loterias/documentos/Loter%C3%ADa%20Nacional/Dossier%20de%20prensa/DOSSIER%20PRENSA%20SORTEO%20LOTERIA%20NACIONAL%20JUEVES%209%20DE%20ABRIL%20DE%202026.pdf
- SELAE terminology: https://www.loteriasyapuestas.es/es/paginas-informativas/terminologia
- SELAE 27 Aug 2026 current Thursday result: https://www.loteriasyapuestas.es/es/loteria-nacional/resultados/loteria-nacional-premios-mayores-del-sorteo-del-27-de-agosto-de-2026
