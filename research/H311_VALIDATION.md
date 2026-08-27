# H311 VALIDATION

Validated: 2026-08-27

## Independent arithmetic checks

Inputs:
- N = 10,000 tickets
- price = £20
- max per person = 499
- snapshot sold = 1,215
- stated prize pot = £200,000
- separately stated end cash prize = £1,000

Checks:
- full acquisition face cost = 10,000 × £20 = **£200,000**;
- deliberately favourable combined liabilities = £200,000 + £1,000 = **£201,000**;
- favourable full-pool gross ratio = **1.005 = 100.5%**;
- maximum one-person identifier control = 499 / 10,000 = **4.99%**;
- even if the player already owned 499 sold IDs, minimum external sold IDs = 1,215 − 499 = **716**;
- remaining inventory at snapshot = **8,785**.

All arithmetic is asserted in `src/loto_research/h311_kilted_lucky_dips_takeover_bound.py` and mirrored in `data/derived/h311_kilted_lucky_dips_takeover_bound.json`.

## Logical validation

The full-takeover positive-economics thought experiment requires control of all relevant finite identifiers. Published rules limit a person to 499 entries, strictly below N=10,000. Existing external sold identifiers also remain possible winners of the RNG end draw. Therefore full deterministic ownership cannot be achieved by one eligible player.

The conclusion does not depend on whether the £1,000 end prize is additive to or included in the £200,000 headline. The report deliberately uses the more favourable additive interpretation and still fails execution.

## Verdict

**H311 CLOSED / TAKEOVER-BLOCKED.**

No SUCCESS claim is warranted.
