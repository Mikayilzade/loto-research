# CHECKED PROJECTS / TESTS — H326 APPEND

## H326 — LLF Games £350 cash postal-route takeover

Checked: 2026-08-28
Status: **CLOSED / CAP-AND-EXECUTION-BLOCKED**

Mechanism tested: hard finite single-winner cash pool + free postal route whose real postage cost is below the online ticket price.

Current recurring draw snapshot:
- 350 identifiers;
- £350 cash liability;
- £1.99 online price;
- £0.91 current Royal Mail 2nd Class postage;
- max 35 entries per person;
- 10 sold at checked snapshot;
- random number allocation after order/postal validation.

Exact stronger-than-real economics:
- paid full pool: £696.50 cost → 50.2513% gross;
- postal full pool: £318.50 cost → **109.8901% gross**, +£31.50;
- snapshot all-remaining fantasy: 340 × £0.91 = £309.40 → 113.1222% against the £350 prize.

Rigorous blocker:
- person cap controls at most 10% of the pool;
- even from zero sold, 315 identifiers must remain uncontrolled;
- one uncontrolled valid identifier preserves a legal external-winner outcome;
- postal processing is non-atomic and entries are only allocated after receipt/validation;
- operator terms allow refusal of entries.

Strict guaranteed cash floor: **£0**.

Reusable lesson: favourable full-postal economics alone are insufficient. For a single-winner finite pool, `max_per_player >= required takeover support` and deterministic acceptance/reservation are mandatory gates before a >100% acquisition ratio can become a guaranteed-profit construction.

Primary sources:
- https://llfgames.com/competition/win-350-cash-for-1-99-56/
- https://www.royalmail.com/sending/uk/2nd-class
