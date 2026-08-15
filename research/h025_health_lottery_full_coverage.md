# H025 — The Health Lottery full-space coverage

Updated: 2026-08-15
Status: **Big Win + Wednesday/Saturday Free Prize Draw REJECTED; All Or Nothing REJECTED**

## Goal
Continue fast analytic coverage screens on current finite/fixed-prize games, prioritizing structures with deterministic subsidy. The Health Lottery is unusually relevant because Wednesday/Saturday Big Win entries automatically receive a second £100,000 Free Prize Draw entry at no additional price.

## Sources checked
Current operator pages (August 2026):
- Big Win / player guide: https://www.healthlottery.co.uk/players-guide/
- Big Win FAQ: https://www.healthlottery.co.uk/faq/
- All Or Nothing: https://www.healthlottery.co.uk/aon/

Current published mechanics:
- Big Win: choose 5 of 50; £1 per line; draw also has one Bonus Ball.
- Main prizes: 5 = £25,000*; 4+Bonus = £10,000; 4 = £300; 3+Bonus = £50; 3 = £10; 2+Bonus = £5; 2 or 1+Bonus = free ticket.
- `*` Match-5 top prize is shared if multiple winners.
- Wednesday/Saturday: every £1 Big Win line automatically enters an additional 5-of-50 Free Prize Draw; Match 5 shares a £100,000 cash prize; no lower prizes.
- All Or Nothing: choose 12 of 24; £1 per line; prizes symmetric around 6 matches; 12 or 0 = £25,000*; 11/1 = £250; 10/2 = £25; 9/3 = £2.50; 8/4 = £1; 5/6/7 = no win. Top prize is shared if multiple winners.

# 1. Big Win full space on Wednesday/Saturday
Buy every 5-subset of 50 exactly once.

`S = C(50,5) = 2,118,760` lines, therefore cost = **£2,118,760**.

For any realized 5-main + 1-bonus draw, exact counts in our portfolio are deterministic:
- 5 mains: `1`
- 4 mains + Bonus: `C(5,4)=5`
- 4 mains, no Bonus: `C(5,4)*44=220`
- 3 mains + Bonus: `C(5,3)*44=440`
- 3 mains, no Bonus: `C(5,3)*C(44,2)=9,460`
- 2 mains + Bonus: `C(5,2)*C(44,2)=9,460`
- 2 mains, no Bonus: `C(5,2)*C(44,3)=132,440`
- 1 main + Bonus: `C(5,1)*C(44,3)=66,220`

Cash from fixed main-draw tiers, while granting our Match-5 ticket the full £25,000 despite possible external sharing:

`£25,000 + 5*£10,000 + 220*£300 + 440*£50 + 9,460*£10 + 9,460*£5 = £304,900`.

The two free-ticket tiers produce `132,440 + 66,220 = 198,660` free tickets. To create an intentionally favorable upper screen, value each at full face value **£1**, even though a free ticket is not withdrawable cash and can itself lose: **£198,660 nominal value**.

Because we also own every 5-subset in the separate Wednesday/Saturday Free Prize Draw, one of our lines necessarily matches its five winning numbers. Again grant ourselves the entire advertised **£100,000**, ignoring external sharing.

Optimistic deterministic package value:

`£304,900 + £198,660 + £100,000 = £603,560`.

Optimistic coverage return:

`£603,560 / £2,118,760 = 28.4865%`.

Optimistic guaranteed deficit:

`£2,118,760 - £603,560 = £1,515,200`.

This is already much stronger than needed for rejection. Real guaranteed cash value is lower because:
- Match-5 prizes may be shared with external winners;
- the £100k Free Prize Draw may be shared;
- free tickets are replay value, not cash, and can return zero;
- execution/capital costs are omitted.

**Conclusion: even the operator-funded second draw does not come remotely close to overcoming full-space acquisition cost. REJECTED.**

# 2. All Or Nothing full space
Buy every 12-subset of 24.

`S = C(24,12) = 2,704,156` lines; cost = **£2,704,156**.

For any realized winning 12-set, a portfolio line has exactly `m` matches in

`C(12,m) * C(12,12-m) = C(12,m)^2`

ways. Thus winner counts are deterministic.

Relevant symmetric counts:
- m=12 or 0: 1 each
- m=11 or 1: `12^2=144` each
- m=10 or 2: `66^2=4,356` each
- m=9 or 3: `220^2=48,400` each
- m=8 or 4: `495^2=245,025` each

For an intentionally favorable rejection bound, treat both m=12 and m=0 tickets as if each received the full £25,000 top prize, even though the operator states that the top prize is shared if there are multiple winners.

Optimistic gross:

`2*£25,000 + 2*144*£250 + 2*4,356*£25 + 2*48,400*£2.50 + 2*245,025*£1`

`= £1,071,850`.

Optimistic deterministic return:

`£1,071,850 / £2,704,156 = 39.6371%`.

Optimistic guaranteed deficit:

`£1,632,306`.

Actual guaranteed return is weaker because the £25,000 top prize is shared and execution costs are omitted.

**Conclusion: REJECTED as guaranteed-profit full-space strategy.**

## Strategic result
H025 closes two more current UK finite structures, including one with a genuine deterministic extra-draw subsidy. This strengthens H021's broader lesson: a free auxiliary draw can be economically real yet still be far too small to compensate for the takeout embedded in buying the entire combination space.

No SUCCESS. Continue fast analytic screens on current finite/fixed-payout/final-draw products; deep-dive only states with deterministic coverage return or external subsidy near/above 100% of cost.
