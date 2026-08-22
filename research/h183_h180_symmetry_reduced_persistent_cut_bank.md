# H183 — H180 symmetry reduction + persistent 246-counterexample cut bank

Updated: 2026-08-22
Status: **NO SUCCESS; RESTRICTED DIAGONAL CYCLIC-AFFINE FAMILY STILL FEASIBLE AFTER 246 ADAPTIVE COUNTEREXAMPLES**

## Target
Continue H180's exact master/separator search for the unresolved H175 condition: six transversal layers must produce `n3 >= 3` for every balanced `4+4+4+4+4` draw.

Restricted H180 layer family:

`z = a*x + a*y + c (mod 16)`, with odd `a in {1,3,5,7,9,11,13,15}` and `c in 0..15`.

Support allocation remains:
- three layers on `(0,1,2)`;
- one layer on `(0,3,4)`;
- one layer on `(1,3,4)`;
- one layer on `(2,3,4)`.

H180's unrestricted restricted-family count was `C(128,3)*128^3 = 715,917,361,152` designs.

## Exact WLOG symmetry reduction
H183 adds two transformations that preserve the universal balanced-draw property and remain inside the restricted family.

### 1. Normalize the `(2,3,4)` layer shift to `c=0`
Apply the same translation `x' = x+v` to the local symbols of all five groups. A layer

`z = a*x + a*y + c`

becomes

`z' = a*x' + a*y' + [c + (1-2a)v] (mod 16)`.

For odd `a`, `1-2a` is odd and therefore invertible modulo 16. Hence for the chosen `(2,3,4)` layer there is always a `v` making the transformed shift zero. Balanced 4-subsets are mapped bijectively, so a universally valid design exists iff an equivalent orientation with this selected layer having `c=0` exists.

Thus the fourth support needs only 8 candidate representatives instead of 128.

### 2. Order the `(0,3,4)` and `(1,3,4)` single layers
Swapping groups 0 and 1 leaves every `(0,1,2)` layer unchanged because `a*x+a*y+c` is symmetric in its first two inputs. The swap exchanges only the `(0,3,4)` and `(1,3,4)` layers. Therefore one may require the candidate id on `(0,3,4)` to be no greater than the candidate id on `(1,3,4)` without losing an equivalence class.

The symmetry-reduced master orientation count is therefore

`C(128,3) * [128*129/2] * 8 = 22,547,202,048`,

about **31.75x smaller** than the raw H180 restricted universe. This is a symmetry reduction, not a claim that all orbits have equal size.

## Faster but still rigorous separation loop
H183 keeps H180's exact master MILP but uses a fast balanced local-search adversary first. This changes only witness discovery, not the proof standard:
- any returned witness explicitly contains exactly four symbols from each group;
- its `n3` is recomputed exactly from the chosen 1,536 transversal triples;
- any explicit `n3<=2` witness is therefore a rigorous rejection of that master candidate;
- if local search stops above 2, the exact MILP separator is invoked;
- timeout/inconclusive solver status is never accepted as validation.

## Substantial continuation result
Starting from the same 8 deterministic initial H180 random balanced cuts, H183 generated **246 additional adaptive counterexample cuts** against successive symmetry-reduced master solutions.

Exact score histogram of those 246 rejected master candidates:
- `n3=0`: **20**;
- `n3=1`: **45**;
- `n3=2`: **181**.

So **246/246 master-selected candidates were explicitly broken**.

One candidate was materially harder for the local adversary: after 73 adaptive cuts, local search stopped at `n3=3`. Its layer ids were
- `(0,1,2)`: `[15,21,90]` = `(a,c) = (1,15),(3,5),(11,10)`;
- `(0,3,4)`: id `1` = `(1,1)`;
- `(1,3,4)`: id `96` = `(13,0)`;
- `(2,3,4)`: id `32` = `(5,0)`.

The exact MILP separator then found the balanced witness

`[[0,1,8,9], [4,5,12,13], [0,8,10,14], [0,2,8,10], [5,7,13,15]]`

with **exact `n3=2`**, so the apparently boundary-level candidate was rejected rather than misclassified as success.

## Persistent checkpoint
The full accumulated bank now contains:
- 8 initial H180 balanced cuts;
- 246 adaptive H183 counterexample cuts;
- **254 total balanced necessary cuts**.

It is saved compressed at:

`data/derived/h183_h180_witness_bank.zlib.b64`

Continuation code:

`src/loto_research/h183_h180_symmetry_persistent_cuts.py`

This fixes an important H180 workflow weakness: later runs can resume from the accumulated adversarial bank instead of regenerating the first cuts.

## Current master state after all 254 persisted cuts
The symmetry-reduced master is **still feasible**. One current master solution after all persisted cuts has ids:
- `(0,1,2)`: `[3,16,94]` = `(a,c) = (1,3),(3,0),(11,14)`;
- `(0,3,4)`: `[1]` = `(1,1)`;
- `(1,3,4)`: `[9]` = `(1,9)`;
- `(2,3,4)`: `[16]` = `(3,0)`.

This candidate has not been certified and must be attacked by the next separator run. Master feasibility after a finite cut bank is **not** evidence that it satisfies unseen balanced draws.

## What H183 establishes
1. H180 can be reduced WLOG from 715.9B raw designs to a 22.55B orientation master.
2. The adaptive exact-rejection bank grows from H180's 20 candidates to **246 additional explicitly broken master candidates**.
3. A heuristic-hard `n3=3` candidate was independently broken by exact MILP at `n3=2`, confirming the timeout/non-validation discipline.
4. The adversarial witness bank is now persisted and reusable.
5. The restricted diagonal cyclic-affine family is **not yet proved impossible** because the master remains feasible after the finite cut bank.

## Next action
1. Resume directly from the 254 persisted witnesses and separate the current master solution; continue until master infeasibility or an exact separator is certified infeasible.
2. Add safe symmetry/orbit-derived witness batches or stronger valid inequalities if they materially accelerate master closure.
3. If the restricted family becomes infeasible, expand to general cyclic-affine `z=a*x+b*y+c (mod 16)` with independent odd `a,b`.
4. Do not call a solver timeout or local-search minimum above 2 a valid construction.

## Result
**ЕЩЁ НЕ УСПЕХ.** The H175 sub-4,560 design gate is much more tightly constrained and persistent now, but no universal `n3>=3` construction or impossibility proof has yet been obtained.
