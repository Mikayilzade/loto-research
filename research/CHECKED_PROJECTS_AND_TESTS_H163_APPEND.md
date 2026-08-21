# H163 audit-ledger append — NJ Green Ball atomicity lower bound

Updated: 2026-08-22
Terminal state after packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H163 NJ Pick-3 Green Ball atomicity** | Can another official Pick-3 bet type compress the forced-state all-outcome cover into one ticket? | Max positive-prize support of any published single Play is Pair = 10 of 1,000 outcomes. Therefore at least **100 Plays** are required; with official max **10 Plays/Ticket**, minimum is **10 Tickets**. Existing 100-Pair construction attains the bound exactly. | **ONE-TICKET COMPRESSION REJECTED / STRUCTURAL MULTI-TICKET BLOCKER VALIDATED**. Public rules still do not guarantee rollback of earlier completed tickets if a later required wager is refused. `research/h163_nj_green_ball_atomicity_lower_bound.md`, `src/loto_research/h163_nj_pick3_support_bound.py`, `data/derived/h163_nj_pick3_support_bound.csv` |

## New evidence preserved
- Current official Pick-3 rules: Ticket max 10 Plays; Straight support 1; 3-way Box/Wheel support <=3; 6-way Box/Wheel <=6; Pair support 10; Pair is therefore support-maximal.
- Exact lower bound: `ceil(1000/10)=100` Plays and `ceil(100/10)=10` Tickets.
- Existing 100 ordered Pair bets are play-count optimal because they partition all 1,000 outcomes into 100 disjoint supports of size 10.
- The second forced Green Ball draw does not allow a one-ticket strict cover; a 10-Play ticket can cover at most 100 outcomes and leaves at least 900 uncovered.
- Current public cancellation language does not establish a guaranteed all-prior-ticket rollback if a later ticket in the required basket fails.
- Self-sale evidence remains strong but no explicit commission-accounting sentence for owner-personal purchase was located.

## Do not repeat without new evidence
Do not retry Pick-3 bet-type compression. Reopen NJ Green Ball atomicity only with one of:
1. official batch/reservation mechanism accepting all required tickets as one transaction;
2. explicit guaranteed rollback of all earlier tickets in a multi-ticket requested basket;
3. new game/promotion whose strict forced-state coverage fits on one ticket/system transaction;
4. explicit official self-sale commission confirmation plus an independent solution to the atomicity gate.
