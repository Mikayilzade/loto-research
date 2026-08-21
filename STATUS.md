# STATUS

Updated: 2026-08-21
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H150 — Missouri Club Keno marked-ball full-cover theorem (Bulls-Eye / Double Bulls-Eye / Multiplier)**.

### H150 major result
H149's exact 20-of-80 full-cover theorem was extended to Keno games where one or two of the 20 drawn balls are specially marked.

For Bulls-Eye (one distinguished winning ball), if every k-subset of the 80 numbers is purchased and a ticket has j total drawn-number matches:
- no marked ball: `C(19,j)C(60,k-j)` tickets;
- marked ball included: `C(19,j-1)C(60,k-j)` tickets.

Therefore with ordinary payout `A_j` and Bulls-Eye payout `B_j`, deterministic gross is:

`G_BE=sum_j [A_j C(19,j)C(60,k-j)+B_j C(19,j-1)C(60,k-j)]`.

For Double Bulls-Eye (two marked winning balls), exact ticket counts with 0/1/2 marks are:
- `C(18,j)C(60,k-j)`;
- `2C(18,j-1)C(60,k-j)`;
- `C(18,j-2)C(60,k-j)`.

Current Missouri official paytables were screened exactly for Spots 1-10.

Best current deterministic/nominal ratios:
- ordinary Club Keno: **62.4391%** (3-Spot);
- Bulls-Eye: **60.6500%** (3-Spot);
- Double Bulls-Eye nominal: **65.3369%** (9-Spot).

The official $1m-per-ticket / $5m same-Spot liability language can only reduce the Double Bulls-Eye strict floor, so the nominal 65.3369% is already sufficient to reject the current fixed-paytable class.

Multiplier is even weaker for a strict guarantee: it doubles cost while the legal wheel includes a 1x state, so the best worst-case full-cover ratio is at most **31.2196%**.

Status: **CURRENT MISSOURI MARKED-BALL/MULTIPLIER FIXED-PAYTABLE GUARANTEE CLASS REJECTED / REUSABLE EXACT THEOREM VALIDATED / NO SUCCESS**.

Files:
- `research/h150_missouri_club_keno_marked_ball_cover.md`
- `src/loto_research/keno_marked_ball_cover.py`
- `data/derived/h150_missouri_bullseye_full_cover.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H150_APPEND.md`

## Preserved lottery conclusions
- Cash WinFall historical rolldown: genuine historical +EV control, not current guarantee.
- H108 Lotto Texas 2023 near-full acquisition: operationally real; current Texas route legally closed and duplicate jackpot sharing defeats strict guarantee.
- H109-H112 fixed raffle/scratch/sealed-pack standard takeover class materially closed.
- H113-H116 Azerbaijan 4+4 ordinary/realistic carryover guarantee routes materially closed; reopen only on rare high-order zero-category states, major primary-rule improvement, extreme observable sales collapse, or explicit operator-funded addition.
- H114 TezLoto published-state full coverage negative; empirical RNG/bias route remains only with reliable bulk history and >27.78% out-of-sample probability lift.
- H117-H121 ordinary fixed-board/promo full-takeover screens materially closed.
- H122/H128 Florida fixed-board undersubscription: strong +EV class validated, but no strict guarantee because external tickets can occupy all winning slots.
- H124 lottery loyalty rebate deterministic but insufficient for guaranteed coverage.
- H129 deterministic all-unsold takeover theorem validated; sampled NC board fails strict floor.
- H130 replenishing Fast Play grids are not depleting inventories; buy-the-pot rejected.
- H131 statewide Nth-ticket coupon ownership rejected because unrelated purchases can take coupon positions.
- H132 purchase-local deterministic free-ticket subsidy ownership solved structurally, but Mega Millions fails because of unbounded jackpot sharing.
- H133 capped wallet bonuses confirmed but tested compact games remain below strict break-even.
- H134 random free tickets / second-chance entries cannot be counted at face value toward a guaranteed floor.
- H135 scalable BOGO + non-shareable compact coverage: best tested Washington Match 4 reaches 91.4361% strict return.
- H136-H140 Kentucky deposit-promo + Pick 3: positive conditional arithmetic exists, but promo entitlement and wager acceptance are not locked before nonwithdrawable funding.
- H141 North Carolina checkout architecture validates whole-cart immediate discount mechanics, but no current offer crosses break-even.
- H142 validates Virginia Keno 1-Spot at **75% fixed deterministic cover**, still the best current standard fixed-paytable Keno benchmark in this branch.
- H143 confirms Virginia as best screened standard state-Keno target; no >25% pre-locked subsidy found.
- H144 validates Nebraska municipal Keno periodic special paytables + free-play coupons as a dynamic search class.
- H145 validates withdrawable Play+ funding + pre-start void execution architecture and the coupon-adjusted Pick-1 trigger `>3.00x` with a $5 credit on a $20 cover.
- H146 recovers an actual 2026 Kearney Pick-1 special at exactly 3.00x: 75% face return and exact break-even under the hypothetical $5 coupon; also proves scheduled promo dates are not enough because specials may be withdrawn early.
- H147 validates sequential cover with pre-close rollback as a real risk-control mechanism, but bulk/atomic rollback for an 80-number cover remains unproven.
- H148 recovers the Omaha August `$2` 3-Spot special and closes it at only **70.7644%** deterministic full-cover return.
- H149 generalizes the Keno screen to every fixed exact-hit paytable and precomputes Hit-k break-even multipliers.
- **H150 generalizes deterministic coverage again to one/two specially marked winning balls; current Missouri Bulls-Eye/Double Bulls-Eye/Multiplier paytables all remain below 75%, so they are closed as current strict-guarantee candidates.**

## Azerbaijan live branches
- `4+4`: only rare exceptional carryover states / materially better primary rules.
- `TezLoto`: only bulk-history RNG/bias testing on reliable recovered data.
- `Poz-Qazan`: remaining-prize conditional edge remains data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Resume recovery of current August 2026 numeric Nebraska specials from Big Red community pages/images (Lincoln, Fremont, Norfolk, Kearney, La Vista and smaller communities) and run each complete paytable through H149 immediately.** Do not infer a current paytable from stale cached promo images.
2. Escalate only paytables with `R_k>1`, or `0.75<R_k<=1` when a genuinely pre-owned deterministic coupon/discount exceeds `1-R_k`.
3. Prioritize active Pick-1 `p>4.00x`; for multi-tier specials use the full H149 formula rather than headline Hit-k payout alone.
4. Search outside Nebraska for compact fixed non-shareable Keno/paytable variants with deterministic cover **>75%**, now including marked-ball/bonus-ball structures via H150.
5. Search for single-ticket/way-ticket or documented batch/void mechanisms that can make complete cover acceptance or rollback strict once a threshold-crossing paytable exists.
6. Continue fixed-board raffle monitor with H129 worst-case floor and H122/H128 +EV denominator math.
7. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
8. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
9. Azerbaijan 4+4 only on materially new primary rules or rare high-order carryover state.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe append packets are authoritative additions where direct replacement of the large master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H150_APPEND.md`.
Latest case: `research/h150_missouri_club_keno_marked_ball_cover.md`.
