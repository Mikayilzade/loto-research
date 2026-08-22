"""H183: symmetry-reduced persistent cutting-plane continuation for H175/H180.

Target gate: six transversal Latin layers must satisfy n3 >= 3 for every
balanced 4+4+4+4+4 draw.  This script continues the restricted H180 family

    z = a*x + a*y + c (mod 16),  a odd.

Two exact WLOG symmetry reductions are added:
1) the single layer on support (2,3,4) may be normalized to c=0 by applying
   the same translation x -> x+v in all five 16-symbol groups;
2) supports (0,3,4) and (1,3,4) may be ordered by candidate id because
   swapping groups 0 and 1 leaves the three (0,1,2) layers unchanged.

The accumulated witness bank is persisted in
`data/derived/h183_h180_witness_bank.zlib.b64` so later runs do not restart.
Every stored witness is itself a valid necessary cut regardless of how it was
found.  Heuristic search is used only to FIND witnesses; a returned n3 score
is recomputed exactly.  If the heuristic cannot reach <=2, the exact MILP
separator is used.  Solver timeout is never treated as validation.
"""
from __future__ import annotations

import base64
import json
import random
import zlib
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, lil_matrix

ODDS = np.array([1, 3, 5, 7, 9, 11, 13, 15], dtype=int)
PARAMS = np.array([(a, a, c) for a in ODDS for c in range(16)], dtype=int)
SUPPORTS = [(0, 1, 2), (0, 3, 4), (1, 3, 4), (2, 3, 4)]
NP = len(PARAMS)
ROOT = Path(__file__).resolve().parents[2]
BANK = ROOT / "data" / "derived" / "h183_h180_witness_bank.zlib.b64"


def load_witness_bank(path: Path = BANK):
    raw = base64.b64decode(path.read_text().strip())
    return json.loads(zlib.decompress(raw).decode())


def layer_hits(witness, support):
    i, j, k = support
    xs = np.asarray(witness[i], dtype=int)
    ys = np.asarray(witness[j], dtype=int)
    target = np.zeros(16, dtype=np.int8)
    target[witness[k]] = 1
    values = (
        PARAMS[:, 0, None, None] * xs[None, :, None]
        + PARAMS[:, 1, None, None] * ys[None, None, :]
        + PARAMS[:, 2, None, None]
    ) % 16
    return target[values].sum(axis=(1, 2)).astype(float)


def witness_row(witness):
    return np.concatenate([layer_hits(witness, s) for s in SUPPORTS])


def solve_master(witnesses, time_limit=10.0):
    """Solve H180 master with exact H183 WLOG symmetry breaking."""
    n = 4 * NP
    rows = 4 + len(witnesses) + 2
    A = lil_matrix((rows, n))
    lb = np.full(rows, -np.inf)
    ub = np.full(rows, np.inf)

    for s in range(4):
        A[s, s * NP : (s + 1) * NP] = 1
        required = 3 if s == 0 else 1
        lb[s] = ub[s] = required

    for r, witness in enumerate(witnesses, start=4):
        A[r, :] = witness_row(witness)
        lb[r] = 3

    r = 4 + len(witnesses)
    # WLOG normalize the chosen (2,3,4) layer to c=0.
    disallowed = [pid for pid, p in enumerate(PARAMS) if int(p[2]) != 0]
    A[r, 3 * NP + np.asarray(disallowed)] = 1
    lb[r] = ub[r] = 0

    # WLOG swap groups 0/1 so candidate-id(B) <= candidate-id(C).
    ids = np.arange(NP, dtype=float)
    A[r + 1, NP : 2 * NP] = ids
    A[r + 1, 2 * NP : 3 * NP] = -ids
    ub[r + 1] = 0

    result = milp(
        np.zeros(n),
        integrality=np.ones(n, dtype=int),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=LinearConstraint(csr_matrix(A), lb, ub),
        options={"time_limit": time_limit, "presolve": True, "mip_rel_gap": 0},
    )
    if result.x is None:
        return None, result
    chosen = [
        np.flatnonzero(result.x[s * NP : (s + 1) * NP] > 0.5).tolist()
        for s in range(4)
    ]
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


