# H307 STATUS — Salexmo published instant-win numbers / random-allocation blocker

Updated: 2026-08-27
Branch: `research-work`
State: **CLOSED / TARGETING-BLOCKED**

## Candidate
Salexmo `£300 CASH FOR 3P, PLUS CASH INSTANT WINS 11/9/26` is a finite 40,000-entry competition priced at £0.03 per paid ticket. The live competition page publishes the remaining £30 instant-win ticket numbers and labels them `Available!`, while also advertising `Choose Your Tickets!`.

At the checked snapshot:
- 5,583 / 40,000 entries sold;
- 34,417 entries remaining;
- 9 / 10 £30 instant wins remained;
- maximum 10,000 tickets per user;
- paid ticket price £0.03;
- postal entries receive 29 tickets and are eligible for instant prizes.

If the player could select one of the published available instant-win identifiers, a £0.03 -> £30 deterministic purchase would be an immediate strict-profit construction. Therefore H307 tested the allocation rule rather than ordinary expected value.

## Governing rule blocker
Salexmo Terms §4.1(B) explicitly states that all entrants meeting the entry requirements are **randomly allocated an entry number on completion and payment**; the same method is used for free-route entrants. An instant prize is won only if the randomly allocated entry number equals the published instant-win number.

Therefore `Choose Your Tickets!` cannot be treated as proof that a player can choose a specific numerical identifier. The page itself also says ticket number(s) are shown only after the order is confirmed.

## Exact worst-case bound
At the checked snapshot there are at least:

`34,417 remaining entries - 9 remaining instant IDs = 34,408 non-instant remaining IDs`.

Since the per-user cap is only 10,000, a legal random allocation exists in which **all 10,000 player entries are non-instant**. The main draw also has legal external-winning outcomes because the player cannot control the entire 40,000-entry pool and 5,583 entries were already sold.

Hence the strict withdrawable-cash floor of any permitted H307 portfolio is **£0**. Published visible instant-win identifiers do not create a targetable arbitrage under the governing random-allocation rule.

## Terminal conclusion
**H307 is CLOSED / TARGETING-BLOCKED.** Do not reopen merely because a Salexmo page shows unclaimed instant-win numbers. Reopen only if a binding/current rule or actual checkout mechanism proves that the player can select and reserve the exact numerical identifier before payment, contrary to the checked random-allocation terms.

## NEXT ACTION
Continue outside H225-X* with a genuinely targetable finite-inventory mechanism: exact winning identifiers/prize-bearing assets must be selectable or reservable **before** payment, not randomly allocated after purchase.
