# CHECKED_PROJECTS_AND_TESTS — H234 append

Date: 2026-08-24
Scope: lottery-only continuation; Rhode Island Keno H175 / H225 general cyclic-affine family.

## H232 authoritative result consumed
- Exact 44-way H232 merge exists and passed its own strict merge assertions.
- H228 quotient coefficient states screened: **306,450**.
- Envelope survivors: **306,450**.
- Exact coefficient states retaining at least one legal shift tuple against the stored witness bank: **306,098**.
- Exact surviving shift tuples: **139,869,763**.
- `all_general_cyclic_affine_designs_rejected_by_stored_witnesses = false`.
- Conclusion: **H225 family NOT CLOSED by H232**. The stored witness bank is insufficient; positive H232 survivors are not validated constructions and require unrestricted separation.

## H234 — one actual survivor per H232 chunk, unrestricted exact separation
**Hypothesis / test:** actual shift-level designs that survive the stored H232 witness bank can still be broken by a balanced 4+4+4+4+4 draw with `n3 <= 2` when the original unrestricted draw space is searched exactly.

**Selection:** deterministic first stored exact survivor + first legal shift tuple from each of 44 H232 sector×chunk partitions.

**Method:** reconstruct each normalized six-layer H225 design (1,536 triples) and run the exact H180 MILP separator with five exact group-size constraints and `sum(completed triples) <= 2`.

**Safety of inference:**
- feasible separator incumbent => exact balanced counterexample for that selected design and a valid new universal cut;
- timeout/no incumbent => inconclusive only;
- breaking all 44 sampled actual survivors would still not close all 306,098 H232 survivor states without a subsequent family-wide rescreen.

**Implementation:**
- `src/loto_research/h234_h232_first_survivor_exact_separation.py`
- `.github/workflows/h234-h232-survivor-separation.yml`
- `research/h234_h232_first_survivor_exact_separation.md`

**Target outputs:**
- `data/derived/h234_h232_first_survivor_separation.json`
- `data/derived/h234_new_witnesses.json`

**Status:** RUNNING/PENDING at packet creation. No SUCCESS and no H225 closure claimed.
