# H339 — Goldie Lucks current `Every Other Ticket Wins!` + free-phone route gate

Date checked: 2026-08-28

## Goal
Test a genuinely new acquisition mechanism after H334-H338: a binding free **telephone** entry route that can avoid postage and mail-loss costs, while also screening the current Goldie Lucks `Every Other Ticket Wins!` candidate.

## Current draw facts
Current search/operator evidence advertises:
- 37,500 total tickets;
- 18,750 instant winners;
- £2.50 paid ticket price;
- £1,000 end prize;
- close date 2026-08-31.

Therefore the instant layer has exactly `37,500 - 18,750 = 18,750` ticket IDs with no instant prize. This is a 50% zero-instant support.

## Entry-route rules
Goldie Lucks T&Cs state that free telephone entry is available only to raffles with less than four days between launch and closing and carrying a Quick Draw tag. A random ticket number is allocated to a qualifying call and emailed to the entrant. Raffles with a longer time-span must use the free postal route.

The current `Every Other Ticket Wins!` page was indexed/live more than four days before its 2026-08-31 close, so it cannot satisfy the `<4 day` phone-entry condition. Its free route is therefore postal under the published rule.

The postal schedule assigns one Entry Number per received postcard. Current UK 2nd Class standard-letter postage is £0.91.

## Exact single-entry bound
Because 18,750 legal IDs have no instant prize, one valid postal entry can legally be allocated to such an ID. On that branch:

`instant withdrawable cash = £0`

`postage cost = £0.91`

`instant-layer net <= -£0.91`

This bound is stronger after adding postcard/material/labour costs. It is independent of which of the 18,750 zero-instant IDs is received.

The £1,000 end prize does not create a per-entry guaranteed floor because a single entry can legally lose the end draw.

## What is and is not closed
Closed with zero arithmetic inconclusive:
- single postal-entry guaranteed-profit attempt on the current draw;
- any claim that `Every Other Ticket Wins` alone implies a positive per-ID cash floor.

Not yet closed:
- every possible large multi-entry portfolio, because this pass did not recover the complete instant-prize amount vector and exact entrant cap from the live page.

## New lane unlocked
The operator's Quick Draw phone route is genuinely different from H334-H338. If a live `<4 day` Quick Draw has an all-cash every-ID instant layer, a phone call could remove both the £0.91 postal acquisition cost and postal non-receipt branch. The rigorous screen is:

1. verify Quick Draw tag and `<4 day` launch-to-close interval;
2. verify telephone route is binding and assigns an Entry Number;
3. recover exact total ID count and all cash-prize counts;
4. verify `zero-withdrawable-cash support = 0`, or solve the exact worst-case allocation for the allowed number of calls;
5. subtract any unavoidable telephone marginal charge;
6. reject if discretionary anti-abuse/substitution terms preserve a legal zero-cash branch.

## Sources
- Goldie Lucks live site/search: https://www.goldieluckscompetitions.co.uk/
- Goldie Lucks T&Cs: https://www.goldieluckscompetitions.co.uk/terms-conditions
- Current draw index: https://www.competitionshowroom.com/competition/goldielucks-every-other-ticket-wins
- 2026 UK postage cross-check: https://postofficehours.co.uk/postage-rates

## Result
**NO SUCCESS.** New exact checkpoint obtained and a lower-friction phone-entry mechanism identified for the next live-candidate search.
