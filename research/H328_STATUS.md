# H328 STATUS

Updated: 2026-08-28
State: **CLOSED / RANDOM-ALLOCATION ZERO-SUPPORT BLOCKED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Result

H328 tested the current BOTB `Carnival Extravaganza` finite Instant Wins pool against the BOTB Pass subsidy route.

Current published snapshot:
- 999,999 maximum ticket identifiers;
- £1.29 paid entry;
- 4,761 instant prizes won;
- 195,204 instant prizes left;
- therefore 199,965 prize-bearing identifiers represented by the snapshot and **800,034 zero-instant identifiers**.

BOTB states Instant Wins ticket numbers are randomly generated after checkout. Therefore a subsidised bundle can force a positive instant-prize floor only if its guaranteed size exceeds all zero-instant support.

H328 deliberately grants an impossible stronger subsidy stress: all 209 monthly Ultimate-plan entries from the documented Pass configuration may be redirected into this single pool, despite the documented Instant-Win allocation being only 15. Since `800,034 >= 209`, there remains a legal allocation where all subsidised tickets receive zero-instant identifiers. The separate £2,000 end draw also has zero worst-case floor while external identifiers remain.

**Strict guaranteed withdrawable-cash floor: £0.**

Files:
- `research/h328_botb_carnival_pass_gate.md`
- `research/H328_VALIDATION.md`
- `src/loto_research/h328_botb_carnival_pass_gate.py`
- `data/derived/h328_botb_carnival_pass_gate.json`

## H225 lane

`H225-X*` remains **CLOSED / EXHAUSTED** at X20 with 0 coefficient survivors / 0 legal shift tuples. Do not create X21/X22 from the unchanged family.

## NEXT ACTION

Do not reopen H328 unless allocation/subsidy scale materially changes. Continue with a new finite lottery/prize mechanism where subsidised acquisition exceeds all zero-cash support, exact prize IDs can be selected/reserved before purchase, or every possible identifier has a positive withdrawable-cash floor above effective acquisition cost.
