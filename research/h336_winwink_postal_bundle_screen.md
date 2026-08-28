# H336 — WinWink live provably-fair postal bundle screen

## Question
Can WinWink's unusual free-postal allocation rule plus an `Every Ticket Wins` instant-win universe create a strict guaranteed cash profit?

## Sources checked on 2026-08-28
- Live competition: `https://winwink.co.uk/competitions/pokemon-mega-pack-charizard-rip-1`
- Current terms: `https://winwink.co.uk/terms`
- Royal Mail current 2nd Class sheet pricing (25 stamps for £22.75 => £0.91 each): `https://shop.royalmail.com/scotland-country-definitives-full-sheet-25-x-2nd-class`

## Mechanism
The current WinWink terms allocate each valid postal submission a number of tickets equal to:

`floor(second-class stamp cost / competition ticket price)`, with a minimum of one ticket.

This is materially different from the one-postcard-one-ticket rule used by many UK operators and could, for sufficiently cheap games, create a deterministic bundle subsidy.

For the checked Charizard competition:
- paid ticket price = £2.50;
- second-class stamp = £0.91;
- postal allocation = max(1, floor(0.91 / 2.50)) = 1 ticket.

## Exact live universe
The competition states 7,274 tickets and pre-commits 7,274 instant-win positions. Published prize counts reconcile exactly:

| class | count | cash value used |
|---|---:|---:|
| Shiny Charizard GX PSA 10 | 1 | £916 |
| Charizard EX PSA 10 | 1 | £541 |
| Charizard V ACE 10 | 1 | £250 |
| Charizard SWSH260 ACE 10 | 1 | £217 |
| Charizard VStar Japanese PSA 10 | 1 | £167 |
| £100 cash | 3 | £100 |
| Crown Zenith PSA 10 | 1 | £75 |
| Charizard Promo PSA 9 | 1 | £67 |
| Rainbow PSA 9 | 1 | £62 |
| £50 cash | 8 | £50 |
| £25 cash | 20 | £25 |
| £20 cash | 15 | £20 |
| £10 cash | 60 | £10 |
| £5 WinWink credit | 200 | £4 cash alternative |
| £2 WinWink credit | 800 | £2 cash alternative |
| £1 WinWink credit | 1,500 | £1 cash alternative |
| 50p WinWink credit | 1,445 | £0.42 cash alternative |
| 10p WinWink credit | 3,215 | £0.08 cash alternative |

Totals:
- identifiers = **7,274 / 7,274**;
- all-cash-alternative liability = **£9,159.10**;
- arithmetic inconclusive = **0**.

## Strict bound
One postal submission gets one random/pre-committed identifier. There are 3,215 legal identifiers whose withdrawable cash alternative is £0.08.

Even before postcard material and labour:

`minimum accepted-entry net <= £0.08 - £0.91 = -£0.83`.

Therefore strict guaranteed cash profit is impossible for this live game.

## Independent execution blockers
The current terms also say:
- lost/delayed/non-delivered entries are at entrant risk;
- tracked, signed-for and premium-rate postage is not valid for free entry;
- postal entries must arrive by the stated cut-off;
- entries must be handwritten;
- the promoter may disqualify conduct contrary to the spirit/intention of the competition.

These are not needed for the arithmetic rejection, but independently prevent upgrading the postal route into a deterministic guaranteed-delivery channel.

## Reusable result
WinWink's postal formula should be screened whenever `ticket price < second-class stamp price`, because one postcard can then allocate multiple tickets. The correct guarantee test is not average value: compute the **worst possible cash sum over every bundle of k allocated identifiers** where `k = floor(stamp/ticket_price)`, then compare that bundle floor with complete postal marginal cost. H336 only has k=1 and fails immediately.

## Verdict
**CLOSED / NOT SUCCESS.** Zero arithmetic inconclusive; explicit legal below-cost branch remains.