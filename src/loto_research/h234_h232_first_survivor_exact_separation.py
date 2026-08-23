"""H234: unrestricted exact separator for one actual H232 survivor per chunk.

H232 proved that the stored balanced-witness bank is far from closing the H225
cyclic-affine family: 306,098 quotient coefficient states still admit at least one
globally consistent legal shift tuple.  H234 therefore follows the prescribed
next action and asks the unrestricted exact H180 separator for a fresh balanced
4+4+4+4+4 draw with n3 <= 2 against actual shift-level H232 survivors.

One deterministic design is selected from each of H232's 44 disjoint chunks: the
first stored coefficient survivor and its first stored legal shift tuple.  Each
job is independent.  A returned witness is an exact counterexample for that
specific design and is also a valid new universal cut for later family screens.
A timeout/no incumbent is explicitly inconclusive and never validation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from loto_research.h180_h175_master_cutting_plane import exact_separator
from loto_research.h226_general_coefficient_envelope_prescreen import COEFFS

ROOT = Path(__file__).resolve().parents[2]
H232 = ROOT / "data" / "derived" / "h232_exact_shift_csp_merged.json"
OUTDIR = ROOT / "data" / "derived" / "h234_separator_shards"
MERGED = ROOT / "data" / "derived" / "h234_h232_first_survivor_separation.json"
NEW_WITNESSES = ROOT / "data" / "derived" / "h234_new_witnesses.json"
EXPECTED_STATES = 306_450
EXPECTED_SURVIVORS = 306_098
EXPECTED_SHIFT_TUPLES = 139_869_763
JOBS = 44


def load_h232() -> dict:
    d = json.loads(H232.read_text())
    assert d["packet"] == "H232"
    assert d["chunk_shards"] == 44
    assert d["sector_shards"] == 11
    assert d["quotient_coefficient_states_screened"] == EXPECTED_STATES
    assert d["exact_shift_surviving_coefficient_states"] == EXPECTED_SURVIVORS
    assert d["exact_surviving_shift_tuples"] == EXPECTED_SHIFT_TUPLES
    assert d["all_general_cyclic_affine_designs_rejected_by_stored_witnesses"] is False
    return d


def build_triples(beta: int, gamma: int, coefficients: tuple[int, int, int], shifts: tuple[int, int, int]) -> np.ndarray:
    """Build the exact normalized H225 6-layer design as 1,536 triples."""
    assert len(coefficients) == len(shifts) == 3
    a_layers = []
    for p, c in zip(coefficients, shifts):
        a, b = COEFFS[p]
        a_layers.append((int(a), int(b), int(c)))
    assert len(set(a_layers)) == 3, a_layers

    # support, affine layers (z = a*x + b*y + c mod 16)
    blocks = (
        ((0, 1, 2), tuple(a_layers)),
        ((0, 3, 4), ((1, int(beta), 0),)),
        ((1, 3, 4), ((1, int(gamma), 0),)),
        ((2, 3, 4), ((1, 1, 0),)),
    )
    triples = []
    for (i, j, k), layers in blocks:
        for a, b, c in layers:
            for x in range(16):
                for y in range(16):
                    z = (a * x + b * y + c) % 16
                    triples.append((i * 16 + x, j * 16 + y, k * 16 + z))
    out = np.asarray(triples, dtype=np.int16)
    assert out.shape == (1536, 3), out.shape
    return out


def balanced(witness) -> bool:
    return (
        isinstance(witness, list)
        and len(witness) == 5
        and all(
            isinstance(g, list)
            and len(g) == 4
            and len(set(map(int, g))) == 4
            and all(0 <= int(x) < 16 for x in g)
            for g in witness
        )
    )


def solve_job(job: int, time_limit: float) -> dict:
    assert 0 <= job < JOBS
    sector_index, chunk_index = divmod(job, 4)
    d = load_h232()
    sector = d["sectors"][sector_index]
    chunk = sector["chunks"][chunk_index]
    assert chunk["sector_index"] == sector_index
    assert chunk["chunk_index"] == chunk_index
    assert chunk["exact_shift_surviving_coefficient_states"] > 0
    survivors = chunk["first_exact_survivors"]
    assert survivors, (sector_index, chunk_index)
    chosen = survivors[0]
    coefficients = tuple(map(int, chosen["coefficients"]))
    shift_examples = chosen["first_shift_examples"]
    assert shift_examples, (sector_index, chunk_index, coefficients)
    shifts = tuple(map(int, shift_examples[0]))
    beta, gamma = map(int, sector["representative"])

    triples = build_triples(beta, gamma, coefficients, shifts)
    separated, result = exact_separator(triples, time_limit=time_limit)
    out = {
        "packet": "H234",
        "job": job,
        "sector_index": sector_index,
        "chunk_index": chunk_index,
        "representative": [beta, gamma],
        "coefficients": list(coefficients),
        "coefficient_pairs": [list(map(int, COEFFS[p])) for p in coefficients],
        "shifts": list(shifts),
        "triples": int(len(triples)),
        "separator_status": int(result.status),
        "separator_message": str(result.message),
        "counterexample_found": separated is not None,
        "conclusive_for_selected_design": separated is not None,
    }
    if separated is not None:
        score, witness = separated
        assert score <= 2
        assert balanced(witness)
        out["n3"] = int(score)
        out["witness"] = [[int(x) for x in g] for g in witness]
    else:
        out["n3"] = None
        out["witness"] = None
        out["interpretation"] = "No feasible incumbent returned within this job: inconclusive, not validation."
    return out


def witness_key(w) -> tuple:
    return tuple(tuple(sorted(map(int, g))) for g in w)


def merge(paths: list[Path]) -> tuple[dict, dict]:
    rows = []
    for p in paths:
        d = json.loads(p.read_text())
        assert d["packet"] == "H234"
        rows.append(d)
    rows.sort(key=lambda x: x["job"])
    assert len(rows) == JOBS, len(rows)
    assert [x["job"] for x in rows] == list(range(JOBS))
    assert [(x["sector_index"], x["chunk_index"]) for x in rows] == [divmod(i, 4) for i in range(JOBS)]

    found = [x for x in rows if x["counterexample_found"]]
    unique = {}
    for row in found:
        w = row["witness"]
        assert row["n3"] <= 2 and balanced(w)
        unique.setdefault(witness_key(w), w)

    merged = {
        "packet": "H234",
        "method": "44_actual_H232_shift_designs_unrestricted_exact_n3_le_2_separation",
        "source_packet": "H232",
        "selected_actual_designs": JOBS,
        "counterexamples_found": len(found),
        "inconclusive_jobs": JOBS - len(found),
        "unique_balanced_counterexamples": len(unique),
        "all_selected_designs_broken": len(found) == JOBS,
        "source_h232_quotient_states": EXPECTED_STATES,
        "source_h232_exact_surviving_coefficient_states": EXPECTED_SURVIVORS,
        "source_h232_exact_surviving_shift_tuples": EXPECTED_SHIFT_TUPLES,
        "jobs": rows,
        "interpretation": (
            "Each returned balanced witness exactly breaks its selected H232 shift-level design and is a valid new cut. "
            "Even if all 44 selected designs are broken, this alone does not close the 306,098 surviving coefficient states; "
            "the new witnesses must be fed back into a family-wide exact screen. Missing witnesses are inconclusive only."
        ),
    }
    witness_packet = {
        "packet": "H234",
        "source": "H232 first exact survivor from each of 44 sector×chunk jobs",
        "witness_count": len(unique),
        "witnesses": list(unique.values()),
        "validity": "Every stored witness is balanced 4+4+4+4+4 and was returned by the unrestricted exact n3<=2 MILP separator.",
    }
    return merged, witness_packet


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", type=int)
    ap.add_argument("--time-limit", type=float, default=240.0)
    ap.add_argument("--merge-dir", type=Path)
    args = ap.parse_args()

    if args.job is not None:
        out = solve_job(args.job, args.time_limit)
        OUTDIR.mkdir(parents=True, exist_ok=True)
        p = OUTDIR / f"job_{args.job:02d}.json"
        p.write_text(json.dumps(out, indent=2) + "\n")
        print(json.dumps({k: v for k, v in out.items() if k != "witness"}, indent=2))
        print("RESULT_FILE", p)
        return

    assert args.merge_dir is not None
    merged, witnesses = merge(sorted(args.merge_dir.rglob("job_*.json")))
    MERGED.parent.mkdir(parents=True, exist_ok=True)
    MERGED.write_text(json.dumps(merged, indent=2) + "\n")
    NEW_WITNESSES.write_text(json.dumps(witnesses, indent=2) + "\n")
    print(json.dumps({k: v for k, v in merged.items() if k != "jobs"}, indent=2))
    print("RESULT_FILE", MERGED)
    print("WITNESS_FILE", NEW_WITNESSES)


if __name__ == "__main__":
    main()
