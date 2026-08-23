# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H198 — RI doubler multi-game semantics / Kick Back recovery**.

### H198 major result
Fresh official Rhode Island Lottery pages still list **`Kick Back with Keno Promotion`** as a current promotion in August 2026, but its exact public rules/landing payload remain unrecovered from indexed/static routes.

H198 also resolves a tempting execution shortcut from historical Lucky 3 Spot doubler rules. Official 2024/2025 rules state that when a qualifying Lucky 3 Spot message appears on a ticket containing **multiple Keno games**, eligible wins for all games on that ticket may be doubled. This confirms that one printed pre-draw 2x entitlement can apply across multiple Keno games on a ticket.

However, RI's current Keno interface separately exposes `Consecutive games`, and the historical rules do **not** state that thousands of independently specified selections for one single draw can be packaged on one ticket. H173/H175 require all constituent selections to face the same 20-number draw. Therefore multi-game/consecutive-draw language does not solve the H175 same-draw throughput gate.

A separate homepage phrase `Get a free ticket when you buy 2` was tested and must not be attributed to Kick Back Keno: its public link resolves to Mega Millions.

Files:
- `research/h198_ri_doubler_multigame_semantics_and_kickback_recovery.md`
- `data/derived/h198_ri_doubler_multigame_semantics.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H198_APPEND.md`

### Preserved H197 result
The current Rhode Island Lottery **50% First-Time Deposit Match** is a genuine Keno-eligible subsidy but capped at **$50**. Against H173's $4,560 ordinary 3-spot basket, maximum bonus leaves about **-$2,010 guaranteed** without a true deterministic 2x overlay. It cannot substitute for the missing doubler.

### Preserved H196 result
Fresh official RI pages showed `Kick Back with Keno Promotion`, but exact public rules remained unrecovered. Even an optimistic deterministic `buy 2, get 1 free` Keno subsidy would raise H173 ordinary floor only to **82.236825%**, insufficient without another nonlinear benefit such as a pre-draw prize multiplier.

### Preserved H195 result
Current iKeno exposes a single selection/amount/consecutive-games/options -> `Buy Now` flow with no visible Keno `QTY` or `Add to cart`, unlike Mega Millions. H175 would require 4,336 independently specified selections, implying 18.0667 completed submissions/sec over a full 240-second interval under the public flow. This materially weakens execution but is not a hard impossibility proof.

### Preserved H175/H191 mathematical state
The unresolved H175 4,336-play doubled 3-spot hybrid still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

- H185: 297 stored exact witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit exact counterexamples across two rejected candidates; timeout/no-incumbent remained inconclusive.
- H188: globally safe normalized representative count **12,289,536**.
- H189 full-S3 quotient was withdrawn by H190 as globally unsafe.
- H191 exact stabilizer classification safely reduces to **12,277,776** representatives only (~0.096% saving), materially exhausting further coordinate-symmetry quotienting.
- No universal construction or restricted-family impossibility proof exists yet.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeovers materially closed; residual raffle takeover theorem exists but tested boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias route needs reliable bulk history.
- Several Keno/Pick conditional overlays can reach/exceed 100% only in favorable modifier states; random modifier assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- H173 conditional 4,560-play doubled RI 3-spot cover remains mathematically valid.
- H175 4,336-play hybrid remains open pending universal `n3>=3` construction/impossibility.
- Michigan current pre-draw multiplier architecture exists but random ticket tagging prevents strict ex-ante guarantee.
- Historical RI Lucky 3 Spot shows genuine pre-draw 2x printed entitlement; H198 confirms multi-game ticket applicability but not same-draw bulk-selection packaging.
- H197 closes current RI first-deposit match as a standalone replacement for the missing 2x overlay; reopen only if cap/terms materially improve or a much smaller deterministic conversion cover is found.

## NEXT ACTION
1. **Highest live priority remains recovery of exact official rules/landing payload for active `Kick Back with Keno Promotion`.** Determine dates, deterministic/random award, eligible wager/spot types, retailer vs iLottery, caps, cash/bonus nature, cancellation/disqualification and whether entitlement is known/vested before draw.
2. Search authoritative retailer-terminal / playslip / registered-ticketless documentation for exact **same-draw distinct selection capacity**. H198 closes the invalid shortcut from historical `multiple games on one ticket` wording.
3. Specifically test whether current Kick Back includes a **pre-draw multiplier** or combines a free-ticket/rebate with multiplier value; H196 closes simple buy-2/get-1 alone and H197 closes the $50 first-deposit match as substitutes for H173's doubler.
4. Recover authoritative cutoff/throughput/rate-limit evidence. H195 establishes a conservative public-flow requirement of 18.07 independent H175 submissions/sec over 240 seconds; do not call execution impossible without a hard cap/prohibition.
5. Resume H191/H188 exact pruning in parallel using existing balanced cuts; solver-certified infeasibility closes restricted diagonal family, timeout never does.
6. If diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` and reuse accumulated witnesses.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H198_APPEND.md`.
Latest case: `research/h198_ri_doubler_multigame_semantics_and_kickback_recovery.md`.
