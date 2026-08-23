# H238 — Random-tag acquisition bound

Date: 2026-08-24
Status: NOT SUCCESS

## Question

Can repeated purchases under a random pre-draw Doubler/Tripler promotion turn H236's conditional doubled 3-spot construction into a strict guaranteed-profit strategy?

## Model

Let:

- `N = C(80,3) = 82,160` required distinct 3-spot combinations;
- `p` = probability that a purchased ticket receives an eligible 2X-or-better promotional tag;
- `k` = number of independently tagged purchase attempts made for each required combination.

For one required combination, probability of obtaining at least one tagged copy after `k` attempts is

`1 - (1-p)^k`.

Under independent tagging across attempts and combinations, probability that all `N` combinations have at least one tagged copy is

`P_all = [1 - (1-p)^k]^N`.

This formula is deliberately favorable: it assumes stable known `p`, independence, unlimited ability to repeat the exact desired wager, and no draw-close/retailer/transaction bottleneck.

## Strict-guarantee result

For every finite `k` and every `0 < p < 1`, `(1-p)^k > 0`, so the probability that at least one required combination remains untagged is strictly positive.

Therefore repeated random acquisition cannot produce a mathematical 100% guarantee in any finite number of purchases unless the rules provide an additional deterministic bound (for example, every Nth eligible ticket is guaranteed a tag) or `p = 1`.

This alone is sufficient to reject random Tripler Time tagging as the missing guarantee mechanism from H236.

## Near-certainty scale

For illustration, solve for the smallest `k` such that the probability that all 82,160 combinations are tagged is at least `1-epsilon`.

| hypothetical tag probability p | k for total failure < 1e-3 | k for total failure < 1e-6 | k for total failure < 1e-9 |
|---:|---:|---:|---:|
| 1% | 1,814 | 2,501 | 3,188 |
| 5% | 356 | 490 | 625 |
| 10% | 173 | 239 | 305 |
| 20% | 82 | 113 | 144 |
| 50% | 27 | 37 | 47 |

These counts are attempts **per combination**. Total purchase attempts are `N*k`. Even the hypothetical 20% case requires 6,737,120 attempts for only a 99.9% all-covered target, not a strict guarantee.

## Economic consequence

The acquisition attempts themselves cost money unless failed/unmultiplied tickets can be neutralized, refunded, or repurposed without expected loss. Thus repeated acquisition generally worsens economics before transaction/time constraints are considered.

A random free multiplier can improve expected value, but it cannot by itself convert a negative or conditional strategy into a finite deterministic arbitrage whose profit is guaranteed on every execution path.

## Verdict

NOT SUCCESS.

Random ticket-level Doubler/Tripler assignment fails the strict-guarantee criterion for any finite purchasing protocol without a deterministic bounded-assignment rule.

## Next action

H239: search current lottery promotions/rules for deterministic multiplier assignment mechanisms: all-ticket overlays, every-Nth-ticket awards with a known finite N, coupon/rebate schedules, guaranteed bonus windows, or other pre-purchase/predraw conditions that can be forced across a complete coverage set. Prioritize official rule documents over marketing pages.
