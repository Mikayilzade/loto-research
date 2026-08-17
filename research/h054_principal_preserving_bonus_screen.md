# H054 — principal-preserving deposit / funding bonus screen

Updated: 2026-08-17
Status: **mechanism class real; no strict terminal guarantee found in current screen**

## Question
Can a current deterministic signup/funding bonus be combined with a cash-like principal position so that the qualifying principal is preserved while a separate bonus creates a strictly positive all-outcome cash floor?

The attractive structure is:

`G = C_min + B_min - P - F`

where:
- `P` = qualifying principal deposited/funded;
- `C_min` = minimum contractually recoverable principal after every allowed branch;
- `B_min` = minimum vested, withdrawable reward after every allowed branch;
- `F` = all fees/tax/FX/funding/withdrawal costs.

A terminal SUCCESS needs `G > 0`, not merely positive expected value.

## 1. Azerbaijan bank scan — current principal-preserving products, but no separate guaranteed cash gift

### XalqKart balance yield
Current Xalq Bank campaign page (published 1 July 2026) offers XalqKart free of charge through 30 December and **7% annual return on AZN card balances from 300 to 20,000 AZN through 31 December 2026**.

Source:
- https://www.xalqbank.az/en/personal/campaigns/xalqkart-i-indi-pulsuz-elde-edin-en

This is genuinely principal-preserving in normal operation: the money remains a card-account balance rather than being consumed by a purchase. But reward accrues through time. The previously established H051 gate therefore applies: an immediate closure/insolvency/eligibility termination branch can leave newly accrued reward arbitrarily close to zero. It is not a separate vested upfront subsidy.

Status: **useful yield, not terminal guarantee**.

### Xalq Bank deposit lottery
Current `Əmanət` campaign runs 1 April–30 December 2026 and gives depositors chances for cash prizes, including two 50,000-AZN prizes.

Source:
- https://www.xalqbank.az/en/personal/campaigns/lotereya-en

Principal can be protected under qualifying deposit rules, but the promotional cash component is random. Its strict minimum is zero.

Status: **REJECTED as guaranteed bonus leg**.

### Current fee-discount business campaigns
AccessBank (through 1 September 2026) and Yelo Bank (extended through 30 September 2026) offer substantial deterministic fee discounts / free banking services to new business customers.

Sources:
- https://special.azertag.az/en/xeber/4298107
- https://www.yelo.az/en/news/yelo-bank-extends-welcome-to-business-campaign/

These reduce future transaction costs but do not create separately withdrawable positive cash with zero required consumption. They cannot satisfy `B_min > F` by themselves.

Status: **cost reduction only**.

## 2. Interactive Brokers current Refer-a-Friend — principal can remain cash, reward is separate, but vesting/market floor fails

Current IBKR terms dated 2 July 2026 state that an eligible referred client receives **$1 of IBKR stock for each $300 of net deposits**, up to $1,000 of shares. The explicit excluded-residency list includes mainland China, Spain, Portugal, Japan, Denmark, Israel and Poland; Azerbaijan is not listed as an automatic exclusion, although actual account eligibility remains subject to IBKR approval and local law.

Primary sources:
- https://ndcdyn.interactivebrokers.com/aces/Agreement/AgreementVersion/4841
- https://www.interactivebrokers.com/en/trading/referral-member-to-member.php

This is the closest current non-bank match to the target structure because the qualifying deposit may be cash and need not be spent on a wager or purchase.

However the reward fails the strict floor for multiple independent reasons:
1. During the award period, withdrawals reduce/reclaim the welcome-share balance proportionally.
2. Awarded shares **cannot be sold, transferred or hedged for one year from each award date**.
3. If the account closes or ceases to be in good standing before the anniversary date, unvested shares are forfeited.
4. The eventual cash value is exposed to IBKR share-price risk during the mandatory holding period; there is no contractual positive minimum redemption value.
5. IBKR may change/close the program for new participants and retains program-abuse/suspicious-activity discretion.

