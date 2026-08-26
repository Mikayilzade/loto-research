# H300 independent validation

Validated: 2026-08-27
Result: **PASS — strict guaranteed-profit claim rejected**

## Source facts rechecked

The live Net-A-Deal “£10,000 Instant wins August #2 | Every ticket wins” page states 49,999 tickets, maximum 1,000 entries per person, £0.49 per paid entry, random ticket-number allocation, and the prize schedule 10×£500 + 12×£250 + 10×£100 + 40×£25 Site Credit. Tickets not receiving those listed instant wins are entered into a separate £5,000 rewards competition.

## Arithmetic checks

- cash instant-win identifiers: `10 + 12 + 10 = 32`;
- site-credit identifiers: `40`;
- residual rewards-draw identifiers: `49,999 - 32 - 40 = 49,927`;
- per-person entry cap: `1,000`;
- `49,927 >= 1,000`;
- max paid spend: `1,000 × £0.49 = £490`;
- listed cash instant-win total: `£9,000`;
- listed site-credit face total: `£1,000`.

## Worst-case proof

Because ticket identifiers are randomly allocated and at least 1,000 residual identifiers exist, an allowed 1,000-ticket purchase has a legal allocation in which every purchased identifier is residual. Residual identifiers only create entries into a separate random rewards competition. A legal rewards-draw outcome can award the £5,000 prize elsewhere.

Therefore there exists a legal overall outcome with **£0 withdrawable cash** for any entrant limited to at most 1,000 paid tickets. Strict guaranteed cash profit is impossible under the checked mechanic.

## Validation gates

- no expected-value inference used: PASS;
- no assumption that advertised “Every ticket wins” means cash: PASS;
- per-person cap explicitly incorporated: PASS;
- random ticket allocation explicitly incorporated: PASS;
- later rewards draw treated by worst-case, not average: PASS;
- result reproducible from committed Python/JSON: PASS.

This validation closes H300 for the stated mechanism only. It does not claim all Net-A-Deal competitions are unprofitable under every possible future promotion.
