# H041 — free-bet token conversion through matched lay

Updated: 2026-08-16
Status: **mechanical positive cash-floor VALIDATED after both legs fill; current terminal SUCCESS blocked by bookmaker promotion-abuse / jurisdiction / revocability gate**

## Question
Can a genuinely granted stake-not-returned sportsbook free-bet token be converted into guaranteed withdrawable cash by laying the same outcome on a betting exchange?

This differs from H039/H040. There is no refund branch. The free token itself has zero cash acquisition cost after qualification, and the hedge converts its contingent profit into an outcome-independent cash amount.

## 1. Exact conversion theorem
Let:
- `F` = free-bet token stake; stake is not returned;
- `O_b` = bookmaker decimal odds;
- `O_l` = exchange lay decimal odds;
- `c` = exchange commission on lay winnings;
- `x` = lay stake.

If the bookmaker selection wins:

`P_win = F*(O_b-1) - x*(O_l-1)`.

If it loses:

`P_loss = x*(1-c)`.

Equalizing both branches gives:

`x* = F*(O_b-1)/(O_l-c)`

and deterministic cash profit after both legs are accepted:

`P* = F*(O_b-1)*(1-c)/(O_l-c)`.

For any valid `F>0`, `O_b>1`, `O_l>1`, and `0<=c<1`, this value is strictly positive.

Therefore a **granted, irrevocable, stake-not-returned free-bet token + fully matched compatible exchange lay is mechanically a sure cash conversion**.

Code:
- `src/loto_research/free_bet_conversion.py`
- `tests/test_free_bet_conversion.py`

Sensitivity:
- `data/derived/h041_free_bet_conversion_screen.csv`

## 2. Qualifying cash bet
For cash qualifying stake `Q`, equalized lay is:

`y* = Q*O_b/(O_l-c)`

and the guaranteed qualifier result is:

`Q_floor = -Q + y*(1-c)`.

At nearly equal prices this is approximately zero, usually a very small negative qualifying loss.

## 3. Current Sky Bet welcome-offer screen
Official Sky Bet support page recovered on 2026-08-16 states:
- minimum deposit £5;
- first qualifying bet only **£0.05+**;
- qualifying odds **1/1 (2.00 decimal) or greater**;
- reward **3 x £10 Free Bet tokens**;
- free-bet stakes are not returned;
- tokens expire 30 days after crediting.

Source:
- https://support.skybet.com/app/answers/detail/welcome-offer-sky-bet

Mechanical illustration at bookmaker 2.00 / lay 2.00:
- with 0% exchange commission, each £10 token locks £5; three tokens lock £15; a perfectly matched 5p qualifier is flat;
- with 2% exchange commission, each £10 token locks ~£4.949495; three tokens plus the equalized 5p qualifier lock ~**£14.84798**;
- even at lay odds 2.20 versus bookmaker 2.00 and 2% commission, modeled package floor remains ~**£13.48119**.

These are settlement-mechanics results, not a terminal executable guarantee.

## 4. Independent operator confirmation that matched betting is a real mechanism
Smarkets' current help/education material explicitly describes matched betting as using bookmaker free-bet bonuses plus an exchange lay to cover outcomes and lock in profit.

Sources:
- https://help.smarkets.com/hc/en-gb/articles/115003678149-What-is-matched-betting
- https://news.smarkets.com/education/what-is-matched-betting/

Smarkets also currently advertises 0% exchange commission for 60 days to eligible new UK/IE/Malta users under code `COMMFREE`, subject to its terms.

Source:
- https://help.smarkets.com/hc/en-gb/articles/13242929620893-Trade-with-0-at-Smarkets-for-60-days

This independently validates that the hedge construction is operationally standard, not a purely theoretical artifact.

## 5. Why this is NOT terminal SUCCESS yet
Sky Bet's own general promotion terms explicitly classify attempts to exploit promotions through bets where the customer has **no or limited risk of loss** as promotion abuse, unless absence of risk is itself a key part of the promotion. They reserve the right to withhold promotional amounts/free stakes/bonuses in such cases.

Source:
- https://support.skybet.com/app/answers/detail/general-sky-bet-promotion-terms/

The specific welcome offer also reserves discretion to withhold/restrict/cancel the offer under promotion-abuse and risk policies.

Therefore the mechanical floor is not a **contractual** floor: the free-bet/winnings branch may be clawed back or denied if the bookmaker identifies matched low-risk use.

There is also an access issue: the verified Smarkets commission promotion is UK/IE/Malta-specific, while the project ultimately needs an executable lawful route for the user or a clearly specified eligible participant.

## 6. Necessary conditions for H041 terminal SUCCESS
A current offer can qualify only if all are verified before staking:
1. reward is deterministically earned after a bounded qualifying action;
2. token winnings are withdrawable cash;
3. token stake-not-returned mechanics are explicit;
4. same event/selection can be laid under settlement-compatible rules;
5. sufficient exchange depth is matched before exposure becomes irreversible;
6. bookmaker terms **do not permit void/clawback solely because the position is hedged / low-risk / guaranteed-profit**;
7. exchange terms permit the hedge;
8. KYC/jurisdiction/payment eligibility is lawful and deterministic;
9. commission, FX, tax, void and dead-heat rules leave every settlement branch positive;
10. the qualifying bet itself is hedged or its worst-case loss is below the token-conversion floor.

## Conclusion
**H041 is a stronger result than ordinary +EV:** after credit is valid and both legs are irrevocably accepted, a free-bet token has an exact positive cash floor.

But current verified Sky Bet + Smarkets evidence does not satisfy the project terminal guarantee because the bookmaker side retains an explicit promotion-abuse branch for no/limited-risk play.

Status:
- mechanical theorem: **VALIDATED**;
- real-world matched-betting mechanism: **VALIDATED**;
- current Sky/Smarkets example: **positive mechanical floor, REJECTED as strict contractual guarantee**;
- terminal SUCCESS: **NOT YET**.

## Next highest-value search
Search current bookmaker/free-token offers where:
- the promotion terms explicitly allow hedging/matched betting; or
- the reward becomes irrevocably vested before hedge use and there is no low-risk/arbitrage clawback language.

Do not repeat offers whose incorporated general terms contain a no/limited-risk promotion-abuse clause.
