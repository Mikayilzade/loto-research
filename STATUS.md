# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H211 — H175 combined residual-translation + stabilizer quotient**.

### H211 major result
H211 safely combines H210's exact residual `C16` translation quotient with H191's exceptional S3 stabilizer saving.

H210 translations preserve the A-layer coefficient `a`. H191's exceptional sector consists exactly of the 16 layers with `a=15`. On that sector H210 acts on shifts as `c -> c+13t (mod16)`; because 13 is invertible mod16, the action is free on every 3-element subset just as in H210.

Exact split:
- all A subsets: `C(128,3)=341,376`;
- exceptional `a=15` subsets: `C(16,3)=560`, hence `35` translation-orbits;
- generic subsets: `340,816`, hence `21,301` translation-orbits.

Applying H191's B/C coefficient class counts after H210 canonicalization gives:

`21,301*36 + 35*15 = 767,361`.

Therefore the current exact safe restricted-family checkpoint is **767,361 representatives**, improving H210 by 735 classes and H188 by about 16.016x.

Files:
- `research/h211_h175_combined_translation_stabilizer_quotient.md`
- `src/loto_research/h211_combined_translation_stabilizer_quotient.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H211_APPEND.md`

### Preserved H210/H191/H188 mathematical state
The unresolved H175 4,336-play doubled RI 3-spot hybrid still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

- H185: 297 stored exact witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit exact counterexamples across two rejected candidates; timeout/no-incumbent remained inconclusive.
- H188: globally safe normalized representative count `12,289,536`.
- H189 full-S3 quotient was withdrawn by H190 as globally unsafe.
- H191: stabilizer-aware safe saving applies only to A subsets wholly in the `a=15` sector.
- H210: residual translation quotient reduced the family to `768,096` classes.
- **H211: exact combined quotient reduces it to `767,361` classes.**
- No universal construction or restricted-family impossibility proof exists yet.

### Preserved H209 promotion state
The official Rhode Island Lottery currently lists `Kick Back with Keno Promotion`, but H209 could not recover exact current campaign mechanics from public primary-source assets. Do not repeat exhausted title/PDF/banner search variants without new evidence/indexing. Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist, but that promotion explicitly made doubled Keno tickets non-cancellable.

### Preserved H208-H207 execution state
Current RI online/iLottery is closed as a sole strict-guarantee H173/H175 execution channel because purchases can be delayed/refused under official Terms. Ordinary RI retailer/SSVM is also closed as the sole strict-guarantee channel because terminal jam/misprint/reissue before the target draw creates a non-atomic incomplete-acquisition branch under recovered public rules.

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
1. **Highest priority: enumerate/canonicalize the 767,361 H211 restricted diagonal classes against the accumulated exact balanced witness/cut bank.** Persist exact survivor count/list or solver-independent infeasibility evidence.
2. Run exact `n3<=2` separation only on surviving classes; timeout never validates a design.
3. If the restricted diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` while reusing accumulated balanced witnesses.
4. Reopen current `Kick Back with Keno` only on materially new primary evidence.
5. Search other current lottery-issued deterministic pre-draw overlays in smaller state spaces that do not require thousands of separately accepted wagers.
6. Reopen RI H173/H175 execution only upon materially new forced-acceptance/atomic bulk mechanism or rule change.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H211_APPEND.md`.
Latest case: `research/h211_h175_combined_translation_stabilizer_quotient.md`.
