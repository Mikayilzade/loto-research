# Checked projects and test variants

Updated: 2026-08-15
Purpose: permanent audit trail of what has been tested, what worked, what failed, and what remains. Do not remove failed paths; append/revise status with evidence.

Completion criterion for the research program:
1. find a reproducible, executable profit guarantee after all costs and outcome branches; OR
2. exhaust the currently defensible project/edge classes and document why each fails or remains data-blocked.

## Checked / active projects

| Project / mechanism | Test variant | Result | Status | Main evidence |
|---|---|---|---|---|
| Cash WinFall | historical roll-down, May 9 2011 cash-only EV | +10.69% expected ROI before tax/execution | validated historical +EV mechanism | `research/cash_winfall_benchmark.md` |
| Azerbaijan Beşdə 5 | exact probability + full displayed prize-table EV | ~53.56% gross return upper-bound | rejected as ordinary +EV | `research/azerbaijan_baseline.md` |
| Azerbaijan Super Keno | base 1-AZN table EV | ~59.86% gross before tax | rejected as ordinary +EV | `research/azerbaijan_baseline.md` |
| Azerbaijan Super Keno | 1x/2x/5x/10x multiplier economics | proportional stake/payout; after-tax ROI slightly worsens as multiplier rises | no multiplier edge | `research/superkeno_multiplier_economics.md` |
| Azerbaijan 4+4 | exact combinatorics | jackpot 1/23,474,025; any listed prize ~18.61% | validated math | `research/4plus4_baseline.md` |
| Azerbaijan 4+4 | draw-level payout-engine reconstruction | III=11U, IV=5U, VII=9U, VIII=14U, IX=7U, V+VI=2U | strongly reproduced; multiple out-of-sample rows | `research/4plus4_economics_inference.md` |
| Azerbaijan 4+4 | V/VI hierarchy split | combined 2U reallocated when needed to protect prize order | strong empirical rule | `research/4plus4_economics_inference.md` |
| Azerbaijan 4+4 | zero-winner II–VI carryover | potentially material; adjacent-state proof unavailable | testing/data-blocked | H014; `STATUS.md` |
| Azerbaijan 4+4 | category II ≈20U | suggestive only; winner-story arithmetic alone insufficient | unvalidated | `research/4plus4_category2_lead.md` |
| Azerbaijan 4+4 | hidden archive/API search | archive client-rendered; authoritative endpoint not recovered | blocked; do not repeat blind URL guessing | `research/azerlotereya_archive_api_discovery.md` |
| Azerbaijan 4+4 | Telegram result-card archive | official draw cards exist; current tooling cannot fetch Telegram CDN JPEG | blocked by tooling | `STATUS.md` |
| Kazakhstan 4/20 | zero-winner lower-pool -> next superprize transition | exact identity reproduced on 3 independent transitions | validated active mechanism | `research/kazakhstan_4x20_control.md` |
| Kazakhstan 4/20 | sampled-state EV | ~55% return; break-even superprize ~3.395bn KZT vs ~227m | mechanism real, sampled state negative | same note |
| UK Lotto pre-2026 | historical Must Be Won rolldown | July 2025 sampled rolldown still negative | no immediate +EV | UK Lotto research notes |
| UK Lotto 2026 | two-round Must Be Won | July 18 2026 sampled state ~£1.53/£2 | negative sampled state | `research/uk_lotto_regime_2026.md` |
| UK Lotto | Wednesday Must Be Won calendar edge | historical demand uplift usually exceeds break-even cushion | materially weakened | H016 |
| Shared-pool number choice | jackpot collision / unpopular-combination bound | exact-jackpot component can improve, but bounded; not standalone cure | useful optimizer only | `research/h015_crowd_sharing.md` |
| Shared-pool number choice | lower-tier competitor-intensity sensitivity | potentially large payout uplift if crowd intensity can be predictably reduced | promising, crowd model unvalidated | H015 |
| Azerbaijan Poz-Qazan | initial-series exact after-tax EV | Prestij ~69.91%; Meqa 7 ~66.88%; Qoşa 2 ~66.31%; 4 Fəsil ~62.98% | ordinary initial states negative | `research/poz_qazan_remaining_prize_edge.md` |
| Azerbaijan Poz-Qazan | remaining-prize conditional EV | denominator exists institutionally but no public live registration-specific count found | testing/data-blocked | H010 |
| Azerbaijan Poz-Qazan | infer inventory from winner carousel | invalid because carousel mixes different registrations/eras | rejected method | H010 note |
| Powerball US 2026 | fixed lower-tier EV + no-sharing/no-tax cash-jackpot break-even floor | lower tiers ~0.31988 USD EV; cash jackpot must exceed ~490.93m USD even before tax/sharing | threshold baseline established; real threshold higher | `research/powerball_progressive_threshold.md` |

## Hypothesis classes not yet fully tested

- H002: full Powerball / Mega Millions / EuroMillions progressive threshold including tax, sharing and sales response.
- H004: covering designs / wheels as risk-profile optimization.
- H005: nonlinear portfolio/cap/guarantee effects.
- H006: physical draw bias with multiple-testing controls.
- H007: high-frequency RNG anomaly tests: Ekspres Keno, Şanslı 6, ONLOTO.
- H008: cross-jurisdiction same-jackpot EV differences, especially US vs UK Powerball.
- H009: promotions/cashback/free-ticket/second-chance overlays.
- H011: lawful visible-ticket information leak for instant tickets.
- H012: full-space coverage / buy-the-pot in current finite games.
- H015: empirical pre-draw crowd-choice model, beyond theoretical sensitivity bounds.
- Additional current lotteries and lottery-like products outside the initial catalog.

## Permanent controls / already rejected as standalone edges

- hot/cold numbers;
- “due” numbers / gambler’s fallacy;
- numerology;
- martingale/bet sizing on negative EV;
- ML fitted and tested on the same draws;
- number-picking systems that do not alter probabilities or payout sharing;
- brute-force enumeration where it cannot change the underlying expectation.

## Rule for future work
Every new research packet must either:
- add a row/result here; or
- update an existing row with stronger evidence/status.

The detailed hypothesis registry remains `research/HYPOTHESES.md`; this file is the human-readable audit ledger requested for later review.
