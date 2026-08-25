# H268 VALIDATION — New Zealand Powerball terminal duplicate bound

Date: 2026-08-25
Result: **VALIDATED REJECTION / NO STRICT GUARANTEE**

## Independent arithmetic checks

Current pre-2026-09-13 matrix:
- `C(40,6) = 3,838,380`;
- × 10 Powerballs = **38,383,800** paired lines;
- × NZ$1.50 = **NZ$57,575,700** full-cover cost;
- fixed PB D7 count = `C(6,3) * C(33,3) = 109,120`;
- fixed PB D7 cash = **NZ$1,636,800**;
- Standard-Lotto D7 count across ten PB copies = **1,091,200**;
- rules value = **NZ$3,055,360**, but strict immediate cash floor used = **0** because the prize is four future bonus selections.

With legal external copies of the realised D1 line and the rules-minimum current prize-pool assumptions (60% pool less maximum reserve set-aside: 5% of Standard turnover and 10% of Powerball turnover), exhaustive integer scan `m=0..200,000` verifies:
- NZ$50m jackpot: minimum at **m=18,968**, gross **NZ$10,281,979.962637568**, ratio **0.17858193582774623**;
- NZ$60m sensitivity: minimum at **m=19,884**, gross **NZ$10,282,494.71341036**, ratio **0.17859087624484568**.

Enacted 2026-09-13 matrix:
- × 14 Powerballs = **53,737,320** paired lines;
- cost = **NZ$80,605,980**;
- PB D7 = **109,120 × NZ$20 = NZ$2,182,400**;
- PB D8 count = `C(6,2)*C(33,3)=81,840`;
- PB D8 = **NZ$982,080**;
- amended minimum PB pool 55% less unchanged maximum 10% reserve set-aside gives a conservative legal 45% available-turnover base before fixed tiers/pari allocations.

At NZ$60m jackpot, exhaustive integer scan `m=0..200,000` verifies:
- minimum at **m=23,175**;
- gross **NZ$15,122,347.333168669**;
- cost **NZ$80,605,980**;
- deficit **NZ$65,483,632.66683133**;
- ratio **0.18760825602726583**.

## Structural validation

For every purchased paired line `(S,p)`, there exists a legal drawing whose six winning Lotto numbers are exactly `S` and whose Powerball is exactly `p`. Therefore every non-empty portfolio has at least one legal draw state in which it produces Powerball Division 1 itself. Hence no non-empty portfolio can force the no-D1 terminal rolldown branch across all draw outcomes.

The duplicate counterexample is stronger for complete coverage: complete coverage guarantees one own Powerball D1 line, while a finite legal external block of copies of that same realised line dilutes the carried jackpot share. The model credits the associated extra turnover into lower prize pools rather than ignoring it. The resulting gross is still far below acquisition cost.

## Source gates checked

1. Lotto Rules 2025 rule 10: Standard selection NZ$0.70; Powerball selection NZ$0.80.
2. Rule 4 definitions: 6/40 Standard Lotto and Powerball 1..10 before the amendment.
3. Rules 25 and 29: prize pool minimums and maximum reserve set-asides.
4. Rule 30: current Powerball divisions, D1 allocation 94.720%, fixed D7 NZ$15.
5. Rules 32–34: terminal/no-further-jackpot and specified-date rolldown to next-lowest winning division.
6. Rule 26 / rule 59: Standard Lotto D7 value NZ$2.80, satisfied as four bonus Standard selections.
7. Lotto Amendment Rules 2026, effective 2026-09-13: PB 1..14; minimum PB pool 55%; D1 share 94.620%; fixed D7 NZ$20; new D8 NZ$12; fixed tiers excluded from ordinary reallocation/share rules.

Primary authority: New Zealand Legislation, `Lotto Rules 2025 (SL 2025/174)` and `Lotto Amendment Rules 2026 (SL 2026/51)`.

## Validation verdict

The H268 conclusion is safe: **the NZ Powerball terminal/Must-Be-Won mechanism is not a strict guaranteed-profit takeover under either the current 10-Powerball matrix or the enacted September 2026 14-Powerball matrix.** The rejection needs only one legal below-cost state; H268 provides explicit finite such states and also proves that portfolio coverage cannot force the no-D1 rolldown condition.
