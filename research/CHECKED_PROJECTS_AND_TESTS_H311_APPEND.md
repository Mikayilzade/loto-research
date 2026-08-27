# CHECKED PROJECTS AND TESTS — H311 APPEND

## H311 — Kilted Lucky Dips finite-pool takeover bound

Checked 2026-08-27.

Mechanism tested: every-ticket-wins finite pool with headline liabilities at/above full face acquisition cost.

Live facts:
- 10,000 tickets;
- £20 each;
- £200,000 stated prize pot;
- separately stated £1,000 cash end prize;
- 499 maximum entries per person;
- random ticket allocation after order;
- 1,215 sold / 8,785 remaining at snapshot.

Strongest arithmetic reading:
- full face cost = £200,000;
- player-favourable liabilities = £201,000;
- nominal full-takeover gross = **100.5%**.

Exact blocker:
- one person may control at most 499 / 10,000 = **4.99%** of identifiers;
- at least 716 already-sold identifiers are external even if the same player hypothetically owned 499 sold entries;
- an external identifier remains a legal end-draw winner;
- complete deterministic takeover is therefore forbidden by the published cap.

Status: **CLOSED / TAKEOVER-BLOCKED**.

Useful forward filter: retain >100% finite-pool economics, but require `max_per_user >= mathematically required identifier set` plus immediate electronic reservation/control.
