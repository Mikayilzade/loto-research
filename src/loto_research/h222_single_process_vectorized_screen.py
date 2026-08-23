"""H222: single-process exact replacement for H219's 36 repeated shard setup.

Scientific predicate is unchanged: every H212-normalized restricted H175 class
must have incidence >=3 on every one of the 4,878 stored exact balanced witnesses.

H219 recomputes the expensive H212 A-orbit enumeration independently in each of
36 jobs. H222 computes rows, A-orbits and the 4878 x 3992 A-incidence matrix once,
then evaluates all 36 normalized B/C pairs in one process.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

from loto_research.h187_support4_normalized_merged_master import merged_active_rows
from loto_research.h212_h175_affine_unit_orbits import enumerate_orbits

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h222_single_process_survivors.json"
BC_PAIRS = [(16 * i, 16 * j) for i in range(8) for j in range(i, 8)]


def run() -> dict:
    rows, h185_n, h186_n = merged_active_rows()
    R = np.asarray(rows, dtype=np.uint8)
    assert R.shape == (4878, 512)

    reps, orbit_sizes, exceptional = enumerate_orbits()
    assert len(reps) == 3992
    assert len(BC_PAIRS) == 36
    reps_arr = np.asarray(reps, dtype=np.int16)

    # Exact A contribution for every witness x normalized A representative.
    A = (
        R[:, reps_arr[:, 0]]
        + R[:, reps_arr[:, 1]]
        + R[:, reps_arr[:, 2]]
    )

    survivors = []
    shard_counts = []
    for shard, (b, c) in enumerate(BC_PAIRS):
        bc = (
            R[:, 128 + b].astype(np.uint8)
            + R[:, 256 + c].astype(np.uint8)
            + R[:, 384].astype(np.uint8)
        )
        keep = np.all(A + bc[:, None] >= 3, axis=0)
        ids = np.flatnonzero(keep)
        shard_counts.append(int(len(ids)))
        for idx in ids:
            survivors.append({
                "shard": shard,
                "B": int(b),
                "C": int(c),
                "A": [int(x) for x in reps[int(idx)]],
            })

    out = {
        "packet": "H222",
        "method": "single_process_vectorized_exact_cut_bank",
        "h185_stored": int(h185_n),
        "h186_witnesses": int(h186_n),
        "exact_cut_rows": int(len(R)),
        "A_orbits": int(len(reps)),
        "bc_classes": int(len(BC_PAIRS)),
        "normalized_classes_screened": int(len(reps) * len(BC_PAIRS)),
        "orbit_sizes": {str(k): int(v) for k, v in sorted(orbit_sizes.items())},
        "exceptional_a15_A_orbits": int(exceptional),
        "shard_survivor_counts": shard_counts,
        "survivor_count": int(len(survivors)),
        "survivors": survivors,
    }
    assert out["normalized_classes_screened"] == 143712
    assert out["survivor_count"] == sum(shard_counts)
    return out


def main() -> None:
    out = run()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "survivors"}, indent=2))
    print("RESULT_FILE", OUT)


if __name__ == "__main__":
    main()
