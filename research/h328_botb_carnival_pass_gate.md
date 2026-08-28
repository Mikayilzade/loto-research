# H328 — BOTB Carnival Extravaganza × BOTB Pass subsidy gate

Date: 2026-08-28
State: CLOSED / RANDOM-ALLOCATION ZERO-SUPPORT BLOCKED
Global state: NO SUCCESS; NOT EXHAUSTED

## Question
Could the current BOTB Pass discount/subscription mechanism turn a current finite Instant Wins pool into a strict guaranteed-profit construction?

## Current live witness
BOTB's current `Carnival Extravaganza` page (checked 2026-08-28) publishes:
- online ticket price: £1.29;
- maximum identifier universe: 999,999 tickets;
- instant prizes already won: 4,761;
- instant prizes left: 195,204;
- hence published instant-prize identifiers represented by the snapshot: 199,965;
- advertised instant-prize pool: over £500,000;
- separate end prize: £2,000 cash;
- ticket numbers are randomly generated after checkout.

Sources:
- https://www.botb.com/prizes/instantwin
- https://support.botb.com/hc/en-gb/articles/32649573626898-How-to-use-BOTB-Pass-tickets
- https://www.botb.com/win
- secondary plan-detail cross-check: https://radubucur.com/botb-pass.html

## Exact zero-support gate
Using the page's finite identifier universe and current instant-prize counts:

`999,999 - (4,761 + 195,204) = 800,034`

So the universe contains 800,034 identifiers that are not represented by an instant prize in this snapshot.

Because BOTB states that Instant Wins ticket numbers are randomly generated after checkout, a subsidised bundle does not select prize IDs. A strict positive instant-prize floor requires the guaranteed acquired bundle to be larger than the entire zero-prize support. Therefore the necessary forcing condition is:

`subsidised_bundle_size > 800,034`.

The documented BOTB Pass product is nowhere near that scale. As an intentionally player-favourable stress test, H328 grants the old/publicly documented Ultimate configuration all 209 monthly entries as if every one could be redirected into this one Instant Wins pool (the actual documented Instant-Win allocation was only 15). Even this impossible stronger grant satisfies:

`209 <= 800,034`.

Hence there is a legal allocation in which every subsidised ticket receives a zero-instant identifier. The £2,000 end draw does not create a positive worst-case floor because a portfolio this small leaves external eligible identifiers.

Result under the favourable 209-ticket stress: strict withdrawable-cash floor = £0.

## Independent full-pool economics check
Even ignoring execution and granting impossible complete paid ownership from inception:

- full paid cost = `999,999 × £1.29 = £1,289,998.71`;
- advertised instant prize value + end prize <= player-favourable `£500,000 + £2,000 = £502,000` lower advertised headline basis (the operator says 'over £500k'; this arithmetic is only a sanity screen, not the closure proof);
- headline ratio at £502,000 = 38.9148%.

The rigorous H328 closure does NOT depend on the headline-value ratio; it depends on the exact zero-support/random-allocation witness above.

## Validation
Assertions reproduced by `src/loto_research/h328_botb_carnival_pass_gate.py`:
- prize identifiers = 199,965;
- zero-instant identifiers = 800,034;
- zero support >= 209;
- zero support >= 15;
- legal all-zero-instant allocation exists for the favourable 209-ticket subsidy stress;
- therefore instant-prize guaranteed cash floor is zero;
- end-draw floor is zero while external identifiers remain.

## Closure scope
H328 closes the current Carnival × documented BOTB Pass finite-subsidy route. It does not claim all future BOTB Instant Wins are closed. Reopen only if a future deterministic/subsidised bundle can force acquisition of more than the complete remaining zero-cash support, or BOTB exposes selectable/reservable prize-bearing identifiers before purchase.

## NEXT ACTION
Search for a genuinely different live finite pool where either:
1. discounted/free guaranteed acquisition exceeds all remaining zero-cash support; or
2. prize-bearing identifiers are selectable and atomically reserved before payment; or
3. every possible allocated identifier has a positive withdrawable-cash floor whose minimum exceeds effective subsidised acquisition cost.
