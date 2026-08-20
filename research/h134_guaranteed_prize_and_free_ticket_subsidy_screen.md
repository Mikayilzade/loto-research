# H134 — guaranteed-prize subscriptions and free-ticket subsidy screen

Updated: 2026-08-20
Status: **FALSE-SUBSIDY CLASSES FORMALIZED / CURRENT LIVE EXAMPLES REJECTED / NO SUCCESS**

## Goal
Extend H133's deterministic subsidy threshold by distinguishing three promo assets that are often advertised with similar face values but have very different worst-case cash value:

1. **withdrawal-ineligible wallet credit** that can be directed into a deterministic complete cover;
2. **a free random lottery ticket** that can legally return zero;
3. **a guaranteed prize promise** that requires future paid participation.

For strict guaranteed-profit research, only cash that survives every legal outcome may be counted in the floor.

## General extension of the H133 theorem
Let:
- `C` = external cash required from the player;
- `P` = deterministic cash payout from the covered base game(s);
- `B_d` = deterministic game-eligible subsidy that can be directed into the cover;
- `F_r` = face value of free random tickets;
- `G` = guaranteed cash/prize amount that is contractually owed after satisfying all conditions;
- `K` = mandatory future cost needed to vest `G`.

Strict pre-tax guaranteed profit satisfies:

`GuaranteedProfit = P + G - (C + K - B_d)`

A free random ticket has strict floor:

`floor(F_r) = 0`

unless its own rules guarantee a positive cash payout in every ticket state.

Therefore **free-ticket face value must not be added to deterministic subsidy `B_d`**. It may improve EV, but not the guaranteed cash floor.

Similarly, a future prize promise should be counted as `G` only after all mandatory vesting costs `K` are included.

---

## Current live screen 1 — The Scotto "Play Free Until September" + guaranteed prize

Official terms checked 2026-08-20:
- sign up between 2026-07-24 and 2026-08-20;
- daily draws are free until the first subscription payment on 2026-09-01;
- subscription price is **£11.50/month**;
- players who remain subscribed for their first 12 months are guaranteed at least **£12** if they do not otherwise win a daily prize;
- cancelling before 12 months removes entitlement to the promised prize;
- the operator reserves the right to vary/cancel the promotion by website notice;
- the offer is restricted to residents of Great Britain.

Primary sources:
- https://playthescotto.com/play-free/?Slug=playfree
- https://playthescotto.com/terms-conditions/
- https://playthescotto.com/help/?Slug=help

### Worst-case economics
The free pre-September daily draws are genuine zero-cost lottery exposure, but they do not guarantee any payout.

To vest the explicit first-year guaranteed prize, the player must remain active for 12 months. Using the published subscription cost:

- mandatory paid subscription cost = `12 * £11.50 = £138.00`;
- guaranteed prize floor = `£12`;
- strict guaranteed return ratio = `£12 / £138 = 8.6957%`;
- strict guaranteed profit = `£12 - £138 = -£126` before any transaction/friction cost.

If the player wins another qualifying prize earlier, that does not improve the strict minimum because the promotion only guarantees that some prize will occur; the floor remains at least £12, not total prizes above total subscription spend.

Result: **REJECTED guaranteed-profit route**. The offer is a real guaranteed-prize mechanism but the guarantee is far smaller than the mandatory vesting cost.

---

## Current live screen 2 — Hoosier Lottery retailer buy-X/get-free-scratch promotions

Official retailer promotion page checked 2026-08-20 lists current examples including:

- Murphy USA (2026-08-05 to 2026-09-27): buy two $5 `100,000 Gold Bar` Scratch-offs in one transaction and **may receive a free $1 Scratch-off**;
- Village Pantry (2026-08-04 to 2026-09-27): buy one $10 `Go For The Green` Scratch-off and **may receive a free $1 Scratch-off**.

Primary source:
- https://hoosierlottery.com/promotions-events/retailer-promotions/

These offers have nominal promo rates around 9.09% of bundle face value (`$1 free` on `$10 paid + $1 free`). But for a strict guarantee:

- the purchased scratch tickets can legally lose;
- the free $1 scratch can legally lose;
- therefore bundle minimum cash payout is **$0** unless a specific pack/ticket rule proves otherwise.

Thus the free ticket has positive EV/entertainment value but **zero guaranteed cash subsidy**.

Result: **REJECTED as deterministic subsidy**. Do not add the $1 face amount to `B_d` in H133-style coverage calculations.

---

## Current live screen 3 — free one-off lottery ticket events

Hoosier Lottery also advertised a free $1 Scratch-off on Hoosier Lottery Day (2026-08-15), one per eligible visitor while supplies lasted.

Primary source:
- https://hoosierlottery.com/promotions-events/state-fair/

This is a true zero-cost free-roll and is positive EV to an eligible attendee, but strict worst-case profit is still exactly `$0` because the free ticket can lose. It can never satisfy terminal SUCCESS under the project's strict positive-profit definition.

Result: **POSITIVE-EV FREE-ROLL CLASS VALIDATED / STRICT GUARANTEE REJECTED**.

---

## Reusable screening rule
When scanning current lottery promotions, classify the benefit before comparing percentages:

### A. Deterministic usable subsidy
Examples: wallet credit or ticket discount that can be applied to a player-chosen deterministic coverage. Count at usable amount, subject to cap and eligibility.

### B. Random free ticket / bonus draw
Strict value = **0** unless every legal ticket/draw outcome pays positive cash. Do not count face value as subsidy.

### C. Guaranteed prize after paid vesting
Count the guaranteed amount `G`, but subtract every mandatory subscription/purchase/holding cost needed to vest it. Screen using `G > K` before combining with any base-game floor.

### D. Random sweepstakes / second chance
Strict value = **0** because a legal no-win branch remains.

This prevents false positives where a promotion advertises 50%-100% nominal value but contributes little or nothing to the all-outcomes cash floor.

## Result
**NO SUCCESS.**

H134 closes two superficially attractive subsidy branches:
- free random tickets cannot repair a deterministic coverage deficit because their strict cash value is zero;
- guaranteed-prize subscriptions must be evaluated net of mandatory vesting cost, and the current Scotto offer has only an ~8.70% guaranteed return floor.

## Next priority
Continue H133/H134 search only for promotions where the benefit is **deterministic and player-owned before the draw**: direct discount, unrestricted lottery wallet credit, fixed cash coupon, guaranteed per-block cash award, or a free ticket whose own rules guarantee positive cash in every state. Prioritize effective deterministic subsidy above the exact `C-P` deficit of compact non-shareable coverage.
