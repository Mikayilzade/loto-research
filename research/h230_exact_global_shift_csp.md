# H230 — exact globally consistent shift CSP for the H225 general cyclic-affine family

Date: 2026-08-23
Status: INCONCLUSIVE / exact computation launched

## Scope
Lottery-only continuation of the Rhode Island Keno H175 4,336-play hybrid search. No non-lottery branches considered.

## Why H230 is materially stronger than H229
H229 screens the 306,450 H228 quotient coefficient states with H226's rowwise optimistic envelope. That envelope may allow a state because witness 1 is maximized by one shift choice and witness 2 by a different incompatible shift choice.

H230 removes that relaxation. For each quotient coefficient-state representative that passes the H226 envelope, it enumerates the complete legal shift state space for the three A layers and requires **one globally consistent shift tuple** to satisfy every stored exact balanced-witness constraint simultaneously.

Legal shift counts per coefficient pattern are finite and exact:
- three distinct coefficient blocks: `16^3 = 4096` shift tuples;
- one repeated coefficient block: `C(16,2)*16 = 1920` canonical legal tuples;
- all three coefficient blocks equal: `C(16,3) = 560` canonical legal tuples.

For repeated coefficient blocks, canonical increasing shifts remove only permutations of identical A layers; they do not remove distinct designs.

## Exact predicate
For normalized sector `(beta,gamma)`, fixed B/C/D incidence determines required A incidence `need(w)=max(0,3-B(w)-C(w)-D(w))` for each exact balanced witness signature `w`.

An actual A shift tuple survives the stored bank iff for every stored witness:

`A_p(w,c1) + A_q(w,c2) + A_r(w,c3) >= need(w)`.

H230 filters candidate shift tuples witness-by-witness. Witness ordering is only a runtime heuristic; all witness constraints are applied exactly.

## Symmetry / proof standard
H230 searches exactly one coefficient-multiset representative from every H228 true stabilizer orbit in each of the 11 ordered-sector orbits. This is WLOG because those stabilizers are automorphisms of the complete support/design problem.

If a representative actual design is killed by a stored balanced witness, every design in its symmetry orbit is killed by the corresponding inverse-transformed balanced witness. The transformed witness does not need to be separately present in the stored bank for the existence-of-counterexample proof.

Therefore, if H230 returns:

`exact_shift_surviving_coefficient_states = 0`,

then **every design in the full H225 general cyclic-affine family has a balanced draw with n3<=2**, and the entire family is finitely closed.

If positive survivors remain, they pass only the accumulated witness bank and still require exact unrestricted `n3<=2` separation before any construction can be validated.

## Execution
Added:
- `src/loto_research/h230_exact_shift_csp_screen.py`
- `.github/workflows/h230-exact-shift-csp.yml`

Target artifact:
- `data/derived/h230_exact_shift_csp.json`

The workflow has a 360-minute ceiling and rebases before committing the result. Timeout or missing output remains inconclusive.

## Next action
1. Check H230 result first; also accept a late H229 result.
2. If H230 has zero exact shift survivors, close H225 general cyclic-affine family immediately.
3. If H230 has actual shift survivors, run exact unrestricted `n3<=2` separation only on those designs, adding any new counterexamples back into the witness bank and iterating.
4. Separately accept any late zero-survivor restricted-family artifact under H221.
