# H299 — Current capped-raffle full-takeover screen

Date checked: 2026-08-27
State: **CLOSED for strict guaranteed-profit full takeover**

## Goal

Continue the finite-pool line after H298, but require a materially stronger candidate: a hard-capped pool where complete ownership of every issued identifier could plausibly return more than acquisition cost.

The test is deliberately stronger than real execution. For every case below, assume one player can buy **every ticket from inception**, no ticket is unavailable, there are no transaction fees, taxes, eligibility problems, resale haircuts, or competing owners, and every published prize liability is collected by that player. If this impossible-perfect takeover is still below cost, real execution cannot restore a strict guarantee.

## Screened current/upcoming pools

### 1. NAVMC Crocktoberfest Golden Ticket — 18 Oct 2026
Official/current event page states only 100 Golden Tickets, $100 each, with one $1,000 cash prize.

- full pool cost: 100 × $100 = **$10,000**
- total player-facing cash liability: **$1,000**
- perfect-takeover gross: **10.0%**
- deficit: **$9,000**

Source: https://navmc.org/

### 2. Golden Lake Improvement Association — 6 Sep 2026 cash raffle
The association publishes 200 tickets at $100 and three cash prizes: $7,000, $2,000 and $1,000.

- full pool cost: 200 × $100 = **$20,000**
- total cash prizes: **$10,000**
- perfect-takeover gross: **50.0%**
- deficit: **$10,000**

Source: https://goldenlakeassociation.com/drawings/

### 3. DPCA Top 20 Conformation 50/50 raffle — Oct 2026
Current page states only 100 tickets at $100, with one winner taking half the pot, up to $5,000.

- full pool cost: **$10,000**
- maximum full-pool winner liability: **$5,000**
- perfect-takeover gross: **50.0%**
- deficit: **$5,000**

Source: https://dpca.org/cardio-clinic-wae-fundraisers-wine-tasting-rules/

### 4. Millville Army Air Field Museum — 2 Dec 2026 50/50 cash raffle
The museum publishes 500 tickets at $50. The listing gives a $10,000 first prize or one of five $500 prizes, with prize amounts based on a full sellout. To avoid understating the player's case, H299 uses the **most favourable cumulative reading**: $10,000 + 5×$500 = $12,500 total liability.

- full pool cost: 500 × $50 = **$25,000**
- player-favourable gross upper bound: **$12,500**
- perfect-takeover gross: **50.0%**
- deficit: **$12,500**

Source: https://p47millville.org/events/

## Result

The strongest screened pool reaches only **50%** of complete acquisition cost. Therefore none of these four pools can produce a strict guaranteed profit by complete finite-pool takeover. The conclusion does not depend on execution friction, ticket availability, external buyers, taxes, or timing; all of those were already removed in the player's favour.

A future candidate in this line should not be opened unless either:

1. deterministic player-facing liabilities exceed the exact cheapest complete acquisition cost; or
2. a documented external subsidy/discount fills the exact takeover deficit.

For a 50%-ratio structure, the external deterministic uplift must equal **at least 50% of full-pool cost for break-even and strictly more for profit**.

## Reproducibility

- model: `src/loto_research/h299_current_capped_raffle_screen.py`
- derived result: `data/derived/h299_current_capped_raffle_screen.json`
- validation: `research/H299_VALIDATION.md`
