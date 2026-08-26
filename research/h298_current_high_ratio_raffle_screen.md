# H298 — current high-ratio hard-capped raffle screen

Checked: 2026-08-27
State: **CLOSED for checked candidates / NO SUCCESS globally**

## Goal
Continue the finite/reservable-pool lane after H297, but focus on current pools whose published prize liabilities are materially closer to the exact cost of buying every issued entry. The test deliberately gives the player the impossible-favorable assumption of owning the full ticket universe from inception. If even that state is below cost, real execution cannot produce a strict guaranteed profit.

## 1. Chelsea Fire Company Liberty Street Raffle — strongest H298 near-miss
Source: Town of Wappinger July 2026 newsletter, https://content.govdelivery.com/accounts/NYTWAPPINGER/bulletins/41e781c

Published terms in the municipal newsletter:
- USD 100 per ticket;
- only 250 tickets;
- 33 cash prizes totaling USD 20,000;
- main drawing 2026-11-07;
- five USD 100 early-bird prizes were scheduled for 2026-08-01.

Exact impossible-perfect takeover:
- full acquisition: `250 * 100 = USD 25,000`;
- all advertised cash liabilities, including the already-past early-bird prizes: `USD 20,000`;
- gross ratio: `20,000 / 25,000 = 80.0000%`;
- deficit: `USD 5,000`.

This is intentionally stronger than a purchase begun on 2026-08-27 because it still credits the five early-bird prizes. Removing those already-resolved USD 500 of liabilities would lower the current upper bound to 78% if the original 250-ticket cost basis were retained. Thus no execution detail can push the published cash-prize takeover above break-even without a separate deterministic subsidy worth more than USD 5,000 on the full pool.

## 2. PACC St. Jude raffle
Source: Polish American Citizens Club announcements, https://www.paccalbany.com/announcements

Published current terms:
- 500 tickets maximum;
- USD 10 each;
- prizes USD 1,500 + USD 1,000 + USD 500 = USD 3,000;
- drawing 2026-09-12.

Full takeover: USD 5,000 cost vs USD 3,000 cash liabilities = **60.0000%**, deficit USD 2,000.

## 3. Tour de Cure — The 100 Club
Source: RaffleTix current draw page, https://www.raffletix.com.au/the100club2026

Published current terms:
- only 100 tickets;
- cash prizes AUD 1,000 + AUD 300 + AUD 200 = AUD 1,500;
- packages: 1 for AUD 50, 3 for AUD 120, 6 for AUD 210;
- draw 2026-11-02.

Exact integer minimization over the published packages gives the cheapest way to acquire exactly 100 entries as:
- 16 six-entry packs = 96 entries for AUD 3,360;
- 1 three-entry pack = AUD 120;
- 1 single = AUD 50;
- total = **AUD 3,530**.

Thus perfect takeover returns `1,500 / 3,530 = 42.4929178%`, deficit AUD 2,030.

## 4. Henley Sharks Great White Raffle
Source: Henley Sharks official club site, https://www.henleysharks.com.au/

Published current terms:
- AUD 10,000 grand prize;
- only 500 tickets;
- AUD 100 per ticket;
- draw 2026-09-26.

Cash-only full-pool ratio is `10,000 / 50,000 = 20%`. The ticket also includes six drinks and food, so it is not a pure lottery-price observation. H298 does not assign those consumption benefits a cash/resale value; therefore this candidate is not used as the strongest mathematical rejection. The cash liability itself is nevertheless far below acquisition cost.

## Validation / conclusion
The executable model in `src/loto_research/h298_current_high_ratio_raffle_screen.py` asserts all prize sums, the Tour de Cure package optimum, and that every checked full-pool ratio is below 1. Derived values are stored in `data/derived/h298_current_high_ratio_raffle_screen.json`.

Best checked candidate is Chelsea Fire at **80.0%** even under a stronger-than-current assumption that credits already-scheduled early-bird liabilities. H298 therefore finds no strict guaranteed-profit takeover.

## NEXT ACTION
Prioritize current hard-capped pools only when published deterministic player-facing liabilities are near or above 80% of the exact cheapest full-acquisition cost. A Chelsea-like pool becomes interesting only with a documented deterministic discount/subsidy above 25% of acquisition cost (strictly more than USD 5,000 on USD 25,000), or with additional guaranteed liabilities not already included in the USD 20,000 total. Avoid repeating H297/H298 candidates absent materially changed official economics.
