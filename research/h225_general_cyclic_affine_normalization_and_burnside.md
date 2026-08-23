# H225 — general cyclic-affine normalization + exact Burnside quotient

Date: 2026-08-23
Status: mathematical reduction validated; no lottery SUCCESS

## Why this packet
H224 exact restricted-family output was still absent at packet start. Rather than spend another run only changing the same screen implementation, H225 advances the next branch already specified by STATUS: the general cyclic-affine family

`z = a*x + b*y + c (mod 16)`, with odd `a,b`.

This strictly contains the previous diagonal restriction `a=b`.

## 1. Exact coordinate-normalization theorem
Use independent affine relabelings of the five 16-point groups,

`x_g' = u_g*x_g + t_g`, with odd units `u_g`.

These relabelings biject balanced `4+4+4+4+4` draws and therefore preserve the universal `n3>=3` question.

For a layer `(a,b,c)` on support `(i,j,k)`, the transformed parameters are

- `a' = u_k*a/u_i`,
- `b' = u_k*b/u_j`,
- `c' = u_k*c - a'*t_i - b'*t_j + t_k` modulo 16.

For the three one-layer supports B=(0,3,4), C=(1,3,4), D=(2,3,4), every general design can be normalized exactly to

- `D = (1,1,0)`,
- `B = (1,beta,0)`,
- `C = (1,gamma,0)`,

where `beta,gamma` are odd. Swapping groups 0 and 1 exchanges B/C, so only 36 unordered `(beta,gamma)` sectors are needed.

## 2. Residual stabilizer
After that normalization, the remaining affine stabilizer has exactly the parameter form

- common odd scale `u`,
- free translations `t2,t3`,
- `t4=t2+t3`,
- `t0=t2+(1-beta)t3`,
- `t1=t2+(1-gamma)t3`.

Thus it has `8*16*16 = 2048` parameter elements.

On an A=(0,1,2) layer `(a,b,c)` it acts as

`(a,b,c) -> (a,b, u*c + (1-a-b)t2 - [a(1-beta)+b(1-gamma)]t3)`.

Important structural consequence: **A coefficients `(a,b)` are invariants of the residual action; only the shift moves.**

## 3. Exact Burnside quotient without enumerating 178m A triples
The A-layer universe has `8*8*16 = 1024` layers and a design chooses 3 distinct A layers. Naive normalized count after B/C ordering is

`36 * C(1024,3) = 6,423,588,864`.

H225 applies Burnside's lemma directly to 3-element subsets. If a permutation has `f1` fixed points, `f2` two-cycles and `f3` three-cycles, the number of fixed 3-subsets is exactly

`C(f1,3) + f1*f2 + f3`.

Because the residual action preserves each coefficient pair `(a,b)`, cycle counts reduce to affine permutations of only 16 shifts, making the complete Burnside calculation small and exact.

For `beta<gamma`, B/C swap identifies the two ordered sectors, so one residual quotient is retained. For `beta=gamma`, the swap is an internal stabilizer and H225 includes its full coset in the Burnside average.

## 4. Exact count
The verified result is:

- raw normalized classes before residual quotient: **6,423,588,864**;
- off-diagonal B/C sectors after residual quotient: **30,776,576**;
- diagonal B=C sectors including swap: **5,466,528**;
- total exact canonical general cyclic-affine classes: **36,243,104**.

This is a **177.236x exact reduction** from the normalized raw space.

Diagonal sector orbit counts are:

- beta 1: 1,010,284
- beta 3: 486,908
- beta 5: 749,164
- beta 7: 486,908
- beta 9: 1,010,284
- beta 11: 486,908
- beta 13: 749,164
- beta 15: 486,908

The residual-only sector counts take only three values: `968,384`, `1,491,648`, `2,013,888`.

## 5. Consequence
This does not prove or disprove a universal H175 construction. It does, however, make the specified post-restricted general family finite and precisely quantified at **36.24 million** canonical classes instead of 6.42 billion normalized raw classes (and vastly more before B/C/D normalization).

The accumulated 4,878 exact balanced witnesses can be reused as necessary cuts for this family once the restricted-family screen is resolved or in parallel with a general-family screen.

## Reproducibility
- `src/loto_research/h225_general_cyclic_affine_normalization.py`
- `src/loto_research/h225_general_cyclic_affine_burnside.py`

The Burnside code contains exact integer assertions for the totals and symmetry checks; no Monte Carlo or solver timeout is involved.
