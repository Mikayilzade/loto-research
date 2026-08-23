"""H212 exact affine-unit quotient for the H175/H188 restricted family.

H210 used the residual translation action
  (a,c) -> (a, c + (2a-1)t) mod 16.
H212 adds common multiplication of all five group coordinates by any odd unit
u in Z/16Z. This preserves B,C,D zero shifts, D=(1,0), all coefficients, and
maps A layers by
  (a,c) -> (a, u*c + (2a-1)t) mod 16.
The 8*16=128 maps form a group. We enumerate its exact orbits on all 3-element
A-layer subsets; this is solver-independent finite enumeration.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations

MOD = 16
ODDS = (1, 3, 5, 7, 9, 11, 13, 15)
LAYERS = tuple((a, c) for a in ODDS for c in range(MOD))
INDEX = {p: i for i, p in enumerate(LAYERS)}
GROUP = tuple((u, t) for u in ODDS for t in range(MOD))


def act_layer(p: tuple[int, int], g: tuple[int, int]) -> tuple[int, int]:
    a, c = p
    u, t = g
    return a, (u * c + (2 * a - 1) * t) % MOD


def permutations() -> tuple[tuple[int, ...], ...]:
    out = []
    for g in GROUP:
        perm = tuple(INDEX[act_layer(p, g)] for p in LAYERS)
        assert len(set(perm)) == len(LAYERS)
        out.append(perm)
    assert len(set(out)) == 128
    return tuple(out)


def enumerate_orbits():
    perms = permutations()
    seen: set[tuple[int, int, int]] = set()
    orbit_sizes: Counter[int] = Counter()
    reps: list[tuple[int, int, int]] = []
    exceptional = 0

    for s in combinations(range(len(LAYERS)), 3):
        if s in seen:
            continue
        orb = {tuple(sorted(p[i] for i in s)) for p in perms}
        seen.update(orb)
        rep = min(orb)
        reps.append(rep)
        orbit_sizes[len(orb)] += 1
        if all(LAYERS[i][0] == 15 for i in s):
            exceptional += 1

    assert len(seen) == 341_376
    assert len(reps) == 3_992
    assert orbit_sizes == Counter({128: 1920, 64: 1088, 32: 640, 16: 344})
    assert exceptional == 9
    return reps, orbit_sizes, exceptional


def main():
    reps, sizes, exceptional = enumerate_orbits()
    conservative_representatives = len(reps) * 36
    assert conservative_representatives == 143_712
    print('group_size', len(GROUP))
    print('raw_A_sets', 341_376)
    print('A_orbits', len(reps))
    print('orbit_sizes', dict(sorted(sizes.items())))
    print('exceptional_a15_A_orbits', exceptional)
    print('H212_conservative_representatives', conservative_representatives)
    print('H211_representatives', 767_361)
    print('reduction_vs_H211', 767_361 / conservative_representatives)


if __name__ == '__main__':
    main()
