# STATUS

Updated: 2026-08-21
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H149 — general Nebraska Keno full-paytable deterministic theorem + break-even atlas**.

### H149 major result
H148's Hit-k-only formula is now generalized to an arbitrary fixed k-Spot paytable.

If every k-subset of 80 numbers is purchased and 20 numbers are drawn, then for every legal draw the number of our tickets with exactly j hits is fixed:

`N(k,j)=C(20,j)C(60,k-j)`.

Therefore for stake `s` and exact-hit payouts `P_j`:
- tickets = `C(80,k)`;
- cost `S=s C(80,k)`;
- deterministic gross `G=sum_j P_j C(20,j)C(60,k-j)`;
- exact all-outcome return `R_k=G/S`.

This is not an EV approximation: complete k-subset ownership removes draw randomness from the gross payout whenever the paytable is fixed/non-shareable.

Hit-k-only standalone break-even payout multiples are now precomputed for k=1..10:
- k=1: **4.000000x**
- k=2: **16.631579x**
- k=3: **72.070175x**
- k=4: **326.435501x**
- k=5: **1,550.568627x**
- k=6: **7,752.843137x**
- k=7: **40,979.313725x**
- k=8: **230,114.607843x**
- k=9: **1,380,687.647059x**
- k=10: **8,911,711.176471x**

A deterministic pre-owned credit/discount fraction `d` inverts a fixed-paytable cover exactly when `R_k + d > 1`, assuming the credit reduces external cash dollar-for-dollar and does not alter payout eligibility.

The generalized calculator reproduces H148 Omaha August 2026 exactly: 82,160 `$2` 3-Spot tickets, `$116,280` deterministic gross, **70.764484%** return.

Status: **GENERAL EXACT KENO SCREEN VALIDATED / NO SUCCESS**.

Files:
- `research/h149_nebraska_keno_general_full_paytable_theorem.md`
- `src/loto_research/keno_full_cover.py`
- `data/derived/h149_keno_hitk_break_even_thresholds.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H149_APPEND.md`

Fresh public-web search for additional August community specials returned transient service errors during this run; no unsupported live paytable was inferred. Resume live special recovery next run.

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
- H142 validates Virginia Keno 1-Spot at 75% fixed deterministic cover.
- H143 confirms Virginia as best screened standard state-Keno target; no >25% pre-locked subsidy found.
- H144 validates Nebraska municipal Keno periodic special paytables + free-play coupons as a dynamic search class.
- H145 validates withdrawable Play+ funding + pre-start void execution architecture and the coupon-adjusted Pick-1 trigger `>3.00x` with a $5 credit on a $20 cover.
- H146 recovers an actual 2026 Kearney Pick-1 special at exactly 3.00x: 75% face return and exact break-even under the hypothetical $5 coupon; also proves scheduled promo dates are not enough because specials may be withdrawn early.
- H147 validates sequential cover with pre-close rollback as a real risk-control mechanism, but bulk/atomic rollback for an 80-number cover remains unproven.
- H148 recovers the current Omaha August `$2` 3-Spot special and closes it at only 70.7644% deterministic full-cover return.
- **H149 generalizes the Keno screen to every fixed exact-hit paytable and precomputes all Hit-k-only break-even multipliers; any newly recovered community special can now be classified exactly without simulation.**

## Azerbaijan live branches
- `4+4`: only rare exceptional carryover states / materially better primary rules.
- `TezLoto`: only bulk-history RNG/bias testing on reliable recovered data.
- `Poz-Qazan`: remaining-prize conditional edge remains data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: resume recovery of current August 2026 numeric Nebraska specials from Big Red community images/pages (Lincoln, Fremont, Norfolk, Kearney, La Vista and smaller communities) and run each complete paytable through H149 immediately.**
2. Escalate only paytables with `R_k>1`, or `0.75<R_k<=1` when a genuinely pre-owned deterministic coupon/discount exceeds `1-R_k`.
3. Prioritize active Pick-1 `p>4.00x`; for multi-tier specials use the full H149 formula rather than headline Hit-k payout alone.
4. Search for a single-ticket/way-ticket or documented batch construction/void mechanism that can make complete cover acceptance or rollback strict once a threshold-crossing paytable exists.
5. Continue scan outside Nebraska for compact non-shareable games with deterministic coverage ratio >75% or checkout-level subsidies above exact deficit.
6. Continue fixed-board raffle monitor with H129 worst-case floor and H122/H128 +EV denominator math.
7. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
8. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
9. Azerbaijan 4+4 only on materially new primary rules or rare high-order carryover state.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe append packets are authoritative additions where direct replacement of the large master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H149_APPEND.md`.
Latest case: `research/h149_nebraska_keno_general_full_paytable_theorem.md`.
