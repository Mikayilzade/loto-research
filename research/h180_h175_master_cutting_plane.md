# H180 — H175 master-design cutting-plane prototype

Updated: 2026-08-22
Status: **NO SUCCESS; GENERAL H175 GATE REMAINS OPEN**

## Target
Advance H175 beyond repeated random-design screening. The unresolved condition is universal: every balanced `4+4+4+4+4` 20-number draw must complete at least three of the six add-on transversal layers (`n3>=3`).

## Exact restricted master family
H180 introduces a master MILP over a large structured Latin family rather than selecting one random design at a time.

Each candidate Latin layer is

`z = a*x + a*y + c (mod 16)`

with odd `a in {1,3,5,7,9,11,13,15}` and `c in {0,...,15}`. Because odd multiplication and translation are permutations modulo 16, every candidate is a Latin square.

There are 128 candidate layers for each support. H175 requires:
- 3 layers on support `(0,1,2)`;
- 1 layer on `(0,3,4)`;
- 1 layer on `(1,3,4)`;
- 1 layer on `(2,3,4)`.

Therefore this restricted master universe contains

`C(128,3) * 128^3 = 715,917,361,152`

distinct six-layer designs before any symmetry reduction.

## Cutting-plane method
For a finite accumulated set of balanced witnesses, the master MILP chooses six layers subject to `n3>=3` on every stored witness.

An exact adversarial separator MILP then searches the chosen design for any balanced draw with `n3<=2`:
- exactly 4 selected symbols in each of five 16-symbol groups;
- binary hit variables for every selected transversal triple;
- total completed triples constrained to at most 2.

If a witness exists, it is added to the master as a new cut. A separator timeout is never interpreted as validation. Master infeasibility on accumulated exact cuts would prove the entire restricted family impossible.

## H180 deterministic run
Seed: `180180`.
Initial random balanced cuts: 8.

Twenty master/separator cycles completed with solver status `optimal` for both the master and separator. Every master-selected design was exactly rejected by a balanced `n3<=2` witness.

Separator-score sequence:

`[2,1,2,0,2,2,2,2,2,2,2,2,2,2,0,2,0,0,2,2]`

Histogram:
- `n3=0`: 4 master candidates;
- `n3=1`: 1 master candidate;
- `n3=2`: 15 master candidates.

Thus **20/20 adaptively chosen master candidates were broken by exact MILP**, including candidates explicitly optimized to survive all previously accumulated cuts. This is materially stronger evidence than another independent random bank.

The run had not yet driven the master to infeasibility, so it is **not** a proof that all 715.9B designs in the restricted family fail. It is also not evidence that any surviving master solution satisfies unseen balanced draws.

## Interpretation
H180 validates the intended master-design + adversarial-separation architecture from STATUS and shows that the H175 gate remains highly fragile even under adaptive design selection.

The important new distinction is methodological:
- H178/H179: screen fixed/random concrete designs;
- H180: let a master optimizer redesign the six layers after every exact counterexample, then attack the new optimum again.

Twenty consecutive exact separations mean the optimizer has not found even a locally cut-resistant diagonal cyclic-affine construction yet.

## Next action
1. Continue the H180 exact cut loop until either:
   - the restricted master becomes infeasible, yielding a proof for the entire diagonal cyclic-affine family; or
   - an exact separator proves infeasible for a candidate with a sufficiently long/verified solve, yielding a promising design requiring independent certification.
2. If the restricted family closes, expand the master pool to general cyclic-affine `z=a*x+b*y+c (mod 16)` with odd independent `a,b` (1,024 layers/support), using persisted witness cuts and memory-safe batching.
3. General H175 remains open until a construction or impossibility result covers arbitrary allowed Latin/transversal designs.

## Reproducibility
Code: `src/loto_research/h180_h175_master_cutting_plane.py`.

## Result
**ЕЩЁ НЕ УСПЕХ.** Twenty adaptive master designs from a 715.9-billion-design restricted H175 family were each exactly broken by balanced `n3<=2` witnesses, but the family has not yet been proved infeasible.
