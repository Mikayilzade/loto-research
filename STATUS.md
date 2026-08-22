# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H194 — Rhode Island Keno same-draw execution correction**.

### H194 major result
H194 re-checked H193's optimistic interpretation of Rhode Island Keno's `$150` ordinary Ticket / Registered Ticketless Play maximum.

Current 2026 official Keno rules say:
- one Keno selection contains 1–10 spots;
- wager per single draw is `$1/$2/$5/$10`;
- that wager can be played for up to **15 consecutive draws**;
- ordinary Keno Ticket / Registered Ticketless Play maximum is **$150**.

Thus the `$150` cap is naturally and exactly explained by `15 × $10`; it is **not evidence** that a single purchase object can contain 150 arbitrary distinct $1 same-draw selections.

The current iKeno UI independently exposes one flow: `Pick your numbers` -> `Amount per game` -> `Consecutive games` -> options -> `Buy Now`. No public multi-line/bulk builder for hundreds or thousands of independently specified same-draw selections was recovered.

Therefore H193's `29 H175 / 31 H173 max-value objects` figures are withdrawn as execution evidence. Under the currently visible online interface model, H175 still needs **4,336 independently specified selections** in one target draw and H173 needs **4,560**. Consecutive-draw replication does not help same-draw coverage.

This materially weakens online execution but is not a formal impossibility theorem because no authoritative statement has yet been recovered excluding hidden cart aggregation, retailer multi-play packaging, batch tooling or a bulk/API mechanism.

Fresh 2026-08-23 retrieval still shows **`Kick Back with Keno Promotion`** on the official homepage. Exact terms remain unrecovered from public retrievable promotion text / indexed 2026 promotion PDFs, so no subsidy or multiplier is assumed.

Files:
- `research/h194_ri_keno_single_selection_execution_correction.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H194_APPEND.md`

### Preserved H193 result
H193 correctly recovered the $150 ordinary Keno cap and four-minute draw cadence, but its `ceil(plays/150)` packaging counts were only hypothetical lower bounds and are superseded by H194's correction.

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
1. **Highest live priority: recover exact official rules/landing payload for active `Kick Back with Keno Promotion`.** Determine dates, deterministic/random award, eligible wager/spot types, retailer vs iLottery, caps, cash/bonus nature, cancellation/disqualification and whether entitlement is known/vested before draw.
2. Recover authoritative current Keno packaging mechanics: whether a retailer Ticket or Registered Ticketless transaction can contain multiple independently specified plays for the **same draw**, and the exact plays-per-ticket/cart/checkout limits.
3. Recover cutoff/throughput evidence. Without a multi-play object, H175/H173 require thousands of submissions inside one four-minute draw window.
4. If promotion supplies deterministic pre-draw multiplier or sufficient purchase-local subsidy, plug immediately into H173/H175 worst-case economics.
5. Resume H191/H188 exact pruning in parallel using existing balanced cuts; solver-certified infeasibility closes restricted diagonal family, timeout never does.
6. If diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` and reuse accumulated witnesses.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H194_APPEND.md`.
Latest case: `research/h194_ri_keno_single_selection_execution_correction.md`.
