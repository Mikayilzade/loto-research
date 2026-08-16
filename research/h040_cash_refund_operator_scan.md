# H040 — current cash-refund operator scan + selective-refund theorem

Updated: 2026-08-16
Status: **no terminal guarantee found; operator class materially narrowed**

## Goal
Extend H039 beyond Betfair. Search current sportsbook cash-refund / money-back offers and apply the contract-first guarantee gate before spending time on hedge optimization.

A terminal candidate must simultaneously have:
1. deterministic eligibility;
2. withdrawable cash refund;
3. refund coverage broad enough to support an all-outcome hedge;
4. irrevocably executable hedge legs;
5. no anti-arbitrage / guaranteed-profit clawback branch;
6. positive net floor after commissions, taxes, FX and settlement rules.

## 1. New theorem — selective refund cannot manufacture a surebet
Suppose we back a selection with stake `S` at bookmaker decimal odds `O_b` and lay the same selection on an exchange at lay odds `O_l` using lay stake `x`. Let exchange commission be `c`.

If the selection wins:

`P_win = S*(O_b-1) - x*(O_l-1)`.

If it loses in a **non-refunded** losing outcome:

`P_bad_loss = -S + x*(1-c)`.

If it loses in a refunded outcome with cash refund `R`:

`P_refunded_loss = P_bad_loss + R`.

Whenever even one legal non-refunded losing outcome remains, the refund cannot improve the worst losing branch. Strict positive profit requires both:

`x > S/(1-c)`

and

`x < S*(O_b-1)/(O_l-1)`.

Such an `x` exists iff:

`(O_b-1)*(1-c) > (O_l-1)`.

That is already an ordinary bookmaker-vs-exchange arbitrage condition **without counting the promotion**.

### Consequence
A cash-refund promotion limited to selected losing states (for example, only a horse finishing 2nd–4th/5th) can improve EV and reduce downside, but it cannot by itself create a strict all-outcome sure profit if other losing states remain.

Implemented in:
- `src/loto_research/promo_hedge.py`
- `tests/test_promo_hedge.py`

## 2. Current operator screen
Data:
- `data/derived/h040_cash_refund_contract_screen.csv`

### bet365
Current/general promotion language and Azerbaijan-facing general terms explicitly treat all-outcome guaranteed-profit / arbitrage betting as prohibited activity or allow promotional value to be reclaimed when the offer is used to create guaranteed profit.

Sources:
- https://help.az.bet365.com/sk/terms-and-conditions
- https://www.bet365.com/promos/en-gb/home/5612-westham-arsenal-moneyback

Status: **REJECTED contract gate**.

### Paddy Power
Official help currently describes a first-bet **Money Back as Cash if You Lose** offer: stake refunded as cash up to GBP10/EUR10 for eligible new customers in the UK or Republic of Ireland.

This is mechanically the right refund form, but Paddy Power promotion/general terms permit invalidation/withholding where a promotion allows guaranteed wins/profits with no or minimal risk.

Sources:
- https://helpcenter.paddypower.com/app/answers/detail/a_id/10047/
- https://www.paddypower.com/aboutUs/Terms.and.Conditions/

Status: **REJECTED contract gate and not Azerbaijan-accessible under stated eligibility**.

### Sky Bet — important partial exception, but current cash offer still fails
Sky Bet General Promotion Terms prohibit exploiting promotions with no/limited risk **except where absence of risk is a key part of the promotion**. This is the most interesting contract wording found in this packet because it shows an operator can explicitly carve out a promotion designed to remove risk.

However the current official Money Back as Cash horse-racing examples refund only specified losing finishing positions (for example 2nd–5th) rather than every losing state. Under the selective-refund theorem above, this cannot create a strict surebet unless an independent bookmaker/exchange arbitrage already exists.

The specific promotion terms also preserve eligibility / promotion-abuse discretion.

Sources:
- https://support.skybet.com/app/answers/detail/general-sky-bet-promotion-terms/?mobile=1
- https://promos.skybet.com/promotion?promoCode=SOMRNVHRFL280726

Status: **REJECTED current guarantee; retain the explicit-risk-exception wording as a future lead**.

### BetVictor
Current First Bet Shield refunds a losing first bet using Free Bets, not withdrawable cash. Free-bet stake is not returned and the token cannot be cashed out.

Source:
- https://www.betvictor.com/en-en/offer/ASE3

Status: **REJECTED refund-form gate**.

### BetMGM
Current first-bet offer returns a losing qualifying wager as Bonus Bets. Official terms state Bonus Bets are nonwithdrawable and their stake is not returned.

Source:
- https://www.az.betmgm.com/en/engage/lan/sports/first-bet-offer

Status: **REJECTED refund-form gate**.

### FanDuel
No-Sweat / Bet Back offers return value as nonwithdrawable Bonus Bets and are restricted to selected regulated US jurisdictions.

Source:
- https://www.fanduel.com/research/fanduel-nfl-promo-offer-choose-your-reward-for-nfl-games-today-1-25-26

Status: **REJECTED refund-form/access gate**.

## 3. Strategic result
H039's theoretical cash-refund surebet mechanism remains valid, but the current operator search shows two recurring blockers:

1. **true full cash refunds** tend to be paired with anti-guaranteed-profit / minimal-risk clauses; or
2. offers avoid cash entirely and pay **free bets / bonus bets**, whose cash floor is not equal to face value.

The new selective-refund theorem closes a third apparent route: limited-place horse-racing refunds do not create strict guarantees unless the underlying odds already form an arbitrage.

## 4. What remains genuinely open
The best future H039/H040 target is now much narrower:
- full losing-stake refund in **withdrawable cash**;
- refund applies to every losing outcome of the qualifying bet;
- operator terms explicitly permit or do not reserve clawback for matched/minimal-risk play;
- offer available in a jurisdiction the user can lawfully access;
- both sides can be fully hedged before event risk.

Sky Bet's phrase excluding cases where absence of risk is explicitly the key part of a promotion is a useful contract template. A future promotion that combines that exception with a full cash-loss refund would deserve immediate re-opening.

## Current conclusion
**NO SUCCESS.** The cash-refund surebet class is scientifically valid but no currently verified offer in this expanded operator screen satisfies both the mechanical and contractual guarantee gates.
