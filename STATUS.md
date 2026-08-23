# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H210 — H175 residual translation quotient**.

### H210 major result
H210 returned to the unresolved H175 4,336-play doubled 3-spot hybrid after H209's current Rhode Island promotion search became data-blocked.

H188 had already normalized singleton supports B=(0,3,4), C=(1,3,4), D=(2,3,4) to zero shifts, with D fixed to `(a,c)=(1,0)`. H210 identifies an additional exact residual coordinate translation, for any `t mod16`:

`(group0,group1,group2,group3,group4) -> (-t,-t,-t,+t,0)`.

This preserves B,C,D zero shifts and coefficients. On each A=(0,1,2) layer it acts as

`(a,c) -> (a, c+(2a-1)t mod16)`.

Since every allowed `a` is odd, `2a-1` is invertible mod16. Every nonidentity action has only cycles of length `2,4,8,16`, so no nonidentity translation can fix a 3-element A subset. Therefore the 16-element action is **free** on all `C(128,3)=341,376` A sets.

Exact quotient:
- A orbits: `341,376 / 16 = 21,336`;
- H188 normalized B/C coefficient pairs: `36`;
- **H210 exact representatives: 768,096**.

This is a mathematically safe **16x reduction** from H188's `12,289,536` representatives. It is much stronger than H191's ~0.096% stabilizer saving; the two quotient systems have not yet been combined further.

Files:
- `research/h210_h175_residual_translation_quotient.md`
- `src/loto_research/h210_residual_translation_orbits.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H210_APPEND.md`

### Preserved H209 result
The official Rhode Island Lottery currently lists `Kick Back with Keno Promotion`, but H209 could not recover exact current campaign mechanics from public primary-source assets. Do not repeat the exhausted title/PDF/banner search variants without new evidence/indexing. Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist, but that promotion explicitly made doubled Keno tickets non-cancellable.

### Preserved H208-H207 execution result
Current RI online/iLottery is closed as a sole strict-guarantee H173/H175 execution channel because purchases can be delayed/refused under official Terms. Ordinary RI retailer/SSVM is also closed as the sole strict-guarantee channel because terminal jam/misprint/reissue before the target draw creates a non-atomic incomplete-acquisition branch under recovered public rules.

### Preserved H175/H191 mathematical state
The H175 4,336-play doubled 3-spot hybrid still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

- H185: 297 stored exact witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit exact counterexamples across two rejected candidates; timeout/no-incumbent remained inconclusive.
- H188: globally safe normalized representative count `12,289,536`.
- H189 full-S3 quotient was withdrawn by H190 as globally unsafe.
- H191 stabilizer-aware safe count `12,277,776` (~0.096% saving).
- **H210 independently supplies a much stronger exact quotient to 768,096 residual-translation classes.**
- No universal construction or restricted-family impossibility proof exists yet.

### Preserved promotion state
- Historical RI Lucky 3 Spot proves a genuine pre-draw printed 2x entitlement can exist, but eligible doubled tickets were explicitly non-cancellable.
- Ordinary paid Keno Plus is not a substitute because its multiplier is random and costs an equal add-on wager.
- Current `Kick Back with Keno Promotion` is officially visible/live, but exact current mechanics remain unrecovered and must not be guessed.
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
1. **Highest priority: enumerate/canonicalize the 768,096 H210 restricted diagonal classes against the accumulated exact balanced witness/cut bank.** Persist exact survivor count/list or solver-independent infeasibility evidence.
2. Run exact `n3<=2` separation only on surviving classes; timeout never validates a design.
3. If the restricted diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` while reusing accumulated balanced witnesses.
4. Reopen current `Kick Back with Keno` only on new primary evidence: exact campaign rules, retailer launch alert, campaign-detail page, or direct operator documentation.
5. Search other current lottery-issued deterministic pre-draw overlays in smaller state spaces that do not require thousands of separately accepted wagers.
6. Reopen RI H173/H175 execution only upon materially new forced-acceptance/atomic bulk mechanism or rule change.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H210_APPEND.md`.
Latest case: `research/h210_h175_residual_translation_quotient.md`.
