# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed numbered lottery packet: **H236 — RI Lucky 3 Spot doubled 3-spot full-space threshold + execution test**.
Latest completed exact family packet: **H235 — H234-augmented exact 44-way family rescreen**.
Current exact family continuation: **H237 — 44-way unrestricted exact separation of actual H235 survivors** (launched/pending merge).

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

### H235 authoritative result
H235 feeds all 44 H234 exact counterexamples back into the H228/H232 exact family screen. Each witness is expanded through all affine symmetries `x -> u*x+v mod 16` with odd `u`, adding **5,632** balanced witness instances before full-signature deduplication. The H228 quotient universe and exact legal-shift CSP are unchanged, so H235 is directly comparable to H232.

Authoritative merged output:
- `data/derived/h235_h234_augmented_exact_shift_rescreen.json`

Independent auxiliary audit (`packet = H235-AUDIT`, not a numbered research packet) verified all 44 disjoint chunks, all 11 sector totals, and reaggregated the decisive totals from leaf records:
- quotient coefficient states: **306,450 / 306,450**;
- augmented witness instances before signature dedupe: **30,206**;
- general-signature unique witnesses: **19,656**;
- envelope survivor states: **306,450**;
- exact shift-surviving coefficient states: **303,802**;
- exact surviving legal shift tuples: **90,425,060**;
- `h225_general_cyclic_affine_family_closed = false`.

Thus H235 strengthens H232 but does **not** close H225:
- coefficient survivors: `306,098 -> 303,802`;
- shift tuples: `139,869,763 -> 90,425,060`.

Auxiliary audit files:
- `src/loto_research/h236_h235_certificate_audit.py` (legacy filename only; output packet is `H235-AUDIT` so it does not claim H236 numbering);
- `data/derived/h236_h235_certificate_audit_summary.json`.

### H237 — current exact family continuation
H237 follows H235 positive survivors. It selects one actual shift-level H235 survivor from each of the 44 sector×chunk partitions and runs the unrestricted exact balanced `n3<=2` separator independently.

Files:
- `src/loto_research/h237_h235_first_survivor_exact_separation.py`;
- `.github/workflows/h237-h235-first-survivor-separation.yml`.

Expected outputs when merged:
- `data/derived/h237_h235_first_survivor_separation.json`;
- `data/derived/h237_new_witnesses.json`.

Each of 44 separator jobs has a 180-second exact MILP budget. Any returned witness is a rigorous new universal cut; timeout/no incumbent is inconclusive and never validation. If H237 returns new witnesses, feed genuinely new witnesses into the next full 44-way incremental rescreen. H237 itself cannot close the full H225 family merely by breaking sampled survivors.

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
- `research/h236_ri_lucky3_full_coverage_threshold.md`;
- `src/loto_research/h236_ri_lucky3_full_coverage_threshold.py`;
- `data/derived/h236_ri_lucky3_full_coverage_threshold.json`;
- `research/CHECKED_PROJECTS_AND_TESTS_H236_APPEND.md`.

Result: historical Lucky 3 full-coverage execution path **rejected as strict guarantee on recovered evidence**; current Kick Back remains evidence-blocked pending materially new primary rules.

### Preserved restricted-family state
- H224/H223/H222/H219 exact restricted outputs have not produced an authoritative closure result at this checkpoint.
- H221 proves any schema-valid restricted exact screen with `survivor_count=0` over all 143,712 H212-normalized classes closes that restricted family without a second MILP.

### Preserved promotion/execution state
- Current RI `Kick Back with Keno Promotion` is officially visible, but exact mechanics remain unrecovered; do not infer historical Lucky 3 mechanics without primary evidence.
- Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist; H236 adds the exact doubled full-space threshold but rejects executable all-entitlement coverage on recovered evidence.
- Current RI online/iLottery and ordinary retailer/SSVM remain closed as sole strict-guarantee execution channels under recovered public rules.

## NEXT ACTION
1. **Check H237 merged output first.** Missing output proves nothing.
2. If H237 has new exact balanced witnesses, deduplicate them against H234 and feed only genuinely new cuts into the next 44-way H225 incremental exact rescreen.
3. If any H237 jobs are inconclusive, retry only those jobs with a larger exact separator budget; never treat timeout/no incumbent as validation.
4. If a later incremental family rescreen reaches zero exact shift-surviving coefficient states across all 306,450 quotient states, record exact closure of H225 and move to the next still-open lottery-specific class.
5. Accept any late schema-valid restricted exact zero-survivor result separately under H221.
6. Reopen current `Kick Back with Keno` only on materially new primary evidence, especially rules revealing deterministic entitlement issuance, cancellation rights, or a promotion-wide multiplier.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H236_APPEND.md`.
