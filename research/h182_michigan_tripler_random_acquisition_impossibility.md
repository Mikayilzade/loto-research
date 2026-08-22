# H182 — Michigan Tripler Time random-acquisition impossibility

Updated: 2026-08-22
Status: **CURRENT EX-ANTE GUARANTEE REJECTED / CONDITIONAL TAGGED-TICKET STATE RETAINED**

## Purpose
H181 found a live August 2026 Michigan Club Keno promotion in which a free `DOUBLER` or `TRIPLER` entitlement, once printed on a ticket, is known before the covered Club Keno drawings and persists across all drawings on a multi-draw ticket. H182 tests the missing acquisition question: can a player guarantee obtaining such a tagged ticket at bounded external cost?

## Current official evidence
### 1. August 2026 promotion is explicitly random
Michigan Lottery's current promotions page states that for a limited time in August 2026 **random Club Keno tickets** print with a `DOUBLER` or `TRIPLER` message.

Current official promotion page:
- https://www.michiganlottery.com/promotions/current-promotions

The issuer-operated 2026-07-30 announcement independently says tickets are eligible at no additional cost and that **if a player receives** a Doubler or Tripler message, eligible Club Keno, Plus 3 and Kicker prizes are multiplied. A multi-draw ticket carrying the message applies the multiplier to eligible winnings for all drawings on that ticket.

Official announcement:
- https://milotteryconnect.com/2026/07/30/club-keno-tripler-time-gives-players-a-chance-to-double-and-triple-their-winnings-13/

### 2. Official retailer material confirms the same random-ticket mechanism
The 2026 May Tripler Time retailer communication, from the Michigan Lottery asset host, explicitly says:
- `RANDOM CLUB KENO TICKETS WILL PRINT WITH A DOUBLER OR TRIPLER MESSAGE`;
- valid winning tickets carrying the message receive the multiplier;
- on a multi-draw ticket, all eligible winnings in all drawings on that ticket are doubled or tripled.

Official retailer PDF:
- https://assets.ctfassets.net/d6o62jwe1jlr/5JFKDislMnMvZ0k0bib3UZ/efda9c1905cb4ed244aa2d4130fc4a63/tt_may_rcp.pdf

The August public page uses the same `random Club Keno tickets` mechanism. No current primary source recovered in this packet publishes a deterministic Nth-ticket rule, minimum tag frequency, finite without-replacement allocation, or maximum number of untagged tickets between tags.

### 3. Tag is not publicly observable before purchase commitment
Michigan Lottery's current official Club Keno purchase instructions say the player completes a playslip and then takes it to the retailer **to pay and get the ticket printed**. The Doubler/Tripler entitlement is a message on the printed ticket.

Official current FAQ:
- https://faq.michiganlottery.com/in-store-games-information-baceb743/in-store-draw-games-faq-2612cd91/club-keno-eab11f0a/how-to-play-club-keno-f8d62e6b

The same FAQ states Club Keno is in-store only, wagers can be $1-$20 per draw, and one ticket can cover 1-60 consecutive drawings.

No official current rule was found allowing the player to preview the random promotional tag before committing payment, or to cancel/refund a paid untagged Club Keno ticket merely because no promotional message printed.

## Random-acquisition impossibility theorem
Consider any ex-ante strategy that begins before the first qualifying Club Keno ticket is purchased and requires at least one free Doubler/Tripler tag to create its positive deterministic overlay.

Let `T_i` denote whether qualifying purchase `i` receives a usable promotional multiplier.

Under the public August 2026 rules:
- `T_i` is assigned to **random tickets**;
- no deterministic upper bound `N` is published such that at least one of `T_1,...,T_N` must be tagged;
- no player-controlled pre-payment observation mechanism is published.

### Finite purchase strategy
For every finite purchase cap `N`, the public rules do not exclude the branch

`T_1 = T_2 = ... = T_N = no tag`.

Therefore a finite strategy cannot prove possession of the multiplier entitlement that its guaranteed-profit theorem requires.

### Buy-until-tag strategy
A strategy of repeatedly buying until a Tripler/Doubler appears has no published finite worst-case stopping time. For any proposed finite cost cap, the public rules permit a longer all-untagged sequence. Hence the external acquisition cost has no certified finite upper bound.

A strict guaranteed-positive-net-profit strategy requires a bounded worst-case cost. Therefore `buy until random tag` fails the project guarantee criterion even if the probability of eventually obtaining a tag is very high.

### Why multi-draw persistence does not cure acquisition
A tagged multi-draw ticket is valuable because one printed multiplier persists for up to the ticket's future drawings. But persistence starts **after** the random tag has been obtained. It multiplies conditional value; it does not create a finite ex-ante acquisition bound.

## Interaction with ordinary Keno wagers
The failed acquisition purchases are not refundable promotional probes: they are ordinary paid lottery wagers. Their stochastic prize value cannot be counted as guaranteed recovery of acquisition cost.

For strict-guarantee purposes, a legal branch can combine an arbitrarily long sequence of untagged purchases with unfavorable Keno outcomes on those purchases. Thus their external cash cost cannot be ignored or replaced by expected value.

This conclusion does not require knowing the exact Doubler/Tripler probability. A positive probability estimate could support an EV strategy, but cannot create a deterministic worst-case stopping bound.

## Result
- Current August 2026 Tripler Time: **LIVE and free on qualifying tagged tickets**.
- Multiplier entitlement after printing: **observable pre-draw and persistent across a multi-draw ticket**.
- Tag acquisition: **explicitly random** under current official evidence.
- Published deterministic issuance floor / Nth-ticket rule / bounded waiting rule: **NONE FOUND**.
- Pre-payment tag preview: **NONE FOUND; current FAQ describes pay then printed ticket**.
- Ex-ante strict guaranteed-profit use of Tripler Time: **REJECTED under current public executable conditions**.

This closes H181 as a current **guaranteed subsidy source**. The tagged-ticket state remains a legitimate conditional state for EV/conditional-overlay research, but it must not be called a guaranteed acquisition.

## Reopen only if new primary evidence establishes at least one of
1. a deterministic maximum number of purchases before a Doubler/Tripler must print;
2. a finite without-replacement tag allocation visible to the player with a certified remaining-tag count;
3. a lawful pre-payment preview/reservation of the promotional tag;
4. a guaranteed no-cost cancellation/refund of every untagged probe before draw exposure;
5. another deterministic player-owned subsidy that does not rely on the random tag.

## Next research
Return highest priority to lottery mechanisms whose profitable state is guaranteed **before cash commitment**: continue H180/H175 exact block-design separation and scan smaller-state pre-locked doublers or deterministic scheduled modifiers. Do not spend additional runs estimating Michigan Tripler probabilities unless new evidence supplies a hard issuance bound; probability alone cannot satisfy SUCCESS.
