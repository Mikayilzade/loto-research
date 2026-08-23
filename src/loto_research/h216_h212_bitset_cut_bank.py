"""H216 fast exact H212 cut-bank screen using threshold bitsets.

Scientifically identical to H213: enumerate all 143,712 H212 representatives and
reject a design iff any stored exact H185+H186 cut has n3 < 3.

Optimization: for each exact cut row, precompute bitmasks of A-orbit reps with
A-contribution >=1, >=2, >=3. For each of 36 B/C pairs, the B+C+D contribution
sets the required A threshold, and the surviving A reps are obtained by integer
bitset intersections. This removes the ~700M Python scalar checks in H213.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

from loto_research.h187_support4_normalized_merged_master import merged_active_rows
from loto_research.h212_h175_affine_unit_orbits import enumerate_orbits

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h216_h212_bitset_survivors.json"


def mask_from_bool(v: np.ndarray) -> int:
    m = 0
    for i in np.flatnonzero(v):
        m |= 1 << int(i)
    return m


def enumerate_survivors():
    rows, h185_n, h186_n = merged_active_rows()
    R = np.asarray(rows, dtype=np.uint8)
    reps, orbit_sizes, exceptional = enumerate_orbits()
    reps_arr = np.asarray(reps, dtype=np.int16)
    bc_pairs = [(16 * i, 16 * j) for i in range(8) for j in range(i, 8)]

    assert R.shape == (4878, 512)
    assert len(reps) == 3992
    assert len(bc_pairs) == 36

    # A contribution per cut and A-orbit representative: 0..3.
    A = R[:, reps_arr[:, 0]] + R[:, reps_arr[:, 1]] + R[:, reps_arr[:, 2]]
    masks = {
        1: [mask_from_bool(A[r] >= 1) for r in range(len(R))],
        2: [mask_from_bool(A[r] >= 2) for r in range(len(R))],
        3: [mask_from_bool(A[r] >= 3) for r in range(len(R))],
    }
    all_mask = (1 << len(reps)) - 1

    survivors = []
    per_bc_counts = []
    for b, c in bc_pairs:
        # D is fixed id0. B/C are zero-shift ids 16*i,16*j.
        bc = R[:, 128 + b].astype(np.int16) + R[:, 256 + c].astype(np.int16) + R[:, 384].astype(np.int16)
        sm = all_mask
        for ridx, q in enumerate(bc):
            need = 3 - int(q)
            if need <= 0:
                continue
            if need > 3:
                sm = 0
                break
            sm &= masks[need][ridx]
            if sm == 0:
                break
        count = sm.bit_count()
        per_bc_counts.append([int(b), int(c), int(count)])
        while sm:
            lsb = sm & -sm
            i = lsb.bit_length() - 1
            a0, a1, a2 = reps[i]
            survivors.append({"A": [int(a0), int(a1), int(a2)], "B": int(b), "C": int(c), "D": 0})
            sm ^= lsb

    total = len(reps) * len(bc_pairs)
    result = {
        "packet": "H216",
        "screen": "H212 exact representatives against merged H185+H186 exact necessary cuts via threshold bitsets",
        "scientifically_equivalent_to": "H213",
        "h185_stored_witnesses": int(h185_n),
        "h186_explicit_witnesses": int(h186_n),
        "active_unique_exact_cut_rows": int(len(R)),
        "A_orbits": int(len(reps)),
        "BC_pairs": int(len(bc_pairs)),
        "total_H212_representatives": int(total),
        "rejected_by_cut_bank": int(total - len(survivors)),
        "survivor_count": int(len(survivors)),
        "per_BC_survivor_counts": per_bc_counts,
        "survivors": survivors,
        "interpretation": "survivor means unresolved only; zero survivors closes H212/H214 restricted family under the existing exact cut bank; nonzero survivors require exact n3<=2 separation",
    }
    return result


def main():
    result = enumerate_survivors()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("survivors", "per_BC_survivor_counts")}, indent=2))
    print("RESULT_FILE", OUT)


if __name__ == "__main__":
    main()
