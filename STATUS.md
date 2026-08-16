# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H034 Ontario DAILY KENO completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H034 — Ontario DAILY KENO CLOSED as guarantee
Files:
- `research/h034_ontario_daily_keno_full_coverage.md`
- `data/derived/h034_ontario_daily_keno_full_coverage.csv`
- `src/loto_research/ontario_daily_keno.py`
- `tests/test_ontario_daily_keno.py`

Current official OLG mechanics:
- 20 numbers drawn from 1–70;
- Pick 2 through Pick 10;
- CAD 1/2/5/10 stakes with linear published prize scaling;
- fixed nominal prize table;
- one prize per selection;
- aggregate payout in each prize category capped at CAD 4,000,000, with proportional reduction if exceeded;
- Advance Play exists, but no deterministic multi-draw discount was identified in current public mechanics.

Exact full-coverage identity for Pick `k`:
- variants = `C(70,k)`;
- selections with exactly `m` matches = `C(20,m) * C(50,k-m)`.

Deliberately favorable **uncapped** full-space gross-return ratios:
- Pick 2: **55.0725%**
- Pick 3: **52.0643%**
- Pick 4: **52.8414%**
- Pick 5: **42.0329%**
- Pick 6: **44.3424%**
- Pick 7: **48.3379%**
- Pick 8: **46.6006%**
- Pick 9: **43.0412%**
- Pick 10: **44.7615%**.

Best favorable result is only 55.07%. The statutory category cap can only reduce large-portfolio payouts. By symmetry these ratios are also the uncapped gross EV/stake of a base selection in each Pick class. Therefore every nonnegative additive mixture has negative expectation; a strict all-outcome positive-profit portfolio would imply positive expectation and is impossible under the ordinary additive rules.

Status: **REJECTED as guaranteed-profit additive/coverage class**.

# H033 — New Zealand Bullseye discounted multi-draw coverage CLOSED as guarantee
Files:
- `research/h033_nz_bullseye_discounted_coverage.md`
- `data/derived/h033_nz_bullseye_full_space.csv`
- `src/loto_research/nz_bullseye.py`
- `tests/test_nz_bullseye.py`

Current official rules validate an unusually large deterministic pricing nonlinearity:
- normal selection: NZ$2 per draw;
- 7 consecutive draws: NZ$10 instead of NZ$14;
- 14 consecutive draws: NZ$20 instead of NZ$28;
- deterministic discount: **28.5714%**.

Full Bullseye number space is exactly 1,000,000 six-digit selections. Owning all selections gives, every draw, exactly:
- Division 1: 1 own winning selection;
- Division 2: 10;
- Division 3: 90;
- Division 4: 900;
- Division 5: 9,000;
- Division 6: 90,000 bonus-ticket selections.

7-draw full coverage therefore costs **NZ$10,000,000**; 14-draw coverage costs **NZ$20,000,000**.

Despite the discount, strict guaranteed cash profit fails. Divisions 1–5 are shared/capped cash pools and the current rules provide no useful pre-draw hard cap on external duplicate winning selections. External duplicates can dilute our finite pool share arbitrarily; Division 6 is a bonus ticket, not guaranteed terminal cash. Full coverage also guarantees a Division-1 winner every covered draw, preventing continued no-winner jackpot accumulation during the coverage sequence.

Status:
- 28.57% multi-draw discount: **VALIDATED nonlinearity / EV overlay lead**;
- strict standalone guaranteed-profit full coverage: **REJECTED**.

# H032 — Canada DAILY GRAND CLOSED
Full coverage of `C(49,5)*7 = 13,348,188` lines costs CAD 40,044,564. Favorable face-value gross was only 44.3472%; strict immediate-cash floor 36.2112%. Combo Play is linear pricing. **REJECTED guarantee.**

# Recently closed branches
- H031 Georgia/Virginia Cash Pop Cover All: guaranteed win but strict floor only 33.33% of coverage cost.
- H029/H029b Virginia Pick 3/4/5 including FIREBALL: additive-family guarantee rejected by expectation upper bound.
- H030 Virginia Cash 5 + EZ Match: current full-space route strongly negative; jackpot sharing prevents strict future guarantee without hard external-winner cap.
- H021–H028 current compact/fixed/full-space screens: all sampled products rejected.
- Beşdə 5 and ONLOTO 1–10 full coverage: rejected.
- Powerball/Mega Millions/EuroMillions full-space terminal guarantees: rejected.
- H012a/H004 ordinary additive wheels: rejected by expectation theorem.
- H015 anti-crowd standalone: rejected as guarantee; overlay only.

# Other active / blocked branches
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; current raw-book acquisition remains runtime/data blocked.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Next priorities
1. Continue fast analytic screen on **additional current compact finite/fixed-payout products**, but prioritize candidates with deterministic discounts/subsidies or optimistic coverage return materially above the now-common 40–60% range.
2. Search specifically for **discount + non-shared fixed cash payouts**; H033 proves meaningful pricing nonlinearities exist, while H034 shows ordinary fixed-payout Keno without subsidy remains far from the hurdle.
3. H020 live-data arbitrage immediately if raw public books become retrievable.
4. H019 capped competitions only when cash floor/full-cap economics improve materially.
5. H006/H007 only after reliable histories/machine metadata become obtainable.
6. H010/H014 if new authoritative data routes appear.
7. H018 conditional-EV calibration if exact mechanics/live endpoint become recoverable.
8. Advanced controls before EXHAUSTED: more current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
