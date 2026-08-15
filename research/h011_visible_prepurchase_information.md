# H011 — lawful visible pre-purchase information leakage

Updated: 2026-08-15
Status: **no executable deterministic pre-purchase ticket-decoding edge validated; ordinary visible scratch-ticket channels rejected; new H018 time-state lead opened**

## Goal
Find information that is lawfully observable **before committing to purchase** and causally predicts a specific ticket/play payout strongly enough to create a guaranteed or materially positive selection edge.

The key distinction is between:
- information visible before purchase;
- information obtainable only after purchase/activation;
- game-level statistics that do not identify a specific unsold ticket;
- post-purchase validation data.

## Screened channel 1 — exposed serial/barcode on physical scratch tickets
### New York
Official NY Lottery NYL+ material states that a Scratch-Off has:
- a 14-digit serial number on the back; and
- a separate 14-digit `SCRATCH TO CASH` number **under the scratch-off portion**.

Official claim material also says validation codes must match Lottery computer records.

Implication: the publicly exposed serial is not documented as a prize decoder; a second validation credential is intentionally hidden under the play area. No lawful official interface was found that maps the visible back serial alone to prize status before purchase.

Sources:
- https://nylottery.ny.gov/ht/page/nyl-plus-procedures
- https://nylottery.ny.gov/how-to-claim/

Status: **REJECTED as validated pre-purchase decoder**.

### Virginia
Virginia Lottery Rewards explicitly describes retail flow as `BUY. PLAY. SCAN. CLAIM` and says retail points come from **purchasing** a game and then scanning the barcode. It also states that scanning an already-owned but unplayed Scratcher can notify the player whether it is a winner or nonwinner.

This is important: post-purchase barcode validation can reveal the outcome before the latex is manually played. But official material does **not** authorize or document scanning unsold retailer inventory to decide whether to buy it. The purchase-first wording makes this unusable as a lawful pre-purchase edge under project rules.

Source:
- https://www.valottery.com/rewards/faq

Status: **POST-PURCHASE INFORMATION ONLY; REJECTED for H011 terminal use**.

## Screened channel 2 — public remaining-prize tables
New York and Virginia publish remaining/unclaimed prize counts for scratch games.

Examples:
- New York scratch game pages show prizes remaining/paid out and inception odds.
- Virginia game pages show `Winning Tickets At Start` and `Winning Tickets Unclaimed`.

These data are game-level states. They do not identify which unsold physical ticket contains a prize. Without a reliable remaining-unsold-ticket denominator and ticket-location mapping, they can support conditional EV estimation but not deterministic ticket selection.

New York additionally states for current scratch-off pages that prizes are randomly distributed in the game and tickets may continue to be sold after top prizes are claimed.

Sources:
- https://nylottery.ny.gov/scratch-off-games/
- https://nylottery.ny.gov/scratch-off-game?game=1684
- https://www.valottery.com/data/scratcher-games/2399-life-of-luxury

Status: **NO TICKET-SPECIFIC LEAK; merges conceptually with H010 remaining-inventory problem**.

## Screened channel 3 — pack/ticket position, visible numbering, retailer location
No current official mapping was found from pack position / exposed ticket number / retailer location to prize outcome. In particular, the current New York game material explicitly describes prizes as randomly distributed.

Historical anecdotes or reverse-engineered printing weaknesses are not enough under project rules; H011 requires a current causal mechanism and forward validation.

Status: **NO CURRENT VALIDATED CHANNEL**.

## Screened channel 4 — online instant-game visible state
For ordinary online instant games, outcome information is generated/committed as part of the paid play. Virginia terms say choosing `Play Now` elects to purchase and deducts the game value; the game becomes complete when outcome status identifies whether a prize was won. Demo outcomes do not award prizes.

Source:
- https://www.valottery.com/termsandconditions

Status: **NO ORDINARY PRE-PURCHASE OUTCOME LEAK VALIDATED**.

# NEW LEAD — H018 Virginia Lucky Contestant time-state jackpot
During H011 screening, a materially different mechanism was found.

Virginia Lottery's current `Lucky Contestant` online game states:
- daily jackpot is guaranteed to be won each day;
- each day a target time is randomly selected from a published weighted time distribution;
- jackpot odds improve as that hidden selected time approaches;
- at 60 minutes before selected time: jackpot odds `1 in 150,000`;
- at 30 minutes before selected time: `1 in 30,000`;
- **at the selected time: `1 in 1`**;
- jackpot may also be won earlier according to standard odds;
- plays cost $0.20–$30.

Published selected-time weight buckets:
- 01:00–02:00: 10%
- 02:00–08:00: 10%
- 08:00–14:00: 10%
- 14:00–18:00: 10%
- 18:00–20:00: 15%
- 20:00–21:00: 15%
- 21:00–22:00: 15%
- 22:00–23:45: 15%.

Primary source:
- https://www.valottery.com/lotteryonline/3850

## Why this is different
This is a **causal, operator-published nonstationary probability mechanism**, not a hot/cold-number pattern. The hidden target time prevents immediate deterministic exploitation, but public time of day + whether the daily jackpot is still alive can potentially create a Bayesian state signal.

The key future question is not predicting random symbols. It is:

`P(target time is near now | jackpot has survived until now, published target-time prior, earlier-play hazard)`

and whether expected jackpot value per wager can cross ticket cost in any observable survival/time state.

## Why it is not SUCCESS yet
- exact selected time is hidden;
- the jackpot can be won before target time;
- other-player wager intensity/hazard is unknown;
- we need exact mechanics for wager-size scaling of jackpot probability/payout;
- purchase latency and jackpot-state synchronization matter;
- even if +EV exists, a strict all-outcome guaranteed-profit strategy would require a stronger hedge/coverage construction.

H018 therefore opens as a **high-priority state-dependent EV/possible arbitrage lead**, not a guarantee claim.

# H011 conclusion
No current lawful deterministic visible-ticket decoder was validated in the screened NY/Virginia physical scratch channels.

H011 standalone guarantee status: **REJECTED on currently evidenced channels**.

The important output of this packet is the new H018 time-state mechanism, which should be quantified next before broad blind RNG testing.
