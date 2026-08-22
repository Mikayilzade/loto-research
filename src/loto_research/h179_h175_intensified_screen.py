"""H179: intensified adversarial screen for H175's 4,336-play balanced gate.

Reuses the deterministic H178 design bank, but increases local-search effort and
adds exact MILP checks on heuristic-hard candidates.  Local scores >2 are never
accepted as validation; only explicit n3<=2 witnesses reject a design.
"""
from __future__ import annotations

import random
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix, csr_matrix

SUPPORTS = [(0, 1, 2)] * 3 + [(0, 3, 4), (1, 3, 4), (2, 3, 4)]


def generate_design(seed: int):
    rng = random.Random(seed)
    triples = []
    incidence = [[] for _ in range(80)]
    for support in SUPPORTS:
        base = "cyclic" if rng.random() < 0.5 else "xor"
        pr = rng.sample(range(16), 16)
        pc = rng.sample(range(16), 16)
        po = rng.sample(range(16), 16)
        i, j, k = support
        for a in range(16):
            for b in range(16):
                z = (pr[a] + pc[b]) % 16 if base == "cyclic" else (pr[a] ^ pc[b])
                triples.append((i * 16 + a, j * 16 + b, k * 16 + po[z]))
    triples = np.asarray(triples, dtype=np.int16)
    for ti, triple in enumerate(triples):
        for v in triple:
            incidence[int(v)].append(ti)
    return triples, incidence


def exact_score(triples, selected) -> int:
    return int(np.sum(selected[triples[:, 0]] & selected[triples[:, 1]] & selected[triples[:, 2]]))


def local_adversary(triples, incidence, seed: int, restarts: int = 40, max_steps: int = 60):
    rng = random.Random(seed)
    best = 10**9
    best_selected = None
    for _ in range(restarts):
        selected = np.zeros(80, dtype=bool)
        for g in range(5):
            for v in rng.sample(range(g * 16, (g + 1) * 16), 4):
                selected[v] = True
        score = exact_score(triples, selected)
        if score < best:
            best, best_selected = score, selected.copy()
        if score <= 2:
            return best, best_selected

        for _ in range(max_steps):
            best_move = None
            best_new_score = score
            for g in range(5):
                chosen = np.flatnonzero(selected[g * 16:(g + 1) * 16]) + g * 16
                unchosen = np.flatnonzero(~selected[g * 16:(g + 1) * 16]) + g * 16
                for old in chosen:
                    selected[old] = False
                    for new in unchosen:
                        selected[new] = True
                        candidate = exact_score(triples, selected)
                        selected[new] = False
                        if candidate < best_new_score:
                            best_new_score = candidate
                            best_move = (int(old), int(new))
                    selected[old] = True
            if best_move is None:
                break
            old, new = best_move
            selected[old] = False
            selected[new] = True
            score = best_new_score
            if score < best:
                best, best_selected = score, selected.copy()
            if score <= 2:
                return best, best_selected
    return best, best_selected


def exact_counterexample_le2(triples, time_limit: float = 6.0):
    m = len(triples)
    n = 80 + m
    aeq = lil_matrix((5, n))
    for g in range(5):
        aeq[g, g * 16:(g + 1) * 16] = 1

    atr = lil_matrix((m, n))
    for r, (a, b, c) in enumerate(triples):
        atr[r, int(a)] = 1
        atr[r, int(b)] = 1
        atr[r, int(c)] = 1
        atr[r, 80 + r] = -1

    ahit = lil_matrix((1, n))
    ahit[0, 80:] = 1
    constraints = [
        LinearConstraint(csr_matrix(aeq), np.full(5, 4), np.full(5, 4)),
        LinearConstraint(csr_matrix(atr), -np.inf * np.ones(m), np.full(m, 2)),
        LinearConstraint(csr_matrix(ahit), -np.inf, 2),
    ]
    result = milp(
        np.zeros(n),
        integrality=np.ones(n, dtype=int),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=constraints,
        options={"time_limit": time_limit, "presolve": True},
    )
    if result.x is None:
        return None, result.status, result.message
    selected = result.x[:80] > 0.5
    witness = [[i for i in range(16) if selected[g * 16 + i]] for g in range(5)]
    return (exact_score(triples, selected), witness), result.status, result.message


def main():
    histogram = {}
    hard = []
    for idx in range(100):
        seed = 178000 + idx
        triples, incidence = generate_design(seed)
        score, _ = local_adversary(triples, incidence, 200000 + idx)
        histogram[score] = histogram.get(score, 0) + 1
        if score > 2:
            hard.append((seed, score))
    print("H179 local histogram:", dict(sorted(histogram.items())))
    print("explicit local counterexamples:", sum(v for k, v in histogram.items() if k <= 2))
    print("heuristic-hard designs:", len(hard))

    for seed in (178033, 178042, 178008):
        triples, _ = generate_design(seed)
        witness, status, message = exact_counterexample_le2(triples)
        print(seed, witness, status, message)


if __name__ == "__main__":
    main()
