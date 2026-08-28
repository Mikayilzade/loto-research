# H326 — LLF Games £350 cash postal-route takeover bound

Date checked: 2026-08-28
State: **CLOSED / CAP-AND-EXECUTION-BLOCKED**

## Why this was worth opening

H325's NEXT ACTION asked for a finite pool where acquisition can be cheaper than the normal ticket price and deterministic liabilities can exceed exact acquisition cost. The live recurring LLF Games **Win £350 Cash For £1.99!** draw is a genuine near-miss because LLF offers a free postal entry route and current Royal Mail 2nd Class postage is only **£0.91**.

This is materially different from ordinary undersold-draw screening: under an impossible full postal takeover, the economics actually cross 100%.

## Current draw snapshot

Operator page checked for the draw closing **2 September 2026**:
- 350 total tickets;
- £1.99 paid online entry;
- £350 cash prize;
- max 35 entries per person;
- snapshot 10 / 350 sold;
- draw stated to happen regardless of sellout;
- ticket numbers are allocated randomly.

Source: https://llfgames.com/competition/win-350-cash-for-1-99-56/

LLF's governing terms on the same page state:
- one free postal entry per postcard;
- a valid postal entry is allocated a random number from those still available;
- free and paid entries are subject to the same competition limits;
- entries arriving after sellout are not counted;
- the company may refuse an entrant's entry at its discretion.

Current Royal Mail 2nd Class standard-letter/postcard postage is **£0.91**.
Source: https://www.royalmail.com/sending/uk/2nd-class

## Exact economics

### Impossible full paid takeover

350 × £1.99 = **£696.50** cost.

£350 / £696.50 = **50.2512563% gross**.

No positive result.

### Impossible full postal takeover

350 × £0.91 = **£318.50** postage cost.

£350 / £318.50 = **109.8901099% gross**.

Nominal deterministic surplus if all 350 identifiers could be controlled by one eligible player: **£31.50**.

This is a real arithmetic crossing of the target threshold, not an EV argument.

### Snapshot residual fantasy bound

With 10 sold, 340 remain. If one player could impossibly acquire every remaining identifier by valid second-class postal entries:

340 × £0.91 = **£309.40**.

£350 / £309.40 = **113.1221719% gross**, nominal surplus **£40.60**.

But this still does not create a guarantee because the already sold identifiers remain possible winners.

## Rigorous blocker

The per-person cap is only **35 / 350 = 10%** of the full pool.

Even from a hypothetical pristine 0-sold launch, one eligible player must leave at least:

350 − 35 = **315 uncontrolled identifiers**.

For a one-winner random draw, any one uncontrolled valid identifier preserves a legal outcome where that identifier wins. Therefore the actual strict one-player cash floor is **£0**.

At the checked snapshot, the 10 already sold tickets further strengthen the blocker, but they are not even needed: the cap alone is terminal for a one-player full-support guarantee.

Postal execution also is not atomic or reservable. Entries must physically arrive, are assigned randomly only after validation, can lose the race to sellout, and LLF reserves discretion to refuse entries. So the positive full-postal arithmetic cannot be converted into a rigorous executable takeover.

## Reusable result

A postal-route finite pool can have **liability > full postal acquisition cost** and still be useless for strict guarantee if `max_per_person < total_winning_support`.

For a single-winner draw, the structural gate must be checked before celebrating favourable postal economics:

1. `max_per_person >= number_of_identifiers_needed_to_eliminate_all_external_winners`;
2. entry acceptance/reservation must be sufficiently deterministic;
3. only then compare prize liability to exact acquisition cost.

H326 passes the economics gate under an impossible full takeover but fails gates 1 and 2.

## Reproducibility

- `src/loto_research/h326_llf_postal_takeover_bound.py`
- `data/derived/h326_llf_postal_takeover_bound.json`
- `research/H326_VALIDATION.md`
- `research/H326_STATUS.md`
