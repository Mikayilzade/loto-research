# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## GO-mode
User message `го` means: continue the next highest-value research packet without clarification. Chat output stays minimal. After each meaningful packet:
1. save raw/derived data and/or code;
2. update the relevant research note;
3. update `research/CHECKED_PROJECTS_AND_TESTS.md`;
4. update this file when the strategic conclusion changes.

This file is the authoritative handoff checkpoint. Read `START_HERE.md`, `PROJECT_RULES.md`, `RESEARCH_PLAN.md`, `AGENTS.md` and `research/CHECKED_PROJECTS_AND_TESTS.md` before work.

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H012 — full-space / buy-the-pot: active priority
Files:
- `src/loto_research/full_space.py`
- `tests/test_full_space.py`
- `data/derived/h012_full_space_screen.csv`
- `research/h012_full_space_coverage.md`

## Azerbaijan Beşdə 5 — CLOSED
Full coverage of all `C(36,5)=376,992` variants costs **376,992 AZN**.
For every possible draw the exact full-space match counts are fixed:
- 5 matches: 1
- 4: 155
- 3: 4,650
- 2: 44,950.

Even granting the full 50,000-AZN jackpot and ignoring tax/sharing, deterministic gross payout is only **201,900 AZN**.
Guaranteed pre-tax/pre-sharing net: **-175,092 AZN**; return **53.5555%**.

Status: **REJECTED as guaranteed-profit coverage**.

## Azerbaijan ONLOTO — all base types CLOSED
Exact ordered-draw identity implemented: when every k-subset of 50 is bought once, the number of variants whose final selected number appears at position j is `C(j-1,k-1)`. This makes full-space payout deterministic from the published multiplier table.

Guaranteed gross-return ratios for bet types 1–10:
- 1: 78.0000%
- 2: 77.5510%
- 3: 77.5408%
- 4: 77.6878%
- 5: 77.5309%
- 6: 76.5943%
- 7: 77.3335%
- 8: 77.3440%
- 9: 77.3644%
- 10: 77.2782%.

All are guaranteed losses before tax/execution. Type-6 indexed table has one flagged local non-monotone parsed cell sequence, but the ~23% deficit is far too large for a plausible one-cell correction to reverse.

Status: **REJECTED as guaranteed-profit coverage**.

## Azerbaijan 4+4 — H012 still BLOCKED
Full base space = `C(20,4)^2 = 23,474,025` variants.
Exact guarantee theorem remains blocked by:
- authoritative per-base/system-ticket pricing for 4+4 vs 5+5/6+6;
- category-II/carryover rule;
- pool response and jackpot sharing when our portfolio itself dominates sales.
No evidence of a nonlinear cheap system-ticket discount has been found yet.

# Other active/validated branches
- Cash WinFall: historical +EV mechanism validated, not current guarantee.
- H014 Azerbaijan 4+4 state-dependent pool/carryover: testing/data-blocked.
- H017 Kazakhstan 4/20 zero-winner lower-pool → next-superprize: validated mechanism, sampled state strongly negative.
- H015 anti-crowd: validated EV/share optimizer but **rejected as standalone guaranteed-profit path**.
- H010 Poz-Qazan remaining-prize edge: data-blocked on live remaining-ticket denominator.
- H002 Powerball progressive threshold: optimistic cash break-even floor already established; real threshold higher.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` contains the full checked-project / test-variant trail and remaining branches.

# Safe next priorities
1. Continue **H012** with other current finite/final-draw games and search specifically for accumulated guaranteed pools or nonlinear system-ticket pricing.
2. H012a/H004: partial covering / integer-programmed guaranteed lower-tier floors.
3. H005: nonlinear portfolio/cap/guarantee interactions.
4. H009: current promotional subsidies that can combine with coverage.
5. H002: progressive jackpots with all real sharing/tax/sales-response constraints.
6. H014/H010 when new data routes appear.
7. H006/H007 physical/RNG anomaly branches after reliable histories are collected.
