"""H178: deterministic adversarial screen for the H175 4,336-play gate.

The six transversal-layer support allocation is fixed to
3x(0,1,2) + (0,3,4) + (1,3,4) + (2,3,4).
Each 16x16 Latin layer is a independently relabelled (isotopic) cyclic or
XOR group table.  A balanced adversary selects exactly four symbols from each
of five groups.  A candidate fails H175 whenever <=2 complete transversal
triples are contained in such a selection.

Dependencies: numpy, scipy (milp/HiGHS).
"""
from __future__ import annotations

import random
from dataclasses import dataclass
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix, csr_matrix

SUPPORTS = [(0, 1, 2)] * 3 + [(0, 3, 4), (1, 3, 4), (2, 3, 4)]


def generate_design(seed: int):
    rng = random.Random(seed)
    triples = []
    specs = []
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
        specs.append((support, base, pr, pc, po))
    triples = np.asarray(triples, dtype=np.int16)
    incidence = [[] for _ in range(80)]
    for ti, triple in enumerate(triples):
        for v in triple:
            incidence[int(v)].append(ti)
    return triples, incidence, specs


def exact_score(triples, selected) -> int:
    return sum(1 for a, b, c in triples if selected[a] and selected[b] and selected[c])


def local_adversary(triples, incidence, seed: int, restarts: int = 15, max_steps: int = 60):
    """Greedy balanced 4-per-group descent. Returns best n3 and witness."""
    rng = random.Random(seed)
    best = 10**9
    best_selected = None
    for _ in range(restarts):
        selected = [False] * 80
        for g in range(5):
            for v in rng.sample(range(g * 16, (g + 1) * 16), 4):
                selected[v] = True
        score = exact_score(triples, selected)
        if score < best:
            best, best_selected = score, selected.copy()
        if score <= 2:
            return score, selected

        for _ in range(max_steps):
            best_move = None
            best_new_score = score
            for g in range(5):
                chosen = [v for v in range(g * 16, (g + 1) * 16) if selected[v]]
                unchosen = [v for v in range(g * 16, (g + 1) * 16) if not selected[v]]
                for old in chosen:
                    removed = sum(
                        1 for ti in incidence[old]
                        if all(selected[int(v)] for v in triples[ti])
                    )
                    selected[old] = False
                    for new in unchosen:
                        added = 0
                        for ti in incidence[new]:
                            ok = True
                            for v in triples[ti]:
                                vv = int(v)
                                if vv != new and not selected[vv]:
                                    ok = False
                                    break
                            if ok:
                                added += 1
                        candidate_score = score - removed + added
                        if candidate_score < best_new_score:
                            best_new_score = candidate_score
                            best_move = (old, new)
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
                return score, selected.copy()
    return best, best_selected


def exact_counterexample_le2(triples, time_limit: float = 10.0):
    """MILP feasibility: balanced selection with n3 <= 2.

    y_t is forced to 1 whenever all three vertices of triple t are selected:
    x_a+x_b+x_c-y_t <= 2.  Since sum(y)<=2, any feasible solution is a
    rigorous H175 counterexample.  Infeasibility is only accepted when HiGHS
    returns an optimal/infeasible terminal status, not on a time limit.
    """
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
    n3 = exact_score(triples, selected)
    witness = [
        [i for i in range(16) if selected[g * 16 + i]]
        for g in range(5)
    ]
    return (n3, witness), result.status, result.message


def main():
    histogram = {}
    local_counterexamples = 0
    for idx in range(100):
        triples, incidence, _ = generate_design(178000 + idx)
        score, _ = local_adversary(triples, incidence, 991000 + idx)
        histogram[score] = histogram.get(score, 0) + 1
        local_counterexamples += score <= 2
    print("100-design local histogram:", dict(sorted(histogram.items())))
    print("local n3<=2 counterexamples:", local_counterexamples)

    # Exact follow-ups used in H178.  Seeds 178001, 178004 and 178059 all
    # return certified feasible balanced witnesses with n3=2 in the recorded run.
    for seed in (178001, 178004, 178059):
        triples, _, _ = generate_design(seed)
        witness, status, message = exact_counterexample_le2(triples)
        print(seed, witness, status, message)


if __name__ == "__main__":
    main()
