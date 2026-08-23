# H202 — Rhode Island `Kick Back with Keno` promotion attribution gate

Updated: 2026-08-23
Status: **NO SUCCESS; PROMO LIVE, EXACT MECHANICS STILL UNRESOLVED**
Scope: LOTTERY ONLY.

## Target
Continue H201 from the highest-priority live branch: recover exact current official mechanics for Rhode Island Lottery's active `Kick Back with Keno Promotion`, and test whether currently visible promotional copy establishes a deterministic Keno subsidy usable by H173/H175.

## Fresh official evidence
The current Rhode Island Lottery homepage, crawled on 2026-08-23, explicitly lists **`Kick Back with Keno Promotion`** among its active/current promotional carousel items. This confirms that the promotion itself is live/current.

The same official site also exposes the copy **`Get a free ticket when you buy 2`** elsewhere on the homepage. However, following that live official link resolves to the Rhode Island Lottery **Mega Millions** purchase page, not to Keno and not to a Keno promotion-rules document.

Therefore the visible `buy 2 -> free ticket` wording cannot safely be attributed to `Kick Back with Keno` from the current public page structure. Treating it as Keno terms would be an unsupported inference.

Fresh searches of the official RI Lottery domain for the exact promotion title and likely 2026 promotion-rule PDF paths returned the homepage/current-promotion listing but no indexed rules document or text exposing:
- promotion dates;
- eligible Keno spot sizes;
- minimum wager;
- whether the reward is deterministic or randomized;
- whether the free ticket uses the player's selected numbers or Quick Pick;
- whether the reward applies to the same draw or a future draw;
- whether it is retailer-only, iLottery-only, or both;
- per-player/per-day/per-ticket caps;
- whether Plus/Overtime wagers qualify;
- cancellation/disqualification clauses.

## Why this matters for H173/H175
H173/H175 need a subsidy that is both mathematically sufficient and known/owned before the relevant draw. A generic `buy 2 get 1 free` could materially reduce base cost if it truly applied deterministically to eligible 3-spot Keno selections, but H196 already showed that even an optimistic deterministic 2-paid/1-free benefit **alone** is insufficient to make the undoubled H173 cover strictly profitable.

More importantly, H202 establishes that the current visible `Get a free ticket when you buy 2` phrase is not evidence of Keno eligibility at all. It must not be used in any Keno guarantee calculation unless an official promotion rule or Keno-specific page ties the phrase to `Kick Back with Keno`.

## Exact classification after H202
- `Kick Back with Keno Promotion` active/current: **CONFIRMED**.
- `Get a free ticket when you buy 2` visible on current RI Lottery site: **CONFIRMED**.
- that phrase belongs to `Kick Back with Keno`: **NOT PROVED; current live link routes to Mega Millions**.
- deterministic Keno free-ticket entitlement: **NOT PROVED**.
- pre-draw 2x/free-doubler entitlement compatible with H173/H175: **NOT PROVED**.

## New non-repeat rule
Do not cite the homepage `Get a free ticket when you buy 2` text as a Keno subsidy unless a new official source explicitly associates it with Keno. Future work must recover the promotion detail/rules endpoint, archived official copy, retailer material, or another primary RI Lottery source.

## Sources
- Current official RI Lottery homepage/current carousel: https://www.rilot.com/en-us/home.html
- Current official homepage alternate portal rendering: https://www.rilot.com/content/portal/en/home.html?vm=r
- Official link reached from `Get a free ticket when you buy 2`: https://www.rilot.com/en-us/megamillions.html
- Current RI Lottery Keno rules: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules2026.pdf

## Verdict
**ЕЩЁ НЕ УСПЕХ.** `Kick Back with Keno` is definitely live, but its exact subsidy mechanics remain unrecovered; the tempting `buy 2 -> free ticket` homepage copy currently routes to Mega Millions and cannot be credited to Keno.
