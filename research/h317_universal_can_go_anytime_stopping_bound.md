# H317 — Universal Competitions “Can Go Anytime” stopping-time bound

Date: 2026-08-27
State: **CLOSED / NO SUCCESS**

## Why this mechanism was worth checking

Universal Competitions currently runs a finite-pool format in which an instant prize may be hit before the advertised ticket pool sells out. Once the instant prize is hit, the competition ends and a second jackpot winner is drawn from the entries sold up to that stopping time. This is structurally different from a normal fixed-date raffle because a player who could acquire the entire unsold tail would force the instant trigger before any later external entry could exist.

The live £100 cash version therefore tests whether a stopping-time finite pool can create a deterministic takeover even when ordinary fixed-pool buyouts fail.

## Live rules / snapshot used

The competition page states:
- ticket price: **£0.10**;
- finite pool: **3,999** tickets;
- snapshot sold: **1,135 / 3,999**;
- advertised instant prize: **£100 cash**;
- “Guaranteed Winner” and the competition runs until the instant cash is won;
- when the instant cash is won, the competition is done and a jackpot winner is drawn from all entries sold up to that point;
- ticket numbers are randomly allocated only after an order is placed.

General terms additionally state that online entrants choose a required number of entries and complete checkout/payment, but entries may be limited once the competition maximum is reached. The promoter does not accept responsibility for entries that fail or are delayed, and retains cancellation/amendment/disqualification rights under the published terms.

## Exact player-favourable bound

I intentionally give the player a stronger payout than the page body strictly certifies: count the £100 instant cash **plus a separate full £100 jackpot**, i.e. **£200 total liability**.

Full pool:
- `3,999 × £0.10 = £399.90` acquisition cost;
- favourable maximum liability = **£200**;
- gross ratio = **50.01250313%**.

Current unsold tail:
- remaining tickets = `3,999 - 1,135 = 2,864`;
- full-tail acquisition cost = **£286.40**;
- even if the same player receives both the instant £100 and the full £100 jackpot, maximum gross = **£200**;
- gross ratio = **69.83240223%**;
- deterministic deficit = **£86.40**.

Therefore the stopping-time feature does not rescue the economics. Even an impossible-perfect acquisition of every remaining identifier, with both advertised cash liabilities awarded to us, remains strictly below break-even.

## Structural conclusion

For a stop-on-hit finite competition, define `R` as the remaining ticket count, `p` ticket price, and `L` the total player-facing liability that can be forced once the remaining tail is monopolized. A necessary condition for a strict takeover profit is

`L > R × p`.

H317 fails this gate decisively: `£200 < £286.40`.

This is stronger than an execution rejection. No atomic checkout, reservation, or eligibility assumption can turn this particular live cash pool into guaranteed profit under the checked payout ceiling.

## Reopen condition

Reopen this mechanism only if a live stop-on-hit pool satisfies the exact inequality `forced liability > cost of all currently uncontrolled identifiers`, preferably with electronically reservable entries and no material per-player cap.

Reproducible artifacts:
- `src/loto_research/h317_universal_can_go_anytime_bound.py`
- `data/derived/h317_universal_can_go_anytime_bound.json`
- `research/H317_STATUS.md`
