# H291 — Michigan iLottery bonus mechanics × Daily 3 exact-cover threshold

Date: 2026-08-26
Status: **SCREENED / NO CURRENT PUBLIC STRICT-PROFIT QUALIFIER**

## Why this packet

H225-X* is already terminally exhausted at X20, so this packet follows the global search for deterministic external subsidy that can lift an exact lottery cover above 100% worst-case cash recovery.

Michigan is worth screening because the Lottery publicly documents several online bonus classes, including deposit-match bonus credit and a distinct **Play & Get Bonus Cash** class where earned Bonus Cash can be withdrawn.

Official evidence:
- Michigan Lottery bonus types: https://help.michiganlottery.com/support/solutions/articles/158000441667-types-of-online-bonus-offers
- Current FAQ variant: https://faq.michiganlottery.com/account-information-d9a19100/online-bonuses-f2b270a4/types-of-online-bonus-offers-08356151
- Michigan Lottery mobile app FAQ confirms Daily 3 and Daily 4 are among draw tickets purchasable in the app: https://faq.michiganlottery.com/en/mobile-app-information-052d5f4e/general-mobile-app-faq-8406c09a/michigan-lottery-mobile-app-faq-673b607c
- 2025 Michigan Lottery ACFR states Daily 3/4 were planned for iLottery availability in FY2026 Q2: https://audgen.michigan.gov/wp-content/uploads/2026/03/2025-Michigan-Lottery-Annual-Comprehensive-Financial-Report.pdf

## Exact Daily 3 construction

Use every 3-digit Straight outcome from 000 through 999 once at the $0.50 wager level.

- lines: **1,000**
- stake per line: **$0.50**
- exact cover cost: **$500**
- for every legal draw, exactly one Straight line wins
- $0.50 Straight prize used by the current game structure: **$250**
- deterministic base-game gross: **$250**
- deterministic base-game return: **50%**

This is stronger for guarantee analysis than using uncontrolled free games or random promotional outcomes because the base-game payout is invariant over all draw states.

## Deposit-match threshold

Let `m` be the deposit-match fraction and assume, favorably, that the entire match is immediately spendable on this cover.

External cash needed for the $500 cover is

`cash = 500 / (1 + m)`.

Guaranteed withdrawable draw winnings are $250. Strict positive profit therefore requires

`250 > 500 / (1 + m)`

which simplifies to

`m > 1`.

So the exact threshold is **strictly greater than a 100% deposit match**.

Examples:
- 10% match → cash needed $454.5455; floor loss $204.5455; 55% cash recovery.
- 40% match → cash needed $357.1429; floor loss $107.1429; 70% recovery.
- 100% match → cash needed $250; guaranteed $250; **break-even only**.
- 101% match → cash needed $248.7562; guaranteed $250; floor profit $1.2438.

## Public bonus evidence gate

Michigan Lottery's public FAQ gives **sample** deposit-match offers such as 10% and tiered examples up to 40%. It also states the maximum bonus credit awarded may vary. Those examples are not evidence of a current universal >100% match.

The same official FAQ documents **Play & Get Bonus Cash**, with a sample such as play $25 and receive $5 Bonus Cash; the Bonus Cash is described as withdrawable. That is a useful mechanism, but the published sample is only a 20% cash rebate on qualifying play and is not stated as a repeatable entitlement over a $500 Daily 3 cover. It therefore cannot be scaled into a deterministic profitable cover from the public rules.

More importantly, available offers are account-specific and shown in `My Bonus Activity`; the public FAQ does not establish a current universal offer above the exact >100% threshold.

## Channel caveat

Michigan's current public documentation is internally asynchronous: the mobile-app FAQ explicitly lists Daily 3/4 as purchasable, while a generic web draw-purchase FAQ still lists only Mega Millions, Powerball, Lotto 47, Fantasy 5, and Millionaire for Life. This discrepancy does **not** affect the arithmetic closure of currently public sample match rates, because even a perfect execution path with a 100% match reaches only break-even.

## Conclusion

**No rigorous SUCCESS.** Michigan supplies the right *kind* of deterministic subsidy, but no current public Lottery-controlled evidence establishes a universally available deposit match **strictly above 100%**, nor a repeatable withdrawable Bonus-Cash reward large enough to bridge the $250 deficit of the exact $500 Straight cover.

Reopen H291 only if a current eligible account has one of the following Lottery-controlled offers and the offer can be verified before play:
1. deposit match **>100%** with at least enough matched balance to fund the exact cover; or
2. deterministic withdrawable Bonus Cash that, combined with the invariant $250 Daily 3 cover payout, exceeds the external cash committed; or
3. another fixed-pay Michigan draw construction with deterministic base floor materially above 50%.

Reproducible arithmetic:
- `src/loto_research/h291_michigan_daily3_bonus_threshold.py`
- `data/derived/h291_michigan_daily3_bonus_threshold.json`
