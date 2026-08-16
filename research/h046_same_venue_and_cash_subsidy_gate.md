# H046 — same-clearing-venue arbitrage + deterministic cash-subsidy gate

Updated: 2026-08-16
Status: **same-market arbitrage validated mechanically but rejected as terminal strict guarantee; sampled deterministic-cash subsidy routes do not establish Azerbaijan-executable guaranteed profit**

## Goal
Test the two highest-priority routes left by H045:
1. remove cross-operator settlement mismatch by putting all hedge legs inside one clearing venue / one market;
2. find a cash-like subsidy that is contractually earned independently of risky replay and can therefore turn a zero/low-risk hedge into strictly positive cash profit.

The project terminal standard is stronger than ordinary arbitrage language: every reachable execution/settlement branch must leave **strictly positive net profit**, not merely non-negative capital preservation.

## A. Same-market exchange dutching theorem
Consider a single mutually-exclusive/exhaustive exchange market with decimal back odds `o_i` on every outcome. Let total stake be `S` and choose stakes

`stake_i = K / o_i`

with equalized gross return `K`. Then

`S = K * sum_i(1/o_i)`

so

`K = S / q`, where `q = sum_i(1/o_i)`.

If all bets are fully matched and `q < 1`, pre-commission profit in every ordinary settled outcome is

`P = K - S = S * (1/q - 1) > 0`.

Betfair states that Exchange commission is charged on **net winnings on a market**, and not on a net losing market. If the ordinary outcome profit is equalized and positive, commission rate `c` gives

`P_net = (1-c) * P`.

Thus a fully matched same-market book with `q < 1` is a genuine post-fill surebet under normal settlement and avoids the H045 problem of two operators applying different event rules.

### Official mechanism support
Current Betfair Exchange rules explicitly describe:
- matching back and lay bets;
- cross-selection matching inside a market;
- cross-market matching for equivalent selections;
- price-time priority for competing unmatched liquidity.

Current Betfair commission documentation states commission is applied to net market winnings.

Sources:
- https://support.betfair.com/app/answers/detail/exchange-general-rules
- https://support.betfair.com/app/answers/detail/a_id/413/
- https://www.betfair.com/aboutUs/Betfair_Charges.html

## B. Decisive strict-guarantee failure: whole-market void
The same authoritative Exchange framework also preserves reachable branches in which:
- Betfair may void certain bets or a whole market for integrity/fairness reasons;
- sport-specific abandonment/non-start rules can void all still-undetermined bets;
- when a single bet is void, stake is returned.

If all legs of our same-market dutch are voided together, all stakes are returned. Ignoring deposit/withdrawal friction, terminal net profit is exactly:

`0`.

The project's SUCCESS definition requires **strictly positive** net profit in every reachable branch. Therefore:

> A same-market fully matched exchange arbitrage is a validated normal-settlement surebet, but it is **not a terminal strict guarantee** because the full-market-void branch collapses profit to zero.

This is materially stronger than H045: settlement isomorphism is no longer the issue; the common clearing rule itself contains a zero-profit state.

Additional source:
- https://support.betfair.com/app/answers/detail/betfair-general-terms-and-conditions/

## C. Execution gate remains independently important
Even before the void theorem, an apparent exchange arb visible in the order book is not guaranteed until all required legs are irrevocably matched at sufficient depth. Betfair rules state first-come-first-served matching among orders at equal price and note that unmatched bets can be cancelled. Therefore a pre-click screenshot of `q<1` is not proof of executable profit.

H020's fee/depth scanner remains useful for ordinary post-fill arbitrage research, but it cannot by itself satisfy terminal SUCCESS.

## D. Deterministic cash-subsidy screen
### Betfair Points / commission discount
Current official Betfair documentation says customers earn Betfair Points from Exchange activity and those points can reduce future commission. This is a fee reduction, not withdrawable cash principal. It cannot independently convert the whole-market-void branch into strictly positive cash profit.

Sources:
- https://support.betfair.com/app/answers/detail/385-exchange-what-are-betfair-points1
- https://support.betfair.com/app/answers/detail/414-exchange-what-is-the-discount-rate/

### My Betfair Rewards
Rewards depend on completing monthly wagering goals and then credit bonuses. They are conditional on activity and package/region eligibility, not an irrevocable cash amount earned before risky execution. No Azerbaijan-specific deterministic cash entitlement was established from the current official material.

Source:
- https://support.betfair.com/app/answers/detail/a_id/6801/

### Refer-and-Earn / referral cash
A current official UK/ROI Betfair promotion genuinely pays £10 **in cash** per qualified referral, but:
- it is restricted to UK/Republic of Ireland residence and same-country referrer/referee;
- the referred person must stake £10+ and settle qualifying activity;
- hedging/reduced-liability qualifying bets are excluded;
- promotion terms retain anti-abuse / guaranteed-profit clawback language.

Therefore this is useful evidence that withdrawable-cash promotions exist as a product class, but it is not Azerbaijan-executable and does not provide an unconditional deterministic subsidy controlled solely by our portfolio.

Source:
- https://promos.betfair.com/promotion?promoCode=CACQRAEAUTOUKI&tab=tcs

### Affiliate CPA
Betfair's official affiliate scheme can pay a one-off CPA bounty for newly referred players, but application approval and qualifying third-party acquisition are separate commercial activity. It is not a deterministic wagering subsidy attached to our own hedge and does not satisfy the project's guaranteed lottery/betting-profit criterion.

Sources:
- https://www.betfair.com/aboutUs/Affiliate.Scheme.html
- https://partnerships.betfair.com/

## H046 conclusion
1. **Same-market exchange arbitrage:** mechanically VALIDATED under ordinary settlement after all legs are matched and `sum(1/odds)<1` after fees.
2. **Terminal guaranteed profit:** REJECTED, because a reachable whole-market-void branch returns stakes and produces 0 profit.
3. **Betfair Points/commission rebates:** useful cost reduction, not cash subsidy and cannot repair the zero-profit void branch.
4. **Current cash referral evidence:** real withdrawable cash exists, but sampled official current offer is jurisdiction-restricted, third-party dependent, and has anti-guarantee conditions.
5. **No Azerbaijan-executable irrevocable deterministic cash subsidy has been established in this packet.**

## Strategic implication
The remaining strict-guarantee search must now avoid not only cross-operator settlement mismatch but also any product where a valid cancellation/void branch can merely restore principal. A terminal SUCCESS needs either:
- a separate **irrevocable cash entitlement that survives void/cancellation**, large enough to leave positive net profit; or
- a non-wagering contractual arbitrage with no zero-profit rescission branch; or
- a finite game/promotion whose rules themselves force strictly positive net proceeds after every allowed cancellation/settlement state.

## Next branch
H047 should prioritize **irrevocable post-qualification cash entitlements that survive subsequent wager voids**, regulated rebates/rewards already vested as cash, and any same-clearing products whose cancellation rules explicitly preserve the subsidy. Ordinary free bets, points, discretionary promo credits and pre-fill price discrepancies are already insufficient.
