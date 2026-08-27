# H314 checked-project append

## WinWink £50k COIN FLIP — 2026-08-27 live snapshot

Result: **CLOSED / CAP-BLOCKED / ZERO STRICT CASH FLOOR**.

Checked mechanism:
- finite pool of 142,857 ticket positions;
- 71,428 instant-win positions cryptographically precommitted before sales;
- £1 entry;
- maximum 21,429 entries per person;
- winning positions sealed/unreadable before purchase.

Fresh snapshot:
- 1,615 sold;
- 70,598 instant wins remaining;
- therefore 70,644 losing positions remain.

Strict test:
`remaining losing positions (70,644) >= player cap (21,429)`.

Hence a legal allocation exists where every ticket permitted to one player is non-winning, so the guaranteed cash floor is £0. The advertised 1-in-2 hit rate is irrelevant to a strict guarantee under this cap.

Source:
- https://winwink.co.uk/competitions/50k-coin-flip

Reusable gate learned:
For hidden/precommitted instant-win positions, reject immediately whenever the player's maximum controllable inventory does not exceed the remaining losing inventory. Reopen only if prize-bearing identifiers become selectable/reservable before payment or the acquisition cap is large enough to eliminate every losing identifier.
