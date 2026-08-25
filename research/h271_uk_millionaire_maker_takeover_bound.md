# H271 — UK EuroMillions Millionaire Maker finite-code takeover screen

Date: 2026-08-25
State: **CLOSED / REJECTED for strict guaranteed-profit takeover under checked rules**

## Why this mechanism was opened

The UK EuroMillions add-on is unusually relevant to the current NEXT ACTION. It is a guaranteed-winner raffle attached to every UK EuroMillions entry, and the current National Lottery material explicitly describes a £1,000,000 winner-facing prize with reserve-fund support/top-up. This is genuine external prize funding rather than a mere relabelling of the ordinary EuroMillions main prize pool.

The Gambling Commission EuroMillions game specification says each EuroMillions entry automatically takes part in UK Millionaire Maker and receives a raffle number; the winner is selected randomly from the automatically generated raffle numbers. Current National Lottery material keeps the retail EuroMillions price at £2.50 per line.

## Exact arithmetic

For the ordinary UK Millionaire Maker prize of £1,000,000:

- raffle-only break-even acquisition count at £2.50 per EuroMillions line: `£1,000,000 / £2.50 = 400,000` lines;
- strict positive gross from the raffle prize alone would therefore require control of every eligible raffle code while buying at most **399,999** paid lines;
- the EuroMillions main outcome matrix is `C(50,5) * C(12,2) = 139,838,160` lines;
- buying one copy of every main outcome would cost **£349,595,400**;
- one £1m Millionaire Maker prize is only **0.2860449537%** of that main-space acquisition cost.

The main-space cover is not itself the target takeover; it is included to show that covering EuroMillions numbers does not economically or structurally substitute for controlling the separate raffle identifiers.

## Structural blocker — stronger than the arithmetic

The decisive issue is ownership, not average value.

Raffle codes are **automatically generated** for sold EuroMillions entries and the raffle draw selects from those generated codes. The player does not choose the code. Therefore a strict guarantee requires the portfolio to own **every generated valid raffle code for that draw**.

If even one eligible code is externally owned, there is a legal raffle outcome in which that external code is selected. In that outcome the portfolio receives **£0** from Millionaire Maker. This is a direct counterexample to any claim that buying a large but non-monopolizing set of EuroMillions lines forces the £1m subsidy.

The syntactic code namespace does not fix the problem: the draw is from generated participating codes, not from a pre-published finite inventory that can be reserved or bought out. Public EuroMillions sales continue to generate additional eligible codes until sales close. No checked rule gives a player a mechanism to reserve all future codes, prevent outside issuance, or choose specific raffle identifiers.

## European Millionaire Maker note

Special European Millionaire Maker events can award multiple €1m prizes and use generated codes across participating countries. That is an even stronger external subsidy, but it does not repair the takeover condition: UK main-number coverage does not control foreign generated codes, and any uncontrolled participating code preserves a legal external-winning outcome. Reopen only if a special event publishes a hard, reservable identifier inventory or another rule that makes total code ownership certifiable before the draw.

## Conclusion

H271 validates a useful filter:

> Guaranteed-winner raffles are attractive only when the eligible identifier set is both finite **and controllably monopolizable**. A guaranteed prize is not a guaranteed portfolio payout when the organiser keeps generating unique identifiers for outside purchasers.

Under the checked UK EuroMillions / Millionaire Maker rules, strict guaranteed-profit takeover is therefore rejected.

## Sources checked

- UK Gambling Commission, Schedule 3 Game Specification — EuroMillions / UK Millionaire Maker: automatic raffle entry and random selection from generated raffle numbers.
- The National Lottery current EuroMillions pages / responsible-play material: £2.50 per line.
- The National Lottery current wording: £1,000,000 Millionaire Maker / European Millionaire Maker treatment and reserve-fund top-up.
- National Lottery winner material: each ticket receives a unique raffle code.

## Reproducibility

- `src/loto_research/h271_uk_millionaire_maker_takeover_bound.py`
- `data/derived/h271_uk_millionaire_maker_takeover_bound.json`
