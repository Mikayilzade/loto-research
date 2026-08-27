# H305 — The Giveaway Guys current capped cash-draw takeover screen

Date checked: 2026-08-27
Status: **CLOSED / TAKEOVER-BLOCKED**

## Why this packet

H304's NEXT ACTION asked for electronically reservable finite pools where one eligible player can control nearly all or all identifiers, or where a free/discounted route uses the same finite inventory with a sufficiently large cap. The Giveaway Guys is relevant because current competition pages publish a finite ticket count, a per-person cap, paid online allocation, and a free postal route into the same competition.

## Current draws checked

| Draw | Pool | Max/person | Paid price | Prize | Impossible full-buyout cost | Prize/cost | Max controllable fraction |
|---|---:|---:|---:|---:|---:|---:|---:|
| £6,767 cash — 6 Sep 2026 | 20,195 | 500 | £0.67 | £6,767 | £13,530.65 | 50.0124% | 2.4759% |
| £4,444 cash — 4 Sep 2026 | 20,195 | 500 | £0.44 | £4,444 | £8,885.80 | 50.0124% | 2.4759% |
| £2,500 cash — 28 Aug 2026 | 6,995 | 250 | £0.70 | £2,500 | £4,896.50 | 51.0569% | 3.5740% |
| £750 cash — 28 Aug 2026 | 1,195 | 30 | £1.29 | £750 | £1,541.55 | 48.6523% | 2.5105% |

The £2,500 draw is the strongest ownership case, but the player can control at most 250/6,995 = **3.5739814%** of identifiers. At the cap, **6,745** legal external identifiers remain.

## Strict guarantee result

For every checked draw, `max_per_person < pool_size`. Therefore even granting perfect acquisition of every entry allowed to one person, at least one uncontrolled ticket number remains. That uncontrolled identifier is a legal winning result. Hence the draw-prize worst-case cash floor for the player's capped portfolio is exactly **£0**.

This is stronger than an EV objection: it is a direct admissible-outcome obstruction. No assumptions about sales rate, randomness quality, or other players' behavior are needed.

## Free-entry route does not fix the cap

The live competition pages state that free postal entries are limited to one competition entry per postcard and remain subject to the **same maximum number of entries per entrant shown on the individual competition page**. They are entered only if the prize draw is not already full when the postcard is received. Thus the free route neither raises the ownership cap nor creates electronic reservation certainty.

This means the H302 postal-delay blocker is still present, while the per-person cap independently kills takeover even if every mailed entry arrived successfully.

## Secondary full-buyout economics

Even under the impossible stronger assumption that the cap disappeared and one player could own all identifiers, the advertised cash prize is only about **48.65%–51.06%** of paid face acquisition cost in these four examples. Thus a paid full takeover would still be below break-even.

## Sources

- £6,767 current draw: https://thegiveawayguys.co.uk/products/6-767-cash-1
- £4,444 current draw: https://thegiveawayguys.co.uk/products/4-444-cash-10
- £2,500 current draw: https://thegiveawayguys.co.uk/products/2-500-tax-free-cash-37
- £750 current draw: https://thegiveawayguys.co.uk/products/750-cash-27

## Reproducibility

- `src/loto_research/h305_giveaway_guys_cap_screen.py`
- `data/derived/h305_giveaway_guys_cap_screen.json`

## Terminal decision

**H305 CLOSED / TAKEOVER-BLOCKED.** Do not revisit this operator's ordinary fixed-odds cash draws unless a materially different draw is published with either (a) per-person ownership cap equal to the full finite inventory, or (b) a separate electronically reservable free/discount route that can legally consume essentially all identifiers. A mere postal free-entry route subject to the same small cap is insufficient.

## NEXT ACTION

Continue the H304/H305 search theme, but require at screening time:

1. finite hard cap `N`;
2. player cap close to `N` (preferably exactly `N`), **or** electronic no-purchase entries that reserve from the same pool with cap close to `N`;
3. guaranteed winner / liabilities that survive undersell;
4. exact acquisition economics capable of crossing 100% before spending time on execution details.
