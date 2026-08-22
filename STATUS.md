# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H174 — Rhode Island doubled-Keno clique-partition exhaustion + Keno Plus timing gate**.

### H174 major result
H173's conditional free-2x 3-spot Keno construction was tested against the complete obvious family of disjoint clique partitions.

For a partition of 80 numbers into group sizes `g_i`, buying every 3-subset inside each group gives cost `sum C(g_i,3)`. For any 20-number draw with group hit counts `s_i`, exact doubled payout is `sum[50*C(s_i,3)+5*C(s_i,2)*(g_i-s_i)]`. Dynamic programming therefore gives the exact worst case without enumerating `C(80,20)` draws.

All nondecreasing integer partitions of 80 into **1 through 8 groups** were screened: **411,498 constructions** total.

Best/cheapest strict-positive results by group count:
- 1 group: `(80)` -> 82,160 cost / 114,000 worst gross = 138.7537%;
- 2 groups: `(40,40)` -> 19,760 / 25,500 = 129.0486%;
- 3 groups: `(26,27,27)` -> 8,450 / 10,170 = 120.3550%;
- 4 groups: **`(20,20,20,20)` -> 4,560 / 5,000 = 109.6491%**;
- 5 groups: no strict positive; `(16,16,16,16,16)` is exactly 100%;
- 6-8 groups: no strict positive.

Therefore **H173's 4,560-play construction is proven cheapest within the entire tested 1–8-group clique-partition family**. A smaller guaranteed portfolio must use genuinely different selective cross-group/cyclic/block-design structure rather than merely changing partition sizes.

H174 also tested the tempting current Keno Plus timing branch. The 2026 rules say Plus costs an equal additional wager and its wheel is drawn just before the applicable Keno draw. Current Rhode Island FAQ states iLottery wagering is unavailable during each game's draw-break period, and no official same-draw post-wheel purchase path was found. Thus the multiplier must still be treated as unknown when committing the wager; the 2x/3x/4x/5x/10x wheel cannot currently be used as a pre-purchase guaranteed state.

The live August 2026 homepage still shows **`Kick Back with Keno Promotion`**, but its primary current rules and the primary current 3-spot paytable remain unrecovered.

Status: **H173 OPTIMAL WITHIN CLIQUE-PARTITION FAMILY / KENO PLUS POST-WHEEL EXPLOIT REJECTED ABSENT NEW OFFICIAL EVIDENCE / CURRENT FREE-2X TERMS + EXECUTION STILL UNPROVEN**.

Files:
- `research/h174_ri_keno_partition_exhaustion_and_plus_timing.md`
- `src/loto_research/h174_ri_keno_partition_search.py`
- `data/derived/h174_ri_keno_partition_summary.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H174_APPEND.md`

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not current guarantee.
- H108 Lotto Texas 2023: near-full acquisition operationally real; current Texas route legally closed and jackpot sharing blocks strict guarantee.
- H109-H112 fixed raffle/scratch/sealed-pack standard takeover materially closed.
- H113-H116 Azerbaijan `4+4` ordinary/realistic carryover guarantee routes materially closed; reopen only on rare high-order zero-category states, major rule change, extreme observable sales collapse, or explicit external subsidy.
- H114 TezLoto published-state full coverage negative; empirical RNG/bias route remains only with reliable bulk history and >27.78% out-of-sample probability lift.
- H122/H128 Florida fixed-board undersubscription: strong +EV class, no strict guarantee because external tickets can occupy winning slots.
- H129/H159 residual raffle takeovers have exact worst-case forced-slot theorem; sampled boards fail strict floor.
- H130 replenishing Fast Play grids are not depleting inventories.
- H131 statewide Nth-ticket coupons fail ownership because unrelated purchases can take target positions.
- H132 deterministic purchase-local free-ticket ownership is structurally valid, but Mega Millions jackpot sharing blocks strict guarantee.
- H133-H141 wallet/deposit/cart subsidy architectures screened; Kentucky crossed pre-tax break-even mathematically but failed pre-commitment acceptance/entitlement gates.
- H142 Virginia Keno 1-Spot deterministic cover = **75%**; no >25% pre-locked subsidy found.
- H144-H149 Nebraska dynamic-special screening/void architecture developed.
- H150-H153 broader Keno screens: La Vista benchmark **81.0636%**, ordinary state tables remain below strict break-even.
- H154 KenoGO Minor/Major can exceed 100% after state resolution, but profitable state is unknown until betting closes.
- H155-H156 universal free multiplier would work for some Keno tables, but current promos assign multiplier randomly or charge offsetting surcharge.
- H157 BCLC deterministic `X paid + Y free` architecture is structurally correct; current offer not strong enough.
- H158 Emirates Draw deterministic cart discount validated but EASY6/SURE economics fail strict floor.
- H159 fixed-board residual takeover theorem preserved.
- H160 Michigan cumulative-trigger promotion: forced-red Daily 3 reaches exactly **100% gross**, making compatible pre-locked subsidy sufficient.
- H161-H163 New Jersey Green Ball: forced-state Pair cover reaches 100%; retailer commissions create conditional 105%-106.25%, but atomicity remains unresolved.
- H164-H169 North Carolina forced Pick 3 Double Draw reaches 100% gross and retailer-discount economics can be positive, but current public rules allow liability-limit refusal and lack whole-basket atomic rollback; strict guarantee rejected.
- H170 Barbados Pick 3 Mega Ball Pair cover reaches **106% in successful-MB state**, but MB success is random; strict floor 26.5%.
- H171 Jamaica Cash Pot + Mega reaches **136.11% in Gold state**, but modifier state is random after purchase; strict floor 38.89%.
- H172 Rhode Island proves that lottery-issued 2x entitlement can be printed/locked before the draw; naive doubled 3-spot full space = **138.7537% conditional**, but 82,160 plays are operationally too large and current 2026 promo terms remain unresolved.
- H173 reduces that conditional strict doubled cover to **4,560 plays / 109.6491% worst-case pre-tax** using four 20-number triple cliques.
- **H174 exhaustively screens 411,498 clique partitions with 1–8 groups and proves 4×20 is the cheapest strict-positive member; smaller cover now requires non-clique block design. Keno Plus cannot currently be treated as a known pre-purchase multiplier state.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: recover official 2026 Rhode Island `Kick Back with Keno` rules and current primary RI 3-spot paytable.** If it is a free deterministic pre-locked 2x, H173/H174 provide a strict 109.65% pre-tax construction and a closed simple-partition search.
2. Search **non-clique structured block/cyclic designs below 4,560 plays** satisfying `50*n3(S)+5*n2(S) > |F|` for every 20-number draw. Use symmetry, covering-design bounds, integer programming / adversarial separation, not brute force over all draws.
3. Recover Rhode Island terminal/ticket mechanics: maximum number of distinct 3-spot selections per ticket/transaction, whether a specific future Keno draw can be targeted, and actual throughput sufficient to place a reduced portfolio into one draw.
4. Search current pre-printed/pre-locked free doublers in lotteries with smaller state spaces than 80-number Keno.
5. Continue scheduled Keno special/paytable search for deterministic >100% coverage states known before purchase; La Vista **81.0636%** remains current ordinary benchmark.
6. Continue BCLC deterministic `X paid + Y free` Keno monitor; reopen on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
7. Continue Nebraska/community fixed scheduled-special recovery where enhanced paytable is known before purchase.
8. Continue H159 live/announced fixed-board raffle monitor, prioritizing flat boards near/exceeding 100% worst-case residual floor.
9. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H174_APPEND.md`.
Latest case: `research/h174_ri_keno_partition_exhaustion_and_plus_timing.md`.
