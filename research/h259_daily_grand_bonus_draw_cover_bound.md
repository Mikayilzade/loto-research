# H259 — DAILY GRAND Bonus Draw main-space cover bound

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: **REJECTED for strict guaranteed positive net profit**

## Question

Can Canada's DAILY GRAND promotional Bonus Draws turn a complete cover of the 5-number main space into a guaranteed-profit portfolio, avoiding the much larger 7-Grand-Number full-space cost tested in H032?

This is a materially different nonlinear construction from H032: on the June 18 and June 22, 2026 Bonus Draw dates, every valid DAILY GRAND play received **three additional 5/49 Bonus Draws at no extra charge**, each paying up to C$500,000 lump sum for matching all five main numbers.

## Current official evidence

Official 2026 DAILY GRAND Bonus Draw Game Conditions (approved 2026-05-29; effective 2026-06-18 and 2026-06-22):
https://assets.lotoquebec.com/ressources/assets/v3/assets/blt8296e79a7001648c/bltdae888c401cdbf6e/6a29619c1c149a52cda44e2b/2026-06_Grande_Vie_Bonus_Draw_Game_Conditions_EN-LQ.pdf

Official WCLC DAILY GRAND page / current prize table:
https://www.wclc.com/games/daily-grand.htm

Key rules:
- ordinary play: choose 5 main numbers from 1–49 plus one Grand Number from 1–7; C$3 per selection;
- each Bonus Draw uses only the five main numbers;
- three Bonus Draw selections are made per qualifying draw date;
- a unique winning Bonus Selection receives C$25,000/year for life or C$500,000 lump sum;
- if a winning Bonus Selection occurs on multiple winning selections/tickets, the C$500,000 lump-sum liability is divided among them.

## Cheapest deterministic Bonus-Draw cover

To guarantee owning the exact five-number combination drawn in every Bonus Draw, buy each 5-subset of 49 exactly once:

`N = C(49,5) = 1,906,884 selections`.

Each such selection must carry some Grand Number, but the Bonus Draw ignores it. Therefore the idealized minimum acquisition cost is

`S = 1,906,884 × C$3 = C$5,720,652`.

The Grand Number attached to each covered main set may be assigned arbitrarily. We therefore need a bound valid against **every possible assignment**, not merely the simple construction where all tickets use the same Grand Number.

## Base-draw average upper bound

Take the ordinary DAILY GRAND draw state uniformly over all

`C(49,5) × 7 = 13,348,188`

main+Grand outcomes.

Every legal C$3 selection has the same average cash payout under this uniform state distribution. For an intentionally player-favorable upper bound, ignore external sharing and grant the full headline C$7,000,000 top lump sum and C$500,000 second-prize lump sum whenever a single selection matches those categories. Exclude Free Play from cash.

Using the current prize table, the per-selection cash expectation under this favorable no-sharing model is:

`C$1.2736275515448239`.

Therefore **for any assignment of Grand Numbers to the 1,906,884 covered main combinations**, the average ordinary-draw cash gross of the whole portfolio is exactly:

`1,906,884 × 1.2736275515448239 = C$2,428,660`.

Because the minimum over legal ordinary draw states cannot exceed the average, there exists at least one ordinary draw state in which base cash gross is at most **C$2,428,660**. Real jackpot/second-prize sharing only lowers this upper bound.

## Give the promotion its impossible best case

The cover contains every 5-number main combination exactly once, so it contains a winner in each of the three Bonus Draws.

Now deliberately ignore the published sharing rule and grant our portfolio the entire C$500,000 liability in **all three** Bonus Draws:

`B_max = 3 × C$500,000 = C$1,500,000`.

Thus the average-state / best-possible-promotion upper bound is

`G_max = C$2,428,660 + C$1,500,000 = C$3,928,660`.

Against cost C$5,720,652:

- gross upper ratio: **68.6750%**;
- deficit: **C$1,791,992**.

Therefore at least one legal ordinary DAILY GRAND draw state leaves this complete Bonus-Draw-cover portfolio strictly below stake **even after giving it all three Bonus Draw prizes without any sharing at all**.

## Why a different Grand-Number assignment cannot rescue it

The proof does not assume a particular Grand-Number coloring. Each purchased selection has identical average payout over the uniform ordinary draw-state space, so the portfolio average is invariant under how the seven Grand Numbers are assigned to the 1,906,884 covered main sets. If every draw state were profitable, the average would also exceed cost; it does not.

Buying extra selections to duplicate main combinations can only increase cost. Under the actual Bonus Draw rule it can also create internal sharing of the fixed C$500,000 Bonus Draw liability. Therefore duplication does not invalidate the closure of the minimum exact-cover construction and cannot turn the fixed three-draw C$1.5m maximum subsidy into an everywhere-positive guarantee by additive repetition.

## Result

**REJECTED.** DAILY GRAND's three free Bonus Draws are a genuine externally funded nonlinear subsidy and a one-copy 5/49 cover guarantees hitting all three bonus selections. Nevertheless the subsidy is far too small: even an impossible no-sharing C$1.5m bonus grant plus a player-favorable no-sharing ordinary-draw average reaches only **68.6750%** of the C$5.720652m acquisition cost. Hence some legal ordinary draw state must lose money.

Reopen only if a future DAILY GRAND promotion materially increases deterministic fixed Bonus Draw cash beyond the exact covering deficit, changes ticket pricing, or supplies a separately guaranteed non-shareable award large enough to cross the bound.
