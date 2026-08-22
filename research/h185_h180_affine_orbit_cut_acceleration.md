# H185 — H180 affine-orbit cut acceleration

Updated: 2026-08-22
Status: **NO SUCCESS; RESTRICTED DIAGONAL CYCLIC-AFFINE FAMILY STILL FEASIBLE**

## Target
Continue the H175/H180 4,336-play balanced transversal gate from the authoritative H184 checkpoint. The unresolved requirement remains: every balanced `4+4+4+4+4` draw must complete at least three of the six transversal layers (`n3>=3`).

Restricted layer family remains

`z = a*x + a*y + c (mod 16)`, `a` odd.

## Starting checkpoint
H183 persisted 254 balanced necessary cuts. H184 then exactly rejected its recorded current master candidate with one additional `n3=2` witness, so the authoritative pre-H185 state was 255 known cuts.

H185 merged H184's exact delta and continued the master/adversary loop. In addition to the official H184 witness, H185 generated **42 further explicit balanced counterexamples**. Every heuristic witness was accepted only after exact recomputation of its completed-triple count.

H185-only score histogram:
- `n3=0`: **6**;
- `n3=1`: **3**;
- `n3=2`: **33**.

Thus all **42/42 H185-tested candidates** were explicitly rejected. Together with H184's exact delta, there are 43 post-H183 witnesses.

## Safe common-affine orbit cuts
The major acceleration is to expand every post-H183 witness under

`x' = u*x + v (mod 16)`,

for odd `u in {1,3,5,7,9,11,13,15}` and `v in {0,...,15}`.

This gives at most 128 images per witness. Each image is itself a legal balanced `4+4+4+4+4` draw, so its `n3>=3` inequality is automatically a valid necessary cut for any universal design.

The transformation also preserves the restricted family. A layer

`z = a*x + a*y + c`

becomes

`z' = a*x' + a*y' + [u*c + (1-2a)*v] (mod 16)`,

so the same odd `a` remains and only the shift changes.

After deduplication, H185's active master contains **4,878 unique balanced cut rows**.

## Persistent merged bank
Stored exact witnesses:
- H183 base: 254;
- H184 official exact delta: 1;
- H185 new explicit witnesses: 42;
- **merged actual witness bank: 297**.

The orbit-expanded rows are regenerated deterministically from bank indices `>=254`; they need not be stored individually.

Files:
- `data/derived/h185_h180_witness_bank.zlib.b64`
- `data/derived/h185_h180_affine_orbit_delta.json`
- `src/loto_research/h185_h180_affine_orbit_cut_acceleration.py`

## Solver discipline
No timeout is interpreted as validation. One intermediate master call returned a time-limited incumbent; that candidate was independently checked against all 4,558 active cuts at that stage and had minimum cut score 4 before its separate explicit `n3=0` counterexample was added. All other reported master checkpoints were feasible solver solutions; candidate rejection always uses an explicit balanced witness with exact recomputed `n3<=2`.

## Current master after 4,878 active rows
The symmetry-reduced master is still feasible. The current unresolved ids are

`[[18,54,111],[12],[88],[16]]`.

Parameters:
- support `(0,1,2)`: `(a,c)=(3,2),(7,6),(13,15)`;
- support `(0,3,4)`: `(1,12)`;
- support `(1,3,4)`: `(11,8)`;
- support `(2,3,4)`: `(3,0)`.

This is only the next separator target, not a validated construction.

## Interpretation
The restricted family has not been proved impossible, but the exact continuation is materially stronger than H184: 297 reusable explicit witnesses now generate 4,878 unique active necessary cuts, and 42 additional H185 candidates have been broken.

## Next action
1. Attack current master ids `[[18,54,111],[12],[88],[16]]` and continue the orbit-accelerated loop.
2. If solve time grows, add targeted single-group translation/orbit rows or a stronger exact master formulation rather than restarting.
3. A master infeasibility result on these valid cuts proves the entire symmetry-reduced restricted family impossible; a separator timeout does not validate a candidate.
4. If the diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod 16)` with independent odd `a,b`, reusing all balanced witnesses.

## Result
**ЕЩЁ НЕ УСПЕХ.** H185 raises the persistent exact witness bank to 297 and the active symmetry/orbit cut set to 4,878, but the restricted diagonal cyclic-affine master remains feasible.