# H005 — nonlinear portfolio / pricing / promotion overlay screen

Updated: 2026-08-15
Status: **no terminal guarantee found; important nonlinear subclasses screened**

## Goal
Search mechanisms that evade the H012a linear-portfolio impossibility theorem. A candidate must alter acquisition cost, payout, outcome support, or add an external subsidy. Mere packaging of the same variants is not enough.

## Structural taxonomy
A nonlinear overlay can matter only through one or more of:
1. **discounted acquisition**: constituent plays cost less in a system/bundle than separately;
2. **bounded subsidy**: cashback, deposit match, free-ticket credit, coupon or loyalty value;
3. **conditional rebate**: refund/credit in losing states;
4. **extra prize layer**: second-chance/promotional draw attached to ordinary play;
5. **payout cap/floor/rolldown**: portfolio changes how a shared or accumulated pool is allocated;
6. **inventory state**: remaining-prize composition changes conditional economics;
7. **cross-market hedge/arbitrage**: another market pays against lottery outcomes.

A strict all-outcome profit guarantee requires the combined payoff floor to exceed total net acquisition cost. Positive EV alone is not sufficient.

## Current evidence screen

### A. Azerbaijan system packaging
Current 4+4 public rules expose 5+5 and 6+6 system play, which generate 25 and 225 base variants respectively. The project has not recovered authoritative evidence of a price below the sum of constituent variants. Without a genuine discount, system packaging does not break linearity. Single systems are already guarantee-rejected because legal 0+0 outcomes pay zero.

**Status: no nonlinear price edge demonstrated; exact price remains a data item for full-space 4+4.**

### B. Azerlotereya bonuses/campaigns
The participation contract explicitly permits bonuses/campaigns and says bonus/points can be restricted to play or other platform services. This proves a subsidy channel exists institutionally, but not that a currently claimable bonus has cash-equivalent value sufficient for a guarantee.

Historical `Sürətli Şans` campaign (2025) awarded promotional-lottery entries for ordinary spend; bonus-funded play itself did not generate entries. This is an **extra random prize layer**, not an all-outcome rebate. Therefore it can increase EV but cannot by itself guarantee profit unless the base portfolio already has a nonnegative floor or the promotion gives deterministic redeemable value exceeding the deficit.

Current Azerlotereya campaign search on 2026-08-15 surfaced tournament-style spend/leaderboard campaigns but no public deterministic cashback/free-ticket offer large enough to establish a guaranteed-profit floor.

Sources:
- https://www.azerlotereya.com/ishtirak-muqavilesi
- https://www.azerlotereya.com/faq/suretli-sans
- https://www.azerlotereya.com/kampaniyalar/qol-yagisi
- https://www.azerlotereya.com/kampaniyalar/qizil-gunler

### C. Lottery courier second-chance / free-ticket offers
Lotto.com public promotion terms expose a useful archetype: new-customer second chance can grant non-withdrawable order credit when the first order is entirely non-winning, capped at the lesser of order price or $10; free-ticket promotions equal one base line and exclude add-ons.

This **does break simple one-period linearity** because the rebate is state-dependent. However it does **not create a cash-profit guarantee**:
- credit is non-payable/non-withdrawable;
- it is capped;
- it requires the first order to be entirely non-winning;
- after credit is replayed, the replacement ticket can also lose;
- a winning first order may still return less than acquisition cost and then does not qualify for the losing-order credit.

Thus there remains a positive-probability terminal branch with net loss. The promotion can improve EV/variance but is not terminal SUCCESS.

Source:
- https://az.lotto.com/promoterms

### D. Deposit-match promotions
Georgia Lottery's July 1–21 2026 online offer gave eligible never-deposit users a 50% bonus up to $125; both deposit and bonus funds were lottery-only and nonwithdrawable. This is a genuine acquisition subsidy, but it had expired before the current 2026-08-15 screen and did not itself make the funds cash. Even during validity, a strict profit guarantee would require a hedged/covered game portfolio whose minimum cash payout exceeds the user's actual cash deposit. No such paired construction is established here.

Source:
- https://www.galottery.com/en-us/player-zone/player-zone-promotions.html

### E. Promotional lotteries attached to economically useful purchases
Azerbaijan law separately regulates promotional lotteries. Current examples include bank/business or vehicle-purchase promotions where entries arise from underlying economic activity. If the underlying transaction would have been made anyway at identical economics, the lottery entry has near-zero marginal acquisition cost and therefore nonnegative expected incremental value. But **random promotional prizes are not guaranteed profit**; a no-prize outcome remains.

Examples screened:
- Kia Azerbaijan `Qızıl Açar`, 06.05.2026–29.08.2026: qualifying Kia purchase provides an entry to win another vehicle.
- ABB `Şanslı Fərdi Sahibkar`, 18.05.2026–18.08.2026: qualifying business actions create chances for prizes.

These are useful for the broader positive-EV/free-option catalog but fail the project's strict all-outcome guarantee criterion.

Sources:
- https://www.kia.com/content/kwcms/az/az/shopping-tools/kampaniyalar.html
- https://abb-bank.az/kampaniyalar/sansli-ferdi-sahibkar-lotereyasi-sans-sizin-olsun
- https://www.cbar.az/law-178/decision-no-1951100017?language=en

## Necessary-condition filters established

### Filter 1 — random extra layer is insufficient
If an overlay only adds a random prize and has a legal zero-overlay-prize outcome, then it cannot repair a base portfolio whose minimum net payoff is negative unless the base payoff in every zero-overlay branch is already nonnegative.

### Filter 2 — nonwithdrawable credit is not cash profit
A deterministic or conditional bonus denominated only in lottery play must be valued by the minimum cash payoff obtainable after required replay, not at face value. If replay can lose completely, its guaranteed cash value is zero absent a separate coverage construction.

### Filter 3 — finite cashback can only close a known deficit
For base portfolio cost C and minimum cash payout F, deterministic withdrawable cashback B creates a strict guarantee only if `F + B > C` after fees/tax. A capped cashback below `C-F` cannot create SUCCESS.

### Filter 4 — system tickets need real unit-cost nonlinearity
A system ticket representing N constituent base variants changes guarantee economics only if its price or payout differs from the exact sum of those N variants, or if it unlocks an additional prize layer. Convenience alone is irrelevant.

## Current conclusion
H005 is **not globally closed**, because live promotions and jurisdiction-specific system pricing change over time. But several major subclasses are now filtered cheaply:
- ordinary system packaging without discount: no edge;
- random second-chance/promotional entries: no standalone guarantee;
- nonwithdrawable free-play credit with losing replay branches: no standalone cash guarantee;
- expired deposit match: not executable now;
- free promotional entries attached to normal purchases: positive incremental EV possible, not guaranteed profit.

The highest-value continuation is H009: search **current, executable deterministic subsidies/cashback/free-play offers**, and for each calculate the maximum base-game guaranteed deficit that the subsidy could close. Only offers that survive the necessary-condition filters deserve portfolio optimization.
