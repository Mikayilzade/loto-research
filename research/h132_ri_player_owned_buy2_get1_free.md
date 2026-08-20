# H132 — Rhode Island player-owned `buy 2, get 1 free` lottery subsidy

Updated: 2026-08-20
Status: **PLAYER-OWNED DETERMINISTIC SUBSIDY CLASS VALIDATED / MEGA MILLIONS GUARANTEE STILL REJECTED / PROMO TERMS PARTLY DATA-GATED**

## Why this branch matters
H131 showed that a cash subsidy can exceed ticket cost but a statewide `Nth` allocation does not belong to the player: unrelated purchases can occupy the subsidized positions. H132 searches for the missing structural property — a benefit created directly by the player's own purchase.

The current official Rhode Island Lottery home page displays **“Get a free ticket when you buy 2”**. The displayed call-to-action resolves to the Rhode Island Mega Millions page in the current site navigation/crawl. This is materially different from H131 because the free-ticket entitlement is purchase-local rather than a statewide serial position.

Primary current sources checked 2026-08-20:
- Rhode Island Lottery home page: https://www.rilot.com/en-us/home.html
- Rhode Island Lottery Mega Millions page reached from the offer CTA: https://www.rilot.com/en-us/megamillions.html

The crawler does not expose the complete promotion contract (dates, caps, eligible purchase channel, whether free play is same draw, whether multiplier/other features are included), so exact current execution eligibility remains data-gated. The structural result below is therefore conditional on the plain-language `buy 2, get 1 free` entitlement applying to standard $5 current-format Mega Millions plays as linked by the official page.

## Deterministic subsidy math
Current-format Mega Millions price = $5 per play. If every three qualifying plays cost only two paid plays, the effective acquisition cost is:

`effective price = 2*$5/3 = $3.333333... per play`

This is a **33.3333% deterministic purchase subsidy** on the ticket count. Unlike random second chance, statewide Nth coupons, or prize-dependent rebates, the third play is attached to the purchaser's own qualifying purchase.

## Full-space stress test
Reuse the exact current Mega Millions combination space and strict lower-tier floor from H002a:
- complete space: `290,472,336` plays;
- ordinary full-space spend at $5: `$1,452,361,680`;
- strict worst-legal-multiplier non-jackpot floor under full coverage: `$216,590,680`.

With an unlimited exact 2-paid-for-3 promotion, full-space paid cost would fall to:

`$1,452,361,680 * 2/3 = $968,241,120`.

The strict non-jackpot floor would then recover:

`$216,590,680 / $968,241,120 = 22.3695%` of subsidized spend.

If our jackpot-winning line were guaranteed to be the **sole** jackpot winner, the cash jackpot needed merely to break even before tax/fees would fall from H002a's `$1,235,771,000` to:

`$968,241,120 - $216,590,680 = $751,650,440`.

So a 33.3333% player-owned ticket subsidy is economically large: it reduces the sole-winner strict cash hurdle by **$484,120,560**.

## Why it is still not a guaranteed-profit strategy
The terminal blocker survives unchanged:
1. complete coverage guarantees that we own one jackpot-winning combination;
2. Mega Millions permits other players to hold the same winning combination;
3. jackpot cash is shared among jackpot-winning tickets;
4. there is no useful pre-draw hard cap on the number of external duplicate jackpot winners.

Therefore no finite positive jackpot amount can create a strict all-outcome profit floor unless external jackpot sharing is bounded/removed. The free-ticket subsidy meaningfully improves EV and the sole-winner threshold, but does not solve the sharing branch.

Additional execution blockers:
- exact promotion terms/caps were not exposed by the public crawler;
- a cap of only a few free tickets would make the full-space calculation hypothetical rather than executable;
- geolocation/residency/online-purchase restrictions may apply;
- taxes and transaction/execution limits remain adverse.

## Structural theorem from H132
A purchase-local `buy a, receive b extra tickets` promotion is a genuine deterministic subsidy. For a portfolio with ordinary acquisition cost `S`, the subsidized spend is `S*a/(a+b)` if the benefit scales without cap.

It can create a terminal guarantee only if, after applying the subsidy, **the minimum payout across every legal outcome** exceeds subsidized spend plus taxes/fees/execution costs. A subsidy alone cannot repair an unbounded shared-prize branch.

## Result
**No SUCCESS.**

Important positive result: the project has now found the player-owned deterministic allocation class that H131 was explicitly searching for. The current Rhode Island offer demonstrates that own-purchase ticket subsidies exist in live official lottery operations. For Mega Millions, however, even an unlimited 33.3333% ticket subsidy still fails strict guaranteed-profit because jackpot sharing remains externally unbounded.

## Next research use
Prioritize the same purchase-local subsidy mechanism on games where:
- top/fixed prizes are not shareable;
- outcome space is compact enough for complete/complementary coverage;
- free-ticket benefit scales or has a high cap;
- minimum full-coverage payout is already near the unsubsidized cost.

That combination, not another large shared jackpot, is the highest-value continuation.