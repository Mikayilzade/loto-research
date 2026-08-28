# H338 — WinWink cheap postal-bundle grand-prize cap theorem

Checked 2026-08-28.

## Question
Can WinWink's current £0.20 games exploit Terms 3.13 so that one £0.91 second-class postal submission receives four tickets and creates a strict guaranteed-profit route even when the competition has only a single grand prize?

## Live candidates
### Armageddon
- total identifiers: 2,000;
- £0.20 per paid ticket;
- maximum 300 tickets per person;
- one £200 grand prize;
- no instant-win layer;
- draw 2026-08-30;
- postal deadline 2026-08-29.

### Necromunda Skirmish
- total identifiers: 1,000;
- £0.20 per paid ticket;
- maximum 150 tickets per person;
- one £90 grand prize;
- no instant-win layer;
- draw 2026-09-02;
- postal deadline 2026-09-01.

## Postal allocation
Current WinWink Terms clause 3.13: valid postal submissions receive `floor(second-class stamp / ticket price)` tickets, minimum one. With current second-class postage £0.91 and ticket price £0.20:

`k = floor(0.91 / 0.20) = 4`.

## Exact cap proof
For a grand-prize-only finite identifier game, strict cash profit from random ticket allocation requires controlling every identifier that can legally win the only cash-convertible prize. If the per-person cap C is less than universe size N, then at least N-C identifiers remain outside the entrant's portfolio, hence an external grand-prize-winning draw state remains legal and the entrant's cash floor is £0.

Armageddon: `N=2000`, `C=300`, external support at least `1700` IDs.
Necromunda: `N=1000`, `C=150`, external support at least `850` IDs.

Therefore both games admit an explicit legal outcome with zero entrant prize cash. Since postage is positive, guaranteed net is strictly negative before adding postcard, handwriting or labour costs.

## Validation
- both candidates are open/live at check time;
- both have exactly one published grand prize and no instant-win schedule;
- both per-person caps are published and strictly below total IDs;
- k=4 is exact under current £0.91 / £0.20 Terms formula;
- arithmetic inconclusive: 0;
- no delivery/processing assumption is needed for rejection, because even a perfectly accepted entry has a zero-cash legal branch.

## Verdict
**CLOSED / NOT SUCCESS.**

## Reusable theorem
For any finite grand-prize-only random-ID competition with total identifiers N and entrant cap C<N, a postal bundle multiplier k cannot create strict guaranteed cash profit by itself. The entrant retains a legal zero-prize branch because at least N-C eligible winning identifiers are external. Reopen only if the prize structure gives every possible allocated ID a positive cash floor or C>=N and full-universe acquisition is otherwise executable.
