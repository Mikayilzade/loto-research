# H135 — Washington Happy Hour deterministic subsidy + compact coverage

Updated: 2026-08-20
Status: **SCALABLE PLAYER-OWNED SUBSIDY VALIDATED / COMPACT FIXED-PRIZE COVERAGE STILL NEGATIVE / NOT SUCCESS**

## Goal
Test H133/H134 on a rare lottery promotion where the subsidy is both player-owned and explicitly scalable by transaction size, then pair it with a compact, non-shareable fixed-prize game.

## Official promotion control
Washington's Lottery ran a `Happy Hour` promotion on Match 4 from **October 12–25, 2025**:

- purchase a **$10 Match 4 ticket**;
- receive a **$4 Match 4 ticket free**;
- multiple promotional offers were explicitly allowed in $10 increments;
- current draw only.

That is a deterministic subsidy of `$4` for each `$10` paid, i.e. total ticket face value `$14` per `$10` cash outlay. If the promotional free plays can be directed into distinct required selections, the effective coverage-cost factor is `10/14 = 71.4286%`, a **28.5714% discount** from face value.

Primary source: Washington's Lottery Happy Hour offer (`id=14466`).

A later Lotto Happy Hour on **June 14–27, 2026** used the same scalable structure: buy $5 Lotto and receive $1 Lotto free; multiple offers were expressly allowed in $5 increments. This confirms the mechanism is recurring rather than a one-off typo, although that specific promotion is expired as of 2026-08-20.

Primary source: Washington's Lottery Happy Hour offer (`id=14495`).

## Why Match 4 is a strong test
Current Washington Match 4 is unusually favorable for a deterministic-coverage screen:

- choose 4 numbers from 1–24;
- ticket cost: **$2 per play**;
- 4/4 pays **$10,000** and the official page expressly says the top prize **is not divided among winners**;
- 3/4 pays **$20**;
- 2/4 pays **$2**.

This removes the external jackpot-sharing failure that closes many full-space strategies.

Primary source: Washington's Lottery Match 4 page.

## Exact full-space identity
Number of selections:

`N = C(24,4) = 10,626`

Face-value full-cover cost:

`C = 10,626 × $2 = $21,252`

For any realized winning 4-set, a complete cover deterministically contains:

- one 4/4 winner: `1 × $10,000 = $10,000`;
- `C(4,3) × C(20,1) = 80` 3/4 winners: `80 × $20 = $1,600`;
- `C(4,2) × C(20,2) = 1,140` 2/4 winners: `1,140 × $2 = $2,280`.

Therefore deterministic gross payout is:

`P = $13,880`

Base full-space return:

`P / C = 65.3115%`

## Best-case Happy Hour application
Under the strongest player-favorable interpretation — every free $4 ticket can be deliberately assigned to still-uncovered Match 4 selections, no duplicates, no transaction cap beyond the published $10 increments — effective cash cost becomes:

`C_eff = $21,252 × (10/14) = $15,180`

Strict deterministic gross return:

`$13,880 / $15,180 = 91.4361%`

Guaranteed loss before tax/travel/execution:

`$15,180 - $13,880 = $1,300`

So even the unusually strong 40%-of-spend subsidy is insufficient.

## Required subsidy threshold
Match 4's deterministic base coverage ratio is `r = 0.653115`.

The exact face-value discount required merely to break even is:

`1-r = 34.6885%`.

Equivalently, if the promotion is phrased as free face value per paid cash amount, required bonus-on-spend is:

`1/r - 1 = 53.1124%`.

Therefore a scalable Match 4 promotion must provide **more than $5.311 of controllable free Match 4 value per $10 paid** before costs/taxes to create a positive strict full-cover floor. The observed $4 per $10 is materially short.

## Washington Lotto Happy Hour control
The June 2026 Lotto Happy Hour provided `$1 free per $5 paid`, only a 16.6667% face-value discount. Washington Lotto also has a progressive/shareable jackpot, so it is structurally weaker than Match 4 for a guaranteed-profit test. No deeper full-space execution is justified under H133/H134 because the subsidy is much smaller and jackpot sharing remains an adverse branch.

## Current OLG BOGO control
Ontario's current 2026 `Buy 1 LOTTO 6/49, Get 1 on Us` and `Buy 1 LOTTO MAX, Get 1 on Us` offers are real deterministic game-specific bonuses, but each is targeted to selected account holders and capped at one $3/$6 bonus per promotion period. They are not scalable coverage subsidies. A single additional random/draw ticket has no useful strict cash floor unless it can close a complementary cover, and the one-ticket cap is negligible relative to the huge combination spaces.

## Result
H135 validates the exact type of promotion H133/H134 was designed to find: **deterministic, player-owned and scalable** free lottery value. Pairing it with a compact fixed-prize game also removes prize sharing.

Yet the strongest observed Washington Match 4 structure still reaches only **91.4361% deterministic gross return** under deliberately generous assumptions.

**Conclusion: NOT SUCCESS.**

## New screening threshold
For Washington Match 4 or any game with equivalent deterministic coverage ratio `r`, do not spend execution effort on scalable purchase-local promotions unless:

`bonus_on_spend > 1/r - 1`

For current Match 4 payouts this means **>53.1124% free controllable ticket value per paid dollar** before execution costs.

This threshold makes future promo scans much faster: a `buy $10 get $4` offer is insufficient; roughly `buy $10 get >$5.31` is the first mathematically interesting range.

## Sources
- Washington's Lottery, Match 4 game page, accessed 2026-08-20.
- Washington's Lottery, Happy Hour Match 4 offer, Oct 12–25 2025.
- Washington's Lottery, Happy Hour Lotto offer, Jun 14–27 2026.
- OLG, current 2026 LOTTO 6/49 and LOTTO MAX targeted BOGO terms, accessed 2026-08-20.
