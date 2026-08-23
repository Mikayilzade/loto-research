# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H214 — joint H212 affine-unit + H191 exceptional-S3 symmetry audit**.

### H214 major result
H214 closes the joint-symmetry compatibility question deliberately left open by H212.

H191 proved that the extra coordinate S3 stabilizer is legal iff all three A layers have slope `a=15`, where each layer is `x0+x1+x2=c (mod16)` and is individually S3-invariant. H212's exact affine-unit enumeration contains exactly **9** A orbits wholly inside this exceptional sector, out of **3,992** total A orbits.

The H212 affine-unit action and H191 exceptional coordinate-S3 action are compatible at the set level in that sector. Therefore:
- 3,983 generic H212 A orbits retain all 36 normalized B/C coefficient classes;
- 9 exceptional `a=15` H212 A orbits may safely use the exact 15 S3 coefficient classes.

Exact safe joint representative count:

`3,983*36 + 9*15 = 143,523`.

This saves only 189 representatives (about 0.1315%) versus H212's 143,712, so the symmetry direction is now materially exhausted.

Files:
- `research/h214_h212_h191_joint_symmetry_audit.md`
- `src/loto_research/h214_h212_h191_joint_symmetry_audit.py`
- `data/derived/h214_h212_h191_joint_symmetry_summary.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H214_APPEND.md`

### H213 implementation note
`src/loto_research/h213_h212_cut_bank_enumeration.py` was added as the deterministic finite enumerator for screening H212 representatives against the accumulated exact cut bank. No H213 scientific survivor result is recorded yet; do not treat the existence of the script/workflow as evidence. The authoritative completed result is H214.

### Preserved H175 mathematical state
The unresolved H175 4,336-play doubled RI 3-spot hybrid still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

- H185: 297 stored exact witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit exact counterexamples across two rejected candidates; timeout/no-incumbent remained inconclusive.
- H188: globally safe normalized representative count `12,289,536`.
- H189 full-S3 quotient was withdrawn by H190 as globally unsafe.
- H191: stabilizer-aware extra S3 is valid only for A subsets wholly in the `a=15` sector.
- H210: residual translation quotient reduced the family to `768,096` classes.
- H211: combined translation/stabilizer count `767,361`.
- H212: stronger affine-unit quotient reduced conservatively to `143,712` classes.
- **H214: exact joint H212+H191 quotient safely reduces to `143,523` classes.**
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
1. **Highest priority: exact-screen the 143,523 H214 joint representatives against the accumulated 4,878 exact balanced witness/cut rows.** Persist exact survivor count/list or solver-independent infeasibility evidence.
2. Run exact `n3<=2` separation only on surviving classes; timeout never validates a design.
3. If the restricted diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` while reusing accumulated witnesses.
4. Reopen current `Kick Back with Keno` only on materially new primary evidence.
5. Search other current lottery-issued deterministic pre-draw overlays in smaller state spaces that do not require thousands of separately accepted wagers.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H214_APPEND.md`.
Latest case: `research/h214_h212_h191_joint_symmetry_audit.md`.
