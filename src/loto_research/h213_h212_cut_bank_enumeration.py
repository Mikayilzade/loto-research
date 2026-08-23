"""H213 exact enumeration of all H212 restricted representatives against the
accumulated H185+H186 exact balanced witness/cut bank.

This is a finite, solver-independent screen.  A design survives iff every
stored necessary cut has n3 >= 3.  Survivors are NOT validated universal
designs; they only remain unresolved and must be sent to exact separation.
"""
from __future__ import annotations

import json
from pathlib import Path

from loto_research.h187_support4_normalized_merged_master import merged_active_rows
from loto_research.h212_h175_affine_unit_orbits import enumerate_orbits

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h213_h212_cut_bank_survivors.json"


def enumerate_survivors():
    rows, h185_n, h186_n = merged_active_rows()
    reps, orbit_sizes, exceptional = enumerate_orbits()
    bc_pairs = [(16 * i, 16 * j) for i in range(8) for j in range(i, 8)]
    assert len(reps) == 3992
    assert len(bc_pairs) == 36
    assert len(rows) == 4878

    survivors = []
    total = 0
    rejected = 0
    reject_cut_hist = [0] * len(rows)

    for a_rep in reps:
        a0, a1, a2 = a_rep
        for b, c in bc_pairs:
            total += 1
            first_bad = None
            for ridx, r in enumerate(rows):
                n3 = int(r[a0]) + int(r[a1]) + int(r[a2])
                n3 += int(r[128 + b]) + int(r[256 + c]) + int(r[384])
                if n3 < 3:
                    first_bad = ridx
                    break
            if first_bad is None:
                survivors.append({"A": [a0, a1, a2], "B": b, "C": c, "D": 0})
            else:
                rejected += 1
                reject_cut_hist[first_bad] += 1

    assert total == 143712
    assert rejected + len(survivors) == total
    result = {
        "packet": "H213",
        "screen": "H212 exact representatives against merged H185+H186 exact necessary cuts",
        "h185_stored_witnesses": h185_n,
        "h186_explicit_witnesses": h186_n,
        "active_unique_exact_cut_rows": len(rows),
        "A_orbits": len(reps),
        "BC_pairs": len(bc_pairs),
        "total_H212_representatives": total,
        "rejected_by_cut_bank": rejected,
        "survivor_count": len(survivors),
        "survivors": survivors,
        "first_reject_cut_hist_nonzero": [[i, n] for i, n in enumerate(reject_cut_hist) if n],
        "interpretation": "survivor means unresolved only; universal n3>=3 still requires exact separation/infeasibility proof",
    }
    return result


def main():
    result = enumerate_survivors()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("survivors", "first_reject_cut_hist_nonzero")}, indent=2))
    print("RESULT_FILE", OUT)


if __name__ == "__main__":
    main()
