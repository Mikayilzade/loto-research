# CHECKED PROJECTS AND TESTS — H310 APPEND

## H310 — Reel Raffle app-exclusive free £1,000 draw

Checked 2026-08-27.

Tested mechanism: zero-price finite cash pool as a possible complete-takeover guarantee.

Live facts used:
- £0.00 entry;
- £1,000 cash prize;
- 99,999 maximum tickets;
- 50 maximum entries per person;
- 10,585 entries already present at snapshot;
- draw closes 27 Sep 2026.

Exact blocker:
- any one player can own at most 50 existing entries;
- at least 10,535 current entries are necessarily external;
- an external ticket is a legal winner;
- therefore worst-case player cash = £0 and strict guaranteed profit fails.

Status: **CLOSED / TAKEOVER-BLOCKED**.

Do not retest the same draw unless the personal cap or inventory state changes in a way that permits complete control of all possible winning entries.
