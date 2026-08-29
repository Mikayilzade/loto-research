# CODEX NEXT TASK — 29 AUG 2026

Branch: `research-work`
Created from branch head observed before this plan: `db8f2492167a84155480ed5bc18add557bcc5241` (H357).

## Goal
Do NOT immediately create H358.
First repair the project map so the repository again tells the truth about what has already been tested. Then compress the hundreds of results into reusable filters. Only after that, use remaining session time on the strongest still-open mechanism class.

Work through the stages below in order. When a stage is complete, mark it COMPLETE in this file and continue to the next stage without asking the user. Use coherent commits, preferably one commit per stage. Before every write, re-check branch HEAD so parallel work is not overwritten.

H225-X* is terminal. `research/H225_EXACT_STATUS.md` says X20 = 0 coefficient survivors / 0 legal shift tuples after the complete 44-shard / 306,450-state rescreen. Do not create X21/X22 unless the mathematical family itself is deliberately changed.

---

## STAGE 0 — SYNC AND PROTECT
Status: TODO

1. Read:
   - `STATUS.md`
   - `research/H225_EXACT_STATUS.md`
   - newest commits on `research-work`
   - newest numbered H status/result files, at least H340-H357.
2. Confirm the current real HEAD and latest completed H packet.
3. Detect any parallel commits created after this file. Preserve them.
4. Do not rewrite large historical files blindly.

Exit condition:
- current HEAD and latest H packet are known;
- no collision with parallel work.

---

## STAGE 1 — BUILD THE REAL H-PACKET INVENTORY
Status: TODO

The root `STATUS.md` is stale around H268 while the branch has progressed to at least H357. Build a machine-readable inventory rather than fixing this by hand.

1. Enumerate numbered lottery packets from the repository/commit history.
2. For every H packet where evidence exists, record at minimum:
   - H number;
   - name/mechanism;
   - state: CLOSED / OPEN / EVIDENCE-BLOCKED / SUCCESS / EXHAUSTED or closest defensible category;
   - main blocker/result;
   - best guaranteed or favourable ratio if available;
   - key status/report/model files;
   - exact reopening condition when one is known.
3. Treat intentional missing/renumbered H numbers as gaps, not as missing research. Do not invent content.
4. Prefer a small script for reproducibility.

Create/update:
- `tools/build_h_packet_inventory.py` (or equivalent);
- `data/derived/h_packet_inventory.json`;
- `research/H_PACKET_INDEX.md`.

Validation:
- every discovered `H*_STATUS.md` is either represented or explicitly reported as unparsed;
- no duplicate H number silently wins;
- print counts: discovered, parsed, skipped, duplicate/conflict.

Exit condition:
- a reproducible inventory exists and validation counts are explicit.

---

## STAGE 2 — RECONCILE THE PROJECT STATUS
Status: TODO

Repair the stale project-level navigation without deleting historical detail.

1. Update `STATUS.md` so its current checkpoint reflects the actual latest completed H packet and current terminal state.
2. Preserve the H225 closure exactly: CLOSED / EXHAUSTED, no X21/X22.
3. Do NOT paste 90 giant packet summaries into the top of STATUS.
4. Instead point STATUS to `research/H_PACKET_INDEX.md` for the complete inventory.
5. Make the project-level NEXT ACTION filter-based, not "try another random lottery".

Also create a short human-readable checkpoint:
- `research/CURRENT_POSITION.md`

`CURRENT_POSITION.md` must answer in simple language:
- what has been completed;
- what is definitely impossible/closed;
- what kinds of mechanisms remain plausible;
- what the best near-hits were;
- what should be done next.

Exit condition:
- opening `STATUS.md` now leads a new chat/Codex run to the real H357+ state instead of H268.

---

## STAGE 3 — COMPRESS FAILURES INTO REUSABLE FILTERS
Status: TODO

Stop treating each failed game as isolated. Group the research into general blockers/lemmas.

Create:
- `research/MECHANISM_FILTERS.md`
- optionally `data/derived/mechanism_filter_map.json`

At minimum classify evidence into these families when supported:
1. base payout / average-return below cost;
2. jackpot or top-tier dilution by external duplicates;
3. portfolio itself prevents a required no-winner / rolldown condition;
4. per-player cap or already-sold identifiers prevents full control;
5. legal zero-cash outcomes remain in the reachable support;
6. acquisition/acceptance is not guaranteed or atomic (postal loss, operator refusal, etc.);
7. reward is site credit/free play/non-withdrawable rather than cash;
8. deterministic subsidy exists but is too small;
9. channel/eligibility/timing blocks the otherwise-good arithmetic;
10. principal is preserved but minimum profit is still zero.

