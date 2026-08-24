# H256 — New Jersey Quick Draw Progressive 50% Bonus Hours full-cover closure

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: **REJECTED for guaranteed-profit full coverage**

## Question

Can the currently scheduled New Jersey Quick Draw Progressive **50% Bonus Hours** promotion turn a controlled full combinatorial cover into a strictly positive all-draw cash result?

This is a high-value test because the promotion is current, deterministic at the qualifying-ticket level, applies to player-selected Quick Draw numbers, and does not require a jackpot/rolldown no-winner event.

## Current primary evidence

Official NJ Lottery Quick Draw page:
https://www.njlottery.com/en-us/drawgames/quickDraw.html

Official 2026 Bonus Hours rules (effective 2026-07-02):
https://www.njlottery.com/content/dam/portal/pdfs/drawgames/quickdraw/promo-rules/Official-Rules-Quick-Draw-Full-Network-BONUS-HOURS-Effective-07_02_2026_V2.pdf

Official Quick Draw Progressive game rules (effective 2024-03-21):
https://www.njlottery.com/content/dam/portal/pdfs/drawgames/quickdraw/Quick_Draw_Progressive_Game_Rules_effective_3.21.24.pdf

Official Multiplier addendum:
https://www.njlottery.com/content/dam/portal/pdfs/drawgames/quickdraw/Quick_Draw_Game_Rules_Addendum_Multiplier_effective_3.21.24.pdf

Verified current facts:
- Bonus Hours schedule runs on specified Thursdays from 2026-07-02 through 2026-12-31; the next listed date after this checkpoint is **2026-08-27, 5–7 p.m.**
- A qualifying wager is **$10 or more on a single Quick Draw Progressive ticket** at a licensed NJ retailer during the promotion period.
- Eligible purchases may include BULLSEYE, Double BULLSEYE or Multiplier.
- An eligible ticket prints: `THIS TICKET QUALIFIES / FOR A 50% BONUS / IF IT IS A WINNER. / (JACKPOT EXCLUDED)`.
- The 50% increase **never applies to the Progressive Jackpot**.
- Player-selectable base wager amounts include $1, $2, $3, $4, $5 and $10 per drawing, so the $10 qualification threshold does not prevent controlled number selection.
- Quick Draw uses an 80-number matrix and draws 20 winning numbers; the player chooses 1–10 spots.
- BULLSEYE doubles the base wager cost; Double BULLSEYE triples it.
- For 9-spot and 10-spot prizes, combined liability is capped at $3,000,000 and can become pari-mutuel. Ignoring that cap is therefore player-favorable for an upper-bound screen.

The promotion rules also reserve broad modification/cancellation/disqualification discretion. That would independently prevent a terminal guarantee, but H256 does **not need** that contractual blocker: the nominal mathematics already stays below break-even.

## Exact full-cover identities

For a k-spot base game, buy every k-subset of the 80-number matrix. Number of controlled lines:

`N_k = C(80,k)`.

For any realized 20-number winning set, exactly

`C(20,m) * C(60,k-m)`

covered lines match exactly `m` numbers. Therefore the aggregate base payout is outcome-independent.

### BULLSEYE

There is one BULLSEYE number among the 20 drawn numbers. For exactly `m` total matches:
- lines containing the BULLSEYE: `C(19,m-1) * C(60,k-m)`;
- lines not containing it: `C(19,m) * C(60,k-m)`.

Use the published BULLSEYE prize for the first count and ordinary Quick Draw prize for the second. Cost is `2*N_k` base-dollar units.

### Double BULLSEYE

There are two BULLSEYE numbers among the 20. If a covered line contains `b` of them (`b=0,1,2`) while matching `m` total winning numbers, the exact count is

`C(2,b) * C(18,m-b) * C(60,k-m)`.

Use the published ordinary / Match One / Match Both prize column for `b=0/1/2`. Cost is `3*N_k` base-dollar units.

For every fixed-prize branch, Bonus Hours multiplies the winning amount by 1.5. The Progressive Jackpot is excluded and therefore is not included in the deterministic floor.

## Exact results

| Spot | Base +50% | BULLSEYE +50% | Double BULLSEYE +50% |
|---:|---:|---:|---:|
| 1 | 75.0000% | 76.8750% | 77.5000% |
| 2 | 90.1899% | **82.2389%** | **84.4937%** |
| 3 | 89.4961% | 80.6725% | 83.0915% |
| 4 | 89.6042% | 79.2700% | 82.1930% |
| 5 | **90.4791%** | 77.0030% | 79.3008% |
| 6 | 89.6810% | 75.8377% | 78.3935% |
| 7 | 89.3037% | 76.0585% | 78.4522% |
| 8 | 89.3512% | 74.3454% | 76.4486% |
| 9 | 89.4612% | 72.5018% | 75.1876% |
| 10 | 90.2332% | 77.4587% | 80.6599% |

Best deterministic nominal return anywhere in the controlled base/BULLSEYE/Double-BULLSEYE full-cover family is therefore the **5-spot base game at 90.4791%**. It still loses **9.5209% of stake before taxes, execution cost, retailer capacity, claim friction or any 9/10 pari-mutuel reduction**.

The unusually small 2-spot state space does not rescue the add-ons: even with the full +50% bonus, BULLSEYE reaches only 82.2389% and Double BULLSEYE 84.4937%.

## Multiplier strict branch

The official Multiplier is selected once per Quick Draw drawing from `{1X,2X,3X,4X,5X,10X}`. **1X is a legal outcome with 40% probability.** The add-on doubles the base wager cost.

In the legal 1X branch the Multiplier contributes no payout increase. Even granting the Bonus Hours +50% to every base fixed prize, the best base 5-spot fixed return becomes at most

`0.9047914111 / 2 = 0.4523957056`,

or **45.2396% of total Multiplier stake**. Thus Multiplier cannot create a strict all-outcome guarantee. BULLSEYE/Double-BULLSEYE prizes are explicitly not multiplied, so combining add-ons cannot remove this 1X blocker.

## Progressive Jackpot cannot be imported into the guarantee

Each Quick Draw Progressive ticket receives nine `Your Jackpot Numbers` randomly from the system. The player does not control those nine numbers, and the Bonus Hours 50% increase explicitly excludes jackpot wins. A legal execution branch exists in which none of the purchased tickets' random jackpot sets wins, so the strict guaranteed jackpot contribution is **$0**.

Expected progressive value is therefore irrelevant to the terminal guarantee test.

## Conclusion

**REJECTED.** The active 50% Bonus Hours promotion is a real deterministic payout uplift on qualifying fixed prizes, but it is not large enough. Exact outcome-independent full coverage remains below stake for every base spot 1–10 and for every BULLSEYE / Double-BULLSEYE spot 1–10. Multiplier has a legal 1X branch and the Progressive Jackpot has a zero-win branch.

This closes the current NJ Quick Draw Progressive 50% Bonus Hours controlled full-cover class. Reopen only if the guaranteed non-jackpot uplift materially exceeds the exact deficit (best current base hurdle: >65.8914% uplift rather than 50%), or rules create a separately guaranteed subsidy not financed by additional wager cost.

Reproduction:
- `src/loto_research/h256_nj_quick_draw_bonus_hours.py`
- `data/derived/h256_nj_quick_draw_bonus_hours.json`
