# H278 — Georgia Lottery 50% first-deposit bonus exact-cover screen

Date checked: 2026-08-26
State: **CLOSED / REJECTED for checked compact exact-cover routes**

## Mechanism

Georgia Lottery currently advertises a one-time iHOPE promotion for players who have never deposited: the first qualifying deposit of at least $10 receives a 50% bonus, capped at $125. A $250 cash deposit therefore creates at most $375 of restricted lottery purchasing power. Both deposited and bonus funds are restricted to lottery purchases and cannot themselves be withdrawn.

This is a genuine deterministic external subsidy, so it is structurally more interesting than a random second-chance raffle. Under a deliberately player-favourable assumption that every resulting lottery prize is immediately usable as cash, strict profit from spending the matched balance requires a deterministic lottery return greater than `1 / 1.5 = 66.6666667%` of wagered funds.

Promotion source: https://www.galottery.com/en-us/player-zone/player-zone-promotions.html

## 1. Georgia FIVE exact cover

Georgia FIVE uses five digits 0–9, $1 per play. The current fixed table ranges from $10,000 for all five exact through lower prefix/suffix matches.

An exact enumeration of all 100,000 five-digit plays against any fixed outcome gives:

- cover cost: **$100,000**;
- invariant gross: **$53,650**;
- wager return: **53.6500%**;
- even after multiplying purchasing power by 1.5, gross/cash-deposit equivalent: **80.4750%**.

Because the game is symmetric under relabelling of the winning five-digit outcome, the same average-return ratio applies to every primitive play and therefore to every nonnegative additive portfolio. Since minimum legal-outcome gross cannot exceed average gross, the 50% deposit match cannot turn Georgia FIVE into an everywhere-profitable additive portfolio.

Game source: https://gas-origin2.galottery.com/en-us/games/draw-games/georgia-five.html

## 2. CASH POP all-number guarantee

CASH POP draws one of 15 numbers. Online players may cover all 15 numbers; the site explicitly calls this guaranteed to win. For every wager level currently published, the smallest assigned prize is exactly 5 times the per-number wager. Prize amounts are randomly assigned and revealed on the purchased ticket.

For any number of complete 15-number covers, a legal worst case is that every purchased number receives the minimum 5x prize. Therefore:

- cost per complete cover = `15w`;
- guaranteed cash prize floor = `5w`;
- exact worst-case ratio = **1/3 = 33.3333%**;
- after a 50% matched bankroll, guaranteed gross/cash-deposit equivalent = **50.0000%**.

Buying multiple copies does not change this ratio. Retail-only instant wins do not help this online deposit promotion route.

Game source: https://www.galottery.com/en-us/games/draw-games/cash-pop.html

## 3. KENO! exact full-combination covers

KENO draws 20 of 80 numbers and allows 1–10 Spot wagers. For each spot size `k`, H278 buys every `C(80,k)` selection and counts exactly how many tickets match `t` of the 20 drawn numbers: `C(20,t) C(60,k-t)`. This makes the gross invariant across draw outcomes.

All base-game exact-cover ratios are below the 2/3 subsidy hurdle. The best is **7 Spot**:

- base exact-cover ratio: **65.0263524%**;
- with 50% deposit bonus measured against original cash deposit: **97.5395286%**.

So even the best checked base KENO cover remains below cash break-even.

BULLS-EYE doubles the base ticket cost. H278 additionally counts whether each covered selection contains the one BULLS-EYE number among the 20 winners. The best checked BULLS-EYE cover is **4 Spot** at **64.3343998%** of wager cost, or **96.5015997%** of original cash deposit after the 50% bonus.

MULTIPLIER cannot improve a strict guarantee: it doubles the base cost and the official mechanism includes a legal `None` multiplier branch, so a worst-case proof may select that branch.

KENO source: https://www.galottery.com/en-us/games/draw-games/keno.html

## Result

The current 50% first-deposit match is a real deterministic subsidy, but it does **not** cross the exact guarantee threshold for the compact fixed-payout constructions checked here:

- CASH POP complete number cover: 33.3333% wager floor;
- Georgia FIVE: 53.6500% symmetric exact-return bound;
- best base KENO complete-combination cover: 65.0263524%;
- best BULLS-EYE KENO cover: 64.3343998%;
- MULTIPLIER has a legal no-multiplier branch while doubling cost.

The near miss is KENO 7 Spot: the promotion lifts the exact full-cover return only to **97.5395% of deposited cash**, still short of break-even before any tax, account, eligibility, execution, or withdrawal friction.

This packet does **not** claim every Georgia Lottery product is exhausted. It closes these compact exact-cover routes under Promotion 27012. A future continuation should either inspect a materially higher deterministic subsidy, or a different Georgia product with a rigorously provable worst-case wager return above **66.6667%**.

Reproducible arithmetic:
- `src/loto_research/h278_georgia_deposit_bonus_cover_bound.py`
- `data/derived/h278_georgia_deposit_bonus_cover_bound.json`
