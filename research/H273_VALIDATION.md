# H273 VALIDATION — Moldova AUGUST GENEROS 2026

Validated: 2026-08-25
Packet: `H273`
Result: **CLOSED / REJECTED**

## Source validation

Primary rules page checked directly on 2026-08-25:
- https://7777.md/pages/?pr=1539

Confirmed from the published rules:
- campaign period: 1–31 August 2026;
- funded from organizer revenue with no separate campaign participation fee;
- every MDL 100 of eligible real-money turnover creates one Special Prize participation;
- 17–30 Aug registration period has one Mercedes-Benz CLE 200 Coupé prize or MDL 1,000,000 cash substitute;
- special-prize winners are selected using the platform RNG from registered participations;
- electronic-ticket tournament has 1,000 paid places and MDL 500,000 total bonus pool;
- tournament awards are bonus funds with x10 E-ticket or x5 SPORT wagering requirement;
- calendar bonus mechanisms include conditional/periodic and random awards.

## Arithmetic validation

Special-prize cash/cash-substitute values:
- 7 × MDL 100,000 = MDL 700,000;
- 7 × MDL 60,000 = MDL 420,000;
- current-period cash substitute = MDL 1,000,000;
- campaign total = **MDL 2,120,000**.

## Strict-guarantee validation

### Current Special Prize
For any finite number `N >= 1` of our entries, if at least one external eligible participation exists, the RNG may legally select that external participation. Hence an admissible outcome exists with our promotional cash receipt equal to zero.

Therefore:
`min_outcome promotional cash = 0` whenever `external_entries >= 1`.

No hard issuance cap or player reservation mechanism was found in the checked rules, so complete ownership cannot be certified.

### Tournament
For any finite own score `S`, the published rules impose no hard global points cap. A legal adversarial configuration can contain 1,000 external participants with scores `> S`, making our rank worse than 1,000 and our tournament award zero.

Therefore no finite pre-draw score establishes a strict positive tournament floor under the published rules.

### Calendar bonuses
The checked calendar offers are conditional/periodic and several values are random. Bonus awards are not equivalent to unconditional cash. They cannot be inserted as a deterministic positive cash floor before their specific offer terms and outcome are known.

## Code/data consistency

The structural witnesses encoded in:
- `src/loto_research/h273_moldova_august_generos_guarantee_screen.py`

match the stored derived packet:
- `data/derived/h273_moldova_august_generos_guarantee_screen.json`

Required conclusions:
- current special-draw floor with one external eligible entry = **0 MDL**;
- tournament floor with 1,000 higher external scores = **0 MDL**;
- fixed unconditional calendar cash floor established = **0 MDL**.

## Final validation

H273 is closed for the project's strict deterministic-profit target. The promotion does inject genuine external money, but the checked money is allocated through open random draws, an unbounded leaderboard, or conditional/random bonus offers. None is a finite monopolizable guaranteed liability.
