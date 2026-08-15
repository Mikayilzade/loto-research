# H009 — current deterministic subsidy / promotion screen

Updated: 2026-08-15
Status: **no currently verified executable guaranteed-profit subsidy found in screened official sources**

## Objective
Search live official lottery promotions for deterministic value that can break the negative payoff floor established by H012/H012a/H005. Priority is not ordinary positive EV: the terminal target requires a cash-profit floor above total out-of-pocket cost in every legal outcome.

Cheap filter from H005:

`guarantee possible only if F + B_cash_floor > C_all_in`

where `F` is the minimum guaranteed cash payout from the required wagering portfolio, `B_cash_floor` is deterministic withdrawable subsidy after fees/restrictions, and `C_all_in` is required out-of-pocket spend plus execution costs.

Random second chances, sweepstakes, draw entries and nonwithdrawable bonus credits are rejected early unless a separate coverage strategy removes their losing branch.

## 1. Azerbaijan — Azerlotereya current campaigns
Official current-campaign index:
- https://www.azerlotereya.com/kampaniyalar

At the 2026-08-15 checkpoint the indexed current-campaign page states **"Cari kampaniya mövcud deyil"** (no current campaign).

### 10 oyna, 10 qazan — important stale/inconsistent near-candidate
Official campaign page:
- https://www.azerlotereya.com/kampaniya/10oyna-10qazan

It advertises a 10-AZN welcome bonus for first-time registrants who deposit and play at least 10 AZN and verify the account. The page text says up to 31 August and first 10,000 qualified users.

However:
- the page is indexed/labeled as a **past campaign**;
- the official FAQ still states campaign dates **14 April–31 July 2026**;
- the current-campaign index says there is no current campaign.

Therefore it cannot be treated as an executable 2026-08-15 offer without direct operator confirmation. This conflict is itself a rule-versioning warning: never infer live eligibility from a stale campaign landing page.

Even under the favorable hypothetical that the offer were still live, the terminal guarantee is not established:
- qualifying requires at least 10 AZN of completed play before bonus credit;
- bonus is capped at 10 AZN;
- unused additional balance can be withdrawn only with a 30% commission according to the FAQ (the page also references minimum-withdrawal/commission conditions);
- qualification is restricted to first-time users / campaign capacity and the operator reserves campaign-control rights in FAQ text;
- no verified <=10-AZN wagering portfolio has a guaranteed cash floor large enough to turn the welcome bonus into a strict all-outcome positive net-profit theorem.

A pure worst-case cash comparison is already unfavorable if the initial 10 AZN can lose completely: a 10-AZN bonus withdrawn at 70% net yields 7 AZN, leaving a -3 AZN cash deficit before any other costs. The bonus can instead be wagered without turnover requirement, but that reintroduces losing outcomes and is not cash at face value for guarantee purposes.

Result: **not executable as current offer; not a proven guarantee even under favorable hypothetical continuity.**

## 2. Virginia Lottery — new-player bonus-games archetype
Official online-game page and terms:
- https://www.valottery.com/lotteryonline
- https://www.valottery.com/termsandconditions

The official site advertises a limited new-player first-deposit offer requiring at least a $10 deposit to receive bonus games. Virginia terms state:
- promotional offers generally have no cash value unless expressly stated;
- purchases use bonus funds before deposited funds;
- deposits and promotional value are not withdrawable; only prizes may be withdrawn;
- online purchase/deposit requires physical presence in Virginia.

Thus bonus games are **random free-play value, not deterministic withdrawable cashback**. A legal all-losing bonus-game branch remains.

Result: **REJECTED as standalone guaranteed-profit subsidy.** It may improve EV for an eligible Virginia player but cannot satisfy terminal guarantee without separate complete coverage.

## 3. Georgia Lottery — deposit-match control
Official promotions page:
- https://www.galottery.com/en-us/player-zone/player-zone-promotions.html

The official page preserves a July 2026 offer: 50% first-deposit bonus up to $125, qualifying deposit >=$10. It expired **2026-07-21**. Both deposited and bonus funds were lottery-only and nonwithdrawable.

Result: **not current; nonwithdrawable bonus class already rejected as a cash guarantee.**

## 4. New York Lottery — points / second-chance architecture
Official promotions / NYL+ pages:
- https://nylottery.ny.gov/promotions/
- https://nylottery.ny.gov/nylplus-eligible-games

NYL+ provides points / exclusive games / second-chance entries from eligible tickets. Current/preserved promotion architecture is overwhelmingly drawing/points based rather than deterministic cash rebate. A second-chance or points outcome has no positive cash floor unless redemption itself has guaranteed cash value above the underlying ticket deficit; no such verified current structure was found in this packet.

Result: **no deterministic cash-floor candidate found.**

## 5. Florida Lottery — current Bonus Play
Official current promotion portal:
- https://secondchance.flalottery.com/secondchance/login.do

Current portal lists Bonus Play promotions (e.g. Pick & Pop / Celebrate Summer). By construction these are extra promotional chances/drawings, so a no-prize branch remains.

Result: **REJECTED as standalone guarantee; retain only as EV overlay.**

## 6. Virginia rewards / Summer Sizzle control
Official 2026 Summer Sizzle page:
- https://www.valottery.com/rewards/promotions/summersizzle

Eligible scratchers generated entries into a drawing for 15 prize packages. Odds depend on total entries. Promotion ended 2026-08-02.

Result: expired and random-only; **no guarantee**.

## New operational rule — stale campaign conflict
A promotion is `EXECUTABLE-CURRENT` only if all three are consistent:
1. current official promotion index / current operator navigation;
2. specific promotion landing page / terms;
3. dates and eligibility in FAQ/rules.

If a landing page says future/current dates but official index labels it past or FAQ dates have expired, status is `STALE-CONFLICT`, not current. Direct operator confirmation would be required before economic use.

## Screen summary
| Operator / offer class | Current on 2026-08-15? | Deterministic withdrawable cash floor? | Terminal guarantee result |
|---|---:|---:|---|
| Azerlotereya current campaign index | no campaign listed | no | no candidate |
| Azerlotereya 10-play/10-bonus | stale/conflicting | at best bonus subject to withdrawal/game restrictions | not executable; no proof |
| Virginia new-player bonus games | limited offer shown | no, bonus games/promotional value | rejected standalone |
| Georgia 50% deposit match | expired 2026-07-21 | no | rejected/not current |
| New York NYL+ / promotions | current program | points/drawings, not verified cash floor | no candidate |
| Florida Bonus Play | current portal | random promotional chance | rejected standalone |
| Virginia Summer Sizzle | expired 2026-08-02 | random drawing | rejected |

## Strategic conclusion
The active-promotion search produced no current, verified deterministic subsidy that survives H005's all-outcome cash-floor filter.

This does **not** globally close H009 because promotions change frequently and can be jurisdiction/account-specific. It does close the screened current official-source set and adds a crucial stale-page verification rule.

Next highest-value work:
1. H005 genuine **nonlinear system-ticket pricing / deterministic prize floors** in current games;
2. H002 progressive jackpot threshold with sharing/tax/sales response, to identify structural states that might need only a small deterministic subsidy;
3. revisit H009 only when a new active offer appears or an official current index exposes deterministic cashback/discount rather than random bonus play.
