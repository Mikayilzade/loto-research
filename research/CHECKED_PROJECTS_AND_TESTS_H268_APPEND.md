# CHECKED PROJECTS AND TESTS — H268 append

## H268 — New Zealand Powerball terminal / Must Be Won

Tested: 2026-08-25.

Mechanisms checked:
- terminal jackpot / Must Be Won rolldown to next-lowest winning Powerball division;
- exact full outcome-space takeover before 2026-09-13 (6/40 × PB 1..10);
- enacted 2026-09-13 matrix (6/40 × PB 1..14, new fixed D8);
- fixed lower-tier contribution;
- explicit external-D1 duplicate dilution with associated turnover still credited to lower prize pools.

Result: **REJECTED for strict guaranteed profit.**

Key blockers/results:
- any non-empty portfolio contains a line that is itself a legal D1 draw outcome, so no non-empty portfolio can force the no-D1 rolldown branch in every state;
- current one-copy full cover costs **NZ$57,575,700**;
- at NZ$50m jackpot, a legal finite state with **18,968 external exact D1 duplicates** leaves only **NZ$10,281,979.96** gross to the cover under conservative rules-minimum pool arithmetic;
- even NZ$60m on the same current matrix leaves only **NZ$10,282,494.71** at the scanned minimum;
- enacted 2026-09-13 full cover costs **NZ$80,605,980**; at NZ$60m, **23,175 external D1 duplicates** give only **NZ$15,122,347.33** gross.

Files:
- `research/h268_nz_powerball_terminal_duplicate_bound.md`
- `research/H268_VALIDATION.md`
- `src/loto_research/h268_nz_powerball_terminal_duplicate_bound.py`
- `data/derived/h268_nz_powerball_terminal_duplicate_bound.json`

Do not reopen ordinary NZ Powerball Must-Be-Won full-cover takeover unless a structural rule changes: unique/reservable D1 identifiers, fixed per-winning-selection terminal jackpot, hard cap on external duplicates, or another deterministic subsidy that survives duplicate minimisation.
