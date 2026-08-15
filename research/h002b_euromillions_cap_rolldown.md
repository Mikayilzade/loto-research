# H002b — EuroMillions cap / rolldown / full-space guarantee

Updated: 2026-08-15
Status: **terminal guaranteed-profit path rejected; cap/rolldown remains structurally interesting only for EV, not guarantee**

## Current primary-source rules checked
Spain SELAE current help/rules pages state:
- 5 of 50 main numbers + 2 of 12 stars;
- price **€2.50 per simple bet**;
- jackpot odds **1 / 139,838,160**;
- **50% of collection is allocated to prizes**;
- jackpot starts at least €17m and is capped at **€250m**;
- each Spanish bet also receives an El Millón code, with one €1m Spanish winner, but that code prize is itself chance-based.

FDJ current 2026 operator material confirms the cap mechanism:
- jackpot can grow to **€250m**;
- at the cap it may be offered repeatedly;
- if still unclaimed on the terminal cap draw, the jackpot is redistributed to lower winning ranks.

Primary sources checked 2026-08-15:
- https://www.loteriasyapuestas.es/es/centro-de-ayuda/como-se-juega/jugar-a-euromillones
- https://www.loteriasyapuestas.es/es/centro-de-ayuda/como-se-juega/como-jugar-a-euromillones
- https://www.fdj.fr/mag/actus/article-jackpot-euromillions-209M-euros-100326

## Full-space identity
Combination space:

`C(50,5) * C(12,2) = 139,838,160` simple bets.

At €2.50 each:

`cost = €349,595,400`.

For any realized draw, complete coverage produces exact category counts:

| Match | Covered winning lines |
|---|---:|
| 5+2 | 1 |
| 5+1 | 20 |
| 5+0 | 45 |
| 4+2 | 225 |
| 4+1 | 4,500 |
| 3+2 | 9,900 |
| 4+0 | 10,125 |
| 2+2 | 141,900 |
| 3+1 | 198,000 |
| 3+0 | 445,500 |
| 1+2 | 744,975 |
| 2+1 | 2,838,000 |
| 2+0 | 6,385,500 |

The jackpot cap alone is **€99,595,400 below** full-space acquisition cost even if we were the sole jackpot winner and ignored every tax/execution issue.

## Decisive cap-rolldown incompatibility theorem
A terminal cap rolldown occurs only if there is **no 5+2 winner**.

Complete coverage contains the realized 5+2 combination by construction. Therefore our own portfolio guarantees that at least one jackpot-winning line exists.

Hence:

**A complete-coverage portfolio cannot simultaneously guarantee full outcome coverage and trigger the no-jackpot-winner condition required for the €250m cap rolldown to lower tiers.**

This closes the most attractive apparent guaranteed-arbitrage construction: buying the whole space on the terminal capped draw to collect the rolled-down €250m is logically impossible because buying the whole space prevents the rolldown event.

## Partial-coverage alternative
If we omit at least one combination so a no-jackpot-winner state remains possible, then there is at least one legal draw outside our jackpot coverage. The rolldown itself is also state-dependent and lower-rank pools are shared. Thus partial coverage does not yield an all-outcome positive-profit guarantee by itself.

## Sharing obstruction
EuroMillions jackpot and lower main-game tiers are shared pools. There is no useful pre-draw hard cap on the number of external winning bets. For a strict all-outcome guarantee, external duplicate entries therefore form an adverse legal branch that can dilute our share. This is the same terminal obstruction already identified for Powerball and Mega Millions.

## 50% prize-pool observation
SELAE states that 50% of collection goes to prizes. Our own complete-space purchase would contribute €349,595,400 of sales and €174,797,700 to the overall prize pool under that headline allocation. This does not create arbitrage: only a subset is allocated to any one tier, legacy jackpot reserves/carryovers are shared, and external winners can claim portions of the pools.

## Ancillary El Millón
Every Spanish EuroMillions bet receives an El Millón code and one €1m Spanish winner exists each draw. But full main-number coverage does not guarantee ownership of the randomly selected winning code while external tickets exist. It cannot repair the terminal guarantee.

## Conclusion
- Full-space cost: **€349.5954m**.
- Maximum jackpot: **€250m**.
- Complete coverage guarantees a 5+2 hit and therefore **prevents terminal cap rolldown**.
- Partial coverage leaves uncovered draw outcomes.
- External sharing remains unbounded by a useful pre-draw cap.

**H002b EuroMillions is REJECTED as a terminal guaranteed-profit strategy.**

The cap/rolldown remains relevant for positive-EV analysis and crowd-sharing optimization, but not for the project's strict guarantee criterion.
