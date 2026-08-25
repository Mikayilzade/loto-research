# H271 STATUS

Updated: 2026-08-25
Terminal state for packet: **CLOSED / REJECTED**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Result

H271 screened UK EuroMillions Millionaire Maker as a candidate external-subsidy / finite-identifier takeover. It is genuinely attractive structurally because every UK EuroMillions entry automatically receives a raffle number and the raffle guarantees a £1,000,000 winner.

The strict guarantee fails at identifier control. Raffle numbers are automatically generated for sold entries and the winning number is selected from those generated participating numbers. If even one valid code belongs to an outside player, that code is itself a legal winning outcome and our portfolio receives £0 from Millionaire Maker. The checked rules provide no way to choose, reserve, or pre-buy every future generated code while public sales remain open.

Exact arithmetic gives the secondary gate:
- £2.50 current line price;
- £1,000,000 ordinary raffle prize;
- raffle-only break-even at **400,000** paid lines and strict-positive ceiling **399,999**;
- `C(50,5)*C(12,2) = 139,838,160` EuroMillions main outcomes;
- one-copy main-space cover costs **£349,595,400**;
- one £1m raffle prize is only **0.2860449537%** of that cost.

Thus ordinary main-number coverage cannot substitute for a code takeover, and a code takeover is not certifiably executable under the checked issuance rules.

Files:
- `research/h271_uk_millionaire_maker_takeover_bound.md`
- `research/H271_VALIDATION.md`
- `src/loto_research/h271_uk_millionaire_maker_takeover_bound.py`
- `data/derived/h271_uk_millionaire_maker_takeover_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H271_APPEND.md`

## NEXT ACTION

Continue outside the closed H225 family. Prefer a guaranteed-winner or external-subsidy mechanism where identifiers are not merely unique, but **hard-capped and player-reservable/monopolizable before draw close**. A second priority is a promotion that adds a fixed payout to every winning selection independently of external duplicate ownership. Do not reopen ordinary UK Millionaire Maker unless issuance/reservation rules materially change.
