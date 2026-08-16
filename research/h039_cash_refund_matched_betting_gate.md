# H039 — cash-refund / matched-betting guarantee gate

Updated: 2026-08-16
Status: **mechanical arbitrage exists; strict guarantee rejected where promo terms permit clawback for guaranteed/minimal-risk play**

## Question
Can a deterministic cash-refund gambling promotion be converted into guaranteed positive cash by hedging all sporting outcomes?

This is stronger than ordinary free-play EV. A cash refund can have face-value cash floor if the qualifying bet loses, so in principle a two-sided hedge can create an all-outcome profit.

## Live relevant offer found — Betfair Exchange, Azerbaijan eligible
Betfair currently publishes a new-customer Exchange offer on its international site:
- accounts registered in **Azerbaijan** are explicitly eligible;
- promo code `EXCN10`;
- first Exchange bet within 30 days must risk at least **€10** and settle;
- if that qualifying bet loses, Betfair states it will refund **€10 in cash**;
- unmatched, unsettled or voided bets do not qualify.

Primary offer page:
- https://www.betfair.com/rs

The same page was freshly retrieved on 2026-08-16 and states `Bet €10 and if you don't win, we'll refund you in cash` and lists Azerbaijan among eligible countries.

## Mechanical hedge theorem
Let:
- `S` = qualifying back-bet stake;
- `O > 1` = decimal odds;
- `L` = opposing lay stake at the same odds;
- `R` = cash refund if the qualifying back bet loses;
- ignore commission for the first identity.

If the backed selection wins:

`P_win = (S-L)(O-1)`.

If it loses:

`P_lose = -S + L + R`.

For the advertised case `R=S`, choose any `0 < delta < S` and set:

`L = S-delta`.

Then:
- `P_win = delta*(O-1) > 0`;
- `P_lose = S-delta > 0`.

Thus **if** both opposing positions are irrevocably valid and the cash refund is contractually unconditional after a qualifying loss, an S-sized cash-refund offer admits a strict positive-profit hedge. Commission merely requires `delta` large enough that the winning branch remains positive after commission; it does not remove the mechanism.

This is a genuine constructive arbitrage theorem, not an EV argument.

## Why the live Betfair offer is NOT terminal SUCCESS
Betfair's current Standard Promotional Terms expressly create a contractual failure branch.

The official General Terms page incorporates the Standard Promotional Terms. Section `4. Irregular play` states that if Betfair becomes aware of a customer who, while participating in a promotion, becomes able to **guarantee wins and/or profits with no or only minimal risk**, Betfair may close the account, invalidate transactions/game play, and/or withhold winnings.

Primary terms:
- https://support.betfair.com/app/answers/detail/betfair-general-terms-and-conditions/

Therefore the exact hedge that mathematically converts the refund into a sure profit can itself trigger operator remedies. That makes the promotional payment legally/operationally non-deterministic from the research program's strict guarantee perspective.

Additional evidence: Betfair's promotion-exclusion guidance says patterns indicating promotion abuse or activity against the spirit of promotions may cause immediate exclusion. Some other Betfair promotional pages state even more directly that guaranteed-profit use can lead to reclaiming the bonus element.

## Necessary contract gate for future matched-promo SUCCESS
A promo-hedge may count as terminal SUCCESS only if all of the following are established before execution:
1. eligibility is deterministic and already satisfied;
2. qualifying and hedge bets can both be fully matched/accepted before event risk begins;
3. settlement rules for both legs are identical enough to eliminate mismatch/void branches, or those branches are separately hedged;
4. refund/rebate is withdrawable cash, not bonus credit;
5. refund amount and timing are fixed;
6. **terms do not reserve a clawback/void/exclusion right specifically for guaranteed-profit, matched, arbitrage, minimal-risk or irregular play**;
7. commissions, FX, deposit/withdrawal charges, taxes and capital requirements leave every branch strictly positive;
8. no account/market limit can reduce one hedge leg after the other has become irrevocable.

If condition 6 fails, mathematical surebet is not a strict executable guarantee under PROJECT_RULES.

## Broader promo scan notes
### OLG / Virginia / Georgia style lottery credits
Current/recent operator programs reviewed remain lottery-only credits/free play rather than withdrawable cash. H038 already proves that such credits retain zero cash floor unless they can fully cover a finite outcome space with positive minimum cash payout.

### Bet365-style money-back/free-bet offers
Current official terms found generally pay losses as Bet Credits rather than cash and/or include promotion-abuse provisions aimed at guaranteed-profit constructions. They are therefore weaker than the Betfair cash-refund example for the strict-guarantee target.

### Prize-linked deposit lotteries
Current Azerbaijan bank promotional lotteries were also surfaced (e.g. Xalq Bank `Əmanət` lottery). They can attach a free random-prize chance to an interest-bearing deposit, but the lottery component itself has a zero-prize branch. Guaranteed deposit interest is ordinary deposit return, not a guaranteed lottery edge, so it is tracked as an adjacent passive-income mechanism rather than terminal lottery SUCCESS.

## Conclusion
H039 produces an important distinction:
- **mathematical matched-promo arbitrage:** VALIDATED;
- **current executable strict guarantee from the Betfair Azerbaijan cash-refund offer:** REJECTED because the operator's incorporated promotional terms explicitly reserve remedies against guaranteed/minimal-risk profit patterns.

Future cash-refund promotions should be screened contract-first. A genuinely unconditional withdrawable-cash refund without an anti-arbitrage clawback clause would immediately become a top-priority candidate because the constructive hedge proof is already complete.
