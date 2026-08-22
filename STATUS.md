# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H196 — Rhode Island Keno active-promo upper bound**.

### H196 major result
Fresh official Rhode Island Lottery pages still show **`Kick Back with Keno Promotion`**, but exact public rules remain unrecovered.

A separate current homepage rendering exposes **`Get a free ticket when you buy 2`**, but the current page structure does not establish that this phrase belongs to Keno; the exposed click resolves to Mega Millions. Therefore it is not treated as a verified Keno term.

H196 nevertheless tested the strongest optimistic interpretation as a pure subsidy upper bound. H173's validated doubled 3-spot cover has 109.6491% worst-case gross **with** a true 2x doubler. Without the doubler its ordinary floor is **54.82455%**. Even if Keno had an idealized deterministic `buy 2, get 1 free` offer with fully equivalent free tickets, effective cost would be 2/3 of face and the strict floor would rise only to **82.236825%**.

Therefore a simple buy-2/get-1 Keno subsidy is **insufficient by itself** to make H173 guaranteed-profitable. The live promotion remains relevant only if its exact rules contain a stronger nonlinear feature such as a pre-draw prize multiplier or another deterministic overlay.

Historical control remains the official 2025 Lucky 3 Spot Keno promotion, where qualifying 3-spot tickets carried a printed pre-draw doubler message, winning prizes were doubled, and eligible tickets could not be cancelled.

Files:
- `research/h196_ri_keno_buy2_get1_upper_bound.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H196_APPEND.md`

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

## NEXT ACTION
1. **Highest live priority remains recovery of exact official rules/landing payload for active `Kick Back with Keno Promotion`.** Determine dates, deterministic/random award, eligible wager/spot types, retailer vs iLottery, caps, cash/bonus nature, cancellation/disqualification and whether entitlement is known/vested before draw.
2. Specifically test whether the live promo includes a **pre-draw multiplier** or combines free tickets with multiplier value; H196 closes simple buy-2/get-1 alone as insufficient for H173.
3. Search authoritative retailer-terminal / registered-ticketless documentation for exact Keno plays-per-ticket/transaction and whether multiple independently specified selections may share one same-draw object.
4. Recover authoritative cutoff/throughput/rate-limit evidence. H195 establishes a conservative public-flow requirement of 18.07 independent H175 submissions/sec over 240 seconds; do not call execution impossible without a hard cap/prohibition.
5. Resume H191/H188 exact pruning in parallel using existing balanced cuts; solver-certified infeasibility closes restricted diagonal family, timeout never does.
6. If diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` and reuse accumulated witnesses.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H196_APPEND.md`.
Latest case: `research/h196_ri_keno_buy2_get1_upper_bound.md`.
