# Current Research Position

Updated: 2026-08-29

## In plain language
The project has tested hundreds of lottery mechanisms and has reached numbered packet **H357**. It has **not** found a strategy that guarantees positive net profit in every allowed draw and execution outcome. The search is not declared exhausted, because a few tightly specified mechanisms could still work if current rules supply the missing condition.

## What is complete
- The numbered research stream has evidence through H357. The full reproducible map is `research/H_PACKET_INDEX.md` rather than a hand-maintained list.
- The large H225 cyclic-affine construction search is finished. Its exact H225-X20 rescreen found zero surviving coefficient states and zero legal shift tuples.
- Repeated failures now support general pre-screening: prize budgets below cost, shareable jackpots, self-defeating no-winner conditions, uncontrolled identifiers, zero-cash outcomes, non-binding acquisition, non-cash rewards and undersized subsidies can usually be rejected before expensive modelling.

## What is definitely impossible or closed
Under the rules actually tested, the following are closed unless a material condition changes:
1. The unchanged H225-X* family; no X21/X22 is justified.
2. Ordinary full-cover games whose entire player-favourable payout is below acquisition cost.
3. A guarantee based on a shareable jackpot when external duplicate winners are not strictly capped.
4. A rolldown requiring no top-tier winner when the proposed portfolio itself contains a top-tier winner for every draw.
5. A cash-profit claim where a reachable outcome pays only site credit, free play or a non-cash prize.
6. Postal/free-entry constructions where money is spent before acceptance and the rules allow loss, delay, rejection or sellout.

## Best near-hits
- **H334 Audrey Cash Cow:** every identifier paid at least £1 cash and estimated direct postcard cost was below £1, but receipt/acceptance was not guaranteed.
- **H332 Win A Million Cash Grab:** full all-cash arithmetic was 184.824%, but there was no atomic reservation and terms allowed delay, reassignment and anti-exploit action.
- **H349 UK Set For Life Super Chance:** isolated full cover returned 114.168%; three external top-tier duplicates made it lose money.
- **H351 Massachusetts Megabucks:** a high jackpot made isolated coverage strongly positive, but four external jackpot duplicates defeated even a stronger-than-real subsidy bound.
- **H353 NZ Strike:** isolated terminal arithmetic reached 109.657%, but the portfolio prevented the no-winner rolldown and one duplicate was enough to make it lose.
- **H262 LOTTO 6/49 terminal Gold Ball:** terminal jackpot economics could cross cost, but the open, computer-generated identifier pool could not be monopolized.

## What remains plausible
Only narrow structural lanes remain worth priority attention:
- every reachable identifier pays withdrawable cash and allocation is binding, digital and zero/low cost;
- a special-event subsidy is fixed per winning entry or otherwise cannot be diluted by other winners;
- the entire finite winning-identifier support can be reserved atomically and exclusively below its guaranteed cash value;
- a principal-preserving product also binds itself to a strictly positive minimum payment above principal.

These are plausible search classes, not validated opportunities.

## What to do next
1. Turn the repeated blockers into explicit reusable filters and apply them before creating a packet.
2. Rank near-hits by the smallest realistic rule change that would defeat their blocker.
3. Search current rules only in the priority lanes above; create H358 only if a candidate survives every cheap filter and merits exact work.
