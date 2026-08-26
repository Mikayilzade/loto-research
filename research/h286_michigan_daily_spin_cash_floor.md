# H286 — Michigan Lottery Daily Spin to Win guaranteed-reward cash-floor audit

Date: 2026-08-26
State: **CLOSED / REJECTED for strict guaranteed-profit use**

## Question
Michigan Lottery's current Daily Spin to Win is unusually interesting because the Lottery states that **every player that spins wins a prize**. Does that make the free daily spin a deterministic external subsidy with positive withdrawable cash value?

## Authoritative mechanics checked
Michigan Lottery's current FAQ says:
- the game is free and available once per day to an eligible Michigan Lottery account;
- every spin wins a prize;
- the current prize classes are **in-store free play**, **online free play / bonuses**, or **entries into a monthly cash-prize giveaway**;
- prizes are immediately awarded to the account.

The separate prize-location FAQ confirms those three channels: in-store free-play coupons, online free-play bonuses, and monthly giveaway entries.

Michigan's bonus FAQ distinguishes **Bonus Cash**, which can be withdrawn, from bonus credit/free games. The Daily Spin FAQ does not say that every spin awards Bonus Cash; instead a legal prize outcome is a monthly giveaway entry. A giveaway entry is only a chance in a later random drawing and has no guaranteed immediate cash payment.

Primary sources checked 2026-08-26:
- Michigan Lottery, Daily Spin to Win Information: https://faq.michiganlottery.com/promotions-giveaways-and-offers-information-62f7cc/daily-spin-to-win-c6e5ee/daily-spin-to-win-information-c6418a
- Michigan Lottery, Locating Daily Spin to Win Prizes: https://faq.michiganlottery.com/promotions-information-62f7ccba/daily-spin-to-win-c6e5eece/locating-daily-spin-to-win-prizes-b2c48a78
- Michigan Lottery, Types of Online Bonus Offers: https://help.michiganlottery.com/support/solutions/articles/158000441667-types-of-online-bonus-offers
- Michigan Lottery, How to Withdraw Winnings: https://help.michiganlottery.com/support/solutions/articles/158000441529-how-to-withdraw-winnings

## Exact worst-case result
Let `V(p)` be guaranteed immediately withdrawable cash value of a possible spin prize `p`.

A monthly giveaway entry has:

`V(giveaway_entry) = 0`

because there is a legal later drawing outcome in which that entry is not selected. Therefore, even though every spin wins *something*:

`min_p V(p) = 0`.

So the deterministic statement "every spin wins a prize" does **not** imply a positive deterministic cash subsidy.

The result does not depend on assigning a speculative retail/expected value to free play. One legal prize class already has zero guaranteed cash floor, which is sufficient to set the whole spin's worst-case cash floor to zero.

## Stronger interpretation
Repeated free daily spins also do not by themselves create a strict finite cash guarantee unless the rules impose a finite-state elimination or guaranteed cash award after a bounded number of spins. The checked FAQ publishes no such terminal guarantee. For any fixed finite number of spins, the public rules do not establish that a withdrawable-cash prize must occur.

## Conclusion
**REJECT for the current strict-guarantee objective.** Michigan Daily Spin to Win is a genuine guaranteed-reward mechanism but not a guaranteed-*cash* mechanism. Reopen only if the prize wheel changes so every possible segment has a positive withdrawable-cash floor, or if a bounded terminal rule guarantees Bonus Cash after finitely many spins.
