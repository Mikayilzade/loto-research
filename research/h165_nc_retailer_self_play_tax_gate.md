# H165 — NC retailer self-play legality + 2026 tax-floor stress test

Updated: 2026-08-22
Status: **SELF-PLAY LEGALITY STRONGLY VALIDATED / TERMINAL GUARANTEE STILL REJECTED ON COMMISSION-ATTRIBUTION, TAX, ACTIVE-STATE AND EXECUTION GATES**

## Scope
Lottery-only continuation of H164. This packet does **not** repeat the Pick-3 Pair-cover arithmetic; it tests the two highest-value unresolved H164 questions that can be advanced from public sources now:

1. may an NC lottery retailer/retailer employee lawfully play lottery games; and
2. does the 7% overlay survive the new 2026 federal wagering-loss rule under plausible tax structures?

## 1. Retailer self-play legality
North Carolina Education Lottery itself answered this question directly in an official 2016 security/retailer article:

> “Lottery retailers can play lottery games in all U.S. lotteries.”

NCEL added that one state, Indiana, had a special restriction on a retailer claiming a prize bought at its own store; NC was not identified as having such a restriction.

Official source:
- https://nclottery.com/News/2016/9/21/Some-facts-and-information-on-players-who-beat-the-odds

NCEL reiterated in a 2018 retailer-compliance response that **there is no law in North Carolina that bars retailers from playing the lottery**, while noting that many retailers voluntarily adopt employee “No Play on Duty” policies.

Official source:
- https://nclottery.com/NewsBlogDetails/2018/8/22/Lottery-conducts-checks-on-retailers

Current Chapter 18C disqualifies Commission/Director/NCEL employees and household members, but does not list ordinary lottery retailers among persons prohibited from buying/claiming tickets. Current retailer eligibility rules likewise do not create a blanket retailer-player prohibition.

Primary/current sources:
- https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByChapter/Chapter_18c.pdf
- https://nclottery.com/RetailerApplication

### Result on self-play
**CLOSED POSITIVELY:** a blanket legal theory that “NC retailer owners/employees cannot play” is false. Retailer play is permitted subject to ordinary rules and any private employer policy.

### Remaining narrower commission-attribution gate
The current NCEL retailer contract and G.S. 18C-142 state that retailer compensation is **7% of the face/retail value of tickets or shares sold by the retailer**.

Sources:
- https://nclottery.com/Content/Docs/Retailer_Contract_v1.pdf
- https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByChapter/Chapter_18c.pdf

NCEL also states publicly that retailers earn 7% on each ticket sold / 7 cents per dollar sold.

Sources:
- https://nclottery.com/RetailerApplication
- https://nclottery.com/NewsBlogDetails/2019/7/16/A-shout-out-to-those-who-sell-our-tickets-pay-out-prizes

This makes commission treatment of an otherwise valid own-store purchase **strongly supported**, especially where the retailer is a legal entity distinct from the individual purchaser. However, the public material recovered in this run still does not contain the exact accounting sentence required for terminal proof: e.g. “a retailer-owner’s personal ticket purchased at the owner’s licensed location is included in commission-bearing gross sales.”

Therefore H164 Gate 2 is **narrowed but not fully closed**.

## 2. 2026 federal wagering-loss rule stress test
H164’s pre-tax deterministic economics on a forced Double Draw state are:

- face spend: $50
- guaranteed Pick-3 prizes: $50
- retailer commission if commission-bearing: $3.50
- pre-tax economic surplus: **+$3.50**

Beginning in tax years after 2025, IRC §165(d), as amended by Public Law 119-21, allows a wagering-loss deduction equal to only **90% of wagering losses**, limited to wagering gains.

Primary/current sources:
- Public Law text: https://www.congress.gov/119/plaws/publ21/PLAW-119publ21.htm
- IRS 2026 proposed regulation explanation: https://www.irs.gov/irb/2026-19_IRB
- IRS Publication 505 (2026): https://www.irs.gov/publications/p505

If the $50 ticket cost is treated as $50 of wagering losses against $50 of wagering gains, the maximum federal wagering-loss deduction is $45. This creates **$5 of taxable gambling income even though prize cash merely equals ticket cost**.

If the same economic owner is also taxed on $3.50 of retailer commission, a simple combined marginal-rate screen is:

`after_tax_profit = 3.50 - (5.00 + 3.50) * combined_incremental_tax_rate`

Break-even combined incremental rate:

`3.50 / 8.50 = 41.1764706%`

North Carolina’s 2026 individual income-tax rate is 3.99%.

Official source:
- https://www.ncdor.gov/taxes-forms/individual-income-tax/tax-rate-schedules

At a 37% federal marginal rate + 3.99% NC rate, the simplified after-tax cushion is only about **+$0.01585 per $50 cover**, before any self-employment/payroll/business-entity tax, deduction interaction, retailer operating cost, terminal fee allocation, or other friction. Any additional effective burden above ~0.1865 percentage points eliminates that simplified cushion.

At lower federal marginal rates the cushion is larger, but this does **not** create a universal after-tax floor. A taxpayer who cannot use the wagering-loss deduction as assumed can fare much worse.

## 3. Execution evidence retained
Current official Pick-3 rules remain favorable relative to NJ:
- a retail Pick-3 ticket may be canceled on the issuing terminal within 15 minutes of purchase or before draw break, whichever comes first;
- game rules also allow NCEL to stop accepting a number when prize liability exceeds a predetermined limit.

Sources:
- https://nclottery.com/pick3-how-to-play
- https://nclottery.com/FAQGames
- https://qa.nclottery.com/Content/Docs/2.04B%20Carolina%20Pick%203%20Game%20Rules.pdf

The cancellation window supports a practical rollback attempt but still is not an atomic all-or-none basket guarantee under terminal/system outage.

## Exact conclusions
- **Retailer may play NC lottery games:** VALIDATED by direct NCEL statements.
- **7% retailer commission rate:** VALIDATED current by statute/contract.
- **Own-store personal ticket definitely commission-bearing:** STRONGLY SUPPORTED but not explicitly proven by a public NCEL accounting sentence.
- **2026 tax gate:** materially worse than pre-2026; the 7% gross overlay is razor-thin under top marginal individual rates and is not a universal net-profit floor.
- **Current forced Double Draw state:** not active as of this checkpoint; next cycle must be revalidated.
- **Atomic execution:** still unproven.

## Terminal result
**NOT SUCCESS.** H164 remains the strongest recurring lottery-specific execution architecture, but after H165 the remaining gates are sharper:

1. written/current confirmation that owner-personal own-store Pick-3 sales are commission-bearing gross sales;
2. current forced Double Draw state;
3. a rollback/acceptance procedure that removes every allowed partial-cover loss branch;
4. an explicit taxpayer/entity structure with positive after-tax floor after the 2026 90% wagering-loss cap and all operating costs.

Reopen H164/H165 only on new evidence for one of those four gates; do not repeat the already-closed question of whether NC retailers are generally allowed to play.