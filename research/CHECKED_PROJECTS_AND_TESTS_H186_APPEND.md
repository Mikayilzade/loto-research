# H186 audit append — H185 mass counterexample packet

Updated: 2026-08-22
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H186 H175/H185 4,336-play balanced transversal gate** | attack H185 current master `[[18,54,111],[12],[88],[16]]` with 500 seeded balanced local-search restarts; exact rescore every accepted witness | **141 distinct explicit counterexamples**: `n3=0` ×9, `n3=1` ×32, `n3=2` ×100 | **H185 candidate REJECTED; family OPEN**; `research/h186_h185_mass_counterexample_packet.md` |
| **H186 affine-orbit expansion A** | apply safe common-affine `x -> u*x+v`, odd `u`, 16 shifts to the 141 exact witnesses | **14,872 unique valid cut rows** within H186 Packet A | **VALID exact acceleration** |
| **H186 next restricted master** | solve Packet-A rows under H183 WLOG constraints | feasible candidate `[[17,26,95],[80],[104],[16]]` found | **NOT VALIDATED; attacked immediately** |
| **H186 second exact attack** | 300 seeded balanced local-search restarts against next candidate | **48 distinct explicit counterexamples**: `n3=0` ×5, `n3=1` ×7, `n3=2` ×36 | **SECOND CANDIDATE REJECTED** |
| **H186 affine-orbit union** | deduplicate affine rows from all 189 H186 witnesses | **18,952 unique valid H186 rows** | **VALID** |
| **H186 follow-up master** | solve all 18,952 H186-only rows | time limit reached with no incumbent | **INCONCLUSIVE; timeout is not infeasibility** |

Conclusion: no universal `n3>=3` construction and no restricted-family impossibility proof yet. Merge H186 witnesses into the H185 persistent bank and continue exact separation; do not repeat the two rejected candidates.