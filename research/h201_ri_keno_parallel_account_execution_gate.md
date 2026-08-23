# H201 — RI Keno parallel-account execution gate

Updated: 2026-08-23
Status: **NO SUCCESS; SINGLE-ACCOUNT DEVICE PARALLELISM CLOSED**
Scope: LOTTERY ONLY.

## Target
Continue H200's Rhode Island Keno execution branch. Test whether H173/H175 same-draw bulk acquisition can be made execution-safe simply by parallelizing iLottery purchases across multiple devices or accounts.

## Fresh official evidence
Current Rhode Island Lottery FAQ states that a player may use the app on multiple devices, but **may not purchase iLottery games on more than one device at a time using a single VIP Club account**.

Current iLottery Terms additionally state:
- access/use of an iLottery account is strictly limited to its registered authorized user;
- credentials may not be shared;
- a player is prohibited from opening more than one iLottery account;
- each online purchaser must be registered/KYC-verified and physically located in Rhode Island;
- purchases remain subject to account/Lottery limits and may be delayed or refused in the Lottery's discretion.

The current official Group Play page supports pooling specifically for Powerball and Mega Millions; it does not establish a Keno group-purchase mechanism or atomic syndicate basket.

## Consequence for H173/H175
The simple execution shortcut

> one player / one account + many phones in parallel

is officially unavailable.

A multi-person Keno syndicate is not shown to be prohibited by the sources reviewed, but it is a materially different execution model: every participant would need a separate lawful account, KYC/geolocation, funding and successful acceptance of their assigned basket before the same Keno draw. Because each account can independently face purchase limits, delay/refusal, and because no official Keno syndicate/atomic group checkout is documented, partitioning the 4,336 or 4,560 selections across people does **not** convert H173/H175 into a strict guaranteed acquisition route.

This does not prove practical bulk execution impossible. It closes only the strongest same-account parallel-device shortcut and leaves a coordinated multi-account syndicate as an operational hypothesis rather than a guaranteed mechanism.

## New execution classification
- **Single account, serial web/app purchasing:** allowed in principle, capacity/atomicity unresolved.
- **Single account, simultaneous multiple devices:** **REJECTED by official FAQ**.
- **Multiple accounts controlled by one player:** **REJECTED by one-account-per-player / authorized-user terms**.
- **Multiple independent lawful players:** possible as a syndicate hypothesis, but **NOT GUARANTEED** because no Keno group-play/atomic acceptance mechanism is documented and per-account refusal/limit branches remain.

## Verdict
**ЕЩЁ НЕ УСПЕХ.** Current Rhode Island rules close single-player multi-device/account parallelism as the easy way to acquire the H173/H175 basket. A true multi-person Keno syndicate remains possible only operationally and still lacks guaranteed all-basket acceptance.

## Sources
- RI Lottery FAQ: https://www.rilot.com/en-us/player-zone/faqs.html
- RI Lottery iLottery Terms / Privacy Policy: https://www.rilot.com/en-us/about-us/privacy-policy.html
- RI Lottery Registration / iLottery account terms: https://www.rilot.com/en-us/registration.html
- RI Lottery Group Play: https://www.rilot.com/content/interactive/ilottery/en/group-play.html
- RI Lottery Rules 2026: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules2026.pdf
