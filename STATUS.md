# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H236 — RI Lucky 3 Spot doubled 3-spot full-space threshold + execution test**.
Still-running/pending exact family packet: **H235 — H234-augmented exact 44-way family rescreen**.

### H232 preserved authoritative result
- quotient coefficient states screened: **306,450**;
- coefficient states retaining at least one globally consistent legal shift tuple: **306,098**;
- exact surviving shift tuples against the old stored witness bank: **139,869,763**;
- expanded witness instances: **24,574**;
- general-signature unique witnesses: **15,572**.

H232 did **not** close H225; its witness bank was only a necessary screen.

### H234 authoritative result
`data/derived/h234_h232_first_survivor_separation.json` and `data/derived/h234_new_witnesses.json` exist.

Exact top-level result:
- selected actual H232 survivor designs: **44** (one from every sector×chunk partition);
- exact unrestricted balanced `n3<=2` counterexamples found: **44/44**;
- inconclusive jobs: **0**;
- unique balanced counterexamples: **44**;
- `all_selected_designs_broken = true`.

Conclusion: all 44 sampled actual H232 survivors are rigorously non-universal. This still does not alone close the remaining H232 survivor family.

### H235 packet
H235 feeds all 44 H234 exact counterexamples back into the H228/H232 exact family screen. Each witness is expanded through all affine symmetries `x -> u*x+v mod 16` with odd `u`, adding **5,632** balanced witness instances before full-signature deduplication. The H228 quotient universe and exact legal-shift CSP are unchanged, so the result is directly comparable to H232.

Files:
- `src/loto_research/h235_h234_augmented_exact_shift_rescreen.py`
- `.github/workflows/h235-h234-augmented-rescreen.yml`
- `research/CHECKED_PROJECTS_AND_TESTS_H235_APPEND.md`

Target authoritative output:
- `data/derived/h235_h234_augmented_exact_shift_rescreen.json`

Interpretation:
- `exact_shift_surviving_coefficient_states = 0` exactly closes the H225 general cyclic-affine family;
- positive survivors mean another unrestricted separator packet is required;
- missing/failed output is inconclusive.

As of the H236 checkpoint, the merged H235 output was still absent; this proves nothing and H235 remains pending.

### H236 — RI Lucky 3 Spot Keno promotion coverage theorem
Fresh official-source recheck confirmed that historical Rhode Island `Lucky 3 Spot Keno` promotions created a real printed pre-draw entitlement that doubled winning prizes on qualifying **3-spot** tickets. Qualifying Lucky tickets were explicitly non-cancellable; retailer preprinting was prohibited. General RI Keno rules ordinarily allow same-day same-terminal cancellation before the draw.

Exact full-space identity for one 20/80 3-spot draw:
- all 3-subsets: **82,160**;
- 0/3 matches: **34,220**;
- 1/3 matches: **35,400**;
- 2/3 matches: **11,400**;
- 3/3 matches: **1,140**.

If every $1 line had a true 2x entitlement, deterministic gross would be `2*(11,400*P2 + 1,140*P3)` and strict pre-tax profit requires:

`10*P2 + P3 > 36.03508771929825`.

This is a reusable exact promotion threshold, but **not an executable guarantee**: recovered historical rules do not establish a lawful/operational way to obtain the doubled entitlement for all 82,160 distinct combinations inside the finite promotion window/location, nor entitlement frequency/issuance control. Current 2026 RI homepage visibly advertises `Kick Back with Keno Promotion`, but exact current mechanics remain unrecovered, so historical mechanics may not be assumed.

Files:
- `research/h236_ri_lucky3_full_coverage_threshold.md`
- `src/loto_research/h236_ri_lucky3_full_coverage_threshold.py`
- `data/derived/h236_ri_lucky3_full_coverage_threshold.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H236_APPEND.md`

Result: historical Lucky 3 full-coverage execution path **rejected as strict guarantee on recovered evidence**; current Kick Back remains evidence-blocked pending materially new primary rules.

### Preserved restricted-family state
- H224/H223/H222/H219 exact restricted outputs have not produced an authoritative closure result at this checkpoint.
- H221 proves any schema-valid restricted exact screen with `survivor_count=0` over all 143,712 H212-normalized classes closes that restricted family without a second MILP.

### Preserved promotion/execution state
- Current RI `Kick Back with Keno Promotion` is officially visible, but exact mechanics remain unrecovered; do not infer historical Lucky 3 mechanics without primary evidence.
- Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist; H236 now adds the exact doubled full-space threshold but rejects executable all-entitlement coverage on recovered evidence.
- Current RI online/iLottery and ordinary retailer/SSVM remain closed as sole strict-guarantee execution channels under recovered public rules.

## NEXT ACTION
1. **Check H235 merged output first.** Missing output proves nothing.
2. If H235 has zero exact survivors, record exact closure of H225 general cyclic-affine family and move to the next still-open lottery-specific class.
3. If H235 has positive survivors, select actual survivors from affected sectors/chunks only and run another unrestricted exact `n3<=2` separator packet; feed only genuinely new witnesses into the next incremental rescreen.
4. Accept any late schema-valid restricted exact zero-survivor result separately under H221.
5. Reopen current `Kick Back with Keno` only on materially new primary evidence, especially rules revealing deterministic entitlement issuance, cancellation rights, or a promotion-wide multiplier.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H236_APPEND.md`.
