# H036 — Irish Plus full coverage + active OLG targeted bonus screen

Updated: 2026-08-16
Status: **NO guaranteed-profit strategy found; three additional structural branches closed/screened**

## Why this packet
The current priority is deterministic discount/rebate/subsidy combined with fixed or finite payout structures. This packet therefore tests:
1. Irish Daily Million Plus full-space coverage;
2. Irish EuroMillions Plus full-space coverage;
3. current OLG targeted lottery-bonus promotions that superficially resemble 100% rebates.

The standard is strict guarantee, not merely positive EV.

---

## 1. Daily Million Plus — complete 6/39 coverage
Official current page states:
- 6 numbers from 1–39, plus one bonus number in the draw;
- play from EUR1;
- Plus top prize EUR500,000, shared if necessary;
- lower awards: 5+bonus EUR5,000; 5 EUR250; 4+bonus EUR50; 4 EUR15; 3+bonus EUR5; 3 EUR2 Scratch Card.

Primary source:
- https://www.lottery.ie/game-information/daily-million-plus

Full 6/39 space:

`C(39,6) = 3,262,623` lines.

For a fixed realized draw (6 main + 1 bonus), complete coverage produces the exact ticket counts:
- 6 main: 1
- 5 main + bonus: 6
- 5 main: 192
- 4 main + bonus: 480
- 4 main: 7,440
- 3 main + bonus: 9,920
- 3 main: 99,200.

At EUR1 per line, total cost is EUR3,262,623.

Deliberately favorable valuation, granting the entire EUR500,000 top prize to our unique winning line and valuing the EUR2 Scratch Card at full EUR2 face value:

`gross = 500,000 + 6*5,000 + 192*250 + 480*50 + 7,440*15 + 9,920*5 + 99,200*2`

`gross = EUR961,600`.

Optimistic return:

`961,600 / 3,262,623 = 29.4732%`.

Because the EUR500,000 top prize is shareable, a strict pre-draw cash floor cannot safely credit the entire headline top prize. Removing it gives only EUR461,600, or **14.1481%** of cost.

Conclusion: **REJECTED guaranteed-profit full coverage**.

---

## 2. EuroMillions Plus — complete 5/50 coverage
Official current Irish page states:
- Plus uses the first five EuroMillions main numbers;
- top prize EUR500,000, subject to prize limits;
- 4 matches pays EUR2,000;
- 3 matches pays EUR20;
- top-prize odds 1 in 2,118,760.

Primary source:
- https://www.lottery.ie/game-information/euromillions-plus

The 5-number space is:

`C(50,5) = 2,118,760`.

Complete coverage against any realized 5-number main draw produces:
- 5 matches: 1 line;
- exactly 4: `C(5,4)C(45,1)=225` lines;
- exactly 3: `C(5,3)C(45,2)=9,900` lines.

At an EUR1 Plus stake per line, cost is EUR2,118,760.

Even granting the full EUR500,000 top prize:

`gross = 500,000 + 225*2,000 + 9,900*20 = EUR1,148,000`.

Optimistic return:

`1,148,000 / 2,118,760 = 54.1826%`.

The non-top fixed cash component is only EUR648,000 = **30.5839%** of cost. Prize limits/sharing cannot improve the guarantee.

Conclusion: **REJECTED guaranteed-profit full coverage**.

---

## 3. Current OLG targeted lottery bonuses — real subsidy, not guaranteed cash rebate
Fresh official OLG pages expose an unusually important live promotion class.

### A. LOTTO MAX: buy at least CAD6, receive CAD6 LOTTO MAX bonus
Official terms are dated June 22, 2026 through March 31, 2027. A selected eligible participant must opt in and spend at least CAD6 on LOTTO MAX within 24 hours. The reward is a CAD6 LOTTO MAX-specific bonus.

Critical constraints:
- targeted: participant must have been selected by OLG;
- one redemption during the promotion period;
- reward capped at CAD6 regardless of spend;
- reward is game-specific bonus funds, not withdrawable guaranteed cash;
- the bonus itself must be risked on lottery tickets and can return zero.

Primary source:
- https://www.olg.ca/en/promotions/lottery/retention/buy-a-lotto-max-get-lotto-max-lottery-bonus.terms.html?bonusId=3612

At the minimum qualifying spend the *face-value* subsidy equals 100% of paid spend, but the strict guaranteed cash value of the bonus is still zero before it is wagered because the resulting ticket can lose.

### B. LOTTO 6/49: buy at least CAD3, receive CAD3 game-specific bonus
Official current OLG page similarly advertises a CAD3 LOTTO 6/49 bonus after at least CAD3 qualifying spend.

Terms likewise cap the reward at CAD3 and allow redemption only once during the promotion period.

Primary sources:
- https://www.olg.ca/en/promotions/lottery/retention/buy-a-lotto-649-get-lotto-649-lottery-bonus.html
- https://www.olg.ca/en/promotions/lottery/retention/buy-a-lotto-649-get-lotto-649-lottery-bonus.terms.html?bonusId=3613

### C. LOTTO MAX: buy CAD18, receive CAD6
A second current targeted structure provides CAD6 bonus after at least CAD18 LOTTO MAX spend: a 33.33% face-value subsidy at the minimum spend. It remains targeted, capped and non-cash.

Primary source:
- https://www.olg.ca/en/promotions/lottery/retention/buy-lotto-max-get-a-lotto-max-lottery-bonus.terms.html?bonusId=4018

### D. Birthday bonuses
Current OLG birthday bonus pages show additional targeted free lottery-bonus value, including a CAD10 promotion valid July 1–December 31, 2026. These are useful as zero-acquisition-cost EV overlays for an eligible individual, but still do not create guaranteed cash profit because the bonus must be used on lottery play and can lose.

Primary source:
- https://www.olg.ca/en/promotions/10-lottery-bonus-birthday-gift.html

## Structural conclusion from the OLG promo class
These promotions are genuine deterministic **face-value subsidies conditional on account eligibility**, so H009 should not treat all bonuses as merely random contests.

However they fail the terminal guarantee criterion for two separate reasons:
1. **bonus conversion risk** — game-specific bonus funds are not cash and the purchased ticket can pay zero;
2. **scale cap** — the one-time CAD3/CAD6/CAD10 reward cannot subsidize a full finite-space coverage portfolio enough to erase normal lottery takeout.

This is still strategically valuable: if a future promotion offers withdrawable cashback, a guaranteed-value voucher, or an uncapped/repeatable bonus, it should be screened immediately.

---

## Code / reproducibility
- `src/loto_research/irish_plus_and_promo.py`
- `tests/test_irish_plus_and_promo.py`
- `data/derived/h036_irish_plus_and_olg_promo_screen.csv`

The Daily Million base-game calculation already existed in H024; the H036 test reproduces that identity only as a regression/control and does not claim a new branch.

## H036 final status
- Daily Million Plus full coverage: **REJECTED**.
- EuroMillions Plus full coverage: **REJECTED**.
- OLG targeted `buy X → receive lottery bonus` class: **REAL SUBSIDY, but REJECTED as standalone guaranteed-cash strategy under current caps/conversion rules**.
- Terminal project state remains **NO SUCCESS; NOT EXHAUSTED**.
