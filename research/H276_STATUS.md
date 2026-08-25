# H276 STATUS — UK Thunderball fixed-prize exact bound

Updated: 2026-08-25
Branch: `research-work`
State: **CLOSED / REJECTED for checked strict-guarantee construction**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Checkpoint
H225-X* remains rigorously closed at X20 with **0 coefficient survivors / 0 legal shift tuples**. No X21/X22 work was created.

H276 opened a new fixed-per-winning-selection candidate: UK National Lottery Thunderball. The current checked game uses 5 of 39 main numbers plus 1 of 14 Thunderballs, costs £1 per line, and pays fixed prizes from £3 through £500,000.

Exact result:
- complete line universe: **8,060,598**;
- one-copy full-cover cost: **£8,060,598**;
- invariant fixed gross: **£4,262,568**;
- deficit: **£3,798,030**;
- return: **52.8815355883%**.

Stronger closure:
- by symmetry, every primitive legal line has the same 52.8815355883% average gross over the complete draw universe;
- every nonnegative portfolio therefore has the same average gross/cost ratio;
- since `minimum legal-outcome gross <= average gross < cost`, **no nonnegative portfolio of ordinary Thunderball lines can guarantee strict positive profit** under the checked paytable.

## Files
- `src/loto_research/h276_uk_thunderball_fixed_prize_bound.py`
- `data/derived/h276_uk_thunderball_fixed_prize_bound.json`
- `research/h276_uk_thunderball_fixed_prize_bound.md`
- `research/H276_VALIDATION.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H276_APPEND.md`

## NEXT ACTION
Do not reopen H225-X* or H276 under unchanged rules. Continue the global search with a structurally different mechanism where an external deterministic subsidy, hard-capped/reservable terminal identifier set, or forced payout raises the worst-case floor rather than merely the expectation. Prefer mechanisms whose additive value can be proved before attempting large cover optimization.
