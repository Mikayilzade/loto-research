# H038 — deterministic rebate / lottery-credit guarantee screen

Updated: 2026-08-16
Status: **strict guarantee class substantially closed; free-credit overlays remain positive-EV/free-roll only unless a compact coverable product exists**

## Goal
Test whether cashback, free-ticket credit, lottery bonus funds, loyalty/replay value, or second-chance promotions can create a strictly positive **cash** floor across every legal outcome.

This packet focuses on deterministic subsidy rather than random promotional draws.

## Necessary-condition theorem
Let:
- `S` = cash spend required to qualify;
- `m` = minimum cash payout of the purchased portfolio across all outcomes;
- `R` = guaranteed **withdrawable cash** rebate;
- `C` = execution/transaction costs.

Worst-case net cash is:

`m + R - S - C`.

Therefore strict guaranteed profit requires:

`m + R > S + C`.

If the underlying portfolio has a legal zero-cash outcome (`m=0`), a true cash rebate must exceed **100% of qualifying spend plus costs** to create a strict standalone guarantee.

### Lottery credit / free play is not cash rebate
If the promotional value can only be spent on another lottery wager and that credited wager itself has a legal zero-cash outcome, the credit's strict cash floor is **0**, regardless of advertised face value.

Thus a 100%-face-value `buy one, get one free` lottery promotion can materially raise EV but does **not** by itself establish guaranteed positive cash profit.

Implementation:
- `src/loto_research/rebate_guarantee.py`
- `tests/test_rebate_guarantee.py`

## Current official OLG examples
### LOTTO MAX buy one, get one on us
Current official terms run **June 22, 2026–March 31, 2027** for selected eligible Ontario accounts.

Mechanics:
- purchase at least **CAD 6** of LOTTO MAX using cash/direct pay;
- receive a **CAD 6 LOTTO MAX Bonus**;
- bonus can only be used toward LOTTO MAX online purchases;
- promotion may be redeemed only once during the applicable promotion period;
- bonus is non-transferable.

OLG's Player Agreement separately defines Bonus Funds as notional value and explicitly excludes them from withdrawable `Unutilized Funds` when awarded. Bonus Funds are used to play eligible games; they are not cash at receipt.

Strict guarantee result:
- qualifying cash spend = CAD 6;
- direct-ticket minimum cash outcome = 0;
- bonus-ticket minimum cash outcome = 0;
- package worst-case cash result = **-CAD 6**.

Status: **REJECTED as strict cash guarantee**.

Primary official sources:
- https://www.olg.ca/en/promotions/lottery/retention/buy-a-lotto-max-get-lotto-max-lottery-bonus.html
- https://www.olg.ca/en/promotions/lottery/retention/buy-a-lotto-max-get-lotto-max-lottery-bonus.terms.html?bonusId=3612

### LOTTO 6/49 buy one, get one on us
Current official terms likewise run **June 22, 2026–March 31, 2027** for selected eligible accounts.

Mechanics:
- purchase at least **CAD 3** of LOTTO 6/49;
- receive **CAD 3 LOTTO 6/49 Bonus**;
- lottery-specific bonus, one redemption per promotion period.

Strict guarantee result:
- cash spend = CAD 3;
- both original and bonus play retain legal zero-cash outcomes;
- worst-case package cash result = **-CAD 3**.

Status: **REJECTED as strict cash guarantee**.

Primary official source:
- https://www.olg.ca/en/promotions/lottery/retention/buy-a-lotto-649-get-lotto-649-lottery-bonus.html

## Strongest zero-cost current subsidy found: OLG birthday bonus
OLG currently publishes a **CAD 10 Lottery Bonus Birthday Gift**, amended June 30, 2026 and stated for **July 1–December 31, 2026**.

Mechanics shown on the official page:
- no qualifying ticket purchase is stated;
- eligible player opts in during the offer window;
- CAD 10 is placed in the Lottery Bonus Balance;
- bonus can be used for lottery games available on OLG.ca.

This is economically better than buy-one-get-one because acquisition cash spend is **zero**. It is therefore a genuine **free-roll / positive-EV subsidy** for an eligible account.

However terminal SUCCESS still fails because strict positive profit requires a positive cash payout in every legal downstream outcome. Ordinary OLG games retain losing outcomes.

### Compact-coverage check
The obvious route would be to use the free CAD 10 to cover every outcome of a tiny game and force at least some withdrawable prize.

Current sampled OLG products do not fit:
- POKER LOTTO costs CAD 2/hand, is Quick Pick only, and overall odds of any prize are 1 in 3.66; five free hands can all legally lose.
- LIGHTNING LOTTO costs CAD 2/play, each play contains three 5-of-49 selections; CAD 10 buys only 15 selections, far below complete outcome coverage.
- MEGADICE LOTTO is Quick Pick and retains ordinary losing outcomes.

No ≤CAD10 fully coverable OLG lottery product with a strictly positive cash floor was found in this screen.

Status:
- **positive-EV/free-roll overlay: VALIDATED in principle for eligible birthday accounts**;
- **strict positive-profit guarantee: NOT ESTABLISHED**.

Official sources:
- https://www.olg.ca/en/promotions/10-lottery-bonus-birthday-gift.html
- https://www.olg.ca/en/lottery/play-poker-lotto/faqs.html
- https://www.olg.ca/en/lottery/play-lightning-lotto/about.app-content.html
- https://www.olg.ca/en/lottery/play-megadice-lotto/about.html

## Random second-chance promotions remain outside the deterministic guarantee class
California Lottery's 2026 SuperLotto Plus 2nd Chance Bonus Draw had five random CAD/USD-equivalent cash winners selected from entries. Such promotions can improve EV but preserve a no-promo-prize outcome for any individual entrant.

Status: **REJECTED as standalone strict guarantee mechanism**.

## Strategic conclusion
H038 closes a broad misconception:

**face-value subsidy is not cash-floor subsidy.**

For terminal guaranteed-profit research, future promotion scans should prioritize only:
1. genuinely withdrawable deterministic cash rebates;
2. zero-cost credits that can be converted through a fully coverable game with positive minimum cash payout;
3. deterministic discounts/rebates combined with an already positive portfolio floor.

Targeted free lottery credits remain worth tracking as positive-EV opportunities, but they are not `SUCCESS` unless conversion can be made strictly positive in every outcome.
