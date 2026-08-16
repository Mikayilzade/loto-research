# H044 — Azerbaijan-accessible promotion + external hedge screen

Updated: 2026-08-16
Status: **promising architecture; terminal guarantee NOT established**

## Goal
Search for a current promotion that is simultaneously:
1. accessible to an Azerbaijan resident;
2. deterministic enough to acquire a cash/free-bet subsidy;
3. compatible with an independently matched hedge;
4. not contractually voidable merely because the combined position is low-risk;
5. strong enough to produce a strictly positive all-outcome net cash floor after commissions and settlement risks.

## Candidate A — eTopaz first-deposit 15% free bet
Current operator promotion page states:
- new first-deposit users receive a free bet equal to **15% of the first deposit**;
- minimum deposit is **20 AZN**;
- after the deposit, the **first bet must settle**, after which the free bet is loaded automatically;
- free-bet stake is not returned; only winnings are returned;
- free bet may be used on singles and combos and expires after 14 days;
- operator reserves the right to change or cancel the promotion.

Primary current source:
- https://www.etopaz.az/eng/promotions

The current page does **not** state a minimum qualifying first-bet amount or minimum odds in the indexed text. This is important because, if the qualifying stake can be kept very small relative to the 15% deposit-linked token, acquisition economics could be materially better than ordinary deposit-match offers.

However, the absence of a published minimum in indexed text is **not proof that no platform-level minimum stake applies**.

### Contract gate
The first-deposit offer text does not explicitly say that external hedging/arbitrage voids the free bet. By contrast, the separate weekly-cashback offer on the same promotions page explicitly says promotion abuse is not permitted. That difference is noteworthy but insufficient for a strict guarantee because:
- eTopaz retains an explicit right to change/cancel the promotion;
- general account/betting terms may contain additional discretionary or abuse clauses not recovered in machine-readable form;
- an operator-side void, market correction or settlement mismatch can leave the external hedge standing.

Status: **best local acquisition lead found so far, but contract certainty incomplete**.

## Candidate B — Betfair Exchange as independent hedge venue
Betfair's current international new-customer Exchange page explicitly includes **Azerbaijan** among eligible countries for its Exchange offer and describes the Exchange as peer-to-peer, with both back and lay betting.

Sources:
- https://www.betfair.com/be
- https://support.betfair.com/app/answers/detail/betfair-general-terms-and-conditions/
- https://support.betfair.com/app/answers/detail/exchange-general-rules

Important distinction:
- **do not rely on the Betfair risk-free promotion itself** for a guarantee: Betfair Standard Promotional Terms allow action where a customer becomes able to guarantee wins/profits with no or minimal risk.
- using the ordinary Exchange solely as an independent hedge venue is structurally different. Betfair's general terms prohibit self-matching/collusion/manipulation, but the retrieved ordinary Exchange rules do not create a blanket prohibition on an independently matched external hedge against another bookmaker.

### Settlement mismatch gate
Betfair's general sports rules explicitly warn that when related bets are placed across Betfair products and/or third parties, one bet can be voided while another stands.

Therefore even a perfectly sized pre-event hedge is **not a strict all-outcome guarantee** unless the two selected contracts have settlement rules that are proven compatible for every cancellation, postponement, dead-heat, correction and void branch.

This is now a first-class H044 execution gate.

## Candidate C — Betfair risk-free €10 promo
Current page states:
- Azerbaijan is eligible;
- first Exchange bet must risk at least €10 and settle within 30 days;
- if it loses, Betfair refunds €10.

But Betfair Standard Promotional Terms state that if promotional participation lets a customer guarantee wins/profits with no or minimal risk, Betfair may invalidate transactions and/or withhold winnings.

Status: **REJECTED as terminal surebet subsidy despite Azerbaijan eligibility**.

## Candidate D — eTopaz weekly cashback
Current page states free-bet cashback of 5%/7%/10% based on weekly net losses, max 500 AZN, with x-freebet mechanics and an explicit no-abuse note.

Because acquisition requires realized net losses and the reward itself is a free bet rather than cash, this is weaker than the first-deposit 15% route for strict guarantee research.

Status: **not terminal; retain only as EV/rebate overlay**.

## Candidate E — offshore/global comparison controls
Search surfaced global operators with deposit matches/cashback, but many have one or more of:
- explicit arbitrage/low-risk hedging prohibition;
- high wagering requirements;
- country restrictions;
- bonus balances rather than immediately withdrawable cash;
- discretionary/host-only allocation.

These controls reinforce that H044 should prioritize **local deterministic acquisition + independent non-promotional hedge venue**, not another generic welcome-bonus list.

## Mechanical economics
Let:
- `D` = first deposit;
- `F = 0.15D` = eTopaz free-bet face value;
- `q` = qualifying first-bet stake;
- `Cq` = worst-case cash cost of hedging/settling the qualifying bet;
- `rho` = guaranteed cash-conversion fraction of the free-bet token after external hedge, net of exchange commission/spread;
- `Cf` = fixed execution/FX/withdrawal costs.

Then a necessary condition for a strict positive floor is:

`rho * 0.15D > Cq + Cf`.

This is only a **necessary** economics condition. A terminal proof additionally needs:
- deterministic token credit after a valid first bet;
- current platform minimum qualifying stake/odds;
- accepted deposit/withdrawal route from Azerbaijan;
- two-way matched hedge liquidity before exposure;
- compatible settlement/void rules across both legs;
- no promo/general-term clause permitting clawback specifically because the combined structure is hedged/low-risk;
- all commissions, FX and withdrawal fees included.

## Current conclusion
H044 produced the strongest Azerbaijan-specific acquisition architecture so far:

**eTopaz deposit-linked 15% free bet → ordinary Betfair Exchange external hedge**.

It is **not yet SUCCESS**. The blocker is no longer basic country access or token existence. The remaining blockers are narrow and testable:
1. recover authoritative eTopaz general terms and minimum-bet/odds rules;
2. establish whether promotion entitlement is irrevocable once the first bet settles;
3. choose a specific market pair and prove settlement equivalence across all void/cancel branches;
4. verify current Betfair commission/liquidity and cash-in/out costs from Azerbaijan;
5. compute the worst-case net floor with those real parameters.

If all five gates pass, this branch could move from `promising` to a genuine executable guarantee candidate. Until then terminal state remains **NO SUCCESS; NOT EXHAUSTED**.
