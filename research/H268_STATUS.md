# H268 STATUS

Updated: 2026-08-25
Packet: **H268 — New Zealand Powerball terminal / Must Be Won duplicate bound**
Terminal state: **CLOSED / REJECTED FOR STRICT GUARANTEE**

## Result

H225-X* remains rigorously closed at X20 and was not extended.

H268 tested New Zealand Powerball's terminal / Must Be Won rolldown against exact complete outcome coverage and explicit legal external Division-1 duplication.

### Current pre-2026-09-13 matrix
- `C(40,6) * 10 = 38,383,800` paired outcome lines.
- NZ$1.50 per line.
- Full-cover cost: **NZ$57,575,700**.
- At a NZ$50m jackpot stress level, a legal state with **18,968 external exact D1 duplicates** leaves gross **NZ$10,281,979.962637568**, a deficit of **NZ$47,293,720.037362434**.
- Even a NZ$60m sensitivity remains below cost: minimum gross **NZ$10,282,494.71341036** at **19,884** duplicates.

### Enacted 2026-09-13 matrix
- `C(40,6) * 14 = 53,737,320` paired outcome lines.
- Full-cover cost: **NZ$80,605,980**.
- At NZ$60m jackpot stress, a legal state with **23,175 external exact D1 duplicates** leaves gross **NZ$15,122,347.333168669**, a deficit of **NZ$65,483,632.66683133**.

### Structural blocker
Every purchased paired line is itself a legal Powerball Division-1 draw outcome. Therefore every non-empty portfolio preserves at least one legal draw state in which it creates Division 1 itself. A portfolio cannot force the no-D1 terminal rolldown branch in every draw state. Complete coverage guarantees an own D1 winner and therefore prevents the rolldown condition rather than forcing it.

The explicit duplicate construction is sufficient to reject strict guaranteed profit: the model credits external duplicate turnover into lower pools while diluting the shareable D1 prize, and still produces finite legal states far below acquisition cost.

## Files
- `research/h268_nz_powerball_terminal_duplicate_bound.md`
- `research/H268_VALIDATION.md`
- `src/loto_research/h268_nz_powerball_terminal_duplicate_bound.py`
- `data/derived/h268_nz_powerball_terminal_duplicate_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H268_APPEND.md`

## NEXT ACTION
Continue the global lottery search outside closed H225-X* and H268. Prioritize terminal/forced-distribution mechanisms where top-prize eligibility is hard-capped and monopolizable before cutoff, or where accumulated external money is paid as a fixed amount per winning selection and survives external-duplicate stress. Do not reopen ordinary New Zealand Powerball full-cover takeover unless a structural rule changes.
