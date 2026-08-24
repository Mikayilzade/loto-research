"""H225-X5: unrestricted exact separators for actual H225-X4 survivors.

Run only when H225-X4 leaves positive exact survivors.  One actual shift-level
survivor is selected from each still-positive X4 chunk.  Zero-survivor chunks
are explicit skips.  Returned balanced n3<=2 witnesses are deduplicated against
all earlier H225 cut generations (H234, H225-X1, H225-X3).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from loto_research.h180_h175_master_cutting_plane import exact_separator
from loto_research.h226_general_coefficient_envelope_prescreen import COEFFS
from loto_research.h234_h232_first_survivor_exact_separation import (
    balanced,
    build_triples,
    witness_key,
)

ROOT = Path(__file__).resolve().parents[2]
X4 = ROOT / "data" / "derived" / "h225_x4_incremental_exact_rescreen.json"
H234 = ROOT / "data" / "derived" / "h234_new_witnesses.json"
X1 = ROOT / "data" / "derived" / "h240_new_witnesses.json"
X3 = ROOT / "data" / "derived" / "h225_x3_new_witnesses.json"
OUTDIR = ROOT / "data" / "derived" / "h225_x5_separator_shards"
MERGED = ROOT / "data" / "derived" / "h225_x5_survivor_separation.json"
NEW = ROOT / "data" / "derived" / "h225_x5_new_witnesses.json"
JOBS = 44


def load_x4():
    d = json.loads(X4.read_text())
    assert d["packet"] == "H225-X4"
    assert d["chunk_shards"] == 44
    assert d["quotient_coefficient_states_screened"] == 306450
    assert len(d["sectors"]) == 11
    assert sum(int(s["quotient_coefficient_states"]) for s in d["sectors"]) == 306450
    return d


def solve_job(job: int, time_limit: float):
    assert 0 <= job < JOBS
    si, ci = divmod(job, 4)
    d = load_x4()
    sec = d["sectors"][si]
    ch = sec["chunks"][ci]
    assert (int(ch["sector_index"]), int(ch["chunk_index"])) == (si, ci)

    survivor_states = int(ch["exact_shift_surviving_coefficient_states"])
    survivor_shift_tuples = int(ch["exact_surviving_shift_tuples"])
    if survivor_states == 0:
        assert survivor_shift_tuples == 0
        return {
            "packet": "H225-X5",
            "job": job,
            "sector_index": si,
            "chunk_index": ci,
            "skipped_no_survivor": True,
            "x4_chunk_survivor_states": 0,
            "x4_chunk_survivor_shift_tuples": 0,
            "counterexample_found": False,
            "conclusive_for_selected_design": True,
            "n3": None,
            "witness": None,
        }

    survivors = ch["first_exact_survivors"]
    assert survivors, (si, ci, survivor_states)
    chosen = survivors[0]
    coefficients = tuple(map(int, chosen["coefficients"]))
    shifts = tuple(map(int, chosen["first_shift_examples"][0]))
    beta, gamma = map(int, sec["representative"])
    triples = build_triples(beta, gamma, coefficients, shifts)
    separated, res = exact_separator(triples, time_limit=time_limit)

    out = {
        "packet": "H225-X5",
        "job": job,
        "sector_index": si,
        "chunk_index": ci,
        "skipped_no_survivor": False,
        "x4_chunk_survivor_states": survivor_states,
        "x4_chunk_survivor_shift_tuples": survivor_shift_tuples,
        "representative": [beta, gamma],
        "coefficients": list(coefficients),
        "coefficient_pairs": [list(map(int, COEFFS[p])) for p in coefficients],
        "shifts": list(shifts),
        "triples": int(len(triples)),
        "separator_status": int(res.status),
        "separator_message": str(res.message),
        "counterexample_found": separated is not None,
        "conclusive_for_selected_design": separated is not None,
    }
    if separated is None:
        out.update(
            n3=None,
            witness=None,
            interpretation="No feasible incumbent returned within budget: inconclusive, not validation.",
        )
    else:
        score, witness = separated
        assert score <= 2 and balanced(witness)
        out.update(
            n3=int(score),
            witness=[[int(x) for x in group] for group in witness],
        )
    return out


def load_old_witnesses():
    old = []
    for path, packet in ((H234, "H234"), (X1, "H240"), (X3, "H225-X3")):
        d = json.loads(path.read_text())
        assert d["packet"] == packet
        assert len(d["witnesses"]) == int(d["witness_count"])
        old.extend(d["witnesses"])
    return old


def merge(paths):
    rows = sorted(
        [json.loads(p.read_text()) for p in paths],
        key=lambda x: int(x["job"]),
    )
    assert len(rows) == JOBS
    assert [int(x["job"]) for x in rows] == list(range(JOBS))

    active = [r for r in rows if not r["skipped_no_survivor"]]
    found = [r for r in active if r["counterexample_found"]]

    unique = {}
    for r in found:
        assert int(r["n3"]) <= 2 and balanced(r["witness"])
        unique.setdefault(witness_key(r["witness"]), r["witness"])

    oldkeys = {witness_key(w) for w in load_old_witnesses()}
    new = {k: w for k, w in unique.items() if k not in oldkeys}
    x4 = load_x4()

    merged = {
        "packet": "H225-X5",
        "source_packet": "H225-X4",
        "source_file": str(X4.relative_to(ROOT)),
        "x4_survivor_states": int(x4["exact_shift_surviving_coefficient_states"]),
        "x4_survivor_shift_tuples": int(x4["exact_surviving_shift_tuples"]),
        "total_chunks": JOBS,
        "active_survivor_chunks": len(active),
        "skipped_zero_survivor_chunks": JOBS - len(active),
        "counterexamples_found": len(found),
        "inconclusive_active_jobs": len(active) - len(found),
        "unique_balanced_counterexamples": len(unique),
        "genuinely_new_witnesses": len(new),
        "all_selected_active_designs_broken": len(found) == len(active),
        "jobs": rows,
    }
    witness_packet = {
        "packet": "H225-X5",
        "witness_count": len(new),
        "witnesses": list(new.values()),
        "deduplicated_against": ["H234", "H225-X1", "H225-X3"],
        "validity": "Every stored witness is balanced and returned by unrestricted exact n3<=2 MILP separation.",
    }
    return merged, witness_packet


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", type=int)
    ap.add_argument("--time-limit", type=float, default=180.0)
    ap.add_argument("--merge-dir", type=Path)
    args = ap.parse_args()

    if args.job is not None:
        out = solve_job(args.job, args.time_limit)
        OUTDIR.mkdir(parents=True, exist_ok=True)
        path = OUTDIR / f"job_{args.job:02d}.json"
        path.write_text(json.dumps(out, indent=2) + "\n")
        print(json.dumps({k: v for k, v in out.items() if k != "witness"}, indent=2))
        return

    assert args.merge_dir is not None
    merged, witness_packet = merge(sorted(args.merge_dir.rglob("job_*.json")))
    MERGED.write_text(json.dumps(merged, indent=2) + "\n")
    NEW.write_text(json.dumps(witness_packet, indent=2) + "\n")
    print(json.dumps({k: v for k, v in merged.items() if k != "jobs"}, indent=2))


if __name__ == "__main__":
    main()
