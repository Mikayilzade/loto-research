"""H219: exact vectorized replacement for the H217/H218 H175 cut-bank screen.

Scientific predicate is identical to H217: for each normalized H212 candidate and
all 4,878 stored exact balanced-witness rows, require total incidence >= 3.
The change is computational only: evaluate all 3,992 A representatives for one
B/C shard with NumPy broadcasting instead of constructing 14,634 Python big-int
bit masks per shard.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from loto_research.h187_support4_normalized_merged_master import merged_active_rows
from loto_research.h212_h175_affine_unit_orbits import enumerate_orbits

ROOT = Path(__file__).resolve().parents[2]
BC_PAIRS = [(16 * i, 16 * j) for i in range(8) for j in range(i, 8)]
SHARD_DIR = ROOT / "data" / "derived" / "h219_shards"
MERGED = ROOT / "data" / "derived" / "h219_vectorized_merged_survivors.json"


def screen_shard(idx: int) -> dict:
    rows, h185_n, h186_n = merged_active_rows()
    R = np.asarray(rows, dtype=np.uint8)
    reps, _, _ = enumerate_orbits()
    reps_arr = np.asarray(reps, dtype=np.int16)
    assert R.shape == (4878, 512)
    assert len(reps) == 3992
    assert len(BC_PAIRS) == 36

    # Exact A contribution for every witness row x every H212 A representative.
    A = (
        R[:, reps_arr[:, 0]]
        + R[:, reps_arr[:, 1]]
        + R[:, reps_arr[:, 2]]
    )

    b, c = BC_PAIRS[idx]
    bc = (
        R[:, 128 + b].astype(np.uint8)
        + R[:, 256 + c].astype(np.uint8)
        + R[:, 384].astype(np.uint8)
    )

    # Candidate survives iff every stored exact witness row has incidence >= 3.
    # uint8 is safe: maximum value is 6.
    survive = np.all(A + bc[:, None] >= 3, axis=0)
    ids = np.flatnonzero(survive)
    survivors = [[int(x) for x in reps[int(i)]] for i in ids]

    return {
        "packet": "H219",
        "method": "vectorized_exact_cut_bank",
        "shard": idx,
        "B": b,
        "C": c,
        "D": 0,
        "h185": h185_n,
        "h186": h186_n,
        "exact_cut_rows": len(R),
        "A_orbits": len(reps),
        "survivor_count": len(survivors),
        "A_survivors": survivors,
    }


def write_shard(idx: int) -> Path:
    out = screen_shard(idx)
    SHARD_DIR.mkdir(parents=True, exist_ok=True)
    p = SHARD_DIR / f"shard_{idx:02d}.json"
    p.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "A_survivors"}, indent=2))
    print("RESULT_FILE", p)
    return p


def merge() -> Path:
    shards = []
    for idx in range(36):
        p = SHARD_DIR / f"shard_{idx:02d}.json"
        if not p.exists():
            raise FileNotFoundError(f"missing exact shard {idx}: {p}")
        d = json.loads(p.read_text())
        assert d["packet"] == "H219"
        assert d["shard"] == idx
        assert d["exact_cut_rows"] == 4878
        assert d["A_orbits"] == 3992
        assert d["survivor_count"] == len(d["A_survivors"])
        shards.append(d)

    total = sum(d["survivor_count"] for d in shards)
    survivors = [
        {"shard": d["shard"], "B": d["B"], "C": d["C"], "A": a}
        for d in shards
        for a in d["A_survivors"]
    ]
    assert total == len(survivors)
    out = {
        "packet": "H219",
        "method": "vectorized_exact_cut_bank",
        "exact_cut_rows": 4878,
        "A_orbits_per_shard": 3992,
        "bc_shards": 36,
        "normalized_classes_screened": 36 * 3992,
        "survivor_count": total,
        "survivors": survivors,
    }
    MERGED.parent.mkdir(parents=True, exist_ok=True)
    MERGED.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "survivors"}, indent=2))
    print("RESULT_FILE", MERGED)
    return MERGED


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("shard")
    sp.add_argument("idx", type=int, choices=range(36))
    sub.add_parser("merge")
    args = ap.parse_args()
    if args.cmd == "shard":
        write_shard(args.idx)
    else:
        merge()


if __name__ == "__main__":
    main()
