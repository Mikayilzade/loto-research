# CHECKED_PROJECTS_AND_TESTS — H142 append

Updated: 2026-08-21
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H142 Virginia Keno 1-Spot** | Buy every one of the 80 distinct 1-Spot numbers for the same draw at $1 each | exactly 20 winners × $3 = **$60** on $80 face; deterministic ratio **75%** | **VALIDATED high cover ratio**; official Keno rules make all tiers except 10/10 fixed; `research/h142_virginia_keno_75pct_cover_rewards_threshold.md` |
| H142 subsidy theorem | Apply deterministic player-owned face subsidy/free play to full 1-Spot cover | positive pre-tax iff face discount `q > 25%`, equivalently pre-locked Keno-usable free play `F > $20` on $80 face | **VALIDATED threshold theorem**; `data/derived/h142_virginia_keno_subsidy_thresholds.csv` |
| H142 pari-mutuel control | Test public warning that Keno prizes can become pari-mutuel | official rules limit pari-mutuel conversion to 10-Spot match-10 after $2m liability cap; **all other payout values fixed** | **1-Spot crowd-sharing blocker CLOSED** |
| H142 Virginia Rewards | 5 points/$1, 250 points per free-play coupon, Keno eligible, max 5,000 points/month free-play redemption | useful architecture, but public rules retrieved do not lock coupon Keno denomination/value >$20 for target cover; first $80 earns 400 points only after purchase | **NOT sufficient current guaranteed subsidy / OPEN only with exact coupon denomination or >25% promo** |
| H142 execution | 80 same-draw tickets / terminal acceptance | Keno rules allow unaccepted play refund; tickets cannot cancel; one play per ticket; four-minute draw cycle | **NOT terminal SUCCESS** until complete basket is reliably accepted/locked or partial rejection cannot create loss |

## New no-repeat rule
Do not reopen ordinary Virginia Keno 1-Spot math: the 75% full-cover identity and fixed-payout status are proven. Reopen H142 only for genuinely new evidence on (a) >25% pre-committed player-owned subsidy, (b) exact Rewards coupon value/usability, (c) atomic/batch same-draw acceptance, or (d) tax/execution lock.
