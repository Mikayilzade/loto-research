# H317 checked-project append

## Universal Competitions — stop-on-hit cash pool

Status: **CLOSED / NO SUCCESS** (2026-08-27)

Checked the live `£100 CASH!! 1 PRIZE! CAN GO ANYTIME!!!! £100 Cash Jackpot!!` finite pool because its draw ends immediately when the instant cash identifier is hit, creating a potentially useful stopping-time takeover mechanism.

Exact snapshot:
- 3,999 total tickets at £0.10;
- 1,135 sold, 2,864 remaining;
- remaining-tail cost £286.40.

Deliberately favourable bound grants the player both the £100 instant cash and a separate full £100 jackpot = £200 total. Even impossible-perfect ownership of every remaining identifier therefore returns only **69.83240223%**, a deterministic £86.40 deficit.

Reusable rejection gate: stop-on-hit pools require `forced liability > cost of all uncontrolled remaining identifiers`. H317 fails before reservation/checkout friction is considered.

Files:
- `research/h317_universal_can_go_anytime_stopping_bound.md`
- `research/H317_STATUS.md`
- `src/loto_research/h317_universal_can_go_anytime_bound.py`
- `data/derived/h317_universal_can_go_anytime_bound.json`
