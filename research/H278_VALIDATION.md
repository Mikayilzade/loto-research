# H278 VALIDATION

Validated: 2026-08-26
Packet: **H278 — Georgia Lottery iHOPE 50% first-deposit bonus exact-cover screen**
Verdict: **REJECTED for checked compact exact-cover routes; global research NOT EXHAUSTED**

## Independent arithmetic gates

Promotion gate:
- qualifying first deposit bonus = 50%, maximum bonus $125;
- maximum fully matched cash deposit = $250;
- maximum restricted playing balance = $375;
- strict cash-profit wager-return hurdle under the deliberately favourable assumption that all prizes become withdrawable cash = `250/375 = 2/3`.

Georgia FIVE gate:
- enumerated universe = exactly 100,000 five-digit plays;
- exact mutually-exclusive payout classification reproduces invariant gross **$53,650**;
- ratio = **0.5365**;
- after 1.5x matched purchasing power = **0.80475 < 1**.

CASH POP gate:
- exactly 15 possible draw numbers;
- complete cover cost = `15w`;
- minimum currently published assigned prize = `5w`;
- legal all-minimum assignment state gives guaranteed-cover floor `5/15 = 1/3`;
- after 1.5x matched purchasing power = **0.5 < 1**.

KENO base full-cover gate:
- for every spot count `k=1..10`, all `C(80,k)` selections are counted;
- for a fixed 20-number draw, exact multiplicity for `t` matches is `C(20,t) C(60,k-t)`;
- maximum base full-cover ratio occurs at **7 Spot = 0.6502635236812452**;
- matched-deposit equivalent = **0.9753952855218677 < 1**.

KENO BULLS-EYE gate:
- BULLS-EYE cost is exactly one additional base wager, so total cover cost doubles;
- for `t` KENO matches, selections containing the BULLS-EYE are counted as `C(19,t-1) C(60,k-t)` and those excluding it as `C(19,t) C(60,k-t)`;
- maximum checked BULLS-EYE ratio occurs at **4 Spot = 0.6433439977743776**;
- matched-deposit equivalent = **0.9650159966615663 < 1**.

KENO MULTIPLIER gate:
- option doubles base cost;
- official mechanism includes a legal `None` multiplier result;
- therefore it cannot improve a strict worst-case floor over the corresponding base ticket.

## Closure scope

H278 rigorously closes the current 50% deposit-match route for:
1. Georgia FIVE additive portfolios via exact symmetry-average bound;
2. CASH POP complete-number covers via explicit legal minimum-prize assignment;
3. base KENO complete-combination covers for every 1–10 Spot size;
4. KENO+BULLS-EYE complete-combination covers for every 1–10 Spot size;
5. MULTIPLIER as a strict-guarantee enhancer because of the legal `None` branch.

It does not assert a universal theorem over every Georgia Lottery product. The global state remains **NO SUCCESS; NOT EXHAUSTED**.
