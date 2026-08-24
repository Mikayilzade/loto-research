# H260 — DAILY GRAND Bonus Draw main-space cover bound

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: **REJECTED for strict guaranteed positive net profit**

## Question
Can Canada's DAILY GRAND promotional Bonus Draws turn a complete cover of the 5-number main space into a guaranteed-profit portfolio, avoiding the much larger 7-Grand-Number full-space cost tested in H032?

On June 18 and June 22, 2026, every valid DAILY GRAND play received three additional 5/49 Bonus Draws at no extra charge, each paying up to C$500,000 lump sum for matching all five main numbers.

## Official evidence
2026 DAILY GRAND Bonus Draw Game Conditions (approved 2026-05-29; effective 2026-06-18 and 2026-06-22):
https://assets.lotoquebec.com/ressources/assets/v3/assets/blt8296e79a7001648c/bltdae888c401cdbf6e/6a29619c1c149a52cda44e2b/2026-06_Grande_Vie_Bonus_Draw_Game_Conditions_EN-LQ.pdf

Current WCLC DAILY GRAND prize table:
https://www.wclc.com/games/daily-grand.htm

Rules used:
- ordinary play: 5 main numbers from 1–49 plus one Grand Number from 1–7; C$3 per selection;
- Bonus Draw ignores the Grand Number and uses only the five main numbers;
- three Bonus Draw selections are made per qualifying draw date;
- unique winning Bonus Selection: C$25,000/year for life or C$500,000 lump sum;
- duplicate winning selections share the C$500,000 liability.

## Cheapest deterministic Bonus-Draw cover
Buy every 5-subset of 49 exactly once:

`N = C(49,5) = 1,906,884 selections`.

Idealized minimum cost:

`S = 1,906,884 × C$3 = C$5,720,652`.

Each covered main set may carry any Grand Number. The proof therefore must hold for every possible Grand-Number assignment.

## Base-draw average upper bound
Uniformly average over all `C(49,5)×7 = 13,348,188` ordinary main+Grand outcomes. Every legal C$3 selection has the same cash expectation. To favor the player, ignore external sharing and grant the full C$7m top and C$500k second-prize lump sums whenever applicable; Free Play is assigned zero immediate cash value.

Per-selection favorable cash average:

`C$1.2736275515448239`.

For any Grand-Number assignment on the complete one-copy main-space cover, portfolio average ordinary-draw cash is therefore exactly:

`1,906,884 × 1.2736275515448239 = C$2,428,660`.

The minimum legal draw-state gross cannot exceed the average, so at least one ordinary draw state pays at most C$2,428,660 under this already favorable no-sharing model.

## Give the promotion its impossible best case
The cover contains the exact five-number combination for every Bonus Draw. Ignore the published sharing rule and give our portfolio the full C$500,000 in all three Bonus Draws:

`B_max = C$1,500,000`.

Then

`G_max = C$2,428,660 + C$1,500,000 = C$3,928,660`.

Against C$5,720,652 cost:
- gross upper ratio: **68.6750%**;
- deficit: **C$1,791,992**.

Thus some legal ordinary DAILY GRAND draw state remains strictly below stake even after granting all three promotional prizes without sharing.

## Why Grand-Number coloring cannot rescue it
The portfolio average is invariant under the assignment of the seven Grand Numbers because every individual selection has the same average over the complete ordinary draw-state space. If every state were profitable, the average would exceed cost; it does not.

Duplicating main combinations increases acquisition cost and, under actual Bonus Draw rules, can create internal sharing of the fixed C$500,000 liability. It cannot turn the fixed C$1.5m maximum three-draw subsidy into an everywhere-positive additive cover.

## Result
**REJECTED.** The three free DAILY GRAND Bonus Draws are a genuine nonlinear subsidy and a one-copy 5/49 cover guarantees hitting each bonus selection, but even an impossible no-sharing bonus grant plus favorable base-game cash reaches only 68.6750% of cover cost. Reopen only if a future promotion materially increases deterministic non-shareable Bonus Draw cash or lowers the acquisition hurdle.
