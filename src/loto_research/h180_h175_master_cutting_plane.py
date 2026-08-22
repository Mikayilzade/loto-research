"""H180: master-design cutting-plane prototype for H175's balanced n3>=3 gate.

Exact framework over the diagonal cyclic-affine Latin family
    z = a*x + a*y + c (mod 16), a odd, c in 0..15.
There are 128 candidate Latin layers per support. H175 chooses 3 layers on
support (0,1,2) and one layer on each of (0,3,4),(1,3,4),(2,3,4), so this
restricted master space contains C(128,3)*128^3 = 715,917,361,152 designs.

Each iteration:
1) master MILP chooses six layers satisfying all accumulated balanced witnesses;
2) exact separator MILP searches a balanced 4+4+4+4+4 draw with n3<=2;
3) any witness is added as a cutting plane.

A separator timeout/infeasibility is NOT treated as validation. A master
infeasibility would be a proof that this entire restricted family cannot meet
universal n3>=3.
"""
from __future__ import annotations

import gc
import random
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix, csr_matrix

ODDS = np.array([1, 3, 5, 7, 9, 11, 13, 15], dtype=int)
PARAMS = np.array([(a, a, c) for a in ODDS for c in range(16)], dtype=int)
SUPPORTS = [(0, 1, 2), (0, 3, 4), (1, 3, 4), (2, 3, 4)]
NP = len(PARAMS)


def random_witness(rng: random.Random):
    return [sorted(rng.sample(range(16), 4)) for _ in range(5)]


def layer_hits(witness, support):
    i, j, k = support
    xs = np.array(witness[i])
    ys = np.array(witness[j])
    target = np.zeros(16, dtype=np.int8)
    target[witness[k]] = 1
    values = (
        PARAMS[:, 0, None, None] * xs[None, :, None]
        + PARAMS[:, 1, None, None] * ys[None, None, :]
        + PARAMS[:, 2, None, None]
    ) % 16
    return target[values].sum(axis=(1, 2)).astype(float)


def solve_master(witnesses, time_limit=10.0):
    n = 4 * NP
    rows = 4 + len(witnesses)
    A = lil_matrix((rows, n))
    lb = np.empty(rows)
    ub = np.empty(rows)

    for s in range(4):
        A[s, s * NP : (s + 1) * NP] = 1
        required = 3 if s == 0 else 1
        lb[s] = ub[s] = required

    for r, witness in enumerate(witnesses, start=4):
        for s, support in enumerate(SUPPORTS):
            A[r, s * NP : (s + 1) * NP] = layer_hits(witness, support)
        lb[r] = 3
        ub[r] = np.inf

    result = milp(
        np.zeros(n),
        integrality=np.ones(n, dtype=int),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=LinearConstraint(csr_matrix(A), lb, ub),
        options={"time_limit": time_limit, "presolve": True},
    )
    del A
    gc.collect()

    if result.x is None:
        return None, result

    chosen = []
    for s in range(4):
        chosen.append(
            np.flatnonzero(result.x[s * NP : (s + 1) * NP] > 0.5).tolist()
        )
    return chosen, result


def build_triples(chosen):
    triples = []
    for s, (i, j, k) in enumerate(SUPPORTS):
        for pid in chosen[s]:
            a, b, c = map(int, PARAMS[pid])
            for x in range(16):
                for y in range(16):
                    z = (a * x + b * y + c) % 16
                    triples.append((i * 16 + x, j * 16 + y, k * 16 + z))
    return np.asarray(triples, dtype=np.int16)


def exact_separator(triples, time_limit=8.0):
    """Find a balanced draw with <=2 completed triples, exactly via MILP."""
    m = len(triples)
    n = 80 + m
    A = lil_matrix((5 + m + 1, n))
    lb = np.full(5 + m + 1, -np.inf)
    ub = np.full(5 + m + 1, np.inf)

    for g in range(5):
        A[g, g * 16 : (g + 1) * 16] = 1
        lb[g] = ub[g] = 4

    for q, (a, b, c) in enumerate(triples):
        r = 5 + q
        A[r, int(a)] = 1
        A[r, int(b)] = 1
        A[r, int(c)] = 1
        A[r, 80 + q] = -1
        ub[r] = 2

    A[5 + m, 80:] = 1
    ub[5 + m] = 2

    result = milp(
        np.zeros(n),
        integrality=np.ones(n, dtype=int),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=LinearConstraint(csr_matrix(A), lb, ub),
        options={"time_limit": time_limit, "presolve": True},
    )
    del A
    gc.collect()

    if result.x is None:
        return None, result

    selected = result.x[:80] > 0.5
    witness = [
        [i for i in range(16) if selected[g * 16 + i]] for g in range(5)
    ]
    score = int(
        np.sum(
            selected[triples[:, 0]]
            & selected[triples[:, 1]]
            & selected[triples[:, 2]]
        )
    )
    return (score, witness), result


def main(iterations=20):
    rng = random.Random(180180)
    witnesses = [random_witness(rng) for _ in range(8)]
    scores = []

    for iteration in range(iterations):
        chosen, master = solve_master(witnesses)
        print("iteration", iteration, "master_status", master.status, "cuts", len(witnesses))
        if chosen is None:
            print("MASTER_INFEASIBLE", master.message)
            return

        printable = [[PARAMS[i].tolist() for i in ids] for ids in chosen]
        print("chosen", printable)
        triples = build_triples(chosen)
        separated, separator = exact_separator(triples)
        print("separator_status", separator.status, separator.message)
        if separated is None:
            print("NO_EXACT_WITNESS_RETURNED")
            return

        score, witness = separated
        scores.append(score)
        print("n3", score, "witness", witness)
        witnesses.append(witness)

    print("scores", scores)
    print("histogram", {s: scores.count(s) for s in sorted(set(scores))})


if __name__ == "__main__":
    main()
