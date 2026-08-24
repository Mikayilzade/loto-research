# H255 — UK Lotto lower-tier boost covering-design impossibility

Date: 2026-08-24
Status: NOT A SUCCESS
Scope: lottery-only

## Question
Can a deterministic lower-tier promotion, such as the historical UK Lotto **Match 3 = £100** special event, be converted into guaranteed profit with a partial combinatorial covering design, avoiding full-space jackpot-sharing problems?

## Mechanism
UK Lotto uses 6 numbers from 59 at £2 per line. Historical special events have boosted Match 3 from £30 to **£100** while retaining the ordinary higher fixed tiers. A covering-design idea is attractive because the subsidy is paid directly into a lower tier and does not require the no-jackpot-winner branch.

Historical mechanism source checked:
- https://www.national-lottery.com/news/saturdays-lotto-draw-must-be-won

## Exact averaging theorem
For any fixed 6-number ticket, over all `C(59,6)=45,057,474` possible main-number draws, the exact-Match-3 probability is

`C(6,3) C(53,3) / C(59,6) = 0.010398274878880249`.

Therefore even a £100 Match-3 prize contributes only

`£100 × p3 = £1.039827487888025`

of average cash per £2 ticket.

Including the ordinary fixed cash tiers in the player's favor:
- Match 4 = £140;
- Match 5 = £1,750;
- Match 5 + Bonus = £1,000,000;

produces total average fixed cash of only

`£1.2493332404741555` per £2 line = **62.4667%** of stake.

This gives a stronger impossibility result than testing individual covering designs. For any multiset/portfolio of such tickets, total payout averaged uniformly over all possible draws equals the sum of the per-ticket averages by linearity. If the portfolio had strictly positive cash profit on **every** draw, then its average payout would necessarily exceed its total cost. But the average fixed cash return is only 62.4667% of cost. Contradiction.

Thus no partial covering design, wheel, multiplicity pattern, or unequal ticket weighting built solely from these additive fixed tiers can guarantee positive cash profit on every draw.

## What this does not close
The theorem does not apply if an additional nonlinear mechanism is present, for example:
- jackpot/rolldown money that is externally accumulated and forced into these tiers;
- a rebate/free-entry subsidy whose deterministic cash-equivalent value is large enough to cross the hurdle;
- a promotion that pays an externally funded amount based on portfolio-level conditions rather than independently per ticket.

Those require separate analysis.

## Reproducibility
- `src/loto_research/h255_uk_lotto_match3_boost_impossibility.py`
- `data/derived/h255_uk_lotto_match3_boost_impossibility.json`

## Conclusion
**NOT A SUCCESS.** A large fixed Match-3 boost is not enough: even under £100 Match-3 and favorable inclusion of higher fixed tiers, the additive average cash return is only 62.4667%, which rules out an all-draw guaranteed-profit covering portfolio.
