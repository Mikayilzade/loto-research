# CHECKED PROJECTS AND TESTS — H347 append

Date: 2026-08-29

## H347 — UK National Lottery Thunderball fixed-prize exact-cover screen
- Goal: test `STATUS.md` NEXT ACTION #1 on a current game with fixed advertised payouts per winning line across all prize categories.
- Matrix: 5 numbers from 1-39 plus 1 Thunderball from 1-14.
- Ticket price: £1 per line.
- Exact outcome-space cover: `C(39,5)*14 = 8,060,598` lines.
- Exact cover cost: **£8,060,598**.
- Exact category partition: **8,060,598 / 8,060,598 lines classified**.
- Advertised fixed-prize full-cover gross: **£4,262,568**.
- Deficit: **£3,798,030**.
- Return: **52.8815355883%**.
- Arithmetic inconclusive: **0**.
- Closure-relevant inconclusive: **0**.
- Result: **CLOSED / NOT SUCCESS**. Even before applying the operator's exceptional prize-reduction caveat, full advertised fixed-prize receipts are far below cost. Prize reductions can only weaken the floor.
- Reopen only on a material rule/payout/subsidy change that adds enough deterministic per-line value to move the exact full-cover bound above 100%.

Artifacts:
- `research/h347_uk_thunderball_fixed_cover.md`
- `research/H347_VALIDATION.md`
- `research/H347_STATUS.md`
- `src/loto_research/h347_uk_thunderball_fixed_cover.py`
- `data/derived/h347_uk_thunderball_fixed_cover.json`
