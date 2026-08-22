# H175 — Rhode Island doubled-Keno 4,336-play hybrid transversal gate

Updated: 2026-08-22
Status: **NEW SUB-4,560 CONDITIONAL DESIGN CLASS IDENTIFIED / FIRST AFFINE REALIZATION REJECTED / NOT SUCCESS**

## Purpose
H173/H174 established a conditional strict-positive doubled 3-spot Keno cover with 4,560 plays and proved it cheapest inside the complete 1–8 group clique-partition family. H175 searches outside that family.

The conditional numerical assumptions remain unchanged from H172-H174: a free deterministic pre-locked 2x on a 3-spot table paying $25 for 3/3 and $2.50 for 2/3 per $1 base wager. These assumptions are still not current-primary-verified for the live Rhode Island promotion, so this packet is mathematical design work only.

## Base: five groups of sixteen
Partition the 80 Keno numbers into five disjoint groups of 16 and buy every internal triple.

- base plays = `5*C(16,3)=2,800`;
- exact worst-case doubled gross = $2,800;
- the unique count-composition attaining that minimum is `4+4+4+4+4`.

The next-lowest base composition is `3+4+4+4+5`, paying $2,975.

Thus 5x16 is an exact break-even skeleton that can potentially be lifted with a much smaller cross-group add-on.

## Transversal Latin-square add-on
For any three 16-number groups A,B,C, one Latin-square transversal layer contains exactly 256 triples, one for every ordered pair `(a,b)` with a unique `c=L(a,b)`.

For a draw taking `a,b,c` numbers from those three groups, every selected cross-pair belongs to exactly one layer block. Therefore if `n3` of the layer blocks are fully contained in the draw,

`Q = ab+ac+bc = n2+3*n3`

and the doubled payout from the layer is exactly

`5*Q + 35*n3`.

In particular the pair-only lower bound is `5*(ab+ac+bc)`, independent of the actual Latin square.

## Six-layer / 4,336-play hybrid
Add exactly six 256-block transversal layers to the 2,800-play base:

- add-on plays = `6*256 = 1,536`;
- total plays/cost = **4,336**.

There are 10 choices of a three-group support among five groups. H175 exhaustively enumerated all weak allocations of six layers across those 10 supports:

`C(6+10-1,10-1)=C(15,9)=5,005` allocations.

For each allocation, all 10,451 feasible draw count-compositions `(s1,...,s5)` with `0<=si<=16` and `sum si=20` were evaluated using:

`base_pay(si) + 5 * sum_layers (s_i s_j + s_i s_k + s_j s_k)`.

### Key allocation
A particularly strong allocation is:

- 3 layers on groups `(0,1,2)`;
- 1 layer on `(0,3,4)`;
- 1 layer on `(1,3,4)`;
- 1 layer on `(2,3,4)`.

For this allocation:

- balanced `4+4+4+4+4` pair-only gross = **$4,240**;
- every **non-balanced** count-composition has pair-only gross at least **$4,370**;
- total cost is **$4,336**.

Therefore every non-balanced draw is already strict-positive without using any full-triple bonus at all.

The entire guarantee problem collapses to the balanced count-composition.

## Exact remaining balanced condition
In a balanced draw, each Latin layer contributes pair-only payout `$240`, so six layers contribute `$1,440` and the 2,800-play base contributes $2,800:

`2,800 + 1,440 = 4,240`.

Each fully contained transversal triple replaces three pair-only incidences with a 3/3 result and increases payout by an additional **$35**.

To beat the $4,336 cost strictly:

`4,240 + 35*n3 > 4,336`

so it is necessary and sufficient that

**`n3 >= 3` for every balanced 4-from-each-group draw.**

If such six Latin layers can be constructed, the hybrid would have:

- cost = $4,336;
- worst gross >= `$4,240 + 3*$35 = $4,345`;
- strict pre-tax surplus >= **+$9**;
- strict gross floor >= **100.2076%**.

This would improve the wager count from H173's 4,560 to 4,336, a **4.91% reduction**.

## First explicit affine realization: REJECTED
H175 tested the natural GF(16) affine family `L_alpha(r,c)=r + alpha*c` using finite-field arithmetic.

For the strong support allocation above, a concrete realization used:

- coefficients `1,2,4` for the three `(0,1,2)` layers;
- coefficient `1` for each of `(0,3,4)`, `(1,3,4)`, `(2,3,4)`.

A binary MILP with exactly four selected symbols in each of the five groups minimized the number of fully contained transversal blocks across all 1,536 add-on triples.

Result:

**minimum balanced full triples = 0.**

Hence that natural affine construction fails the required `n3>=3` gate and is rejected.

Separate affine screening also showed that concentrating 1–5 affine layers on one three-group support can leave at least four output symbols absent from some balanced 4x4 submatrix, allowing zero full triples for an adversarial 4-symbol choice. Six concentrated affine layers improve output coverage but still fail broader near-balanced requirements in tested candidates.

## What H175 proves
1. H173 is not yet a mathematical lower bound outside clique partitions.
2. A concrete **4,336-play candidate architecture** exists whose only unresolved combinatorial requirement is extremely sharp: six 16x16 Latin/transversal layers must hit every balanced five-group draw in at least three full blocks.
3. For the strong 3+1+1+1 support allocation, **all non-balanced count-compositions are already safe by pair counting alone**.
4. The first natural GF(16) affine realization fails exactly, with a MILP adversarial balanced draw containing zero full add-on triples.

## Result
- New sub-4,560 target: **4,336 plays**.
- Non-balanced compositions: **closed positive** for the identified support allocation, pair-only floor $4,370 > $4,336.
- Balanced composition: requires universal `n3>=3`.
- First affine realization: **REJECTED (MILP minimum n3=0)**.
- Terminal SUCCESS: **NO**.

## Next research
1. Solve the balanced `n3>=3` six-layer transversal design problem using CP-SAT/MILP/cutting planes or prove it impossible.
2. Search non-affine Latin squares / permutations and mixed support allocations that preserve the non-balanced $4,336 floor.
3. If 4,336 is impossible, test 7-layer and other hybrid constructions only when total play count remains below 4,560.
4. In parallel, continue recovery of current official Rhode Island promotion/paytable/execution terms; none of this becomes executable without a current free pre-locked 2x.