Therefore even if cash principal is preserved, `B_min` is not strictly positive in cash terms.

Status: **MECHANISM VERY CLOSE; strict guaranteed-profit path REJECTED**.

## 3. eToro current deposit promotions — real subsidy, principal-preservation/vesting gates fail

### Tiered deposit bonus
A current eToro landing page advertises free assets after qualifying deposits: $40 for $500–999, $100 for $1,000–4,999, $300 for $5,000–9,999, and $500 for $10,000+.

Source:
- https://go.etoro.com/en/deposit/tiered-bonus

The public landing page alone does not establish universal Azerbaijan eligibility, an irrevocable cash reward, or a cash-value floor for the awarded assets. Without promotion-specific binding terms proving all three, it cannot be promoted to terminal candidate.

### Crypto transfer promotion
The current July 1–August 31 2026 global campaign awards stocks worth **5% of monthly net crypto deposits**, capped at $2,000/month, with stock rewards locked from withdrawal for 90 days. Terms also allow eToro to cancel, terminate or suspend the promotion at its sole discretion without prior notice.

Source:
- https://cloud.connect.etoro.com/CryptoInSummerPromo2026Global

The qualifying principal is crypto rather than fixed cash and therefore has no fiat principal floor; withdrawals also reduce the net-deposit base. The reward itself is a locked market asset.

Status: **REJECTED strict guarantee**.

## 4. Trading 212 control
Trading 212's most recently indexed Invite-a-Friend campaign ran 8 June–9 July 2026, so it is **not current on 17 August 2026**. The campaign did provide a useful control structure: after funding, a random fractional share worth €8–€100 was awarded, could be sold immediately, and sale proceeds could be withdrawn only after a lock period.

Sources:
- https://helpcentre.trading212.com/hc/en-us/articles/360007291258-Invite-Your-Friends-Get-Free-Fractional-Shares
- https://helpcentre.trading212.com/hc/en-us/articles/35700500586653-How-can-I-check-when-the-lock-up-period-for-my-bonus-ends

Because the indexed campaign is expired, it is not an executable current candidate. Future campaigns should be checked because a **fixed minimum reward + tiny refundable deposit + explicit survival after funding withdrawal** would be structurally interesting.

## Class theorem from this screen
A principal-preserving promotion is still insufficient for strict guarantee unless the reward is both **vested** and **cash-floor protected**.

Four recurring failure modes now cover most funding bonuses:
1. **time vesting** — reward can be forfeited before vesting;
2. **withdrawal clawback** — preserving principal by withdrawing it destroys the reward;
3. **market reward** — shares/crypto have no fixed positive cash floor during lockup;
4. **operator discretion / eligibility** — reward can be denied under a permitted contractual branch.

Thus the target is narrower than “deposit bonus”:

> **Immediate or irrevocably vested cash credit, triggered by a principal-preserving action, with no proportional clawback on principal withdrawal and with bounded all-in costs below the credit.**

That is the exact H055 search target.

## Current conclusion
- Current principal-preserving promotional mechanisms exist.
- IBKR is a particularly strong structural near-miss because deposited principal may remain cash while a separate asset reward is granted.
- None of the screened current mechanisms establishes `B_min > 0` in withdrawable cash under every contractually allowed branch.
- **No terminal guaranteed-profit strategy found.**

## Next research
H055 should search specifically for **immediately vested cash account-opening / salary-switch / transfer / funding credits**, not generic cashback, points, lottery chances, fee discounts or market-valued free shares. Highest value candidates are regulated bank/broker offers where:
- the qualifying deposit remains cash/protected;
- reward amount is fixed, not `up to`/random;
- reward is credited before or immediately after funding;
- reward survives withdrawal of the qualifying principal or has only a short, fully deterministic hold;
- no investment/trading/spending requirement exists;
- eligibility is open to Azerbaijan or another clearly executable jurisdiction.
