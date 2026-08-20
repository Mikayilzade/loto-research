# H120 — FDJ Grand LOTO forced-distribution / full-space bound

Updated: 2026-08-20
Status: **RECENT REAL FORCED-DISTRIBUTION MECHANISM VALIDATED / FULL-SPACE GUARANTEE REJECTED UNDER A VERY FAVORABLE SUBSIDY BOUND / NO SUCCESS**

## Question
Could the French FDJ Grand LOTO event become a buy-the-pot guarantee because the jackpot is guaranteed and, if no rank-1 winner exists, the jackpot is redistributed to lower prize tiers rather than rolling away?

## Verified 2026 event mechanics
For the 26 June 2026 Grand LOTO de l'été, official FDJ material states:
- choose 5 numbers from 49 and 1 Chance number from 10;
- stake = **€5 per simple line**;
- jackpot = **€20,000,000**;
- if no rank-1 winner exists, the €20m jackpot is **redistributed to lower prize tiers** instead of rolling forward;
- each validated line receives a Grand LOTO code;
- **100 codes win €20,000 each**, i.e. a further €2,000,000 fixed code-prize board.

Official sources:
- https://www.fdj.fr/mag/actus/article-grand-loto-20M-euros-260626
- https://www.fdj.fr/mag/questions/article-comment-tenter-sa-chance-grand-loto-20M-euros-260626
- https://www.fdj.fr/jeux-de-tirage/grandloto?jeu=loto

FDJ's current LOTO page states that from 4 May 2026 the player-return rate is **54.35%**. This is the current LOTO-family benchmark used only as a deliberately favorable player-funded-return screen, not as a claim that every euro of a Grand LOTO ticket is independently guaranteed back at that rate.

Source:
- https://www.fdj.fr/jeux-de-tirage/loto

## Full-space acquisition
Number of simple outcome lines:

`N = C(49,5) * 10 = 19,068,840`.

At €5 per line:

`S = 19,068,840 * €5 = €95,344,200`.

Full coverage necessarily owns the realized 5+Chance combination, so in the literal full-space portfolio the no-rank-1 branch cannot occur because our own portfolio creates a rank-1 winner. The forced-redistribution feature is therefore not directly capturable by full coverage; it matters only to partial/uncovered portfolios.

That is the same structural incompatibility seen in other jackpot rolldown systems: buying every outcome removes the very state required for a no-jackpot-winner redistribution.

## Deliberately favorable subsidy upper screen
To avoid understating the mechanism, grant the buyer all of the following simultaneously:
1. the full current LOTO-family 54.35% return fraction on the **entire €95.3442m Grand-Loto spend** as though every euro attributable to our purchases were capturable by us;
2. the **entire €20m jackpot** as external value;
3. **all 100 code prizes** (€2m total), even though external tickets/codes exist and full ownership of code prizes is not guaranteed;
4. zero taxes, zero execution friction, zero sharing loss and no purchasing limits.

Player-funded return under this deliberately generous assumption:

`0.5435 * €95,344,200 = €51,819,572.70`.

Add the entire €22m headline jackpot + code board:

`€51,819,572.70 + €22,000,000 = €73,819,572.70`.

Favorable gross ratio:

`€73,819,572.70 / €95,344,200 = 77.4243%`.

Remaining deficit even under these buyer-favorable assumptions:

`€21,524,627.30`.

Equivalent subsidy hurdle: after granting the full €22m headline board, the player-funded return fraction would have to exceed approximately **76.925% of total spend** merely to break even before tax/execution/sharing. The official current LOTO-family return benchmark is 54.35%, far below that hurdle.

## Important conservatism / reopen gate
This packet intentionally does not claim that 54.35% is a contractual per-draw Grand-Loto floor. Instead it uses it as a generous screening benchmark and separately grants the complete €22m headline board to the buyer.

Reopen H120 only if primary Grand-Loto rules show one of the following materially stronger facts:
- a special-draw prize allocation above **76.925% of total stake** *in addition to* the €22m board;
- materially more than €22m of operator/reserve-funded external value guaranteed to this draw;
- a capped/closed ticket supply that lets one buyer atomically own all relevant codes/prize rights at a steep discount;
- a partial-coverage construction that captures forced redistribution without leaving any loss state.

## Historical control
The actual 26 June 2026 draw had **two jackpot winners** sharing the €20m jackpot and 100 €20k code winners. This illustrates the sharing problem in live play; the generous screen above already ignores that deterioration.

Official result:
- https://www.fdj.fr/jeux-de-tirage/loto/resultats/vendredi-26-juin-2026

## Conclusion
Grand LOTO has a real and unusually strong lottery-specific feature: a €20m jackpot that is forced into lower tiers if rank 1 is absent, plus a €2m fixed code board. But full-space acquisition costs **€95.3442m**, and full coverage itself prevents the no-rank-1 redistribution branch. Even after granting the buyer the whole €22m headline board and an extremely favorable 54.35% return on all own spend, gross recovery is only **77.4243%**.

**H120 REJECTED as a strict full-space guaranteed-profit route under verified 2026 economics.**

Terminal state remains: **NO SUCCESS; NOT EXHAUSTED**.
