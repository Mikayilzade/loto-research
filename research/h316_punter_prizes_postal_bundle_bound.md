# H316 — Punter Prizes postal-bundle no-subsidy bound

Status: **CLOSED / NO STRICT GUARANTEED PROFIT**

Snapshot: 2026-08-27, current `CASH DASH 3` competition.

## Why this was worth testing

Punter Prizes has an unusual free-entry rule: if a competition ticket costs less than second-class postage, one separately posted entry can be credited with multiple competition entries, up to the value of the postage. That looks superficially like a deterministic subsidy and therefore deserved a strict takeover calculation rather than an EV estimate.

The live CASH DASH 3 page was especially attractive because it calls itself a **no margin competition** and publishes a finite pool of 20,000 tickets at £0.10, with ten £100 cash instant wins and ten £100 ticket bundles, and no end prize.

## Current official/live facts used

Live Punter Prizes page on 2026-08-27:
- ticket price: £0.10;
- ticket limit: 20,000;
- 1,811 sold / 18,189 remaining at snapshot;
- 10 × £100 cash + 10 × £100 ticket bundles;
- two of those 20 instant prizes were already claimed, leaving 9 cash + 9 bundle prizes;
- no end prize;
- postal route credits multiple entries only up to second-class-postage value;
- each postal entry must be in a separate envelope;
- late entries are rejected;
- if paid entries fill a cap before a postal entry is received, the postal entry is not included;
- promoter does not acknowledge receipt or pre-confirm correctness.

Royal Mail's current 2nd Class letter price is £0.91.

## Exact full-pool arithmetic

Paid full takeover, under an impossible favourable assumption that a single player can acquire all 20,000 identifiers:

- cost = 20,000 × £0.10 = **£2,000**;
- total advertised face value = 10 × £100 cash + 10 × £100 bundles = **£2,000**;
- return = **100.0000%**.

This is at best break-even, not strict profit. The calculation also deliberately values the ticket bundles at their full £100 face value rather than imposing any cash-conversion haircut.

### Postal bundling

At £0.91 postage and £0.10 per competition entry, the stated `up to postage value` rule can credit at most:

`floor(0.91 / 0.10) = 9 entries per posted letter`.

Therefore a hypothetical full postal takeover requires:

- `ceil(20,000 / 9) = 2,223` separately posted letters;
- postage = `2,223 × £0.91 = £2,022.93`;
- face-value return = `£2,000 / £2,022.93 = 98.8665%`.

So this postal bundling is **not a discount below the paid-entry price**. The floor operation guarantees effective postage cost per credited entry is at least the ticket price (except exact divisibility, where it can only equal it).

## Current remaining-pool stress

At the live snapshot, 1,811 tickets and two £100 prizes had already gone. Even granting ownership of every remaining ticket and treating the nine remaining ticket bundles at full face value:

- remaining prize face = **£1,800**;
- paid cost of all 18,189 remaining tickets = **£1,818.90**;
- paid return = **98.9609%**;
- postal letters required = `ceil(18,189/9)=2,021`;
- postage = **£1,839.11**;
- postal return = **97.8734%**.

Thus the live residual inventory is already arithmetically below break-even even before execution risk.

## Reusable theorem from H316

For a ticket price `p` below postage `s`, if the promoter credits at most `floor(s/p)` entries per separately-posted item, then the postage cost per credited entry satisfies

`s / floor(s/p) >= p`.

Therefore this form of postal bundling can never create a strict per-entry acquisition discount relative to paying the ticket price. It can only equal or exceed the paid acquisition cost. A positive takeover would still require the underlying finite pool itself to have liabilities strictly above paid full-pool cost.

## Execution blockers (independent of arithmetic)

Even if the economics were positive, current CASH DASH 3 cannot be turned into a rigorous takeover from this snapshot because external tickets already exist. The postal route is also non-atomic: receipt is not guaranteed, entries can lose the race against paid sales, and acceptance is known only after processing.

## Conclusion

**H316 CLOSED.** The Punter Prizes multi-entry postal rule is not the electronic/free subsidy sought by the current research lane. CASH DASH 3 itself is exactly break-even under impossible full paid ownership and below break-even through the postal route; the current residual pool is below break-even by either route.

Do not reopen this exact mechanism unless either:
1. a competition publishes deterministic player-facing liabilities strictly greater than its exact paid full-pool cost, or
2. the free-entry rule changes so that one postal/electronic action receives more entries than the monetary value of its acquisition cost, with deterministic reservation/acceptance.

Reproducible files:
- `src/loto_research/h316_punter_prizes_postal_bundle_bound.py`
- `data/derived/h316_punter_prizes_postal_bundle_bound.json`
