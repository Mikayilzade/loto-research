# H283 execution verification — 2026-08-26

Branch: `research-work`
State: **ARITHMETIC VALID; EXECUTION GATE STILL OPEN**

## Scope

Follow-up on H283 Pennsylvania iLottery Refer-A-Friend + PICK 3 Front Pair cover. H225-X* was checked first and remains CLOSED / EXHAUSTED at X20; no H225-X21/X22 work is warranted.

## Fresh official evidence checked

1. PA iLottery Terms & Conditions currently define Draw products as products sold both at retailers and through the PA iLottery System, and state that a purchase can include a chosen number of Plays and chosen numbers/selections. Purchases are final once made. This is useful evidence that multi-play draw purchases are supported, but it does not publish the maximum PICK 3 online play count per transaction.
   - https://www.pailottery.com/p/terms-and-conditions/

2. PA iLottery currently advertises PICK games as available for online Draw Game purchase.
   - https://www.pailottery.com/promotions/welcome-to-ilottery/
   - https://www.pailottery.com/games/draw-games/

3. PA iLottery Help confirms that online limits can be game-specific: Powerball / Mega Millions are explicitly capped at five plays for up to 26 consecutive draws. This means absence of a published PICK 3 online cap cannot be assumed to imply an unlimited or 100-play transaction.
   - https://help.pailottery.com/hc/en-us/articles/8063697229972-Can-I-purchase-Powerball-and-Mega-Millions-tickets-online

4. Current 2026 retailer terminal documentation for PICK 3 states:
   - FRONT PAIR is a supported play type;
   - ticket cost may be $0.50-$5 per play;
   - maximum value of a single PICK 3 ticket is $100;
   - terminal UI supports ADD TO CART and BUY NOW;
   - a confirmation popup appears if a preset purchase limit is exceeded.
   These are strong compatibility signals for a $100 / 100-Pair cover at retail, but they do not prove the online PA iLottery transaction limit or atomicity.
   - https://www.palottery.pa.gov/PaLotteryWebSite/media/Retailer-Documents/QRG/WAVE-X_Terminal-Operations-Guide_2-2-2026.pdf
   - https://www.palottery.pa.gov/PaLotteryWebSite/media/Retailer-Documents/QRG/WAVE-8_Terminal-Operations-Guide_9-24-2024.pdf

5. Current Terms do not contain a broad clause saying the Lottery may selectively refuse any otherwise valid purchase at will. They do, however, require geolocation, account verification and sufficient funds, and permit account suspension/termination for unlawful, fraudulent or improper use. This is less restrictive than the execution blocker found in Kentucky/NH, but still does not establish all-or-none acquisition of 100 specific online Pair selections.

6. Current Bonus Policy still treats Bonus Money as restricted non-withdrawable funds usable for Plays and points to promotion-specific rules. H283's previously saved arithmetic remains unchanged: $100 complete Front Pair cover -> exactly one $50 cash win for every PICK 3 outcome. With the current referred-player $100 Bonus Money after a qualifying $10 first deposit, the conditional external-cash floor remains $50 gross / +$40 vs deposit if the full cover is accepted.
   - https://www.pailottery.com/p/bonus-policy/

## Execution conclusion

The new evidence materially strengthens H283:
- online PICK draw products are unquestionably supported;
- multi-play purchases and player-selected numbers are contemplated by the binding iLottery Terms;
- unlike Kentucky/NH, no checked PA iLottery Terms clause grants a general discretionary right to reject a valid purchase merely because of its selected numbers;
- retail PICK 3 explicitly permits a $100 single ticket.

But the rigorous SUCCESS gate is still not met. No public official source located in this pass establishes **all three** of:
1. the online PICK 3 transaction permits at least 100 distinct Front Pair plays for the same drawing;
2. all 100 selections can be committed atomically / all-or-none, rather than as separately accepted purchases;
3. no hidden online-specific line/cart/payout-liability cap can stop the set after only a strict subset has been acquired.

A partial cover has zero useful worst-case guarantee, so inference from retail limits is not sufficient for a rigorous claim.

## NEXT ACTION

Keep H283 open and focused. Highest-value evidence would be an official PA iLottery PICK 3 online purchase help page, UI/manual or customer-support statement explicitly confirming the per-transaction number of PICK 3 plays and whether one checkout containing 100 distinct Front Pair selections is accepted as one completed transaction. Do not declare SUCCESS until that execution fact is established.
