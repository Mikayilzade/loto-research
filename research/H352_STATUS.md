# H352 STATUS — Enable Lottery / Gatherwell additive Super Draw

State: CLOSED / NO SUCCESS
Date: 2026-08-29
Branch: research-work

## Result
The H225-X* exact-family was checked first and remains rigorously CLOSED / EXHAUSTED at H225-X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

H352 tested a genuinely new live additive-promotion mechanism: Enable Lottery weekly tickets (£1 each) currently qualify both for the ordinary weekly lottery and the Gatherwell £2,000 Super Draw closing 29 Aug 2026. The Super Draw permits unlimited entries per person, but the winner is selected by RNG from all eligible entries, including entries from other participating Gatherwell lotteries.

The mechanism cannot yield a strict guaranteed-profit takeover. Existing external eligible tickets already exist. For any player purchase count N>0, there is a legal outcome in which an external eligible entry wins the weekly guaranteed raffle prize and an external eligible entry wins the separate Super Draw. The selected six-digit Game Number does not remove this blocker because the weekly guaranteed prize selection is explicitly ticket-based and each ticket is unique.

Even granting the player the strongest possible six-digit jackpot coverage, a complete 000000–999999 cover costs at least £1,000,000 at £1 per ticket while the advertised jackpot is only £25,000. Thus:
- N < 1,000,000: a legal six-digit winning number can be outside the player's set; combined guaranteed cash floor can be £0; net <= -N.
- N >= 1,000,000: grant the full £25,000 jackpot as guaranteed; the weekly guaranteed prize and Super Draw can still both go to external entries; net <= £25,000 - N <= -£975,000.

Arithmetic inconclusive: 0.
Closure-relevant inconclusive: 0.

## Evidence
- Enable Lottery game rules: https://www.enablelottery.org.uk/game-rules
- Live Enable Lottery page / current Super Draw rules: https://www.enablelottery.org.uk/

## NEXT ACTION
Continue outside H225-X*. Prioritize additive subsidies where the extra payment is made per winning entry or where all eligible identifiers/entries can be deterministically monopolized at bounded cost. Random single-winner promotions over an open external-entry pool are now pre-screened out unless a binding mechanism can eliminate every external eligible entry before the draw.
