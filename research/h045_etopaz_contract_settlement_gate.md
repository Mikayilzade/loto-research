# H045 — eTopaz contract + settlement-equivalence gate

Updated: 2026-08-16
Status: **H044 strict-guarantee route REJECTED; promo remains EV-only / discretionary**

## Goal
Resolve the two highest-value blockers left by H044:
1. whether eTopaz general terms permit using the 15% first-deposit free bet as part of a deliberately hedged / loss-avoiding construction;
2. whether an eTopaz leg and a Betfair Exchange leg can be treated as a strict all-branch hedge under current settlement rules.

## Primary current sources
- eTopaz Terms & Conditions: https://www.etopaz.az/eng/terms-conditions
- eTopaz Promotions: https://www.etopaz.az/eng/promotions
- eTopaz Football rules: https://www.etopaz.az/eng/betting-rules/football
- eTopaz Table Tennis rules: https://etopaz.az/eng/betting-rules/table-tennis
- eTopaz Baseball rules: https://etopaz.az/eng/betting-rules/baseball
- Betfair Exchange General Rules: https://support.betfair.com/app/answers/detail/exchange-general-rules
- Betfair Exchange Football rules: https://support.betfair.com/app/answers/detail/exchange-football-soccer-rules/
- Betfair Exchange Tennis rules: https://support.betfair.com/app/answers/detail/exchange-tennis-rules/
- Betfair Exchange Baseball rules: https://support.betfair.com/app/answers/detail/exchange-baseball-rules/

## 1. General-terms gate is now recovered
The current eTopaz Terms & Conditions materially change H044.

### Contract language relevant to matched / low-risk use
Article 4.2.1 says the subscriber account/services may be used only for the permitted games and may not be used, among other things, for commercial purposes, for obtaining another income, or for avoiding loss outside the agreement's purpose.

This language is broader than the first-deposit promotion page and creates a direct contractual risk for a construction whose purpose is explicitly to hedge the qualifying/free-bet exposure into a deterministic positive floor.

The same terms also state:
- one account per subscriber;
- BAL LINE may close a subscription without giving a reason (4.5.3);
- game/operator rules may be changed and the subscriber has no compensation claim for those changes (5.2.2);
- BAL LINE may set betting limits (5.2.3);
- the service scope and agreement terms may change (8.1 / agreement-change language);
- winnings are paid after applicable tax/withholding; withdrawals require an account in the subscriber's own name;
- minimum bank-account withdrawal currently stated as 3 AZN (7.5), subject to change.

Separately, the first-deposit promotion itself says the company may change or cancel the promotion at any time.

### Terminal implication
For this project, SUCCESS requires a **strict guarantee**, not merely likely operator tolerance.

A strategy whose positive floor relies on deliberately using eTopaz as one leg of an external hedge cannot be called strictly guaranteed while the governing contract contains language prohibiting use for obtaining other income / avoiding loss and allows discretionary account/promotion changes.

Therefore H044 fails the contract-permission gate even before liquidity, FX, or commission are modeled.

Status: **REJECTED as strict guarantee**.

## 2. Settlement-equivalence gate also fails for the obvious football pair
Even if the contractual problem were ignored, eTopaz and Betfair do not expose identical abandonment/postponement rules.

### eTopaz football
Current football rules state that if a suspended match resumes within 48 hours, open bets are settled on the final result; otherwise unsettled bets are void.

### Betfair Exchange football
Current Exchange rules use a materially different rescheduling/abandonment framework. A postponed match can stand when confirmed for the current/following three days subject to the stated confirmation timing; Betfair's general match rule also uses a three-day completion window where no more specific rule applies.

### Concrete asymmetric branch
A football match is suspended and resumes after more than 48 hours but within Betfair's applicable three-day window / qualifying reschedule conditions.

Then it is possible for:
- eTopaz leg: **void**;
- Betfair leg: **stand**.

The external hedge is therefore not an all-branch identity. A balanced normal-result payoff does not prove a deterministic floor.

Betfair itself explicitly warns that related bets across Betfair and third parties can have one leg void while another stands.

Status: **football settlement-equivalence proof FAILED**.

## 3. Cross-sport recheck does not rescue the architecture
A small current rule screen shows that the mismatch is not a one-off football artifact.

### Table tennis
- eTopaz: postponed/abandoned match not resumed within 48h -> void.
- Betfair default match rule: three-day completion window unless a sport/market-specific rule overrides it.

This leaves the same 48h-versus-3-day mismatch class.

### Baseball
- eTopaz: postponed game generally void unless played on the originally scheduled day; abandoned game can remain live if resumed within 48h.
- Betfair MLB: if it starts and is later abandoned/postponed, official result can remain relevant for up to three days; if it does not start on scheduled date, bets are void.

Again there are branches where the two contracts do not share the same state transition.

### Tennis
Rules differ on retirement/settlement details. eTopaz and Betfair both contain conditional settlement and void rules, but they are not textually identical; no exhaustive equivalence theorem is available from the current generic rules.

Conclusion: switching sports does not remove the need for exact market-by-market settlement proof, and the recovered eTopaz contract gate already rejects strict guaranteed-profit use.

## 4. Promotion economics after the gate
The H044 necessary condition remains mechanically true:

`rho * 0.15D > Cq + Cf`

But it is now only an **EV / promotion-conversion screen**, not a terminal guarantee route, because `rho` cannot be treated as contractually guaranteed under a deliberately hedged use.

The current 15% free-bet offer remains potentially valuable to an ordinary eligible customer, but the project may not promote it to guaranteed arbitrage.

## 5. New general theorem from H045
For any two-operator matched-promotion strategy, a strict guaranteed floor requires **both**:

1. **contract-permission condition**: neither operator may reserve a relevant right to invalidate/claw back the subsidy or bet specifically because the combined use is hedged, arbitrage-like, commercial, income-seeking, or loss-avoiding;
2. **settlement-isomorphism condition**: every reachable event state (normal result, postponement, abandonment, venue change, correction, retirement, dead heat, void, resettlement) must map both legs into payoffs whose combined minimum remains above total cost.

Ordinary matched normal outcomes are insufficient.

## H045 conclusion
**H044 eTopaz 15% free bet -> Betfair Exchange external hedge is REJECTED as a strict guaranteed-profit strategy.**

Two independent blockers are now evidenced:
- eTopaz general-contract language conflicts with deliberate income-seeking / loss-avoiding account use and retains discretionary change/closure powers;
- obvious cross-operator sports pairs have asymmetric void/settlement branches.

This does not invalidate matched betting as an EV technique. It closes this specific Azerbaijan-accessible promotion architecture under the project's strict SUCCESS definition.

## Next research priority
Move away from discretionary bookmaker promotions and search for structures where the subsidy is **already withdrawable cash or legally fixed consideration** before hedging, or where both opposing contracts clear on the same venue/clearing rule set. These reduce the two H045 failure modes.
