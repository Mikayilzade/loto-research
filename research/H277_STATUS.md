# H277 STATUS — Millionaire for Life

Updated: 2026-08-26
Branch: `research-work`
State: **CLOSED / REJECTED**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## New checkpoint

H277 tested the current 2026 multi-state Millionaire for Life game using an exact full-space calculation and a stronger portfolio-wide symmetry proof.

- Matrix: 5 of 58 + 1 of 5 Millionaire Ball.
- Price: $5.
- Exact outcome space: 22,910,580.
- Complete-cover acquisition cost: $114,552,900.
- Player-favourable dominating model: top two published cash options treated as fixed undiluted $18m and $2.2m, despite official pari-mutuel weakening.
- Exact complete-cover gross: $60,584,320.
- Return: 52.8876353196%.
- Deficit: $53,968,580.

Because legal plays and draw outcomes are symmetric, every primitive play has the same average-return ratio under this dominating model. Every nonnegative portfolio therefore has that same average ratio. Since minimum outcome gross cannot exceed average gross, no ordinary current ticket portfolio can guarantee strict profit.

Files:
- `src/loto_research/h277_millionaire_for_life_portfolio_bound.py`
- `data/derived/h277_millionaire_for_life_portfolio_bound.json`
- `research/h277_millionaire_for_life_portfolio_bound.md`
- `research/H277_VALIDATION.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H277_APPEND.md`

## NEXT ACTION

Continue outside H225 with a genuinely different lottery-specific mechanism. Prioritize a deterministic external subsidy, hard-capped/reservable identifier pool, or forced-distribution rule whose winner-facing worst-case value is not bounded below 100% by simple additive symmetry. Do not reopen H277 unless its payout/promotion structure materially changes.
