# H195 — Rhode Island Keno bulk-cart interface differential

Updated: 2026-08-23
Status: **NO SUCCESS; EXECUTION GATE MATERIALLY HARDER**
Scope: LOTTERY ONLY.

## Question
Does the current Rhode Island iLottery interface expose any public mechanism that could plausibly aggregate the 4,336 independently specified H175 Keno 3-spot selections into a small number of same-draw checkout objects?

## Fresh official evidence
Fresh retrieval on 2026-08-23 from the official Rhode Island Lottery site shows a product-level UI difference.

### iKeno
The current Keno purchase page exposes exactly one four-step wager flow:
1. `Pick your numbers`
2. `Amount per game`
3. `Consecutive games`
4. `Select Game Options`

The visible purchase action is `Buy Now`. The page does **not** expose a `QTY` selector or `Add to cart` control for Keno. It also states that ticket purchases cannot be canceled or refunded.

Source: https://www.rilot.com/en-us/keno.html

### Mega Millions control
The current Mega Millions purchase page on the same Rhode Island Lottery platform visibly exposes:
- `QTY`
- `Add to cart`
- `Buy Now`
- `Activate Subscription`

Source: https://www.rilot.com/en-us/megamillions.html

This same-site control matters: cart/quantity capabilities are not merely hidden from all lottery product scrapes. They are explicitly rendered for Mega Millions while absent from the rendered Keno purchase flow.

## Execution implication
H194 already corrected the mistaken interpretation that the $150 Keno ticket maximum proves 150 different same-draw selections can be packed into one object. H195 adds product-specific interface evidence against that packing assumption.

Under the **currently observable public iKeno flow**, each independently specified H175 selection must be treated as requiring its own wager submission unless new authoritative evidence proves otherwise.

Required H175 selections: **4,336**.
Required H173 selections: **4,560**.

Using a deliberately generous full 4-minute (240-second) draw interval as the entire executable purchase window gives lower-bound submission rates:
- H175: `4336 / 240 = 18.0667` independent completed wager submissions per second.
- H173: `4560 / 240 = 19.0000` independent completed wager submissions per second.

If the usable wagering window is shorter because of draw cutoff/processing latency, the required rate is higher. The live Keno page observed a next-draw clock and separate wagering-open time, but H195 does not assume an exact universal cutoff window from one transient page state.

## What this proves / does not prove
### Supported
- Current public iKeno renders a single-selection purchase flow with `Buy Now` and no visible Keno `QTY` or `Add to cart` control.
- The same official platform does render `QTY` and `Add to cart` for Mega Millions, so their absence on Keno is meaningful product-specific evidence.
- No public bulk builder or batch cart for thousands of arbitrary Keno same-draw selections has been recovered through H195.
- Without such a mechanism, H175/H173 execution requires thousands of independent submissions in minutes.

### Not proved
- This is **not** a formal theorem that hidden retailer-terminal batching, undocumented operator tooling, private API endpoints, or privileged syndicate interfaces cannot exist.
- No authoritative maximum transactions-per-second or explicit prohibition on automated/batch Keno purchase has been recovered.
- Therefore execution is materially implausible under the public interface but not formally impossible.

## Promotion control
The official Rhode Island Lottery homepage still displays `Kick Back with Keno Promotion` in fresh August 2026 retrieval. However, the homepage also contains a generic `Get a free ticket when you buy 2` callout whose navigational association could not be reliably tied to Keno: the rendered carousel/link mapping is dynamic and one recovered click resolved to Mega Millions. H195 therefore does **not** attribute that free-ticket wording to the Keno promotion.

## Result
**ЕЩЁ НЕ УСПЕХ.** H195 materially hardens the execution blocker: current iKeno lacks the cart/quantity controls that the same platform exposes for Mega Millions, leaving H175 at at least 4,336 separately specified wager submissions and a conservative required throughput of 18.07 submissions/second over four minutes. Exact Kick Back with Keno terms and any non-public/batch execution mechanism remain unresolved.
