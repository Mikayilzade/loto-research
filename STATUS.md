# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H197 — Rhode Island first-deposit-match Keno bound**.

### H197 major result
The currently advertised Rhode Island Lottery **50% First-Time Deposit Match** is a genuine current lottery-specific subsidy and official rules explicitly allow its iLottery Bonus Money to be played on **online Keno or eInstants**.

Official rules: promotion began 2025-03-10 and continues until an announced end date; eligible first-ever Plus-member deposit gets 50% Bonus Money capped at **$50**. Current iLottery Terms (updated 2026-07-14) say player deposits generally cannot be withdrawn, Bonus Money cannot be cashed out, and promotional offers are discretionary/cancellable.

Against the H173 ordinary 3-spot basket:
- face cost: **$4,560**;
- H173 worst-case gross with a true 2x doubler: ~**$5,000 = 109.6491%**;
- without that doubler: ~**$2,500 = 54.82455%**;
- maximum first-deposit bonus: **$50**;
- minimum cash required to fund the $4,560 basket after max bonus: **$4,510**;
- ordinary worst-case cash result: approximately **-$2,010**.

Thus the live first-deposit match cannot substitute for the missing deterministic pre-draw 2x Keno overlay. It offsets only ~1.0965% of H173 face cost while ordinary H173 needs ~45.1755% external subsidy to break even.

Files:
- `research/h197_ri_first_deposit_match_keno_bound.md`
- `data/derived/h197_ri_first_deposit_match_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H197_APPEND.md`

### Preserved H196 result
Fresh official Rhode Island Lottery pages still show **`Kick Back with Keno Promotion`**, but exact public rules remain unrecovered. A simple deterministic `buy 2, get 1 free` Keno subsidy, even if granted as an optimistic hypothetical, raises H173 ordinary floor only to **82.236825%** and is insufficient without another nonlinear benefit such as a pre-draw prize multiplier.

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
- H197 closes current RI first-deposit match as a standalone replacement for the missing 2x overlay; reopen only if cap/terms materially improve or a much smaller deterministic conversion cover is found.

## NEXT ACTION
1. **Highest live priority remains recovery of exact official rules/landing payload for active `Kick Back with Keno Promotion`.** Determine dates, deterministic/random award, eligible wager/spot types, retailer vs iLottery, caps, cash/bonus nature, cancellation/disqualification and whether entitlement is known/vested before draw.
2. Specifically test whether the live promo includes a **pre-draw multiplier** or combines free tickets with multiplier value; H196 closes simple buy-2/get-1 alone and H197 closes the current $50 first-deposit match as substitutes for H173's doubler.
3. Search authoritative retailer-terminal / registered-ticketless documentation for exact Keno plays-per-ticket/transaction and whether multiple independently specified selections may share one same-draw object.
4. Recover authoritative cutoff/throughput/rate-limit evidence. H195 establishes a conservative public-flow requirement of 18.07 independent H175 submissions/sec over 240 seconds; do not call execution impossible without a hard cap/prohibition.
5. Resume H191/H188 exact pruning in parallel using existing balanced cuts; solver-certified infeasibility closes restricted diagonal family, timeout never does.
6. If diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` and reuse accumulated witnesses.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H197_APPEND.md`.
Latest case: `research/h197_ri_first_deposit_match_keno_bound.md`.
