# H044 — Azerbaijan-accessible promotion + external hedge screen

Updated: 2026-08-16
Status: **strict-guarantee route REJECTED by H045; retain only as EV/promotion architecture**

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

The current page does not state a minimum qualifying first-bet amount or minimum odds in the indexed offer text. That originally made this the strongest local acquisition lead because token size is deposit-linked rather than explicitly qualifying-stake-linked.

## H045 contract result — decisive
The current eTopaz general Terms & Conditions were subsequently recovered:
- https://www.etopaz.az/eng/terms-conditions

Article 4.2.1 contains language preventing use of the account/services for commercial purposes, obtaining another income, or avoiding loss outside the agreement's permitted purpose. The terms also permit account cancellation without a stated reason, operator betting limits, and rule/service changes. The promotion itself can be changed/cancelled at any time.

Under this project's strict SUCCESS definition, the 15% token therefore cannot be treated as an irrevocable subsidy for a deliberately externally hedged guaranteed-profit construction.

Detailed closure:
- `research/h045_etopaz_contract_settlement_gate.md`
- `data/derived/h045_contract_settlement_gate.csv`

Status: **REJECTED as strict guaranteed-profit route; may remain ordinary EV/promotion value for eligible users**.

## Candidate B — Betfair Exchange as independent hedge venue
Betfair's current international Exchange materials include Azerbaijan among eligible countries and the Exchange supports peer-to-peer back/lay betting.

Sources:
- https://www.betfair.com/be
- https://support.betfair.com/app/answers/detail/betfair-general-terms-and-conditions/
- https://support.betfair.com/app/answers/detail/exchange-general-rules

Important distinction:
- Betfair's own risk-free promotion was already rejected because promotional terms allow action where play creates guaranteed/minimal-risk profit.
- ordinary Exchange hedging is structurally different, but that alone does not solve the eTopaz contract gate.

## H045 settlement result — independent second failure
Betfair's rules explicitly warn that related third-party bets can have one leg void while another stands.

The obvious football pair fails an explicit equivalence check:
- eTopaz suspended-match continuation boundary: **48 hours**;
- Betfair Exchange football/general reschedule-completion framework: materially different, including relevant windows up to **three days**.

Therefore a match can occupy a legal branch where eTopaz voids and Betfair stands. Table-tennis/baseball rechecks show similar cross-rule asymmetries.

Status: **cross-operator settlement identity not established; football pair explicitly FAILED**.

## Candidate C — Betfair risk-free €10 promo
Azerbaijan eligibility and cash-refund mechanics were real, but Betfair Standard Promotional Terms allow invalidation/withholding where promotional participation creates guaranteed profit with no/minimal risk.

Status: **REJECTED as terminal surebet subsidy**.

## Candidate D — eTopaz weekly cashback
Free-bet cashback based on weekly net losses remains weaker than first-deposit acquisition for strict guarantees because acquisition itself requires losses and the reward is non-cash free-bet value.

Status: **retain only as EV/rebate overlay**.

## Mechanical economics
Let:
- `D` = first deposit;
- `F = 0.15D` = eTopaz free-bet face value;
- `q` = qualifying first-bet stake;
- `Cq` = worst-case cash cost of hedging/settling the qualifying bet;
- `rho` = cash-conversion fraction of the free-bet token after external hedge;
- `Cf` = execution/FX/withdrawal costs.

Necessary economics condition:

`rho * 0.15D > Cq + Cf`.

This remains useful for EV screening, but H045 shows it is **not sufficient for strict guarantee**, because contract permission/irrevocability and all-branch settlement equivalence fail.

## Final H044 conclusion
The architecture

**eTopaz deposit-linked 15% free bet -> ordinary Betfair Exchange external hedge**

was the strongest Azerbaijan-specific matched-promotion lead found so far, but H045 closes it as a terminal strategy.

Two independent failures now exist:
1. eTopaz general terms conflict with deliberate income-seeking/loss-avoiding account use and retain discretionary powers relevant to the subsidy/execution;
2. cross-operator settlement rules are not isomorphic, with an explicit football 48h-vs-3-day asymmetric branch.

Terminal state remains **NO SUCCESS; NOT EXHAUSTED**.
