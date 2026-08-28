# H326 STATUS

Updated: 2026-08-28
State: **CLOSED / CAP-AND-EXECUTION-BLOCKED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Result

H326 tested the current LLF Games recurring **£350 Cash For £1.99** finite pool using its free postal entry route.

This produced a genuine positive-arithmetic near miss. With 350 total identifiers and current Royal Mail 2nd Class postage of £0.91, an impossible one-player full postal takeover would cost only **£318.50** against a **£350 cash prize**, i.e. **109.8901% gross / +£31.50**.

However the live draw limits one person to only **35 / 350 = 10%** of the pool. Even from a zero-sold launch, at least **315 identifiers** must remain outside one player's control. The checked snapshot already had 10 sold. Ticket assignment is random after validation, postal receipt is not atomic/reservable, sold-out arrivals are not accepted, and LLF reserves discretion to refuse entries.

Therefore a legal external-winning outcome necessarily remains and the strict one-player guaranteed cash floor is **£0**.

H326 is closed despite crossing 100% under impossible full ownership.

## Files

- `research/h326_llf_postal_takeover_bound.md`
- `research/H326_VALIDATION.md`
- `src/loto_research/h326_llf_postal_takeover_bound.py`
- `data/derived/h326_llf_postal_takeover_bound.json`

## H225 lane

`H225-X*` remains **CLOSED / EXHAUSTED** at X20 with 0 coefficient survivors / 0 legal shift tuples. Do not create X21/X22 from the unchanged family.

## NEXT ACTION

Prioritize another finite subsidized/free-entry pool that already passes the H326 economics gate **and** has `max_per_player >= takeover size`, ideally with electronic/atomic reservation. The strongest target is a fresh zero-sold pool with deterministic player-facing cash liabilities above exact discounted acquisition cost. Do not reopen H326 unless the person cap or reservation mechanics materially change.
