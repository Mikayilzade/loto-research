# H304 — Elite Competitions finite-pool cap barrier

Date: 2026-08-27
State: CLOSED / TAKEOVER-BLOCKED

## Goal

Advance the post-H303 search for an electronically confirmed finite draw where one player could monopolize all eligible identifiers and therefore force the prize. This packet screens four current Elite Competitions draws that publish a hard total-entry count, a per-player entry cap, ticket price, and a guaranteed prize.

## Current draws checked

| Draw | Total entries N | Max/player M | Price | Guaranteed advertised prize/cash alternative | M/N |
|---|---:|---:|---:|---:|---:|
| £101,000 Cash | 4,999,999 | 20,000 | £0.05 | £101,000 cash | 0.40000008% |
| £88,000 Cash | 2,999,999 | 12,500 | £0.08 | £88,000 cash | 0.41666681% |
| £1.8m Dream Home & Away bundle | 25,999,999 | 7,500 | £0.19 | £1,250,000 cash alternative | 0.02884615% |
| Time & Tyres Wheel | 5,000,000 | 15,000 | £0.10 | published prize value £190,000; £500 guaranteed end draw | 0.30000000% |

Sources:
- https://www.competitionshowroom.com/competition/elite-competitions-101000-cash
- https://www.competitionshowroom.com/competition/elite-competitions-88000-cash
- https://www.competitionshowroom.com/competition/elite-competitions-18-million-dream-home-away-bundle
- https://www.competitionshowroom.com/competition/elite-competitions-the-time-tyres-wheel

## Exact gate

For a one-winner finite-ID draw, deterministic takeover requires control of every identifier that can be selected. A necessary condition is therefore `M >= N` for one account/person unless rules provide a separate mechanism for reserving the remaining identifiers.

All four live candidates fail this condition by orders of magnitude. The strongest ownership fraction is only 12,500 / 2,999,999 = 0.41666681%.

This is stronger than an EV rejection. Even if the prize is guaranteed and paid in full, there remain millions of legal identifiers that the player is forbidden to own. Any one such external identifier can be selected, yielding zero prize to the candidate portfolio.

## Economics sanity check

The published full-sellout economics are also below 100% for the three ordinary prize draws:
- £101k Cash: £101,000 / (£0.05 × 4,999,999) = 40.40000808%.
- £88k Cash: £88,000 / (£0.08 × 2,999,999) = 36.66667889%.
- Dream Home cash alternative: £1,250,000 / (£0.19 × 25,999,999) = 25.30364470%.

Thus even an impossible waiver of the per-player caps would not make complete paid takeover profitable for those three.

## Conclusion

H304 is closed for strict guaranteed-profit takeover. These current Elite draws do have electronically confirmed tickets and hard finite totals, but the explicit per-player caps prevent deterministic ownership, and the full-sellout economics of the principal prize draws are independently below break-even.

Do not reopen these specific draws unless either the player cap is removed to at least the full remaining inventory or a deterministic discount/free-entry route materially changes the acquisition floor.
