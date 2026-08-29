# H350 VALIDATION — Irish Lotto Plus Raffle

Validation date: 2026-08-29

## Independent arithmetic

For `M=10,000` raffle codes, `N` owned entries imply `min multiplicity <= floor(N/M)` by pigeonhole. At €500 per matching raffle entry and €1 incremental Lotto Plus cost per Play:

`ordinary gross floor <= 500*floor(N/10000)`

`ordinary net <= 500*floor(N/10000)-N`.

For `N=10000q+r`, this is `-9500q-r`, strictly negative for every positive integer `N`.

Representative certificates:
- N=9,999: gross-floor upper bound €0; cost €9,999; net <= **-€9,999**.
- N=10,000: gross-floor upper bound €500; cost €10,000; net <= **-€9,500**.
- N=10,001: gross-floor upper bound €500; cost €10,001; net <= **-€9,501**.
- N=100,000: gross-floor upper bound €5,000; cost €100,000; net <= **-€95,000**.

Executable sanity scan over `N=1..2,000,000`: **0 nonnegative cases**. The symbolic proof, not the finite scan, establishes all-N closure.

## Rule checks

Issue 8 confirms sequential four-digit entries `0000..9999`, one entry number per Lotto Plus Play, €1 per Play, fixed €500 match prize, and a €1m event that is either shared among matching Ticket Owners or awarded to one selected matching Ticket Owner. The €1m award is explicitly additional to the €500 ordinary raffle prize.

A legal external matching Ticket Owner therefore prevents a positive strict floor for the €1m component in the single-winner mode and creates external dilution in shared mode. No hard external-owner cap or ownership reservation was established.

## Inconclusive accounting

- identifier-count inconclusive: **0**
- cost/prize inconclusive: **0**
- arithmetic inconclusive: **0**
- closure-relevant inconclusive: **0**

H225-X* was not modified; it remains CLOSED / EXHAUSTED at H225-X20.
