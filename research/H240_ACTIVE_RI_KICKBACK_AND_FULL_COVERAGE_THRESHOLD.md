# H240 — Active Rhode Island Kick Back promo vs full 3-spot coverage threshold

Date: 2026-08-24
Status: NOT SUCCESS

## New active promotion found
Rhode Island Lottery is currently advertising `Kick Back with Keno` on Thursdays this summer, June 25 through August 27, 2026, from 4 p.m. to 8 p.m. Official RI Lottery social posts state: make a $5 Keno purchase in a single transaction and receive a $1 bonus.

As of 2026-08-24, the final advertised window is Thursday, 2026-08-27.

This is important because it is a deterministic purchase-time promotional benefit, unlike random Doubler/Tripler ticket tags.

## Why the current $1-on-$5 layer is insufficient by itself
The nominal promotional layer is 20% of qualifying purchase value ($1 per $5 transaction), before considering any restrictions on what the bonus can be used for or its redemption value.

For comparison, the exact full-coverage mathematics for an 80-number / 20-drawn 3-spot game is fixed for every draw:

- total distinct 3-spots: C(80,3) = 82,160
- exactly 3 hits: C(20,3) = 1,140
- exactly 2 hits: C(20,2) * C(60,1) = 11,400
- exactly 1 hit: C(20,1) * C(60,2) = 35,400
- exactly 0 hits: C(60,3) = 34,220

Using the current Ohio KENO 3-spot pay table as a verified reference example ($27 for 3/3, $2 for 2/3), full coverage returns deterministically:

11,400*$2 + 1,140*$27 = $53,580

on $82,160 of $1 wagers, an exact base return of 65.213%.

Therefore a *free* universal payout multiplier would need to exceed:

82,160 / 53,580 = 1.533407...

So the minimum continuous uplift threshold is about +53.34%. A free universal 2X would return $107,160, guaranteeing $25,000 gross profit before operational/tax costs.

A 20% promotional benefit alone is below this threshold. Even if treated optimistically as dollar-for-dollar cash value, 65.213% + 20% = 85.213% of stake-equivalent value, still below break-even in the Ohio reference model.

## Historical mechanism that *would* clear the threshold
Rhode Island's `Lucky 3 Spot Keno` promotions in 2024 and 2025 were deterministic venue/time promotions for 3-spot tickets: qualifying winning 3-spot tickets had their prizes doubled, and eligible tickets printed a message stating that any prize would be doubled. No additional Keno Plus purchase is stated as a requirement in those promotion rules.

Thus a genuine free all-qualifying-ticket 2X overlay has existed in Rhode Island. The missing piece is not theoretical feasibility but whether such a promotion is active/announced again and whether transaction/terminal limits permit the necessary coverage.

## Current execution blockers
1. `Kick Back with Keno` is only a $1 bonus per $5 purchase, not a universal 2X prize overlay.
2. Exact current Rhode Island 3-spot base payout table still needs to be extracted from an authoritative source before applying the 82,160-cover calculation directly to RI.
3. The bonus's exact redemption/use rules need to be located; treating it as cash-equivalent is only an upper-bound simplification.
4. Full 82,160-combination same-draw entry remains operationally unrealistic unless bulk/multi-board terminal limits or a compressed covering design are established.
5. Historical Lucky 3 Spot 2X windows were venue-limited and expired.

## Verdict
NOT SUCCESS. The current RI promotion is deterministic and active through 2026-08-27, but its nominal 20% benefit is too small to rescue a full 3-spot coverage construction on the verified Ohio reference economics. Historical Rhode Island Lucky 3 Spot promotions prove that a free deterministic 2X layer has existed and would be the correct class of mechanism to monitor for recurrence.

## Sources
- RI Lottery official X post, 2026-08-06: https://x.com/RILottery/status/2085350176974377450
- RI Lottery current Keno page: https://www.rilot.com/en-us/keno.html
- RI Lottery Lucky 3 Spot Keno & Bingo Doubler rules (2025): https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/LaunchAlertRules-Lucky3SpotKenoBingoDoubler.pdf
- RI Lottery Lucky 3 Spot Keno rules (2024): https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2024/Lucky3SpotKenoRule091224.pdf
- Ohio Lottery current KENO page/pay table: https://www.ohiolottery.com/games/keno
