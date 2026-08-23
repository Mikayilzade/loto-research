# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H225 — general cyclic-affine normalization + exact Burnside quotient**.

### H225 major result
H224's restricted-family exact output was still absent at H225 start, so no restricted-family closure was inferred. Instead of spending another packet only polling/reimplementing that screen, H225 advanced the next mathematical branch already specified in the queue: general cyclic-affine layers `z=a*x+b*y+c (mod16)` with odd `a,b`, strictly containing the previous diagonal `a=b` family.

Using independent affine relabelings of the five 16-point groups, every general design is proved WLOG-normalizable to sole layers
- `D=(1,1,0)`,
- `B=(1,beta,0)`,
- `C=(1,gamma,0)`,
with odd `beta,gamma`; group0/group1 swap reduces these to 36 unordered B/C sectors.

The exact residual stabilizer has `8*16*16=2048` elements and acts on each A layer `(a,b,c)` by preserving `(a,b)` and changing only `c`. Burnside's lemma then counts orbits of 3-element A-layer subsets exactly, without enumerating `C(1024,3)` triples.

Exact finite-space result:
- normalized raw classes: `36*C(1024,3) = 6,423,588,864`;
- off-diagonal B/C canonical classes: `30,776,576`;
- diagonal B=C canonical classes including swap stabilizer: `5,466,528`;
- **total exact general cyclic-affine canonical classes: `36,243,104`**;
- exact reduction from normalized raw space: **177.236x**.

Files:
- `src/loto_research/h225_general_cyclic_affine_normalization.py`
- `src/loto_research/h225_general_cyclic_affine_burnside.py`
- `research/h225_general_cyclic_affine_normalization_and_burnside.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H225_APPEND.md`

This is a mathematical reduction, not a universal construction or impossibility proof.

### Preserved H224/H221 restricted-family state
- H224 bulk-vectorized exact screen target `data/derived/h224_bulk_vectorized_survivors.json` was absent at H225 start; missing output remains inconclusive.
- H219/H222/H223 earlier exact full-screen outputs were also not authoritative closure results.
- H221 proves that any schema-valid exact full restricted screen with `survivor_count=0` over all 143,712 H212-normalized classes is itself a complete finite impossibility certificate for that restricted family; no second MILP is required.

### Preserved H175 mathematical state
The unresolved H175 4,336-play doubled RI 3-spot hybrid still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

Restricted diagonal family:
- H185: 297 stored exact witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit exact counterexamples across two rejected candidates.
- H212: affine-unit quotient `143,712` classes.
- H214: exact joint H212+H191 quotient `143,523` classes.
- H224: fastest exact restricted cut-bank screen implementation so far; result pending through H225 start.

General cyclic-affine family:
- H225 exact normalization/Burnside quotient: **36,243,104 canonical classes**.
- The same 4,878 exact balanced witnesses are valid necessary cuts and can be reused for general-family screening.
- No universal construction or general-family impossibility proof exists yet.

### Preserved promotion/execution state
- Current RI `Kick Back with Keno Promotion` is officially visible, but exact current mechanics remain unrecovered; do not repeat H209's exhausted searches without new evidence.
- Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist, but doubled tickets were explicitly non-cancellable.
- Current RI online/iLottery and ordinary retailer/SSVM remain closed as sole strict-guarantee execution channels under recovered public rules.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeovers materially closed; residual raffle takeover theorem exists but tested boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias route needs reliable bulk history.
- Several Keno/Pick conditional overlays can reach/exceed 100% only in favorable modifier states; random modifier assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- H173 conditional 4,560-play doubled RI 3-spot cover remains mathematically valid.
- H175 4,336-play hybrid remains open pending universal `n3>=3` construction/impossibility plus executable pre-draw subsidy/channel conditions.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Check H224/H223/H222/H219 exact restricted-screen result artifacts first.** If any schema-valid result has zero survivors, close the H212 restricted diagonal family immediately under H221. If survivors remain, exact-separate only those survivors.
2. In parallel / if restricted outputs remain operationally blocked, build an exact cut-bank pre-screen for the H225 **36,243,104** general cyclic-affine canonical classes, exploiting the coefficient-pair preservation and Burnside sector structure rather than enumerating raw designs.
3. For any surviving general-family candidate, run exact `n3<=2` separation; timeout never validates a design.
4. Reopen current `Kick Back with Keno` only on materially new primary evidence.
5. Do not spend future packets merely swapping equivalent restricted-screen implementations unless concrete diagnostics identify a new fix.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H225_APPEND.md`.
Latest case: `research/h225_general_cyclic_affine_normalization_and_burnside.md`.
