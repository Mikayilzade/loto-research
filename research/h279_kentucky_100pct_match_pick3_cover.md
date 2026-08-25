# H279 — Kentucky Lottery 100% first-deposit match + Pick 3 exact cover

## Result

**Arithmetic strict-profit candidate found; not yet certified as globally executable.**

The Kentucky Lottery's live August 2026 promotion matches an eligible player's first-ever deposit by 100%, up to $250 in Bonus funds. Bonuses must be spent on Kentucky Lottery games purchased online. Deposited funds are also non-withdrawable until used for lottery purchases, while resulting prize winnings are tracked separately and may be withdrawn under the account rules.

Kentucky Pick 3 is available online. Current official Pick 3 rules allow a $0.50 Straight wager paying $300 at odds 1/1000 and $0.50 Front/Back/Split Pair wagers paying $30 at odds 1/100.

## Exact construction A — 100-pair cover

For one Pick 3 drawing, buy every Front Pair `00` through `99` exactly once at $0.50.

- selections: 100;
- lottery wallet required: $50;
- cash first deposit: $25;
- deterministic 100% match: $25;
- exactly one Front Pair wins for every possible 3-digit outcome;
- guaranteed withdrawable prize gross: $30;
- cash profit before tax/fees: **$5**;
- guaranteed gross / original cash deposit: **120%**;
- guaranteed profit / original cash deposit: **20%**.

## Exact construction B — 1000-Straight cover

Buy all `000` through `999` Straight wagers once at $0.50.

- selections: 1,000;
- lottery wallet required: $500;
- cash first deposit: $250;
- deterministic 100% match: $250 (promotion cap);
- exactly one Straight wins;
- guaranteed prize gross: $300;
- cash profit before tax/fees: **$50**;
- guaranteed gross / original cash deposit: **120%**.

The arithmetic is exact and does not rely on jackpot sharing, prize-pool EV, historical frequency, or random promotional selection.

## Why H279 is not yet promoted to global SUCCESS

The remaining issue is **execution certification, not arithmetic**.

1. Internet play requires the player to meet Kentucky account/identity rules and to be physically located within Kentucky when playing.
2. The Pick 3 rules expressly permit KLC to impose a prize-liability limit for a drawing and cut off sales if a wager would cause liability to exceed that limit; the limit need not be publicly announced.
3. The online Terms of Use separately reserve the right to refuse an attempted purchase.
4. Therefore the research cannot yet prove *before purchase* that all 100 required Pair wagers, or all 1,000 Straight wagers, will be accepted for the same draw. A partially accepted cover loses the deterministic floor.

This makes H279 the strongest deterministic-subsidy candidate found so far, but under the project's strict standard it is a **conditional arithmetic success / execution-data blocker**, not yet a rigorous global SUCCESS.

## High-value next check

Determine whether Kentucky iLottery provides an atomic or pre-validated multi-selection purchase mechanism for Pick 3, or whether published/observable sales controls guarantee that a uniform $30 liability increment across all outcomes can be accepted when submitted sufficiently early. If full same-draw acquisition can be certified, the 100-pair construction is an immediate strict-profit theorem for an eligible account while the 100% first-deposit promotion remains live.

## Sources checked

- Kentucky Lottery current Promotions page, August 2026 First Ever Deposit 100 Percent Match.
- Kentucky Lottery Pick 3 official short rules (minimum wagers, fixed payouts, online availability, liability-limit clause).
- Kentucky Lottery Fun Club / iLottery Terms of Use (wallet accounting, bonus-first purchase order, physical-location requirement, purchase refusal, withdrawal of prize winnings).

Reproducible arithmetic: `src/loto_research/h279_kentucky_100pct_match_pick3_cover.py`.
Derived result: `data/derived/h279_kentucky_100pct_match_pick3_cover.json`.
