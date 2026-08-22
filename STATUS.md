# STATUS

Updated: 2026-08-22
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H173 — Rhode Island doubled 3-spot Keno reduced block cover**.

### H173 major result
H172's naive all-`C(80,3)=82,160` triple cover is not necessary under a free pre-locked 2x 3-spot architecture.

Partition the 80 Keno numbers into **four disjoint groups of 20** and buy every 3-number subset only within each group:
- plays = `4*C(20,3) = 4,560`;
- under the H172 screened 3-spot paytable ($25 for 3/3, $2.50 for 2/3), a free guaranteed 2x pays $50 and $5 respectively;
- if the actual 20-number draw hits the four groups in counts `s1+...+s4=20`, portfolio gross is `sum[50*C(si,3)+5*C(si,2)*(20-si)]`;
- the exact minimum occurs at the balanced draw composition **5+5+5+5**;
- minimum gross = **$5,000** on **$4,560** stake;
- strict conditional pre-tax floor = **109.6491%**, surplus **+$440**.

This cuts wager count from **82,160 to 4,560 (94.45% reduction)**. At the official $150 ordinary-ticket monetary cap, the theoretical lower bound falls from 548 to 31 ticket-equivalents, though this does **not** prove that 150 distinct selections fit on one ticket/action.

Control: five groups of 16 numbers using all internal triples gives exactly **100%** doubled worst-case return (2,800 -> 2,800), establishing a clean break-even boundary for this simple partition family.

### Why this is NOT SUCCESS
1. The live 2026 Rhode Island homepage advertises **`Kick Back with Keno Promotion`**, but official current rules were still not recovered; H173 cannot assume it is the historical Lucky 3 Spot free 2x mechanic.
2. The `$25/$2.50` 3-spot table remains secondary-source screened; the current primary RI dynamic paytable was not recovered.
3. All 4,560 distinct selections must target the same draw. Keno draws every four minutes, historical Lucky 3 Spot rules prohibit advance pre-printing, and public rules do not establish an atomic/bulk interface or the number of distinct selections packable per terminal action.
4. Historical promotion rules reserve modification/suspension/cancellation discretion and validation rights.
5. The +$440 pre-tax margin still needs a positive after-tax/cost floor under an executable taxpayer/entity structure.

Status: **REDUCED STRICT PRE-TAX COVER VALIDATED CONDITIONALLY ON PRE-LOCKED FREE 2X / CURRENT TERMS + PAYTABLE + SAME-DRAW EXECUTION NOT PROVEN**.

Files:
- `research/h173_ri_keno_reduced_block_cover.md`
- `src/loto_research/h173_ri_keno_reduced_cover.py`
- `data/derived/h173_ri_keno_reduced_cover.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H173_APPEND.md`

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
- **H173 reduces that conditional strict doubled cover to 4,560 plays with a 109.6491% worst-case pre-tax floor by using four 20-number triple cliques; current promo/paytable/same-draw execution remain the terminal blockers.**

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: recover official 2026 Rhode Island `Kick Back with Keno` rules and current primary RI 3-spot paytable.** If it is a free deterministic pre-locked 2x, H173 supplies a strict 109.65% pre-tax reduced cover.
2. Recover Rhode Island terminal/ticket mechanics: maximum number of distinct 3-spot selections per physical ticket/transaction, whether a specific future Keno draw can be targeted, and throughput sufficient to place one H173 portfolio into one draw.
3. Search **smaller structured block/cyclic designs than 4,560 plays** satisfying `50*n3(S)+5*n2(S) > |F|` for every 20-number draw; use analytic bounds / optimization rather than brute force over all draws.
4. Search current pre-printed/pre-locked free doublers in lotteries with smaller state spaces than 80-number Keno.
5. Continue scheduled Keno special/paytable search for deterministic >100% coverage states known before purchase; La Vista **81.0636%** remains current ordinary benchmark.
6. Continue BCLC deterministic `X paid + Y free` Keno monitor; reopen on `Y/X > 0.6631579` for Pick 2 or `>0.6015595` for Pick 3.
7. Continue Nebraska/community fixed scheduled-special recovery where enhanced paytable is known before purchase.
8. Continue H159 live/announced fixed-board raffle monitor, prioritizing flat boards near/exceeding 100% worst-case residual floor.
9. H007 TezLoto/RNG only upon recovery of reliable bulk history/API.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy master file is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H173_APPEND.md`.
Latest case: `research/h173_ri_keno_reduced_block_cover.md`.
