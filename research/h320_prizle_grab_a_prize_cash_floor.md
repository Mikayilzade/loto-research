# H320 — Prizle Grab A Prize guaranteed-win cash-floor bound

Updated: 2026-08-27
State: **CLOSED / ZERO-WITHDRAWABLE-CASH-FLOOR**

## Why this was worth testing

After H319, the priority was a genuinely different finite mechanism where every acquired identifier has positive deterministic value rather than an ordinary pool in which most tickets can simply lose. Prizle's current **Grab A Prize** is unusually strong on that dimension: it advertises **8,000 instant prizes for 8,000 instant identifiers**, so every ticket receives an instant prize. The page also publishes a separate £500 end draw.

Current indexed operator data used for this packet:

- 8,000 instant-prize identifiers;
- £4.99 per paid entry;
- maximum 1,000 entries per person;
- every ticket guarantees an instant win;
- instant prizes include cash, products/gift cards and site credit;
- the £500 end-draw prize is withdrawable cash;
- site-credit prizes are credited to the Prizle account and are available for use on competitions.

Source: `https://prizle.co.uk/competitions/grabaprize-4` (current indexed page, checked 2026-08-27).

The Prizle home page also listed Grab A Prize among current competitions when checked: `https://prizle.co.uk/`.

## Exact inventory decomposition

The full published instant schedule decomposes exactly as follows.

### Site-credit-only identifiers

| face value | count |
|---:|---:|
| £25 | 39 |
| £10 | 80 |
| £5 | 1,600 |
| £3 | 502 |
| £2 | 1,779 |
| £1 | 1,000 |
| £0.50 | 1,000 |
| £0.25 | 500 |
| £0.10 | 300 |
| £0.05 | 100 |
| £0.01 | 100 |

Total: **7,000 site-credit-only identifiers**, face value **£16,500**.

### Cash instant identifiers

- 1 × £100;
- 20 × £10;
- 50 × £5;
- 400 × £2;
- 500 × £1.

Total: **971 cash identifiers**, face value **£1,850**.

### Products / gift cards

The schedule contains 17 singleton physical-product prizes plus 12 gift/product identifiers (4 × £25 Just Eat, 4 × £99 AirTag packs, 4 × £25 Costa), for **29 identifiers**. Using every displayed face value gives **£6,508.97**.

Therefore:

`7,000 site-credit + 971 cash + 29 product/gift = 8,000 instant identifiers`.

This exact identity is asserted by the reproducible model.

## Strict cash-floor proof

The target is guaranteed **withdrawable cash**, not advertised prize face value.

The current indexed snapshot showed **6,985 site-credit-only identifiers still available**. This exceeds the one-player cap of **1,000**. Consequently there is a legal allocation in which all 1,000 of one player's entries land on site-credit-only identifiers and none land on a cash or product instant prize.

The separate £500 end draw does not repair the guarantee. A one-player portfolio cannot control the complete 8,000-identifier pool, so there is a legal end-draw outcome won by an external identifier.

Hence:

**strict withdrawable-cash floor = £0.**

This remains true even though the competition literally guarantees an instant prize on every ticket.

## Stronger site-credit stress

For completeness, H320 also asks how much *site-credit face value* is forced if the player buys the maximum 1,000 entries and the adversarial allocation uses the cheapest currently-available site-credit identifiers.

The 1,000 cheapest distinct available identifiers are:

- 100 × £0.01 = £1;
- 100 × £0.05 = £5;
- 298 × £0.10 = £29.80;
- 500 × £0.25 = £125;
- 2 × £0.50 = £1.

Total guaranteed site-credit face under that deliberately favourable interpretation: **£161.80**.

Maximum paid spend is `1,000 × £4.99 = £4,990`, so this floor is only **3.24248497%** of paid spend and is not withdrawable cash. Reusing site credit on another random competition cannot be counted as cash without a separate deterministic conversion theorem.

## Full advertised face sanity check

Valuing all displayed non-cash goods at full displayed face and site credit at full face:

- site credit: £16,500;
- cash instants: £1,850;
- products/gift cards: £6,508.97;
- end draw: £500;
- total displayed face: **£25,358.97**.

This total is not itself a takeover opportunity because the one-player cap is 1,000/8,000 and identifier allocation is random.

## Closure

H320 is **CLOSED / ZERO-WITHDRAWABLE-CASH-FLOOR** for the strict-profit objective.

Reusable lesson: an `every ticket wins` pool is not enough. Before valuing the prize schedule, partition identifiers by **withdrawable-cash floor**. If a zero-cash/nonwithdrawable class contains at least as many still-available identifiers as the player cap, then a one-player strict cash guarantee is impossible unless a separate end-draw/takeover mechanism is itself guaranteed.

## Files

- `src/loto_research/h320_prizle_grab_a_prize_cash_floor.py`
- `data/derived/h320_prizle_grab_a_prize_cash_floor.json`
- `research/H320_VALIDATION.md`
- `research/H320_STATUS.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H320_APPEND.md`
