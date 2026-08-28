# H337 — WinWink cheap-ticket postal bundle zero-support screen

Checked 2026-08-28.

## Question
Does WinWink's current postal allocation rule create a strict guaranteed-profit bundle when the ticket price is low enough that one compliant postal submission receives multiple tickets?

## Live candidate
`MYSTERY CASH! £5,000 Jackpot prize!`

Current live facts:
- 122,667 total ticket identifiers;
- £0.30 paid ticket price;
- 13,673 pre-committed instant-win identifiers;
- closes 2026-09-05;
- postal entries eligible for instant wins on the same basis as paid entries.

Current WinWink Terms clause 3.13 allocates `floor(second-class stamp cost / ticket price)` tickets, minimum one. Royal Mail's current second-class letter price is £0.91.

Therefore one valid postal submission receives:

`floor(0.91 / 0.30) = 3 tickets`.

This is the first exact k>=2 WinWink postal-bundle screen following H336.

## Exact zero-support bound
The cryptographic commitment states exactly 13,673 instant-win positions among 122,667 total identifiers.

Hence exact non-instant support is:

`122,667 - 13,673 = 108,994 identifiers`.

Because `108,994 >= 3`, there exists a legal three-ticket allocation in which all three postal tickets are non-instant identifiers. That bundle has withdrawable instant cash exactly £0.

Thus even granting a perfectly received and accepted submission and zero postcard/material/labour cost beyond postage:

`worst bundle net <= £0 - £0.91 = -£0.91`.

No instant-prize amount distribution needs to be estimated: the exact committed zero-support count alone is sufficient.

## Validation
- total universe: 122,667;
- committed instant-win positions: 13,673;
- exact zero-instant identifiers: 108,994;
- postal bundle size: 3;
- zero-support capacity for a full bundle: yes;
- arithmetic inconclusive: 0;
- execution inconclusive relevant to rejection: 0;
- strict guaranteed profit: FAIL.

Ordinary postal non-delivery risk remains an additional independent blocker, but is not needed for closure.

## Reusable theorem
For a postal bundle of size `k`, if the eligible identifier universe contains at least `k` zero-withdrawable-cash identifiers and allocation is not controllable by the entrant, then the strict cash floor of the accepted bundle is zero. A positive guaranteed-profit screen therefore requires either fewer than `k` zero-cash identifiers or a deterministic allocation rule that excludes them.

## Verdict
**CLOSED / NOT SUCCESS.** This genuinely tests the new k>=2 branch proposed by H336 and closes it for the current live £0.30 Mystery Cash game with zero arithmetic inconclusive.
