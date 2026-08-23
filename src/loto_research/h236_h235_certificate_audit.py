"""H236: independent compact audit of the large H235 merged certificate.

This stage does not rerun the expensive CSP. It parses the committed H235 merged
artifact, independently checks the complete 44-shard / 11-sector partition and
recomputes all decisive totals from the leaf chunk records. A small summary is
persisted so the large certificate can be inspected and used as a stable gate.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "data" / "derived" / "h235_h234_augmented_exact_shift_rescreen.json"
OUT = ROOT / "data" / "derived" / "h236_h235_certificate_audit_summary.json"

EXPECTED_REPS = ((1,1),(1,3),(1,5),(1,7),(1,9),(1,15),(3,5),(3,9),(3,13),(5,9),(7,9))
EXPECTED_STATES = (7806,23052,23052,23052,23052,23052,45760,23052,45760,23052,45760)
EXPECTED_TOTAL = 306450


def bounds(n: int, chunk: int) -> tuple[int, int]:
    return n * chunk // 4, n * (chunk + 1) // 4


def audit() -> dict:
    d = json.loads(SRC.read_text())
    assert d["packet"] == "H235"
    assert d["chunk_shards"] == 44
    sectors = d["sectors"]
    assert len(sectors) == 11

    leaf_states = leaf_env = leaf_exact_states = leaf_tuples = 0
    signatures = set()
    witness_meta = set()
    chunk_pairs = []
    sector_summary = []

    for si, sec in enumerate(sectors):
        assert sec["sector_index"] == si
        assert tuple(sec["representative"]) == EXPECTED_REPS[si]
        assert sec["quotient_coefficient_states"] == EXPECTED_STATES[si]
        chunks = sec["chunks"]
        assert len(chunks) == 4

        s_states = s_env = s_exact = s_tuples = 0
        for ci, ch in enumerate(chunks):
            assert ch["packet"] == "H235"
            assert ch["sector_index"] == si and ch["chunk_index"] == ci
            assert tuple(ch["representative"]) == EXPECTED_REPS[si]
            assert ch["sector_total_quotient_states"] == EXPECTED_STATES[si]
            lo, hi = bounds(EXPECTED_STATES[si], ci)
            assert (ch["chunk_start"], ch["chunk_stop"]) == (lo, hi)
            assert ch["chunk_quotient_states"] == hi - lo
            chunk_pairs.append((si, ci))
            s_states += ch["chunk_quotient_states"]
            s_env += ch["envelope_survivor_states"]
            s_exact += ch["exact_shift_surviving_coefficient_states"]
            s_tuples += ch["exact_surviving_shift_tuples"]
            signatures.add(ch["general_signature_unique_witnesses"])
            witness_meta.add((
                ch["base_expanded_witness_instances"], ch["h234_raw_witnesses"],
                ch["h234_affine_expanded_instances"],
                ch["augmented_witness_instances_before_signature_dedupe"],
                ch["h185_stored"], ch["h186_witnesses"],
            ))

        assert s_states == EXPECTED_STATES[si]
        assert s_env == sec["envelope_survivor_states"]
        assert s_exact == sec["exact_shift_surviving_coefficient_states"]
        assert s_tuples == sec["exact_surviving_shift_tuples"]
        leaf_states += s_states; leaf_env += s_env
        leaf_exact_states += s_exact; leaf_tuples += s_tuples
        sector_summary.append({
            "sector_index": si,
            "representative": list(EXPECTED_REPS[si]),
            "quotient_states": s_states,
            "envelope_survivors": s_env,
            "exact_coefficient_survivors": s_exact,
            "exact_shift_tuple_survivors": s_tuples,
        })

    assert chunk_pairs == [(s,c) for s in range(11) for c in range(4)]
    assert leaf_states == EXPECTED_TOTAL
    assert leaf_states == d["quotient_coefficient_states_screened"]
    assert leaf_env == d["envelope_survivor_states"]
    assert leaf_exact_states == d["exact_shift_surviving_coefficient_states"]
    assert leaf_tuples == d["exact_surviving_shift_tuples"]
    assert len(signatures) == 1 and len(witness_meta) == 1
    assert d["all_general_cyclic_affine_designs_rejected_by_augmented_witnesses"] == (leaf_exact_states == 0)

    meta = next(iter(witness_meta))
    summary = {
        "packet": "H236",
        "audit_target": "H235",
        "audit": "independent_leaf_reaggregation_and_schema_partition_check",
        "all_44_chunks_present_and_disjoint": True,
        "all_11_sector_totals_verified": True,
        "quotient_coefficient_states_verified": leaf_states,
        "envelope_survivor_states": leaf_env,
        "exact_shift_surviving_coefficient_states": leaf_exact_states,
        "exact_surviving_shift_tuples": leaf_tuples,
        "h225_general_cyclic_affine_family_closed": leaf_exact_states == 0,
        "general_signature_unique_witnesses": next(iter(signatures)),
        "base_expanded_witness_instances": meta[0],
        "h234_raw_witnesses": meta[1],
        "h234_affine_expanded_instances": meta[2],
        "augmented_witness_instances_before_signature_dedupe": meta[3],
        "pre_h186_bank_size": meta[4],
        "h186_witnesses": meta[5],
        "sectors": sector_summary,
        "interpretation": (
            "If exact_shift_surviving_coefficient_states is zero, the committed H235 leaf records form a complete finite impossibility certificate for the H225 general cyclic-affine family. Otherwise the remaining exact states are unresolved."
        ),
    }
    return summary


def main() -> None:
    out = audit()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    print("RESULT_FILE", OUT)


if __name__ == "__main__":
    main()
