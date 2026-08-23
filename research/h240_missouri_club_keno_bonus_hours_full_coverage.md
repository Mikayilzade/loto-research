# H240 — Missouri Club Keno Bonus Hours full-coverage upper-bound closure

Date: 2026-08-24
Branch: `research-work`
Status: REJECTED for guaranteed-profit base Club Keno full coverage
Scope: LOTTERY ONLY

## Question
Can Missouri Lottery's deterministic Club Keno `Bonus Hours` mechanism make full combinatorial coverage of any ordinary base Club Keno spot category (1–10 spots) strictly profitable?

## Primary evidence
Missouri Lottery current Club Keno rules state:
- spots 1 through 10 are available from an 80-number field with 20 winning numbers drawn;
- base payouts are published per $1 wager;
- a player may buy 1, 2, 3, 4, 5, 10 or 20 consecutive drawings;
- the maximum Club Keno ticket price is $250;
- current payout tables match the 2026 Fact Book.

Missouri Lottery's official Club Keno Bonus Hours promotional material states the qualifying structure is a **10-draw single ticket**, with increased prizes of **up to 50%** on base prizes of $2 or greater. Official materials also state Multiplier wagers are ineligible; progressive jackpot prizes and 10-of-10 prizes are not increased; coupons cannot be combined with the promotion.

The retailer promotional-materials page still labels `Club Keno Bonus Hours Promotion` as current, but the linked flyer currently resolves to a December 2025 promotion. Therefore this packet treats the mechanic as a real recurring deterministic lottery promotion and closes the mathematical base-coverage class; it does **not** assert an executable August 2026 promotion window.

## Exact full-space method
For an s-spot base game, buy every `C(80,s)` distinct s-subset. For any fixed 20-number draw, the number of tickets matching exactly h selected numbers is fixed:

`N(s,h) = C(20,h) * C(60,s-h)`.

Thus full-space base gross is deterministic:

`G_s = sum_h N(s,h) * payout(s,h)`.

Because Bonus Hours requires a 10-draw ticket, full coverage must be carried through ten consecutive drawings. Both spend and deterministic base gross scale by exactly 10, so the gross-return ratio is unchanged.

## Dominating upper-bound test
To reject the class without needing the exact tier-by-tier Bonus Hours uplift schedule, grant the player a strictly more favorable hypothetical promotion than the official one:

**Every base prize in every spot category is multiplied by 1.5, with no exclusions.**

This dominates the real promotion because the real rules only say `up to 50%`, exclude $1 prizes, exclude 10-of-10 from the increase, and impose other restrictions.

Exact results per $1 base line:

| Spot | Base full-space return | Universal +50% upper bound | Official-exclusion-aware upper bound |
|---:|---:|---:|---:|
| 1 | 50.0000% | 75.0000% | 75.0000% |
| 2 | 60.1266% | 90.1899% | 90.1899% |
| 3 | 62.4391% | **93.6587%** | **93.6587%** |
| 4 | 61.2678% | 91.9018% | 81.2700% |
| 5 | 62.2542% | 93.3813% | 93.3813% |
| 6 | 60.0292% | 90.0438% | 83.5528% |
| 7 | 60.4173% | 90.6260% | 81.8763% |
| 8 | 58.2033% | 87.3050% | 87.3050% |
| 9 | 58.4969% | 87.7454% | 82.0401% |
| 10 | 60.1555% | 90.2332% | 89.6721% |

The best possible category under the deliberately over-generous universal +50% assumption is 3-spot at only **93.6587%** of spend. Therefore no base spot category can reach break-even, even before taxes, travel, transaction throughput, ticket limits or other execution costs.

### Concrete 3-spot 10-draw example
- distinct 3-spots: `C(80,3) = 82,160`;
- cost for one complete $1 cover across the required 10 draws: `$821,600`;
- deterministic base gross per draw: `$51,300`;
- deterministic base gross for 10 draws: `$513,000`;
- hypothetical universal +50% gross: `$769,500`;
- deterministic deficit even under this stronger-than-real promotion: **-$52,100**.

## Consequence
The recurring Missouri Bonus Hours mechanism cannot create a guaranteed positive-profit strategy by fully covering any **ordinary base Club Keno** spot category 1–10. This is stronger than testing only 3-spot and stronger than using the literal published promotion, because the rejection survives a universal +50% payout assumption.

This packet does **not** close Bulls-Eye / Double Bulls-Eye full-space constructions; those add-ons change both state space, price and payout table and require a separate exact packet if still defensible.

## Verdict
**REJECTED — base Club Keno full-coverage class under Bonus Hours.** Even a hypothetical universal +50% uplift on every base prize has a maximum deterministic return of 93.6587%, so the actual promotion cannot guarantee profit.

## Sources
- Missouri Lottery current Club Keno rules: https://molottery.com/club-keno/rules.jsp
- Missouri Lottery current Club Keno payout page: https://www.molottery.com/club-keno/club-keno.jsp
- Missouri Lottery 2026 Fact Book: https://www.molottery.com/news/files/documents/2026FactBook2.pdf
- Missouri Lottery retailer promotional materials: https://retailer.molottery.com/displaytopic.do?topic=promotional-materials
- Missouri Lottery Bonus Hours flyer: https://retailer.molottery.com/documents/sell_in/KenoBonusHoursSellIn.pdf
- Historical official Bonus Hours rules/details: https://www.molottery.com/article.do?id=1018&method=s
