# STATUS

Updated: 2026-08-21
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H159 — fixed-board raffle residual takeover forced-slot floor**.

### H159 major result
H158's residual-raffle zero-floor test has been strengthened into an exact worst-case theorem for the only interesting regime where the number of already-sold external tickets `e` is still below the number of guaranteed winning slots `W`.

For a fixed board with prizes sorted ascending `p1 <= ... <= pW`, if a buyer acquires **every remaining ticket** after `e` external sales:
- if `e >= W`, strict buyer prize floor is **0**;
- if `e < W`, the exact strict payout floor is the sum of the **`W-e` cheapest prizes**, because the external tickets may occupy the `e` most valuable winner slots;
- strict margin is `G(e) = sum(cheapest W-e prizes) - ticket_price*(T-e)`.

This closes misleading cases where `remaining ticket cost < headline prize board` but the buyer cannot force the valuable prizes.

Virginia's 2026 Commanders Golden Pass / Capitals Career In A Year design was screened exactly:
- `T=150,000`, ticket price `$20`, `W=3,506`;
- board = `3,000 x $100 + 500 x $500 + 5 x $10,000 + 1 x $950,000-value top prize`;
- full acquisition cost = **$3,000,000**;
- entire advertised board = **$1,550,000**;
- best strict state is already `e=0`: **-$1,450,000 / 51.6667%**;
- every `e>0` worsens the guarantee because each external ticket saves only $20 while it can remove a forced prize worth at least $100 (and the first can remove the $950k top prize).

Therefore this high-winner raffle design is **rejected for every possible sales state**, not just after sellout.

Michigan's official online-raffle architecture remains worth monitoring because it explicitly permits unlimited aggregate ticket purchases (250 per cart, repeated carts), but a fresh August 2026 public screen did not surface a current active board/live state with `G(e)>0`.

Status: **NO SUCCESS / H159 FORCED-SLOT THEOREM VALIDATED / VIRGINIA 2026 HIGH-WINNER RESIDUAL TAKEOVER CLOSED FOR ALL SALES STATES**.

Files:
- `research/h159_residual_raffle_forced_slot_floor.md`
- `src/loto_research/h159_residual_raffle_floor.py`
- `data/derived/h159_virginia_residual_raffle_floor.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H159_APPEND.md`

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
- H158 validates a current deterministic cart-discount architecture at Emirates Draw, but EASY6 remains far below break-even; current SURE residual buyouts have zero strict floor once external sold tickets can occupy all winner slots.
- **H159 generalizes residual raffle screening: when `e<W`, use the `W-e` cheapest forced prizes, not the whole board. Virginia's 2026 150k-ticket/3,506-winner design fails at every possible `e`.**

## Azerbaijan live branches
- `4+4`: only rare exceptional carryover states / materially better primary rules.
- `TezLoto`: only bulk-history RNG/bias testing on reliable recovered data.
- `Poz-Qazan`: remaining-prize conditional edge remains data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Apply H159 `G(e)` to any live/announced fixed-board raffle with many guaranteed winners and visible remaining inventory.** Prioritize boards with full-board payout ratio near/above 100% or an explicit external subsidy; reject immediately when the cheapest forced slots cannot cover remaining cost.
2. Monitor Michigan online raffles specifically: its no-aggregate-ticket-limit architecture is unusually compatible with an all-remaining takeover if a subsidized/high-payout board appears.
3. Continue BCLC/current Keno deterministic `X paid + Y free` monitor; reopen immediately on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
4. Continue Nebraska/community scheduled-special recovery where the enhanced paytable is fixed before purchase.
5. Search other state/provincial Keno products for deterministic bundles and universal no-cost multipliers, prioritizing base cover ratios >67–75%.
6. For any candidate, test complete-basket limits, liability/proration, cancellation/rollback, taxes, geographic eligibility and timing before terminal promotion.
7. Reopen progressive/rolldown buy-the-pot only where verified external subsidy is large relative to exact full-space deficit and sharing is bounded.
8. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
9. Azerbaijan 4+4 only on materially new primary rules or rare high-order carryover state.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H159_APPEND.md`.
Latest case: `research/h159_residual_raffle_forced_slot_floor.md`.
