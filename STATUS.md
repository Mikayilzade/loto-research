# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H195 — Rhode Island Keno bulk-cart interface differential**.

### H195 major result
H195 compared fresh 2026-08-23 official Rhode Island Lottery purchase interfaces rather than inferring packaging from the $150 Keno ticket cap.

Current iKeno exposes one four-step flow (`Pick your numbers` -> `Amount per game` -> `Consecutive games` -> options) followed by **`Buy Now`**. It does **not** visibly expose `QTY` or `Add to cart` for Keno.

A same-platform Mega Millions control explicitly exposes both **`QTY`** and **`Add to cart`**. Thus cart/quantity functionality is renderable by the platform but absent from the public Keno flow; this is meaningful product-specific evidence against assuming arbitrary bulk same-draw Keno packing.

Under the currently observable public flow, H175 still requires **4,336 separately specified selections** and H173 **4,560**. Even granting the full four-minute draw interval as the purchase window gives conservative lower-bound completion rates:
- H175: **18.0667 submissions/sec**;
- H173: **19.0000 submissions/sec**.

This materially strengthens the execution blocker but is **not a formal impossibility proof**: hidden retailer batching, undocumented batch/API tooling or privileged syndicate interfaces have not been authoritatively excluded.

Fresh official homepage retrieval still displays **`Kick Back with Keno Promotion`**. A separate homepage phrase `Get a free ticket when you buy 2` cannot safely be attributed to Keno because the carousel/link mapping is dynamic and a recovered click resolved elsewhere. No subsidy is assumed without exact promotion terms.

Files:
- `research/h195_ri_keno_bulk_cart_interface_differential.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H195_APPEND.md`

### Preserved H194 result
H194 corrected H193: the ordinary $150 Keno Ticket / Registered Ticketless maximum is naturally explained by up to 15 consecutive draws at $10 and does not prove 150 independently specified same-draw selections per object.

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
2. Search authoritative retailer-terminal / registered-ticketless documentation for exact Keno plays-per-ticket/transaction and whether multiple independently specified selections may share one same-draw object.
3. Recover authoritative cutoff/throughput/rate-limit evidence. H195 establishes a conservative public-flow requirement of 18.07 independent H175 submissions/sec over 240 seconds; do not call execution impossible without a hard cap/prohibition.
4. If promotion supplies deterministic pre-draw free tickets, multiplier or sufficient purchase-local subsidy, plug immediately into H173/H175 worst-case economics.
5. Resume H191/H188 exact pruning in parallel using existing balanced cuts; solver-certified infeasibility closes restricted diagonal family, timeout never does.
6. If diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` and reuse accumulated witnesses.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H195_APPEND.md`.
Latest case: `research/h195_ri_keno_bulk_cart_interface_differential.md`.
