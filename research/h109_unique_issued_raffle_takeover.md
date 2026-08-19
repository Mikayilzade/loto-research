# H109 — unique-issued-number raffle / guaranteed-winner takeover screen

Updated: 2026-08-19
Status: **CLASS MATERIALLY CLOSED FOR STRICT GUARANTEE / NO SUCCESS**

## Goal
Test whether raffle-style lottery mechanics can solve the main defect of ordinary full-space jackpot coverage: duplicate jackpot sharing.

The attractive structure is a **unique issued number**: only one ticket can hold a given raffle/GPD number, so if the buyer can own every eligible issued number, the top raffle prize cannot be shared with an external duplicate.

This packet tests two distinct forms:
1. fixed finite ticket supply with fixed prize pool;
2. dynamically issued unique-number draws where the winner is selected from all issued entries.

## General theorem
Let:
- `N` = eligible unique raffle tickets/numbers;
- `c` = all-in acquisition cost per ticket;
- `P` = total guaranteed cash prize pool available to the full set;
- `E` = externally held eligible tickets.

### Fixed finite supply
If the buyer can own all `N` tickets, full takeover gross is exactly the sum of all guaranteed prizes `P`.

Strict full-takeover profit requires:

`P > N*c + all execution/tax costs`.

If `P <= N*c`, full takeover is deterministically non-profitable regardless of draw randomness.

For any proper subset of a unique-number raffle, an unowned ticket can be selected for a prize unless the purchased subset itself has a deterministic per-ticket cash floor above cost. Therefore uniqueness removes **duplicate sharing**, but does not remove **selection risk**.

### Dynamic issued-number draw
If each purchase causes a fresh unique number to be issued and the winning number is selected from **all issued entries**, then strict takeover requires `E=0` at draw close. If even one external eligible number exists, there is a legal draw outcome in which that external number wins and the buyer receives zero from the unique-number side.

Thus a buy-the-pot guarantee requires an enforceable mechanism to acquire/own every eligible issued number or to prevent any external issuance. Ordinary open public sale does not provide that lock.

## Screen A — Irish Christmas Millionaire Raffle 2025 control
Official Irish National Lottery information states:
- exactly **600,000 tickets**;
- ticket price **€25**;
- **8,500 guaranteed prizes**;
- total prize value **€6,342,500**;
- official stated prize-fund proportion **42.28%** on sellout.

Full-supply cost:

`600,000 * €25 = €15,000,000`.

Deterministic full-supply gross:

`€6,342,500`.

Deterministic deficit before execution/tax:

`€6,342,500 - €15,000,000 = -€8,657,500`.

Gross-return ratio:

`€6,342,500 / €15,000,000 = 42.2833%`.

Therefore even perfect acquisition of every unique raffle ticket would lock in a large loss. The unique-number property solves sharing, but the operator takeout dominates.

Primary source:
- Irish National Lottery, Millionaire Raffle: https://www.lottery.ie/game-information/millionaire-raffle

Classification: **REJECTED guaranteed-profit full takeover**.

## Screen B — Canada LOTTO 6/49 Gold Ball Draw, current 2026
Current official Canadian/OLG/WCLC rules state:
- every **$3** LOTTO 6/49 play receives a **unique 10-digit Gold Ball Draw Number**;
- one winner is selected at random **from all Gold Ball Draw selections issued** for that draw;
- the selected number wins either **$1,000,000** or the growing Gold Ball jackpot;
- the Gold Ball jackpot starts at $10m and can grow to $68m;
- players cannot choose the Gold Ball number.

Primary sources:
- WCLC current game page: https://www.wclc.com/games/lotto-649.htm
- OLG Gold Ball page: https://www.olg.ca/en/lottery/play-lotto-649-encore/goldball.html

### Why uniqueness is not takeover
The computer issues the unique number **because a play is purchased**. The eligible set is not a fixed publicly purchasable inventory that one buyer can sweep. Any external purchase creates an external eligible number.

With even one external Gold Ball number, there is a legal outcome where that number is selected. The buyer's Gold Ball cash floor is therefore `0` unless the buyer can guarantee ownership of every issued entry at cutoff.

### Stress test: even complete Classic 6/49 coverage does not rescue the zero-Gold-Ball branch
Classic space:

`C(49,6) = 13,983,816` plays.

At $3 per play:

`S = $41,951,448`.

For a complete Classic cover, exact fixed-tier counts include:
- 3/6: `246,820` tickets at $10 = `$2,468,200`;
- 2/6 + Bonus: `172,200` tickets at $5 = `$861,000`;
- 2/6: `1,678,950` Free Plays.

For a deliberately buyer-favorable upper bound in a branch with one external $3 ticket:
- grant full $5m Classic jackpot to our cover;
- grant **the entire** 18.33% Classic Pools Fund to our tickets, despite possible external sharing;
- value every 2/6 Free Play at full $3 face value as though it were immediate cash;
- add all fixed 3/6 and 2/6+Bonus cash.

This optimistic upper bound is approximately:

`$5,000,000 + 18.33%*($41,951,448+$3) + $3,329,200 + $5,036,850`

`= $21,055,750.97`

or only **50.19%** of the $41.951m full-cover spend.

Therefore the legal branch `external Gold Ball number wins -> our Gold Ball payout = 0` is already enough to reject a strict guaranteed-profit construction, even under extremely favorable treatment of every Classic component.

Classification: **UNIQUE-WINNER MECHANISM VALIDATED / STRICT TAKEOVER GUARANTEE REJECTED**.

## Historical control — OLG WINTARIO50
OLG's 2025 WINTARIO50 used randomly issued unique eight-digit numbers and drew 800 winning numbers from the eligible plays issued. It demonstrates the same dynamic-issued-entry architecture: uniqueness prevents duplicate ownership but does not let a player choose or sweep a fixed number inventory.

Official prize pool:
- 100 × $50,000
- 150 × $5,000
- 450 × $500
- 100 × $50

Total fixed prizes: **$5,980,000**.

Source:
- OLG WINTARIO50 Game Conditions: https://www.olg.ca/en/lottery/play-wintario50/wintario50-game-conditions.html

The game is complete and is only retained as a structural control.

## Result
H109 closes an important buy-the-pot sub-class:

1. **Fixed unique-number raffles** are attractive only if total guaranteed prize pool exceeds the all-in cost of acquiring the entire fixed supply. The Irish control is far below this threshold at 42.28%.
2. **Dynamic unique-number guaranteed-winner draws** eliminate prize sharing but create an ownership problem: an external issued entry creates a legal zero-payout branch for the buyer.
3. Therefore future raffle takeover search should only reopen when BOTH are present:
   - a fixed/capped eligible supply that can legally and operationally be acquired in full before draw close; AND
   - total guaranteed cash prizes / external subsidy exceed full acquisition cost after tax and execution.

No current strict guaranteed-profit lottery strategy was established.
