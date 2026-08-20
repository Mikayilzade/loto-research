# H125 — fixed-board raffle near-threshold calibration

Updated: 2026-08-20
Status: **MONITOR CLASS STRENGTHENED / NO TERMINAL GUARANTEE / NO CURRENT POSITIVE LIVE STATE**

## Goal
Extend H122/H123 with fresh fixed-board raffle controls that can be screened in one line before any deeper work:

`break_even_eligible_denominator N* = guaranteed cash-value prize board / ticket price`.

If a deadline draw awards the fixed board among the tickets actually sold, a late entrant has positive pre-tax EV only when the eligible sold-ticket denominator is below `N*`. This remains expected value, not a guarantee, unless the purchased portfolio itself has a strictly positive minimum payout in every legal draw outcome.

## Case A — Jersey Hospice Care Million Pound Lottery 2026

### Verified 2026 facts
The 2026 draw was scheduled for 31 July 2026. Published draw information gives:
- ticket price: **£300**;
- fixed prize board: **£1,300,000**;
- prizes: £1,000,000 + £100,000 + £75,000 + £50,000 + £25,000 + five × £10,000;
- permit: Jersey Gambling Commission `CP-2643-26`.

A Jersey Hospice Care social update indexed in July 2026 stated **only 2,500 tickets remaining**.

Sources:
- Association of Jersey Charities / 2026 draw listing: https://www.jerseycharities.org/diary/3039/million-pound-lottery-draw
- Channel 103 / 2026 draw listing: https://www.channel103.com/local/events/event/million-pound-lottery-draw/
- Jersey Hospice Care LinkedIn company feed (indexed post with 2,500 remaining): https://www.linkedin.com/company/jersey-hospice-care

### Cap uncertainty
A directly crawlable 2026 source stating the total issued-ticket cap was not recovered in this packet. However, the immediately preceding architecture is strongly anchored at **7,000 tickets**:
- ITV reported 7,000 available each year for the 2023 edition;
- 2025 launch coverage states only 7,000 tickets were available;
- 2021 reported 7,000 sold.

Controls:
- https://www.itv.com/news/channel/2023-05-15/tickets-go-on-sale-for-jersey-hospice-cares-million-pound-lottery
- https://channeleye.media/jersey-hospice-care-launches-2025-million-pound-lottery/
- https://jerseyeveningpost.com/news/2021/09/03/million-pound-lottery-numbers-are-drawn/

Therefore the 7,000-cap calculation below is explicitly a **continuity sensitivity**, not a claimed verified 2026 cap.

### Exact threshold
With `B = £1,300,000` and `p = £300`:

`N* = B / p = 4,333.333... sold tickets`.

Under a 7,000-ticket cap, `2,500 remaining` implies `4,500 sold`.

Then:
- EV/ticket = `£1,300,000 / 4,500 = £288.8889`;
- gross return = **96.2963%**;
- pre-tax expected ROI = **-3.7037%**.

So this was a **near-threshold miss**. It is much closer than most fixed-board raffles checked in H118/H121/H123, but not positive on the 7,000-cap sensitivity.

The edge would appear only below 4,334 eligible sold tickets. Under a 7,000 cap that means more than 2,666 tickets remaining. Thus an earlier state around **>=2,667 remaining** would cross the pre-tax EV threshold if the full fixed board were guaranteed at the deadline and only sold tickets were in the draw.

### Why no guarantee
Even below the EV threshold, one ticket or any incomplete portfolio can legally lose. Terminal SUCCESS would require either:
1. complete eligible ownership at cost below the guaranteed board; or
2. a rule-guaranteed minimum allocation to our purchased block that exceeds its cost.

Neither is established here.

## Case B — Minnesota Millionaire Raffle 2026

Official Minnesota Lottery rules/pages give:
- **1,000,000 tickets**;
- **$10** each;
- exact 20,000-prize board;
- sold out in 14 days, on 3 Nov 2025.

Prize board:
- 2 × $1,000,000
- 5 × $100,000
- 5 × $50,000
- 5 × $25,000
- 40 × $20,000
- 10 × $10,000
- 100 × $500
- 150 × $200
- 6,200 × $100
- 13,483 × $50

Exact board value = **$5,149,150**.

Therefore:
- `N* = 5,149,150 / 10 = 514,915 tickets`;
- sellout spend = **$10,000,000**;
- sellout gross return = **51.4915%**.

The raffle sold out extremely early, so no undersubscribed late-entry state existed. This is a clean negative control showing that a large fixed board is irrelevant when demand rapidly pushes the denominator far above break-even.

Primary sources:
- Minnesota Lottery 2026 raffle page: https://www.mnlottery.com/games/raffle/raffle-2026
- launch/prize schedule: https://www.mnlottery.com/news-release-raffle-returns-oct-21-with-exciting-changes

## Case C — Michigan online raffle architecture

Michigan Lottery's current FAQ confirms a reusable architecture:
- limited ticket supply;
- fixed ticket cost;
- predetermined prizes;
- draw either after sellout **or at a predetermined date/time**;
- winners selected from tickets sold.

This is exactly the architecture H122/H123 monitor wants, because deadline-type products can become +EV if demand undershoots the fixed board enough.

Current FAQ sources:
- https://faq.michiganlottery.com/online-games-information-286703b2/online-raffles-faq-c254e42f/online-raffles-overview-189c4315
- https://faq.michiganlottery.com/online-games-information-286703b2/online-raffles-faq-c254e42f/viewing-my-online-raffle-tickets-2e2c9e85

No crawlable active Michigan raffle with a current sold/remaining count and prize board was recovered in this packet, so no live EV claim is made.

## Monitor rule after H125
For every candidate, stop early unless all of the following are available:
1. fixed/published prize-board value `B`;
2. ticket price `p`;
3. deadline draw from actual sold entries (or another rule that preserves the board under undersubscription);
4. observable sold count or tickets remaining;
5. late purchases remain eligible for the full relevant board.

Compute `N* = B/p` first. Only candidates materially below the tax/cost-adjusted threshold deserve deeper execution research.

## Result
H125 does not produce SUCCESS. It strengthens the monitor class with:
- a **near-break-even historical/current-season control** (Jersey 2026 sensitivity: ~96.30% gross at the indexed 2,500-remaining state under the recent 7,000-ticket architecture);
- a **high-demand negative control** (Minnesota 2026: 51.4915% sellout gross, sold out in 14 days);
- a **current reusable deadline-or-sellout architecture** (Michigan online raffles) awaiting a live measurable state.

The most valuable next move remains a live official raffle whose observable denominator is materially below its fixed-board break-even threshold before sales close.