For every filter provide:
- plain statement;
- when it can reject a candidate cheaply;
- representative H examples;
- what exact condition would defeat the filter.

Important: call something a theorem only where the repository actually proves it. Otherwise label it a rule/filter/empirical blocker.

Exit condition:
- a new candidate can be screened against these filters before expensive exact work.

---

## STAGE 4 — RANK THE NEAR-HITS AND REOPEN CONDITIONS
Status: TODO

Create:
- `research/NEAR_HITS_AND_REOPEN_CONDITIONS.md`

Rank the strongest historical candidates, with special attention to the already observed classes around:
- H332/H334: all-cash or every-ID-positive economics where execution/acceptance killed the guarantee;
- H349/H351/H353: isolated full-cover economics above 100% where external duplicate winners/dilution killed the guarantee;
- H262 and similar finite-identifier jackpot ideas where monopoly/issuance control was the blocker.

Do not reopen them just because they were close. For each, write the ONE material change needed to justify reopening, for example:
- binding zero-cost digital allocation;
- atomic reservation;
- non-dilutable fixed-per-winning-entry subsidy;
- hard cap on external top-tier duplicates;
- exclusive finite identifier ownership;
- new promotion/payout large enough to cross a computed threshold.

Exit condition:
- top near-hits are ranked by how small/realistic the missing condition is.

---

## STAGE 5 — DEFINE THE NEW SEARCH PLAYBOOK
Status: TODO

Create:
- `research/NEXT_SEARCH_PLAYBOOK.md`

The playbook must force cheap rejection before deep analysis.

For each new candidate:
1. identify the external subsidy / finite-control mechanism;
2. ask whether a legal zero-cash branch remains;
3. ask whether external duplicates can dilute the supposed guarantee;
4. ask whether our own portfolio prevents the special branch;
5. ask whether acquisition is binding/atomic/exclusive enough;
6. compute a fast necessary break-even bound;
7. only then run exact combinatorics/full-cover code.

Priority search lanes after consolidation:
A. **All-ID positive withdrawable cash + binding zero/low-cost digital acquisition.**
B. **Special-event/external subsidy with isolated full-cover >100% AND no duplicate dilution.**
C. **Finite unique identifiers where one player can actually reserve/own the full winning support at bounded cost.**
D. **Principal-preserving systems only if there is a binding positive minimum bonus/interest/prize above principal.**

Explicitly deprioritize ordinary jackpot/full-cover, generic Keno/Pick-3, site-credit "Every Ticket Wins", and postal free-entry candidates unless materially new rules defeat an existing filter.

Exit condition:
- future work has a clear decision tree and does not need one H packet per obvious rejection.

---

## STAGE 6 — USE REMAINING SESSION TIME ON THE BEST NEW LEAD
Status: TODO

Only start this stage after Stages 0-5 are COMPLETE.

1. Search current rules/promotions for genuinely new candidates matching lanes A-C first.
2. Do not duplicate any closed H packet.
3. Use the filters to reject weak candidates cheaply without assigning an H number.
4. Create H358 only if a candidate survives the cheap filters and deserves a substantive exact packet.
5. For any created H packet, save model/data/report/validation/status as usual.
6. Never claim SUCCESS unless every legal/execution branch needed for the guarantee is closed.

If no candidate survives, that is acceptable: record the search coverage and stop rather than manufacturing H numbers.

Exit condition:
- either a new substantive H packet is completed, or a documented targeted search found no survivor.

---

## STAGE 7 — FINAL SESSION REPORT
Status: TODO

Create/update:
- `research/CODEX_SESSION_2026-08-29.md`

Keep it understandable to a non-specialist. Include:
- real latest H number;
- approximately how many packet records are inventoried;
- H225 exact-family result in one sentence;
- number of main blocker/filter classes;
- top 3-5 near-hits and what specifically killed each;
- whether any real open candidate remains now;
- the next 3 actions in priority order.

Then update this file so every completed stage says COMPLETE.

Do not restart hourly automation.
Do not enable autonomous tasks.
Do not spend money or perform lottery purchases.

## Final response to user
When all feasible stages are complete, report briefly:
- `CODEX SESSION COMPLETE`;
- stages completed;
- latest HEAD SHA;
- whether a new H packet was created;
- the single most important finding/blocker.
