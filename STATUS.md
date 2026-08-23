# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed numbered lottery packet: **H241 — Missouri Club Keno Bulls-Eye / Double Bulls-Eye Bonus Hours full-coverage upper-bound closure**.
Latest completed exact family packet: **H235 — H234-augmented exact 44-way family rescreen**.
Current exact family continuation: **H237 — 44-way unrestricted exact separation of actual H235 survivors** (launched/pending merge).

### H232/H234/H235 exact-family state
- H232 screened **306,450** quotient coefficient states; **306,098** retained at least one legal shift tuple; **139,869,763** exact legal shift tuples survived the then-current witness bank.
- H234 selected 44 actual H232 survivor designs and found exact unrestricted balanced `n3<=2` counterexamples for **44/44**, with no inconclusive jobs.
- H235 added all 44 H234 witnesses with affine symmetries and rescreened the full family: **303,802** coefficient states and **90,425,060** legal shift tuples still survive. H225 remains open.

### H237 — current exact family continuation
Expected merged outputs:
- `data/derived/h237_h235_first_survivor_separation.json`
- `data/derived/h237_new_witnesses.json`

As of H241 these outputs are still absent on `research-work`. Missing output proves nothing. Any returned witness is a rigorous new cut; timeout/no incumbent is inconclusive and never validation.

### H236 — RI Lucky 3 Spot threshold
Historical Rhode Island Lucky 3 Spot promotions created a real printed pre-draw entitlement doubling winning 3-spot prizes. For full 20/80 3-spot coverage, strict pre-tax profit under a true universal free 2X entitlement requires `10*P2 + P3 > 36.03508771929825`. The theorem is valid, but universal entitlement acquisition and finite-window execution were not established.

### H238 — current RI Kick Back
Current Rhode Island `Kick Back with Keno` remains **DATA-BLOCKED / NOT SUCCESS**. Ordinary Keno Plus remains random, not player-selectable 2X.

### H239 — Georgia / North Carolina deterministic Bonus Hours
- Georgia +30% full 3-spot coverage: **81.1709%** deterministic return; rejected.
- North Carolina +50% with mandatory Multiplier: **48.9107%** guarantee-relevant return; rejected.

### H240 — Missouri base Club Keno Bonus Hours
All ordinary base Club Keno spot categories 1–10 were screened by exact full coverage under a deliberately stronger-than-real promotion granting universal +50% to every base prize. Best category: **3-spot at 93.6587%**. Base full-coverage class rejected.

### H241 — Missouri Bulls-Eye / Double Bulls-Eye Bonus Hours
Official Missouri rules establish Bulls-Eye doubles ticket cost, Double Bulls-Eye triples it, and Bonus Hours permits qualifying multi-draw Bulls-Eye / Double Bulls-Eye wagers while excluding Multiplier.

Exact marked-number counting inside a fixed 20/80 draw:
- Bulls-Eye: `C(1,r) C(19,m-r) C(60,s-m)`.
- Double Bulls-Eye: `C(2,r) C(18,m-r) C(60,s-m)`.
- payout uses ordinary base for r=0, Bulls-Eye for r=1, Double Bulls-Eye for r=2.

A dominant upper bound grants **+50% to every payout with no exclusions**, stronger than actual Bonus Hours.

Results across every spot 1–10:
- best Bulls-Eye: **3-spot at 90.9749%**;
- best Double Bulls-Eye: **9-spot at 98.0054%**;
- therefore neither add-on can guarantee profit under the real weaker promotion.

Files:
- `research/h241_missouri_bullseye_bonus_hours_full_coverage.md`
- `src/loto_research/h241_missouri_bullseye_bonus_hours_full_coverage.py`
- `data/derived/h241_missouri_bullseye_bonus_hours_full_coverage.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H241_APPEND.md`

### Preserved restricted-family state
- H224/H223/H222/H219 exact restricted outputs have not produced an authoritative closure result at this checkpoint.
- H221 proves any schema-valid restricted exact screen with `survivor_count=0` over all 143,712 H212-normalized classes closes that restricted family without a second MILP.

## NEXT ACTION
1. **Check H237 merged output first.**
2. If H237 has new exact balanced witnesses, deduplicate against H234 and feed only genuinely new cuts into the next 44-way H225 incremental exact rescreen.
3. Retry only genuinely inconclusive H237 jobs with larger exact separator budgets; never treat timeout/no incumbent as validation.
4. If a later incremental family rescreen reaches zero exact shift-surviving coefficient states across all 306,450 quotient states, record exact closure of H225.
5. Accept any late schema-valid restricted exact zero-survivor result separately under H221.
6. Reopen RI Kick Back only on materially new current primary evidence.
7. Missouri base/Bulls-Eye/Double Bulls-Eye Bonus Hours full-coverage variants are closed unless rules materially change.
8. If H237 remains absent, move to the next non-duplicate lottery-specific nonlinear edge class from the audit ledger, prioritizing active deterministic overlays/rolldowns over already-closed additive full-coverage games.
9. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H241_APPEND.md`.
