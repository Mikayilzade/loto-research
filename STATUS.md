# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H208 — RI retail/SSVM strict-execution failure**.

### H208 major result
H208 moved the H173/H175 execution test from iLottery to physical Rhode Island retailer terminals / self-service vending machines (SSVMs).

Current RI rules cap an ordinary Keno Ticket at **$150** and Keno draws every **4 minutes**. Therefore, even under the most favorable possible packing assumption, complete acquisition requires at least:

- H175: `ceil(4,336 / 150) = 29` separately issued $1-ticket-equivalents;
- H173: `ceil(4,560 / 150) = 31` separately issued $1-ticket-equivalents.

RI Lottery's current Retailer FAQ expressly recognizes Lottery terminal jams/misprints. The prescribed handling is to reprint and contact the IGT hotline; Keno misprints should be voided prior to the draw, and credit for damaged/misprinted tickets may be given **at Lottery discretion**. No current rule recovered in H208 grants an atomic all-or-none physical transaction covering the full required portfolio or an irrevocable right to force successful reissuance of every failed component before the target draw.

Thus the allowed branch

`>=1 required physical issuance fails/misprints and is not successfully reissued before target draw`

cannot be excluded. Since H173/H175 require complete ownership of all prescribed same-draw wagers, their deterministic payoff theorem is lost in that branch.

**Consequence:** current ordinary retail-terminal/SSVM issuance is now **CLOSED as the sole strict-guarantee execution channel** for H173/H175. This does not reject practical/+EV execution, future operator-approved atomic bulk facilities, or the underlying H175 mathematics.

Files:
- `research/h208_ri_retail_ssvm_strict_execution_failure.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H208_APPEND.md`

### Preserved H207 result
Current RI online/iLottery is closed as a sole strict-guarantee execution channel because official Terms do not guarantee purchase timeliness and allow attempted purchases to be delayed/refused.

### Preserved H175/H191 mathematical state
The unresolved H175 4,336-play doubled 3-spot hybrid still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

- H185: 297 stored exact witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit exact counterexamples across two rejected candidates; timeout/no-incumbent remained inconclusive.
- H188: globally safe normalized representative count **12,289,536**.
- H189 full-S3 quotient was withdrawn by H190 as globally unsafe.
- H191 exact stabilizer classification safely reduces to **12,277,776** representatives only (~0.096% saving), materially exhausting further coordinate-symmetry quotienting.
- No universal construction or restricted-family impossibility proof exists yet.

### Preserved promotion state
- Historical RI Lucky 3 Spot proves a genuine pre-draw printed 2x entitlement can exist.
- Ordinary paid Keno Plus is not a substitute because its multiplier is random and costs an equal add-on wager.
- Current `Kick Back with Keno Promotion` is visibly live, but exact current mechanics remain unrecovered; the homepage `buy 2 -> free ticket` teaser was traced to Mega Millions, not Keno.
- Michigan current pre-draw multiplier architecture exists but random ticket tagging prevents a strict ex-ante guarantee.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeovers materially closed; residual raffle takeover theorem exists but tested boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias route needs reliable bulk history.
- Several Keno/Pick conditional overlays can reach/exceed 100% only in favorable modifier states; random modifier assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- H173 conditional 4,560-play doubled RI 3-spot cover remains mathematically valid.
- H175 4,336-play hybrid remains open pending universal `n3>=3` construction/impossibility.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Highest priority: recover exact current `Kick Back with Keno Promotion` rules through new primary-source assets, retailer notices, cached documents or linked campaign files.** Test whether it supplies a deterministic pre-draw subsidy, free wager or locked multiplier and whether its issuance terms avoid the H207/H208 execution failure branches.
2. Resume H191/H188 exact pruning with existing balanced cuts; solver-certified infeasibility closes restricted diagonal family, timeout never does.
3. If diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` and reuse accumulated witnesses.
4. Search other current lottery-issued deterministic pre-draw overlays that operate in smaller state spaces and do not require thousands of separately accepted wagers.
5. Reopen RI online or physical H173/H175 strict execution only upon materially new evidence: forced acceptance/atomic bulk acquisition, operator-backed syndicate facility, or rule changes curing refusal/failure branches.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H208_APPEND.md`.
Latest case: `research/h208_ri_retail_ssvm_strict_execution_failure.md`.
