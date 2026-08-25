# CHECKED PROJECTS AND TESTS — H273 append

## H273 — Moldova National Lottery / 7777.md `AUGUST GENEROS 2026`

Status: **CLOSED / REJECTED for strict deterministic-profit construction**.

Checked because the campaign is funded from organizer revenue and therefore represents genuine external promotional money attached to gambling turnover.

Key rule facts verified from the active official-partner rules page on 2026-08-25:
- each MDL 100 of eligible real-money turnover creates one Special Prize participation;
- the current 17–30 Aug period awards one Mercedes-Benz CLE 200 Coupé or MDL 1,000,000 cash substitute;
- participations are assigned automatically and winner selection is random;
- electronic-ticket tournament pays top 1,000 from a MDL 500,000 bonus pool;
- tournament bonuses require x10 E-ticket or x5 SPORT wagering;
- calendar offers include conditional/periodic/random bonus mechanisms.

Tests completed:
1. **External-entry adversary:** for every finite own entry count, one external eligible current-period entry leaves a legal outcome where the external entry wins and our special-prize cash is zero.
2. **Identifier takeover test:** no hard issuance cap or player-reservable promotional identifier mechanism found; full pre-draw ownership cannot be certified.
3. **Leaderboard adversary:** for every finite own tournament score, 1,000 higher external scores are not ruled out by the published rules, so a zero-award rank remains legal.
4. **Cash-equivalence test:** tournament/calendar bonus funds are not unconditional cash and carry wagering/use conditions; face bonus amounts cannot be treated as deterministic cash profit.
5. **Campaign-liability arithmetic:** stated special-prize cash/cash-substitute values total MDL 2,120,000 across the three periods, but that external money is not deterministically allocable to a finite portfolio.

Primary source:
- https://7777.md/pages/?pr=1539

Artifacts:
- `research/h273_moldova_august_generos_guarantee_screen.md`
- `research/H273_VALIDATION.md`
- `src/loto_research/h273_moldova_august_generos_guarantee_screen.py`
- `data/derived/h273_moldova_august_generos_guarantee_screen.json`
- `research/H273_STATUS.md`

Reopen gate: only if a future version adds a hard capped/reservable promotional pool, a fixed bonus paid to every qualifying entry, or another deterministic liability whose full takeover cost can be bounded below the guaranteed cash-equivalent payout.
