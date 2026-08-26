# CHECKED PROJECTS / TESTS — H282 append

## H282 — Kentucky CASH POP + August 2026 deposit subsidy

Status: **REJECTED / CLOSED for strict guaranteed-profit construction**.

Checked mechanism:
- current Kentucky Lottery 100% first-deposit match up to $250 (Aug 1-31, 2026);
- CASH POP native `Cover All` over 15 numbers;
- all allowed stakes $1/$2/$5/$10;
- current published minimum prizes $5/$10/$25/$50;
- favorable stress tests granting stacking with current $50 Tiki Tuesday or 25% Summer Friday deposit bonuses.

Exact blocker:
- a strict guarantee must cover all 15 winning numbers;
- in a legal minimum-prize-assignment branch, payoff on winning number i is exactly 5 times stake assigned to i;
- least-covered-number argument gives universal worst-case gross `<= total_spend/3` for any nonnegative CASH POP portfolio;
- 100% deposit match therefore yields at most `2/3` recovery of deposited cash through withdrawable prizes;
- favorable Tiki stack reaches only 77.7778% cash recovery;
- favorable Summer-Friday stack reaches only 75%.

This closes CASH POP more strongly than a one-ticket Cover All test: arbitrary stake mixtures, ticket grouping and multi-draw portfolios inherit the same one-third wallet-spend worst-case ceiling.

Reopen condition: deterministic subsidy usable on CASH POP exceeds 200% of deposited cash, or the game changes so the minimum-prize-multiple / 15-number geometry pushes the exact worst-case ratio materially above 1/3.

Artifacts:
- `research/h282_kentucky_cashpop_bonus_bound.md`
- `research/H282_VALIDATION.md`
- `research/H282_STATUS.md`
- `src/loto_research/h282_kentucky_cashpop_bonus_bound.py`
- `data/derived/h282_kentucky_cashpop_bonus_bound.json`
