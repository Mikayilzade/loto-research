# H333 — per-entry postal cash-floor correction to H332

Updated: 2026-08-28
State: **CLOSED AS CURRENT STRATEGY / IMPORTANT POSITIVE ARITHMETIC CANDIDATE**

## Why this packet exists
H332 tested a full 10,000-postcard takeover of Win A Million's historical `Cash Grab`. That was stronger than necessary. If every accepted postal entry has a deterministic cash prize whose minimum exceeds the actual postage cost, then a **single accepted entry** already has positive guaranteed gross and no pool takeover is required.

## Exact arithmetic
Historical Cash Grab published 10,000 tickets and exactly 10,000 cash prizes. The minimum published instant prize was **£1 cash** (9,419 IDs); the other 580 IDs paid at least £2, and 1 ID is accounted for by the remaining higher tiers so the published prize-count vector sums exactly to 10,000. Total published instant cash = **£16,719**.

Royal Mail's current 2026 Second Class letter/postcard price is **£0.91**. Therefore, conditional on one valid postal entry being accepted into this exact prize structure:

- acquisition cost = £0.91;
- deterministic minimum cash payout = £1.00;
- strict gross floor = **£1.00 / £0.91 = 109.8901098901%**;
- strict net floor = **+£0.09 per accepted postal entry**.

This is identifier-independent. Random ticket allocation, external entrants, sharing, and full-pool reservation are irrelevant because every identifier has cash floor >= £1.

## Current rules check
Win A Million Terms updated 7 July 2026 say a valid postal entry:
- must be a separate unenclosed postcard with sufficient first/second-class postage;
- is processed within three working days of receipt;
- is entered into the next qualifying Prize Draw;
- for Instant Wins receives entries equal in value to £1 of paid online entries or the selected game entry price, whichever is higher;
- if received after closing / no tickets remain, may be allocated to the next equivalent Instant Win competition of the same format and prize structure.

However, those current terms post-date the historical Cash Grab close (6 June 2026), and current public tracking shows **0 active Win A Million competitions**. The repository therefore does **not** yet have contemporaneous evidence that this exact £1-minimum all-cash game was governed by the same postal-processing rule while live, nor a currently live equivalent game to execute now.

The terms also reserve account restrictions/closure for excessive or unfair participation. That does not alter the one-entry arithmetic, but it prevents scaling from being treated as unconditionally guaranteed without a live-game entitlement check.

## Validation / zero-inconclusive checks
- Published Cash Grab prize counts: exact sum = 10,000 / 10,000.
- Published Cash Grab instant cash: exact sum = £16,719.
- Minimum cash-bearing identifier = exactly £1.
- Current Second Class postage = exactly £0.91.
- One-entry floor arithmetic has no random variable once acceptance into that prize structure is conditioned.
- **0 arithmetic inconclusive conditions.**
- **1 execution/temporal condition remains unresolved:** no live/current qualifying all-cash game under the verified current postal terms.

## Result
This materially strengthens H332: a full takeover is unnecessary. The correct target is a live postal/free-entry instant-win pool with **minimum withdrawable cash per accepted entry > marginal compliant acquisition cost**.

This packet is **not SUCCESS** because the qualifying Cash Grab is historical and the verified postal rules are later/current; a live equivalent is not presently evidenced.

## NEXT ACTION
Search live/current UK prize competitions for the per-entry inequality directly:
`minimum withdrawable cash on every accepted identifier > compliant postal marginal cost`.
Prioritize games where current terms bind valid postal processing and where the operator cannot substitute into a weaker prize structure. Do not require full-pool takeover if this per-entry floor holds.

Sources checked 2026-08-28:
- Win A Million Cash Grab page (historical, closed)
- Win A Million Terms & Conditions, updated 2026-07-07
- Royal Mail Second Class current pricing
- CompWatch current Win A Million operator snapshot (0 active competitions)
