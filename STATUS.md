# STATUS

Updated: 2026-08-21
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H158 — Emirates Draw deterministic cart promos + SURE residual takeover**.

### H158 major result
A fresh 2026 scan found a genuinely deterministic player-owned cart subsidy in Emirates Draw: the current Onam EASY6 promotion (published August 16, valid through August 30, 2026) automatically discounts five EASY6 entries from USD 30 to USD 21, i.e. **30% off**, repeatable during the promotion. Recent August EASY6 offers also reached buy-6-get-3-free (**33.3333% effective subsidy**).

Exact EASY6 full-cover math, however, decisively rejects the route:
- space `C(39,6)=3,262,623`;
- face cost **$19,575,738**;
- even granting our cover the entire advertised shared Match-6/5/4 pools plus every fixed Match-3 payout, favorable gross is only **$4,138,120**;
- current 30%-discount cover cost **$13,703,016.60**, favorable ratio **30.198606%**;
- hypothetical/scalable buy-6-get-3 cost **$13,050,492**, favorable ratio **31.708536%**.

The same packet tested a more deceptive live state in Emirates SURE raffles. On the August 21 snapshot, the cost of **all currently remaining tickets** was below the advertised prize board in SURE1, SURE2 and SURE3. This is not a guarantee because already-sold external tickets remain eligible and can occupy every winner slot:
- SURE1: 2,377 external tickets vs 1 winner;
- SURE2: 2,334 external tickets vs 1 winner;
- SURE3: 12,143 external tickets vs 5 winners.
Therefore buying every remaining ticket still has a legal **$0 strict prize floor**.

H158 reinforces a reusable residual-raffle theorem: for total tickets `T`, remaining `R`, and `W` winning slots, if `T-R >= W`, then absent another structural constraint, all `W` winners can be external and a residual buyer has zero strict prize floor. Apply this before any `remaining cost < headline prize pool` arithmetic.

Status: **NO SUCCESS / CURRENT DETERMINISTIC EMIRATES PROMOS SCREENED NEGATIVE; CURRENT SURE RESIDUAL BUYOUTS REJECTED BY EXTERNAL-WINNER FLOOR**.

Files:
- `research/h158_emirates_draw_deterministic_promos_and_sure_residual_takeover.md`
- `data/derived/h158_emirates_promo_screen.csv`
- `src/loto_research/h158_emirates_promo_screen.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H158_APPEND.md`

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
- H142 validates Virginia Keno 1-Spot at **75% fixed deterministic cover**; H143 found no >25% pre-locked Virginia subsidy.
- H144-H149 establish Nebraska dynamic-special screening, withdrawable Play+ funding, pre-start void architecture and exact fixed-paytable cover theorem.
- H150-H153 screen additional Keno structures; La Vista remains a strong ordinary/special benchmark at **81.0636%** while major ordinary state tables stay below it.
- H154 finds KenoGO Jackpot Minor/Major 1-Spot full-cover states at 125%/312.5%, but the state resolves after sales cutoff; unconditional floor 37.5%.
- H155 proves a universal pre-announced no-cost 2x on current PA 4-SPOT would yield 129.743674% deterministic gross, but current PA/MD promotions assign boosts probabilistically/Nth-ticket, CT resolves its multiplier too late, and Oregon fixed Special Keno remains below break-even.
- H156 proves that paid multiplier add-ons must be judged net of surcharge: Ohio's universal Double BOOSTER solves ownership but leaves the guaranteed cover ratio unchanged; BCLC/Michigan free Doublers remain randomly assigned.
- H157 proves BCLC Value Bundles are the right deterministic ownership architecture. A future buy-3-get-2-free (or stronger) bundle would cross the current Pick-2/Pick-3 exact coverage threshold, while current 2026 BCLC promotion is random Doubler and does not qualify.
- **H158 validates a current deterministic cart-discount architecture at Emirates Draw, but EASY6 remains far below break-even even with 30–33.33% subsidy. It also closes the current SURE residual-buyout illusion: `remaining cost < prize board` is insufficient when already-sold external tickets can occupy all winner slots.**

## Azerbaijan live branches
- `4+4`: only rare exceptional carryover states / materially better primary rules.
- `TezLoto`: only bulk-history RNG/bias testing on reliable recovered data.
- `Poz-Qazan`: remaining-prize conditional edge remains data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: search fixed-board raffles with many guaranteed winner slots and live remaining inventory where `external sold < W`.** Only these can force at least one residual-buyer prize; compute the exact worst-case allocation of the cheapest winning slots before purchase cost.
2. Continue current/announced Keno Value Bundle / deterministic free-draw monitor. For BCLC reopen immediately on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
3. Search other state/provincial Keno products for deterministic `X paid + Y free` bundles and universal no-cost multipliers, prioritizing base cover ratios >67–75% and liability-safe ticket volumes.
4. Continue Nebraska/community scheduled-special recovery where the enhanced paytable is fixed before purchase.
5. For any qualifying candidate, immediately test complete-basket transaction limits, liability/proration caps, cancellation/rollback, taxes, geographic eligibility and timing.
6. Continue fixed-board raffle monitor using H129/H158 worst-case winner-slot allocation before EV arithmetic; do not treat headline residual prize pool as guaranteed.
7. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
8. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
9. Azerbaijan 4+4 only on materially new primary rules or rare high-order carryover state.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe append packets are authoritative additions where direct replacement of the large master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H158_APPEND.md`.
Latest case: `research/h158_emirates_draw_deterministic_promos_and_sure_residual_takeover.md`.
