# H209 — Rhode Island `Kick Back with Keno` public-rule recovery gate

Updated: 2026-08-23
Status: **NO SUCCESS; CURRENT PROMOTION CONFIRMED LIVE, EXACT TERMS NOT RECOVERED**
Scope: LOTTERY ONLY.

## Purpose
H208 closed ordinary Rhode Island retail/SSVM issuance as the **sole** strict-guarantee execution channel for the H173/H175 large same-draw Keno covers. `STATUS.md` therefore made recovery of the exact current `Kick Back with Keno Promotion` rules the highest priority: only materially new promotion terms such as a deterministic pre-draw subsidy plus an execution mechanism curing H207/H208 could reopen the route.

H209 performs that primary-source recovery pass and, importantly, records the exact proof boundary so future runs do not repeatedly infer mechanics from a homepage banner.

## Current primary facts recovered

### 1. The promotion is genuinely current
The official Rhode Island Lottery homepage currently lists **`Kick Back with Keno Promotion`** among its live promotion carousel items.

Primary source:
- Rhode Island Lottery homepage: https://www.rilot.com/en-us/home.html

The homepage therefore validates **existence/currentness only**. It does not expose the promotion's eligibility formula, subsidy, prize multiplier, purchase minimum, location/time restriction, cancellation treatment, issuance process, or atomicity.

### 2. The official current Promotions page does not expose machine-readable rules in the recovered public view
The official `All Promotions` page identifies itself as the page for current promotions, but the recovered public page leaves the live promotion list behind a dynamic loading component and does not return `Kick Back with Keno` mechanics or a rules link in the indexed representation.

Primary source:
- https://www.rilot.com/en-us/player-zone/promotions.html

H209 also searched the official `rilot.com` domain for exact-title variants, `KickBack`, `Kick Back`, `Keno`, `Rules`, `Official Rules`, and the known `/content/dam/interactive/ilottery/pdfs/Promotions/2026/` asset pattern. No current `Kick Back with Keno` rule PDF or campaign-detail page was recovered. The search did recover other 2026 promotion PDFs, confirming that the asset family itself is searchable when indexed.

This is a **data-recovery result**, not evidence that no rules document exists anywhere.

### 3. Current base Keno rules cannot substitute for missing promotion-specific terms
The current official 2026 Keno rules state that a physical Keno ticket may be cancelled only on the same day, from the same terminal, and before the draw; a multi-draw ticket may be cancelled only before its first draw. Registered Ticketless Play and exchange tickets cannot be cancelled.

Primary source:
- current Rhode Island Lottery Rules (official indexed 2026 rules): https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules_2026.pdf

Those annual rules describe ordinary Keno plus the paid `Plus` and `Overtime` features. They do **not** provide recovered `Kick Back with Keno` eligibility/economic terms. Therefore the base-game cancellation clause cannot by itself prove that a promotional Kick Back ticket is cancellable.

### 4. Primary historical precedent proves that RI promotion-specific rules can override ordinary Keno cancellation
The official 2025 `Lucky 3 Spot Keno & Bingo Doubler` rules are especially relevant because this is the same lottery, same Keno game, and the exact kind of pre-draw multiplier architecture needed by H173/H175.

The rules state, among other things:
- qualifying three-spot Keno tickets at the promotion location/time could have prizes doubled;
- eligible tickets printed a pre-draw `Lucky 3 Spot Keno` message;
- retailers could not print eligible tickets in advance of sale;
- **Keno tickets with the Lucky 3 Spot message could not be cancelled.**

Primary source:
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/LaunchAlertRules-Lucky3SpotKenoBingoDoubler.pdf

This is decisive for the proof standard: Rhode Island can and does create promotion-specific cancellation restrictions that are stricter than the base Keno cancellation rule.

## Exact proof consequence
Let a proposed current Kick Back strategy require both:

1. a promotion-specific deterministic subsidy/multiplier/free wager `S`; and
2. the H208 physical rollback architecture to protect against incomplete acquisition of the H173/H175 basket.

The strict guarantee is not established unless a **current promotion-specific primary source** proves all relevant properties, including:

- `S` is deterministic and known/locked before the affected draw;
- the exact eligible wager/spot/price/location/time class covers the intended basket;
- every required promotional ticket remains cancellable or the purchase is otherwise atomic;
- cancellation/refund does not destroy the subsidy in a way that leaves an uncancellable partial basket;
- issuance limits, one-per-player/transaction restrictions, random tagging, or retailer discretion do not break complete ownership;
- the promotion is active at the time of execution.

Because the exact current Kick Back rules are unrecovered, none of these can be assumed from the title.

The 2025 Lucky 3 Spot source additionally blocks a tempting shortcut: **base-game cancellability + a guessed pre-draw doubler cannot be combined as if they were independent rules.** A promotion can explicitly make the doubled ticket non-cancellable.

## H209 search/repetition boundary
The following public-source paths have now been checked and should not be repeated without new evidence/indexing:

- exact phrase `"Kick Back with Keno"` on official `rilot.com`;
- exact phrase plus `Promotion`, `Rules`, and `Official Rules`;
- official `/pdfs/Promotions/2026/` searches for Keno/KickBack variants;
- current Rhode Island homepage carousel;
- current `All Promotions` page;
- current Keno game page / annual Keno rules;
- official historical Keno promotion PDFs for comparable multiplier/cancellation mechanics;
- broad web search for exact-title copies or official social/news mirrors.

Recovered current public evidence still stops at the title/banner.

## Reopen conditions
Reopen `Kick Back with Keno` as an executable strict-guarantee candidate only if one of the following is recovered:

1. the exact current official rules/campaign asset;
2. an official retailer notice/launch alert containing the complete mechanics;
3. an official current campaign page exposing eligibility + prize/subsidy + cancellation/issuance terms;
4. direct operator documentation that resolves those same fields.

A screenshot/banner/title alone is insufficient.

## Result
**ЕЩЁ НЕ УСПЕХ.** The current `Kick Back with Keno Promotion` is officially confirmed live, but its economics and execution terms remain unproved; a primary historical RI doubler shows that promotion-specific rules can explicitly disable Keno cancellation, so no guaranteed subsidy/rollback combination can be inferred from the current banner.