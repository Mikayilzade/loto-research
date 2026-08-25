# CHECKED PROJECTS AND TESTS — H266 APPEND

## H266 — Australian Super66 terminal / must-be-won exact-cover screen

- Opened because Super66 combines a finite 10^6 identifier universe, fixed lower prizes, a jackpot, and a terminal must-be-won/rolldown mechanic.
- Current Lotterywest page checked: A$1/game; six digits automatically generated; D2-D5 fixed prizes A$6,666 / A$666 / A$66 / A$6.60.
- Current WA rules compilation checked for ordered-match criteria and higher-division precedence.
- Impossible-favourable exact one-copy cover of all 1,000,000 identifiers audited.
- Exact invariant winning counts: D1=1, D2=18, D3=180, D4=1,800, D5=17,901.
- Fixed D2-D5 gross = **A$476,814.60**, only **47.68146%** of the A$1,000,000 cover cost.
- D1 share required for strict break-even = **A$523,185.40**; with `E` external duplicate D1 entries, strict profit requires `J > 523185.40*(E+1)`.
- 22 Aug 2026 A$80,000 jackpot: even impossible sole-D1 ownership gives only **55.68146%** total cover return.
- 8 Aug 2026 A$449,669.85 D1 pool: even granting our cover the entire pool gives only **92.648445%**; actual results had three D1 winning tickets.
- Structural theorem: any nonempty portfolio owns some six-digit identifier `x`, and draw `x` is a legal outcome that makes the portfolio a D1 winner. Therefore no nonempty portfolio can force the terminal no-D1 rolldown in every legal outcome; a full cover necessarily blocks that branch itself.
- Exact player-selected takeover is additionally not established because current Lotterywest material says Super66 numbers are automatically generated.
- No hard pre-draw cap on external duplicates was established.

**Disposition: CLOSED / REJECTED for the current strict guaranteed-profit terminal/takeover mechanism.**

Files:
- `research/h266_super66_terminal_must_be_won_bound.md`
- `research/H266_VALIDATION.md`
- `src/loto_research/h266_super66_terminal_bound.py`
- `data/derived/h266_super66_terminal_bound.json`
