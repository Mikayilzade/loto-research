# H341 — binding free-phone single-winner cap bound

Date: 2026-08-28
State: **CLOSED — NOT SUCCESS**

## Question
H340 established that generic footer language is not enough; this packet asks whether a genuinely contractual non-postal free-phone entry route can itself create a strict guaranteed-profit construction.

## Candidate A — Global Cash Call £700,000
The specific rules for the promotion ending 28 August 2026 explicitly create a **Free Entry Route by phone call**. A participant may make at most **300** free-route entries. After the entry window closes, **one entrant is selected at random from all valid entries**. Simultaneously, paid text and online routes are available, so valid external entries are legally possible.

Thus even granting zero marginal phone cost, there exists a legal outcome where an external entry is selected. Our gross cash in that state is £0.

## Candidate B — Bauer Make Me A Winner £400,000
The current promotion runs through 4 September 2026. Its specific rules allow up to **250 phone entries** per entrant. It also accepts paid SMS, online and RCS entries. After closing, **one entrant from all valid entries** is selected by automated random draw.

Again, any legal external entry preserves a draw state in which the winner is external. Our gross cash floor is therefore £0.

## Exact theorem
For a promotion with:
- one prize awarded to one randomly selected valid entry;
- entrant portfolio size `m` bounded by a finite per-person cap;
- at least one legally possible valid entry outside our portfolio;
- no deterministic consolation payment to every valid entry;

there exists a legal draw state with player gross `0`.

Hence `worst_case_profit <= -acquisition_cost`. Under the strongest possible cost assumption, `acquisition_cost = 0`, so the strict-profit floor is at most exactly `0`, never `> 0`.

This proof does not require estimating total entries, odds, expected value, or the actual number of external entrants. It needs only the legal possibility of one external valid entry.

## Validation accounting
- Global player free-entry cap: 300.
- Bauer player phone-entry cap: 250.
- Global prize count: 1.
- Bauer prize count: 1.
- External-entry branch legally available in both: yes.
- Worst-case player gross in both: £0.
- Arithmetic inconclusive: 0.
- Execution inconclusive relevant to closure: 0.

## Result
**CLOSED / NOT SUCCESS.** Genuine free-phone entry removes postage and postal-loss friction, but ordinary finite-cap single-winner public draws still have a zero-cash legal branch. Repeating more examples of this exact structure cannot produce a strict guarantee.

## NEXT ACTION
Search for a non-postal free-entry mechanism with one of these stronger properties: every reachable allocated identifier carries withdrawable cash; the valid identifier universe has a hard finite cap that one entrant may fully acquire; or a multi-winner/allocation rule gives a strictly positive minimum cash payment to the entrant's whole capped portfolio even with external entrants.

Sources checked:
- https://winplus.heart.co.uk/competition/cashcall/terms-and-conditions
- https://www.winplus.co.uk/competition/13037/cash-call
- https://makemeawinner.co.uk/campaign/MAKEMEAWINNER400K_WINHAPPY
- current Bauer specific terms mirrored in search result for the 4 Sep 2026 promotion