def exact_score(triples, selected):
    return int(
        np.sum(
            selected[triples[:, 0]]
            & selected[triples[:, 1]]
            & selected[triples[:, 2]]
        )
    )


def build_incidence(triples):
    incidence = [[] for _ in range(80)]
    for q, triple in enumerate(triples):
        for v in triple:
            incidence[int(v)].append(q)
    return [np.asarray(v, dtype=np.int32) for v in incidence]


def local_adversary(triples, seed, restarts=40, max_steps=120):
    """Fast witness finder. Any <=2 result is exact after exact_score()."""
    rng = random.Random(seed)
    incidence = build_incidence(triples)
    best = 10**9
    best_selected = None

    for _ in range(restarts):
        selected = np.zeros(80, dtype=bool)
        for g in range(5):
            selected[rng.sample(range(g * 16, (g + 1) * 16), 4)] = True
        score = exact_score(triples, selected)
        if score < best:
            best, best_selected = score, selected.copy()
        if score <= 2:
            return score, best_selected

        for _ in range(max_steps):
            best_new = score
            moves = []
            for g in range(5):
                chosen = np.flatnonzero(selected[g * 16 : (g + 1) * 16]) + g * 16
                unchosen = np.flatnonzero(~selected[g * 16 : (g + 1) * 16]) + g * 16
                for old in chosen:
                    io = incidence[int(old)]
                    loss = int(
                        np.sum(
                            selected[triples[io, 0]]
                            & selected[triples[io, 1]]
                            & selected[triples[io, 2]]
                        )
                    )
                    selected[old] = False
                    for new in unchosen:
                        inn = incidence[int(new)]
                        tt = triples[inn]
                        gain = int(
                            np.sum(
                                (selected[tt[:, 0]] | (tt[:, 0] == new))
                                & (selected[tt[:, 1]] | (tt[:, 1] == new))
                                & (selected[tt[:, 2]] | (tt[:, 2] == new))
                            )
                        )
                        candidate = score - loss + gain
                        if candidate < best_new:
                            best_new = candidate
                            moves = [(int(old), int(new))]
                        elif candidate == best_new:
                            moves.append((int(old), int(new)))
                    selected[old] = True
            if not moves or best_new >= score:
                break
            old, new = rng.choice(moves)
            selected[old] = False
            selected[new] = True
            score = best_new
            if score < best:
                best, best_selected = score, selected.copy()
            if score <= 2:
                return exact_score(triples, selected), selected.copy()
    return best, best_selected


def exact_separator_le2(triples, time_limit=20.0):
    """Exact MILP search for a balanced witness with n3 <= 2."""
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
        options={"time_limit": time_limit, "presolve": True, "mip_rel_gap": 0},
    )
    if result.x is None:
        return None, result
    selected = result.x[:80] > 0.5
    witness = [
        [i for i in range(16) if selected[g * 16 + i]] for g in range(5)
    ]
    return (exact_score(triples, selected), witness), result


def printable_design(chosen):
    return [[PARAMS[i].tolist() for i in ids] for ids in chosen]


def main():
    witnesses = load_witness_bank()
    print("persisted_cuts", len(witnesses))
    chosen, master = solve_master(witnesses)
    print("master_status", master.status, master.message)
    if chosen is None:
        print("MASTER_INFEASIBLE_RESTRICTED_FAMILY")
        return

    print("chosen", printable_design(chosen))
    triples = build_triples(chosen)
    score, selected = local_adversary(triples, seed=183999)
    if score <= 2:
        witness = [[i for i in range(16) if selected[g * 16 + i]] for g in range(5)]
        print("explicit_counterexample", score, witness)
        return

    separated, exact = exact_separator_le2(triples)
    print("exact_separator_status", exact.status, exact.message)
    print("exact_result", separated)


if __name__ == "__main__":
    main()
