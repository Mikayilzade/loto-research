"""H175: 5x16 base + six Latin-square transversal layers.

Conditional model inherited from H172-H174:
$1 3-spot wager, free deterministic 2x, payouts $50 for 3/3 and $5 for 2/3.
"""
from itertools import combinations, product
from math import comb
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix, csr_matrix

GROUP_TRIPLES = list(combinations(range(5), 3))


def base_pay(s: int) -> int:
    return 50 * comb(s, 3) + 5 * comb(s, 2) * (16 - s)


def allocations(total: int, cells: int, pref=()):
    if cells == 1:
        yield pref + (total,)
    else:
        for x in range(total + 1):
            yield from allocations(total - x, cells - 1, pref + (x,))


def composition_screen():
    comps = [x for x in product(range(17), repeat=5) if sum(x) == 20]
    rows = []
    for alloc in allocations(6, 10):
        worst = 10**9
        worst_nonbalanced = 10**9
        worst_comp = None
        for s in comps:
            gross = sum(base_pay(x) for x in s)
            for mult, (i, j, k) in zip(alloc, GROUP_TRIPLES):
                gross += 5 * mult * (s[i]*s[j] + s[i]*s[k] + s[j]*s[k])
            if gross < worst:
                worst, worst_comp = gross, s
            if s != (4, 4, 4, 4, 4):
                worst_nonbalanced = min(worst_nonbalanced, gross)
        rows.append((worst_nonbalanced, worst, alloc, worst_comp))
    return sorted(rows, reverse=True)


def gf_mul(a: int, b: int) -> int:
    # GF(16), irreducible polynomial x^4+x+1 (0b10011)
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 0x10:
            a ^= 0x13
    return out & 0xF


def latin_blocks(group_triple, alpha):
    i, j, k = group_triple
    for r in range(16):
        for c in range(16):
            z = r ^ gf_mul(alpha, c)
            yield (16*i+r, 16*j+c, 16*k+z)


def affine_counterexample_minimum():
    design = [
        ((0,1,2),1), ((0,1,2),2), ((0,1,2),4),
        ((0,3,4),1), ((1,3,4),1), ((2,3,4),1),
    ]
    blocks = [b for t,a in design for b in latin_blocks(t,a)]
    nx, ny = 80, len(blocks)
    n = nx + ny
    c = np.zeros(n)
    c[nx:] = 1
    A = lil_matrix((5+ny, n), dtype=float)
    lower = np.full(5+ny, -np.inf)
    upper = np.full(5+ny, np.inf)
    for g in range(5):
        for v in range(16*g, 16*(g+1)):
            A[g,v] = 1
        lower[g] = upper[g] = 4
    for q, block in enumerate(blocks):
        row = 5+q
        for v in block:
            A[row,v] = 1
        A[row,nx+q] = -1
        upper[row] = 2  # y >= x1+x2+x3-2
    res = milp(
        c,
        integrality=np.ones(n),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=LinearConstraint(csr_matrix(A), lower, upper),
    )
    return res.fun, res


if __name__ == "__main__":
    best = composition_screen()[0]
    print("best nonbalanced floor / overall pair floor / allocation / witness:", best)
    fun, res = affine_counterexample_minimum()
    print("affine balanced minimum full triples:", fun)
    print(res.message)
